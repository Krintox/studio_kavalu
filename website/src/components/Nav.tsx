"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { useEffect, useRef, useState } from "react";
import { useLenis } from "@/components/motion/SmoothScroll";
import { site } from "@/content/site";
import { Clock } from "./Clock";
import { Logo } from "./Logo";
import { StartLink } from "./onboarding/OnboardingContext";
import styles from "./Nav.module.css";

const links = [
  { href: "/work", label: "Work" },
  { href: "/studio", label: "Studio" },
];

const tabs = [
  { href: "/", label: "Home", note: "The crossroads", c: "var(--cream)" },
  { href: "/work", label: "Work", note: "Every project", c: "var(--blue)" },
  { href: "/studio", label: "Studio", note: "Ananya & the roads", c: "var(--cream-2)" },
];

export function Nav() {
  const pathname = usePathname();
  const [hidden, setHidden] = useState(false);
  const [solid, setSolid] = useState(false);
  const [tone, setTone] = useState<"light" | "dark">("light");
  const [ground, setGround] = useState("cream");
  const [open, setOpen] = useState(false);
  const last = useRef(0);
  const away = useRef(false);
  const sheet = useRef<HTMLDivElement>(null);
  const lenis = useLenis();

  // Hide on the way down, return on the way up; read the colour of whatever sits under the bar.
  useEffect(() => {
    let raf = 0;
    const read = () => {
      raf = 0;
      const y = window.scrollY;
      const delta = y - last.current;
      if (Math.abs(delta) > 6) {
        away.current = delta > 0 && y > 160;
        setHidden(away.current);
        last.current = y;
      }
      setSolid(y > 24);
      // while the bar is tucked away there is nothing to colour, so skip the hit test (it forces a layout
      // on every frame of the scroll); the ground is read again the moment the bar comes back
      if (away.current) return;
      const under = document
        .elementsFromPoint(window.innerWidth / 2, 30)
        .find((el) => !el.closest("[data-nav]") && el.closest("[data-tone]"));
      const t = under?.closest("[data-tone]")?.getAttribute("data-tone");
      setTone(t === "dark" ? "dark" : "light");
      // the solid bar takes the colour of the ground it sits on (styles/surfaces.css)
      setGround(under?.closest("[data-surface]")?.getAttribute("data-surface") ?? "cream");
    };
    const onScroll = () => {
      if (!raf) raf = requestAnimationFrame(read);
    };
    read();
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => {
      window.removeEventListener("scroll", onScroll);
      cancelAnimationFrame(raf);
    };
  }, [pathname]);

  useEffect(() => setOpen(false), [pathname]);

  // While the menu is open: pause the page behind, keep the keyboard inside, and hand focus back on
  // close (the same contract as the onboarding drawer).
  useEffect(() => {
    if (!open) return;
    const opener = document.activeElement as HTMLElement | null;
    lenis?.stop();
    const t = window.setTimeout(() => sheet.current?.querySelector<HTMLElement>("a[href]")?.focus(), 60);
    const onKey = (e: KeyboardEvent) => {
      if (e.key === "Escape") setOpen(false);
      if (e.key !== "Tab" || !sheet.current) return;
      const focusables = sheet.current.querySelectorAll<HTMLElement>("a[href], button:not([disabled])");
      if (!focusables.length) return;
      const first = focusables[0];
      const last = focusables[focusables.length - 1];
      if (e.shiftKey && document.activeElement === first) {
        e.preventDefault();
        last.focus();
      } else if (!e.shiftKey && document.activeElement === last) {
        e.preventDefault();
        first.focus();
      }
    };
    window.addEventListener("keydown", onKey);
    return () => {
      window.clearTimeout(t);
      window.removeEventListener("keydown", onKey);
      lenis?.start();
      opener?.focus?.();
    };
  }, [open, lenis]);

  const current = (href: string) => (href === "/" ? pathname === "/" : pathname.startsWith(href));

  return (
    <>
      <header
        className={styles.nav}
        style={{ viewTransitionName: "site-header" }}
        data-nav
        data-hidden={hidden && !open}
        data-solid={solid}
        data-tone={tone}
        data-ground={ground}
      >
        <Link href="/" className={styles.logo} aria-label="Studio Kavalu, home">
          <Logo />
        </Link>
        <nav aria-label="Main" className={styles.links}>
          {links.map((l) => (
            <Link
              key={l.href}
              href={l.href}
              className={styles.link}
              aria-current={current(l.href) ? "page" : undefined}
            >
              {l.label}
            </Link>
          ))}
        </nav>
        <div className={styles.right}>
          <Clock className={styles.clock} />
          <StartLink className={styles.cta}>
            <span className={styles.ctaDot} aria-hidden="true" />
            <span>
              Start <span className={styles.ctaLong}>a project</span>
            </span>
          </StartLink>
          <button
            type="button"
            className={styles.menuButton}
            aria-expanded={open}
            aria-controls="menu-sheet"
            onClick={() => setOpen(true)}
          >
            Menu
          </button>
        </div>
      </header>

      <div
        ref={sheet}
        id="menu-sheet"
        className={styles.sheet}
        data-open={open}
        role="dialog"
        aria-modal="true"
        aria-label="Menu"
        inert={!open}
        onClick={(e) => e.target === e.currentTarget && setOpen(false)}
      >
        <button type="button" className={styles.close} onClick={() => setOpen(false)}>
          Close
        </button>
        <nav className={styles.tabs} aria-label="Menu">
          {tabs.map((t) => (
            <div key={t.href} className={styles.tab} style={{ ["--c" as string]: t.c }}>
              <Link href={t.href} aria-current={current(t.href) ? "page" : undefined}>
                {t.label}
                <small>{t.note}</small>
              </Link>
            </div>
          ))}
          <div className={styles.tabFoot}>
            <a href={`mailto:${site.email}`}>
              {site.email}
            </a>
            <Clock />
          </div>
        </nav>
      </div>
    </>
  );
}
