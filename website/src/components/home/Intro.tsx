"use client";

import Image from "next/image";
import { useMemo, useRef } from "react";
import { Word } from "@/components/brand/Wordmark";
import { allStamps, featured } from "@/content/projects";
import { site } from "@/content/site";
import { gsap, useGSAP } from "@/lib/gsap";
import styles from "./Intro.module.css";

/*
 * The intro, on every load of the home page (brief 6). Her work flashes past full-screen like a studio
 * ident (studied frame by frame on nvmbr.in; research/motion_frames/intros/), on the landing page's own
 * cream paper. The reel speeds up, the last picture develops into its colours as the view pulls back,
 * then the whole reel fades down until it is only a faint ground, her STUDIO / KAVALU rises where the
 * headline will be, and the sheet hands over to the hero, whose own faint reel is already playing the
 * same picture underneath. No wipe: the intro sinks into the hero's background.
 *
 * Flash-safe by construction: the cuts are printed in a plum duotone (#kv-reel in SvgDefs) at half
 * strength over cream, so no cut changes the screen's luminance by anywhere near WCAG 2.3.1's 10%.
 * Any click, key or scroll fast-forwards to the hand-over; reduced motion and Save-Data never play it.
 */

// how long each picture stays, in seconds: slow enough to read the first ones, then a blur of work
const BEATS = [0.24, 0.2, 0.17, 0.145, 0.125, 0.11, 0.096, 0.084, 0.074, 0.066, 0.06, 0.055, 0.052, 0.05];
// the reel's strength while it cuts, and once it has sunk into the hero's background (Hero.module.css .reel)
const STRENGTH = 0.5;
const GROUND = 0.09;

export function Intro() {
  const root = useRef<HTMLDivElement>(null);
  const reel = useMemo(() => {
    const all = allStamps();
    const first = featured[0];
    const last = all.find((f) => f.project.slug === first.slug) ?? all[0];
    const rest = all.filter((f) => f !== last).slice(0, BEATS.length);
    return [...rest, last];
  }, []);

  useGSAP(
    () => {
      const el = root.current;
      if (!el || document.documentElement.dataset.intro !== "play") return;
      const frames = gsap.utils.toArray<HTMLElement>("[data-frame]", el);
      const film = el.querySelector<HTMLElement>("[data-film]")!;
      const letters = gsap.utils.toArray<SVGPathElement>("[data-name] path", el);
      let tl: gsap.core.Timeline | null = null;
      let handOver = 0;

      const finish = () => {
        document.documentElement.dataset.intro = "done";
        window.dispatchEvent(new Event("kv:intro-done"));
      };

      const build = () => {
        tl = gsap.timeline({ onComplete: () => gsap.set(el, { display: "none" }) });
        tl.set(film, { opacity: STRENGTH }, 0);
        let t = 0.25;
        frames.forEach((f, k) => {
          tl!.set(f, { autoAlpha: 1 }, t);
          if (k) tl!.set(frames[k - 1], { autoAlpha: 0 }, t);
          t += k < BEATS.length ? BEATS[k] : 0;
        });
        const last = frames[frames.length - 1];
        // the last picture develops into its colours as the view pulls back a little
        tl.to(last.querySelector("[data-develop]"), { autoAlpha: 0, duration: 0.6, ease: "power1.inOut" }, t + 0.05)
          .fromTo(last.querySelectorAll("img"), { scale: 1.12 }, { scale: 1, duration: 1.1, ease: "expo.out" }, t + 0.05)
          // then the reel sinks: less and less opaque, until it is only the hero's faint ground
          .to(film, { opacity: GROUND, duration: 0.85, ease: "power2.inOut" }, t + 0.45)
          // her name rises where the headline will be
          .fromTo(letters, { y: 118 }, { y: 0, duration: 0.62, ease: "settle", stagger: 0.03 }, t + 0.55)
          .fromTo("[data-intro-sub]", { autoAlpha: 0, y: 8 }, { autoAlpha: 1, y: 0, duration: 0.5, ease: "settle" }, t + 0.9);
        // the hand-over: the sheet fades out over the hero, whose reel shows the same picture underneath
        handOver = t + 1.55;
        tl.add(finish, handOver).to(el, { autoAlpha: 0, duration: 0.75, ease: "power1.inOut" }, handOver);
      };

      // wait until every picture is decoded (at most 1.6 s), so the cuts keep their rhythm and no frame
      // flashes empty
      const imgs = frames.flatMap((f) => [...f.querySelectorAll("img")]);
      const ready = Promise.all(imgs.map((img) => img.decode().catch(() => null)));
      Promise.race([ready, new Promise((r) => window.setTimeout(r, 1600))]).then(build);

      const skip = () => {
        if (tl && tl.time() < handOver) tl.seek(handOver);
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
      <div className={styles.name} data-name>
        <Word word="STUDIO" className={styles.word} />
        <Word word="KAVALU" className={styles.word} />
        <p className={styles.sub} data-intro-sub>
          <span lang="kn">{site.kannada}</span> · {site.byline}
        </p>
      </div>
      <p className={styles.skip}>click to skip</p>
    </div>
  );
}
