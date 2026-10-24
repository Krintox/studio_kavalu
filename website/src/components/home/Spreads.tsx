"use client";

import Image from "next/image";
import Link from "next/link";
import { useRef, type CSSProperties } from "react";
import { PaperClip } from "@/components/Ephemera";
import { featured } from "@/content/projects";
import type { Img, Project } from "@/content/types";
import { gsap, prefersReducedMotion, useGSAP } from "@/lib/gsap";
import { spreadGround } from "@/lib/surfaces";
import styles from "./Spreads.module.css";

type Treatment = "stamp" | "polaroid" | "print" | "taped";

// Where each picture lands on the spread: centre point in % of the screen, width in vw, resting tilt.
const SLOTS: { x: number; y: number; w: number; r: number; t: Treatment }[] = [
  { x: 55, y: 34, w: 19, r: -3, t: "stamp" },
  { x: 77, y: 22, w: 14, r: 5, t: "polaroid" },
  { x: 86, y: 60, w: 12.5, r: -6, t: "taped" },
  { x: 67, y: 69, w: 15, r: 3, t: "print" },
  { x: 38, y: 24, w: 11, r: -8, t: "stamp" },
  { x: 23, y: 40, w: 11, r: 6, t: "polaroid" },
  { x: 92, y: 30, w: 8.5, r: 9, t: "stamp" },
  { x: 54, y: 86, w: 10, r: -4, t: "taped" },
];

function pictures(p: Project): Img[] {
  const seen = new Set<string>();
  return [p.cover, ...p.stamps].filter((im) => (seen.has(im.src) ? false : (seen.add(im.src), true))).slice(0, SLOTS.length);
}

function Piece({ image, slot, index }: { image: Img; slot: (typeof SLOTS)[number]; index: number }) {
  const style = {
    "--x": `${slot.x}%`,
    "--y": `${slot.y}%`,
    "--w": `${slot.w}vw`,
    "--tilt": `${slot.r}deg`,
    "--ratio": slot.t === "polaroid" ? "1 / 1" : `${image.w} / ${image.h}`,
    zIndex: 10 - index,
  } as CSSProperties;
  return (
    <div className={`${styles.piece} ${styles[slot.t]}`} style={style} data-deal data-x={slot.x} data-y={slot.y}>
      <div className={styles.tilt}>
        {slot.t === "polaroid" && index % 2 ? <PaperClip className={styles.clip} /> : null}
        <div className={styles.paper}>
          <div className={styles.window}>
            <Image src={image.src} alt={image.alt} width={image.w} height={image.h} sizes={`${Math.round(slot.w * 1.6)}vw`} />
          </div>
        </div>
      </div>
    </div>
  );
}

function Spread({ project, n, total }: { project: Project; n: number; total: number }) {
  const pics = pictures(project);
  // a spread stands on a plum ground; the project's own colours live in its pictures (BRAND_DESIGN.md §4.4)
  const style = { "--p-bg": "var(--surface)", "--p-ink": "var(--on)" } as CSSProperties;
  return (
    <section className={styles.spread} style={style} {...spreadGround(n - 1)} data-spread aria-labelledby={`spread-${project.slug}`}>
      <div className={styles.sticky} data-sticky>
        <div className={`${styles.inner} paper-grain`} data-inner>
          <header className={styles.head}>
            <p className={styles.count}>
              {String(n).padStart(2, "0")} <span>/ {String(total).padStart(2, "0")}</span>
            </p>
            <ul className={styles.deliverables} aria-label="What we did">
              {project.deliverables.map((d) => (
                <li key={d}>{d}</li>
              ))}
            </ul>
          </header>

          <div className={styles.collage} aria-hidden="false">
            {pics.map((im, k) => (
              <Piece key={im.src} image={im} slot={SLOTS[k]} index={k} />
            ))}
          </div>

          <div className={styles.text} data-text>
            <p className={styles.sector}>
              {project.sector}
              {project.city ? ` · ${project.city}` : ""}
              {project.year ? ` · ${project.year}` : ""}
            </p>
            <h2 id={`spread-${project.slug}`} className={styles.title}>
              {project.title}
            </h2>
            <p className={styles.summary}>{project.summary}</p>
            <Link href={`/work/${project.slug}`} className={styles.cta}>
              Open the case study <span aria-hidden="true">→</span>
            </Link>
          </div>
          <div className={styles.shade} data-shade aria-hidden="true" />
        </div>
      </div>
    </section>
  );
}

export function Spreads() {
  const root = useRef<HTMLDivElement>(null);

  useGSAP(
    () => {
      if (prefersReducedMotion()) return;
      const mm = gsap.matchMedia();
      mm.add("(min-width: 900px)", () => {
        const spreads = gsap.utils.toArray<HTMLElement>("[data-spread]", root.current);
        spreads.forEach((spread, idx) => {
          const pieces = gsap.utils.toArray<HTMLElement>("[data-deal]", spread);
          const inner = spread.querySelector<HTMLElement>("[data-inner]")!;

          // Deal out: every picture starts in one pile at the centre and travels to its own place.
          gsap.timeline({
            scrollTrigger: { trigger: spread, start: idx === 0 ? "top 55%" : "top 75%", end: "top -25%", scrub: 0.4 },
          })
            .from(pieces, {
              // each piece's resting centre is its slot (in % of the screen); the pile sits at 62% / 50%
              x: (_: number, el: HTMLElement) => ((62 - Number(el.dataset.x)) / 100) * window.innerWidth,
              y: (_: number, el: HTMLElement) => ((50 - Number(el.dataset.y)) / 100) * window.innerHeight,
              rotation: (k: number) => (k % 2 ? 8 : -6) + k,
              scale: 0.78,
              ease: "power3.out",
              stagger: 0.05,
              duration: 1,
            })
            .from(spread.querySelectorAll("[data-text] > *"), { y: 40, opacity: 0, stagger: 0.06, duration: 0.6, ease: "power2.out" }, 0.1);

          // Zoom out as whatever comes next slides over this spread.
          const next = spreads[idx + 1] ?? spread.parentElement?.nextElementSibling;
          if (next) {
            gsap.timeline({
              scrollTrigger: { trigger: next as Element, start: "top bottom", end: "top top", scrub: 0.3 },
            })
              .to(inner, { scale: 0.9, yPercent: -3, ease: "none" }, 0)
              .to(spread.querySelector("[data-shade]"), { opacity: 0.55, ease: "none" }, 0);
          }
        });
      });
      return () => mm.revert();
    },
    { scope: root },
  );

  return (
    <div ref={root} className={styles.spreads}>
      {featured.map((p, k) => (
        <Spread key={p.slug} project={p} n={k + 1} total={featured.length} />
      ))}
    </div>
  );
}
