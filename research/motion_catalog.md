# Studio Kavalu: motion catalog (research, October 2026)

Prepared on 23 October 2026 for the Next.js 16 (App Router) + React 19.3 + GSAP 3.15 + Lenis build of
"Studio Kavalu by Ananya". It sits beside `design_direction.md` (the crossroads album: the road, the stamp
and the folder tab) and turns that direction into techniques you can build: where each one goes, which
demo to study, how to wire it, and how to keep it accessible and fast.

What this document is based on: the component pages and source of React Bits (GitHub source, read 23 Oct),
Aceternity, Magic UI, Motion Primitives, Cult UI, Skiper UI, Animata, 21st.dev and Osmo; Codrops tutorials
and demos from 2023 to 2026, read in full; the GSAP, Lenis, React, Next.js and MDN docs; the npm registry;
and MDN browser-compat-data for browser support. The digests of Codrops and award sites were done by research
sub-agents and checked against the source where they matter. If something could not be verified, it says so.

---

## 0. The short version

1. **Spine:** Lenis (`lenis@1.3.27`) drives native scroll, the GSAP ticker drives Lenis, and ScrollTrigger reads
   Lenis. Native touch scroll on phones. One `MotionProvider` in `app/layout.tsx` (section 4).
2. **Page changes:** use React 19.3 `<ViewTransition>`, which is now stable, with Next 16.4. It needs no config flag
   any more, and `<Link transitionTypes>` handles direction. Use it for the site-wide paper-slide and for the
   stamp → case-study cover morph. Use a GSAP overlay (for example, `next-transition-router`) for just one moment,
   the letter → envelope hand-off to /start, or if the native morph can't match the art direction (section 5,
   techniques 13 and 14).
3. **Signature moments**, built by hand with GSAP, are the parts that make the site Kavalu's own:
   - the road that draws and forks (DrawSVG + MotionPath)
   - the hero stamp that expands to full screen (clip-path inset with an inner counter-scale)
   - the project spreads that deal out of a stack (Flip / timeline)
   - the scrapbook desk you drag (Draggable + Inertia)
   - the letter that folds into an envelope (CSS 3D, or paperlab if it earns its weight)
4. **Borrow, don't install, galleries:** React Bits components were rebuilt between 8 and 13 October 2026, and most
   no longer need dependencies. Read them as reference implementations: Stack, Masonry, Folder, Sticker Peel,
   Tear Ticket, Fold Text, Image Trail, Scroll Expand, Noise. Re-skin into the Kavalu system rather than dropping
   them in as-is.
