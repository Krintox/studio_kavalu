"use client";

import Image from "next/image";
import Link from "next/link";
import { useRef, useState, ViewTransition, type CSSProperties, type ReactNode } from "react";
import { PaperClip } from "@/components/Ephemera";
import { StartLink } from "@/components/onboarding/OnboardingContext";
import { services } from "@/content/site";
import type { Block, Img, Project } from "@/content/types";
import { gsap, prefersReducedMotion, useGSAP } from "@/lib/gsap";
import { ground, sheet } from "@/lib/surfaces";
import { typeIn, writeIn } from "@/lib/handmade";
import { imageDrift } from "@/lib/parallax";
import styles from "./CaseStudy.module.css";

type Mount = "tape" | "corners" | "clip" | "none";

/*
 * Every picture is mounted on the page the way it would be in a scrapbook: taped, cornered or clipped,
 * at a slight tilt. Full-bleed real photographs stay straight and edge to edge (the work needs room),
 * and keep only a strip of tape at the top.
 */
function Picture({
  image,
  size,
  sizes,
  mount = "tape",
  tilt = 0,
}: {
  image: Img;
  size: "full" | "wide" | "inset" | "half";
  sizes: string;
  mount?: Mount;
  tilt?: number;
}) {
  const bleed = size === "full" && !image.placeholder;
  const cls = [styles.picture, styles[`size_${size}`], image.placeholder ? styles.isPlaceholder : "", styles[`mount_${mount}`]].join(" ");
  return (
    <figure className={cls} style={{ ["--tilt" as string]: `${bleed ? 0 : tilt}deg` } as CSSProperties}>
      {mount === "clip" ? <PaperClip className={styles.clip} /> : null}
      <div className={styles.frame} data-reveal style={{ aspectRatio: `${image.w} / ${image.h}`, background: image.tone } as CSSProperties}>
        <Image src={image.src} alt={image.alt} width={image.w} height={image.h} sizes={sizes} />
      </div>
    </figure>
  );
}

/** A typed caption on a strip of paper, as you would stick under a print. It types on as it arrives. */
function Label({ children }: { children: ReactNode }) {
  return (
    <p className={styles.caption} data-typed>
      {children}
    </p>
  );
}

function Palette({ colors, heading }: { colors: { name: string; hex: string }[]; heading?: string }) {
  const [copied, setCopied] = useState("");
  const copy = async (hex: string) => {
    try {
      await navigator.clipboard.writeText(hex);
      setCopied(hex);
      window.setTimeout(() => setCopied(""), 1400);
    } catch {
      /* clipboard unavailable */
    }
  };
  return (
    <section className={`container ${styles.palette}`}>
      {heading ? <p className="eyebrow">{heading}</p> : null}
      <ul className={styles.chips}>
        {colors.map((c, k) => (
          <li key={c.hex} style={{ ["--tilt" as string]: `${[-2, 1.5, -1, 2.5, -1.5, 1][k % 6]}deg` }}>
            <button type="button" className={styles.chip} onClick={() => copy(c.hex)} aria-label={`${c.name}, ${c.hex}. Copy the hex code`}>
              <span className={styles.chipColour} style={{ background: c.hex }} />
              <span className={styles.chipName}>{c.name}</span>
              <span className={styles.chipHex} aria-live="polite">
                {copied === c.hex ? "copied" : c.hex}
              </span>
            </button>
          </li>
        ))}
      </ul>
    </section>
  );
}

// mounts and tilts cycle through the page so no two neighbouring prints are held the same way
const MOUNTS: Mount[] = ["tape", "corners", "clip", "tape", "corners"];
const TILTS = [-0.8, 0.9, -0.5, 1.1, -1];

