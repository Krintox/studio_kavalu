"use client";

import { gsap, prefersReducedMotion } from "@/lib/gsap";

/*
 * Parallax, the studio's way (BRAND_DESIGN.md §9): paper and pictures only, never words; a few dozen
 * pixels at most; always scrubbed to the reader's scroll, so it reverses exactly when they scroll back;
 * off under reduced motion. Call these inside a component's useGSAP so they are cleaned up with it.
 */

/**
 * Depth: pieces of a collage drift up at different speeds while their section scrolls away, so the
 * nearer ones (higher `data-depth`, 0–1) move more. Nothing leaves and nothing is added: the same
 * pieces stay in view, only the distances between them breathe.
 */
export function depthDrift(section: Element | null | undefined, pieces: HTMLElement[], range = 120) {
  if (!section || prefersReducedMotion()) return;
  for (const piece of pieces) {
    const depth = Number(piece.dataset.depth ?? 0.3);
    // move the layer under the piece, so its own arrival and resting tilt are left alone
    const layer = (piece.hasAttribute("data-piece") ? piece.firstElementChild : piece) as HTMLElement | null;
    if (!layer) continue;
    gsap.fromTo(
      layer,
      { y: 0 },
      { y: -range * depth, ease: "none", scrollTrigger: { trigger: section, start: "top top", end: "bottom top", scrub: true } },
    );
  }
}

/**
 * Pictures drift inside their mounts: the image sits a little larger than its window and travels
 * through it as the mount passes through the viewport.
 */
export function imageDrift(frames: HTMLElement[], travel = 4) {
  if (prefersReducedMotion()) return;
  for (const frame of frames) {
    const img = frame.querySelector("img");
    if (!img) continue;
    gsap.fromTo(
      img,
      { yPercent: -travel },
      { yPercent: travel, ease: "none", scrollTrigger: { trigger: frame, start: "top bottom", end: "bottom top", scrub: true } },
    );
  }
}
