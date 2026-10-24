"use client";

import Link from "next/link";
import { useRef, useState, type CSSProperties, type ReactNode } from "react";
import { Clock } from "@/components/Clock";
import { Sticker } from "@/components/Ephemera";
import { StartLink } from "@/components/onboarding/OnboardingContext";
import { ScrapPiece } from "@/components/scrapbook/ScrapPiece";
import { deskPins } from "@/content/desk";
import { site } from "@/content/site";
import { Draggable, gsap, prefersReducedMotion, ScrollTrigger, useGSAP } from "@/lib/gsap";
import { writeIn } from "@/lib/handmade";
import styles from "./FooterDesk.module.css";

// The road across the desk (in the board's 1000 × 400 drawing), and the branch that forks off it
// between the ticket and the contact card and runs down to ಕವಲು, "a fork in the road".
const roads = [
  "M120 150 C 220 260, 300 60, 410 170 S 600 280, 690 150 S 840 70, 900 160",
  "M289 147 C 296 220, 340 280, 400 315 S 462 352, 466 382",
];

const pinStyle = (x: number, y: number, r: number) =>
  ({ left: `${x}%`, top: `${y}%`, ["--tilt" as string]: `${r}deg` }) as CSSProperties;

/*
 * One thing on the desk, in four layers: the slot centres it on its spot (CSS only; GSAP never
 * touches it, so the -50% centring can't be rounded away), [data-pin] lands and is dragged,
 * [data-par] leans with the cursor, and the tilt rests at the pin's angle.
 */
function Pin({ className, style, depth, cursor, children }: { className?: string; style: CSSProperties; depth: number; cursor?: string; children: ReactNode }) {
  return (
    <div className={`${styles.pin} ${className ?? ""}`} style={style} data-cursor={cursor}>
      <div data-pin data-depth={depth}>
        <div data-par>
          <div className={styles.tilt} data-tilt>
            {children}
          </div>
        </div>
      </div>
    </div>
  );
}

/*
 * The footer as the last page of the scrapbook: the desk, with the studio's own pins.
 * The three working cards (start, contact, index) are real controls; everything can be nudged around
 * with a mouse, pins lean a little with the cursor (depth), and they pin themselves down when the
 * desk scrolls into view. Touch and reduced motion get the same desk, still.
 */
