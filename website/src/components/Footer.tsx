"use client";

import Link from "next/link";
import { useRef } from "react";
import { Word } from "@/components/brand/Wordmark";
import { FooterDesk } from "@/components/footer/FooterDesk";
import { site } from "@/content/site";
import { gsap, prefersReducedMotion, ScrollTrigger, useGSAP } from "@/lib/gsap";
import { live, SMOOTH } from "@/lib/parallax";
import { StartLink } from "./onboarding/OnboardingContext";
import styles from "./Footer.module.css";

// The cascade from the first site, kept as the studio's signature: each folder is a page.
const folders = [
  { href: "/", label: "Home", note: "start", c: "var(--plum)", t: "var(--tex-plum)", x: "74%" },
  { href: "/work", label: "Work", note: "all of it", c: "var(--oxblood)", t: "var(--tex-oxblood)", x: "58%" },
  { href: "/studio", label: "Studio", note: "who & how", c: "var(--blue)", t: "var(--tex-blue)", x: "42%", light: true },
];

export function Footer() {
  const root = useRef<HTMLElement>(null);

  useGSAP(
    () => {
      if (prefersReducedMotion()) return;
      const mark = root.current!.querySelector<HTMLElement>("[data-mark]")!;
      const studio = gsap.utils.toArray<SVGPathElement>("[data-word='studio'] path", mark);
      const kavalu = gsap.utils.toArray<SVGPathElement>("[data-word='kavalu'] path", mark);
      // STUDIO arrives from the left, KAVALU from the right; letters further out travel further, so the
      // words close up like type being set, and land exactly where they rest. It plays once, by itself,
      // when the mark is well into view: scrubbed to the scroll it finished while only the mark's top
      // edge had come up, so a reader never saw it (recorded in research/working-shots/v3/footer_watch).
      // Offsets are in the SVG's own units (cap height = 100): every letter starts at least most of a
      // word-width away, and each further-out letter 90 units further still.
      const tl = gsap.timeline({ paused: true, defaults: { duration: 1.5, ease: "settle" } });
      tl.fromTo(studio, { x: (i: number) => -(640 + (studio.length - 1 - i) * 90), opacity: 0.2 }, { x: 0, opacity: 1 }, 0).fromTo(
        kavalu,
        { x: (i: number) => 640 + i * 90, opacity: 0.2 },
        { x: 0, opacity: 1 },
        0.08,
      );
      // when the mark's top reaches 72% of the screen, or the end of the page if a tall window never
      // scrolls that far (then the letters would wait off-screen for good)
      const at = () => Math.min(ScrollTrigger.maxScroll(window) - 1, mark.getBoundingClientRect().top + window.scrollY - window.innerHeight * 0.72);
      ScrollTrigger.create({ start: at, once: true, onEnter: () => tl.play() });

      // the folders are laid down one on another as the footer comes up
      gsap.utils.toArray<HTMLElement>("[data-folder]", root.current).forEach((f, k) =>
        gsap.fromTo(
          f,
          { y: 26 * (k + 1) },
          { y: 0, ease: "none", scrollTrigger: { trigger: root.current, start: "top bottom", end: "top 45%", scrub: SMOOTH, ...live(f) } },
        ),
      );
    },
    { scope: root },
  );

  return (
    <footer ref={root} className={styles.footer} data-tone="dark" data-section="footer">
      <nav className={styles.folders} aria-label="Folders">
        {folders.map((f) => (
          <div
            key={f.href}
            className={`${styles.folder} ${f.light ? styles.light : ""}`}
            data-folder
            style={{ ["--c" as string]: f.c, ["--t" as string]: f.t, ["--x" as string]: f.x }}
            data-tone={f.light ? "light" : "dark"}
          >
            <Link href={f.href} className={styles.tab}>
              {f.label} <small>{f.note}</small>
            </Link>
          </div>
        ))}
        <div className={styles.folder} style={{ ["--c" as string]: "var(--deep)", ["--t" as string]: "var(--tex-deep)", ["--x" as string]: "26%" }} data-tone="dark" data-folder>
          <StartLink className={styles.tab}>
            Start a project <small>choose a road</small>
          </StartLink>
        </div>
      </nav>

      <div className={`${styles.body} on-dark`} data-tone="dark">
        <FooterDesk />

        <div className={styles.mark} data-mark aria-hidden="true">
          <Word word="STUDIO" data-word="studio" className={styles.studio} />
          <Word word="KAVALU" data-word="kavalu" className={styles.kavalu} />
          <span className={styles.kn} lang="kn">
            {site.kannada}
          </span>
        </div>
        <div className={styles.legal}>
          <span>© {new Date().getFullYear()} Studio Kavalu. All rights reserved.</span>
          <span>A branding & content house, {site.city}.</span>
        </div>
      </div>
    </footer>
  );
}
