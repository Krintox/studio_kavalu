"use client";

import { useRef } from "react";
import { process } from "@/content/site";
import { gsap, prefersReducedMotion, useGSAP } from "@/lib/gsap";
import { ground, sheet } from "@/lib/surfaces";
import styles from "./Studio.module.css";

/** Listen, Map, Make, Launch: four stops on one road that draws itself as you read down it. */
export function Process() {
  const root = useRef<HTMLElement>(null);

  useGSAP(
    () => {
      if (prefersReducedMotion()) return;
      const line = root.current!.querySelector<HTMLElement>("[data-line]")!;
      gsap.fromTo(line, { scaleY: 0 }, { scaleY: 1, ease: "none", scrollTrigger: { trigger: root.current, start: "top 70%", end: "bottom 60%", scrub: 0.5 } });
      gsap.utils.toArray<HTMLElement>("[data-stop]", root.current).forEach((el) => {
        gsap.from(el.querySelector("[data-dot]"), { scale: 0, duration: 0.5, ease: "back.out(2)", scrollTrigger: { trigger: el, start: "top 72%" } });
        gsap.from(el.querySelector("[data-step-title]"), { x: -24, opacity: 0, duration: 0.8, scrollTrigger: { trigger: el, start: "top 72%" } });
      });
    },
    { scope: root },
  );

  return (
    <section ref={root} className={styles.process} {...ground("process")} aria-labelledby="process-title">
      <div className="container" {...sheet("process")}>
        <p className="eyebrow">How we travel</p>
        <h2 id="process-title" className={styles.h2}>
          One road, <em>four stops.</em>
        </h2>
        <ol className={styles.stops}>
          <span className={styles.line} data-line aria-hidden="true" />
          {process.map((s, k) => (
            <li key={s.step} className={styles.stop} data-stop>
              <span className={styles.dot} data-dot aria-hidden="true" />
              <span className={styles.stopNo}>{String(k + 1).padStart(2, "0")}</span>
              <h3 className={styles.stopTitle} data-step-title>
                {s.step}
              </h3>
              <p className={styles.stopText}>{s.text}</p>
            </li>
          ))}
        </ol>
      </div>
    </section>
  );
}
