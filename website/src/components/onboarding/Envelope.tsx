"use client";

import { useRef } from "react";
import { LogoMark } from "@/components/Logo";
import { site } from "@/content/site";
import { gsap, prefersReducedMotion, useGSAP } from "@/lib/gsap";
import styles from "./Envelope.module.css";

/** The letter goes into the envelope, the flap closes, and the studio stamp lands with its postmark. */
export function Envelope({ reference }: { reference: string }) {
  const root = useRef<HTMLDivElement>(null);
  const date = new Intl.DateTimeFormat("en-GB", { day: "2-digit", month: "short", year: "numeric" }).format(new Date()).toUpperCase();

  useGSAP(
    () => {
      if (prefersReducedMotion()) return;
      const tl = gsap.timeline({ defaults: { ease: "settle" } });
      tl.from("[data-env-letter]", { yPercent: -95, duration: 0.75, ease: "power2.inOut" })
        .set("[data-env-flap]", { zIndex: 1 }, 0)
        .fromTo("[data-env-flap]", { rotationX: 180 }, { rotationX: 0, duration: 0.5, ease: "power2.inOut" }, 0.7)
        .set("[data-env-flap]", { zIndex: 4 }, 0.95)
        .from("[data-env-stamp]", { y: -70, x: 30, rotation: 28, scale: 1.4, opacity: 0, duration: 0.55, ease: "back.out(1.4)" }, 1.15)
        .from("[data-env-mark]", { scale: 1.6, opacity: 0, duration: 0.35, ease: "power3.out" }, 1.55);
    },
    { scope: root },
  );

  return (
    <div ref={root} className={styles.wrap} role="img" aria-label={`Your letter, sealed and stamped. Reference ${reference}.`}>
      <div className={styles.env}>
        <div className={styles.back} />
        <div className={styles.letter} data-env-letter>
          <span />
          <span />
          <span />
          <span />
        </div>
        <div className={styles.pocket} />
        <div className={styles.flap} data-env-flap />
        <p className={styles.address}>
          <span className="hand">{site.founder.name}</span>
          {site.name}
          <br />
          {site.city}
        </p>
        <div className={styles.stamp} data-env-stamp>
          <div className={styles.stampInner}>
            <LogoMark className={styles.stampMark} />
            <span className={styles.stampRef}>{reference}</span>
          </div>
        </div>
        <div className={styles.postmark} data-env-mark aria-hidden="true">
          <svg viewBox="0 0 120 120">
            <defs>
              <path id="pm-ring" d="M60,60 m-43,0 a43,43 0 1,1 86,0 a43,43 0 1,1 -86,0" />
            </defs>
            <circle cx="60" cy="60" r="54" />
            <circle cx="60" cy="60" r="33" />
            <text>
              <textPath href="#pm-ring">KAVALU · BENGALURU · {date} ·</textPath>
            </text>
          </svg>
          <span className={styles.waves} />
        </div>
      </div>
    </div>
  );
}
