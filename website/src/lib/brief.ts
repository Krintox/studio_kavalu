import { createHmac, randomInt, timingSafeEqual } from "node:crypto";
import {
  BUDGET_UNSURE,
  budgets,
  heardFrom as heardOptions,
  needs as needOptions,
  platforms as platformOptions,
  replyVia as replyOptions,
  roads as roadOptions,
  roadsPhrase,
  shootLocations,
  skuCounts,
  socialModes,
  stages,
  timelines,
  type Answers,
  type RoadKey,
} from "@/content/onboarding";

const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
const URL_RE = /(https?:\/\/|www\.)/i;

const clip = (v: unknown, n: number) => (typeof v === "string" ? v.replace(/\u0000/g, "").trim().slice(0, n) : "");
const pick = (v: unknown, allowed: readonly string[]) => (typeof v === "string" && allowed.includes(v) ? v : "");
const pickMany = (v: unknown, allowed: readonly string[]) =>
  Array.isArray(v) ? [...new Set(v.filter((x): x is string => typeof x === "string" && allowed.includes(x)))] : [];

const allBudgets = [
  ...budgets.project.INR,
  ...budgets.project.USD,
  ...budgets.monthly.INR,
  ...budgets.monthly.USD,
  BUDGET_UNSURE,
];

/** Rebuild the answers from scratch, keeping only known values and bounded text. */
export function cleanAnswers(raw: unknown): { answers: Answers; errors: string[] } {
  const r = (raw && typeof raw === "object" ? raw : {}) as Record<string, unknown>;
  const rn = (r.needs && typeof r.needs === "object" ? r.needs : {}) as Record<string, unknown>;
  const answers: Answers = {
    roads: pickMany(r.roads, roadOptions.map((x) => x.key)) as RoadKey[],
    stage: pick(r.stage, stages.map((s) => s.key)),
    needs: {
      branding: pickMany(rn.branding, needOptions.branding),
      identity: pickMany(rn.identity, needOptions.identity),
      social: pickMany(rn.social, needOptions.social),
      film: pickMany(rn.film, needOptions.film),
    },
    skuCount: pick(r.skuCount, skuCounts),
    platforms: pickMany(r.platforms, platformOptions),
    socialMode: pick(r.socialMode, socialModes.map((m) => m.key)),
    shootLocation: pick(r.shootLocation, shootLocations),
    brandName: clip(r.brandName, 80),
    brandLink: clip(r.brandLink, 200),
    brief: clip(r.brief, 3000),
    references: clip(r.references, 2000),
    timeline: pick(r.timeline, timelines.map((t) => t.key)),
    deadline: clip(r.deadline, 60),
    currency: r.currency === "USD" ? "USD" : "INR",
    budget: pick(r.budget, allBudgets),
    name: clip(r.name, 60),
    email: clip(r.email, 120),
    phone: clip(r.phone, 20),
    replyVia: pick(r.replyVia, replyOptions) || "Email",
    heardFrom: pick(r.heardFrom, heardOptions),
    website: clip(r.website, 200),
    ref: clip(r.ref, 60),
  };
  const errors: string[] = [];
  if (!answers.roads.length) errors.push("roads");
  if (!answers.stage) errors.push("stage");
  if (!answers.brandName || URL_RE.test(answers.brandName)) errors.push("brandName");
  if (answers.brief.length < 10) errors.push("brief");
  if (!answers.timeline) errors.push("timeline");
  if (!answers.budget) errors.push("budget");
  if (!answers.name || URL_RE.test(answers.name)) errors.push("name");
  if (!EMAIL_RE.test(answers.email)) errors.push("email");
  return { answers, errors };
}

/* ---------- the signed start time ---------- */

const sign = (secret: string, value: string) => createHmac("sha256", secret).update(value).digest("base64url");

export function startToken(secret: string | undefined) {
  const t = String(Date.now());
  return secret ? `${t}.${sign(secret, t)}` : t;
}

