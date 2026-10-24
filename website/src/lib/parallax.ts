"use client";

import { gsap, prefersReducedMotion } from "@/lib/gsap";

/*
 * Scroll depth (BRAND_DESIGN.md §9.3 "Drift"; brief 6: "proper, professional, really smooth"). Everything
 * here is scrubbed to the reader's scroll, so it reverses exactly when they scroll back; it moves
 * transforms only; and a short scrub lag on top of Lenis turns every wheel tick into a glide. Three
 * kinds of depth, and nothing else moves with the scroll:
 *   media    a picture travels inside its frame (it sits a little larger than the window)
 *   layer    a block of the page drifts against the scroll at its own depth: pictures more, words less
 *   stagger  neighbours in a row move at different speeds, so a grid breathes as it passes
 * Off under reduced motion; halved below 900 px, where the screen is too short to feel depth.
 * Each layer is set at its starting point the moment it is made, so the scroll itself only ever moves
 * things: no measuring on the first frame a section comes into view (traced: that was a stall).
 * Call these inside a component's useGSAP so they are cleaned up with it.
 */

/** The scrub lag, in seconds: long enough to smooth a wheel, short enough to feel attached. */
export const SMOOTH = 0.8;
const scale = () => (window.matchMedia("(max-width: 899px)").matches ? 0.5 : 1);

/**
 * A compositor layer for everything the scroll moves, so it is only moved, never repainted. But every
 * layer the page holds is weighed again whenever anything repaints (traced: about 220 layers on the home
 * page, 8 ms per re-layering here and four times that with a phone's processor). On a phone a mover is
 * therefore promoted only while its trigger is live, and let go a second after it leaves, once the scrub
 * has caught up. A desktop re-layers quickly, and promoting a batch of movers as they came on screen was
 * itself a hitch there, so on a wide screen they keep their layers. Spread it into a scrollTrigger's vars.
 */
export function live(targets: Element | Element[] | null | undefined, prop = "transform") {
  if (!targets) return {};
  if (scale() === 1) {
    gsap.set(targets, { willChange: prop });
    return {};
  }
  let off: gsap.core.Tween | undefined;
  return {
    onToggle: (self: { isActive: boolean }) => {
      off?.kill();
      if (self.isActive) gsap.set(targets, { willChange: prop });
      else off = gsap.delayedCall(1, () => gsap.set(targets, { willChange: "auto" }));
    },
  };
}

/**
 * Media: each frame's picture sits `zoom` times larger than the window and travels `travel`% of the
 * frame's height through it as the frame crosses the viewport. zoom must leave room for the travel:
 * (zoom - 1) / 2 >= travel / 100.
 */
export function mediaParallax(frames: Iterable<Element>, travel = 7, zoom = 1.16) {
  if (prefersReducedMotion()) return;
  const k = scale();
  for (const frame of frames) {
    const img = frame.querySelector("img");
    if (!img) continue;
    gsap.set(img, { scale: zoom, transformOrigin: "50% 50%" });
    gsap.fromTo(
      img,
      { yPercent: -travel * k },
      { yPercent: travel * k, ease: "none", scrollTrigger: { trigger: frame, start: "top bottom", end: "bottom top", scrub: SMOOTH, ...live(img) } },
    );
  }
}

/**
 * Layer: an element drifts from `+px` to `-px` as it crosses the viewport, so it moves against the
 * scroll at its own depth (positive px: it lags behind the page, as something further away does).
 */
export function layerParallax(el: Element | null | undefined, px: number, trigger?: Element | null) {
  if (!el || prefersReducedMotion()) return;
  const d = px * scale();
  gsap.fromTo(
    el,
    { y: d },
    { y: -d, ease: "none", scrollTrigger: { trigger: trigger ?? el, start: "top bottom", end: "bottom top", scrub: SMOOTH, ...live(el) } },
  );
}

/**
 * Stagger: columns drift at speeds that alternate across the page, so a row or a grid breathes as it
 * passes. Everything in one column moves together (a stamp and its caption, a grid's column), so nothing
 * in it closes up on its neighbour; a single column just drifts. `px` is the largest drift.
 */
export function staggerParallax(items: HTMLElement[], px = 48, trigger?: Element | null) {
  if (!items.length || prefersReducedMotion()) return;
  const d = px * scale();
  // columns by the items' centres, so paper tilted a degree or two still lands in its own column
  const centre = (el: HTMLElement) => {
    const r = el.getBoundingClientRect();
    return r.left + r.width / 2;
  };
  const xs = items.map(centre);
  const starts: number[] = [];
  let last = -Infinity;
  for (const x of [...xs].sort((a, b) => a - b)) {
    if (x - last > 24) starts.push(x);
    last = x;
  }
  // one column (a phone): nothing to alternate, and moving it with the page would only cost frames
  if (starts.length < 2) return;
  items.forEach((el, k) => {
    const column = starts.filter((s) => s <= xs[k]).length - 1;
    const amp = column % 2 ? d : d * 0.35;
    gsap.fromTo(
      el,
      { y: amp },
      { y: -amp, ease: "none", scrollTrigger: { trigger: trigger ?? el, start: "top bottom", end: "bottom top", scrub: SMOOTH, ...live(el) } },
    );
  });
}

/**
 * Depth for a collage: pieces drift up at different speeds while their section scrolls away (higher
 * `data-depth`, 0-1, moves more). Nothing leaves: the same pieces stay in view, only the distances
 * between them breathe. Moves the layer under the piece, so its own arrival and tilt are left alone.
 */
export function depthDrift(section: Element | null | undefined, pieces: HTMLElement[], range = 120) {
  if (!section || prefersReducedMotion()) return;
  for (const piece of pieces) {
    const depth = Number(piece.dataset.depth ?? 0.3);
    const layer = (piece.hasAttribute("data-piece") ? piece.firstElementChild : piece) as HTMLElement | null;
    if (!layer) continue;
    gsap.fromTo(
      layer,
      { y: 0 },
      { y: -range * depth, ease: "none", scrollTrigger: { trigger: section, start: "top top", end: "bottom top", scrub: SMOOTH, ...live(layer) } },
    );
  }
}

/** The case study's pictures, drifting inside their mounts (kept for its call site). */
export function imageDrift(frames: HTMLElement[], travel = 7) {
  if (prefersReducedMotion()) return;
  const k = scale();
  for (const frame of frames) {
    const img = frame.querySelector("img");
    if (!img) continue;
    gsap.fromTo(
      img,
      { yPercent: -travel * k },
      { yPercent: travel * k, ease: "none", scrollTrigger: { trigger: frame, start: "top bottom", end: "bottom top", scrub: SMOOTH, ...live(img) } },
    );
  }
}
