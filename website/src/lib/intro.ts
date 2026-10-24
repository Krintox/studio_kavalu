"use client";

/** Run `cb` once the first-visit intro has lifted (or straight away when there is no intro). */
export function afterIntro(cb: () => void) {
  if (typeof document === "undefined") return () => {};
  const html = document.documentElement;
  if (html.dataset.intro !== "play") {
    cb();
    return () => {};
  }
  const on = () => cb();
  window.addEventListener("kv:intro-done", on, { once: true });
  return () => window.removeEventListener("kv:intro-done", on);
}

/** Inline, runs before first paint: decides whether the intro plays this time. */
export const introScript = `(function(){try{var d=document.documentElement;var r=window.matchMedia('(prefers-reduced-motion: reduce)').matches;var s=sessionStorage.getItem('kv-intro');var c=navigator.connection;var sd=!!(c&&c.saveData);d.dataset.intro=(r||s||sd||location.pathname!=='/')?'seen':'play';}catch(e){document.documentElement.dataset.intro='seen';}})();`;
