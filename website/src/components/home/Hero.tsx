"use client";

import Image from "next/image";
import Link from "next/link";
import { useEffect, useMemo, useRef, useState, type CSSProperties } from "react";
import { PaperClip, Sticker } from "@/components/Ephemera";
import { StartLink, useOnboarding } from "@/components/onboarding/OnboardingContext";
import { allStamps, featured, projects } from "@/content/projects";
import { site } from "@/content/site";
import { gsap, prefersReducedMotion, SplitText, useGSAP } from "@/lib/gsap";
import { ground } from "@/lib/surfaces";
import { writeIn } from "@/lib/handmade";
import { depthDrift } from "@/lib/parallax";
import { afterIntro } from "@/lib/intro";
import styles from "./Hero.module.css";

const FRAME_MS = 420;
const tilt = (deg: number) => ({ "--tilt": `${deg}deg` }) as CSSProperties;

/*
 * Every piece on the album page has two layers: the outer one is moved by GSAP (arrival, drift),
 * the inner one keeps its paper tilt in a CSS variable. Keeping them apart means scroll motion
 * never fights the resting angle, and the page still looks right with JavaScript off.
 */
export function Hero() {
  const root = useRef<HTMLElement>(null);
  const frames = useMemo(() => allStamps(), []);
  const first = featured[0];
  const firstIndex = Math.max(
    0,
    frames.findIndex((f) => f.project.slug === first.slug),
  );
  const [i, setI] = useState(firstIndex);
  const [paused, setPaused] = useState(false);
  const [held, setHeld] = useState(false);
  const [inView, setInView] = useState(true);
  const [reduced, setReduced] = useState(false);
  // behind the first-visit intro the flip-book holds on the picture the intro lands on
  const [introDone, setIntroDone] = useState(false);
  const { open: drawerOpen } = useOnboarding();

  useEffect(() => setReduced(prefersReducedMotion()), []);
  useEffect(() => afterIntro(() => setIntroDone(true)), []);

  // The flip-book only runs while it can be seen and isn't held (and never under reduced motion).
  useEffect(() => {
    if (paused || held || !inView || reduced || drawerOpen || !introDone) return;
    const id = window.setInterval(() => setI((v) => (v + 1) % frames.length), FRAME_MS);
    return () => window.clearInterval(id);
  }, [paused, held, inView, reduced, drawerOpen, introDone, frames.length]);

  useEffect(() => {
    const el = root.current;
    if (!el) return;
    const io = new IntersectionObserver(([e]) => setInView(e.isIntersecting), { threshold: 0.05 });
    io.observe(el);
    return () => io.disconnect();
  }, []);

  useGSAP(
    () => {
      if (prefersReducedMotion()) return;
      const q = gsap.utils.selector(root);
      const title = q("[data-title]")[0] as HTMLElement | undefined;

      // Arrival: lines rise out of their masks, the album settles onto the page (after the intro, if any).
      const introPlays = document.documentElement.dataset.intro === "play";
      const stopWaiting = afterIntro(() => {
        if (title) {
          SplitText.create(title, {
            type: "lines",
            mask: "lines",
            autoSplit: true,
            onSplit: (self) =>
              gsap.from(self.lines, { yPercent: 108, duration: 1.1, stagger: 0.08, ease: "settle", delay: 0.05 }),
          });
        }
        gsap.from(q("[data-arrive]"), {
          y: 22,
          opacity: 0,
          filter: "blur(6px)",
          duration: 1,
          stagger: 0.08,
          delay: 0.3,
          clearProps: "filter",
        });
        gsap.from(q("[data-piece]"), {
          opacity: 0,
          y: 28,
          scale: 0.95,
          duration: 1.25,
          stagger: { each: 0.06, from: "center" },
          delay: 0.08,
        });
        // A pen stroke underlines "road." once the headline has landed.
        const scribble = q("[data-scribble]")[0] as unknown as SVGPathElement | undefined;
        if (scribble) {
          const len = scribble.getTotalLength();
          gsap.fromTo(scribble, { strokeDasharray: len, strokeDashoffset: len }, { strokeDashoffset: 0, duration: 0.95, ease: "power2.inOut", delay: 1.15 });
        }
        // The centre stamp fades in where it rests.
        gsap.from(q("[data-center-fig]"), { opacity: 0, filter: "blur(8px)", duration: 1, delay: 0.1, clearProps: "filter" });
        // Once the album has settled, her notes write themselves in; the hint's arrow is the last stroke.
        // Only behind the first-visit intro: otherwise the notes are already on screen before the
        // page wakes up, and un-writing them to write them again would flicker.
        if (!introPlays) return;
        q("[data-written]").forEach((el, i) => {
          const pen = el.hasAttribute("data-pen");
          if (pen) gsap.set(el, { "--pen": 0 });
          const tl = writeIn(el as HTMLElement, { delay: 1.35 + i * 0.5, trigger: false });
          if (pen) tl?.to(el, { "--pen": 1, duration: 0.45, ease: "power1.inOut" });
        });
      });

      // depth: as the hero scrolls away its pieces drift at their own speeds; all of them stay
      depthDrift(root.current, q("[data-depth]") as HTMLElement[]);

      return () => stopWaiting();
    },
    { scope: root },
  );

  const frame = frames[i];
  const anokhiMark = projects[0].stamps[2];
  const nivrittiSign = projects[1].stamps[0];

  return (
    <section ref={root} className={styles.hero} {...ground("hero")} aria-labelledby="hero-title">
      <div className={styles.stage}>
        <div className={styles.copy}>
          <h1 id="hero-title" className={`display ${styles.title}`} data-title>
            {site.headline[0]} <em>{site.headline[1]}</em> {site.headline[2]}{" "}
            <em className={styles.road}>
              {site.headline[3]}
              <svg className={styles.scribble} viewBox="0 0 220 24" aria-hidden="true">
                <path data-scribble d="M4 15c30-7 64-9 98-8 40 1 74 5 112-3M18 20c44-5 98-6 160-2" />
              </svg>
            </em>
          </h1>
          <div className={styles.sub}>
            <p data-arrive>
              Studio Kavalu is a branding and content house in {site.city}. We shape brands, feeds and persona through a
              design lens, backed with strategy.
            </p>
            <div className={styles.ctas} data-arrive>
              <StartLink className={styles.primary}>Start a project</StartLink>
              <Link href="/work" className={styles.secondary}>
                See the work
              </Link>
            </div>
          </div>
        </div>

        <div className={styles.album}>
          {/* the plum twin, a beat behind the colour stamp */}
          <div className={styles.twin} data-piece data-depth="0.3" aria-hidden="true">
            <div className={styles.tilt} style={tilt(-7)}>
              <div className={styles.perf}>
                <div className={styles.window}>
                  <Image src={frame.image.src} alt="" width={frame.image.w} height={frame.image.h} sizes="300px" className={styles.duo} loading="eager" />
                </div>
              </div>
            </div>
          </div>

          <figure
            className={styles.center}
            data-center-fig
            onPointerEnter={() => setHeld(true)}
            onPointerLeave={() => setHeld(false)}
            onFocus={() => setHeld(true)}
            onBlur={() => setHeld(false)}
          >
            <div className={styles.tilt} style={tilt(-1.5)}>
              <div className={styles.perf}>
                <div className={styles.window} data-center>
                  {frames.map((f, k) => (
                    <Image
                      key={f.image.src + k}
                      src={f.image.src}
                      alt={k === i ? f.image.alt : ""}
                      aria-hidden={k !== i}
                      width={f.image.w}
                      height={f.image.h}
                      sizes="320px"
                      fetchPriority={k === firstIndex ? "high" : "low"}
                      loading="eager"
                      className={styles.frame}
                      data-on={k === i}
                    />
                  ))}
                </div>
              </div>
              <figcaption className={styles.label}>
                <Link href={`/work/${frame.project.slug}`} className={styles.labelLink}>
                  <span className={styles.fig}>fig. {String(i + 1).padStart(2, "0")}</span>
                  <span className={styles.figTitle}>{frame.project.title}</span>
                  <span aria-hidden="true">→</span>
                </Link>
                {!reduced ? (
                  <button
                    type="button"
                    className={styles.pause}
                    onClick={() => setPaused((p) => !p)}
                    aria-pressed={paused}
                    aria-label={paused ? "Play the flip-book" : "Pause the flip-book"}
                  >
                    {paused ? "▶" : "❚❚"}
                  </button>
                ) : null}
              </figcaption>
            </div>
            <span className={`hand ${styles.hint}`} aria-hidden="true" data-depth="0.15" data-written data-pen>
              hover to stop on one
            </span>
          </figure>

          <div className={styles.sat1} data-piece data-depth="0.6">
            <div className={styles.tilt} style={tilt(-9)}>
              <div className={`${styles.perf} ${styles.perfBlue}`}>
                <div className={styles.window} style={{ aspectRatio: "4 / 5" }}>
                  <Image src={anokhiMark.src} alt={anokhiMark.alt} width={anokhiMark.w} height={anokhiMark.h} sizes="140px" loading="eager" />
                </div>
              </div>
            </div>
          </div>

          <div className={styles.polaroid} data-piece data-depth="0.5">
            <div className={styles.tilt} style={tilt(6)}>
              <PaperClip className={styles.clip} />
              <div className={styles.polaroidImg}>
                <Image src={nivrittiSign.src} alt={nivrittiSign.alt} width={nivrittiSign.w} height={nivrittiSign.h} sizes="240px" loading="eager" />
              </div>
              <span className={`hand ${styles.polaroidNote}`} data-written>
                Nivritti, 2023
              </span>
            </div>
          </div>

          <div className={styles.definition} data-piece data-depth="0.4">
            <div className={styles.tilt} style={tilt(-3)}>
              <div className={styles.defCard}>
                <p className={styles.defWord}>
                  <span lang="kn" className="kn">
                    {site.word}
                  </span>
                  <span className={styles.defSay}>/{site.say}/</span>
                </p>
                <p className={styles.defText}>
                  <i>n.</i> {site.definition}
                </p>
              </div>
            </div>
          </div>

          <div className={styles.sticker} data-piece data-depth="0.7">
            <div className={styles.tilt} style={tilt(12)}>
              <Sticker text={`${site.name} · ${site.kannada} · ${site.city} · `} size={128} tone="blue">
                <span style={{ fontFamily: "var(--f-sign)", fontSize: 40, lineHeight: 1 }}>{site.byline}</span>
              </Sticker>
            </div>
          </div>
        </div>

        <p className={styles.cue} aria-hidden="true">
          <span>Scroll</span>
          <span className={styles.cueLine} />
          <span>choose a road</span>
        </p>

      </div>
    </section>
  );
}