function BlockView({ block, n }: { block: Block; n: number }) {
  switch (block.type) {
    case "text":
      return (
        <section className={`container ${styles.text}`} {...sheet("caseText")}>
          {block.eyebrow ? <h2 className={styles.textHead}>{block.eyebrow}</h2> : null}
          <div className={styles.textBody}>
            {block.heading ? <p className={styles.textLead}>{block.heading}</p> : null}
            {block.body.map((p) => (
              <p key={p.slice(0, 24)}>{p}</p>
            ))}
          </div>
        </section>
      );
    case "image":
      return (
        <section className={block.size === "full" && !block.image.placeholder ? styles.bleed : "container"}>
          <Picture
            image={block.image}
            size={block.size}
            sizes={block.size === "full" ? "100vw" : "(max-width: 900px) 100vw, 70vw"}
            mount={MOUNTS[n % MOUNTS.length]}
            tilt={TILTS[n % TILTS.length]}
          />
          {block.caption ? <Label>{block.caption}</Label> : null}
        </section>
      );
    case "pair":
      return (
        <section className={`container ${styles.pair}`}>
          <Picture image={block.images[0]} size="half" sizes="(max-width: 900px) 100vw, 45vw" mount={MOUNTS[n % MOUNTS.length]} tilt={TILTS[n % TILTS.length]} />
          <Picture
            image={block.images[1]}
            size="half"
            sizes="(max-width: 900px) 100vw, 45vw"
            mount={MOUNTS[(n + 2) % MOUNTS.length]}
            tilt={-TILTS[(n + 1) % TILTS.length]}
          />
          {block.caption ? <Label>{block.caption}</Label> : null}
        </section>
      );
    case "stamps":
      return (
        <section className={`container ${styles.stampGrid}`}>
          {block.images.map((im) => (
            <span key={im.src} className={styles.stamp} data-reveal>
              <span className={styles.stampWindow}>
                <Image src={im.src} alt={im.alt} width={im.w} height={im.h} sizes="25vw" />
              </span>
            </span>
          ))}
        </section>
      );
    case "palette":
      return <Palette colors={block.colors} heading={block.heading} />;
    case "note":
      return (
        <aside className={`container ${styles.noteWrap}`}>
          <p className={`hand ${styles.note}`} data-written>
            {block.text}
            {block.by ? <span className={styles.noteBy}> — {block.by}</span> : null}
          </p>
        </aside>
      );
    case "quote":
      return (
        <blockquote className={`container ${styles.quote}`}>
          <p>{block.text}</p>
          {block.by ? <footer>{block.by}</footer> : null}
        </blockquote>
      );
  }
}

// A project's own colours open its case study and the "next road" band: they are its content, like its
// photographs (brief 5's "remaining rest"; BRAND_DESIGN.md §4.4).
const own = (pr: Project) => ({ "--p-bg": pr.tone.bg, "--p-ink": pr.tone.ink }) as CSSProperties;

