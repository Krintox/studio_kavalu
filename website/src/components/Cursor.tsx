"use client";

import { useEffect, useRef } from "react";
import { gsap, prefersReducedMotion } from "@/lib/gsap";
import styles from "./Cursor.module.css";

/*
 * The studio's cursor (BRAND_DESIGN.md §10.11). Only for a fine pointer that can hover; touch, keyboard
 * and forced-colours users keep the system cursor. Researched in research/DESIGN_PRINCIPLES_v3.md §4:
 * the dot is exact (a lagging dot makes every click feel late), and what a click will do is said on a
 * small typed paper tag beside the pointer, never on a disc laid over the work it invites you to open.
 *
 *   default  an 8 px ink dot, exactly at the pointer
 *   link     a 36 px ring opens round it (any link or button), following a breath behind
 *   view     a typed tag: "OPEN →", or its own word          [data-cursor="view"] [data-cursor-label]
 *   drag     a typed tag: "← DRAG →"                         [data-cursor="drag"]
 *   text     hidden, so the native caret shows (inputs, textareas)
 *
 * The nearest [data-cursor] wins over a link, so a draggable strip of links still says "drag".
 */
export function Cursor() {
  const ref = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const el = ref.current;
    const fine = window.matchMedia("(hover: hover) and (pointer: fine)");
    const forced = window.matchMedia("(forced-colors: active)");
    if (!el || !fine.matches || forced.matches) return;
    const html = document.documentElement;
    html.classList.add("has-cursor");
    const reduce = prefersReducedMotion();
    const dot = el.querySelector<HTMLElement>("[data-cursor-dot]")!;
    const trail = el.querySelector<HTMLElement>("[data-cursor-trail]")!;
    const label = el.querySelector<HTMLElement>("[data-cursor-text]")!;
    // the dot sits exactly on the pointer; the ring and the tag follow a breath behind (0.14 s)
    const dotX = gsap.quickSetter(dot, "x", "px");
    const dotY = gsap.quickSetter(dot, "y", "px");
    const toX = gsap.quickTo(trail, "x", { duration: reduce ? 0 : 0.14, ease: "power3" });
    const toY = gsap.quickTo(trail, "y", { duration: reduce ? 0 : 0.14, ease: "power3" });
    let shown = false;

    const read = (target: EventTarget | null) => {
      const t = target as Element | null;
      if (!t || !t.closest) return;
      const own = t.closest<HTMLElement>("[data-cursor]");
      const typing = t.closest("input, textarea, select, [contenteditable='true']");
      const link = t.closest("a, button, summary, label[for], [role='button']");
      // whichever is nearer the pointer decides: a word on the link itself (or inside it) wins, a link
      // inside an annotated area (a button on a draggable card) is still a link
      const ownWins = own && (!link || own === link || link.contains(own));
      const state = typing ? "text" : ownWins ? own!.dataset.cursor! : link ? "link" : "default";
      if (el.dataset.state !== state) el.dataset.state = state;
      label.textContent = state === "view" ? own?.dataset.cursorLabel || "Open" : state === "drag" ? own?.dataset.cursorLabel || "Drag" : "";
      el.dataset.tone = t.closest("[data-tone]")?.getAttribute("data-tone") === "dark" || t.closest(".on-dark") ? "dark" : "light";
    };

    const onMove = (e: PointerEvent) => {
      if (e.pointerType !== "mouse") return;
      dotX(e.clientX);
      dotY(e.clientY);
      toX(e.clientX);
      toY(e.clientY);
      if (!shown) {
        shown = true;
        gsap.set(trail, { x: e.clientX, y: e.clientY });
        el.dataset.visible = "true";
      }
    };
    const onOver = (e: PointerEvent) => read(e.target);
    const onLeave = () => {
      el.dataset.visible = "false";
      shown = false;
    };
    const onDown = () => (el.dataset.pressed = "true");
    const onUp = () => (el.dataset.pressed = "false");

    window.addEventListener("pointermove", onMove, { passive: true });
    document.addEventListener("pointerover", onOver, { passive: true });
    document.documentElement.addEventListener("pointerleave", onLeave);
    window.addEventListener("pointerdown", onDown, { passive: true });
    window.addEventListener("pointerup", onUp, { passive: true });
    return () => {
      html.classList.remove("has-cursor");
      window.removeEventListener("pointermove", onMove);
      document.removeEventListener("pointerover", onOver);
      document.documentElement.removeEventListener("pointerleave", onLeave);
      window.removeEventListener("pointerdown", onDown);
      window.removeEventListener("pointerup", onUp);
    };
  }, []);

  return (
    <div ref={ref} className={styles.cursor} data-state="default" data-tone="light" data-visible="false" aria-hidden="true">
      <span className={styles.trail} data-cursor-trail>
        <span className={styles.ring} />
        <span className={styles.tag}>
          <span className={styles.text} data-cursor-text />
        </span>
      </span>
      <span className={styles.dot} data-cursor-dot />
    </div>
  );
}
