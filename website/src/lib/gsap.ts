"use client";

import { gsap } from "gsap";
import { CustomEase } from "gsap/CustomEase";
import { Draggable } from "gsap/Draggable";
import { Flip } from "gsap/Flip";
import { InertiaPlugin } from "gsap/InertiaPlugin";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { SplitText } from "gsap/SplitText";
import { useGSAP } from "@gsap/react";

let registered = false;

if (typeof window !== "undefined" && !registered) {
  gsap.registerPlugin(ScrollTrigger, SplitText, Draggable, InertiaPlugin, Flip, CustomEase, useGSAP);
  // The studio's two curves: "settle" for things arriving, "travel" for things moving between states.
  CustomEase.create("settle", "0.16, 1, 0.3, 1");
  CustomEase.create("travel", "0.65, 0, 0.35, 1");
  gsap.defaults({ ease: "settle", duration: 0.9 });
  // the iOS address bar showing/hiding must not re-measure every trigger
  ScrollTrigger.config({ ignoreMobileResize: true });
  registered = true;
}

export const prefersReducedMotion = () =>
  typeof window !== "undefined" && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

export { gsap, ScrollTrigger, SplitText, Draggable, InertiaPlugin, Flip, useGSAP };
