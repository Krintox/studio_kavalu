"use client";

import Link from "next/link";
import { useCallback, useEffect, useId, useMemo, useRef, useState, type ReactNode } from "react";
import {
  BUDGET_UNSURE,
  budgets,
  emptyAnswers,
  heardFrom,
  isMonthly,
  needs,
  platforms,
  replyVia,
  roads,
  roadsPhrase,
  settings,
  shootLocations,
  skuCounts,
  socialModes,
  stages,
  steps,
  timelines,
  type Answers,
  type Currency,
  type RoadKey,
} from "@/content/onboarding";
import { site } from "@/content/site";
import type { ServiceKey } from "@/content/types";
import { Envelope } from "./Envelope";
import { Letter, letterParts } from "./Letter";
import styles from "./RoadForm.module.css";

const STORE = "kv-brief-v1";
const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
const URL_RE = /(https?:\/\/|www\.)/i;
const CAL = process.env.NEXT_PUBLIC_CAL_LINK || site.booking;
const WA = process.env.NEXT_PUBLIC_WHATSAPP_NUMBER || site.whatsapp;
const TURNSTILE_KEY = process.env.NEXT_PUBLIC_TURNSTILE_SITE_KEY || "";

type Errors = Partial<Record<keyof Answers, string>>;
type Result = { ref: string; delivered: string };

function guessCurrency(): Currency {
  try {
    const tz = Intl.DateTimeFormat().resolvedOptions().timeZone;
    if (tz === "Asia/Kolkata" || tz === "Asia/Calcutta" || /-IN$/i.test(navigator.language)) return "INR";
    return "USD";
  } catch {
    return "INR";
  }
}

function validate(step: number, a: Answers): Errors {
  const e: Errors = {};
  if (step === 0 && !a.roads.length) e.roads = "Choose at least one road, or pick “Not sure yet”.";
  if (step === 1 && !a.stage) e.stage = "Pick the closest one. You can explain more in a moment.";
  if (step === 2) {
    if (!a.brandName.trim()) e.brandName = "Tell us the brand’s name, even a working title.";
    else if (URL_RE.test(a.brandName)) e.brandName = "Just the name here; the link goes in the next box.";
    if (a.brief.trim().length < 10) e.brief = "A line or two is enough. What would you like to change?";
  }
  if (step === 3) {
    if (!a.timeline) e.timeline = "Pick the closest timing.";
    if (!a.budget) e.budget = "Choose the closest range, or “Not sure yet”.";
  }
  if (step === 4) {
    if (!a.name.trim()) e.name = "Tell us what to call you.";
    if (!EMAIL_RE.test(a.email.trim())) e.email = "That email looks incomplete. Check the @ and the part after it.";
  }
  return e;
}

/* ---------- small building blocks ---------- */

function Chips({
  legend,
  help,
  name,
  type,
  options,
  value,
  onChange,
  error,
  big,
}: {
  legend: string;
  help?: string;
  name: string;
  type: "radio" | "checkbox";
  options: { value: string; label: string; help?: string }[];
  value: string | string[];
  onChange: (v: string, checked: boolean) => void;
  error?: string;
  big?: boolean;
}) {
  const id = useId();
  const selected = (v: string) => (Array.isArray(value) ? value.includes(v) : value === v);
  return (
    <fieldset className={styles.group} aria-describedby={[help && `${id}-h`, error && `${id}-e`].filter(Boolean).join(" ") || undefined}>
      <legend className={styles.legend}>{legend}</legend>
      {help ? (
        <p id={`${id}-h`} className={styles.help}>
          {help}
        </p>
      ) : null}
      <div className={big ? styles.roadChips : styles.chips}>
        {options.map((o) => (
          <label key={o.value} className={big ? styles.roadChip : styles.chip}>
            <input
              type={type}
              name={name}
              value={o.value}
              checked={selected(o.value)}
              onChange={(e) => onChange(o.value, e.target.checked)}
            />
            <span>
              <b>{o.label}</b>
              {o.help ? <small>{o.help}</small> : null}
            </span>
          </label>
        ))}
      </div>
      {error ? (
        <p id={`${id}-e`} className={styles.error} role="alert">
          {error}
        </p>
      ) : null}
    </fieldset>
  );
}