5. **Closest live references** (section 5b):
   - **Digital Stamp Collection** (https://marijanapav.com/stamps; open source, Next 16 + React 19 + Lenis + Motion):
     stamps, loupe, binder tabs, typewriter cards, a postcard form.
   - **MERSI** (Awwwards SOTD, Apr 2026), for Flip-based cover → case-study transitions and a collage that resolves
     into a grid.
   - **Obys' Design Books**, for paper sheets you pull to the front.
6. **WebGL only where it earns its place:** one shared OGL canvas, at most, for a subtle riso / ink-bleed hover on the
   work index. Everything else is DOM, CSS and SVG. Paper realism comes from good photography of real paper,
   grain and shadows, not from shaders.

---

## 1. Verified packages (npm registry, 23 Oct 2026)

| Package | Latest (`latest` tag) | Published | Notes that matter |
|---|---|---|---|
| `gsap` | **3.15.0** | 2026-04-13 | The public package ships every plugin. I checked the tarball file list: ScrollTrigger, Flip, SplitText, Observer, ScrollSmoother, Draggable, InertiaPlugin, MorphSVGPlugin, DrawSVGPlugin, plus CustomEase, CustomBounce, CustomWiggle, ScrambleTextPlugin, TextPlugin, MotionPathPlugin, Physics2D, PhysicsProps, ScrollToPlugin, EasePack and GSDevTools. All of them have been free since 3.13 (2025-04-29, the Webflow deal). The `gsap-trial` package is deprecated in favour of `gsap`. 3.14 (2025-12-08) added MorphSVG `smooth` and `curveMode` and the demo hub at demos.gsap.com. 3.15 added `easeReverse`, which replaces `yoyoEase`. |
| `@gsap/react` | **2.1.2** | 2025-01-15 | `useGSAP(cb, { scope, dependencies, revertOnUpdate })`, with `contextSafe` for event handlers. Peer dependencies: `gsap ^3.12.5`, `react >=17`. Needs `"use client"`. |
| `lenis` | **1.3.27** | 2026-10-15 | `respectReducedMotion` is on by default (it forces lerp 1 and makes `scrollTo` instant). Use `lenis/react` for `<ReactLenis root>` and `useLenis`. **2.0.0-dev.5** (2026-09-18, `dev` tag) renames options: `wheel`, `touch` and `programmatic` become groups, `onGesture` replaces `virtualScroll`, and `lock()`/`unlock()` replace `stop()`/`start()`. `autoRaf`, `anchors` and `stopInertiaOnNavigate` default to true, and there is a new `drag` option. Darkroom's own starter (satus) already runs 2.0.0-dev.5 with Next 16.4.2 and React 19.3.1. Pin 1.3.27 for now and wrap the options in one file so the 2.0 move is a one-file change. The old `@studio-freight/lenis` package is deprecated. |
| `motion` | **14.6.0** | 2026-10-22 | 13.0.0 shipped 2026-08-05 and 14.0.0 on 2026-10-02. See section 1a for the breaking changes. `framer-motion` mirrors the same version. |
| `ogl` | **1.0.11** | 2025-01-27 | Unlicense. A small WebGL core, still used by React Bits Ripple Distortion and Morph Slider. |
| `three` | 0.186.1 | 2026-09-24 | Only if paperlab or R3F is used. |
| `next` / `react` | **16.4.2** / **19.3.1** | 2026-10-15 / 2026-10-14 | React 19.3.0 (2026-09-09) made `<ViewTransition>`, `addTransitionType` and Fragment refs stable. Next 16.4's bundled docs say view transitions "work in the App Router with no configuration". The `experimental.viewTransition` page is gone from the 16.4.2 docs. |
| `@number-flow/react` | 0.6.2 | 2026-07-18 | Accessible animated numbers. `respectMotionPreference` defaults to true. |
| `matter-js` | 0.20.0 | 2024-06-23 | Still the easiest 2D physics for DOM stickers, but development has slowed. `planck` 1.5.1 and `@dimforge/rapier2d-compat` 0.21.0 are the maintained alternatives. |
| `@use-gesture/react` | 10.3.1 | 2024-03-21 | Pinch/drag/wheel gestures, as used by React Bits Dome Gallery. No longer updated, but stable. |
| `rough-notation` | 0.5.1 | 2020 | Hand-drawn annotations: highlight, circle, box, underline, bracket. Magic UI's Highlighter wraps it. |
| `paperlab` | 0.8.1 (beta) | 2026-09-18 | Real 3D paper as a React component (peel, unroll, flip, letter-fold, hang, fall, settle, crumple, plus clips and pegs). Peer dependencies: react ≥19, three ≥0.162, @react-three/fiber ≥9, gsap ≥3.12. `@react-three/fiber` 9.8.2 caps React below 19.4. |
| `@paper-design/shaders-react` | 0.0.82 | 2026-10-21 | Paper Shaders (grain, warp and torn edges, halftone). Still pre-1.0. |
| `unicornstudio-react` | 2.4.0 | 2026-10-11 | Unofficial embed for Unicorn Studio scenes, measured at about 240 KB gzip (section 5, technique 38). |
| `next-view-transitions` | 0.3.5 | 2025-12-05 | Not needed on Next 16.4 with React 19.3. |
| `split-type` | 0.3.4 | 2023 | Superseded by the free GSAP SplitText. Don't add it. |

**Suggested install set:**
- **Core:** `gsap@3.15.0`, `@gsap/react@2.1.2`, `lenis@1.3.27`.
- **Optional, each tied to one feature:**
  - `@number-flow/react@0.6.2` (stats)
  - `@use-gesture/react@10.3.1` (pinch on /scrapbook)
  - `matter-js@0.20.0` (the footer sticker pile)
  - `ogl@1.0.11` (only if the ink-bleed hover ships)
  - `rough-notation@0.5.1` (only if you don't hand-draw the SVG marks)
  - `motion@14.6.0` (only if a component is far easier with springs or `layout`. Two animation engines on one
    page is allowed, but never on the same element)
- **Don't add:**
  - `split-type` or `next-view-transitions`: superseded
  - `@studio-freight/lenis`: renamed
  - ScrollSmoother or `locomotive-scroll` alongside Lenis
  - three / R3F, unless paperlab wins its place

**Licences to know:**
- **GSAP** is under the Standard "no charge" licence: commercial client sites are fine. The one prohibition is
  using GSAP inside a visual, no-code animation builder that competes with Webflow.
- **React Bits** is MIT plus the Commons Clause: you can use it in any site, but you can't resell the components
  themselves.
- **Skiper UI** free components require attribution unless you have Pro.
- **Osmo Vault** code is for members only (Solo is about €20–25 a month). The resource descriptions are public.

### 1a. Motion (motion.dev) 13 → 14: what changed and how it fits next to GSAP

Checked against the motion.dev docs, CHANGELOG.md and the 14.6.0 tarball source. GitHub Releases is empty;
the CHANGELOG is the release record.

- **13.0 (2026-08-05).** The only breaking change is that the optional `@emotion/is-prop-valid` dependency is gone.
  If you use styled-components or Emotion, pass it explicitly with `<MotionConfig isValidProp={isPropValid}>`.
  https://motion.dev/docs/react-upgrade-guide
- **14.0 (2026-10-02).** "There are no breaking changes in Motion for React in version 14". Some internal APIs
  were dropped, and `motion` now pins `framer-motion`, `motion-dom` and `motion-utils` to the exact same version,
  so don't install a second, different `framer-motion` alongside it.
- **App Router.** Use `"use client"`, or `import * as motion from "motion/react-client"` in server files. The peer
  range is React 18.2 or later. For bundle size, `motion` is about 43 kB, while `LazyMotion` + `m`
  (`motion/react-m`) is about 5 kB at first render plus 24 kB for `domAnimation` (Motion's bundle-size docs).
- **Worth knowing from 13–14:**
  - `AnimateView` (React, `motion/react-animate-view`, 13.4.0; free; needs React 19.3) and the vanilla
    `animateView()` (free core since 12.41.0) wrap the View Transitions API with springs and interruption
    queues.
  - 14.2: hardware-accelerated independent transforms.
  - 14.3: `stagger` gets `grid` and `from: "edges" | "random"`.
  - 14.5: `useScopeMotion(ref, setup, { deps, transition, matchMedia })`, a `gsap.context`-like scoped,
    self-cleaning setup.
- **Scroll.** `useScroll`/`scroll()` use native `ScrollTimeline`/`ViewTimeline` where possible. Per the 14.6.0 source,
  a value only reaches the GPU when it's bound to `opacity`, `transform`, `clipPath`, `filter` or
  `backgroundColor`, and `useSpring` or function transforms keep it on the main thread.
- **Motion+.** USD 399 once per developer, MIT for client work, installed from a private registry with a
  `MOTION_TOKEN`. These are Motion+-only: `Ticker`, `AnimateNumber`, `Cursor`, `Typewriter`, `ScrambleText` and
  `splitText`. Everything Kavalu needs from that list already exists free in GSAP (ScrambleText, SplitText,
  `horizontalLoop`, `quickTo`), so **Motion+ isn't needed.**
- **With Lenis.**
  - If Motion drives the loop, its docs use `frame.setup(({ timestamp }) => lenis.raf(timestamp), true)`.
    The Lenis README's `frame.update` variant lags main-thread scroll animations by a frame.
    https://motion.dev/docs/lenis
  - On Kavalu, the **GSAP ticker** drives Lenis, and Motion components just read native scroll.
- **With GSAP.**
  - Both libraries write the whole inline `transform`, and Motion's WAAPI animations override inline styles
    while they run.
  - Never animate one element with both. Nest a wrapper instead, for example Motion springs on the outer card
    and GSAP Flip on the inner image.
- **Useful official examples** (`https://motion.dev/examples/<slug>`; F = free source, P = Motion+):
  - `react-shared-layout-animation` (F)
  - `react-animate-view-app-store` (F, a card expand through View Transitions)
  - `react-scroll-horizontal` (F)
  - `js-parallax` (F)
  - `react-follow-pointer-with-spring` (F)
  - `react-text-scroll-word-reveal` (F)
  - `react-scroll-zoom-hero` (P)
  - `react-cursor-magnetic` (P)
  - `react-ticker-scroll` (P)
  - `react-number-counter` (P)

---

## 2. Browser support snapshot (MDN browser-compat-data, main branch, 23 Oct 2026)

| Feature | Chrome | Safari | Firefox | Use on Kavalu |
|---|---|---|---|---|
| Same-document View Transitions (`startViewTransition`, React `<ViewTransition>`) | 111 | 18 | 144 | Yes, as the default page transition. Browsers without it just navigate. |
| `view-transition-class`, transition types (`:active-view-transition-type`) | 125 | 18.2 | 144 / 147 | Yes: directional and paper-slide classes. |
| `view-transition-name: match-element` | 137 | 18.4 | 144 | Optional. |
| Cross-document `@view-transition` (MPA) | 126 | 18.2 | — | Not needed (App Router is same-document). |
| CSS scroll-driven animations (`animation-timeline: view()/scroll()`) | 115 | 26 | **159**: beta now, stable release 27 Oct 2026 | Progressive enhancement for small reveals and parallax that need no JS. |
| CSS scroll-*triggered* animations (`animation-trigger`, `timeline-trigger`) | 146 | — | — | Don't rely on them yet. |
| `clip-path: shape()` (responsive torn edges) | 135 | 18.4 | 148 | Yes, with a `polygon()` fallback. |
| `clip-path: xywh()/rect()` | 119 | 17.2 | 122 | Yes. |
| `@starting-style` (enter transitions without JS) | 117 | 17.5 | 129 | Yes, for menus, tooltips and folder-tab drawers. |
| `linear()` easing (CSS springs) | 113 | 17.2 | 112 | Yes. |
| CSS anchor positioning | 125 | 26 | 147 | Handy for margin notes and tooltips. |
| `corner-shape` | 139 | preview | preview | No. Use `clip-path` for folded corners. |
| `interpolate-size: allow-keywords` | 129 | — | — | No. Animate `grid-template-rows: 0fr→1fr` instead. |

---

## 3. Global motion tokens

The design direction weights the motion like this: Jakub (production polish) is primary, Jhey (play) is for the
scrapbook and the envelope, and Emil (restraint) is for navigation and forms. The tokens follow that. Keep them in
one module (`motion/tokens.ts`) and mirror them as CSS custom properties so GSAP, Motion and CSS agree.

### 3.1 Easing

| Token | CSS | GSAP name | Use |
|---|---|---|---|
| `--ease-glide` | `cubic-bezier(0.16, 1, 0.3, 1)` | `"expo.out"` | The house ease for arrivals: image settles, the end of a hero zoom, stamp lands. This is the curve already in `design_direction.md`. |
| `--ease-soft` | `cubic-bezier(0.22, 1, 0.36, 1)` | `"power4.out"` (quint) | Text line masks and card entrances. Gentler at the very end than expo. |
| `--ease-ui` | `cubic-bezier(0.23, 1, 0.32, 1)` | `CustomEase.create("kv.ui", "0.23,1,0.32,1")` | Hover, press, nav, form feedback. Short durations only. |
| `--ease-travel` | `cubic-bezier(0.76, 0, 0.24, 1)` | `"power3.inOut"` (quart) | Things that move across the screen while visible: FLIP morphs, the cover expanding into a case study, folder-tab drawers. |
| `--ease-wipe` | `cubic-bezier(0.87, 0, 0.13, 1)` | `"expo.inOut"` | Page cover wipes, the preloader lifting away. Use it once per navigation at most. |
| `--ease-leave` | `cubic-bezier(0.32, 0, 0.67, 0)` | `"power2.in"` (cubic) | Exits, kept short (≤ 250 ms). Exits are quieter than entries. |
| `--ease-drawer` | `cubic-bezier(0.32, 0.72, 0, 1)` | `CustomEase.create("kv.drawer", "0.32,0.72,0,1")` | Menus and sheets (the iOS-sheet feel). |
| `--ease-paper` (playful) | `linear()` spring or `cubic-bezier(0.34, 1.56, 0.64, 1)` | `"back.out(1.6)"`, or Motion `{ type: "spring", visualDuration: 0.5, bounce: 0.2 }` | Only for physical paper moments: a sticker dropped, a stamp pressed, a sticky note slapped on. Never for menus, modals or toggles. |
| scrub | `linear` | `"none"` | Every scroll-scrubbed timeline. The feel comes from Lenis and from `scrub`, not from an ease. `containerAnimation` requires `ease: "none"`. |

GSAP 3.15 tip: on anything that opens and closes, such as the menu, the folder tabs, the cursor preview and
filter panels, set `easeReverse: true` or a separate ease like `easeReverse: "power2.in"`. The close then feels
like a close and not like the open played backwards. For toggles, use `tl.timeScale(1.5).reverse()` so the
close is faster than the open.

### 3.2 Durations

| Token | Value | Examples |
|---|---|---|
| `instant` | 0 | Keyboard-initiated changes, focus rings, high-frequency toggles. |
| `micro` | 150–200 ms | Link underline, colour and opacity on hover. |
| `short` | 280–350 ms | Magnetic return, tooltip, menu item, tab underline. |
| `base` | 500–650 ms | Sticker pick-up and drop, card lift, folder tab open. |
| `reveal` | 800–1000 ms | Line-mask headings, image `clip-path` reveals, stamp deal-out. |
| `hero` | 1.1–1.4 s | Stamp → case-study cover, preloader lift, the scrapbook "open". |
| `page` (View Transition) | old out 150–200 ms, new in 300–450 ms, shared morph 450–600 ms | Matches the timing in Next's own guide: a fast exit and a gentler arrival. |
| `intro` | ≤ 1.4–1.6 s, first visit only | The line draws, forks and lifts. It's skipped on repeat visits and with reduced motion. |

### 3.3 Stagger

| Unit | `each` | Total cap |
|---|---|---|
| Lines (SplitText `mask: "lines"`) | 0.06–0.10 s | ≤ 0.5 s |
| Words | 0.025–0.04 s | ≤ 0.6 s |
| Characters (display words only) | 0.012–0.02 s | ≤ 0.5 s |
| Grid or stamp deal-out | `stagger: { each: 0.05, from: "start", grid: "auto" }` | Use `amount: 0.4` for big grids |

Use one staggered moment per view at most. Two staggered lists in the same viewport reads as template motion
(see the anti-list).

### 3.4 Distances, scale and rotation

- Rise: 12–16 px for small UI, 24–40 px or `yPercent: 100` inside a mask for display lines.
- Scale: enter from 0.96–0.98, never from 0. Hover lift on paper is at most 1.02, plus a shadow change, which
  sells "lifted off the page" better than scale does.
- Paper rotation: rest between −4° and +4°. On pick-up, add 2–6° in the drag direction. Clamp to ±8°.
- Blur: up to 4 px, and only on the hero or display elements. Never on body copy (see the anti-list).

### 3.5 Scroll and scrub

- Lenis: `lerp: 0.1` (the default; 0.08 is floatier), `smoothWheel: true`, `syncTouch: false` (native touch),
  `anchors: true`, `stopInertiaOnNavigate: true`, `autoRaf: false` (GSAP drives it). Leave
  `respectReducedMotion: true`.
- `scrub`: Lenis already smooths the scroll, so a big `scrub` doubles the lag and starts to feel like mush.
  - Use `scrub: true` or 0.2–0.5 for things tied to reading position: the road, the hero expansion, spreads.
    Osmo's Flip-on-scroll resources use `scrub: 0.25` with Lenis.
  - Use 0.8–1.2 only for deliberately floaty layers, such as parallax paper and the collage camera.
- `anticipatePin: 1` on pinned sections. `invalidateOnRefresh: true` on anything whose values are measured.
- Don't combine `ScrollTrigger.normalizeScroll()` or ScrollSmoother with Lenis. Pick one smoother; for this
  stack that's Lenis, because it keeps native `position: sticky` working.

### 3.6 Springs (Motion, for component state only)

- UI: `{ type: "spring", visualDuration: 0.3–0.4, bounce: 0 }`
- Paper objects: `{ visualDuration: 0.5, bounce: 0.15–0.25 }`
- Pointer smoothing: `useSpring(v, { stiffness: 300, damping: 30 })`, or `gsap.quickTo(el, "x", { duration: 0.5,
  ease: "power3" })` when GSAP owns the element. Only one library should own any given element's `transform`.

### 3.7 Reduced-motion policy (functional vs decorative)

| Class | Normal | `prefers-reduced-motion: reduce` |
|---|---|---|
| Smooth scroll | Lenis lerp 0.1 | Lenis forces lerp 1 automatically, so scroll is native. |
| Scroll-scrubbed stories (hero expansion, spreads, road) | Pin + scrub | No pin, no scrub. Show the end state, or a 200 ms crossfade when it enters view. |
| Page transitions | Paper slide plus shared morph | Durations set to 0. You may keep a 150 ms opacity crossfade. |
| Parallax and collage camera | On | Off: static composition. |
| Marquees and flip-book stamps | Move | Static, showing the first frame. Every auto-moving thing also gets a pause control (WCAG 2.2.2). |
| Cursor follower, image trail, magnetic buttons | On (fine pointers only) | Off. |
| WebGL hover | On | Off: show the DOM image. |
| Preloader | First visit only | Skipped. |
| Physics (stickers, scrapbook throw) | On | Drag without inertia, and a grid view is offered. |

Implementation: `gsap.matchMedia()` with `{ motion: "(prefers-reduced-motion: no-preference)", reduce:
"(prefers-reduced-motion: reduce)", fine: "(hover: hover) and (pointer: fine)", desktop: "(min-width: 1024px)" }`.
In CSS, add the `::view-transition-*` zero-duration block (section 5, technique 14) and
`@media (prefers-reduced-motion: no-preference)` gates around keyframes.

### 3.8 Performance budget

- Animate `transform`, `opacity` and `clip-path` (small and medium elements). Never animate `width`, `height`, `top`
  or `left`. For full-screen expansions, scale a wrapper and counter-scale the image inside, and test on a
  mid-range Android.
- Use one WebGL canvas per page at most, lazy-loaded with `next/dynamic` (`ssr: false`) once it's in view, and
  disposed on route change.
- Use one rAF for the site, the GSAP ticker. Lenis, the cursor, physics and WebGL all hang off it.
- CLS:
  - give all media an `aspect-ratio`
  - split text only after `document.fonts.ready`, or use SplitText `autoSplit: true`
  - let pin spacers calculate before reveal
  - make the preloader an overlay, never a layout change
- INP: pointer handlers only call `quickTo` setters or write cached values. Don't call `getBoundingClientRect`
  inside `pointermove`.

---

## 4. The motion spine in Next.js (App Router)

```tsx
// app/layout.tsx (server): <body><MotionProvider>{children}</MotionProvider></body>

// components/motion/MotionProvider.tsx
'use client'
import { useEffect, useRef } from 'react'
import { usePathname } from 'next/navigation'
import { gsap } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'
import { Flip } from 'gsap/Flip'
import { SplitText } from 'gsap/SplitText'
import { CustomEase } from 'gsap/CustomEase'
import { DrawSVGPlugin } from 'gsap/DrawSVGPlugin'
import { MotionPathPlugin } from 'gsap/MotionPathPlugin'
import { Draggable } from 'gsap/Draggable'
import { InertiaPlugin } from 'gsap/InertiaPlugin'
import { Observer } from 'gsap/Observer'
import { useGSAP } from '@gsap/react'
import { ReactLenis, useLenis, type LenisRef } from 'lenis/react'
import 'lenis/dist/lenis.css'

gsap.registerPlugin(useGSAP, ScrollTrigger, Flip, SplitText, CustomEase,
  DrawSVGPlugin, MotionPathPlugin, Draggable, InertiaPlugin, Observer)
CustomEase.create('kv.ui', '0.23,1,0.32,1')
CustomEase.create('kv.drawer', '0.32,0.72,0,1')
ScrollTrigger.config({ ignoreMobileResize: true })

export function MotionProvider({ children }) {
  const lenisRef = useRef<LenisRef>(null)
  const pathname = usePathname()

  useEffect(() => {                      // GSAP ticker drives Lenis (one rAF for everything)
    const tick = (t: number) => lenisRef.current?.lenis?.raf(t * 1000)  // instance may arrive a frame late
    gsap.ticker.add(tick)
    gsap.ticker.lagSmoothing(0)
    return () => gsap.ticker.remove(tick)
  }, [])

  useLenis(() => ScrollTrigger.update())  // = lenis.on('scroll', ScrollTrigger.update), lifecycle-safe

  useEffect(() => {                      // route change: no inertia carry-over, fresh measurements
    lenisRef.current?.lenis?.scrollTo(0, { immediate: true, force: true })
    requestAnimationFrame(() => ScrollTrigger.refresh())
  }, [pathname])

  return (<>
    <ReactLenis root ref={lenisRef}
      options={{ autoRaf: false, lerp: 0.1, anchors: true, stopInertiaOnNavigate: true }} />
    {children}
    <GrainOverlay />  {/* fixed, pointer-events:none, aria-hidden */}
  </>)
}
```

Per-section pattern (each animated section is a small client island and the content stays server-rendered):

```tsx
useGSAP(() => {
  const mm = gsap.matchMedia()
  mm.add({ motion: '(prefers-reduced-motion: no-preference)', desktop: '(min-width: 1024px)' }, (ctx) => {
    const { motion, desktop } = ctx.conditions!
    if (!motion) return            // reduced motion: static end state, from CSS
    // ... build timelines and ScrollTriggers here; they are reverted when a condition flips
  })
  return () => mm.revert()
}, { scope: rootRef })
```

Rules of the house:
- Render final content in the HTML. JavaScript only adds the motion. Gate "hidden before reveal" CSS behind
  `html.js`, which an inline script sets in `<head>`, so no-JS and crawlers see everything.
- Mark any element that is mid-transform for a View Transition, or that GSAP owns, with a single owner. Don't let
  Motion and GSAP both write `transform` on the same node.
- `data-lenis-prevent` goes on every nested scroller: the scrapbook canvas, modals, the onboarding letter's
  textarea.
- Kill and refresh: `useGSAP` reverts on unmount. Run `ScrollTrigger.refresh()` after fonts load
  (`document.fonts.ready`), and after hero images decode on pages with pins.

## 5. Technique catalog

How to read each entry:
- **Fit** says how well it suits this site (High, Med or Low), with the reason.
- **Where** is the place on the Kavalu site map from `design_direction.md`.
- **Sources** are the pages to study. Prefer the ones marked ★.
- **Perf/a11y** covers the reduced-motion fallback, mobile and CLS.
- **Sketch** shows the load-bearing calls only.

### A. Scroll foundation

#### 1. Smooth scroll: Lenis + GSAP ticker sync. Fit: High
- **Looks like:** The wheel scroll glides and settles (lerp), while the scrollbar, `position: sticky`, find-in-page and
  anchors keep working, because Lenis drives *native* scroll and doesn't fake it.
- **Where:** Site-wide, mounted once in the root layout.
- **Sources:**
  - ★ https://github.com/darkroomengineering/lenis (README: GSAP ScrollTrigger setup, React package)
  - https://github.com/darkroomengineering/lenis/blob/main/packages/react/README.md
  - Darkroom's Next 16.4 starter, `components/layout/lenis/index.tsx`:
    https://github.com/darkroomengineering/satus (it orders all rAF work with `tempus`, with `Lenis.raf` first)
  - https://www.osmo.supply/resource/lenis-smooth-scroll-setup
- **Stack:** `lenis@1.3.27` (`lenis/react`), `gsap` ticker.
- **Fit:** High. A premium "smooth" feel was the founder's first ask, it costs a few KB, and it's the clock every
  other scroll effect reads.
- **Perf/a11y:**
  - `respectReducedMotion` (default true) turns smoothing off for users who ask.
  - Leave `syncTouch: false` so phones keep native momentum.
  - Add `data-lenis-prevent` to nested scrollers and modals.
  - Lenis is capped at 60 fps on Safari (its README says so).
  - Don't hijack keyboard scrolling: Page Down, Space and arrow keys must still work, so test them.
- **Sketch:** see section 4. Key points:
  - `gsap.ticker.add(t => lenis.raf(t * 1000))`
  - `gsap.ticker.lagSmoothing(0)`
  - `lenis.on('scroll', ScrollTrigger.update)`, or `useLenis(ScrollTrigger.update)` in React
  - `autoRaf: false`
  - on route change, `lenis.scrollTo(0, { immediate: true, force: true })`

#### 2. Parallax paper layers and collage depth. Fit: High
- **Looks like:** The scrapbook layers move at slightly different rates as you scroll: tape and clips are fastest,
  photos are in the middle, the paper ground is slowest. Optionally there's a ±6–10 px drift with the pointer on
  desktop, so the album page feels stacked rather than flat.
- **Where:**
  - the hero album page (satellite stamps)
  - "From the scrapbook" on the home page
  - the founder section (the duotone portrait slightly behind its paper frame)
  - case-study "pair" blocks
- **Sources:**
  - ★ https://www.osmo.supply/resource/global-parallax-setup
  - https://www.osmo.supply/resource/parallax-image-layers
  - Aceternity Parallax Hero Images, mouse-depth layers with springs:
    https://ui.aceternity.com/components/parallax-hero-images
  - Skiper 30 (multi-column scroll parallax, Lenis + Motion): https://skiper-ui.com/v1/skiper30
  - 21st.dev "Parallax Floating" (cursor-drift layers, desktop only) and "Zoom Parallax" (images zooming at
    different speeds): https://21st.dev/@danielpetho/components/parallax-floating ·
    https://21st.dev/@sshahaider/components/zoom-parallax
  - GSAP ScrollSmoother's `data-speed`/`data-lag` model, for the API idea only:
    https://gsap.com/docs/v3/Plugins/ScrollSmoother/
- **Stack:** ScrollTrigger (scrub), `gsap.quickTo` for pointer depth. CSS `animation-timeline: view()` can take over
  simple cases (technique 3).
- **Fit:** High. Layered paper is the concept, and gentle depth sells the physical stack.
- **Perf/a11y:**
  - Keep the amplitude small (yPercent −6 to +6 on images inside `overflow: hidden` frames, 20–60 px on
    stickers). Large parallax is a vestibular trigger, so with reduced motion it's off entirely.
  - Disable pointer depth on touch.
  - No CLS, since only transforms are used.
- **Sketch:**
  ```js
  gsap.utils.toArray('[data-speed]').forEach(el => {
    gsap.to(el, { yPercent: () => (1 - parseFloat(el.dataset.speed)) * 40, ease: 'none',
      scrollTrigger: { trigger: el.closest('section'), start: 'top bottom', end: 'bottom top', scrub: 1,
        invalidateOnRefresh: true } })
  })
  // pointer depth (desktop only)
  const xTo = gsap.quickTo(layer, 'x', { duration: 0.8, ease: 'power3' })
  onPointerMove: xTo((e.clientX / innerWidth - 0.5) * depth * 20)
  ```

#### 3. CSS scroll-driven animations (zero-JS enhancement). Fit: Med
- **Looks like:** Small reveals and parallax that run off the main thread with no JavaScript.
- **Where:** Margin notes, tape strips, sticker wobble on entering, the footer wordmark parallax. Use it for the
  small stuff, not the hero stories, which stay in GSAP.
- **Sources:**
  - ★ https://tympanus.net/codrops/2024/01/17/a-practical-introduction-to-scroll-driven-animations-with-css-scroll-and-view/
  - Codrops "Experimental CSS-only carousels with scroll-driven animations":
    https://tympanus.net/Development/ScrollCarousel/
- **Stack:** CSS. Supported in Chrome 115, Safari 26 and Firefox 159 (stable 27 Oct 2026). Older Firefox and Safari
  just show the static state.
- **Fit:** Med. It's very cheap, but you can't sync it with Lenis smoothing: it follows native scroll, which
  Lenis also drives, so it still works, but it's unsmoothed. Keep it to non-critical flourishes.
- **Perf/a11y:**
  - Wrap it in `@media (prefers-reduced-motion: no-preference)` and `@supports (animation-timeline: view())`.
- **Sketch:**
  ```css
  @supports (animation-timeline: view()) { @media (prefers-reduced-motion: no-preference) {
    .tape { animation: tape-peel linear both; animation-timeline: view(); animation-range: entry 10% cover 40%; }
  }}
  @keyframes tape-peel { from { rotate: -6deg; translate: 0 14px; opacity: 0 } to { rotate: -2deg; translate: 0; opacity: 1 } }
  ```

### B. Zoom in, zoom out, expand

#### 4. Card → fullscreen scroll zoom (the hero stamp expands). Fit: High ★ signature
- **Looks like:** The centre stamp sits in the album page. As you scroll, it's pinned, the headline lifts away, the
  satellites drift apart, and the stamp's frame grows to full bleed. The corner radius and perforation fade, and
  the image inside *counter-zooms* from 1.35 to 1, so the photo seems to settle rather than stretch. The frame
  then takes on the first project's colour and hands over to the spreads.
- **Where:** The home hero (from `design_direction.md`, item 2), and the work index's "featured" item.
- **Sources:**
  - ★ React Bits Scroll Expand, which uses exactly this: a `clip-path: inset(... round r)` frame plus an inner
    `scale(mediaZoom → 1)`, `smoothstep` progress and a scrim/overlay crossfade.
    https://reactbits.dev/animations/scroll-expand (source: `src/content/Animations/ScrollExpand` on GitHub)
  - ★ Osmo "Image to Background (Zoom)" (Flip + ScrollTrigger, Jan 2026):
    https://www.osmo.supply/resource/image-to-background-zoom
  - Osmo "Scaling element on scroll (GSAP Flip)", which chains Flip.fit between waypoints with
    `scrub: 0.25` and Lenis: https://www.osmo.supply/resource/scaling-element-on-scroll-gsap-flip
  - Codrops "Layered zoom scroll effect" (29 Oct 2025, a telescope.fyi recreation):
    https://tympanus.net/codrops/2025/10/29/building-a-layered-zoom-scroll-effect-with-gsap-scrollsmoother-and-scrolltrigger/
    (demo https://tympanus.net/Tutorials/TelescopeZoom/)
    - Worth stealing: thumbnails flying toward the viewer with `perspective: 100vh` and `z: "100vh"`; masked
      cut-out copies of the hero scaling up out of blur; one `--progress` custom property set from `onUpdate`
      driving CSS `scale()`.
    - Don't copy its `ScrollSmoother` + `normalizeScroll` setup under Lenis.
  - Codrops "On-scroll expanding image within typography":
    https://tympanus.net/Development/ImageExpansionTypography/
  - 21st.dev "Scroll media expansion hero":
    https://21st.dev/@arunachalam/components/scroll-expansion-hero
- **Stack:** ScrollTrigger (pin + scrub), with either clip-path animation or `Flip.fit` scrubbed by a timeline.
- **Fit:** High. It's literally "zoom in / expand", the brief's first motion, and it puts the work at full screen
  within one scroll.
- **Perf/a11y:**
  - Use a high-resolution source with `sizes="100vw"`. The hero image is the LCP, so give it
    `fetchpriority="high"`, and don't lazy-load it or hide it behind the preloader.
  - Animate `clip-path` and `transform` only.
  - Mobile: pin for a shorter distance (`end: "+=80%"`). Pins and the iOS address bar don't mix well, so set
    `ignoreMobileResize`.
  - Reduced motion: no pin. Show the full-bleed image at its final state below the headline.
  - CLS: the pin spacer is created before first paint, from server-rendered dimensions.
- **Sketch:**
  ```js
  const tl = gsap.timeline({ defaults: { ease: 'none' }, scrollTrigger: {
    trigger: hero, start: 'top top', end: '+=150%', pin: true, scrub: 0.3, anticipatePin: 1 } })
  tl.to(headline, { yPercent: -30, autoAlpha: 0 }, 0)
    .to(satellites, { x: (i) => offsets[i].x, y: (i) => offsets[i].y, rotate: (i) => offsets[i].r }, 0)
    .fromTo(frame, { clipPath: 'inset(21% 29% round 18px)' }, { clipPath: 'inset(0% 0% round 0px)' }, 0)
    .fromTo(img,   { scale: 1.35 }, { scale: 1 }, 0)
    .to(perforation, { autoAlpha: 0 }, 0.2)
    .to(frame, { backgroundColor: firstProject.color }, 0.8)
  ```
  For a *real* reposition, where the stamp isn't centred, use Flip instead:
  `const s = Flip.getState(stamp); fullBleedSlot.append(stamp); tl.add(Flip.from(s, { scale: true, ease: 'none' }))`.
  Follow the Osmo pattern and rebuild it on resize.

#### 5. Fullscreen → card zoom-out (spread exits, "leaving a spread zooms it out"). Fit: High
- **Looks like:** A full-screen project spread recedes to about 0.9 scale, darkens and rounds its corners as the
  next spread slides up over it. That's the inverse of technique 4, combined with stacking (technique 10).
- **Where:** The home project spreads (item 3), and the case-study "next project" hand-off.
- **Sources:**
  - ★ Codrops "On-scroll animation ideas for sticky sections" (2024): https://tympanus.net/Development/StickySections/
  - Codrops "Sticky grid scroll" (2 Mar 2026):
    https://tympanus.net/codrops/2026/03/02/sticky-grid-scroll-building-a-scroll-driven-animated-grid/
  - Osmo "Stacking cards parallax": https://www.osmo.supply/resource/stacking-cards-parallax
  - Skiper 16, the sticky card stack (Motion + Lenis, free with attribution): https://skiper-ui.com/v1/skiper16
- **Stack:** CSS `position: sticky` for the stacking plus ScrollTrigger scrub for `scale`, `borderRadius` and a
  shade overlay's opacity.
- **Fit:** High. It's the "zoom out" half of the brief, and it keeps a sense of *place*: spreads pile up like
  pages, which suits the album metaphor.
- **Perf/a11y:**
  - Animate a shade overlay's opacity instead of `filter: brightness()`. Filters on full-screen layers are
    costly.
  - Reduced motion: plain stacked sections with no scale.
  - Mobile: keep it, with smaller values (scale to 0.94).
- **Sketch:**
  ```js
  spreads.forEach((s, i) => {
    if (i === spreads.length - 1) return
    gsap.to(s.querySelector('.spread__inner'), { scale: 0.9, borderRadius: 24, ease: 'none',
      scrollTrigger: { trigger: spreads[i + 1], start: 'top bottom', end: 'top top', scrub: true } })
    gsap.to(s.querySelector('.spread__shade'), { opacity: 0.35, ease: 'none',
      scrollTrigger: { trigger: spreads[i + 1], start: 'top bottom', end: 'top top', scrub: true } })
  })
  /* css */ .spread { position: sticky; top: 0; height: 100svh; }
  ```

#### 6. Clip-path / inset expand reveals. Fit: High
- **Looks like:** Images "open" from a slit or from their own frame (`inset(50% 0 50% 0)` → `inset(0)`). Panels
  wipe in like paper slid out of a sleeve. The direction follows the road: a project's images open along the
  same axis as the fork that leads to them.
- **Where:**
  - case-study "full" and "pair" blocks
  - stamp deal-out (combined with technique 11)
  - menu and folder-tab drawers
  - onboarding steps
- **Sources:**
  - ★ Codrops "Image layer animations with clip-path" (2023): https://tympanus.net/Development/LayersAnimation/
  - Codrops "Fullscreen clip animation": https://tympanus.net/Development/FullscreenClipEffect/
  - Codrops "Animated product grid preview with GSAP clip-path" (27 May 2025):
    https://tympanus.net/codrops/2025/05/27/animated-product-grid-preview-with-gsap-clip-path/
    (demo https://tympanus.net/Tutorials/GridToFullPreview)
  - Codrops "On-scroll SVG mask transitions" (11 Mar 2026):
    https://tympanus.net/codrops/2026/03/11/svg-mask-transitions-on-scroll-with-gsap-and-scrolltrigger/
  - Codrops "GSAP EaseReverse clip menu" (3.15 `easeReverse`): https://tympanus.net/Development/EaseReverseClipMenu
  - Skiper 54 (shadcn clip-path carousel): https://skiper-ui.com/v1/skiper54
  - 21st.dev "Scroll Gallery" (sticky full-viewport wipes between full-bleed images; `gsap` + `@gsap/react`):
    https://21st.dev/@soralabs/components/scroll-gallery
- **Stack:** GSAP or CSS transitions on `clip-path: inset()/polygon()/shape()`.
- **Fit:** High. It's crisp, cheap and editorial, and it reads as paper being uncovered rather than "fading in".
- **Perf/a11y:**
  - Every point in a `polygon()` needs a unit, including zeros, and start and end must have the same point
    count (GSAP forum guidance).
  - Reduced motion: no clip; the image is simply present, or fades in over 200 ms.
  - Don't clip-reveal *every* image (see the anti-list). Use it for chapter images only.
- **Sketch:**
  ```js
  gsap.fromTo(img.parentElement, { clipPath: 'inset(0% 0% 100% 0%)' },
    { clipPath: 'inset(0% 0% 0% 0%)', duration: 1, ease: 'expo.out',
      scrollTrigger: { trigger: img, start: 'top 80%' } })
  gsap.fromTo(img, { scale: 1.15 }, { scale: 1, duration: 1.4, ease: 'expo.out', scrollTrigger: { trigger: img, start: 'top 80%' } })
  ```

#### 7. Collage camera tour (scroll pans, zooms and tilts across a collage). Fit: High
- **Looks like:** A large collage of polaroids, stamps and notes laid out like a desk. As you scroll, a "camera" glides
  along a path from one piece to the next, zooming in on each (×2–3), tilting a few degrees, then pulling back.
  It's a guided zoom-in/zoom-out tour of the work.
- **Where:**
  - an "Archive" chapter on /work, or the intro of /scrapbook before free dragging unlocks
  - inside a case study, to walk through a moodboard
- **Sources:**
  - ★ Codrops demo "Scroll-driven polaroid animation with GSAP" (Tom Miller, May 2026):
    https://tympanus.net/Tutorials/Scrollaroids/. The demo script uses
    `.to('.focal-point', { motionPath: paths[i] })` per segment, while `.pov-scale` tweens rotate and scale, and
    `gsap.quickTo('.pov-pan','x'|'y', { duration: 1.3, ease: 'expo' })` follows `-getProperty('.focal-point','x/y')`
    in `onUpdate`, with `scrub: 1`.
  - Explained step by step in "Creating scroll-driven SVG map animations with GSAP" (21 May 2026, which also links
    a reduced-motion variant):
    https://tympanus.net/codrops/2026/05/21/creating-scroll-driven-svg-map-animations-with-gsap/
- **Stack:** ScrollTrigger (pin + scrub) + MotionPathPlugin + quickTo. Plain SVG/DOM, no WebGL.
- **Fit:** High. It's a scrapbook you *tour*, it answers "zoom in, zoom out" with real meaning, and it reuses the
  road motif, since the camera literally follows a road.
- **Perf/a11y:**
  - Use transform-only on two wrapper groups.
  - Keep collage images at display size × 2–3 for the zoom; use AVIF/WebP and a responsive `srcset`.
  - Reduced motion: no camera. Show the collage at overview scale with the items as links.
  - Mobile: a shorter path and less zoom.
- **Sketch:**
  ```js
  const xTo = gsap.quickTo(pan, 'x', { duration: 1.3, ease: 'expo' }), yTo = gsap.quickTo(pan, 'y', { duration: 1.3, ease: 'expo' })
  const tl = gsap.timeline({ defaults: { ease: 'none', duration: 1 },
    scrollTrigger: { trigger: section, start: 'top top', end: '+=500%', pin: true, scrub: 1 },
    onUpdate: () => { xTo(-gsap.getProperty(focal, 'x')); yTo(-gsap.getProperty(focal, 'y')) } })
  paths.forEach((p, i) => tl.to(focal, { motionPath: p }, i).to(zoom, { scale: scales[i], rotate: tilts[i], ease: 'sine.inOut' }, i))
  ```

#### 8. Hover focus / expand within a collage. Fit: Med-High
- **Looks like:** In a loose collage, hovering one piece grows it (≈1.15×) while its neighbours shrink a little and
  ease aside, so the focus is unmistakable without opening anything. A variant is accordion panels that widen on
  hover or focus.
- **Where:** "From the scrapbook" on the home page, the founder's "things I love" collage, and the case-study
  "stamps" block.
- **Sources:**
  - ★ Osmo "Collage focus card on hover" (GSAP 3.15 + CustomEase, July 2026; tap-to-focus on touch):
    https://www.osmo.supply/resource/collage-focus-card-on-hover
  - React Bits Accordion Gallery (GSAP; it handles reduced motion): https://reactbits.dev/components/accordion-gallery
  - Aceternity Focus Cards: https://ui.aceternity.com/components/focus-cards
  - Skiper 52/53, "expand on hover": https://skiper-ui.com/v1/skiper52
- **Stack:** GSAP (or Motion `layout` for the accordion).
- **Fit:** Med-High. It's good for a dense collage. Keep it calm, with one focus change and no blur on the others.
- **Perf/a11y:**
  - It must also work on `:focus-visible` from the keyboard.
  - Touch: tap to focus, tap again to open.
  - Reduced motion: a scale-free outline or shadow change.
- **Sketch:** on `pointerenter`, `gsap.to(item, { scale: 1.15, zIndex: 5 })` and
  `gsap.to(others, { scale: 0.94, x: (i, el) => pushAway(el) })`, all with `duration: 0.6, ease: 'expo.out'`.
  On leave, reverse with `easeReverse: 'power2.inOut'`.

### C. Galleries, stacks and layout changes

#### 9. Pinned horizontal gallery. Fit: Med
- **Looks like:** Vertical scrolling moves a strip of stamps or photos sideways while the section is pinned, with
  inner images parallaxing against the strip.
- **Where:**
  - a single "Contact sheet" chapter inside photo/film-shoot case studies (a film-strip of frames)
  - or the "process" road on /studio
  - not the home page, which already has the hero pin and the spreads
- **Sources:**
  - ★ Codrops "Creating a smooth horizontal parallax gallery: from DOM to WebGL" (19 Feb 2026):
    https://tympanus.net/codrops/2026/02/19/creating-a-smooth-horizontal-parallax-gallery-from-dom-to-webgl/
    (demo https://tympanus.net/Tutorials/HorizontalParallaxGallery/index2.html)
    - The DOM version is enough: images at `width: 125%; left: -12.5%`, shifted by `translate3d(-t*10%)` from
      their distance to the centre.
    - The original is wheel-driven with a `lerp(…, 0.07)` and touch left out. Port it onto a ScrollTrigger pin.
  - Osmo "Horizontal scrolling sections": https://www.osmo.supply/resource/horizontal-scrolling-sections
  - GSAP docs on `containerAnimation`: https://gsap.com/docs/v3/Plugins/ScrollTrigger/
- **Stack:** ScrollTrigger `pin` + a linear tween, with `containerAnimation` for inner triggers.
- **Fit:** Med. It's a good showcase for shoot frames, but it's the most-copied pattern of 2020–2025, and it fights
  with the other pins. Use it once, in a case study, with a real reason (a film contact sheet).
- **Perf/a11y:**
  - Mobile: don't pin. Use a native horizontal `scroll-snap` row, set up with `gsap.matchMedia`.
  - Keyboard: the items must be reachable by Tab, and the section must scroll to keep the focused item visible.
  - Reduced motion: a normal grid.
  - `containerAnimation` triggers can't pin or snap (GSAP docs), and the container tween must use `ease: "none"`.
- **Sketch:**
  ```js
  const tween = gsap.to(track, { x: () => -(track.scrollWidth - innerWidth), ease: 'none',
    scrollTrigger: { trigger: section, pin: true, scrub: 0.5, end: () => '+=' + (track.scrollWidth - innerWidth), invalidateOnRefresh: true } })
  frames.forEach(f => gsap.fromTo(f.querySelector('img'), { xPercent: -8 }, { xPercent: 8, ease: 'none',
    scrollTrigger: { trigger: f, containerAnimation: tween, start: 'left right', end: 'right left', scrub: true } }))
  ```

#### 10. Stacking cards on scroll. Fit: High (as spreads), Med (as small cards)
- **Looks like:** Each card pins near the top; the next card slides up over it; earlier cards shrink slightly
  and dim, building a deck.
- **Where:** The home project spreads (full-screen variant, technique 5), or the /studio process cards
  (Listen, Map, Make, Launch) as index cards stacking.
- **Sources:**
  - ★ React Bits Scroll Stack (rebuilt 10 Oct 2026; native pinning, `itemScale`, `dimAmount`,
    `itemStackDistance`): https://reactbits.dev/components/scroll-stack. Note: it ships its *own* wheel smoothing
    (`smoothScroll` prop), so set `smoothScroll={false}` and `useWindowScroll` under Lenis.
  - Osmo "Stacking sticky cards (bounce)": https://www.osmo.supply/resource/stacking-sticky-cards-bounce
  - Skiper 16 / 17 (Motion / GSAP + rotate): https://skiper-ui.com/v1/skiper17
  - Codrops "On-scroll 3D stack motion" (2024): https://tympanus.net/Development/3DStackMotion/
  - Animata "Stacked sections": https://animata.design/docs/scroll/stacked-sections
- **Stack:** CSS sticky + ScrollTrigger scrub, or Motion `useScroll` + `useTransform`.
- **Fit:** High for spreads, because a pile of pages is on-concept. As generic "feature cards" it's Med, since it's
  common.
- **Perf/a11y:**
  - Avoid `filter: blur` on stacked cards; use an overlay's opacity instead.
  - Reduced motion: no scale or dim; sticky is optional.
  - Use `svh` heights to stop mobile jumps.
- **Sketch:**
  ```css
  .card { position: sticky; top: calc(10vh + var(--i) * 1.25rem); }
  ```
  ```js
  gsap.to(card, { scale: 1 - (n - i) * 0.04, ease: 'none', scrollTrigger: { trigger: card, start: 'top 10%', endTrigger: last, end: 'top 10%', scrub: true } })
  ```

#### 11. Deal-out: stack → collage (images "split off along their own paths"). Fit: High ★ signature
- **Looks like:** A project's images start as a neat stack of prints. As the spread enters, they deal out one by one,
  each on its own curved path, landing in a loose collage with a small rotation and a shadow settling under it.
  On leave they gather back. This is the crossroads idea at small scale: one pile, many roads.
- **Where:** The home project spreads (item 3), the case-study "stamps" block, and the /work "Stamps" view's first
  load.
- **Sources:**
  - ★ Codrops "Image stack entrance animations" (2024): https://tympanus.net/Development/EntranceAnimationForImages/
  - Codrops "Thumbnail flow animation with GSAP MotionPath" (4 Jun 2026):
    https://tympanus.net/codrops/2026/06/04/creating-a-thumbnail-flow-animation-with-gsap-motionpath/
  - Osmo "Dropping cards stack": https://www.osmo.supply/resource/dropping-cards-stack
  - React Bits Bounce Cards, a fan of photo cards that bounce in and spread (rebuilt on springs, 8 Oct 2026):
    https://reactbits.dev/components/bounce-cards
  - Animata "Card spread": https://animata.design/docs/card/card-spread
- **Stack:** GSAP timeline: `Flip` from stacked state to collage state, or per-card `motionPath` with
  `autoRotate: false` plus a final `rotate`.
- **Fit:** High. It's the most "Kavalu" way to present a project: paths splitting from one origin, and the work
  stays big.
- **Perf/a11y:**
  - Only 4–7 images per spread. Pre-size them with `aspect-ratio`.
  - Reduced motion: the collage layout is shown directly.
  - Mobile: a simpler two-column collage dealt with short y-offsets.
- **Sketch:**
  ```js
  const state = Flip.getState(prints)            // prints currently stacked (class .is-stacked)
  spread.classList.remove('is-stacked')          // CSS places them in collage slots (no CSS transforms)
  gsap.set(prints, { rotation: (i) => rots[i] }) // final tilt set through GSAP, so Flip reads and animates it
  Flip.from(state, { duration: 1.1, ease: 'expo.out', stagger: 0.07, absolute: true,
    onComplete: () => gsap.to(shadows, { opacity: 1, duration: 0.4 }) })
  // gotcha (Flip docs): set transforms through GSAP, not CSS classes, on Flip targets, because GSAP caches transform data
  ```
  (Trigger it with `ScrollTrigger.create({ trigger: spread, start: 'top 60%', onEnter, onLeaveBack })`.)

#### 12. Grid ↔ index view switch and "filter by road". Fit: High
- **Looks like:**
  - /work toggles between **Stamps** (a perforated grid) and **Index** (rows). Items glide to their new places
    and sizes instead of popping.
  - Filtering by road (Branding / Identity / Social / Film) slides the non-matching stamps out and closes the gaps.
- **Where:** /work, and the /scrapbook filters.
- **Sources:**
  - ★ Codrops "Animating responsive grid layout transitions with GSAP Flip" (20 Jan 2026):
    https://tympanus.net/codrops/2026/01/20/animating-responsive-grid-layout-transitions-with-gsap-flip/
    (demo https://tympanus.net/Tutorials/GridLayoutTransitions/). A `data-*` attribute switches the CSS grid
    columns, then `Flip.from(state, { duration: 0.8, ease: 'expo.inOut' })`, with an `animated` lock flag. Skip
    its v2 blur-and-brightness flash.
  - Codrops "Grid view switch animation" (2023): https://tympanus.net/Development/GridViewSwitch/
  - Osmo "Layout grid Flip": https://www.osmo.supply/resource/layout-grid-flip
  - Live references:
    - The Lookback (SOTD Mar 2026; timeline, surf and index views, each visible image flipping to its new slot):
      https://tlb.betteroff.studio/
    - Joffrey Spitzer (a slider ↔ grid Flip toggle): https://joffreyspitzer.com/
    - House of Yellow (visual grid ↔ data list with views and delivery time, good for social work):
      https://houseofyellow.nl/
  - GSAP Flip docs (`absolute`, `nested`, `onEnter`/`onLeave`, `prune`): https://gsap.com/docs/v3/Plugins/Flip/
- **Stack:** GSAP Flip. In React, capture the state before `setState`, then run `Flip.from` in a layout effect, or
  use Flip's batch API.
- **Fit:** High. It's the "smooth" quality of an expensive site, and the work stays visible during the change.
- **Perf/a11y:**
  - Run it only on the visible items (`prune: true`).
  - Move focus sensibly after filtering, and announce the result count in an `aria-live="polite"` region.
  - Reduced motion: instant swap.
- **Sketch:**
  ```js
  const state = Flip.getState('.stamp')
  flushSync(() => setView('index'))            // or setFilter(road)
  Flip.from(state, { duration: 0.8, ease: 'power3.inOut', absolute: true, nested: true, prune: true,
    onEnter: els => gsap.fromTo(els, { autoAlpha: 0, scale: 0.96 }, { autoAlpha: 1, scale: 1, duration: 0.5 }),
    onLeave: els => gsap.to(els, { autoAlpha: 0, scale: 0.96, duration: 0.3 }) })
  ```

#### 13. FLIP shared element: stamp → case-study cover (and back). Fit: High ★ signature
- **Looks like:** Clicking a stamp on /work makes that exact image lift and grow into the case-study cover,
  shedding its perforated edge. The rest of the page crossfades or slides beneath it. Going back, the cover
  shrinks into its stamp slot.
- **Where:** /work → /work/[slug], home spreads → case study, "next project" → case study.
- **Two ways to build it:**
  1. **Native (recommended first): React 19.3 `<ViewTransition name>` pairs + Next 16.4.**
     - Put the same `name={`stamp-${slug}`}` on the grid image and the case-study cover, and add
       `share="morph" default="none"` on both.
     - Customise it with `::view-transition-group(.morph) { animation-duration: 550ms }` and an image-pair
       keyframe (Next's guide uses a mid-flight `blur(3px)`; for Kavalu, try a perforation mask fading out
       instead).
     - It handles back navigation if both names exist.
     - Caveats from the React docs:
       - Only one mounted element may have a given name at a time.
       - No pair forms if either side is outside the viewport. Scroll the case-study cover to the top first,
         which Next does on navigation.
       - The morph only plays if the destination renders in the same commit, so prefetch or cache the
         case-study page. If it suspends into a fallback, you get an enter animation instead.
       - The morph is a *snapshot* (an image), so the live content inside doesn't animate.
  2. **GSAP Flip overlay (fallback or bespoke):**
     - On click, clone the image into a fixed `TransitionLayer` in the root layout at its rect
       (`Flip.getState(thumb)`), then `router.push`.
     - When the cover slot mounts (detected with a `usePathname` effect), call
       `Flip.fit(clone, coverSlot, { duration: 1.1, ease: 'power3.inOut', scale: false })`, then swap and remove
       the clone.
     - This gives full control (clip-path, perforation tear, counter-zoom) in every browser, but you own scroll
       reset, focus and cancellation.
- **Sources:**
  - ★ Next.js 16.4 guide "Designing view transitions" (shared-element morph, Suspense reveal, directional
    `transitionTypes`): https://nextjs.org/docs/app/guides/view-transitions; demo
    https://react-view-transitions-demo.labs.vercel.dev (code https://github.com/nextjs/react-view-transitions-demo)
  - React `<ViewTransition>` reference: https://react.dev/reference/react/ViewTransition
  - ★ Codrops "Building an infinite GSAP scroll gallery with parallax and Flip transitions" (30 Jul 2026):
    https://tympanus.net/codrops/2026/07/30/building-an-infinite-gsap-scroll-gallery-with-parallax-and-flip-transitions/
    (demo https://tympanus.net/Tutorials/InfiniteScrollGSAPGallery/). It's the most complete thumbnail →
    fullscreen recipe:
    - set `data-flip-id` *before* `Flip.getState`
    - `await img.decode()` before the morph
    - `Flip.from(state, { targets: preview, absolute: true, duration: 1.2, ease: 'power4.inOut' })`
    - close with `Flip.fit(preview, wrapper, { absolute: true })`
    - a closed/opening/open/closing state machine, with Esc reversing mid-open
  - Codrops "Recreating Palmer's draggable product grid" (Flip into a details panel):
    https://tympanus.net/codrops/2025/09/01/recreating-palmers-draggable-product-grid-with-gsap/
  - MERSI (Awwwards SOTD Apr 2026), the production reference for option 2: the cover is cloned into an overlay, a
    curtain wipes the old page, and `Flip.fit()` morphs the clone into the hero (1.2 s `expo.inOut`; Webflow +
    Taxi.js). https://www.mersi-architecture.com, with the making-of at
    https://tympanus.net/codrops/2026/07/27/between-print-and-digital-the-making-of-mersis-website/
  - Motion Primitives Morphing Dialog (a same-page `layout` morph, for an in-page "quick look"):
    https://motion-primitives.com/docs/morphing-dialog
- **Fit:** High. It's the single most important transition for "project visibility": the work never disappears
  between pages.
- **Perf/a11y:**
  - Move focus to the case-study `<h1>` after navigation, and keep the page title updated.
  - Reduced motion: VT durations of 0 (technique 14), or a 150 ms crossfade.
  - Don't leave both GSAP and VT animating the same element.
- **Sketch (native):**
  ```tsx
  // grid
  <Link href={`/work/${p.slug}`} transitionTypes={['nav-forward']}>
    <ViewTransition name={`stamp-${p.slug}`} share="morph" default="none"><Image ... /></ViewTransition>
  </Link>
  // case study
  <ViewTransition name={`stamp-${slug}`} share="morph" default="none"><div style={{ aspectRatio: '3/2', position: 'relative' }}><Image fill priority ... /></div></ViewTransition>
  ```
  ```css
  ::view-transition-group(.morph) { animation-duration: 550ms; animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1); }
  ```

#### 14. Page transitions: View Transitions API vs GSAP/Barba-style overlay. Fit: High
- **Options:**

  | | Native View Transitions (React `<ViewTransition>` + Next 16.4) | GSAP overlay (a "Barba-style" cover) |
  |---|---|---|
  | Setup | No flag in Next 16.4. Use `<Link transitionTypes={['nav-forward']}>` and `router.push(href, { transitionTypes })`. | A custom `<TransitionLink>` that blocks navigation, plays the cover, then `router.push`. A layout-level overlay reveals on the new `pathname`. |
  | What animates | Snapshots: old and new page images, plus named elements morphing. | Real DOM, including live video and scrubbing; anything you want. |
  | Strengths | Tiny JS. Interruptible. Shared-element morphs for free. Directional classes. Back button morph works when the names match. | Total art direction, the same in every browser. Can run a torn-paper wipe with real paper texture. |
  | Weaknesses | The outgoing page is a static snapshot. Clicks are swallowed during it unless you set `::view-transition { pointer-events: none }`. Safari differences. Popstate (back) doesn't carry types. | You own navigation timing, cancellation, focus, scroll reset and Lenis/ScrollTrigger teardown. It adds about 300–600 ms of perceived latency unless the cover and the fetch run in parallel. |
  | Browsers | Chrome 111+, Safari 18+, Firefox 144+ for same-document. Unsupported browsers just navigate. | All. |

- **Recommendation for Kavalu:**
  - **Native by default.** A "paper slide":
    - The new page arrives like a sheet laid on top: `translateY(24px)` → 0 with a 210 ms fade, after a 150 ms
      exit.
    - The header and folder tabs are anchored (`viewTransitionName: 'site-header'` with
      `animation: none`, as in Next's guide).
    - Stamp morphs come from technique 13.
  - **One GSAP overlay** only for the "Choose your road" → /start moment: the letter folds into an envelope
    (technique 30). Its old-page snapshot would look dead as a native transition.
- **Sources:**
  - ★ https://nextjs.org/docs/app/guides/view-transitions (the directional CSS, header anchoring,
    `pointer-events`, the reduced-motion block)
  - Codrops "Building parallel page transitions with GSAP and React Router" (8 Oct 2026):
    https://tympanus.net/codrops/2026/10/08/building-parallel-page-transitions-with-gsap-and-react-router/
    - Both routes stay mounted on one timeline, and the outgoing page is `inert`.
    - Callbacks receive `reduced: true` under reduced motion.
    - The author says the **Next.js App Router can't do parallel transitions**. His `next-transition-router`
      (npm 0.2.11, beta; `<TransitionRouter leave={…} enter={…}>`) does *sequential* leave → navigate → enter.
      That's the practical helper if Kavalu needs a GSAP overlay on App Router:
      https://github.com/ismamz/next-transition-router
  - Codrops "Building async page transitions in vanilla JavaScript" (26 Feb 2026):
    https://tympanus.net/codrops/2026/02/26/building-async-page-transitions-in-vanilla-javascript/
  - Codrops "Interlude: custom page transitions in Astro" (GSAP, loaded per link), for the transition catalogue
    idea: https://tympanus.net/codrops/2026/10/07/interlude-astro-page-transitions/
  - Osmo's page-transition set, for art direction: shutter, double wipe, masked window, curved wipe, draw-SVG
    page transition, stacked-cards page transition.
    https://www.osmo.supply/resource/draw-svg-page-transition and
    https://www.osmo.supply/resource/stacked-cards-page-transition
  - Codrops "Making CSS View Transitions easy with Velvette" (2024): https://tympanus.net/Tutorials/Velvette/
- **Perf/a11y:**
  - Keep the total under about 600 ms.
  - Focus `<main>` or the `<h1>` after navigation, and announce the route (Next does announce route changes).
  - Reduced-motion CSS, from Next's guide:
    `@media (prefers-reduced-motion: reduce){ ::view-transition-old(*), ::view-transition-new(*), ::view-transition-group(*){ animation-duration:0s !important; animation-delay:0s !important } }`
- **Sketch (native paper slide):**
  ```tsx
  // in each page.tsx (not layout)
  <ViewTransition default="none" enter={{ 'nav-forward': 'paper-in', 'nav-back': 'paper-back', default: 'none' }}
                  exit={{ 'nav-forward': 'paper-out', 'nav-back': 'paper-out', default: 'none' }}>
  ```
  ```css
  ::view-transition-old(.paper-out) { animation: 150ms cubic-bezier(0.32,0,0.67,0) both fade-out; }
  ::view-transition-new(.paper-in)  { animation: 420ms cubic-bezier(0.16,1,0.3,1) 120ms both paper-in; }
  @keyframes paper-in { from { opacity: 0; translate: 0 24px; rotate: 0.4deg } to { opacity: 1; translate: 0; rotate: 0 } }
  /* .paper-back: the same thing with translate: 0 -24px (the sheet comes back from above) */
  ```

#### 15. React Bits gallery components: review for this site
All of these were read from source at https://github.com/DavidHDev/react-bits (`src/content/...`) on 23 Oct
2026. Most were rebuilt 8–13 Oct 2026, and many now have **no dependencies**. The licence is MIT + Commons
Clause, which is fine for the site.

| Component | What it is now (source-verified) | Tech | Fit for Kavalu | Use as |
|---|---|---|---|---|
| **Stack** https://reactbits.dev/components/stack | A pile of cards you drag, flick or click through; thrown cards tuck underneath. `layout="fan"`, `tilt`, `frame` (white print border!), autoplay, keyboard support. | `motion/react` springs, `useReducedMotion` | **High**: a pile of polaroids from a shoot; "flick through the contact prints" | Case-study shoot block; a founder's "favourite frames" pile |
| **Masonry** https://reactbits.dev/components/masonry | Springy reflow, reveal-on-scroll tiles, hover zoom/lift/tilt, captions, lightbox, drag to reorder; columns follow the container. | No dependencies (Hugeicons for UI) | **Med-High**: the /scrapbook *grid view* (the mobile, keyboard and reduced-motion fallback) | Reference for the fallback grid; turn off reorder and hover tilt |
| **Folder** https://reactbits.dev/components/folder | Drops its flap open or opens like a book; pages rise under the cursor; solid/glass/matte; tab position. | No dependencies; WebGL for the glass variant | **High (concept)**: the folder-tab motif | Study it for the footer and nav folder tabs; re-skin as kraft paper with a powder-blue tab |
| **Tilted Card** https://reactbits.dev/components/tilted-card | 3D tilt toward the cursor with glare, soft shadow, floating depth layers, a flip side, gyroscope support; album/gallery/ticket demos. | No dependencies | **Med**: a subtle tilt on a held-up stamp in the Index-view cursor preview, at most 6° | Set `glare` low or 0 (paper isn't glossy) |
| **Bounce Cards** https://reactbits.dev/components/bounce-cards | A fan of photo cards that bounce in, spread, and straighten the hovered one. | Springs, no dependencies | **Med**: fine as a project teaser on the home "four roads" cards | Reduce the bounce for this brand |
| **Circular Gallery** https://reactbits.dev/components/circular-gallery | A curved draggable/scrollable/tabbable gallery; cards open to the full image; rebuilt without dependencies. | Custom WebGL in a canvas | **Low-Med**: a carousel ring reads "template 2025" | Skip, or use at most once for an archive |
| **Dome Gallery** https://reactbits.dev/components/dome-gallery | Images projected on a draggable 3D hemisphere; click to enlarge. | `@use-gesture/react`, CSS 3D | **Low**: spectacle over legibility; fights the paper concept | Skip |
| **Infinite Menu** https://reactbits.dev/components/infinite-menu | A draggable sphere of image tiles that snaps the nearest one forward. | WebGL | **Low**: tech-demo energy | Skip |
| **Flowing Menu** https://reactbits.dev/components/flowing-menu | A full-height menu where a liquid band glides between rows, revealing a marquee of each item; keyboard support. | No dependencies | **Med**: a full-screen nav or the Index view of /work | Use the "editorial" layout with the marquee off; the liquid band could become a strip of washi tape |
| **Card Swap** https://reactbits.dev/components/card-swap | A 3D stack that sends the front card to the back on a timer or fling. | Springs | **Low-Med**: auto-rotating stacks are attention-seekers | Only user-driven, never on a timer |
| **Circular / Depth Carousel**, **Infinite Spiral**, **Drift Wall**, **Flying Posters**, **Lanyard** | 3D rings, rails, helices, perspective walls, a swinging badge | WebGL/CSS 3D | **Low**: these read as 2025–26 component-library demos | Skip |
| **Accordion Gallery** https://reactbits.dev/components/accordion-gallery | Panels expand on hover/focus with parallax imagery and captions. | GSAP; handles reduced motion | **Med**: the "four roads" alternative layout | Optional |
| **Image Trail** https://reactbits.dev/animations/image-trail | One tunable cursor trail (size, lifetime, zoom, drift, rotation, `stack` pile), with presets. | GSAP | **Med-High**: see technique 24 | Use a "stack pile" preset with paper rotation |
| **Sticker Peel** https://reactbits.dev/animations/sticker-peel | A die-cut sticker that peels at the edge nearest the cursor, drags, throws and swings; gloss/matte/holographic. | WebGL2 canvas, no dependencies | **High (concept)**: see technique 27 | Matte finish only |
| **Tear Ticket** https://reactbits.dev/micro/tear-ticket | A ticket whose perforated stub tears off fibre by fibre and drops away; `holes`, `roughness`, `tearAngle`, `ariaLabel`. | `motion/react` | **High**: perforation, which is the stamp motif | The "Book a call" stub, or tearing a stamp off the sheet in /start |
| **Paper Crumple** https://reactbits.dev/micro/paper-crumple | An image that crumples into a textured 3D sheet while you hold and drag. | three.js | **Low-Med**: fun, but heavy | 404 page at most |
| **Fold Text** https://reactbits.dev/text-animations/fold-text | Lines unfold like creased paper (`foldStyle="paper"`, `creaseShading`, `hinge`). | GSAP + ScrollTrigger | **High**: see technique 21 | Chapter titles |
| **Scroll Expand** https://reactbits.dev/animations/scroll-expand | A rounded media frame that grows to full bleed through the viewport (`clip-path inset` + inner zoom). | No dependencies | **High**: a reference for technique 4 | Port the maths to GSAP |
| **Noise** https://reactbits.dev/animations/noise | Film-grain overlay (canvas tile, `fps`, `blendMode`, dust, scratches); pauses when hidden. | Canvas 2D | **Med-High**: see technique 36 | Grain only; no scratches or scanlines |
| **Counter / Count Up** https://reactbits.dev/components/counter | An odometer with rolling digits; locales and currency. | No dependencies / Motion | **Med**: see technique 39 | — |
| **Falling Text** https://reactbits.dev/text-animations/falling-text | Words tumble into a draggable physics pile. | matter-js | **Med**: a playful footer or 404 | — |
| **Scroll Velocity** https://reactbits.dev/text-animations/scroll-velocity | Rows lean and stretch with scroll speed; drag with inertia. | Motion | **Med**: see technique 20 | — |
| **Text Type** https://reactbits.dev/text-animations/text-type | A typewriter with a bar/block/underscore cursor, optional typos. | GSAP | **Med-High**: typewriter labels | No fake typos on a brand site |

### D. Type

#### 16. Text reveals with SplitText: line and word masks, char stagger, and accessibility. Fit: High
- **Looks like:**
  - Display lines rise out of an invisible slot, the classic editorial reveal (lines masked, `yPercent: 100 → 0`).
  - The manifesto reveals word by word, with small inline image pills popping in after key phrases.
  - Per-character stagger is kept for one or two display words (ಕವಲು, chapter names).
- **Where:**
  - hero headline (lines)
  - manifesto (words, scrubbed)
  - chapter titles on case studies (lines)
  - footer wordmark (chars, once)
- **Sources:**
  - ★ GSAP SplitText docs (3.13 rewrite): `mask`, `autoSplit`, `onSplit`, `aria`, `deepSlice`, `propIndex`,
    `smartWrap`. https://gsap.com/docs/v3/Plugins/SplitText/
  - Codrops "From SplitText to MorphSVG: 5 creative demos using free GSAP plugins" (Osmo, 14 May 2025):
    https://tympanus.net/codrops/2025/05/14/from-splittext-to-morphsvg-5-creative-demos-using-free-gsap-plugins/
  - Codrops "7 must-know GSAP tips". Masking lines instead of chars cuts the DOM size (19 elements against 34 in
    their example):
    https://tympanus.net/codrops/2025/09/03/7-must-know-gsap-animation-tips-for-creative-developers/
  - Osmo "Masked text reveal", "Solve cut-off letters (SplitText)" and "Highlight text on scroll":
    https://www.osmo.supply/resource/masked-text-reveal ·
    https://www.osmo.supply/resource/solve-cut-off-letters-split-text
  - Codrops "Some on-scroll text highlight animations": https://tympanus.net/Development/OnScrollTextHighlight/
  - React Bits Split Text, Scroll Reveal and Scroll Float (GSAP; rebuilt 13 Oct 2026):
    https://reactbits.dev/text-animations/split-text
- **Stack:** GSAP SplitText + ScrollTrigger.
- **Fit:** High. Type is half the brand, and masked lines are the most "premium editorial" move there is, *if*
  you ration them.
- **Perf/a11y:**
  - `aria: "auto"` (the default) puts an `aria-label` on the parent and `aria-hidden` on the pieces. For text
    with links or `<em>` inside, use `aria: "none"` plus a visually-hidden copy (per the docs).
  - Split after `document.fonts.ready`, or set `autoSplit: true` and create the tween *inside* `onSplit` (and
    return it), so re-splits on resize keep their progress.
  - Avoid `text-wrap: balance` on split text. Use `font-kerning: none` if the kerning shifts.
  - Revert after a one-time reveal (`onComplete: () => split.revert()`) to restore the DOM for SEO and
    selection.
  - Never split body copy. Reduced motion: no split; the text is simply there.
  - CLS: masks are `overflow: clip` wrappers on lines that already exist, so there's no layout change.
  - Masked descenders (g, y, ಕ) can clip. Add `padding-block: 0.1em; margin-block: -0.1em` to the mask (the
    Osmo cut-off fix).
- **Sketch:**
  ```js
  SplitText.create(h1, { type: 'lines', mask: 'lines', autoSplit: true,
    onSplit: (self) => gsap.from(self.lines, { yPercent: 100, duration: 0.9, ease: 'expo.out', stagger: 0.08,
      scrollTrigger: { trigger: h1, start: 'top 85%', once: true } }) })
  // manifesto (scrubbed words): ink in from 18% to 100% opacity as you read
  SplitText.create(p, { type: 'words', autoSplit: true, onSplit: (s) =>
    gsap.fromTo(s.words, { opacity: 0.18 }, { opacity: 1, stagger: 0.1, ease: 'none',
      scrollTrigger: { trigger: p, start: 'top 75%', end: 'bottom 45%', scrub: true } }) })
  ```

#### 17. Scramble and typewriter labels. Fit: Med-High (as labels), Low (as headlines)
- **Looks like:** The typewriter labels on spreads (client, year, roads) type on or briefly scramble through
  mono glyphs before settling, like a label maker. They stay short and quiet.
- **Where:** Project metadata labels, index-view row numbers, the live "Bengaluru 14:32" clock in the footer,
  form confirmation ("Letter sent.").
- **Sources:**
  - ★ GSAP ScrambleTextPlugin: https://gsap.com/docs/v3/Plugins/ScrambleTextPlugin/
  - GSAP TextPlugin, for typewriting
  - React Bits Text Type (cursor styles; avoid the fake-typo option):
    https://reactbits.dev/text-animations/text-type
  - React Bits Decrypted Text / Scrambled Text / Shuffle
  - Osmo "Text scramble on load, scroll and hover": https://www.osmo.supply/resource/text-scramble-load-scroll-hover
  - Motion Primitives Text Scramble: https://motion-primitives.com/docs/text-scramble
  - Magic UI Hyper Text: https://magicui.design/docs/components/hyper-text
- **Stack:** GSAP ScrambleTextPlugin or TextPlugin, in a mono typewriter face (for example, Recursive with `MONO 1`,
  or Courier Prime).
- **Fit:** Med-High for 1–3-word labels, where it echoes the typewriter card. Low for headlines: scramble on
  big type reads "tech startup".
- **Perf/a11y:**
  - Put the real text in the DOM and `aria-label` on the element. Animate a child marked `aria-hidden`, so screen
    readers don't hear random glyphs.
  - Lock the width (`ch` units, `tabular-nums`) so letters don't jitter. That avoids CLS.
  - Reduced motion: show the final text instantly.
- **Sketch:**
  ```js
  gsap.to(labelInner, { duration: 0.8, scrambleText: { text: 'Packaging · 2026', chars: 'upperCase', speed: 0.6, revealDelay: 0.2 },
    scrollTrigger: { trigger: label, start: 'top 90%', once: true } })
  ```

#### 18. Variable-font hover and proximity effects. Fit: Med-High
- **Looks like:** Nav items and index-view titles subtly change *character* under the cursor rather than just
  colour: a serif softens and gets wonky, a hand font gets bouncier. The best version is a proximity field, where
  letters near the cursor shift axes.
- **Fonts worth testing.** I checked their axes against Google Fonts metadata on 23 Oct 2026:

  | Font | Axes | What it gives Kavalu |
  |---|---|---|
  | **Fraunces** | `SOFT` 0–100, `WONK` 0–1, `opsz` 9–144, `wght` 100–900 | A soft, slightly quirky serif. Animating `SOFT` and `WONK` changes the mood without changing the width much. |
  | **Shantell Sans** | `BNCE` −100–100, `INFM` 0–100, `SPAC`, `wght` 300–800 | Marker handwriting with "bounce" and "informality" axes. Ideal for the founder's margin notes, which can come alive on hover. |
  | **Recursive** | `MONO` 0–1, `CASL` 0–1, `CRSV`, `slnt`, `wght` 300–1000 | Typewriter-mono to casual. It suits the label cards. |
  | **Anek Kannada** | `wdth` 75–125, `wght` 100–800 | Kannada with width and weight axes, for an expressive ಕವಲು wordmark. |
  | **Noto Sans Kannada** | `wdth` 62.5–100, `wght` 100–900 | Kannada with width and weight axes. |

- **Where:** The nav and folder-tab labels (`wght` + `SOFT` on hover), /work Index rows, the founder's
  handwritten notes (`BNCE` wiggle on hover), and the ಕವಲು wordmark (`wdth` breathing on scroll, once).
- **Sources:**
  - ★ Osmo "Variable font weight hover": https://www.osmo.supply/resource/variable-font-weight-hover
  - React Bits Variable Proximity, which says letters "no longer rewrap while letters change weight" (13 Oct
    2026): https://reactbits.dev/text-animations/variable-proximity
  - React Bits Text Pressure (Roboto Flex `wdth`/`wght`/`ital`): https://reactbits.dev/text-animations/text-pressure
- **Stack:** CSS custom properties fed into `font-variation-settings` (or `font-weight`/`font-stretch`), animated
  by CSS transitions or `gsap.quickTo` on the variables.
- **Fit:** Med-High. It's tactile, typographic and cheap, and it signals a type-literate studio. Keep it on
  labels and wordmarks.
- **Perf/a11y:**
  - `wght` and `wdth` change the advance widths, so lines reflow. Use it on `inline-block` items with a fixed
    width, or pick axes that keep metrics (`SOFT`, `WONK`, `BNCE`, `INFM`, `GRAD` in Roboto Flex).
  - Subset the fonts. Variable Kannada files are large, so load only the wordmark glyphs for the hero.
  - Reduced motion: no proximity field; a static weight change on hover is fine.
  - Touch: none.
- **Sketch:**
  ```css
  .tab { font-variation-settings: "wght" var(--w, 420), "SOFT" var(--s, 0); transition: --w .25s var(--ease-ui), --s .25s var(--ease-ui); }
  .tab:hover, .tab:focus-visible { --w: 560; --s: 100; }
  /* register --w and --s with @property { syntax: '<number>' } so they interpolate */
  ```

#### 19. Hand-drawn annotations: underline, circle and bracket that draw themselves. Fit: High
- **Looks like:**
  - Ananya's pen marks key words. A wobbly underline draws under "road", a loose circle around "crossroads",
    a bracket beside a quote.
  - On hover, links get a *different* scribble underline each time.
- **Where:** Hero emphasis words, manifesto keywords, the founder quote, nav and link hovers, form field focus
  (circling the chosen option in the onboarding letter).
- **Sources:**
  - ★ Osmo "Draw random underline": six SVG variants, DrawSVG, drawn out on leave.
    https://www.osmo.supply/resource/draw-random-underline
  - The same idea as a CodePen, from the Codrops free-plugins article: https://codepen.io/osmosupply/pen/qEEKRrx
  - Magic UI Highlighter, which wraps `rough-notation` (highlight, circle, box, bracket, strike-through,
    underline, `iterations`, `isView`): https://magicui.design/docs/components/highlighter
  - Osmo "Highlight marker text reveal": https://www.osmo.supply/resource/highlight-marker-text-reveal
  - Cult UI Squiggle Arrow (static hand-drawn SVG arrows in wavy, bouncy and smooth styles; animate with DrawSVG):
    https://www.cult-ui.com/docs/components/squiggle-arrow
- **Stack:** Hand-drawn SVG paths (draw them with a real pen on a tablet, then export) + DrawSVGPlugin; or
  `rough-notation` for generated strokes.
- **Fit:** High. It's handwriting, it's the founder's voice, and it's cheap. Real, hand-made SVG strokes beat
  generated ones for authenticity.
- **Perf/a11y:**
  - The SVGs are decorative (`aria-hidden`). Keep emphasis semantic too, with `<em>` or `<mark>`.
  - Reduced motion: show the marks already drawn.
  - DrawSVG notes: Firefox sometimes stops short, so draw to `102%` (a docs tip). iOS can render `<rect>`
    strokes wrongly, so use paths.
- **Sketch:**
  ```js
  const variants = gsap.utils.toArray('.scribble path')
  link.addEventListener('pointerenter', () => { const p = gsap.utils.random(variants); gsap.fromTo(p, { drawSVG: '0%' }, { drawSVG: '102%', duration: 0.5, ease: 'power2.out' }) })
  link.addEventListener('pointerleave', () => gsap.to(current, { drawSVG: '100% 100%', duration: 0.35, ease: 'power2.in' }))
  ```

#### 20. Velocity-reactive marquee. Fit: Med
- **Looks like:** A slow ribbon of words or client logos ("Branding · Packaging · Social · Shoots ·") drifts. Scroll
  faster and it surges and leans, then eases back. Reverse scroll reverses it.
- **Where:** One place only, a thin washi-tape strip between the spreads and the manifesto, or the footer
  ("Let's choose a road →").
- **Sources:**
  - ★ GSAP `horizontalLoop` helper (seamlessLoop; `draggable`, `center`, `snap`, `toIndex`):
    https://gsap.com/docs/v3/HelperFunctions/helpers/seamlessLoop
  - React Bits Scroll Velocity (lean and stretch with speed, drag with inertia, `skewWithVelocity`):
    https://reactbits.dev/text-animations/scroll-velocity
  - Magic UI Scroll Based Velocity (Motion): https://magicui.design/docs/components/scroll-based-velocity
  - Osmo "Marquee with scroll direction": https://www.osmo.supply/resource/marquee-with-scroll-direction
  - Codrops "Infinite marquee along an SVG path with React + Motion" (17 Jun 2025):
    https://tympanus.net/codrops/2025/06/17/building-an-infinite-marquee-along-an-svg-path-with-react-motion/
- **Stack:** GSAP loop timeline, whose `timeScale` is tweened from ScrollTrigger `getVelocity()` (or Lenis
  `velocity`).
- **Fit:** Med. It's a recognisable 2020s trope. On-brand only if it's styled as tape or a label strip, slow, and
  used once.
- **Perf/a11y:**
  - **WCAG 2.2.2:** moving content that lasts more than 5 s needs a pause control. Pause on hover and focus, and
    stop it entirely under reduced motion.
  - Clones need `aria-hidden="true"`. Pause it off-screen (ScrollTrigger `onToggle`).
  - Transform only, so no CLS.
- **Sketch:**
  ```js
  const loop = horizontalLoop(items, { repeat: -1, speed: 0.6 })
  let boost = gsap.quickTo(loop, 'timeScale', { duration: 0.6, ease: 'power3' })
  ScrollTrigger.create({ onUpdate: (self) => boost(gsap.utils.clamp(-4, 4, 1 + self.getVelocity() / 400)) })
  // settle back: on scrollEnd -> boost(Math.sign(loop.timeScale()) || 1)
  ```

#### 21. Paper-fold headings (lines unfold like creased paper). Fit: Med-High
- **Looks like:** A chapter title unfolds from a crease: each line (or letter) rotates down from a top hinge, with
  shading on the crease, like a folded note opened flat.
- **Where:** /studio chapter titles ("Listen / Map / Make / Launch"), and the onboarding letter's greeting.
- **Sources:**
  - ★ React Bits Fold Text (`foldStyle="paper"`, `hinge`, `creaseShading`, `perspective`, GSAP + ScrollTrigger):
    https://reactbits.dev/text-animations/fold-text
  - Codrops "PFold" (an old CSS-3D precedent): https://tympanus.net/codrops/2012/10/17/pfold-paper-like-unfolding-effect/
- **Stack:** SplitText lines + CSS 3D (`rotateX`, `transform-origin: top`, `perspective`) + a gradient overlay for the
  crease.
- **Fit:** Med-High. It's a paper verb applied to type. Use it on 2–3 titles at most, because it's showy.
- **Perf/a11y:**
  - It's 3D on text, so keep the perspective large (≥ 700 px).
  - Reduced motion: plain text.
  - The `aria` handling is as in technique 16.

### E. Pointer

#### 22. Magnetic buttons. Fit: Med
- **Looks like:** Primary buttons (Book a call, Send letter, Start here) lean toward the cursor within a small
  radius, and the label moves a bit further than the pill. On leave they spring back.
- **Where:** 2–4 primary CTAs only. Never nav links or the form fields.
- **Sources:**
  - ★ Osmo "Magnetic hover effect": https://www.osmo.supply/resource/magnetic-hover-effect
  - React Bits Magnet (a real spring, axis lock, a movement cap; only the nearest magnet reacts):
    https://reactbits.dev/animations/magnet
  - Aceternity Magnetic Button (Motion spring `stiffness 150, damping 25, mass 0.1`, `maxDistance` clamp):
    https://ui.aceternity.com/components/magnetic-button
  - Motion Primitives Magnetic: https://motion-primitives.com/docs/magnetic
- **Stack:** `gsap.quickTo` on `x` and `y`, or Motion `useSpring`.
- **Fit:** Med. It's a nice tactile detail, but it's on the 2026 cliché list when it's put on everything. Ration it.
- **Perf/a11y:**
  - Fine pointers only (`(hover: hover) and (pointer: fine)`).
  - Keep the hit area unchanged, and never move a focused button.
  - Reduced motion: off.
- **Sketch:**
  ```js
  const xTo = gsap.quickTo(btn, 'x', { duration: 0.5, ease: 'power3' }), yTo = gsap.quickTo(btn, 'y', { duration: 0.5, ease: 'power3' })
  btn.onpointermove = (e) => { const r = rect /* cached on pointerenter */; xTo((e.clientX - r.left - r.width / 2) * 0.3); yTo((e.clientY - r.top - r.height / 2) * 0.3) }
  btn.onpointerleave = () => { gsap.to(btn, { x: 0, y: 0, duration: 0.6, ease: 'power3.out' }) }
  // allow a small 'elastic.out(1, 0.6)' only on the playful "Send letter" CTA; elsewhere no overshoot (see the anti-list)
  ```

#### 23. Cursor follower with a project image preview (the Index view). Fit: High
- **Looks like:** In the /work Index view (rows of names), hovering a row brings in that project's stamp. It follows the
  cursor with lag, slightly turned like a photo held up (±3–5°, tilting with the cursor's velocity), and swaps with a
  quick clip or flip when moving to the next row.
- **Where:** /work Index view, the home "four roads" list, and Journal lists.
- **Sources:**
  - ★ Osmo "Image preview cursor follower": https://www.osmo.supply/resource/image-preview-cursor-follower
  - Osmo "Velocity-based custom cursor": https://www.osmo.supply/resource/velocity-based-custom-cursor
  - Osmo "Directional list hover": https://www.osmo.supply/resource/directional-list-hover
  - Aceternity Following Pointer: https://ui.aceternity.com/components/following-pointer
  - Skiper 6 "Hover members": https://skiper-ui.com/v1/skiper6
  - Codrops "Grid item hover effect" (2023): https://tympanus.net/Development/GridItemHoverEffect/
- **Stack:** One fixed `div` with stacked `<img>`s; `gsap.quickTo(x/y)` from pointer events; rotation from the
  velocity (`gsap.utils.clamp`).
- **Fit:** High, because the design direction asks for it and it shows work without leaving the list. **But** "an
  image floating under the cursor in work lists" is now one of the most templated award-site patterns (section 5b).
  Earn it with Kavalu specifics:
  - the *perforated stamp*, not a bare rectangle
  - the held-photo tilt driven by cursor velocity
  - a small typewriter caption
  - the same stamp then morphs into the case-study cover on click (technique 13)
- **Perf/a11y:**
  - Preload the stamp thumbnails when the Index view mounts (`decode()`), so the first hover isn't blank.
  - Decorative: `aria-hidden`, `pointer-events: none`. Each row is still a real link with a visible title, so
    keyboard focus shows the stamp inline (anchored beside the row) instead of following a cursor.
  - Touch: tapping goes straight to the page. Reduced motion: no follow; the preview sits in a fixed spot.
- **Sketch:**
  ```js
  const xTo = gsap.quickTo(preview, 'x', { duration: 0.45, ease: 'power3' }), yTo = gsap.quickTo(preview, 'y', { duration: 0.45, ease: 'power3' })
  const rTo = gsap.quickTo(preview, 'rotation', { duration: 0.6, ease: 'power3' })
  let lastX = 0
  onPointerMove = (e) => { xTo(e.clientX); yTo(e.clientY); rTo(gsap.utils.clamp(-6, 6, (e.clientX - lastX) * 0.4)); lastX = e.clientX }
  row.onpointerenter = () => { setActive(i); gsap.to(preview, { autoAlpha: 1, scale: 1, duration: 0.35, ease: 'expo.out', easeReverse: 'power2.in' }) }
  ```

#### 24. Hover image trail. Fit: Med
- **Looks like:** Moving the cursor across a zone drops a short trail of project prints that land and fade. The
  Kavalu variant leaves a small *pile* of polaroids with random tilt, as if they'd been tossed on a desk.
- **Where:** The 404 page or the "From the scrapbook" teaser. Optionally the footer's "big wordmark" zone. Not the
  hero, where it fights the work.
- **Sources:**
  - ★ React Bits Image Trail (one tunable trail; `stack` pile, `rotation`, `drift`, `lifetime`; GSAP):
    https://reactbits.dev/animations/image-trail
  - Codrops "Made with GSAP: a fun gravity-based mouse trail" (20 May 2026): prints pop in, drift, fall, bounce
    and drop away (`elastic.out(2, 0.6)` / `back.in`); demo https://madewithgsap.com/codrops.
    https://tympanus.net/codrops/2026/05/20/made-with-gsap-building-a-fun-gravity-based-mouse-trail/
  - Codrops "Ideas for image motion trail animations" (2023): https://tympanus.net/Development/MotionTrailAnimations/
  - Osmo "Stacking image trail" and "Rotating image trail":
    https://www.osmo.supply/resource/stacking-image-trail
  - Codrops "Custom-shaped cursor trail" (ink dragged across paper, WebGPU/TSL, 24 Sep 2026):
    https://tympanus.net/codrops/2026/09/24/custom-shaped-cursor-trail/
  - Animata Trailing Image (`motion/react`, distance `threshold`, `excludeRefs`; the trail layer is
    `aria-hidden` and `pointer-events-none`): https://animata.design/docs/image/trailing-image
  - Paper-native trail variants from award sites:
    - LAX Space (HM 2025): the cursor unrolls a strip of duct tape. A **2D washi-tape trail** is the Kavalu
      version. https://www.laxspace.co/
    - Ten Years Away (SOTD Jun 2026): a halftone-dot cursor trail. https://ten.375.studio/en
- **Stack:** A pool of 8–12 `<img>` elements recycled in a ring buffer + GSAP timelines, spawning by distance
  (`|dx| + |dy| > threshold`).
- **Fit:** Med. It's fun and on-concept as a pile, but overused as a hero gimmick (see the anti-list).
- **Perf/a11y:**
  - Preload the sources first. The Codrops demo uses hidden `<img>` tags, so spawns don't stall.
  - Recycle nodes and don't create one per move.
  - Decorative. Fine pointers only. Reduced motion: off.
- **Sketch:**
  ```js
  if (dist > 90) { const img = pool[i++ % pool.length]
    gsap.timeline().set(img, { x, y, rotation: gsap.utils.random(-12, 12), scale: 0.6, autoAlpha: 1, zIndex: z++ })
      .to(img, { scale: 1, duration: 0.4, ease: 'back.out(1.6)' })
      .to(img, { autoAlpha: 0, duration: 0.6, ease: 'power2.in' }, '+=0.8') }
  ```

### F. Paper and tactile

#### 25. Draggable infinite scrapbook desk: inertia, pinch-zoom, wrap. Fit: High ★ signature
- **Looks like:** A plum desk covered in references, swatches, notes, polaroids and stickers. You grab anywhere and
  throw it; it glides with inertia and wraps endlessly. Pieces lag a little by depth, so the closer ones move more.
  You can wheel or pinch to zoom out for an overview and zoom back in to a piece. Clicking a piece lifts it into a
  focused view (Flip).
- **Where:** /scrapbook (the full experience), and "From the scrapbook" on the home page (a bounded, non-infinite
  mini desk you can "push around").
- **Sources:**
  - ★ Codrops "Building an infinite parallax grid with GSAP and seamless tiling" (11 Jun 2025): a DOM collage laid
    out in Figma, duplicated 2×2 for wrapping, a rAF lerp, per-tile random lag, a mouse offset, an intro fly-out.
    https://tympanus.net/codrops/2025/06/11/building-an-infinite-parallax-grid-with-gsap-and-seamless-tiling/
    (demo https://tympanus.net/Tutorials/InfiniteLayersGrid, repo https://github.com/JorgeCapillo/infinite-layers-grid)
  - Codrops "Recreating Palmer's draggable product grid with GSAP": `Draggable.create(grid, { type: 'x,y', bounds,
    inertia: true, edgeResistance: 0.9 })`, wheel clamped to bounds, Flip into a detail panel.
    https://tympanus.net/codrops/2025/09/01/recreating-palmers-draggable-product-grid-with-gsap/
  - Codrops "Infinite canvas: a seamless, pan-anywhere image space" (7 Jan 2026), the R3F/WebGL version with
    chunk streaming, drag-pan and wheel/pinch zoom, DPR caps and `Suspense fallback={null}`:
    https://tympanus.net/codrops/2026/01/07/infinite-canvas-building-a-seamless-pan-anywhere-image-space/
    (repo https://github.com/edoardolunardi/infinite-canvas)
  - Osmo "Infinite draggable grid (basic / masonry)":
    https://www.osmo.supply/resource/infinite-draggable-grid-basic
  - Skiper 73 "Infinite canvas" (paid): https://skiper-ui.com/v1/skiper73
  - Digital Stamp Collection, a loose draggable field where selecting a stamp brings it under a loupe, operable
    with arrow keys too. It's a keyboard-friendly precedent on the same stack: https://marijanapav.com/stamps
- **Stack:**
  - DOM, not WebGL: real cards keep text crisp, accessible and selectable, and paper shadows work.
  - Panning: either GSAP Draggable on a proxy with `inertia: true`, wrapping positions with `gsap.utils.wrap`, or
    a custom pointer + lerp loop on the GSAP ticker.
  - Zoom: `@use-gesture/react` `useGesture({ onDrag, onPinch, onWheel })`, or Pointer Events with two active
    pointers. Trackpad pinch arrives as `wheel` with `ctrlKey`.
- **Fit:** High. It's the scrapbook made literal, and the design direction already specifies it.
- **Perf/a11y:**
  - Virtualise: render only the tiles near the viewport. Codrops recommends IntersectionObserver or viewport
    checks past about 50–80 items. Use `loading="lazy"`, `decoding="async"` and fixed `aspect-ratio`.
  - Put `touch-action: none` on the canvas only, and `data-lenis-prevent` so Lenis ignores it.
  - Keyboard: Tab moves through the pieces, the canvas pans to the focused one, arrow keys pan and `+`/`−` zoom.
  - The **grid view** (per the design direction) is the fallback for mobile, reduced motion and screen readers.
    Use the same data as a CSS grid list (React Bits Masonry is a reference).
  - Use clamped zoom, and zoom about the pointer focal point (translate by `(1 - k) * (focal - pan)`).
- **Sketch:**
  ```js
  // tick (gsap.ticker): current += (target - current) * 0.08 ; wrap each tile
  tiles.forEach(t => { const x = gsap.utils.wrap(-t.w, tileW - t.w, t.x + current.x * t.depth); gsap.set(t.el, { x, y: ..., scale: zoom }) })
  // drag + inertia via Draggable on an invisible proxy
  Draggable.create(proxy, { type: 'x,y', trigger: desk, inertia: true, onDrag: sync, onThrowUpdate: sync })
  // pinch / ctrl+wheel
  useGesture({ onPinch: ({ offset: [s], origin }) => zoomTo(clamp(0.5, 2, s), origin),
               onWheel: ({ event, delta: [, dy] }) => event.ctrlKey && zoomBy(-dy * 0.01, event) }, { target: deskRef, eventOptions: { passive: false } })
  ```

#### 26. Stickers you can move: GSAP Draggable stickers, and matter.js physics stickers. Fit: High (Draggable), Med (physics)
- **Looks like:**
  - **Draggable:** round "Kavalu" stickers and washi-tape bits sit on sections. Grab one and it lifts, grows a
    drop shadow and tilts. Let go and it settles with a little bounce, staying where you put it (remember
    positions in `localStorage`).
  - **Physics:** in the footer, a jar's worth of stickers (Branding, Packaging, Social, Shoots, ಕವಲು) tumble in and
    pile up. You can throw them around, and they collide.
- **Where:**
  - Draggable: 1–2 stickers per page at most (the hero album page, the founder section).
  - Physics: the footer "sticker drawer", or the 404 page.
- **Sources:**
  - ★ Osmo "Draggable stickers" (Draggable `dragResistance: 0.1`, press tilt and scale, release `back.out(3)`):
    https://www.osmo.supply/resource/draggable-stickers
  - Osmo "Falling 2D objects (Matter.js)": https://www.osmo.supply/resource/falling-2d-objects-matterjs
  - React Bits Falling Text and Folder Float (both use `matter-js`): https://reactbits.dev/text-animations/falling-text ·
    https://reactbits.dev/micro/folder-float
  - Aceternity Draggable Card (Motion `drag` + velocity throw + tilt; the "Polaroid collection" demo):
    https://ui.aceternity.com/components/draggable-card
  - `matter-dom-plugin` (DOM bodies): https://github.com/jorisnoo/matter-dom-plugin
  - GSAP InertiaPlugin + Physics2DPlugin, for physics-lite throws without an engine (as in the Codrops free-plugins
    demos)
- **Stack:**
  - Draggable + InertiaPlugin (no engine) covers 90% of sticker play.
  - `matter-js@0.20.0` only for the footer pile, synced to DOM nodes on the GSAP ticker.
- **Fit:**
  - Draggable stickers: High. They're the scrapbook's most direct "touch me".
  - Physics pile: Med. It's delightful once, but heavier, and it's a well-known trope.
- **Perf/a11y:**
  - Matter's `Mouse` captures wheel events, which blocks page scroll. Remove its wheel listeners:
    `mouse.element.removeEventListener('wheel', mouse.mousewheel)` (`mousewheel`/`DOMMouseScroll` in older builds).
  - On touch, MouseConstraint also blocks scrolling. Gate physics to fine pointers, or show a "Shake the jar"
    button that runs it on demand.
  - Run the engine only while the section is visible (`ScrollTrigger.create({ onToggle })`), and put bodies to
    sleep.
  - Stickers are decorative (`aria-hidden`), but keep any text on them in the DOM elsewhere.
  - Reduced motion: stickers are static, and the footer shows a neat arranged pile.
- **Sketch:**
  ```js
  Draggable.create('.sticker', { bounds: section, inertia: true, edgeResistance: 0.8, zIndexBoost: true,
    onPress() { gsap.to(this.target, { scale: 1.08, rotation: '+=' + gsap.utils.random(-6, 6), boxShadow: '0 18px 30px rgb(39 6 23 / .28)', duration: 0.25 }) },
    onRelease() { gsap.to(this.target, { scale: 1, boxShadow: '0 4px 8px rgb(39 6 23 / .18)', duration: 0.6, ease: 'back.out(3)' }) } })
  // matter: Engine.update(engine, 1000 / 60) inside gsap.ticker; then gsap.set(el, { x: body.position.x - w/2, y: body.position.y - h/2, rotation: body.angle * 57.3 })
  ```

#### 27. Sticker peel. Fit: High (concept), Med (build cost)
- **Looks like:** The corner of a sticker lifts toward the cursor, curling to show its pale backing, with a soft
  shadow. Drag and it peels off and swings as you carry it.
- **Where:** One round "Studio Kavalu · ಕವಲು" sticker on the album page or the contact letter, the "seal" of the brand.
- **Sources:**
  - ★ React Bits Sticker Peel (rebuilt 12 Oct 2026 with a real curl in WebGL2 and no dependencies; `peelDirection`,
    `curlRadius`, `finish: gloss|matte|holo`, `swing`, `friction`, `bounce`):
    https://reactbits.dev/animations/sticker-peel
  - paperlab `peel` behaviour (3D paper, with a heavier R3F stack): https://paperlab.nawwara.studio/
  - For a CSS-only corner lift, see technique 28.
- **Stack:** The React Bits component (a WebGL2 canvas per sticker) as a reference or adapted component.
- **Fit:** High. A peeling sticker is the most tactile moment a scrapbook can have. Use **one**, matte finish.
- **Perf/a11y:**
  - One WebGL2 context per sticker, so limit it to 1–2 per page. Release it on unmount (the source calls
    `WEBGL_lose_context`).
  - Fallback: a static sticker image, with a CSS corner-lift on hover.
  - Reduced motion: static.

#### 28. Page curl and folded corner. Fit: Med-High (CSS corner), Low (full page-turn)
- **Looks like:** A project card's bottom-right corner is dog-eared, and on hover it lifts a little further,
  revealing the next layer (a hint of the next image, or the project's colour). A full book page-turn is the
  heavier cousin.
- **Where:** Stamps and index cards on /work (hover state), and the "next project" card at the foot of a case study.
- **Sources:**
  - ★ Kitty Giraudel, "Folded corner with CSS" (Mar 2026): a `clip-path: polygon()` change, a triangle for the back
    and a shadow triangle. https://kittygiraudel.com/2026/03/05/folded-corner-with-css/
  - `corner-shape` is Chrome 139 only (MDN BCD), so don't rely on it.
  - paperlab `flip` (page turning on its spine) for a lookbook moment: https://paperlab.nawwara.studio/
  - `page-flip` (StPageFlip) 2.0.7: a canvas/HTML flip-book, but unmaintained since 2021. Avoid.
- **Stack:** CSS `clip-path` + a pseudo-element triangle with a `linear-gradient` crease and a shadow, transitioned
  on `:hover`/`:focus-visible`.
- **Fit:** Med-High for the CSS corner: cheap, tactile, on-concept. Low for full page-turns: heavy, gimmicky and
  bad for reading.
- **Perf/a11y:**
  - Pure CSS, so there's no layout change.
  - Under reduced motion, the dog-ear is static and the hover only changes the shadow.
- **Sketch:**
  ```css
  .card { --c: 0px; clip-path: polygon(0 0, 100% 0, 100% calc(100% - var(--c)), calc(100% - var(--c)) 100%, 0 100%); transition: --c .45s var(--ease-glide); }
  .card:hover, .card:focus-visible { --c: 44px; }   /* @property --c { syntax: '<length>'; inherits: false; initial-value: 0px } */
  .card::after { /* the folded flap */ width: var(--c); height: var(--c); background: linear-gradient(135deg, #e9e6d6 45%, #cfc9b4 50%, transparent 52%); }
  ```

#### 29. Tear and rip reveals (and perforated stamp tears). Fit: High
- **Looks like:**
  - **Section tear:** the paper splits along a ragged edge and the two halves pull apart (or one half lifts away)
    to reveal the next section in its colour.
  - **Perforated tear:** a stamp or ticket stub tears off along its perforation, fibre by fibre, when dragged.
- **Where:**
  - Section tear: between the hero and the first spread, or as the transition into "Choose your road".
  - Perforated tear: the "Book a call" stub at the end of the onboarding letter, and stamps in the /work grid
    (tear one off to open it, as a playful alternative to clicking).
- **Sources:**
  - ★ React Bits Tear Ticket (perforated stub; `holes`, `holeSize`, `notch`, `roughness`, `tearAngle`,
    `resistance`, `ariaLabel`; Motion): https://reactbits.dev/micro/tear-ticket
  - Codrops "Designing in Paper as a developer: taking Paper Shaders off the background" (19 Oct 2026): torn-edge
    dividers from Paper's warp shader (scrolling widens them, the mouse twists them).
    https://tympanus.net/codrops/2026/10/19/paper-shaders-off-background/ (demo https://tympanus.net/Demos/PaperDrops/,
    repo https://github.com/twotwentytwo-studio/codrops-paper)
  - Paper Shaders: `@paper-design/shaders-react` 0.0.82, https://shaders.paper.design
  - CSS generators for ragged or zig-zag edges (export a mask, then jitter it by hand):
    https://css-generators.com/fancy-frame/ · https://css-generators.com/custom-borders/
  - GSAP forum guidance on polygon clip tweens (units on every point, equal point counts)
  - paperlab "interaction states: drag a stamp past its threshold and it tears off its sheet"
- **Stack:**
  - Section tear, DOM version: two copies of the section, each clipped with complementary ragged
    `clip-path: shape()`, or `polygon()` with ~40 jittered points generated from a seeded random. GSAP moves them
    apart (`x`, `rotate`) while the next section shows beneath. Add a scanned paper-fibre edge PNG via
    `mask-image` for realism.
  - Perforation: the React Bits Tear Ticket, or a CSS `mask` of `radial-gradient` holes.
- **Fit:** High. Tearing *is* the crossroads gesture (one sheet becoming two paths), and the perforation is the
  stamp motif.
- **Perf/a11y:**
  - `clip-path: shape()` is responsive (Chrome 135, Safari 18.4, Firefox 148). Use `polygon()` in % as the fallback.
  - Duplicate DOM for the halves: mark the copy `aria-hidden` and `inert`.
  - Reduced motion: a straight crossfade or none, with the edge drawn statically.
- **Sketch:**
  ```js
  const edge = jagged(40, seed)    // [[x%, y%], ...] along the tear line
  gsap.set(top, { clipPath: `polygon(0% 0%, 100% 0%, ${edge.map(([x,y]) => `${x}% ${y}%`).join(', ')})` })
  gsap.set(bottom, { clipPath: `polygon(${edge.map(([x,y]) => `${x}% ${y}%`).join(', ')}, 100% 100%, 0% 100%)` })
  gsap.timeline({ scrollTrigger: { trigger: seam, start: 'top 70%', end: 'top 20%', scrub: 0.4 } })
    .to(top, { yPercent: -12, rotate: -1.5, ease: 'none' }, 0).to(bottom, { yPercent: 12, rotate: 1, ease: 'none' }, 0)
  ```

#### 30. Letter fold → envelope → stamp (onboarding "Choose your road"). Fit: High ★ signature
- **Looks like:** After you "send" the letter (a sentence with inline choices):
  1. The page folds into thirds (two 3D creases).
  2. It slides into an envelope.
  3. The flap closes.
  4. A Kavalu stamp lands with a small bounce, and a postmark draws itself (DrawSVG).
  5. "Letter sent" types on.
- **Where:** The home "Choose your road" section and /start.
- **Sources:**
  - ★ paperlab `letter-fold` preset (real 3D paper, `memory` creases, `onCrease`; R3F):
    https://paperlab.nawwara.studio/ (npm `paperlab`, GitHub https://github.com/NourMtir0722/Paperlab). The
    Codrops case study "Real Folds, Real Fire" (18 Oct 2026) explains the arc-length-preserving folds:
    https://tympanus.net/codrops/2026/10/18/real-folds-real-fire/
  - CSS-3D route: three panels with `transform-style: preserve-3d`, `rotateX` about the crease lines, and gradient
    shading. The React Bits Fold Text "paper" style shows the shading idea.
  - Codrops "On-scroll folding 3D cardboard box" (three.js + GSAP, 2022):
    https://tympanus.net/Tutorials/OnScrollFoldingCardboardBox/
  - Digital Stamp Collection: the feedback form is a postcard that flips over and leaves with a "genie" effect, a
    shipped precedent for "form as object". https://marijanapav.com/stamps
- **Stack:**
  - **Recommended:** CSS 3D + a GSAP timeline. It's three DOM panels, so the letter stays real, editable and
    accessible text until it's sent.
  - paperlab only if you accept R3F plus three (lazy-loaded, about one moment per site). It's beta 0.8.1 and needs
    React ≥ 19 below 19.4.
- **Fit:** High. It's the emotional peak of the site. It turns a form into an object, and it's the one place
  where Jhey-level play is justified.
- **Perf/a11y:**
  - The form submits normally (a Server Action). The animation runs *after* success, and the confirmation is
    announced in an `aria-live` region.
  - Focus goes to the confirmation heading.
  - Reduced motion: no fold, just an instant swap to a "Letter sent" card with a static stamp.
  - Mobile: the same, scaled.
- **Sketch:**
  ```js
  gsap.timeline({ defaults: { ease: 'power3.inOut' } })
    .to(panelBottom, { rotateX: 180, duration: 0.6, transformOrigin: 'top' })
    .to(panelTop, { rotateX: -180, duration: 0.6, transformOrigin: 'bottom' }, '-=0.25')
    .to(letter, { y: envelopeY, scale: 0.62, duration: 0.7 })
    .to(flap, { rotateX: 0, duration: 0.45, ease: 'power2.in' })
    .from(stamp, { y: -40, rotate: -18, autoAlpha: 0, duration: 0.5, ease: 'back.out(2.2)' })
    .from(postmark, { drawSVG: '0%', duration: 0.6, ease: 'power2.out' })
  ```

#### 31. paperlab: real 3D paper (peel, unroll, flip, letter-fold, hang, fall, crumple), assessed. Fit: Med
- **What it is:** An Apache-2.0 React library (beta 0.8.1, Sep 2026) that renders paper as real geometry.
  - Arc-length-preserving deformers (`roll`, `curl`, `bend`, `fold`, `wave`, `drape`, `crumple`) and
    12 behaviours (`peel`, `unroll`, `flip`, `letter-fold`, `hang`, `fly`, `fall`, `carry`, `flight`, `crumple`,
    `settle`, `ribbon`).
  - 7 paper stocks and 12 field layouts (`fan`, `spread`, `book`...).
  - Hardware: clips, pegs, thread. Idle physics: `taped`, `dangle`, `breeze`.
  - Instanced galleries in one draw call.
  - Accessibility: `prefers-reduced-motion` freezes behaviours, and a hidden DOM mirror carries the content for
    screen readers and find-in-page.
- **Sources:** https://paperlab.nawwara.studio/ · https://www.npmjs.com/package/paperlab · Codrops case study
  https://tympanus.net/codrops/2026/10/18/real-folds-real-fire/
- **Fit:** Med.
  - For: it's uniquely on-concept, and the paper clips and pegs match the brief.
  - Against: it brings in three + R3F + gsap, it's in beta, and it's WebGL text. Use it for at most one
    lazy-loaded hero object, such as a hanging "work in progress" print on /studio, or the letter fold if the CSS
    version falls short. Prototype it in a sandbox before committing.

#### 32. Stamp flip-book and the perforated stamp frame. Fit: High ★ motif
- **Looks like:**
  - The perforated stamp frames (a scalloped edge) hold project images.
  - The centre hero stamp is a *flip-book* that cycles 4–6 frames of her work every ~0.9 s with a hard cut or a
    0.15 s crossfade, with a plum duotone twin below it.
  - On hover, a stamp lifts slightly with a deeper shadow. On click it hands off to technique 13.
- **Where:** The hero, /work Stamps view, and case-study "stamps" blocks.
- **Sources:**
  - ★ CSS Shape "Stamp" (Temani Afif; a single element, mask-only perforation): https://css-shape.com/stamp/.
    `mask-image` is Baseline (Chrome 120, Safari 15.4, Firefox 53).
  - ★ Digital Stamp Collection (Next.js 16 + React 19 + Motion + Lenis + R3F; open source): a draggable stamp field,
    a loupe inspection, binder tabs, typewriter catalogue cards. https://marijanapav.com/stamps · Codrops
    https://tympanus.net/codrops/2026/06/09/building-an-interactive-digital-stamp-collection-with-shaders-postcards-and-playful-inspection/
    · code https://github.com/buka-studio/www-marijanapav
  - Osmo "Auto image cycle slideshow": https://www.osmo.supply/resource/auto-image-cycle-slideshow
  - Codrops "Repeating image transition" (2025): https://tympanus.net/Development/RepeatingImageTransition/
- **Stack:** CSS mask for perforations; a GSAP timeline with `repeat: -1` for the flip-book, toggling
  `visibility` (no tween) for an honest flip-book feel.
- **Fit:** High. It's the design direction's own motif.
- **Perf/a11y:**
  - The flip-book is auto-moving content, so it needs a pause (WCAG 2.2.2). It pauses on hover/focus, off-screen,
    and under reduced motion (show frame 1).
  - All frames are lazily decoded except frame 1, which might be LCP.
- **Sketch:**
  ```css
  /* Temani Afif's single-element stamp (css-shape.com/stamp): holes only around the edge, content-box stays solid */
  .stamp { --r: 8px; padding: var(--r);
    mask: radial-gradient(50% 50%, #0000 66%, #000 67%) round var(--r) var(--r) / calc(2*var(--r)) calc(2*var(--r)),
          conic-gradient(#000 0 0) content-box; }
  ```
  ```js
  const tl = gsap.timeline({ repeat: -1 }); frames.forEach((f, i) => tl.set(frames, { autoAlpha: (j) => j === i ? 1 : 0 }, i * 0.9))
  ScrollTrigger.create({ trigger: stamp, onToggle: (s) => s.isActive ? tl.play() : tl.pause() })
  ```

#### 33. Polaroid drop and "develop". Fit: Med-High
- **Looks like:** A polaroid drops onto the page (slight overshoot and rotation), and the photo "develops" from a
  milky grey-green to full colour over ~1.2 s. It's a lovely reveal for shoot projects and the founder portrait.
- **Where:** Photo/film-shoot case studies (the first frame), the founder section, "From the scrapbook".
- **Sources:**
  - CSS `filter` from `sepia(.6) saturate(.2) brightness(1.25) contrast(.7) blur(1px)` to `none`, over an inner
    `<img>`
  - The Codrops Scrollaroids demo, for scattered polaroid composition: https://tympanus.net/Tutorials/Scrollaroids/
  - Aceternity Draggable Card's "Polaroid collection": https://ui.aceternity.com/components/draggable-card
- **Stack:** GSAP (`filter` tween) or CSS transition with `@starting-style`.
- **Fit:** Med-High. It's nostalgic, physical and photography-first. Use it once per page.
- **Perf/a11y:**
  - Animating `filter` on a medium image is fine, but on full-screen images it's costly: use an overlay
    `opacity` instead.
  - Reduced motion: developed already.

### G. SVG

#### 34. The road: an SVG path that draws, forks and carries a traveller. Fit: High ★ signature
- **Looks like:**
  - A 1px plum hairline runs down the page, drawing itself as you read.
  - At chapter starts it **forks**, and the branches lead to the section's content. At "Four roads" it splits
    into four, each ending at an index card.
  - A small dot (or tiny stamp) travels along the active branch. On the /studio process, the road bends through
    Listen → Map → Make → Launch.
  - The intro, preloader and onboarding progress use the same line.
- **Where:** Site-wide (chapter starts), "Four roads", /studio process, the preloader, and onboarding.
- **Sources:**
  - ★ Codrops "Creating scroll-driven SVG map animations with GSAP" (21 May 2026):
    `.from(path, { drawSVG: '0 0' })` + `.to(dot, { motionPath: path })` + "camera" `quickTo` follow + a
    reduced-motion variant.
    https://tympanus.net/codrops/2026/05/21/creating-scroll-driven-svg-map-animations-with-gsap/
  - ★ Codrops "Building responsive scroll-triggered curved path animations with GSAP" (17 Dec 2025): the path is
    rebuilt from anchor elements' rects, scrubbed with `invalidateOnRefresh`, rebuilt on a debounced resize, with a
    `gsap.matchMedia` reduced-motion branch.
    https://tympanus.net/codrops/2025/12/17/building-responsive-scroll-triggered-curved-path-animations-with-gsap/
  - GSAP DrawSVGPlugin docs (with the `splitPaths()` helper for multi-segment drawing):
    https://gsap.com/docs/v3/Plugins/DrawSVGPlugin/
  - React Bits Branched Menu (a trunk that branches and traces a line to your pick; an interaction precedent):
    https://reactbits.dev/micro/branched-menu
  - Osmo "Draw path on scroll" and "Follow SVG path on scroll":
    https://www.osmo.supply/resource/draw-path-on-scroll · https://www.osmo.supply/resource/follow-svg-path-on-scroll
  - Skiper 19 "SVG follow scroll": https://skiper-ui.com/v1/skiper19
  - Aceternity Tracing Beam: https://ui.aceternity.com/components/tracing-beam
- **Stack:** Inline SVG + DrawSVGPlugin + MotionPathPlugin + ScrollTrigger (scrub). Build the path *from anchors* in
  JS for responsiveness, following the Codrops Dec 2025 approach.
- **Fit:** High. It's the brand idea in one line. Everything else can be removed and this should stay.
- **Perf/a11y:**
  - Decorative: `aria-hidden`, `focusable="false"`.
  - 1px strokes: set `vector-effect: non-scaling-stroke` for a crisp hairline under scaling, and check DrawSVG
    still reaches 100% (overshoot to 102%, per the docs' Firefox note).
  - Rebuild the path on resize, debounced 200 ms as in the article.
  - Reduced motion: the road is drawn fully, and branches appear without travel.
  - Mobile: a simpler, straighter road.
- **Sketch:**
  ```js
  const tl = gsap.timeline({ defaults: { ease: 'none' }, scrollTrigger: { trigger: chapter, start: 'top 70%', end: 'bottom 60%', scrub: 0.3, invalidateOnRefresh: true } })
  tl.from(trunk, { drawSVG: '0% 0%', duration: 1 })
    .from(branches, { drawSVG: '0% 0%', duration: 1, stagger: 0.15 }, 0.85)          // the fork
    .to(traveller, { motionPath: { path: branches[active], align: branches[active], alignOrigin: [0.5, 0.5] }, duration: 1 }, 0.85)
    .from(cards, { autoAlpha: 0, y: 12, stagger: 0.15, duration: 0.3 }, 1.6)
  ```

#### 35. Signature and handwriting draw. Fit: Med-High
- **Looks like:** Ananya's signature, or a short handwritten line ("see you at the crossroads — A.") writes itself in
  plum ink once.
- **Where:** The founder section (after the quote), the onboarding letter's sign-off, and the footer.
- **Sources:**
  - ★ GSAP DrawSVG (stagger across the stroke paths of a real signature; vectorise her actual signature as
    centre-line strokes, not outlined fills)
  - `vara` 1.4.1 (handwriting-from-font library, 2022): https://www.npmjs.com/package/vara
  - The Osmo DrawSVG scribble demo, as above
- **Stack:** Inline SVG strokes + DrawSVG, with the timeline durations proportional to path length (the DrawSVG docs
  helper).
- **Fit:** Med-High. It's personal and founder-led, and it's authentic only if it's *her* hand.
- **Perf/a11y:**
  - The signature SVG gets `role="img"` and an `aria-label` ("Ananya's signature"), or is decorative next to her
    name in text.
  - Reduced motion: drawn.

### H. Texture and WebGL

#### 36. Grain and paper-noise overlay. Fit: High
- **Looks like:** A faint, warm paper grain over the whole page (cream areas look like stock, not screen), optionally
  flickering very slightly at 8–12 fps for a film-like life on dark plum sections.
- **Where:** Site-wide, fixed overlay. Stronger on the deep-plum "desk" and footer.
- **Sources:**
  - ★ React Bits Noise (a canvas tile generated once, `fps` cap, `blendMode`, pauses when not visible; rebuilt
    8 Oct 2026): https://reactbits.dev/animations/noise
  - Magic UI Noise Texture (SVG `feTurbulence`, desaturation and contrast controls):
    https://magicui.design/docs/components/noise-texture
  - Osmo "Film grain effect": https://www.osmo.supply/resource/film-grain-effect
  - React Bits Grainient (grainy gradients): https://reactbits.dev/backgrounds/grainient
  - Paper Shaders' grain and paper textures: https://shaders.paper.design
- **Stack:** **Best:** a pre-rendered 256×256 grain PNG or AVIF tile on a `position: fixed` pseudo-element with
  `mix-blend-mode: multiply` (on cream) or `soft-light` (on plum), at 4–8% opacity. Optionally use a
  `steps(4)` `background-position` jitter for flicker.
- **Fit:** High. It's what makes cream read as paper. It's nearly free if it's a static tile.
- **Perf/a11y:**
  - Avoid live full-screen `feTurbulence` filters and animated SVG noise, which repaint every frame and are
    costly on mobile.
  - `pointer-events: none; z-index: top; contain: strict`.
  - Keep contrast: test text contrast *with* the grain.
  - Reduced motion: static grain only, which is fine to keep.
- **Sketch:**
  ```css
  body::after { content: ""; position: fixed; inset: -50%; background: url(/tex/grain-256.avif); opacity: .06; mix-blend-mode: multiply;
                pointer-events: none; z-index: 9999; }
  @media (prefers-reduced-motion: no-preference) { .dark-desk::after { animation: grain 0.5s steps(4) infinite; } }
  @keyframes grain { 25% { translate: -2% 3% } 50% { translate: 3% -1% } 75% { translate: -1% -3% } }
  ```

#### 37. WebGL image distortion on hover or scroll. Fit: Low-Med
- **Looks like:** Images bow slightly with scroll speed, or ripple and bulge under the cursor, or one image melts into
  the next on hover.
- **Where:** If anywhere, the /work Index-view preview or the stamp hover in Stamps view (a subtle "ink bleed /
  paper wet" ripple, ≤ 2% displacement). Not on the home spreads, where the photography should stay clean.
- **Sources:**
  - ★ Codrops "How to create distortion and grain effects on scroll with shaders in three.js" (18 Jul 2024): DOM
    images mirrored as planes, `uScrollVelocity` from Lenis bends the vertices, a noisy circle under the cursor,
    velocity clamped. https://tympanus.net/codrops/2024/07/18/how-to-create-distortion-and-grain-effects-on-scroll-with-shaders-in-three-js/
  - Codrops "How to animate WebGL shaders with GSAP: ripples, reveals and dynamic blur" (8 Oct 2025; GSAP tweens
    uniforms, DPR capped at 1.5): https://tympanus.net/codrops/2025/10/08/how-to-animate-webgl-shaders-with-gsap-ripples-reveals-and-dynamic-blur-effects/
  - Codrops "Bulge distortion effect with WebGL" (2023): https://tympanus.net/Tutorials/WebGLBulge/
  - React Bits Ripple Distortion (OGL) and Morph Slider (OGL displacement):
    https://reactbits.dev/animations/ripple-distortion · https://reactbits.dev/components/morph-slider
  - Paper × domgl (paper creasing under the cursor, lens cards, WebGPU): https://tympanus.net/Demos/PaperDrops/
- **Stack:** **OGL** (`ogl@1.0.11`): one fixed canvas, planes synced to DOM rects each frame from cached
  measurements + Lenis scroll, and uniforms tweened by GSAP. The DOM `<img>` stays as layout source and fallback
  (opacity 0 once GL is ready), as both Codrops tutorials do.
- **Fit:** Low-Med. Liquid distortion is a 2019–2024 signature that reads "agency template" now, and it fights paper,
  which doesn't ripple like water. Only a *very* subtle ink-bleed or paper-lens is on-concept.
- **Perf/a11y:**
  - Lazy-load the GL bundle once it's in view. One context per page.
  - Pause when the tab is hidden. DPR ≤ 1.5. Off under `saveData`, coarse pointers and reduced motion.
  - Never let GL be the only copy of an image: keep alt text on the DOM image.

#### 38. Unicorn Studio (no-code WebGL scenes). Fit: Low-Med
- **What it is (checked 23 Oct 2026):** A browser editor for production WebGL scenes: 75+ shader effects (grain,
  noise, distortion…); image, video, text and 3D layers; an AI agent with MCP. Scenes run on a runtime of about
  50 KB gzip, built on curtains.js. https://www.unicorn.studio/docs/
- **Plans:**
  - **Free:** 8 publishes, an irremovable watermark, and *personal and non-commercial use only*.
  - **Legend:** $14/mo billed yearly, or $20/mo monthly. It covers commercial and client use, removes the logo
    (which stays off after you cancel), and adds JSON export for self-hosting and the production CDN.
  - Unicorn may show your logo in its marketing unless you opt out. https://www.unicorn.studio/terms
- **Embed:**
  - The loader script from jsDelivr (`unicornstudio.js@v2.4.3`) with a `data-us-project` div, or self-hosted
    JSON via `data-us-project-src`.
  - Or the *unofficial* `unicornstudio-react` 2.4.0. The research build measured it at about 240 KB gzip, because
    it bundles the SDK and three.js code, so load it only through `next/dynamic`.
  - By default, scene data comes from Google Cloud Storage with a cache-buster on every load, and production mode
    uses `assets.unicorn.studio`. https://www.unicorn.studio/docs/embed/
- **Perf/a11y:**
  - Settings: `lazyLoad`, `fps`, `scale` and `dpi`. Off-screen scenes pause. `setScroll()` syncs with Lenis.
  - The React package's `placeholder` covers loading, errors and missing WebGL.
  - There's **no built-in reduced-motion handling**, so swap in a poster image yourself.
    https://www.unicorn.studio/docs/performance/
- **Fit:** Low-Med. It's fine for **one** hero or "about" atmosphere layer that Ananya wants to tune herself
  without code. That means Legend, self-hosted JSON, a poster fallback, 30 fps and `lazyLoad`.
  - Don't use it for grain, which CSS does better (technique 36).
  - Don't use it for image effects that must stay in sync with Flip and Lenis. One hand-written OGL canvas
    (technique 37) is lighter and avoids running a second WebGL runtime.

### I. Numbers and bookends

#### 39. Number counters. Fit: Med
- **Looks like:** "120+ brands", "8 years", "3 continents" count up once when they enter, ideally as an odometer
  roll rather than a frantic tick.
- **Where:** The /studio "in numbers" line, and the case-study results row (for example, "+38% engagement"). Don't
  put them on the home page.
- **Sources:**
  - ★ NumberFlow (`@number-flow/react` 0.6.2; `respectMotionPreference` defaults to true; `trend`,
    `continuous` plugin, `NumberFlowGroup`): https://number-flow.barvian.me/
  - React Bits Counter (odometer, locales and currency, rebuilt 13 Oct 2026) and Count Up (Motion):
    https://reactbits.dev/components/counter
  - Magic UI Number Ticker: https://magicui.design/docs/components/number-ticker
  - Motion Primitives Sliding Number: https://motion-primitives.com/docs/sliding-number
  - Osmo "Number odometer": https://www.osmo.supply/resource/number-odometer
- **Stack:** NumberFlow in React, or GSAP `gsap.to(obj, { v: 120, snap: { v: 1 }, onUpdate })`.
- **Fit:** Med. Fine for proof points, but stats aren't a studio's strongest story. Let the work speak.
- **Perf/a11y:**
  - Use `font-variant-numeric: tabular-nums` and a fixed width, so there's no CLS.
  - Render the *final* number in the HTML, so screen readers and no-JS users get it, and keep the animated digits
    `aria-hidden`.
  - Reduced motion: the final value, instantly.
- **Sketch:**
  ```js
  const o = { v: 0 }
  gsap.to(o, { v: 120, duration: 1.4, ease: 'power3.out', snap: { v: 1 }, onUpdate: () => (el.textContent = o.v + '+'),
    scrollTrigger: { trigger: el, start: 'top 85%', once: true } })
  ```

#### 40. Preloader and first-visit intro. Fit: High (if ≤ 1.5 s, first visit only)
- **Looks like (Kavalu version, from the design direction):**
  1. On cream, the road draws up from the bottom and forks.
  2. ಕವಲು appears at the fork in plum, with a variable-width breathe.
  3. The intro lifts away like a sheet pulled up (`clip-path`, or `yPercent: -100` with `expo.inOut`), revealing
     the hero already in place.
- **Sources:**
  - ★ Osmo "Willem loading animation" (Nov 2025): the letters rise, the central image box grows to fill the
    viewport, the header text rises; one timeline, `expo` eases, ~1.25 s for the letters and 2 s for the image,
    scroll locked with a `:has()` rule. https://www.osmo.supply/resource/willem-loading-animation
  - Osmo "Welcoming words loader", "Logo reveal loader" and "Crisp loading animation":
    https://www.osmo.supply/resource/welcoming-words-loader
  - Skiper 8 "Words preloader": https://skiper-ui.com/v1/skiper8
  - Animata preloaders "Split reveal" and "Vertical tiles": https://animata.design/docs/preloader/split-reveal
  - Codrops "Hover motion intro animation" (2024): https://tympanus.net/Development/IntroGridMotionTransition
- **Stack:** One GSAP timeline (DrawSVG + SplitText + clip-path). Lenis `stop()` during it (`lock()` in 2.0).
- **Fit:** High as a 1.2–1.5 s brand moment on the *first* visit. Low if it gates content or repeats.
- **Perf/a11y:**
  - Never delay LCP: the hero renders underneath from the start, and the intro is a fixed overlay above it.
    Don't wait for "all images loaded". Wait at most for `document.fonts.ready` plus the hero `img.decode()`,
    with a 1.6 s hard cap.
  - Skip it via `sessionStorage` on repeat visits, and entirely under reduced motion.
  - Make it skippable: a click or keypress jumps the timeline to its end with `tl.progress(1)`.
  - Use `aria-hidden` on the overlay and `aria-busy` on main only while it runs.
- **Sketch:**
  ```js
  if (!sessionStorage.kvIntro && !reduce) { sessionStorage.kvIntro = 1; lenis.stop()
    gsap.timeline({ onComplete: () => { lenis.start(); overlay.remove() } })
      .from(road, { drawSVG: '0% 0%', duration: 0.7, ease: 'power2.inOut' })
      .from(fork, { drawSVG: '0% 0%', duration: 0.35, stagger: 0.08 }, '-=0.1')
      .from(word, { autoAlpha: 0, yPercent: 30, duration: 0.5, ease: 'expo.out' }, '-=0.2')
      .to(overlay, { clipPath: 'inset(0% 0% 100% 0%)', duration: 0.6, ease: 'expo.inOut' }, '+=0.15') }
  ```

#### 41. Footer reveal and "next project" pull. Fit: High
- **Looks like:**
  - **Footer:** the last section slides away to uncover a deep-plum footer sitting *underneath*, as if lifting the
    final page of the album. The folder tabs and the giant STUDIO KAVALU wordmark rise slightly into place
    (parallax ±10%).
  - **Next project:** at the end of a case study, the next project's stamp/cover is partly visible. As you
    continue scrolling, it grows (technique 4 in miniature), and past a threshold it navigates (or you click it).
- **Where:** Every page's footer. The case-study foot.
- **Sources:**
  - ★ Osmo "Footer parallax effect": https://www.osmo.supply/resource/footer-parallax-effect
  - Osmo "Scroll to next page": https://www.osmo.supply/resource/scroll-to-next-page
  - CSS: `footer { position: sticky; bottom: 0; z-index: -1 }` under a `main` with a background, which uncovers
    it with zero JS
  - Codrops "Exploring playful context-aware animations for fixed elements" (2024):
    https://tympanus.net/Development/ContextAwareLogoAnimationScroll
- **Stack:** CSS sticky + a ScrollTrigger scrub for the inner parallax. For "next project", ScrollTrigger progress
  plus an *explicit* link. Don't auto-navigate on scroll without a visible control (it surprises users and breaks
  the back button's expectations).
- **Fit:** High. It's a quiet, premium ending, it's the folder-tab motif's home, and it keeps people moving
  through the work.
- **Perf/a11y:**
  - The footer is a landmark. Its content order stays logical for keyboard users.
  - Reduced motion: a static footer, and the next project is a normal card.
- **Sketch:**
  ```js
  gsap.from('.footer__inner', { yPercent: -30, ease: 'none', scrollTrigger: { trigger: 'footer', start: 'top bottom', end: 'bottom bottom', scrub: true } })
  ```

---

## 5b. Reference sites worth studying (2025–2026)

How these were checked: each award was confirmed on the site's awwwards.com/sites page. The motion is described
from the makers' own Codrops write-ups. A ◇ means the motion was inferred from Awwwards element clips and tags,
not watched. FWA, CSSDA and Godly listings were not cross-checked.

| Site | Award / source | Stack | Signature motion | Steal for Kavalu |
|---|---|---|---|---|
| **Digital Stamp Collection** (Marijana & Robert Pavlinić). https://marijanapav.com/stamps | Codrops 9 Jun 2026 (no award found). Open source: github.com/buka-studio/www-marijanapav | **Next.js 16, React 19**, R3F, Motion, Lenis | A loose, draggable field of stamps. Selecting one inspects it under a glass-loupe shader (drag or arrow keys). The feedback form is a postcard that flips and "genies" away. Binder-divider tabs, typewriter catalogue cards, handwritten notes, paper grain. | **The closest reference to the whole brief, on Kavalu's own stack.** Study it for 25, 26, 30 and 32. |
| **MERSI** (site by FLOT NOIR). https://www.mersi-architecture.com | Awwwards SOTD 10 Apr 2026. Codrops "Between print and digital" (27 Jul 2026) | Webflow, GSAP (Flip, ScrollTrigger, SplitText), Lenis, Taxi.js | The project cover is cloned into an overlay, a curtain wipes the old page, and `Flip.fit()` morphs the clone into the case-study hero (1.2 s `expo.inOut`). The work index starts compact and `Flip.from` reflows it into the full grid on scroll, staggered, and reverses on scroll-up. | The GSAP-overlay version of technique 13. A collage that resolves into a grid (techniques 11 and 12). |
| **Obys' Design Books**. https://library.obys.agency/ | SOTD 17 Dec 2025. Codrops 12 Jan 2026 | Vanilla JS, GSAP | Every page is a paper sheet stacked on screen. Clicking a sheet's edge lifts it and drops it to the front. Grain and accent colour change per book, and filters slide sheets aside. | Case studies or chapters as stacked sheets and folder tabs you pull forward. |
| **Obys** (studio). https://obys.agency/ | SOTD 4 May 2026. Codrops 14 May 2026 | Custom engine (rAF + WAAPI), virtual scroll, WebGL | A persistent logo object rides through every layout and page transition. | One persistent brand object (the road, or a paper clip) that carries every transition. |
| **The Lookback** (Better Off®). https://tlb.betteroff.studio/ | SOTD 27 Mar 2026. Codrops 3 Mar 2026 | Nuxt 3, GSAP | Timeline, "surf" and index views. Switching flips every visible image to its new slot. Items peek out "like a book on a shelf". Images skew with scroll direction. | The Stamps ↔ Index switch (technique 12). |
| **Joffrey Spitzer**. https://joffreyspitzer.com/ | HM 11 Feb 2026. Codrops 18 Feb 2026 | Astro, GSAP (SplitText, Flip, ScrollTrigger), Lenis, Swup | A vertical work slider whose active item scales up; a toggle Flip-morphs it into a grid. A menu label grows into the page title with Flip. | The slider/grid toggle, and a label → title Flip. |
| **House of Yellow** (content agency: film, photo, social). https://houseofyellow.nl/ | HM 22 Jul 2026. Codrops 16 Sep 2026 | WordPress, GSAP (ScrollTrigger, SplitText, MorphSVG), Lenis, Swup | Logo shapes animate over full-screen video. The "Play" button is four marquees running around its edges. The work section toggles between a visual grid and a data list (client, views, delivery time). | A grid/list toggle with *numbers* for Ananya's social-content work. |
| **Ten Years Away** (Studio375). https://ten.375.studio/en | SOTD 26 Jun 2026. Codrops 8 Jul 2026 | **Next.js**, R3F, Lenis, GSAP | A camera moves through comic panels; chapters arrive as scattered panels sliding into place. A 3D flipbook you drag, with page sounds. A halftone cursor trail. Noise shadows streak with scroll speed. | A halftone or riso cursor trail (technique 24), and a lookbook flip for shoots. |
| **LAX Space** (Lax Chee). https://www.laxspace.co/ | HM 3 Sep 2025. Codrops 23 Sep 2025 | Next.js, Three.js, three-mesh-bvh | The cursor or a finger unrolls a 3D duct-tape strip along a smoothed path. Rendering quality is tiered by device. | A **2D washi-tape trail** in the hero or the 404 page (a variant of technique 24). |
| **Ponpon Mania**. https://ponpon-mania.com/ | SOTM Oct 2025. Codrops 7 Oct 2025 | Nuxt, OGL, GSAP, Matter.js | Illustration layers rebuilt as planes that spring away from the cursor. Chapters flip like record sleeves. | Layered cut-paper depth (technique 2), and an OGL + Matter precedent. |
| **Decathlon Yestalgia**. https://decathlonyestalgia.com/ | SOTD 28 Aug 2026. Codrops 12 Sep 2026 | WordPress, piecesjs, GSAP, Lenis, Rive | The menu is a Walkman: cassettes slide out and snap back. Fake-extruded headlines. Explicit reduced-motion rules: durations go to 0 and Rive jumps to its last frame. | A menu that's a physical object (a **folder drawer**), and their reduced-motion policy. |
| **Aralesk, Collages & Motion** ◇. https://www.aralesk.es | HM 17 Aug 2026 | Hand-built JS, GSAP, Lottie, a lazy-loaded three.js water scene | A curtain hero, draggable fabric sheets that reveal video, Lottie loops that start only when in view. | Ananya's real cut-outs as SVG or Lottie loops that run only while visible. |
| **NOTHIN'** (founder-led Paris branding studio) ◇. https://www.noth.in | SOTD 10 Aug 2026 + Portfolio Honors; Lenis showcase | Webflow, GSAP, Taxi.js, WebGL | A cursor-reactive shader hero over SVG. "WORK" split into letters. List images revealed with a cursor and parallax. | One cursor-reactive canvas, in the hero only. |
| **Lama Lama** ◇. https://lamalama.com/ | SOTM Jul 2026 | WordPress, Vite, Swup, one fixed WebGL canvas | The intro grows from the icon logo into an interactive grid; a shader morph and a camera move "step inside". | The mark bursting into a grid of stickers and thumbnails, as a preloader idea (technique 40). |
| **Jesper Landberg** ◇. https://www.jesperlandberg.com | SOTD 29 Sep 2026 | Nuxt, Three.js, GSAP | An infinite project index with seamless WebGL transitions home → project → project. | A "next project" hand-off that never sends you back to the grid (technique 41). |
| **Paperlab / Lights Left On**. https://paperlab.nawwara.studio/ · https://lightslefton.com | Codrops 18 Oct 2026 (no award found) | `paperlab` 0.8.1 (R3F 9, GSAP) | Real-geometry paper: unroll, peel, letter-fold, hang. A gallery of about 40 sheets in one draw call. | One peel or unroll moment (techniques 27, 30, 31). |

Also verified, but not detailed:
- Mr. Panda's Paper Portfolio (a hand-drawn papercraft world, SOTD 11 Mar 2026):
  https://www.mr-pandas-psychologically-safe-portfolio.com/
- GSAP showcase studio picks (https://gsap.com/showcase/): Studio Lumio https://studiolumio.com/ · Revelatio
  https://revelatio.studio/ · Studio375 https://375.studio/ · Fantik Studio http://fantik.studio · Mater
  http://mater.agency · Guillaume Colombel https://guillaumecolombel.fr/ · "Infinite Digital Scrapbook" by
  Chung-Sung Lau https://chungsunglau.co.uk (on-theme, not inspected)
- Lenis showcase picks (https://lenis.dev/showcase, 231 entries): Eduard Bodak https://www.eduardbodak.com/ ·
  12.studio https://www.12.studio/ · GATZARA https://gatzara.studio/ · HAOQI https://haoqi.design/ · Mat Voyce
  https://matvoyce.tv/ · FORMAT (Obys) https://format.obys.agency/

**What these sites share (2025–26):**
- The thumbnail becomes the hero, through a shared-element Flip.
- One collection, several layouts: grid ↔ list, collage → grid, timeline ↔ index.
- Physical objects instead of interface chrome: sheets, flipbooks, postcards, loupes, cassettes, tape.
- Velocity-aware motion fed from one shared animation loop.
- Print textures used as interaction.
- Performance treated as craft: visibility-gated animation, capped DPR, explicit reduced-motion rules.

**What now looks templated across award sites:**
- masked line or letter reveals on every heading
- percentage preloaders and logo intros that hold back the first screen
- curtain or clip-path wipes on every navigation and every image
- **work lists with an image floating under a custom cursor**
- pinned horizontal case studies
- endless marquees and carousels
- generic noise or RGB-split WebGL hovers

Section 7 folds these into the anti-list.

---

## 6. Where everything goes (the Kavalu site map)

| Page / section (from `design_direction.md`) | Techniques (numbers from section 5) | Notes |
|---|---|---|
| **Intro** (first visit) | 40, 34 | The road draws and forks, then ಕವಲು lifts away. ≤ 1.5 s, skippable. |
| **Hero** | 4 (stamp → full bleed), 32 (flip-book stamp), 16 (headline lines), 19 (scribble under "road"), 2 (satellite depth) | The only long pin on the home page. |
| **Project spreads** | 11 (deal-out), 5 + 10 (zoom-out and stack), 6 (clip reveals), 17 (typewriter labels), 13 (cover → case study) | Each spread wears its project colour. |
| **Manifesto** | 16 (word ink-in, scrubbed), 6 (inline image pills scale in) | One staggered moment for the whole section. |
| **Four roads** | 34 (fork into four), 28 (folded-corner index cards), 18 (label axes) | "Start here" pre-fills the letter. |
| **From the scrapbook** | 25 (bounded mini desk), 26 (1–2 stickers), 8 (focus on hover) | "Open the scrapbook" → /scrapbook. |
| **Founder** | 33 (polaroid develops), 35 (signature), 2 (subtle depth) | |
| **Choose your road** | 30 (fold → envelope → stamp), 29 (tear-off stub), 22 (magnetic Send) | The emotional peak. Animation runs after a successful submit. |
| **Footer** | 41 (uncover), 36 (grain), 17 (live Bengaluru clock), optional 26-physics drawer or 20 tape marquee, not both | Folder tabs plus the giant wordmark. |
| **/work: Stamps view** | 32, 12 (view switch / filter by road), 28, 13 | Perforated grid. |
| **/work: Index view** | 23 (cursor stamp preview), 18 (variable-font rows), optional 37 (a whisper of ink-bleed) | Keyboard focus shows the stamp inline. |
| **/work/[slug]** | 13 (cover from stamp), 6, 2, 7 (moodboard camera tour), 9 (contact sheet, shoots only), 39 (results), 41 (next project) | The project palette changes the room. |
| **/studio** | 21 (fold titles), 34 (process road), 10 (process cards stack), 16, 39 | |
| **/scrapbook** | 25 (infinite desk + grid view), 12 (filters), 26, optional 7 (intro tour) | Grid view is the default for touch, keyboard and reduced motion. |
| **/start** | 30, 29, 16 | |
| **404** | 24 (polaroid pile trail) or 26 (physics) or React Bits Paper Crumple | The only place for pure play. |
| **Site-wide** | 1 (Lenis), 14 (paper-slide View Transition, anchored header and tabs), 36 (grain), 19 (link scribbles), 3 (CSS scroll-driven flourishes) | |

**Suggested build order** (each step ships on its own; motion is layered over finished static pages):
1. **Spine:** tokens + `MotionProvider` (Lenis, ticker, `matchMedia` policy) + grain (techniques 1, 36).
2. **Page shell:** native paper-slide View Transition with the anchored header and tabs (14). Footer uncover (41).
3. **The road** (34) and chapter line reveals (16). This sets the visual grammar.
4. **Work:** Stamps grid with perforations (32) → Flip view switch and filters (12) → stamp-to-cover morph (13) →
   Index-view cursor preview (23).
5. **Home story:** hero expansion (4) → spreads deal-out, zoom-out and stack (11, 5, 10) → manifesto ink-in (16).
6. **Tactile layer:** scribbles (19), stickers (26), folded corners (28), tear-off stub (29).
7. **Big moments:** the scrapbook desk with its grid fallback (25), the letter → envelope (30), the intro (40).
8. **Only if there's time and budget:** sticker peel (27), collage camera (7), paperlab (31), ink-bleed WebGL (37).

**Budget per page:**
- at most **one** pinned story
- at most **one** staggered list
- at most **one** auto-moving element (flip-book *or* marquee), and it's pausable
- at most **one** WebGL context

---

## 7. Anti-list: motion that reads as templated, AI-slop or dated in 2026

Use these with restraint, or not at all. The first block matches the patterns that design-motion audits flag in
2026 (pulsing indicators, blur-everywhere, hover-scale-everywhere, stagger spam, bouncy utility springs, uniform
fade-ins, motion-on-mount for static text). The rest is specific to studio and portfolio sites.

1. **The same fade-up on every block.**
   - Identical `opacity + translateY (+ blur)` on every section, card and paragraph, especially body copy and
     nav. Body text should simply *be there*.
   - Keep the design direction's "opacity + 12px + 4px blur" for hero and display moments only. Three distinct
     enter recipes is the ceiling.
2. **Stagger and split spam.**
   - Every heading char-split, every list staggered, scramble/"decrypt" on big headlines.
   - One split moment per view. Scramble is for 1–3-word labels only.
3. **Hover-scale and magnet on everything, and custom cursors that replace the real one.**
   - `hover:scale-105` grids, magnetic nav links, blend-mode blob cursors, "VIEW" bubbles on every card.
   - The generic "image floats under the cursor in a work list" is now the most common award-site pattern
     (section 5b).
   - Magnetic on 2–4 CTAs, the native cursor kept, the follower only in the Index view, and only as the
     perforated, tilted stamp that becomes the cover.
4. **Scroll-jacking and pin abuse.**
   - Wheel hijacking, full-page snap sections, pins longer than about 2 viewports, horizontal galleries "because
     we can", Lenis set so floaty (lerp < 0.06, duration > 1.5 s) that it feels like ice.
   - One pinned story per page. Touch stays native.
5. **Component-library spectacle.**
   - 3D rings, domes, spheres and helices of images (Circular, Dome and Infinite-menu style galleries).
   - Liquid / RGB-shift / glass-refraction image distortion; aurora and gradient-mesh blobs; particle fields.
   - Holographic foil and "liquid glass" cards.
   - These read as 2024–26 demo reels and fight the paper concept. Paper creases, tears, curls and stacks; it
     doesn't ripple or refract.
6. **Looping attention-seekers.**
   - Pulsing dots, breathing CTAs, auto-rotating card stacks and carousels, perpetual logo marquees, auto-playing
     image trails.
   - Anything that moves on its own must be meaningful, slow, and pausable (WCAG 2.2.2).
7. **Preloaders and wipes that gate content.**
   - 0→100% counters, splash screens longer than 2 s, intros on every visit.
   - Curtain or clip wipes on *every* navigation and *every* image. Across award sites these now read as
     templated (section 5b).
   - First visit only, ≤ 1.5 s, skippable. Navigation uses an under-500 ms paper slide. Clip reveals are kept for
     chapter images.
8. **Bouncy springs and elastic eases on utility UI.**
   - Overshoot on menus, modals, dropdowns, toggles and form feedback.
   - Bounce belongs to paper objects (a sticker dropped, a stamp pressed), never to controls.
9. **Dated tropes.** Use these at most once, re-skinned:
   - giant "LET'S TALK" footer marquees
   - velocity skew on all text
   - parallax on every image
   - image-trail hero gimmicks
   - black curtain page wipes
   - "scroll down" bouncing mouse icons
   - WebGL noise blobs behind the logo

---

## 8. Accessibility and performance checklist (definition of done for every motion piece)

- [ ] It works and makes sense with `prefers-reduced-motion: reduce`. Test it with the OS setting *and* with
      Playwright `emulateMedia({ reducedMotion: 'reduce' })` in CI. Darkroom's satus repo has a ready-made e2e
      pattern that records `document.startViewTransition` animations under both settings:
      `e2e/view-transitions.e2e.ts`.
- [ ] Keyboard: everything clickable is focusable and visible. Pins and horizontal sections scroll the focused
      element into view. Nothing animates on keyboard-initiated focus.
- [ ] Screen readers: split text keeps one `aria-label`. Decorative layers (grain, road, cursor, trail,
      stickers) are `aria-hidden`. Animated numbers have their final value in the DOM.
- [ ] Auto-moving content (flip-book, marquee) pauses on hover and focus, off-screen, and has a visible pause
      control if it runs longer than 5 s.
- [ ] No CLS from motion: `aspect-ratio` on all media, fonts loaded before splitting, preloader as an overlay,
      pin spacers stable. Target CLS < 0.1.
- [ ] LCP: the hero image is never behind the preloader or a JS reveal; it has `priority` / `fetchpriority="high"`.
      Target LCP < 2.5 s on a mid-range Android over 4G.
- [ ] INP: pointer handlers write values only (`quickTo`), listeners are passive where possible, and there are
      no layout reads in loops. Target INP < 200 ms.
- [ ] Mobile: native touch scroll (`syncTouch: false`); pins shortened or removed through `gsap.matchMedia`;
      `svh` units; `ScrollTrigger.config({ ignoreMobileResize: true })`. Test on real iOS Safari, which caps at
      60 fps and has the address-bar resize.
- [ ] WebGL and physics pause when hidden or off-screen and are disposed on route change. They're off under
      `saveData` and reduced motion, and a DOM fallback is always present.
- [ ] Cleanup: every effect lives in `useGSAP` or returns a cleanup. There are no duplicate tickers in React
      Strict Mode (the Codrops ghost-trails article flags this). `ScrollTrigger.refresh()` runs after route
      changes and font loads.

---

## 9. Sources index (every URL cited above, grouped)

**GSAP**

- https://gsap.com/docs/v3/Plugins/ScrollSmoother/
- https://gsap.com/docs/v3/Plugins/ScrollTrigger/
- https://gsap.com/docs/v3/Plugins/Flip/
- https://gsap.com/docs/v3/Plugins/SplitText/
- https://gsap.com/docs/v3/Plugins/ScrambleTextPlugin/
- https://gsap.com/docs/v3/HelperFunctions/helpers/seamlessLoop
- https://gsap.com/docs/v3/Plugins/DrawSVGPlugin/
- https://gsap.com/showcase/

**Lenis / darkroom**

- https://github.com/darkroomengineering/lenis
- https://github.com/darkroomengineering/lenis/blob/main/packages/react/README.md
- https://github.com/darkroomengineering/satus
- https://lenis.dev/showcase

**React / Next.js / MDN**

- https://nextjs.org/docs/app/guides/view-transitions
- https://react-view-transitions-demo.labs.vercel.dev
- https://github.com/nextjs/react-view-transitions-demo
- https://react.dev/reference/react/ViewTransition

**Motion (motion.dev)**

- https://motion.dev/docs/react-upgrade-guide
- https://motion.dev/docs/lenis
- https://motion.dev/examples/

**React Bits**

- https://reactbits.dev/animations/scroll-expand
- https://reactbits.dev/components/accordion-gallery
- https://reactbits.dev/components/scroll-stack
- https://reactbits.dev/components/bounce-cards
- https://github.com/DavidHDev/react-bits
- https://reactbits.dev/components/stack
- https://reactbits.dev/components/masonry
- https://reactbits.dev/components/folder
- https://reactbits.dev/components/tilted-card
- https://reactbits.dev/components/circular-gallery
- https://reactbits.dev/components/dome-gallery
- https://reactbits.dev/components/infinite-menu
- https://reactbits.dev/components/flowing-menu
- https://reactbits.dev/components/card-swap
- https://reactbits.dev/animations/image-trail
- https://reactbits.dev/animations/sticker-peel
- https://reactbits.dev/micro/tear-ticket
- https://reactbits.dev/micro/paper-crumple
- https://reactbits.dev/text-animations/fold-text
- https://reactbits.dev/animations/noise
- https://reactbits.dev/components/counter
- https://reactbits.dev/text-animations/falling-text
- https://reactbits.dev/text-animations/scroll-velocity
- https://reactbits.dev/text-animations/text-type
- https://reactbits.dev/text-animations/split-text
- https://reactbits.dev/text-animations/variable-proximity
- https://reactbits.dev/text-animations/text-pressure
- https://reactbits.dev/animations/magnet
- https://reactbits.dev/micro/folder-float
- https://reactbits.dev/micro/branched-menu
- https://reactbits.dev/backgrounds/grainient
- https://reactbits.dev/animations/ripple-distortion
- https://reactbits.dev/components/morph-slider

**Codrops / tympanus**

- https://tympanus.net/codrops/2024/01/17/a-practical-introduction-to-scroll-driven-animations-with-css-scroll-and-view/
- https://tympanus.net/Development/ScrollCarousel/
- https://tympanus.net/codrops/2025/10/29/building-a-layered-zoom-scroll-effect-with-gsap-scrollsmoother-and-scrolltrigger/
- https://tympanus.net/Tutorials/TelescopeZoom/
- https://tympanus.net/Development/ImageExpansionTypography/
- https://tympanus.net/Development/StickySections/
- https://tympanus.net/codrops/2026/03/02/sticky-grid-scroll-building-a-scroll-driven-animated-grid/
- https://tympanus.net/Development/LayersAnimation/
- https://tympanus.net/Development/FullscreenClipEffect/
- https://tympanus.net/codrops/2025/05/27/animated-product-grid-preview-with-gsap-clip-path/
- https://tympanus.net/Tutorials/GridToFullPreview
- https://tympanus.net/codrops/2026/03/11/svg-mask-transitions-on-scroll-with-gsap-and-scrolltrigger/
- https://tympanus.net/Development/EaseReverseClipMenu
- https://tympanus.net/Tutorials/Scrollaroids/
- https://tympanus.net/codrops/2026/05/21/creating-scroll-driven-svg-map-animations-with-gsap/
- https://tympanus.net/codrops/2026/02/19/creating-a-smooth-horizontal-parallax-gallery-from-dom-to-webgl/
- https://tympanus.net/Tutorials/HorizontalParallaxGallery/index2.html
- https://tympanus.net/Development/3DStackMotion/
- https://tympanus.net/Development/EntranceAnimationForImages/
- https://tympanus.net/codrops/2026/06/04/creating-a-thumbnail-flow-animation-with-gsap-motionpath/
- https://tympanus.net/codrops/2026/01/20/animating-responsive-grid-layout-transitions-with-gsap-flip/
- https://tympanus.net/Tutorials/GridLayoutTransitions/
- https://tympanus.net/Development/GridViewSwitch/
- https://tympanus.net/codrops/2026/07/30/building-an-infinite-gsap-scroll-gallery-with-parallax-and-flip-transitions/
- https://tympanus.net/Tutorials/InfiniteScrollGSAPGallery/
- https://tympanus.net/codrops/2025/09/01/recreating-palmers-draggable-product-grid-with-gsap/
- https://tympanus.net/codrops/2026/07/27/between-print-and-digital-the-making-of-mersis-website/
- https://tympanus.net/codrops/2026/10/08/building-parallel-page-transitions-with-gsap-and-react-router/
- https://tympanus.net/codrops/2026/02/26/building-async-page-transitions-in-vanilla-javascript/
- https://tympanus.net/codrops/2026/10/07/interlude-astro-page-transitions/
- https://tympanus.net/Tutorials/Velvette/
- https://tympanus.net/codrops/2025/05/14/from-splittext-to-morphsvg-5-creative-demos-using-free-gsap-plugins/
- https://tympanus.net/codrops/2025/09/03/7-must-know-gsap-animation-tips-for-creative-developers/
- https://tympanus.net/Development/OnScrollTextHighlight/
- https://tympanus.net/codrops/2025/06/17/building-an-infinite-marquee-along-an-svg-path-with-react-motion/
- https://tympanus.net/codrops/2012/10/17/pfold-paper-like-unfolding-effect/
- https://tympanus.net/Development/GridItemHoverEffect/
- https://madewithgsap.com/codrops
- https://tympanus.net/codrops/2026/05/20/made-with-gsap-building-a-fun-gravity-based-mouse-trail/
- https://tympanus.net/Development/MotionTrailAnimations/
- https://tympanus.net/codrops/2026/09/24/custom-shaped-cursor-trail/
- https://tympanus.net/codrops/2025/06/11/building-an-infinite-parallax-grid-with-gsap-and-seamless-tiling/
- https://tympanus.net/Tutorials/InfiniteLayersGrid
- https://tympanus.net/codrops/2026/01/07/infinite-canvas-building-a-seamless-pan-anywhere-image-space/
- https://tympanus.net/codrops/2026/10/19/paper-shaders-off-background/
- https://tympanus.net/Demos/PaperDrops/
- https://tympanus.net/codrops/2026/10/18/real-folds-real-fire/
- https://tympanus.net/Tutorials/OnScrollFoldingCardboardBox/
- https://tympanus.net/codrops/2026/06/09/building-an-interactive-digital-stamp-collection-with-shaders-postcards-and-playful-inspection/
- https://tympanus.net/Development/RepeatingImageTransition/
- https://tympanus.net/codrops/2025/12/17/building-responsive-scroll-triggered-curved-path-animations-with-gsap/
- https://tympanus.net/codrops/2024/07/18/how-to-create-distortion-and-grain-effects-on-scroll-with-shaders-in-three-js/
- https://tympanus.net/codrops/2025/10/08/how-to-animate-webgl-shaders-with-gsap-ripples-reveals-and-dynamic-blur-effects/
- https://tympanus.net/Tutorials/WebGLBulge/
- https://tympanus.net/Development/IntroGridMotionTransition
- https://tympanus.net/Development/ContextAwareLogoAnimationScroll

**Osmo Supply**

- https://www.osmo.supply/resource/lenis-smooth-scroll-setup
- https://www.osmo.supply/resource/global-parallax-setup
- https://www.osmo.supply/resource/parallax-image-layers
- https://www.osmo.supply/resource/image-to-background-zoom
- https://www.osmo.supply/resource/scaling-element-on-scroll-gsap-flip
- https://www.osmo.supply/resource/stacking-cards-parallax
- https://www.osmo.supply/resource/collage-focus-card-on-hover
- https://www.osmo.supply/resource/horizontal-scrolling-sections
- https://www.osmo.supply/resource/stacking-sticky-cards-bounce
- https://www.osmo.supply/resource/dropping-cards-stack
- https://www.osmo.supply/resource/layout-grid-flip
- https://www.osmo.supply/resource/draw-svg-page-transition
- https://www.osmo.supply/resource/stacked-cards-page-transition
- https://www.osmo.supply/resource/masked-text-reveal
- https://www.osmo.supply/resource/solve-cut-off-letters-split-text
- https://www.osmo.supply/resource/text-scramble-load-scroll-hover
- https://www.osmo.supply/resource/variable-font-weight-hover
- https://www.osmo.supply/resource/draw-random-underline
- https://www.osmo.supply/resource/highlight-marker-text-reveal
- https://www.osmo.supply/resource/marquee-with-scroll-direction
- https://www.osmo.supply/resource/magnetic-hover-effect
- https://www.osmo.supply/resource/image-preview-cursor-follower
- https://www.osmo.supply/resource/velocity-based-custom-cursor
- https://www.osmo.supply/resource/directional-list-hover
- https://www.osmo.supply/resource/stacking-image-trail
- https://www.osmo.supply/resource/infinite-draggable-grid-basic
- https://www.osmo.supply/resource/draggable-stickers
- https://www.osmo.supply/resource/falling-2d-objects-matterjs
- https://www.osmo.supply/resource/auto-image-cycle-slideshow
- https://www.osmo.supply/resource/draw-path-on-scroll
- https://www.osmo.supply/resource/follow-svg-path-on-scroll
- https://www.osmo.supply/resource/film-grain-effect
- https://www.osmo.supply/resource/number-odometer
- https://www.osmo.supply/resource/willem-loading-animation
- https://www.osmo.supply/resource/welcoming-words-loader
- https://www.osmo.supply/resource/footer-parallax-effect
- https://www.osmo.supply/resource/scroll-to-next-page

**Aceternity / Magic UI / Motion Primitives / Cult UI / Animata / Skiper / 21st.dev**

- https://ui.aceternity.com/components/parallax-hero-images
- https://skiper-ui.com/v1/skiper30
- https://21st.dev/@danielpetho/components/parallax-floating
- https://21st.dev/@sshahaider/components/zoom-parallax
- https://21st.dev/@arunachalam/components/scroll-expansion-hero
- https://skiper-ui.com/v1/skiper16
- https://skiper-ui.com/v1/skiper54
- https://21st.dev/@soralabs/components/scroll-gallery
- https://ui.aceternity.com/components/focus-cards
- https://skiper-ui.com/v1/skiper52
- https://skiper-ui.com/v1/skiper17
- https://animata.design/docs/scroll/stacked-sections
- https://animata.design/docs/card/card-spread
- https://motion-primitives.com/docs/morphing-dialog
- https://motion-primitives.com/docs/text-scramble
- https://magicui.design/docs/components/hyper-text
- https://magicui.design/docs/components/highlighter
- https://www.cult-ui.com/docs/components/squiggle-arrow
- https://magicui.design/docs/components/scroll-based-velocity
- https://ui.aceternity.com/components/magnetic-button
- https://motion-primitives.com/docs/magnetic
- https://ui.aceternity.com/components/following-pointer
- https://skiper-ui.com/v1/skiper6
- https://animata.design/docs/image/trailing-image
- https://skiper-ui.com/v1/skiper73
- https://ui.aceternity.com/components/draggable-card
- https://skiper-ui.com/v1/skiper19
- https://ui.aceternity.com/components/tracing-beam
- https://magicui.design/docs/components/noise-texture
- https://magicui.design/docs/components/number-ticker
- https://motion-primitives.com/docs/sliding-number
- https://skiper-ui.com/v1/skiper8
- https://animata.design/docs/preloader/split-reveal

**Paper, physics and other libraries**

- https://github.com/ismamz/next-transition-router
- https://github.com/jorisnoo/matter-dom-plugin
- https://paperlab.nawwara.studio/
- https://kittygiraudel.com/2026/03/05/folded-corner-with-css/
- https://shaders.paper.design
- https://css-generators.com/fancy-frame/
- https://css-generators.com/custom-borders/
- https://github.com/NourMtir0722/Paperlab
- https://www.npmjs.com/package/paperlab
- https://css-shape.com/stamp/
- https://www.npmjs.com/package/vara
- https://www.unicorn.studio/docs/
- https://www.unicorn.studio/terms
- https://www.unicorn.studio/docs/embed/
- https://www.unicorn.studio/docs/performance/
- https://number-flow.barvian.me/

**Demo repos, reference sites and other**

- https://marijanapav.com/stamps
- https://tlb.betteroff.studio/
- https://joffreyspitzer.com/
- https://houseofyellow.nl/
- https://www.mersi-architecture.com
- https://codepen.io/osmosupply/pen/qEEKRrx
- https://www.laxspace.co/
- https://ten.375.studio/en
- https://github.com/JorgeCapillo/infinite-layers-grid
- https://github.com/edoardolunardi/infinite-canvas
- https://github.com/twotwentytwo-studio/codrops-paper
- https://github.com/buka-studio/www-marijanapav
- https://library.obys.agency/
- https://obys.agency/
- https://ponpon-mania.com/
- https://decathlonyestalgia.com/
- https://www.aralesk.es
- https://www.noth.in
- https://lamalama.com/
- https://www.jesperlandberg.com
- https://lightslefton.com
- https://www.mr-pandas-psychologically-safe-portfolio.com/
- https://studiolumio.com/
- https://revelatio.studio/
- https://375.studio/
- http://fantik.studio
- http://mater.agency
- https://guillaumecolombel.fr/
- https://chungsunglau.co.uk
- https://www.eduardbodak.com/
- https://www.12.studio/
- https://gatzara.studio/
- https://haoqi.design/
- https://matvoyce.tv/
- https://format.obys.agency/
