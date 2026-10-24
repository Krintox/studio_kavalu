"use client";

import { useEffect, useRef, useState } from "react";
import { useLenis } from "@/components/motion/SmoothScroll";
import { site } from "@/content/site";
import { useOnboarding } from "./OnboardingContext";
import { RoadForm } from "./RoadForm";
import styles from "./OnboardingDrawer.module.css";

/** "Choose your road" as a sheet that slides in over any page, so starting a project never means leaving. */
export function OnboardingDrawer() {
  const { open, close, roads, step, ref, session } = useOnboarding();
  const lenis = useLenis();
  const panel = useRef<HTMLDivElement>(null);
  const opener = useRef<Element | null>(null);
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    if (open) setMounted(true);
  }, [open]);

  // Pause the page behind, trap the keyboard inside, and hand focus back on close.
  useEffect(() => {
    if (!open) return;
    opener.current = document.activeElement;
    lenis?.stop();
    const prevOverflow = document.documentElement.style.overflow;
    document.documentElement.style.overflow = "hidden";
    const t = window.setTimeout(() => panel.current?.querySelector<HTMLElement>("h2, [tabindex='-1']")?.focus(), 60);
    const onKey = (e: KeyboardEvent) => {
      if (e.key === "Escape") close();
      if (e.key !== "Tab" || !panel.current) return;
      const focusables = panel.current.querySelectorAll<HTMLElement>(
        'a[href], button:not([disabled]), input:not([tabindex="-1"]), textarea, select, [tabindex="0"]',
      );
      if (!focusables.length) return;
      const first = focusables[0];
      const last = focusables[focusables.length - 1];
      if (e.shiftKey && document.activeElement === first) {
        e.preventDefault();
        last.focus();
      } else if (!e.shiftKey && document.activeElement === last) {
        e.preventDefault();
        first.focus();
      }
    };
    window.addEventListener("keydown", onKey);
    return () => {
      window.clearTimeout(t);
      window.removeEventListener("keydown", onKey);
      document.documentElement.style.overflow = prevOverflow;
      lenis?.start();
      (opener.current as HTMLElement | null)?.focus?.();
    };
  }, [open, close, lenis]);

  if (!mounted) return null;

  return (
    <div className={styles.root} data-open={open} aria-hidden={!open}>
      <div className={styles.backdrop} onClick={close} />
      <div
        ref={panel}
        className={`${styles.panel} paper-grain`}
        role="dialog"
        aria-modal="true"
        aria-label="Start a project"
        data-lenis-prevent
        inert={!open}
      >
        <div className={styles.bar}>
          <span className={styles.barMark}>
            <span lang="kn" className="kn">
              {site.word}
            </span>
            {site.name}
          </span>
          <button type="button" className={styles.close} onClick={close} aria-label="Close the project form">
            Close <span aria-hidden="true">×</span>
          </button>
        </div>
        <div className={styles.body}>
          <RoadForm key={session} layout="drawer" initialRoads={roads} initialStep={step} from={ref} onDone={close} />
        </div>
      </div>
    </div>
  );
}
