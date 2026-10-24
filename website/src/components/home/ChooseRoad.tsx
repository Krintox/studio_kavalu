"use client";

import { useRef, useState } from "react";
import { useOnboarding } from "@/components/onboarding/OnboardingContext";
import { roads, type RoadKey } from "@/content/onboarding";
import { site } from "@/content/site";
import { gsap, prefersReducedMotion, useGSAP } from "@/lib/gsap";
import { layerParallax } from "@/lib/parallax";
import { ground } from "@/lib/surfaces";
import styles from "./ChooseRoad.module.css";

/** The first step of "Choose your road", inline on the homepage; Continue carries the choice into the flow. */
export function ChooseRoad() {
  const root = useRef<HTMLElement>(null);
  const { start } = useOnboarding();
  const [picked, setPicked] = useState<RoadKey[]>([]);

  const toggle = (key: RoadKey, on: boolean) =>
    setPicked((cur) => (key === "unsure" ? (on ? ["unsure"] : []) : on ? [...cur.filter((r) => r !== "unsure"), key] : cur.filter((r) => r !== key)));

  useGSAP(
    () => {
      if (prefersReducedMotion()) return;
      gsap.from("[data-sheet]", {
        y: 80,
        rotation: -1.5,
        opacity: 0,
        duration: 1.1,
        scrollTrigger: { trigger: root.current, start: "top 75%" },
      });
      layerParallax(gsap.utils.selector(root)("[data-letter]")[0], 34, root.current);
    },
    { scope: root },
  );

  return (
    <section ref={root} className={styles.wrap} {...ground("choose")} aria-labelledby="choose-title">
      <div className="container" data-letter>
        <div className={styles.sheet} data-sheet>
          <div className={styles.copy}>
            <p className="eyebrow">Start a project</p>
            <h2 id="choose-title" className={styles.title}>
              Choose your <em>road.</em>
            </h2>
            <p className={styles.text}>
              Tell us where you&apos;re standing, and we&apos;ll make the next choices with you. Five short steps, about three
              minutes, read by Ananya personally.
            </p>
            <p className={styles.alt}>
              Rather write? <a href={`mailto:${site.email}`}>{site.email}</a>
            </p>
          </div>
          <form
            className={styles.form}
            onSubmit={(e) => {
              e.preventDefault();
              start(picked, { step: picked.length ? 1 : 0, ref: "home" });
            }}
          >
            <fieldset className={styles.group}>
              <legend className={styles.legend}>Which road are you on?</legend>
              <div className={styles.chips}>
                {roads.map((r) => (
                  <label key={r.key} className={styles.chip}>
                    <input type="checkbox" checked={picked.includes(r.key)} onChange={(e) => toggle(r.key, e.target.checked)} />
                    <span>
                      <b>{r.title}</b>
                      <small>{r.help}</small>
                    </span>
                  </label>
                ))}
              </div>
            </fieldset>
            <button type="submit" className={styles.go}>
              {picked.length ? "Continue" : "Start a project"} <span aria-hidden="true">→</span>
            </button>
          </form>
        </div>
      </div>
    </section>
  );
}
