"use client";

import Image from "next/image";
import Link from "next/link";
import { useCallback, useEffect, useRef, useState } from "react";
import { projects } from "@/content/projects";
import { services, site } from "@/content/site";
import type { Img } from "@/content/types";
import { gsap, prefersReducedMotion, useGSAP } from "@/lib/gsap";
import { ground, sheet } from "@/lib/surfaces";
import styles from "./Manifesto.module.css";

/*
 * The house view (BRAND_DESIGN.md §10.12): the brand line is the index of the four roads. The sentence
 * stands still; each of its four choices is a link to its road, with a hand-drawn road under it that
 * forks at the end, and a typed footnote number. The roads draw once, in reading order. Pointing at a
 * choice quiets the other three (never below 50%) and lays one print of that road's work in the margin.
 * Researched in research/DESIGN_PRINCIPLES_v3.md §7 (proposal A); the ink-in words and the pictures
 * inside the sentence it replaces are now off-the-shelf components.
 */

const lead = "A brand is a set of choices;";
// each choice as it reads in the sentence, the punctuation after it, and the line it ends on (desktop)
const choices = [
  { words: "what it says", after: ",", line: 1 },
  { words: "how it looks", after: ",", line: 1 },
  { words: "where it shows up", after: ",", line: 2 },
  { words: "who it speaks to", after: ".", line: 3 },
];

const anokhi = projects[0];
const nivritti = projects[1];
const fillers = projects.find((p) => p.slug === "fillers-not-yet")!;
const stills = projects.find((p) => p.slug === "shoot-stills")!;
// one print of each road's work, laid in the margin while its choice is pointed at
const prints: { img: Img; project: string }[] = [
  { img: anokhi.stamps[6], project: anokhi.title },
  { img: nivritti.stamps[3], project: nivritti.title },
  { img: fillers.stamps[0], project: fillers.title },
  { img: stills.stamps[1], project: stills.title },
];

// a road under one line box: a hairline with a little hand wobble, forking at its end
function roadPath(x0: number, x1: number, y: number, seed: number, fork: boolean) {
  const w = x1 - x0;
  const j = (k: number) => Math.sin(seed * 12.9898 + k * 78.233) * 0.6;
  let d = `M${x0.toFixed(1)},${(y + j(1)).toFixed(1)} C${(x0 + w / 3).toFixed(1)},${(y + j(2)).toFixed(1)} ${(x0 + (2 * w) / 3).toFixed(1)},${(y + j(3)).toFixed(1)} ${x1.toFixed(1)},${y.toFixed(1)}`;
  if (fork) d += ` M${x1.toFixed(1)},${y.toFixed(1)} l7,-4.5 M${x1.toFixed(1)},${y.toFixed(1)} l7,4.5`;
  return d;
}

