"use client";

import Image from "next/image";
import Link from "next/link";
import { useRef } from "react";
import meta from "@/content/image-meta.json";
import { site } from "@/content/site";
import { gsap, prefersReducedMotion, useGSAP } from "@/lib/gsap";
import { ground } from "@/lib/surfaces";
import styles from "./Founder.module.css";

const portrait = (meta as Record<string, { w: number; h: number }>)["studio/ananya-portrait"];

export function Founder({ link = true }: { link?: boolean }) {
  const root = useRef<HTMLElement>(null);

  useGSAP(
    () => {
      if (prefersReducedMotion()) return;
      const tl = gsap.timeline({ scrollTrigger: { trigger: root.current, start: "top 65%" } });
      tl.from("[data-panel]", { y: 60, rotation: -4, opacity: 0, duration: 1.1, ease: "settle" })
        .fromTo(
          "[data-sign]",
          { clipPath: "inset(-20% 100% -20% 0%)" },
          { clipPath: "inset(-20% 0% -20% 0%)", duration: 1.6, ease: "travel" },
          0.45,
        )
        .from("[data-quote] > *", { y: 24, opacity: 0, filter: "blur(5px)", stagger: 0.1, duration: 0.9, clearProps: "filter" }, 0.2);
    },
    { scope: root },
  );

  return (
    <section ref={root} className={styles.founder} {...ground("founder")} aria-labelledby="founder-title">
      <div className={`container ${styles.grid}`}>
        <div className={styles.visual}>
          <div className={styles.panel} data-panel>
            <div className={styles.circle}>
              <Image
                src="/work/studio/ananya-portrait.jpg"
                alt="Ananya, founder of Studio Kavalu"
                width={portrait.w}
                height={portrait.h}
                sizes="260px"
              />
            </div>
            <p className={styles.caption}>
              <span>Founder</span>
              <span>{site.city}</span>
            </p>
          </div>
          <span className={styles.sign} data-sign aria-hidden="true">
            Ananya
          </span>
        </div>

        <div className={styles.copy} data-quote>
          <p className="eyebrow">Meet the founder</p>
          <h2 id="founder-title" className={styles.quote}>
            “{site.founder.quote[0]} <em>{site.founder.quote[1]}</em> {site.founder.quote[2]}”
          </h2>
          {site.founder.bio.map((p) => (
            <p key={p} className={styles.bio}>
              {p}
            </p>
          ))}
          {link ? (
            <Link href="/studio" className={styles.link}>
              The studio, and how we work <span aria-hidden="true">→</span>
            </Link>
          ) : null}
        </div>
      </div>
    </section>
  );
}
