"use client";

import Image from "next/image";
import Link from "next/link";
import { memo, useEffect, useMemo, useRef, useState, type CSSProperties } from "react";
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
// the reel behind the hero changes slowly: atmosphere, not a second flip-book
const REEL_MS = 3400;
// A picture re-renders only when its own props change. The flip-book ticks every 420 ms, and the scroll
// scene and the reel change state too; without this, every picture on the page re-rendered each time.
const Still = memo(Image);
const tilt = (deg: number) => ({ "--tilt": `${deg}deg` }) as CSSProperties;

/*
 * Every piece on the album page has three layers: the outer one arrives (opacity only, so nothing it
 * does moves the layout the scroll scene measures), the middle one is moved by the scroll scene and the
 * mobile parallax, and the inner one keeps its paper tilt in a CSS variable. Keeping them apart means
 * scroll motion never fights the resting angle, and the page still looks right with JavaScript off.
 *
 * The scroll scene (desktop, brief 6): the headline lifts away, every picture on the page glides into
 * the centre stamp, the stamp straightens and opens to the full screen, and the picture dissolves into
 * the powder blue of the first project spread, which deals its prints out of it. It is scrubbed to the
 * scroll, so scrolling back up plays it backwards and the whole collage scatters back.
 */
export function Hero() {
  const root = useRef<HTMLElement>(null);
  const frames = useMemo(() => allStamps(), []);
  // the faint reel behind the hero: one picture from each project in turn, then the rest
  const reel = useMemo(() => frames.slice(0, 12), [frames]);
  const first = featured[0];
  const firstIndex = Math.max(
    0,
    frames.findIndex((f) => f.project.slug === first.slug),
  );
  const [i, setI] = useState(firstIndex);
  const [r, setR] = useState(0);
  const [paused, setPaused] = useState(false);
  const [held, setHeld] = useState(false);
  const [moving, setMoving] = useState(false);
  const [inView, setInView] = useState(true);
  const [reduced, setReduced] = useState(false);
  // behind the intro the flip-book holds on the picture the intro lands on
  const [introDone, setIntroDone] = useState(false);
  const { open: drawerOpen } = useOnboarding();

  useEffect(() => setReduced(prefersReducedMotion()), []);
  useEffect(() => afterIntro(() => setIntroDone(true)), []);
  // the scene opens the first project's cover (a full-resolution picture) whatever the flip-book showed
  useEffect(() => {
    if (moving) setI(firstIndex);
  }, [moving, firstIndex]);

  // The flip-book only runs while it can be seen and isn't held, scrolled into its scene or paused.
  const still = paused || held || moving || !inView || reduced || drawerOpen || !introDone;
  useEffect(() => {
    if (still) return;
    const id = window.setInterval(() => setI((v) => (v + 1) % frames.length), FRAME_MS);
    return () => window.clearInterval(id);
  }, [still, frames.length]);

  // The reel behind keeps its own slow time, and stops with the flip-book's pause button (WCAG 2.2.2).
  useEffect(() => {
    if (paused || moving || !inView || reduced || drawerOpen) return;
    const id = window.setInterval(() => setR((v) => (v + 1) % reel.length), REEL_MS);
    return () => window.clearInterval(id);
  }, [paused, moving, inView, reduced, drawerOpen, reel.length]);

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
      const introPlays = document.documentElement.dataset.intro === "play";

      // Arrival: lines rise out of their masks, the album's pieces come up round the centre stamp (after
      // the intro, which hands over onto that very stamp).
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
          filter: "blur(8px)",
          duration: 1.2,
          stagger: { each: 0.07, from: "center" },
          delay: 0.08,
          ease: "settle",
          clearProps: "filter",
        });
        // A pen stroke underlines "road." once the headline has landed.
        const scribble = q("[data-scribble]")[0] as unknown as SVGPathElement | undefined;
        if (scribble) {
          const len = scribble.getTotalLength();
          gsap.fromTo(scribble, { strokeDasharray: len, strokeDashoffset: len }, { strokeDashoffset: 0, duration: 0.95, ease: "power2.inOut", delay: 1.15 });
        }
        // The centre stamp comes up first, where it rests; the rest of the album gathers round it.
        gsap.from(q("[data-center-fig]"), { opacity: 0, filter: "blur(8px)", duration: 1, delay: 0.05, clearProps: "filter" });
        // Once the album has settled, her notes write themselves in; the hint's arrow is the last stroke.
        // Only behind the intro: otherwise the notes are already on screen before the page wakes up.
        if (!introPlays) return;
        q("[data-written]").forEach((el, k) => {
          const pen = el.hasAttribute("data-pen");
          if (pen) gsap.set(el, { "--pen": 0 });
          const tl = writeIn(el as HTMLElement, { delay: 1.35 + k * 0.5, trigger: false });
          if (pen) tl?.to(el, { "--pen": 1, duration: 0.45, ease: "power1.inOut" });
        });
      });

      const mm = gsap.matchMedia();

      // ---------- the scroll scene (desktop) ----------
      mm.add("(min-width: 900px)", () => {
        const stage = q("[data-stage]")[0] as HTMLElement;
        const tiltEl = q("[data-center-tilt]")[0] as HTMLElement;
        const win = q("[data-center]")[0] as HTMLElement;
        const plate = q("[data-plate]")[0] as HTMLElement;
        const plateImg = q("[data-plate-img]")[0] as HTMLElement;
        const merges = q("[data-merge]") as HTMLElement[];

        // The picture window as it rests, untilted, relative to the stage.
        const box = () => {
          const prev = tiltEl.style.getPropertyValue("--tilt");
          tiltEl.style.setProperty("--tilt", "0deg");
          const s = stage.getBoundingClientRect();
          const w = win.getBoundingClientRect();
          tiltEl.style.setProperty("--tilt", prev);
          return { l: w.left - s.left, t: w.top - s.top, w: w.width, h: w.height };
        };
        // How far a piece must travel for its centre to sit on the window's centre. The piece's own scene
        // offset is taken out, so a refresh in the middle of the scene still measures from its rest.
        const toCentre = (el: HTMLElement, axis: "x" | "y") => {
          const s = stage.getBoundingClientRect();
          const b = box();
          const rect = el.getBoundingClientRect();
          const at = axis === "x" ? rect.left + rect.width / 2 : rect.top + rect.height / 2;
          const own = Number(gsap.getProperty(el, axis)) || 0;
          const target = axis === "x" ? s.left + b.l + b.w / 2 : s.top + b.t + b.h / 2;
          return target - (at - own);
        };

        const tl = gsap.timeline({
          defaults: { ease: "none" },
          scrollTrigger: {
            trigger: root.current,
            start: "top top",
            end: "+=150%",
            pin: true,
            anticipatePin: 1,
            // a long scrub: the scene trails the scroll by about a second, so it glides however the
            // wheel or trackpad moves
            scrub: 1,
            invalidateOnRefresh: true,
            // work out every piece's path whenever the page is measured, not on the first frame of the
            // scroll (traced: 30 ms of measuring in one frame); playing the scene to its end and back
            // computes them all while nothing is moving
            onRefresh: (self) => self.animation?.progress(1).progress(self.progress),
            onUpdate: (self) => setMoving(self.progress > 0.01),
          },
        });

        tl.to(q("[data-lift]"), { y: -80, opacity: 0, duration: 0.26, ease: "power2.in" }, 0)
          .to(q("[data-cue], [data-reel]"), { opacity: 0, duration: 0.2, ease: "power1.in" }, 0)
          .to(tiltEl, { "--tilt": "0deg", duration: 0.24, ease: "power1.inOut" }, 0)
          .to(q("[data-center-label], [data-hint]"), { opacity: 0, duration: 0.14 }, 0)
          // every picture glides into the centre stamp, shrinking and straightening as it tucks in
          .to(
            merges,
            {
              x: (_: number, el: HTMLElement) => toCentre(el, "x"),
              y: (_: number, el: HTMLElement) => toCentre(el, "y"),
              scale: 0.42,
              rotation: 0,
              duration: 0.4,
              ease: "power3.inOut",
              stagger: 0.012,
            },
            0.03,
          )
          .to(merges, { opacity: 0, duration: 0.09, ease: "power1.in", stagger: 0.012 }, 0.33)
          // the stamp's picture takes over from the stamp and opens to the whole screen
          .set(plateImg, { left: () => box().l, top: () => box().t, width: () => box().w, height: () => box().h, opacity: 1 }, 0)
          .set(plate, { autoAlpha: 1 }, 0.46)
          .set(q("[data-center-fig]"), { autoAlpha: 0 }, 0.46)
          .to(
            plateImg,
            { left: 0, top: 0, width: () => stage.clientWidth, height: () => stage.clientHeight, duration: 0.38, ease: "power2.inOut" },
            0.46,
          )
          .to(q("[data-plate-ground]"), { opacity: 1, duration: 0.1 }, 0.8)
          // and dissolves into the first spread's blue paper, out of which the spread deals its prints
          .to(plateImg, { opacity: 0, duration: 0.14, ease: "power1.inOut" }, 0.86);
      });

      // ---------- phones: no pin; the pieces drift at their own depths as the hero scrolls away ----------
      mm.add("(max-width: 899px)", () => {
        depthDrift(root.current, q("[data-depth]") as HTMLElement[]);
      });

      return () => {
        stopWaiting();
        mm.revert();
      };
    },
    { scope: root },
  );

  const frame = frames[i];
  const anokhiMark = projects[0].stamps[2];
  const nivrittiSign = projects[1].stamps[0];

  return (
    <section ref={root} className={styles.hero} {...ground("hero")} aria-labelledby="hero-title">
      <div className={styles.stage} data-stage>
        {/* her work, very faint and slow, behind everything: the intro's reel settles into it */}
        <div className={styles.reel} data-reel aria-hidden="true">
          {reel.map((f, k) => {
            // only the picture fading out, the one showing and the next (already loading) are mounted;
            // at 9% opacity half the screen's resolution is plenty
            const n = reel.length;
            if (k !== r && k !== (r + 1) % n && k !== (r - 1 + n) % n) return null;
            return (
              <Still
                key={f.image.src + k}
                src={f.image.src}
                alt=""
                width={f.image.w}
                height={f.image.h}
                sizes="50vw"
                quality={55}
                className={styles.reelFrame}
                data-on={k === r}
              />
            );
          })}
        </div>

        <div className={styles.copy} data-lift>
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
            <div className={styles.merge} data-merge>
              <div className={styles.tilt} style={tilt(-7)}>
                <div className={styles.perf}>
                  <div className={styles.window}>
                    <Still src={frame.image.src} alt="" width={frame.image.w} height={frame.image.h} sizes="300px" className={styles.duo} loading="eager" />
                  </div>
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
            <div className={styles.tilt} style={tilt(-1.5)} data-center-tilt>
              <div className={styles.perf}>
                <div className={styles.window} data-center>
                  {frames.map((f, k) => (
                    <Still
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
              <figcaption className={styles.label} data-center-label>
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
            <span className={`hand ${styles.hint}`} aria-hidden="true" data-depth="0.15" data-hint data-written data-pen>
              hover to stop on one
            </span>
          </figure>

          <div className={styles.sat1} data-piece data-depth="0.6">
            <div className={styles.merge} data-merge>
              <div className={styles.tilt} style={tilt(-9)}>
                <div className={`${styles.perf} ${styles.perfBlue}`}>
                  <div className={styles.window} style={{ aspectRatio: "4 / 5" }}>
                    <Still src={anokhiMark.src} alt={anokhiMark.alt} width={anokhiMark.w} height={anokhiMark.h} sizes="140px" loading="eager" />
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div className={styles.polaroid} data-piece data-depth="0.5">
            <div className={styles.merge} data-merge>
              <div className={styles.tilt} style={tilt(6)}>
                <PaperClip className={styles.clip} />
                <div className={styles.polaroidImg}>
                  <Still src={nivrittiSign.src} alt={nivrittiSign.alt} width={nivrittiSign.w} height={nivrittiSign.h} sizes="240px" loading="eager" />
                </div>
                <span className={`hand ${styles.polaroidNote}`} data-written>
                  Nivritti, 2023
                </span>
              </div>
            </div>
          </div>

          <div className={styles.definition} data-piece data-depth="0.4">
            <div className={styles.merge} data-merge>
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
          </div>

          <div className={styles.sticker} data-piece data-depth="0.7">
            <div className={styles.merge} data-merge>
              <div className={styles.tilt} style={tilt(12)}>
                <Sticker text={`${site.name} · ${site.kannada} · ${site.city} · `} size={128} tone="blue">
                  <span style={{ fontFamily: "var(--f-sign)", fontSize: 40, lineHeight: 1 }}>{site.byline}</span>
                </Sticker>
              </div>
            </div>
          </div>
        </div>

        <p className={styles.cue} data-cue aria-hidden="true">
          <span>Scroll</span>
          <span className={styles.cueLine} />
          <span>choose a road</span>
        </p>

        {/* the stamp's picture, opening to the whole screen in the scroll scene */}
        <div className={styles.plate} data-plate aria-hidden="true">
          <div className={styles.plateGround} data-plate-ground />
          <div className={styles.plateImg} data-plate-img>
            <Still src={frame.image.src} alt="" fill sizes="100vw" quality={85} />
          </div>
        </div>
      </div>
    </section>
  );
}
