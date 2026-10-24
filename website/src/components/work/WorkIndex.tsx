"use client";

import Image from "next/image";
import Link from "next/link";
import { useMemo, useRef, useState, ViewTransition, type PointerEvent } from "react";
import { services } from "@/content/site";
import type { Project, ServiceKey } from "@/content/types";
import { Flip, gsap, prefersReducedMotion, useGSAP } from "@/lib/gsap";
import { mediaParallax, staggerParallax } from "@/lib/parallax";
import styles from "./WorkIndex.module.css";

type View = "stamps" | "index";

export function WorkIndex({ projects }: { projects: Project[] }) {
  const [view, setView] = useState<View>("stamps");
  const [road, setRoad] = useState<ServiceKey | "all">("all");
  const [hover, setHover] = useState<Project | null>(null);
  const grid = useRef<HTMLUListElement>(null);
  const preview = useRef<HTMLDivElement>(null);

  const shown = useMemo(() => projects.filter((p) => road === "all" || p.services.includes(road)), [projects, road]);

  // Filtering reflows the grid; Flip animates every stamp from its old place to its new one.
  const filter = (next: ServiceKey | "all") => {
    if (next === road) return;
    const items = grid.current?.querySelectorAll("[data-flip]");
    const state = items && !prefersReducedMotion() ? Flip.getState(items) : null;
    setRoad(next);
    if (state)
      requestAnimationFrame(() =>
        Flip.from(state, { duration: 0.7, ease: "settle", absolute: true, onEnter: (els) => gsap.fromTo(els, { opacity: 0, scale: 0.9 }, { opacity: 1, scale: 1, duration: 0.5 }) }),
      );
  };

  // The index preview follows the cursor a little behind it, like a print held up to the list.
  const follow = (e: PointerEvent) => {
    const el = preview.current;
    if (!el) return;
    gsap.to(el, { x: e.clientX, y: e.clientY, duration: prefersReducedMotion() ? 0 : 0.55, ease: "power3.out" });
  };

  // Depth on the stamps: the columns breathe in alternation and each picture travels inside its
  // stamp. Rebuilt whenever the grid changes (a filter or the view), so the columns are re-measured.
  useGSAP(
    () => {
      if (view !== "stamps" || !grid.current) return;
      staggerParallax(gsap.utils.toArray<HTMLElement>("[data-stamp-layer]", grid.current), 40, grid.current);
      mediaParallax(gsap.utils.toArray<HTMLElement>("[data-window]", grid.current), 6, 1.14);
    },
    { scope: grid, dependencies: [view, road], revertOnUpdate: true },
  );

  const href = (p: Project) => `/work/${p.slug}`;

  return (
    <>
      <div className={styles.toolbar}>
        <div className={styles.filters} role="group" aria-label="Filter by road">
          <button type="button" aria-pressed={road === "all"} onClick={() => filter("all")}>
            Everything <sup>{projects.length}</sup>
          </button>
          {services.map((s) => {
            const n = projects.filter((p) => p.services.includes(s.key)).length;
            return (
              <button key={s.key} type="button" aria-pressed={road === s.key} onClick={() => filter(s.key)} disabled={!n}>
                {s.title} <sup>{n}</sup>
              </button>
            );
          })}
        </div>
        <div className={styles.views} role="group" aria-label="View">
          <button type="button" aria-pressed={view === "stamps"} onClick={() => setView("stamps")}>
            Stamps
          </button>
          <button type="button" aria-pressed={view === "index"} onClick={() => setView("index")}>
            Index
          </button>
        </div>
      </div>

      {view === "stamps" ? (
        <ul ref={grid} className={styles.grid}>
          {shown.map((p, k) => (
            <li key={p.slug} data-flip data-flip-id={p.slug} className={styles.cell} style={{ ["--tilt" as string]: `${[-1.6, 1.2, -0.6, 1.8, -1.2][k % 5]}deg` }}>
              <Link href={href(p)} className={styles.card} data-cursor="view" data-cursor-label="Open">
                <ViewTransition name={`cover-${p.slug}`} share="morph" default="none">
                  <span className={styles.stamp} style={{ ["--tone" as string]: p.tone.bg }} data-stamp-layer>
                    <span className={styles.window} data-window>
                      <Image src={p.cover.src} alt={p.cover.alt} width={p.cover.w} height={p.cover.h} sizes="(max-width: 700px) 90vw, 30vw" />
                    </span>
                  </span>
                </ViewTransition>
                <span className={styles.meta}>
                  <span className={styles.no}>{String(projects.indexOf(p) + 1).padStart(2, "0")}</span>
                  <span className={styles.name}>{p.title}</span>
                  <span className={styles.sector}>
                    {p.sector}
                    {p.year ? ` · ${p.year}` : ""}
                  </span>
                </span>
              </Link>
            </li>
          ))}
        </ul>
      ) : (
        <div className={styles.indexWrap} onPointerMove={follow} onPointerLeave={() => setHover(null)}>
          <table className={styles.table}>
            <thead>
              <tr>
                <th scope="col">No.</th>
                <th scope="col">Project</th>
                <th scope="col">Sector</th>
                <th scope="col">Roads</th>
                <th scope="col">Year</th>
              </tr>
            </thead>
            <tbody>
              {shown.map((p) => (
                <tr key={p.slug} onPointerEnter={() => setHover(p)}>
                  <td className={styles.no}>{String(projects.indexOf(p) + 1).padStart(2, "0")}</td>
                  <td>
                    <Link href={href(p)} className={styles.rowLink} onFocus={() => setHover(p)} onBlur={() => setHover(null)}>
                      {p.title}
                    </Link>
                  </td>
                  <td>{p.sector}</td>
                  <td>{p.services.map((s) => services.find((x) => x.key === s)!.title).join(", ")}</td>
                  <td>{p.year ?? "—"}</td>
                </tr>
              ))}
            </tbody>
          </table>
          <div ref={preview} className={styles.preview} data-on={!!hover} aria-hidden="true">
            {hover ? (
              <span className={styles.previewStamp} key={hover.slug}>
                <span className={styles.window}>
                  <Image src={hover.cover.src} alt="" width={hover.cover.w} height={hover.cover.h} sizes="280px" />
                </span>
              </span>
            ) : null}
          </div>
        </div>
      )}
    </>
  );
}