export function Manifesto() {
  const root = useRef<HTMLElement>(null);
  const stage = useRef<HTMLDivElement>(null);
  const [roads, setRoads] = useState<string[]>([]);
  const [active, setActive] = useState<number | null>(null);

  // the roads follow the words: measured from each choice's line boxes, again on resize and once the fonts load
  const measure = useCallback(() => {
    const box = stage.current;
    if (!box) return;
    const o = box.getBoundingClientRect();
    const next = [...box.querySelectorAll<HTMLElement>("[data-choice-words]")].map((el, k) => {
      const size = parseFloat(getComputedStyle(el).fontSize);
      const rects = [...el.getClientRects()];
      return rects
        .map((r, i) => roadPath(r.left - o.left, r.right - o.left, r.bottom - o.top - size * 0.04, k * 4 + i, i === rects.length - 1))
        .join(" ");
    });
    setRoads(next);
  }, []);

  useEffect(() => {
    measure();
    const ro = new ResizeObserver(measure);
    if (stage.current) ro.observe(stage.current);
    document.fonts?.ready.then(measure);
    return () => ro.disconnect();
  }, [measure]);

  useGSAP(
    () => {
      if (prefersReducedMotion() || !roads.length) return;
      const paths = gsap.utils.toArray<SVGPathElement>("[data-road]", root.current);
      paths.forEach((p) => {
        const len = p.getTotalLength();
        gsap.set(p, { strokeDasharray: len, strokeDashoffset: len });
      });
      const marks = gsap.utils.toArray<HTMLElement>("[data-mark]", root.current);
      gsap.set(marks, { autoAlpha: 0 });
      // drawn once, in reading order, as the sentence comes up the screen
      gsap
        .timeline({ scrollTrigger: { trigger: stage.current, start: "top 70%", once: true } })
        .to(paths, { strokeDashoffset: 0, duration: 0.7, ease: "power2.inOut", stagger: 0.22 })
        .to(marks, { autoAlpha: 1, duration: 0.25, ease: "settle", stagger: 0.22 }, 0.55)
        .from("[data-legend] li", { autoAlpha: 0, y: 6, duration: 0.5, ease: "settle", stagger: 0.06 }, 0.9);
      gsap.from("[data-after] > *", {
        y: 24,
        autoAlpha: 0,
        stagger: 0.1,
        duration: 0.9,
        ease: "settle",
        scrollTrigger: { trigger: "[data-after]", start: "top 85%", once: true },
      });
    },
    { scope: root, dependencies: [roads.length] },
  );

  return (
    <section ref={root} className={styles.manifesto} {...ground("manifesto")} aria-labelledby="manifesto-title">
      <div className={`container ${styles.wrap}`} {...sheet("manifesto")}>
        <p className="eyebrow">The house view</p>

        <div ref={stage} className={styles.stage} data-active={active ?? undefined}>
          <h2 id="manifesto-title" className={styles.sentence}>
            <span className={styles.line}>{lead}</span>{" "}
            {[1, 2, 3].map((line) => (
              <span key={line} className={styles.line}>
                {choices.map((c, k) =>
                  c.line === line ? (
                    <span key={c.words} className={styles.choiceWrap} data-on={active === k ? "" : undefined}>
                      <a
                        href={`#road-${services[k].key}`}
                        className={styles.choice}
                        onPointerEnter={() => setActive(k)}
                        onPointerLeave={() => setActive(null)}
                        onFocus={() => setActive(k)}
                        onBlur={() => setActive(null)}
                        data-cursor="view"
                        data-cursor-label={`Road ${String(k + 1).padStart(2, "0")}`}
                      >
                        <span data-choice-words>{c.words}</span>
                        <span className="sr-only"> ({services[k].title})</span>
                      </a>
                      {c.after}
                      <sup className={styles.index} aria-hidden="true" data-mark>
                        {String(k + 1).padStart(2, "0")}
                      </sup>{" "}
                    </span>
                  ) : null,
                )}
              </span>
            ))}
          </h2>

          <svg className={styles.roads} aria-hidden="true">
            {roads.map((d, k) => (
              <path key={k} d={d} data-road data-on={active === k ? "" : undefined} />
            ))}
          </svg>

          <div className={styles.margin} aria-hidden="true">
            {prints.map((p, k) => (
              <figure key={p.img.src} className={styles.print} data-on={active === k ? "" : undefined}>
                <span className={styles.tape} />
                <div className={styles.window}>
                  <Image src={p.img.src} alt="" width={p.img.w} height={p.img.h} sizes="240px" />
                </div>
                <figcaption>
                  {String(k + 1).padStart(2, "0")} · {services[k].title} · {p.project}
                </figcaption>
              </figure>
            ))}
          </div>
        </div>

        <ol className={styles.legend} aria-hidden="true" data-legend>
          {services.map((s, k) => (
            <li key={s.key} data-on={active === k ? "" : undefined}>
              <span>{String(k + 1).padStart(2, "0")}</span> {s.title}
            </li>
          ))}
        </ol>

        <div className={styles.after} data-after>
          <p className={styles.about}>{site.about}</p>
          <div>
            <p className={styles.aim}>
              <span className="hand">{site.aim.slice(0, site.aim.indexOf(":") + 1)}</span>
              {site.aim.slice(site.aim.indexOf(":") + 1)}
            </p>
            <Link href="/studio" className={styles.link}>
              About the studio <span aria-hidden="true">→</span>
            </Link>
          </div>
        </div>
      </div>
    </section>
  );
}