export function CaseStudy({ project: p, next }: { project: Project; next: Project }) {
  const root = useRef<HTMLElement>(null);
  const firstRoad = p.services[0];
  const roadTitle = services.find((s) => s.key === firstRoad)?.title.toLowerCase();

  useGSAP(
    () => {
      if (prefersReducedMotion()) return;
      // A real cover opens from an inset frame to the full width as you start reading.
      if (!p.cover.placeholder) {
        gsap.fromTo(
          "[data-cover]",
          { clipPath: "inset(0% 9% 0% 9% round 6px)" },
          {
            clipPath: "inset(0% 0% 0% 0% round 0px)",
            ease: "none",
            scrollTrigger: { trigger: "[data-cover-wrap]", start: "top 85%", end: "top 15%", scrub: 0.6 },
          },
        );
        gsap.fromTo("[data-cover] img", { scale: 1.18 }, { scale: 1, ease: "none", scrollTrigger: { trigger: "[data-cover-wrap]", start: "top bottom", end: "bottom top", scrub: true } });
      } else {
        gsap.from("[data-cover]", { y: 60, rotation: -3, opacity: 0, duration: 1.2, delay: 0.25 });
      }
      // Pictures are uncovered as they arrive; the words are simply there.
      gsap.utils.toArray<HTMLElement>("[data-reveal]", root.current).forEach((el) => {
        gsap.fromTo(
          el,
          { clipPath: "inset(14% 10% 14% 10%)" },
          { clipPath: "inset(0% 0% 0% 0%)", duration: 1.2, ease: "travel", scrollTrigger: { trigger: el, start: "top 88%" } },
        );
        // the picture settles a little larger than its window, which leaves room for it to drift
        const img = el.querySelector("img");
        if (img) gsap.fromTo(img, { scale: 1.2 }, { scale: 1.09, duration: 1.6, ease: "settle", scrollTrigger: { trigger: el, start: "top 88%" } });
      });
      imageDrift(gsap.utils.toArray<HTMLElement>("[data-reveal]", root.current));
      // captions type on once their print has been uncovered; hand notes write themselves in
      gsap.utils.toArray<HTMLElement>("[data-typed]", root.current).forEach((el) => typeIn(el, { delay: 0.55 }));
      gsap.utils.toArray<HTMLElement>("[data-written]", root.current).forEach((el) => writeIn(el));
    },
    { scope: root },
  );

  return (
    <article ref={root} className={styles.case} {...ground("case")}>
      <header className={`${styles.hero} ${styles.projectGround}`} style={own(p)} data-section="caseHero" data-tone="dark">
        <div className="container">
          <p className={styles.crumb}>
            <Link href="/work">
              Work
            </Link>{" "}
            / {p.title}
          </p>
          <h1 className={styles.title}>{p.title}</h1>
          <dl className={styles.meta}>
            {p.client ? (
              <div>
                <dt>Client</dt>
                <dd>{p.client}</dd>
              </div>
            ) : null}
            {p.year ? (
              <div>
                <dt>Year</dt>
                <dd>{p.year}</dd>
              </div>
            ) : null}
            <div>
              <dt>Sector</dt>
              <dd>
                {p.sector}
                {p.city ? `, ${p.city}` : ""}
              </dd>
            </div>
            <div>
              <dt>Services</dt>
              <dd>{p.deliverables.join(", ")}</dd>
            </div>
          </dl>
        </div>
        <div className={`${styles.coverWrap} ${p.cover.placeholder ? styles.coverSmall : ""}`} data-cover-wrap>
          <ViewTransition name={`cover-${p.slug}`} share="morph" default="none">
            <div className={styles.cover} data-cover>
              <Image src={p.cover.src} alt={p.cover.alt} width={p.cover.w} height={p.cover.h} sizes={p.cover.placeholder ? "520px" : "100vw"} preload />
            </div>
          </ViewTransition>
        </div>
      </header>

      {p.overview ? (
        <section className={`container ${styles.overviewWrap}`}>
          <div className={styles.overview}>
            <PaperClip className={styles.overviewClip} />
            <p className={styles.overviewLabel}>Overview</p>
            <p className={styles.overviewText}>{p.overview}</p>
          </div>
        </section>
      ) : (
        <section className={`container ${styles.overviewWrap}`}>
          <p className={styles.summary}>{p.summary}</p>
        </section>
      )}

      {p.blocks.map((b, k) => (
        <BlockView key={k} block={b} n={k} />
      ))}

      {p.kind === "snapshot" ? (
        <section className={`container ${styles.stampGrid}`}>
          {p.stamps.map((im) => (
            <span key={im.src} className={styles.stamp} data-reveal>
              <span className={styles.stampWindow}>
                <Image src={im.src} alt={im.alt} width={im.w} height={im.h} sizes="30vw" />
              </span>
            </span>
          ))}
        </section>
      ) : null}

      <section className={`container ${styles.cta}`}>
        <p className={styles.ctaText}>
          Building something {roadTitle ? <>that needs {roadTitle}</> : "similar"}?
        </p>
        <StartLink road={firstRoad} from={p.slug} className={styles.ctaButton}>
          Start a project like {p.title} <span aria-hidden="true">→</span>
        </StartLink>
      </section>

      <nav className={`${styles.next} ${styles.projectGround}`} style={own(next)} aria-label="Next project" data-section="caseNext" data-tone="dark">
        <Link href={`/work/${next.slug}`} className={styles.nextLink} data-cursor="view" data-cursor-label="Next">
          <span className={styles.nextLabel}>Next road</span>
          <span className={styles.nextTitle}>{next.title}</span>
          <ViewTransition name={`cover-${next.slug}`} share="morph" default="none">
            <span className={styles.nextStamp}>
              <span className={styles.stampWindow}>
                <Image src={next.cover.src} alt="" width={next.cover.w} height={next.cover.h} sizes="300px" />
              </span>
            </span>
          </ViewTransition>
        </Link>
      </nav>
    </article>
  );
}
