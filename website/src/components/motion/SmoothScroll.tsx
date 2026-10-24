"use client";

import Lenis from "lenis";
import { usePathname } from "next/navigation";
import { createContext, useContext, useEffect, useRef, useState, type ReactNode } from "react";
import { gsap, prefersReducedMotion, ScrollTrigger } from "@/lib/gsap";

const LenisContext = createContext<Lenis | null>(null);
export const useLenis = () => useContext(LenisContext);

/**
 * Lenis drives the page scroll and GSAP's ticker drives Lenis, so ScrollTrigger and the smooth
 * scroll share one clock. Reduced motion (or a touch-first device) keeps native scrolling.
 */
export function SmoothScroll({ children }: { children: ReactNode }) {
  const [lenis, setLenis] = useState<Lenis | null>(null);
  const pathname = usePathname();
  const first = useRef(true);

  useEffect(() => {
    if (prefersReducedMotion()) return;
    // lerp 0.09: a touch more glide than the default, still short of floaty (BRAND_DESIGN.md §9.6)
    // in-page links (the house view's four choices) glide to their target and stop a little short of it
    const instance = new Lenis({ lerp: 0.09, autoRaf: false, anchors: { offset: -48 }, stopInertiaOnNavigate: true });
    const raf = (time: number) => instance.raf(time * 1000);
    instance.on("scroll", ScrollTrigger.update);
    gsap.ticker.add(raf);
    gsap.ticker.lagSmoothing(0);
    setLenis(instance);
    // Web fonts change line lengths and heights; re-measure every trigger once they are in.
    document.fonts?.ready.then(() => ScrollTrigger.refresh());
    return () => {
      gsap.ticker.remove(raf);
      instance.destroy();
      setLenis(null);
    };
  }, []);

  // A new page starts at the top, and every trigger re-measures once its layout has settled.
  useEffect(() => {
    if (first.current) {
      first.current = false;
      return;
    }
    if (lenis) lenis.scrollTo(0, { immediate: true, force: true });
    else window.scrollTo(0, 0);
    const id = requestAnimationFrame(() => ScrollTrigger.refresh());
    return () => cancelAnimationFrame(id);
  }, [pathname, lenis]);

  return <LenisContext.Provider value={lenis}>{children}</LenisContext.Provider>;
}
