"use client";

import { usePathname } from "next/navigation";
import { useEffect } from "react";

const DARK = new Set(["plum", "deep", "oxblood"]);

/*
 * Two jobs for the grounds (styles/surfaces.css, BRAND_DESIGN.md §4.5):
 * 1. Pins every ground's paper to the page. --page-y is each section's distance from the top of the
 *    document, so neighbouring sections on one ground continue one sheet instead of meeting in a cut.
 * 2. Lays the footer's folders on the page they close: the strip above them takes the ground of the
 *    last section.
 */
export function GroundSheet() {
  const pathname = usePathname();

  useEffect(() => {
    const footer = document.querySelector<HTMLElement>("footer[data-section='footer']");
    const grounds = document.querySelectorAll<HTMLElement>("main [data-surface]");
    const last = grounds[grounds.length - 1]?.dataset.surface ?? "cream";
    if (footer) {
      footer.dataset.surface = last;
      footer.dataset.tone = DARK.has(last) ? "dark" : "light";
    }

    let raf = 0;
    const pin = () => {
      raf = 0;
      for (const el of document.querySelectorAll<HTMLElement>("[data-surface]")) {
        const y = Math.round(el.getBoundingClientRect().top + window.scrollY);
        if (el.style.getPropertyValue("--page-y") !== `${y}px`) el.style.setProperty("--page-y", `${y}px`);
      }
    };
    const schedule = () => {
      if (!raf) raf = requestAnimationFrame(pin);
    };
    pin();
    // the page grows as fonts and pictures arrive and as sections open; re-pin whenever it changes size
    const ro = new ResizeObserver(schedule);
    ro.observe(document.body);
    return () => {
      ro.disconnect();
      cancelAnimationFrame(raf);
    };
  }, [pathname]);

  return null;
}