function Field({
  label,
  help,
  error,
  children,
  optional,
}: {
  label: string;
  help?: string;
  error?: string;
  optional?: boolean;
  children: (props: { id: string; "aria-describedby"?: string; "aria-invalid"?: boolean }) => ReactNode;
}) {
  const id = useId();
  const described = [help && `${id}-h`, error && `${id}-e`].filter(Boolean).join(" ") || undefined;
  return (
    <div className={styles.field}>
      <label htmlFor={id} className={styles.label}>
        {label}
        {optional ? <span className={styles.optional}> (optional)</span> : null}
      </label>
      {help ? (
        <p id={`${id}-h`} className={styles.help}>
          {help}
        </p>
      ) : null}
      {children({ id, "aria-describedby": described, "aria-invalid": error ? true : undefined })}
      {error ? (
        <p id={`${id}-e`} className={styles.error} role="alert">
          {error}
        </p>
      ) : null}
    </div>
  );
}

function Progress({ step, onJump }: { step: number; onJump: (s: number) => void }) {
  return (
    <nav className={styles.progress} aria-label="Steps">
      <span className={styles.progressLine} aria-hidden="true">
        <span style={{ transform: `scaleX(${Math.min(step, 4) / 4})` }} />
      </span>
      <ol>
        {steps.map((s, k) => (
          <li key={s.key} data-state={k < step ? "done" : k === step ? "now" : "next"}>
            {k < step ? (
              <button type="button" onClick={() => onJump(k)} aria-label={`Back to step ${k + 1}: ${s.label}`}>
                <i aria-hidden="true" />
                <span>{s.label}</span>
              </button>
            ) : (
              <span aria-current={k === step ? "step" : undefined}>
                <i aria-hidden="true" />
                <span>{s.label}</span>
              </span>
            )}
          </li>
        ))}
      </ol>
    </nav>
  );
}

/* ---------- the form ---------- */

