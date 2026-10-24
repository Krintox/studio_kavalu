"use client";

import { gsap, prefersReducedMotion, SplitText } from "@/lib/gsap";

/*
 * The album's handwork, in motion. Studied frame by frame on the Digital Stamp Collection, whose hand
 * notes are drawn on stroke by stroke (research/motion_frames/sites/NOTES.md):
 *
 *   writeIn  a hand note writes itself in: word after word, each uncovered left to right at pen speed
 *   typeIn   a typed label types on: one character after another, like the strip coming off a typewriter
 *
 * Both run once (on scroll into view, or straight away with `trigger: false`), put the original
 * markup back when they finish, and do nothing under reduced motion, where the words are simply there.
 * Call them inside a component's useGSAP so they are cleaned up with it.
 */

type Options = { delay?: number; trigger?: Element | false };

// Cursive loops and swashes overhang the word box, so the window reaches past it on every side.
const UNWRITTEN = "inset(-40% 112% -50% -12%)";
const WRITTEN = "inset(-40% -12% -50% -12%)";

// Kannada (and any Indic script) is shaped in clusters; splitting it into letters would break the shaping.
const INDIC = /[ऀ-෿]/;

const once = (trigger: Element | false) => (trigger ? { scrollTrigger: { trigger, start: "top 88%", once: true } } : {});

export function writeIn(el: HTMLElement | null | undefined, { delay = 0, trigger = el ?? false }: Options = {}) {
  if (!el || prefersReducedMotion()) return null;
  const split = SplitText.create(el, { type: "words" });
  gsap.set(split.words, { clipPath: UNWRITTEN });
  // the delay is the first word's place in the timeline (a timeline's own delay is not reliably
  // honoured when a ScrollTrigger plays it)
  const tl = gsap.timeline({ ...once(trigger), onComplete: () => split.revert() });
  split.words.forEach((word, i) => {
    // about 25 letters a second, a little quicker on long words, with the pen lifting between words
    const letters = (word.textContent ?? "").trim().length;
    tl.to(word, { clipPath: WRITTEN, duration: Math.min(0.36, 0.04 + letters * 0.04), ease: "power1.inOut" }, i ? ">+0.025" : delay);
  });
  return tl;
}

export function typeIn(el: HTMLElement | null | undefined, { delay = 0, trigger = el ?? false }: Options = {}) {
  if (!el || prefersReducedMotion() || INDIC.test(el.textContent ?? "")) return null;
  // words as well as characters, so a line can only break between words, exactly as it will at rest
  const split = SplitText.create(el, { type: "words,chars" });
  const each = Math.min(0.024, 1.1 / Math.max(split.chars.length, 1));
  gsap.set(split.chars, { opacity: 0 });
  const tl = gsap.timeline({ ...once(trigger), onComplete: () => split.revert() });
  tl.to(split.chars, { opacity: 1, duration: 0.01, stagger: each, ease: "none" }, delay);
  return tl;
}