/** Seconds since the form was opened, or null when the token is missing or forged. */
export function secondsSinceStart(token: unknown, secret: string | undefined): number | null {
  if (typeof token !== "string" || !token) return null;
  const [t, sig] = token.split(".");
  if (!/^\d{13}$/.test(t)) return null;
  if (secret) {
    if (!sig) return null;
    const a = Buffer.from(sign(secret, t));
    const b = Buffer.from(sig);
    if (a.length !== b.length || !timingSafeEqual(a, b)) return null;
  }
  return (Date.now() - Number(t)) / 1000;
}

/* ---------- reference numbers ---------- */

const ALPHABET = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"; // no 0/O or 1/I
export const newReference = () => `KAV-${Array.from({ length: 5 }, () => ALPHABET[randomInt(ALPHABET.length)]).join("")}`;

/* ---------- emails ---------- */

const esc = (s: string) => s.replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c]!);

const label = {
  stage: (k: string) => stages.find((s) => s.key === k)?.label ?? "",
  timeline: (k: string) => timelines.find((t) => t.key === k)?.label ?? "",
  social: (k: string) => socialModes.find((m) => m.key === k)?.label ?? "",
};

export function firstName(name: string) {
  const f = name.split(/\s+/)[0] ?? "";
  return /^[\p{L}'-]{1,30}$/u.test(f) ? f : "there";
}

export function studioEmail(a: Answers, ref: string, flags: string[], sentAt: Date) {
  const roads = roadsPhrase(a.roads);
  const subject = `${flags.length ? "[check] " : ""}New brief · ${a.brandName} · ${roads} · ${a.budget} · ${label.timeline(a.timeline)}`;
  const rows: [string, string][] = [
    ["Reference", ref],
    ["Name", a.name],
    ["Email", a.email],
    ["Phone / WhatsApp", a.phone],
    ["Best way to reach", a.replyVia],
    ["Brand", a.brandName],
    ["Where to see it", a.brandLink],
    ["Roads", roads],
    ["Stage", label.stage(a.stage)],
    ["Branding needs", (a.needs.branding ?? []).join(", ")],
    ["Identity needs", (a.needs.identity ?? []).join(", ")],
    ["Products", a.skuCount],
    ["Social needs", (a.needs.social ?? []).join(", ")],
    ["Platforms", a.platforms.join(", ")],
    ["Social: one-off or ongoing", label.social(a.socialMode)],
    ["Film needs", (a.needs.film ?? []).join(", ")],
    ["Shoot location", a.shootLocation + (a.shootLocation === "Outside India" ? "  (travel)" : "")],
    ["Start", label.timeline(a.timeline)],
    ["Working towards", a.deadline],
    ["Budget", `${a.budget} (${a.currency})`],
    ["Heard from", a.heardFrom],
    ["Came from", a.ref],
    ["Sent", new Intl.DateTimeFormat("en-IN", { dateStyle: "medium", timeStyle: "short", timeZone: "Asia/Kolkata" }).format(sentAt) + " IST"],
    ["Checks", flags.length ? flags.join(", ") : "passed"],
  ];
  const visible = rows.filter(([, v]) => v);
  const wa = a.phone ? `https://wa.me/${a.phone.replace(/\D/g, "")}` : "";
  const html = `<div style="font-family:Georgia,serif;color:#241319;max-width:640px">
<h2 style="font-weight:400;color:#390D26">New brief from ${esc(a.name)} · ${esc(a.brandName)}</h2>
<table style="border-collapse:collapse;width:100%;font-family:Arial,sans-serif;font-size:14px">${visible
    .map(
      ([k, v]) =>
        `<tr><td style="padding:6px 10px;border-bottom:1px solid #e3e0cd;color:#5d4a50;white-space:nowrap;vertical-align:top">${esc(k)}</td><td style="padding:6px 10px;border-bottom:1px solid #e3e0cd">${esc(v)}</td></tr>`,
    )
    .join("")}</table>
<h3 style="font-weight:400;color:#390D26;margin-top:24px">The brief</h3>
<p style="font-family:Arial,sans-serif;font-size:14px;line-height:1.6;white-space:pre-wrap">${esc(a.brief)}</p>
${a.references ? `<h3 style="font-weight:400;color:#390D26">References</h3><p style="font-family:Arial,sans-serif;font-size:14px;white-space:pre-wrap">${esc(a.references)}</p>` : ""}
${wa ? `<p><a href="${esc(wa)}" style="display:inline-block;padding:10px 16px;background:#390D26;color:#F3F3E7;border-radius:999px;text-decoration:none;font-family:Arial,sans-serif;font-size:14px">WhatsApp ${esc(firstName(a.name))}</a></p>` : ""}
</div>`;
  const text = visible.map(([k, v]) => `${k}: ${v}`).join("\n") + `\n\nThe brief:\n${a.brief}\n${a.references ? `\nReferences:\n${a.references}\n` : ""}`;
  return { subject, html, text };
}

/** The client's copy repeats only fixed labels and a cleaned first name, never anything they typed freely. */
export function clientEmail(a: Answers, ref: string, links: { booking?: string; whatsapp?: string; guide?: string }) {
  const name = firstName(a.name);
  const subject = `Your brief is with us, ${name}`;
  const glance = [roadsPhrase(a.roads), label.timeline(a.timeline), a.budget].filter(Boolean).join(" · ");
  const li = (s: string) => `<li style="margin:0 0 8px">${s}</li>`;
  const html = `<div style="font-family:Georgia,serif;color:#241319;max-width:560px;font-size:16px;line-height:1.6">
<p>Hi ${esc(name)},</p>
<p>Thank you for choosing your road with Studio Kavalu. Your brief has reached me, and I read every one myself.</p>
<p style="margin-bottom:6px"><strong>What happens next</strong></p>
<ol style="padding-left:20px;margin-top:0">
${li("I'll reply within one working day (Monday to Friday, IST) with first thoughts and any questions.")}
${links.booking ? li(`If you haven't booked yet, pick a time for a 20-minute intro call: <a href="${esc(links.booking)}" style="color:#390D26">Book a time</a>`) : ""}
${li("After we talk, you'll get a clear proposal, covering scope, timeline and fee.")}
</ol>
<p style="margin-bottom:6px"><strong>While you wait</strong></p>
<ul style="padding-left:20px;margin-top:0">
${li("Gather what you already have: logo files, decks, product photos, anything you love or can't stand.")}
${links.whatsapp ? li(`Prefer WhatsApp? <a href="${esc(links.whatsapp)}" style="color:#390D26">Message us</a> and mention <strong>${esc(ref)}</strong>.`) : ""}
</ul>
<p style="font-family:Arial,sans-serif;font-size:13px;color:#5d4a50">Your brief at a glance: ${esc(glance)} · Reference ${esc(ref)}</p>
<p>Speak soon,<br>Ananya<br><span style="font-family:Arial,sans-serif;font-size:13px;color:#5d4a50">Founder, Studio Kavalu</span></p>
<p style="font-style:italic;color:#390D26">A brand is a set of choices. We make them with you.</p>
<p style="font-family:Arial,sans-serif;font-size:11px;color:#8f7f83">You're receiving this because a brief was sent from studiokavalu.com with this address. If that wasn't you, please ignore this email.</p>
</div>`;
  const text = `Hi ${name},

Thank you for choosing your road with Studio Kavalu. Your brief has reached me, and I read every one myself.

What happens next
1. I'll reply within one working day (Monday to Friday, IST) with first thoughts and any questions.
${links.booking ? `2. If you haven't booked yet, pick a time for a 20-minute intro call: ${links.booking}\n3.` : "2."} After we talk, you'll get a clear proposal, covering scope, timeline and fee.

Your brief at a glance: ${glance} · Reference ${ref}

Speak soon,
Ananya
Founder, Studio Kavalu`;
  return { subject, html, text };
}
