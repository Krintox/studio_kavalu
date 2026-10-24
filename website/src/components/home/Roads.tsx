"use client";

import { useRef } from "react";
import { Doodle } from "@/components/Doodles";
import { StartLink } from "@/components/onboarding/OnboardingContext";
import { services } from "@/content/site";
import { gsap, prefersReducedMotion, useGSAP } from "@/lib/gsap";
import { ground, sheet } from "@/lib/surfaces";
import styles from "./Roads.module.css";

// One road comes down the page and splits four ways; each branch ends above a card.
const W = 1200;
const STEM = 70;
const ENDS = [150, 450, 750, 1050];
const branch = (x: number) => `M600,${STEM} C600,${STEM + 70} ${x},${STEM + 40} ${x},200`;

const rest = [-2.2, 1.4, -1, 2];

export function Roads() {
  const root = useRef<HTMLElement>(null);

  useGSAP(
    () => {
      if (prefersReducedMotion()) return;
      const paths = gsap.utils.toArray<SVGPathElement>("[data-road]", root.current);
      paths.forEach((p) => {
        const len = p.getTotalLength();
        gsap.set(p, { strokeDasharray: len, strokeDashoffset: len });
      });
      // the roads draw while the map rises through the lower half of the screen, and are down before the
      // cards under them arrive (they used to finish only once the map was near the top)
      gsap.timeline({ scrollTrigger: { trigger: "[data-map]", start: "top 92%", end: "top 50%", scrub: 0.5 } })
        .to(paths[0], { strokeDashoffset: 0, ease: "none", duration: 0.35 })
        .to(paths.slice(1), { strokeDashoffset: 0, ease: "none", duration: 0.65 }, 0.35)
        .from("[data-fork-dot]", { scale: 0, transformOrigin: "50% 50%", duration: 0.15, ease: "back.out(2)" }, 0.33);

      gsap.from("[data-card]", {
        y: 90,
        opacity: 0,
        rotation: (k: number) => (k % 2 ? 9 : -8),
        duration: 1.1,
        stagger: 0.09,
        ease: "settle",
        scrollTrigger: { trigger: "[data-cards]", start: "top 90%" },
      });
    },
    { scope: root },
  );

  return (
    <section ref={root} className={styles.roads} {...ground("roads")} aria-labelledby="roads-title">
      <div className="container" {...sheet("roads")}>
        <header className={styles.head}>
          <p className="eyebrow">What we do</p>
          <h2 id="roads-title" className={styles.title}>
            Four choices, <em>four roads.</em>
          </h2>
          <p className={styles.lede}>
            Most brands need more than one. Start where you are, and we will map the rest together.
          </p>
        </header>

        <svg className={styles.map} viewBox={`0 0 ${W} 200`} aria-hidden="true" data-map>
          <path d={`M600,0 L600,${STEM}`} data-road />
          {ENDS.map((x) => (
            <path key={x} d={branch(x)} data-road />
          ))}
          <circle cx="600" cy={STEM} r="5" data-fork-dot />
        </svg>

        <ol className={styles.cards} data-cards>
          {services.map((s, k) => (
            <li
              key={s.key}
              className={`${styles.card} ${s.tone === "blue" ? styles.blue : ""}`}
              style={{ ["--rest" as string]: `${rest[k]}deg` }}
              id={`road-${s.key}`}
              data-card
            >
              <div className={styles.cardInner}>
                <p className={styles.choice}>
                  <span>{String(k + 1).padStart(2, "0")}</span> {s.choice}
                </p>
                <Doodle name={s.key} className={styles.doodle} />
                <h3 className={styles.cardTitle}>{s.title}</h3>
                <p className={styles.line}>{s.line}</p>
                <ul className={styles.items}>
                  {s.items.map((it) => (
                    <li key={it}>{it}</li>
                  ))}
                </ul>
                <StartLink road={s.key} className={styles.start} aria-label={`Start a ${s.title.toLowerCase()} project`}>
                  Start here <span aria-hidden="true">→</span>
                </StartLink>
              </div>
            </li>
          ))}
        </ol>
      </div>
    </section>
  );
}
