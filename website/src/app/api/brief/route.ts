import { appendFile, mkdir } from "node:fs/promises";
import path from "node:path";
import { clientEmail, cleanAnswers, newReference, secondsSinceStart, startToken, studioEmail } from "@/lib/brief";

/*
 * Receives a "Choose your road" brief.
 *
 * Environment (all optional; see website/README.md):
 *   RESEND_API_KEY, BRIEF_TO_EMAIL, BRIEF_FROM_EMAIL   send the brief + the client's copy via Resend
 *   SHEETS_WEBHOOK_URL, SHEETS_WEBHOOK_SECRET          also log each brief to a Google Sheet (Apps Script)
 *   FORM_SIGNING_SECRET                                sign the start time so bots can't fake it
 *   TURNSTILE_SECRET_KEY                               verify Cloudflare Turnstile when the site key is set
 *   NEXT_PUBLIC_CAL_LINK, NEXT_PUBLIC_WHATSAPP_NUMBER  links used in the client's email
 *
 * With nothing configured, development saves briefs to .data/briefs.jsonl; production says so honestly
 * (503 "not-configured") and the form offers to send the letter by email instead.
 */

const env = process.env;
const MIN_SECONDS = 4;

// Best-effort limit per address (per server instance): 5 briefs in 10 minutes.
const hits = new Map<string, number[]>();
function limited(ip: string) {
  const now = Date.now();
  if (hits.size > 2000) hits.clear(); // never let the map grow without bound
  const recent = (hits.get(ip) ?? []).filter((t) => now - t < 10 * 60_000);
  recent.push(now);
  hits.set(ip, recent);
  return recent.length > 5;
}

export async function GET() {
  return Response.json({ token: startToken(env.FORM_SIGNING_SECRET) }, { headers: { "cache-control": "no-store" } });
}

export async function POST(request: Request) {
  const ip = (request.headers.get("x-forwarded-for") ?? "").split(",")[0].trim() || "local";
  if (limited(ip)) return Response.json({ ok: false, reason: "too-many" }, { status: 429 });

  const body = (await request.json().catch(() => null)) as { answers?: unknown; startToken?: unknown; turnstile?: unknown } | null;
  if (!body) return Response.json({ ok: false, reason: "bad-request" }, { status: 400 });

  const { answers, errors } = cleanAnswers(body.answers);
  if (errors.length) return Response.json({ ok: false, reason: "invalid", fields: errors }, { status: 422 });

  // Spam checks flag rather than reject, so a real person who trips one still reaches the studio.
  const flags: string[] = [];
  if (answers.website) flags.push("decoy field filled");
  const secs = secondsSinceStart(body.startToken, env.FORM_SIGNING_SECRET);
  if (secs === null) flags.push("no valid start token");
  else if (secs < MIN_SECONDS) flags.push(`sent in ${secs.toFixed(1)}s`);
  if (env.TURNSTILE_SECRET_KEY) {
    const ok = await fetch("https://challenges.cloudflare.com/turnstile/v0/siteverify", {
      method: "POST",
      body: new URLSearchParams({ secret: env.TURNSTILE_SECRET_KEY, response: String(body.turnstile ?? ""), remoteip: ip }),
    })
      .then((r) => r.json() as Promise<{ success?: boolean }>)
      .then((d) => !!d.success)
      .catch(() => false);
    if (!ok) flags.push("turnstile failed");
  }

  const ref = newReference();
  const sentAt = new Date();
  const delivered: string[] = [];

  if (env.RESEND_API_KEY && env.BRIEF_TO_EMAIL && env.BRIEF_FROM_EMAIL) {
    const send = (payload: Record<string, unknown>) =>
      fetch("https://api.resend.com/emails", {
        method: "POST",
        headers: { authorization: `Bearer ${env.RESEND_API_KEY}`, "content-type": "application/json" },
        body: JSON.stringify(payload),
      });
    const studio = studioEmail(answers, ref, flags, sentAt);
    const res = await send({
      from: env.BRIEF_FROM_EMAIL,
      to: env.BRIEF_TO_EMAIL.split(",").map((s) => s.trim()),
      reply_to: answers.email,
      subject: studio.subject,
      html: studio.html,
      text: studio.text,
    }).catch(() => null);
    if (!res?.ok) return Response.json({ ok: false, reason: "send-failed" }, { status: 502 });
    delivered.push("email");

    if (!flags.length) {
      const cal = env.NEXT_PUBLIC_CAL_LINK;
      const wa = env.NEXT_PUBLIC_WHATSAPP_NUMBER;
      const copy = clientEmail(answers, ref, {
        booking: cal ? (cal.startsWith("http") ? cal : `https://cal.com/${cal}`) : undefined,
        whatsapp: wa ? `https://wa.me/${wa.replace(/\D/g, "")}?text=${encodeURIComponent(`Hi Ananya, my reference is ${ref}.`)}` : undefined,
      });
      await send({
        from: env.BRIEF_FROM_EMAIL,
        to: [answers.email],
        reply_to: env.BRIEF_TO_EMAIL.split(",")[0].trim(),
        subject: copy.subject,
        html: copy.html,
        text: copy.text,
      }).catch(() => null);
    }
  }

  if (env.SHEETS_WEBHOOK_URL) {
    const ok = await fetch(env.SHEETS_WEBHOOK_URL, {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify({ ...answers, cameFrom: answers.ref, secret: env.SHEETS_WEBHOOK_SECRET ?? "", reference: ref, sentAt: sentAt.toISOString(), flags }),
    })
      .then((r) => r.ok)
      .catch(() => false);
    if (ok) delivered.push("sheet");
  }

  if (!delivered.length) {
    if (env.NODE_ENV === "production") return Response.json({ ok: false, reason: "not-configured" }, { status: 503 });
    const dir = path.join(process.cwd(), ".data");
    await mkdir(dir, { recursive: true });
    await appendFile(path.join(dir, "briefs.jsonl"), JSON.stringify({ ref, sentAt, flags, answers }) + "\n", "utf8");
    console.log(`[brief] ${ref} from ${answers.name} <${answers.email}> saved to .data/briefs.jsonl${flags.length ? ` (flags: ${flags.join(", ")})` : ""}`);
    delivered.push("local");
  }

  return Response.json({ ok: true, ref, delivered: delivered.join("+") });
}