export function RoadForm({
  layout,
  initialRoads = [],
  initialStep = 0,
  from = "",
  onDone,
}: {
  layout: "page" | "drawer";
  initialRoads?: RoadKey[];
  initialStep?: number;
  from?: string;
  onDone?: () => void;
}) {
  const [a, setA] = useState<Answers>(() => ({ ...emptyAnswers(undefined), roads: initialRoads, ref: from }));
  const [step, setStep] = useState(initialStep);
  const [errors, setErrors] = useState<Errors>({});
  const [sending, setSending] = useState(false);
  const [failed, setFailed] = useState<"" | "failed" | "not-configured">("");
  const [result, setResult] = useState<Result | null>(null);
  const [copied, setCopied] = useState(false);
  const token = useRef("");
  const turnstile = useRef("");
  const heading = useRef<HTMLHeadingElement>(null);
  const tsBox = useRef<HTMLDivElement>(null);
  const firstRender = useRef(true);

  // Restore a half-written brief from this tab, then guess the currency.
  useEffect(() => {
    try {
      const saved = sessionStorage.getItem(STORE);
      if (saved) {
        const prev = JSON.parse(saved) as Partial<Answers>;
        setA((cur) => ({ ...cur, ...prev, roads: initialRoads.length ? initialRoads : (prev.roads ?? []), ref: from || prev.ref || "" }));
        return;
      }
    } catch {
      /* storage unavailable: start fresh */
    }
    setA((cur) => ({ ...cur, currency: guessCurrency() }));
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  useEffect(() => {
    const id = window.setTimeout(() => {
      try {
        if (!result) sessionStorage.setItem(STORE, JSON.stringify({ ...a, website: "" }));
      } catch {
        /* ignore */
      }
    }, 300);
    return () => window.clearTimeout(id);
  }, [a, result]);

  // A signed start time, so instant bot submissions can be told apart from people.
  useEffect(() => {
    fetch("/api/brief", { method: "GET", cache: "no-store" })
      .then((r) => r.json())
      .then((d: { token?: string }) => {
        token.current = d.token ?? "";
      })
      .catch(() => {});
  }, []);

  // Move focus to the new step's heading so keyboard and screen-reader users land in the right place.
  useEffect(() => {
    if (firstRender.current) {
      firstRender.current = false;
      return;
    }
    heading.current?.focus();
  }, [step]);

  // Invisible Turnstile on the last step, only when a site key is configured.
  useEffect(() => {
    if (step !== 4 || !TURNSTILE_KEY || !tsBox.current) return;
    const w = window as unknown as { turnstile?: { render: (el: HTMLElement, o: object) => string } };
    const mount = () =>
      w.turnstile?.render(tsBox.current!, {
        sitekey: TURNSTILE_KEY,
        appearance: "interaction-only",
        callback: (t: string) => (turnstile.current = t),
      });
    if (w.turnstile) return void mount();
    const s = document.createElement("script");
    s.src = "https://challenges.cloudflare.com/turnstile/v0/api.js?render=explicit";
    s.async = true;
    s.onload = mount;
    document.head.appendChild(s);
  }, [step]);

  const set = useCallback(<K extends keyof Answers>(k: K, v: Answers[K]) => {
    setA((cur) => ({ ...cur, [k]: v }));
    setErrors((cur) => (cur[k] ? { ...cur, [k]: undefined } : cur));
  }, []);

  const toggleRoad = (v: string, checked: boolean) => {
    const key = v as RoadKey;
    setA((cur) => {
      let next: RoadKey[];
      if (key === "unsure") next = checked ? ["unsure"] : [];
      else next = checked ? [...cur.roads.filter((r) => r !== "unsure"), key] : cur.roads.filter((r) => r !== key);
      return { ...cur, roads: next };
    });
    setErrors((cur) => ({ ...cur, roads: undefined }));
  };

  const toggleIn = (list: string[], v: string, checked: boolean) => (checked ? [...list, v] : list.filter((x) => x !== v));

  const blur = (k: keyof Answers) => {
    const e = validate(step, a);
    setErrors((cur) => ({ ...cur, [k]: e[k] }));
  };

  const next = () => {
    const e = validate(step, a);
    setErrors(e);
    if (Object.values(e).some(Boolean)) return;
    setStep((s) => Math.min(s + 1, 4));
  };

  const back = () => setStep((s) => Math.max(s - 1, 0));

  const monthly = isMonthly(a);
  const ranges = [...budgets[monthly ? "monthly" : "project"][a.currency], BUDGET_UNSURE];
  const chosen = a.roads.filter((r): r is ServiceKey => r !== "unsure");

  const plainLetter = useMemo(() => {
    const p = letterParts(a);
    return [
      "Dear Ananya,",
      `We're ${a.brandName || "…"}, ${p.stage ?? "…"}. We'd love your help with ${p.roads || "…"}.`,
      `We're hoping to start ${p.timeline ?? "…"}${a.deadline ? `, ahead of ${a.deadline}` : ""}, with a budget ${p.budget || "…"}.`,
      `The short version: ${a.brief || "…"}`,
      `Write to me at ${a.email || "…"}${a.phone ? `, or on WhatsApp at ${a.phone}` : ""}.`,
      `Warmly, ${a.name || "…"}`,
    ].join("\n\n");
  }, [a]);

  const submit = async () => {
    const e = validate(4, a);
    setErrors(e);
    if (Object.values(e).some(Boolean) || sending) return;
    setSending(true);
    setFailed("");
    try {
      const res = await fetch("/api/brief", {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify({ answers: a, startToken: token.current, turnstile: turnstile.current }),
      });
      const data = (await res.json().catch(() => ({}))) as { ok?: boolean; ref?: string; delivered?: string; reason?: string };
      if (res.ok && data.ok && data.ref) {
        setResult({ ref: data.ref, delivered: data.delivered ?? "" });
        setStep(5);
        try {
          sessionStorage.removeItem(STORE);
        } catch {
          /* ignore */
        }
      } else {
        setFailed(data.reason === "not-configured" ? "not-configured" : "failed");
      }
    } catch {
      setFailed("failed");
    } finally {
      setSending(false);
    }
  };

  const copyAnswers = async () => {
    try {
      await navigator.clipboard.writeText(plainLetter);
      setCopied(true);
      window.setTimeout(() => setCopied(false), 1800);
    } catch {
      /* clipboard blocked: the email link still works */
    }
  };

  const mailto = `mailto:${site.email}?subject=${encodeURIComponent(`New brief · ${a.brandName || "a new brand"}`)}&body=${encodeURIComponent(plainLetter)}`;

  /* ---------- sent ---------- */
  if (step === 5 && result) {
    const first = a.name.trim().split(/\s+/)[0] || "there";
    const low = a.budget === ranges[0];
    const asap = a.timeline === "asap";
    const unsure = a.roads.length === 1 && a.roads[0] === "unsure";
    const calHref = CAL
      ? `${CAL.startsWith("http") ? CAL : `https://cal.com/${CAL}`}?${new URLSearchParams({
          name: a.name,
          email: a.email,
          notes: `Ref ${result.ref} · ${roadsPhrase(a.roads)}`,
        })}`
      : "";
    const waHref = WA
      ? `https://wa.me/${WA.replace(/\D/g, "")}?text=${encodeURIComponent(`Hi Ananya, this is ${first} from ${a.brandName}. My reference is ${result.ref}.`)}`
      : "";
    return (
      <div className={`${styles.sent} ${layout === "page" ? styles.sentPage : ""}`}>
        <Envelope reference={result.ref} />
        <h2 className={styles.sentTitle} tabIndex={-1} ref={heading}>
          Thank you, {first}. Your letter is with Ananya.
        </h2>
        <p className={styles.sentLede}>
          {result.delivered === "local"
            ? `Saved on this computer for testing (no email service is connected yet). Your reference is ${result.ref}.`
            : `A copy is on its way to ${a.email}. Your reference is ${result.ref}.`}
        </p>
        {low ? (
          <p className={styles.note}>
            Thank you for being upfront about budget.
            {settings.identityFrom ? ` Full identity projects usually start at ${settings.identityFrom}.` : ""} If that is a
            stretch right now, a brand audit can be a strong first step, and if we are not the right fit, we will happily point
            you to people who are.
          </p>
        ) : null}
        {asap ? <p className={styles.note}>Tight timeline noted. We will check the calendar today and tell you honestly whether we can do it well.</p> : null}
        {unsure ? <p className={styles.note}>We will suggest a road on the call. Bring whatever you have: decks, photos, half-formed ideas.</p> : null}

        <h3 className={styles.nextTitle}>What happens next</h3>
        <ol className={styles.nextSteps}>
          <li>
            <span>
              <b>Today.</b> Ananya reads your brief herself.
            </span>
          </li>
          <li>
            <span>
              <b>{settings.replyPromise[0].toUpperCase() + settings.replyPromise.slice(1)}.</b> A personal reply with first
              thoughts and a question or two.
            </span>
          </li>
          <li>
            <span>
              <b>A 20-minute intro call.</b> To understand the crossroads you are at.
            </span>
          </li>
          <li>
            <span>
              <b>Within {settings.proposalDays} working days of the call.</b> A proposal with scope, timeline and fee.
            </span>
          </li>
          <li>
            <span>
              <b>Kick-off.</b> Sign, pay the {settings.advance}% advance, and we begin on the agreed date.
            </span>
          </li>
        </ol>
        <div className={styles.sentActions}>
          {calHref ? (
            <a className={styles.primary} href={calHref} target="_blank" rel="noreferrer">
              Pick a time for the intro call →
            </a>
          ) : null}
          {waHref ? (
            <a className={styles.secondary} href={waHref} target="_blank" rel="noreferrer">
              Message us on WhatsApp
            </a>
          ) : null}
          <Link className={styles.secondary} href="/work/nivritti" onClick={onDone}>
            While you wait: how we shaped Nivritti
          </Link>
        </div>
      </div>
    );
  }

  /* ---------- the five steps ---------- */
  const letterAside =
    layout === "page" ? (
      <aside className={styles.aside} aria-label="Your letter so far">
        <p className={styles.asideLabel}>Your letter so far</p>
        <Letter a={a} />
      </aside>
    ) : step < 4 ? (
      <details className={styles.strip}>
        <summary>Your letter so far</summary>
        <Letter a={a} compact />
      </details>
    ) : null;

  return (
    <div className={`${styles.form} ${layout === "page" ? styles.formPage : styles.formDrawer}`}>
      <div className={styles.main}>
        <Progress step={step} onJump={setStep} />

        <form
          className={styles.steps}
          noValidate
          onSubmit={(e) => {
            e.preventDefault();
            if (step < 4) next();
            else submit();
          }}
        >
          {step === 0 ? (
            <div className={styles.step}>
              <p className={styles.kicker}>
                <span lang="kn" className="kn">
                  {site.word}
                </span>{" "}
                Start a project
              </p>
              <h2 className={styles.stepTitle} tabIndex={-1} ref={heading}>
                Choose your <em>road.</em>
              </h2>
              <p className={styles.intro}>
                A brand is a set of choices: what it says, how it looks, where it shows up, who it speaks to. Tell us where
                you&apos;re standing, and we&apos;ll make the next ones with you.
              </p>
              <p className={styles.small}>Five short steps · about three minutes · read by Ananya, personally</p>
              {settings.bookingFrom ? <p className={styles.small}>Now booking projects from {settings.bookingFrom}.</p> : null}
              <Chips
                legend="Which road are you on?"
                help="Choose as many as you like. Unsure is a fine place to start."
                name="roads"
                type="checkbox"
                big
                options={roads.map((r) => ({ value: r.key, label: r.title, help: r.help }))}
                value={a.roads}
                onChange={toggleRoad}
                error={errors.roads}
              />
            </div>
          ) : null}

          {step === 1 ? (
            <div className={styles.step}>
              <h2 className={styles.stepTitle} tabIndex={-1} ref={heading}>
                A little more about <em>that road.</em>
              </h2>
              <p className={styles.intro}>Tap what fits. Skip what doesn&apos;t.</p>
              <Chips
                legend="Where’s the brand today?"
                name="stage"
                type="radio"
                options={stages.map((s) => ({ value: s.key, label: s.label }))}
                value={a.stage}
                onChange={(v) => set("stage", v)}
                error={errors.stage}
              />
              {chosen.includes("branding") ? (
                <Chips
                  legend="Branding: what do you need?"
                  name="needs-branding"
                  type="checkbox"
                  options={needs.branding.map((n) => ({ value: n, label: n }))}
                  value={a.needs.branding ?? []}
                  onChange={(v, c) => set("needs", { ...a.needs, branding: toggleIn(a.needs.branding ?? [], v, c) })}
                />
              ) : null}
              {chosen.includes("identity") ? (
                <>
                  <Chips
                    legend="Visual identity: what do you need?"
                    name="needs-identity"
                    type="checkbox"
                    options={needs.identity.map((n) => ({ value: n, label: n }))}
                    value={a.needs.identity ?? []}
                    onChange={(v, c) => set("needs", { ...a.needs, identity: toggleIn(a.needs.identity ?? [], v, c) })}
                  />
                  {(a.needs.identity ?? []).includes("Packaging") ? (
                    <Chips
                      legend="How many products?"
                      name="sku"
                      type="radio"
                      options={skuCounts.map((n) => ({ value: n, label: n }))}
                      value={a.skuCount}
                      onChange={(v) => set("skuCount", v)}
                    />
                  ) : null}
                </>
              ) : null}
              {chosen.includes("social") ? (
                <>
                  <Chips
                    legend="Social media: what do you need?"
                    name="needs-social"
                    type="checkbox"
                    options={needs.social.map((n) => ({ value: n, label: n }))}
                    value={a.needs.social ?? []}
                    onChange={(v, c) => set("needs", { ...a.needs, social: toggleIn(a.needs.social ?? [], v, c) })}
                  />
                  <Chips
                    legend="Which platforms?"
                    name="platforms"
                    type="checkbox"
                    options={platforms.map((n) => ({ value: n, label: n }))}
                    value={a.platforms}
                    onChange={(v, c) => set("platforms", toggleIn(a.platforms, v, c))}
                  />
                  <Chips
                    legend="One-off or ongoing?"
                    name="social-mode"
                    type="radio"
                    options={socialModes.map((m) => ({ value: m.key, label: m.label }))}
                    value={a.socialMode}
                    onChange={(v) => set("socialMode", v)}
                  />
                </>
              ) : null}
              {chosen.includes("film") ? (
                <>
                  <Chips
                    legend="Film & photography: what do you need?"
                    name="needs-film"
                    type="checkbox"
                    options={needs.film.map((n) => ({ value: n, label: n }))}
                    value={a.needs.film ?? []}
                    onChange={(v, c) => set("needs", { ...a.needs, film: toggleIn(a.needs.film ?? [], v, c) })}
                  />
                  <Chips
                    legend="Where would we shoot?"
                    name="shoot"
                    type="radio"
                    options={shootLocations.map((n) => ({ value: n, label: n }))}
                    value={a.shootLocation}
                    onChange={(v) => set("shootLocation", v)}
                  />
                </>
              ) : null}
              {!chosen.length ? <p className={styles.note}>No problem. We&apos;ll suggest a road on the call.</p> : null}
            </div>
          ) : null}

          {step === 2 ? (
            <div className={styles.step}>
              <h2 className={styles.stepTitle} tabIndex={-1} ref={heading}>
                Now, <em>the brand.</em>
              </h2>
              <Field label="Brand or business name" help="A working title is fine." error={errors.brandName}>
                {(p) => (
                  <input
                    {...p}
                    className={styles.input}
                    autoComplete="organization"
                    maxLength={80}
                    value={a.brandName}
                    onChange={(e) => set("brandName", e.target.value)}
                    onBlur={() => blur("brandName")}
                  />
                )}
              </Field>
              <Field label="Where can we see it?" help="Website or Instagram handle. Skip it if it isn’t live yet." optional>
                {(p) => (
                  <input
                    {...p}
                    className={styles.input}
                    inputMode="url"
                    maxLength={200}
                    value={a.brandLink}
                    onChange={(e) => set("brandLink", e.target.value)}
                  />
                )}
              </Field>
              <Field
                label="What’s the brief?"
                help="A few lines is plenty: what you make, who it’s for, and what needs to change."
                error={errors.brief}
              >
                {(p) => (
                  <textarea
                    {...p}
                    className={`${styles.input} ${styles.textarea}`}
                    rows={4}
                    maxLength={3000}
                    value={a.brief}
                    onChange={(e) => set("brief", e.target.value)}
                    onBlur={() => blur("brief")}
                  />
                )}
              </Field>
              <Field
                label="Anything you love, or don’t?"
                help="Pinterest boards, brands you admire, a Drive folder. One link per line."
                optional
              >
                {(p) => (
                  <textarea
                    {...p}
                    className={`${styles.input} ${styles.textarea}`}
                    rows={2}
                    maxLength={2000}
                    value={a.references}
                    onChange={(e) => set("references", e.target.value)}
                  />
                )}
              </Field>
              <p className={styles.small}>Got files? Reply to our email with them, or share a Drive link above.</p>
            </div>
          ) : null}

          {step === 3 ? (
            <div className={styles.step}>
              <h2 className={styles.stepTitle} tabIndex={-1} ref={heading}>
                Timing <em>and budget.</em>
              </h2>
              <Chips
                legend="When would you like to start?"
                name="timeline"
                type="radio"
                options={timelines.map((t) => ({ value: t.key, label: t.label }))}
                value={a.timeline}
                onChange={(v) => set("timeline", v)}
                error={errors.timeline}
              />
              <Field label="Is there a date we’re working towards?" help="A launch, an event, a festive season." optional>
                {(p) => (
                  <input
                    {...p}
                    className={styles.input}
                    maxLength={60}
                    value={a.deadline}
                    onChange={(e) => set("deadline", e.target.value)}
                  />
                )}
              </Field>
              <div className={styles.currency} role="group" aria-label="Currency">
                {(["INR", "USD"] as Currency[]).map((c) => (
                  <button
                    key={c}
                    type="button"
                    aria-pressed={a.currency === c}
                    onClick={() => setA((cur) => ({ ...cur, currency: c, budget: cur.budget === BUDGET_UNSURE ? cur.budget : "" }))}
                  >
                    {c === "INR" ? "₹ INR" : "$ USD"}
                  </button>
                ))}
              </div>
              <Chips
                legend={monthly ? "What monthly budget are you working with?" : "What budget are you working with?"}
                help="A ballpark helps us shape a proposal that fits. It never changes how carefully we read your brief."
                name="budget"
                type="radio"
                options={ranges.map((r) => ({ value: r, label: r }))}
                value={a.budget}
                onChange={(v) => set("budget", v)}
                error={errors.budget}
              />
              {settings.identityFrom || settings.socialFrom ? (
                <p className={styles.small}>
                  For reference:
                  {settings.identityFrom ? ` identity projects usually start at ${settings.identityFrom}` : ""}
                  {settings.identityFrom && settings.socialFrom ? ", and" : ""}
                  {settings.socialFrom ? ` social media partnerships at ${settings.socialFrom} a month` : ""}.
                </p>
              ) : null}
            </div>
          ) : null}

          {step === 4 ? (
            <div className={styles.step}>
              <h2 className={styles.stepTitle} tabIndex={-1} ref={heading}>
                Where should we <em>reply?</em>
              </h2>
              <div className={styles.pair}>
                <Field label="Your name" error={errors.name}>
                  {(p) => (
                    <input
                      {...p}
                      className={styles.input}
                      autoComplete="name"
                      maxLength={60}
                      value={a.name}
                      onChange={(e) => set("name", e.target.value)}
                      onBlur={() => blur("name")}
                    />
                  )}
                </Field>
                <Field label="Email" error={errors.email}>
                  {(p) => (
                    <input
                      {...p}
                      type="email"
                      className={styles.input}
                      autoComplete="email"
                      inputMode="email"
                      maxLength={120}
                      value={a.email}
                      onChange={(e) => set("email", e.target.value)}
                      onBlur={() => blur("email")}
                    />
                  )}
                </Field>
              </div>
              <Field label="Phone or WhatsApp" optional>
                {(p) => (
                  <input
                    {...p}
                    type="tel"
                    className={styles.input}
                    autoComplete="tel"
                    placeholder="+91"
                    maxLength={20}
                    value={a.phone}
                    onChange={(e) => set("phone", e.target.value)}
                  />
                )}
              </Field>
              <Chips
                legend="Best way to reach you?"
                name="reply"
                type="radio"
                options={replyVia.map((r) => ({ value: r, label: r }))}
                value={a.replyVia}
                onChange={(v) => set("replyVia", v)}
              />
              <Field label="How did you find us?" optional>
                {(p) => (
                  <select {...p} className={styles.input} value={a.heardFrom} onChange={(e) => set("heardFrom", e.target.value)}>
                    <option value="">Choose one</option>
                    {heardFrom.map((h) => (
                      <option key={h} value={h}>
                        {h}
                      </option>
                    ))}
                  </select>
                )}
              </Field>
              {/* decoy for bots: hidden from people, keyboards and screen readers */}
              <div className={styles.decoy} aria-hidden="true">
                <label>
                  Leave this field empty
                  <input tabIndex={-1} autoComplete="off" value={a.website} onChange={(e) => set("website", e.target.value)} />
                </label>
              </div>
              <div className={styles.review}>
                <p className={styles.asideLabel}>Your letter</p>
                <Letter a={a} />
              </div>
              <div ref={tsBox} />
              <p className={styles.small}>We use these details only to reply to you about this project.</p>
              {failed ? (
                <div className={styles.failed} role="alert">
                  <p>
                    {failed === "not-configured"
                      ? "Our inbox isn’t connected yet, so the letter can’t be sent from here. Email it instead; it is already written."
                      : "That didn’t go through on our side. Your answers are saved. Try again, or email them to us."}
                  </p>
                  <div className={styles.failedActions}>
                    <a href={mailto}>Email the letter</a>
                    <button type="button" onClick={copyAnswers}>
                      {copied ? "Copied" : "Copy my answers"}
                    </button>
                  </div>
                </div>
              ) : null}
            </div>
          ) : null}

          <div className={styles.nav}>
            {step > 0 ? (
              <button type="button" className={styles.back} onClick={back}>
                ← Back
              </button>
            ) : (
              <span />
            )}
            {step < 4 ? (
              <button type="submit" className={styles.primary}>
                Continue <small>Next: {steps[step + 1].label.toLowerCase()}</small>
              </button>
            ) : (
              <button type="submit" className={styles.primary} disabled={sending} aria-busy={sending}>
                {sending ? "Sending…" : "Send the letter"}
              </button>
            )}
          </div>
        </form>

        {step === 0 ? (
          <div className={styles.talk}>
            <span>Rather talk first?</span>
            {CAL ? (
              <a href={CAL.startsWith("http") ? CAL : `https://cal.com/${CAL}`} target="_blank" rel="noreferrer">
                Book a 20-minute call
              </a>
            ) : null}
            {WA ? (
              <a href={`https://wa.me/${WA.replace(/\D/g, "")}`} target="_blank" rel="noreferrer">
                WhatsApp
              </a>
            ) : null}
            <a href={`mailto:${site.email}`}>{site.email}</a>
          </div>
        ) : null}
      </div>
      {letterAside}
    </div>
  );
}
