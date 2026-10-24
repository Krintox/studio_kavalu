"use client";

import Image from "next/image";
import { useMemo, useRef } from "react";
import { Word } from "@/components/brand/Wordmark";
import { allStamps, featured } from "@/content/projects";
import { site } from "@/content/site";
import { gsap, useGSAP } from "@/lib/gsap";
import styles from "./Intro.module.css";

/*
 * First visit only, before the hero: her work flashes past full-screen like a studio ident (studied
 * frame by frame on nvmbr.in: ~4 s of cuts that accelerate from ~450 ms to under 100 ms, then the name;
 * research/motion_frames/intros/). The reel speeds up, the last picture zooms out into a stamp, her
 * STUDIO / KAVALU rises under it, and the sheet lifts onto the hero, whose flip-book opens on that same
 * picture. Whether it plays is decided before first paint (introScript), so return visits never see a
 * flash; any click, key or scroll skips to the lift; reduced motion and Save-Data never play it.
 *
 * Flash-safe by construction: the fast frames are printed in plum duotone (#kv-reel in SvgDefs), so no
 * cut changes the luminance by WCAG 2.3.1's 10%. Only the last picture develops into colour, once, as the
 * camera pulls back.
 */

// how long each picture stays, in seconds: slow enough to read the first ones, then a blur of work
const BEATS = [0.24, 0.2, 0.17, 0.145, 0.125, 0.11, 0.096, 0.084, 0.074, 0.066, 0.06, 0.055, 0.052, 0.05];

export function Intro() {
  const root = useRef<HTMLDivElement>(null);
  const reel = useMemo(() => {
    const all = allStamps();
    const first = featured[0];
    const last = all.find((f) => f.project.slug === first.slug) ?? all[0];
    const rest = all.filter((f) => f !== last).slice(0, BEATS.length);
    return [...rest, last];
  }, []);
  const last = reel[reel.length - 1];

  useGSAP(
    () => {
      const el = root.current;
      if (!el || document.documentElement.dataset.intro !== "play") return;
      const frames = gsap.utils.toArray<HTMLElement>("[data-frame]", el);
      const film = el.querySelector<HTMLElement>("[data-film]")!;
      const stamp = el.querySelector<HTMLElement>("[data-stamp]")!;
      const letters = gsap.utils.toArray<SVGPathElement>("[data-name] path", el);
      let tl: gsap.core.Timeline | null = null;
      let lift = 0;

      const finish = () => {
        try {
          sessionStorage.setItem("kv-intro", "1");
        } catch {
          /* private mode: it may play again, which is fine */
        }
        document.documentElement.dataset.intro = "done";
        window.dispatchEvent(new Event("kv:intro-done"));
      };

      const build = () => {
        // where the last picture lands: a 4:5 stamp window a little above the middle
        const h = Math.min(window.innerHeight * 0.36, window.innerWidth * 0.62);
        const w = h * 0.8;
        const top = window.innerHeight * 0.4 - h / 2;
        const left = (window.innerWidth - w) / 2;
        const right = window.innerWidth - left - w;
        const bottom = window.innerHeight - top - h;
        gsap.set(stamp, { top, left, width: w, height: h });

        tl = gsap.timeline({ onComplete: () => gsap.set(el, { display: "none" }) });
        let t = 0.25;
        frames.forEach((f, k) => {
          tl!.set(f, { autoAlpha: 1 }, t);
          if (k) tl!.set(frames[k - 1], { autoAlpha: 0 }, t);
          t += k < BEATS.length ? BEATS[k] : 0;
        });
        // the camera pulls back: the last picture closes in to a stamp window, and the paper edge lands
        const zoom = t + 0.08;
        tl.fromTo(
          film,
          { clipPath: "inset(0px 0px 0px 0px round 0px)" },
          { clipPath: `inset(${top}px ${right}px ${bottom}px ${left}px round 2px)`, duration: 0.78, ease: "expo.inOut" },
          zoom,
        )
          .fromTo(frames[frames.length - 1].querySelectorAll("img"), { scale: 1.12 }, { scale: 1, duration: 0.78, ease: "expo.inOut" }, zoom)
          // the last picture develops from the duotone into its own colours as it pulls back
          .to("[data-develop]", { autoAlpha: 0, duration: 0.7, ease: "power1.inOut" }, zoom + 0.04)
          .fromTo(stamp, { autoAlpha: 0, scale: 1.05 }, { autoAlpha: 1, scale: 1, duration: 0.32, ease: "settle" }, zoom + 0.66)
          .set(film, { autoAlpha: 0 }, zoom + 0.98)
          // her name rises under it, letter by letter
          .fromTo(letters, { y: 118 }, { y: 0, duration: 0.62, ease: "settle", stagger: 0.03 }, zoom + 0.6)
          .fromTo("[data-intro-sub]", { autoAlpha: 0, y: 8 }, { autoAlpha: 1, y: 0, duration: 0.5, ease: "settle" }, zoom + 0.95);
        // the sheet lifts onto the hero
        lift = zoom + 1.75;
        tl.add(finish, lift)
          .to(el, { clipPath: "inset(0% 0% 100% 0%)", duration: 0.78, ease: "travel" }, lift)
          .to("[data-intro-inner]", { y: -70, duration: 0.78, ease: "travel" }, lift);
      };

      // wait until every picture is decoded (at most 1.6 s), so the cuts keep their rhythm and no frame
      // flashes empty
      const imgs = [...frames.map((f) => f.querySelector("img")!), stamp.querySelector("img")!];
      const ready = Promise.all(imgs.map((img) => img.decode().catch(() => null)));
      Promise.race([ready, new Promise((r) => window.setTimeout(r, 1600))]).then(build);

      const skip = () => {
        if (tl && tl.time() < lift) tl.seek(lift);
      };
      const onKey = () => skip();
      el.addEventListener("click", skip);
      window.addEventListener("keydown", onKey);
      window.addEventListener("wheel", skip, { passive: true });
      window.addEventListener("touchmove", skip, { passive: true });
      return () => {
        el.removeEventListener("click", skip);
        window.removeEventListener("keydown", onKey);
        window.removeEventListener("wheel", skip);
        window.removeEventListener("touchmove", skip);
      };
    },
    { scope: root },
  );

  return (
    <div ref={root} className={styles.intro} aria-hidden="true">
      <div className={styles.inner} data-intro-inner>
        <div className={styles.film} data-film>
          {reel.map((f, k) => (
            <div key={`${f.image.src}-${k}`} className={styles.frame} data-frame>
              {k === reel.length - 1 ? (
                <Image src={f.image.src} alt="" fill sizes="100vw" quality={70} loading="eager" draggable={false} />
              ) : null}
              <Image
                src={f.image.src}
                alt=""
                fill
                sizes="100vw"
                quality={70}
                loading="eager"
                draggable={false}
                className={styles.mono}
                data-develop={k === reel.length - 1 ? "" : undefined}
              />
            </div>
          ))}
        </div>
        <div className={styles.stamp} data-stamp>
          <div className={styles.stampWindow}>
            <Image src={last.image.src} alt="" fill sizes="40vh" quality={80} loading="eager" draggable={false} />
          </div>
        </div>
        <div className={styles.name} data-name>
          <Word word="STUDIO" className={styles.word} />
          <Word word="KAVALU" className={styles.word} />
          <p className={styles.sub} data-intro-sub>
            <span lang="kn">{site.kannada}</span> · {site.byline}
          </p>
        </div>
        <p className={styles.skip}>click to skip</p>
      </div>
    </div>
  );
}
