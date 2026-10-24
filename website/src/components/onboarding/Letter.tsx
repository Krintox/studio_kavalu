import type { ReactNode } from "react";
import { BUDGET_UNSURE, roadsPhrase, stages, timelines, type Answers } from "@/content/onboarding";
import styles from "./RoadForm.module.css";

/** An answer slot in the letter: the answer if there is one, otherwise a soft blank. */
function Slot({ value, width = "6em" }: { value?: ReactNode; width?: string }) {
  if (value) return <strong className={styles.filled}>{value}</strong>;
  return <span className={styles.blank} style={{ width }} aria-hidden="true" />;
}

export function letterParts(a: Answers) {
  const stage = stages.find((s) => s.key === a.stage)?.phrase;
  const timeline = timelines.find((t) => t.key === a.timeline)?.phrase;
  const budget = a.budget ? (a.budget === BUDGET_UNSURE ? "that we'd like your advice on" : `around ${a.budget}`) : "";
  const roads = a.roads.length ? (a.roads.length === 1 && a.roads[0] === "unsure" ? "choosing the right road" : roadsPhrase(a.roads)) : "";
  const brief = a.brief.trim();
  const short = brief.length > 160 ? `${brief.slice(0, 160).trimEnd()}…` : brief;
  return { stage, timeline, budget, roads, short };
}

export function Letter({ a, compact }: { a: Answers; compact?: boolean }) {
  const p = letterParts(a);
  return (
    <div className={`${styles.letter} ${compact ? styles.letterCompact : ""}`}>
      {/* the date depends on the reader's clock and time zone, so the server copy may differ */}
      <p className={styles.letterDate} suppressHydrationWarning>
        {new Intl.DateTimeFormat("en-GB", { day: "numeric", month: "long", year: "numeric" }).format(new Date())}
      </p>
      <p className={styles.salute}>Dear Ananya,</p>
      <p>
        We&apos;re <Slot value={a.brandName} width="7em" />, <Slot value={p.stage} width="11em" />. We&apos;d love your
        help with <Slot value={p.roads} width="9em" />.
      </p>
      <p>
        We&apos;re hoping to start <Slot value={p.timeline} width="8em" />
        {a.deadline ? <>, ahead of {a.deadline}</> : null}, with a budget <Slot value={p.budget} width="7em" />.
      </p>
      <p>
        The short version: <Slot value={p.short ? <em>{p.short}</em> : ""} width="14em" />
      </p>
      <p>
        Write to me at <Slot value={a.email} width="9em" />
        {a.phone ? <>, or on WhatsApp at {a.phone}</> : null}.
      </p>
      <p className={styles.signoff}>
        Warmly,
        <br />
        <span className={styles.signName}>{a.name || <Slot width="5em" />}</span>
      </p>
    </div>
  );
}