export function FooterDesk() {
  const root = useRef<HTMLElement>(null);
  const [copied, setCopied] = useState(false);

  const copy = async () => {
    try {
      await navigator.clipboard.writeText(site.email);
      setCopied(true);
      window.setTimeout(() => setCopied(false), 1800);
    } catch {
      window.location.href = `mailto:${site.email}`;
    }
  };

  useGSAP(
    () => {
      const board = root.current?.querySelector<HTMLElement>("[data-board]");
      if (!board) return;
      const slots = gsap.utils.toArray<HTMLElement>("[data-pin]", board);
      const reduce = prefersReducedMotion();

      if (!reduce) {
        // pins land one by one as they come into view, working cards first (on the board they all
        // arrive together; in the stacked layout each card lands as it is reached). In the swipe strip
        // the drop is shorter, so pins don't fall out of its edge.
        const strip = window.matchMedia("(max-width: 1099px)").matches;
        gsap.set(slots, {
          y: (i: number) => (strip ? -22 : -50 - (i % 3) * 18),
          rotation: (i: number) => (i % 2 ? 11 : -9),
          opacity: 0,
        });
        ScrollTrigger.batch(slots, {
          start: "top 88%",
          once: true,
          onEnter: (batch) => gsap.to(batch, { y: 0, rotation: 0, opacity: 1, duration: 1, ease: "settle", stagger: 0.06 }),
        });
        // the postmark presses onto the contact card once the cards are down
        gsap.from("[data-postmark]", {
          scale: 1.45,
          rotation: -32,
          opacity: 0,
          duration: 0.5,
          ease: "back.out(1.6)",
          delay: 0.75,
          scrollTrigger: { trigger: "[data-postmark]", start: "top 88%", once: true },
        });
        // the pencil road draws itself between the cards as the desk comes up, then forks
        // (the masks draw; the dotted roads under them stay dotted)
        const masks = gsap.utils.toArray<SVGPathElement>("[data-road]", board);
        const tl = gsap.timeline({ scrollTrigger: { trigger: board, start: "top 85%", end: "center 45%", scrub: 0.6 } });
        masks.forEach((m, i) => {
          const len = m.getTotalLength();
          tl.fromTo(m, { strokeDasharray: len, strokeDashoffset: len }, { strokeDashoffset: 0, ease: "none", duration: i ? 0.5 : 1 }, i ? 0.55 : 0);
        });
        // her notes write themselves in once their pin is down (the hint last, after the cards)
        gsap.utils.toArray<HTMLElement>("[data-written]", board).forEach((el) =>
          writeIn(el, { delay: el.closest("[data-pin]") ? 0.55 : 1.1 }),
        );
      }

      const mm = gsap.matchMedia();
      mm.add("(pointer: fine) and (min-width: 1100px)", () => {
        let z = 30;
        const drags = Draggable.create(slots, {
          type: "x,y",
          bounds: root.current!,
          inertia: !reduce,
          edgeResistance: 0.75,
          // the controls inside the cards stay clickable; drag from the paper
          dragClickables: false,
          onPress() {
            (this.target as HTMLElement).parentElement!.style.zIndex = String(++z);
            // the piece lifts a little as it is picked up (dragging itself stays, even with reduced motion)
            if (!reduce) gsap.to(this.target.querySelector("[data-tilt]"), { scale: 1.035, duration: 0.25, ease: "power2.out" });
          },
          onRelease() {
            if (!reduce) gsap.to(this.target.querySelector("[data-tilt]"), { scale: 1, duration: 0.5, ease: "settle" });
          },
        });
        if (reduce) return () => drags.forEach((d) => d.kill());

        // cursor depth: each pin's inner layer drifts a few pixels against the cursor
        const layers = slots.map((s) => {
          const el = s.querySelector<HTMLElement>("[data-par]")!;
          const depth = Number(s.dataset.depth || 0.5);
          return { x: gsap.quickTo(el, "x", { duration: 0.9, ease: "power3" }), y: gsap.quickTo(el, "y", { duration: 0.9, ease: "power3" }), depth };
        });
        const onMove = (e: PointerEvent) => {
          const r = board.getBoundingClientRect();
          const nx = (e.clientX - r.left) / r.width - 0.5;
          const ny = (e.clientY - r.top) / r.height - 0.5;
          for (const l of layers) {
            l.x(-nx * 14 * l.depth);
            l.y(-ny * 10 * l.depth);
          }
        };
        const onLeave = () => layers.forEach((l) => (l.x(0), l.y(0)));
        board.addEventListener("pointermove", onMove);
        board.addEventListener("pointerleave", onLeave);
        return () => {
          drags.forEach((d) => d.kill());
          board.removeEventListener("pointermove", onMove);
          board.removeEventListener("pointerleave", onLeave);
        };
      });
      return () => mm.revert();
    },
    { scope: root },
  );

  return (
    <section ref={root} className={`${styles.desk} paper-worn`} aria-labelledby="desk-title">
      <header className={styles.head}>
        <h2 id="desk-title" className={styles.title}>
          What we pin above <em>the desk.</em>
        </h2>
      </header>

      <div className={styles.board} data-board>
        <svg className={styles.road} viewBox="0 0 1000 400" preserveAspectRatio="none" aria-hidden="true">
          <defs>
            {roads.map((d, i) => (
              <mask key={d} id={`desk-road-${i}`} maskUnits="userSpaceOnUse" x="-100" y="-100" width="1200" height="640">
                <path data-road d={d} />
              </mask>
            ))}
          </defs>
          {roads.map((d, i) => (
            <path key={d} className={styles.dots} d={d} mask={`url(#desk-road-${i})`} />
          ))}
        </svg>

        {/* the working cards */}
        <Pin className={styles.ticketPin} depth={0.25} style={pinStyle(17, 31, -2.5)}>
          <div className={styles.ticket}>
            <span className={styles.hole} aria-hidden="true" />
            <p className={styles.ticketKicker}>Admit one · {site.word}</p>
            <p className={styles.ticketTitle}>
              Standing at a <em>crossroads?</em>
            </p>
            <StartLink className={styles.ticketCta}>
              Start a project <span aria-hidden="true">→</span>
            </StartLink>
            <p className={styles.ticketNote}>Five short steps · about three minutes · read by Ananya</p>
          </div>
        </Pin>

        <Pin className={styles.cardPin} depth={0.2} style={pinStyle(48.5, 36, 1.5)}>
          <div className={styles.card}>
            <p className={styles.cardLabel}>Write to the studio</p>
            <button type="button" className={styles.email} onClick={copy} aria-live="polite">
              {copied ? "Copied to clipboard" : site.email}
            </button>
            <dl className={styles.cardMeta}>
              <div>
                <dt>Studio</dt>
                <dd>
                  {site.city}, {site.country}
                </dd>
              </div>
              <div>
                <dt>Local time</dt>
                <dd>
                  <Clock city={false} />
                </dd>
              </div>
              <div>
                <dt>Clients</dt>
                <dd>Worldwide</dd>
              </div>
            </dl>
            <p className={styles.cardLinks}>
              <a href={`mailto:${site.email}`}>Email</a>
              {site.whatsapp ? (
                <a href={`https://wa.me/${site.whatsapp}`} target="_blank" rel="noreferrer">
                  WhatsApp
                </a>
              ) : null}
              {site.instagram ? (
                <a href={`https://instagram.com/${site.instagram}`} target="_blank" rel="noreferrer">
                  Instagram
                </a>
              ) : null}
            </p>
            <div className={styles.postmark} data-postmark aria-hidden="true">
              <svg viewBox="0 0 120 120">
                <defs>
                  <path id="desk-pm" d="M60,60 m-42,0 a42,42 0 1,1 84,0 a42,42 0 1,1 -84,0" />
                </defs>
                <circle cx="60" cy="60" r="54" />
                <circle cx="60" cy="60" r="32" />
                <text>
                  <textPath href="#desk-pm">KAVALU · BENGALURU · INDIA ·</textPath>
                </text>
              </svg>
            </div>
          </div>
        </Pin>

        <Pin className={styles.indexPin} depth={0.3} style={pinStyle(81, 30, -1.5)}>
          <nav className={styles.index} aria-label="Footer">
            <p className={styles.indexTab}>Index</p>
            <ol>
              <li>
                <Link href="/">
                  <span>01</span> Home
                </Link>
              </li>
              <li>
                <Link href="/work">
                  <span>02</span> Work
                </Link>
              </li>
              <li>
                <Link href="/studio">
                  <span>03</span> Studio
                </Link>
              </li>
              <li>
                <StartLink>
                  <span>04</span> Start a project
                </StartLink>
              </li>
            </ol>
          </nav>
        </Pin>

        {/* her pins: scattered on the board; on smaller screens, a strip to swipe through */}
        <div className={styles.pins} role="group" aria-label="Pinned on the desk" data-lenis-prevent-horizontal>
          {deskPins.map((p) => (
            <Pin key={p.item.id} className={styles.deco} depth={p.depth} style={pinStyle(p.x, p.y, p.r)} cursor="drag">
              <ScrapPiece item={p.item} width={p.w || undefined} sizes={`${Math.round((p.w || 160) * 1.5)}px`} />
            </Pin>
          ))}

          <Pin className={styles.deco} depth={0.7} style={pinStyle(36, 6, 10)} cursor="drag">
            <Sticker text={`${site.name} · ${site.kannada} · ${site.city} · `} size={112} tone="blue">
              <span style={{ fontFamily: "var(--f-display)", fontStyle: "italic", fontSize: 30, lineHeight: 1 }}>{site.byline}</span>
            </Sticker>
          </Pin>
        </div>

        <p className={`hand ${styles.hint}`} aria-hidden="true" data-written>
          <span className={styles.hintMove}>go on, move things around</span>
          <span className={styles.hintSwipe}>swipe along the desk →</span>
        </p>
      </div>
    </section>
  );
}
