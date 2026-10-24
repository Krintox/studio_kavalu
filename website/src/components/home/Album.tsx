"use client";

import Image from "next/image";
import Link from "next/link";
import { useRef, useState, type PointerEvent } from "react";
import { allStamps, projects } from "@/content/projects";
import { gsap, prefersReducedMotion, useGSAP } from "@/lib/gsap";
import { ground } from "@/lib/surfaces";
import styles from "./Album.module.css";

/** Every stamp from every project in one row you can drag, scroll or step through. */
export function Album() {
  const root = useRef<HTMLElement>(null);
  const row = useRef<HTMLDivElement>(null);
  const drag = useRef({ on: false, x: 0, left: 0, moved: 0 });
  const [grabbing, setGrabbing] = useState(false);
  const stamps = allStamps();

  useGSAP(
    () => {
      if (prefersReducedMotion()) return;
      gsap.from("[data-album-stamp]", {
        y: 40,
        rotation: (k: number) => (k % 2 ? 6 : -5),
        opacity: 0,
        duration: 0.9,
        stagger: 0.045,
        scrollTrigger: { trigger: row.current, start: "top 85%" },
      });
    },
    { scope: root },
  );

  const step = (dir: 1 | -1) =>
    row.current?.scrollBy({ left: dir * row.current.clientWidth * 0.7, behavior: prefersReducedMotion() ? "auto" : "smooth" });

  // Mouse drag to scroll; touch already scrolls natively.
  const down = (e: PointerEvent<HTMLDivElement>) => {
    if (e.pointerType !== "mouse" || !row.current) return;
    drag.current = { on: true, x: e.clientX, left: row.current.scrollLeft, moved: 0 };
    setGrabbing(true);
  };
  const move = (e: PointerEvent<HTMLDivElement>) => {
    if (!drag.current.on || !row.current) return;
    const dx = e.clientX - drag.current.x;
    drag.current.moved = Math.max(drag.current.moved, Math.abs(dx));
    row.current.scrollLeft = drag.current.left - dx;
  };
  const up = () => {
    drag.current.on = false;
    setGrabbing(false);
  };

  return (
    <section ref={root} className={styles.album} {...ground("album")} aria-labelledby="album-title">
      <div className={`container ${styles.head}`}>
        <div>
          <h2 id="album-title" className={styles.title}>
            Every stamp, <em>every project.</em>
          </h2>
        </div>
        <div className={styles.controls}>
          <Link href="/work" className={styles.all}>
            All work ({projects.length}) <span aria-hidden="true">→</span>
          </Link>
          <button type="button" onClick={() => step(-1)} aria-label="Scroll the album back">
            ←
          </button>
          <button type="button" onClick={() => step(1)} aria-label="Scroll the album forward">
            →
          </button>
        </div>
      </div>
      <div
        ref={row}
        className={styles.row}
        data-grabbing={grabbing}
        onPointerDown={down}
        onPointerMove={move}
        onPointerUp={up}
        onPointerLeave={up}
        onClickCapture={(e) => {
          if (drag.current.moved > 6) {
            e.preventDefault();
            e.stopPropagation();
          }
        }}
      >
        {stamps.map(({ image, project }, k) => (
          <Link
            key={image.src + k}
            href={`/work/${project.slug}`}
            className={styles.item}
            data-cursor="drag"
            data-album-stamp
            style={{ ["--tilt" as string]: `${[-2.5, 1.8, -1, 2.6, -1.8, 1.2][k % 6]}deg` }}
            draggable={false}
          >
            <span className={styles.stamp}>
              <span className={styles.window}>
                <Image src={image.src} alt={image.alt} width={image.w} height={image.h} sizes="220px" draggable={false} />
              </span>
            </span>
            <span className={styles.caption}>
              <span>fig. {String(k + 1).padStart(2, "0")}</span> {project.title}
            </span>
          </Link>
        ))}
      </div>
    </section>
  );
}
