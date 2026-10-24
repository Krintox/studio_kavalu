# Motion studies of reference sites (queue item Q7), 2026-10-24

The brief asked: "use persistant browser to take frames screenshot each 1ms or any time apart and see
how can that be made … see if any of the researched websites had motion design."

**How it was captured.** `research/tools/motion_study.py` drives the persistent Chrome through a
scripted scenario (load, hover, click, wheel) and records three things together:

1. **Every painted frame** through `Page.startScreencast`. That is about 16 ms apart at 60 fps; 1 ms
   is not possible, because a browser only paints once per display refresh.
2. **A per-frame log**, from `requestAnimationFrame`, of up to 140 elements' page position, size,
   scale, rotation and opacity. Fitting each motion's progress curve against standard eases estimates
   its duration and easing.
3. **The browser's own records** of CSS transitions, CSS animations and Web Animations (CDP
   `Animation` domain), with their real durations, delays and easing curves.

Each folder holds `sheet.jpg` (16 frames across the run), `sheet_all.jpg` (up to 48 frames),
`analysis.json` and `log.json`. The footer studies (24 sites) are in `../footers/`.

---

## Digital Stamp Collection: https://marijanapav.com/stamps (`stamps-marijanapav/`)

- **What moves.** The hint "select a stamp to see the details" *writes itself in* over about 2.5 s
  ("…to fe…" → "…to see the data" → "…to see the details"), and then a hand-drawn arrow draws.
- **How it is made.** It is not a font. It is an SVG of 28 hand-drawn strokes
  (`aria-label="Select a stamp to see the details"`) inside a group with `pathLength="1"` and
  `stroke-dasharray="1 1"`. Each stroke's `stroke-dashoffset` runs from 1 to 0. The browser logged
  them as Web Animations of **250 ms ease-out**, staggered (52 animations including a doodled smiley
  drawn the same way). The stamps themselves are WebGL (R3F), so they are not in the DOM log.
- **Also.** Ruled paper fades at its edges through a horizontal gradient mask
  (`linear-gradient(90deg, transparent 0%, black 5%, black 95%, transparent 100%)`), and binder tabs
  run down the right edge.
- **For Kavalu.** Ananya's hand notes should *write themselves in*, once, at pen speed. The notes are
  set in a font (Homemade Apple), not strokes, so the faithful equivalent is a left-to-right reveal
  per line with a slight per-word unevenness, like a pen. Static under reduced motion.

## MERSI: https://www.mersi-architecture.com (`mersi/`)

- **What moves.** The home page is a split-screen project slider. Each wheel step moves the two
  halves in opposite directions, the new image revealed by a vertical wipe. A small project label
  card (name, place, type, year) changes to the next project's colour through a clip wipe, so for a
  moment it is half orange and half green.
- **How it is made.** It is a virtual-scroll slider (transformed list; page coordinates run into the
  hundreds of thousands), Webflow + GSAP, with expo-out glides.
- **For Kavalu.** The project-colour label is an idea for the spreads, which already wear each
  project's colours. Its opposing split-screen wipes are too big a move for this site.

## Obys' Design Books: https://library.obys.agency/ (`obys-books/`, `obys-books-lift/`)

- **What moves.** Pages are stacked paper sheets: a grey about-sheet over a white books-sheet, a
  spiral-bound strip on the right, a contact card. Clicking a sheet's edge **reshuffles the deck** in
  about 1.2 s:
  - 6.50 s: the stack shrinks and slides down-left;
  - 6.72 s: it falls off the bottom;
  - 6.86 s: the screen is empty;
  - 6.93–7.19 s: the new stack rises from the bottom, tilted about −8°;
  - 7.29–7.65 s: the chosen sheet arrives on top and settles.
- **Timings the browser reported.** Transforms are CSS transitions of **500 ms
  `cubic-bezier(0.215, 0.61, 0.355, 1)`** (ease-out-cubic). Colour and opacity changes are **350 ms
  `cubic-bezier(0.43, 0.195, 0.02, 1)`**. Idle loops: `fall-left` / `fall-right` (2–3 s, linear),
  `book-shake` (5 s) and `crawling-line` (20 s).
- **For Kavalu.** Paper as interface works, and Kavalu already does it (folder tabs, the desk). The
  reshuffle is too loud for decoration but right for a deliberate choice, such as filtering the work
  by road. Its 500 ms ease-out lift is a good benchmark for a card coming forward; Kavalu's
  `--e-settle` at 420 ms is in the same family.

## The Lookback: https://tlb.betteroff.studio/ (`lookback/`)

The capture rendered blank: an intro or WebGL stage that never painted for an automated tab. The
browser reported only a 1 s `noise` loop and a 500 ms `cubic-bezier(0.23, 1, 0.32, 1)` opacity
transition. Not usable as evidence, so nothing is taken from it.

---

## What Q7 takes from this, beside the footer studies

| Motion for Kavalu | Seen on | How it will be made |
|---|---|---|
| Hand notes write themselves in | Digital Stamp Collection (stroke write-on, 250 ms per stroke, staggered) | Left-to-right reveal per line at pen speed, once per note, when in view |
| Typed labels type on | Digital Stamp Collection's typewriter cards; reference 2; catalogue technique 17 | Characters appear at typing speed in Courier Prime, once; real text stays readable to screen readers; width locked |
| A card lifts when it is pointed at | Obys (500 ms ease-out-cubic) | `--e-settle` lift with a deeper paper shadow, pointer devices only |

Every addition has a reduced-motion version (it simply appears) and runs once. None of them loops.
