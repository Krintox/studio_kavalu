# Studio Kavalu: design principles v3

**Research for brief 3 (queue items Q13, Q15–Q20, Q22) · 24 October 2026**

This file answers the client's third brief: "do proper research on everything before making every decision,
see how top brand designers + web designers make websites acc to the brand and good design sense." It covers
space, type, surfaces, the cursor, parallax and smooth scroll, the intro, the brand statement and responsive
craft, each ending in a concrete proposal for Kavalu with numbers.

It sits beside `BRAND_DESIGN.md` (the system as built) and `kavalu_instructions.md` (the client's rules, which
outrank everything here). It changes nothing by itself: §10 lists the edits to make in those two files.

**How this was researched**

- **Live code of real studios, read on 24 Oct 2026.** Stylesheets of Here, Koto, Wolff Olins, JKR and Present
  were fetched directly. Markup of nvmbr.in, Obys, Heure Bleue, Collins, Adovasio and Working Stiff Films was
  read through the W3C validator's source view, because a plain fetch strips class names and scripts.
- **Library source and docs.**
  - Lenis: README and `maths.ts`. Darkroom's satus starter. Locomotive Scroll v5. GSAP ScrollSmoother.
  - Cuberto's open-source mouse-follower; Osmo's resources.
  - Codrops' Rapid Layers repo; the Digital Stamp Collection repo.
- **Standards and research.** WCAG 2.2 (2.3.1, 2.3.3, 1.4.4, 1.4.8, 1.4.10, 2.5.8); web.dev on LCP and reduced
  motion; A List Apart on vestibular triggers; NN/g on response times; Smashing on fluid type and zoom; the MIT
  study on rapid image sequences.
- **Our captures.** The 1440×900 captures of 23 Oct (`research/screens/`) were re-read for composition. They
  also caught some cursors and preloaders mid-state.
- **What was not used.** No browser automation, because the user's browser was busy, so nothing was
  frame-recorded for this file. Timings come from code, docs or CSS. Anything inferred from a still is marked.

**Markers used below**

| Marker | Meaning |
|---|---|
| **[CSS]** | Read from the site's live stylesheet or markup on 24 Oct 2026 |
| **[cap: file]** | Seen in our 1440×900 capture of 23 Oct 2026, `research/screens/<file>` |
| **[src]** | Read in published source code |
| **[docs]** | From the library's or standard's own documentation |
| **[catalog]** | From `motion_catalog.md` (researched 23 Oct), not re-checked today |
| **[unverified]** | Inferred, or could not be confirmed |

---

## Contents

0. [The short version](#0-the-short-version)
1. [Space and rhythm](#1-space-and-rhythm)
2. [Typographic hierarchy and scale](#2-typographic-hierarchy-and-scale)
3. [Surfaces and texture](#3-surfaces-and-texture)
4. [Custom cursors](#4-custom-cursors)
5. [Parallax and smooth scroll](#5-parallax-and-smooth-scroll)
6. [Intros and preloaders](#6-intros-and-preloaders)
7. [Presenting the brand statement](#7-presenting-the-brand-statement)
8. [Responsive craft, 320–1920 px](#8-responsive-craft-3201920-px)
9. [Reference URLs to record frame by frame](#9-reference-urls-to-record-frame-by-frame)
10. [Edits to make in BRAND_DESIGN.md and kavalu_instructions.md](#10-edits-to-make-in-brand_designmd-and-kavalu_instructionsmd)
11. [Sources](#11-sources)

---

## 0. The short version

1. **Space is vertical, not sideways.** The measured studios keep side margins at 24–62 px and put 128–256 px
   (14–28% of a 900 px-tall screen) between sections. For Kavalu: `--section-y` ≈ 158 px and `--chapter-y`
   ≈ 246 px at 1440×900 (§1.5).
2. **One idea per view.** A view holds one focal thing and at most two supporting ones. A section uses at most
   three type sizes and one moving thing (§1.4).
3. **Fewer, bigger type steps.** Collapse the 10 display tokens into 6. They should sit about 1.4× apart on
   desktop and about 1.25× apart on phones. Keep every `clamp()` maximum at 2.5× its minimum or less: four
   current tokens break this, which is a WCAG 1.4.4 risk (§2).
4. **Texture lives on each sheet, not on the screen.**
   - Bake the paper into each section's own background. Never use a full-screen fixed `mix-blend-mode` layer.
   - Under small labels, the darkest speck is at most 6% darker than the paper; at 9%, `--ink-faint` falls
     below AA.
   - On dark sheets, use a light speck at no more than +6% (§3).
5. **The cursor is a precise dot plus typed paper tags.**
   - The dot is 8 px and has no lag.
   - Tags such as "OPEN →" are offset from the pointer, so they never cover the work. They straighten from −4°
     to 0° as they appear.
   - The native cursor comes back on text, fields, the drawer, touch input and forced colours (§4).
6. **Parallax is felt, not watched.**
   - Photos move ±5% inside their frames. Hero prints move up to 40 px and ephemera up to 70 px.
   - Nothing else moves: not text, controls, backgrounds or grids.
   - Off below 900 px, on touch devices and with reduced motion (§5).
7. **Lenis stays at lerp 0.1.** It is frame-rate independent: 95% of a scroll in 0.50 s, 99% in 0.77 s. Use
   `wheelMultiplier` 1, native touch, and a scrub of `true` or ≤ 0.3 on top. Never go below lerp 0.08 (§5.1).
8. **The intro is a camera pull-back on the real hero.**
   - Her prints cut inside the centre stamp, from 200 ms down to 50 ms each. The camera pulls back to reveal the
     album page, her STUDIO / KAVALU lettering appears, then it becomes the header logo.
   - About 3.3 s in all, first visit only. Any input fast-forwards it, and it never runs with reduced motion (§6.6).
9. **The montage is flash-safe by construction.**
   - The fast frames are plum duotone, held between relative luminance 0.006 and 0.098. A change of under 0.10
     can never count as a WCAG 2.3.1 "general flash", at any size or speed, and there is no saturated red.
   - Only the last frame develops to full colour (§6.4).
10. **The hero is never hidden while the intro plays.** It renders under the intro from the first paint, so LCP
    is not delayed. web.dev confirms Chromium ignores `opacity: 0` elements for LCP (§6.4).
11. **The brand statement becomes the services index.**
    - The sentence stays still. Each of the four clauses is a link that draws a hairline road with a fork tick,
      once.
    - Hover dims the other clauses to no less than 50% (3.28 : 1) and shows one taped print in the margin.
    - Drop the ink-in and the inline pills: both are now off-the-shelf Framer components (§7).
12. **Responsive by content, tested by zoom.**
    - Keep the 1099 / 899 / 639 breakpoints, use `svh` for stage heights, and gate hover with `(hover: hover)`.
    - Keep targets at 40 px or more (WCAG asks for 24).
    - Test at 320–1920 px, and at 200% and 400% zoom (§8).

---

## 1. Space and rhythm

### 1.1 What the measured studios actually ship

Desktop values, mobile in brackets. The vertical share is measured against a 900 px-tall viewport.

| Studio | Body | Largest display | Display ÷ body | Side margin (desktop) | Vertical spacing | Share of a 900 px view | Text measures |
|---|---|---|---|---|---|---|---|
| **Here Design** https://www.heredesign.com [CSS] | 20 px serif (16) | `min(10vw, 148px)` | 7.4× | 32 px at ≥1512 (16 → 24 → 32) | block margins 6/8/10/12 rem; `py` 9 → 12 rem; `mt-[25vh]`, `mb-[25svh]`; intro `80svh` | 16–21%, 25% gaps | `35em`, 600 px, 820 px |
| **JKR** https://www.jkrglobal.com [CSS] | 18 px (`body-l` 1.125rem at ≥1440) | 9 rem (144 px); `max(4.375rem, 10vw)` below | 8× | statements inset 11–15 vw (`md:mx-[11.1vw]`, `lg:mx-[15vw]`) | `py-36` 144 px → `md:py-52` 208 px; `mb-44` 176 px; `lg:mt-[20vh]` | 16–23% | 48 rem, 64 rem |
| **Koto** https://koto.com [CSS] | 16 px (15) | 64 px | 4× | about 56 px (16-column grid, inferred from its `calc()` widths) | `md:py-63` 252 px; `pb-50` 200 px; hero `pt-115` 460 px | 22–28%, hero 51% | 248–905 px fixed widths |
| **Wolff Olins** https://www.wolffolins.com [CSS] | 16 px; long-form 20 px | 64 px (80 px at ≥1536) | 4–5× | 62 px (`--site-padding` 3.875rem at ≥1024) | `md:mb-64` 256 px; `md:gap-48` 192 px; long-form `pb` 25vh | 21–28% | intro `32ch`, prose `65ch`, `clamp(64ch, 70%, 96ch)` |
| **Present** https://www.presentstudio.co [CSS] | 15 px (14) | 50 px | 3.3× | 20 px base; `md:px-36` 90 px | 90–200 px (its root is 10 px) | 10–22% | prose 570 px |
| **Collins** https://www.wearecollins.com [CSS] (base tokens only; desktop overrides were truncated) | 18 px | 48 px (`--font-size-xl`, base) | 2.7× | 24 px minimum | `--section-padding` 3 rem, `--section-gap` 1.5 rem (base) | — | `--max-width` 768 px (base) |
| **November** https://www.nvmbr.in [CSS] | 16 px | 65 px at weight 100 | 4× | 29 px (`--main-gap`) | the content sheet starts after `margin-top: 100vh`, over a full-screen reel | a full viewport | — |

**What this says, read as a designer**

1. **Whitespace is vertical.** Side margins are modest (24–62 px). The air sits between blocks: 128–256 px on
   desktop, about a quarter of the viewport height. A whole viewport is reserved for one or two stage moments
   (Here's intro at 80svh, November's 100vh reel).
2. **The spacing is a short ladder.** Here uses 6, 8, 10 and 12 rem and almost nothing in between; Wolff Olins 6,
   8, 12 and 16 rem. Few steps, far apart, is what reads as calm.
3. **Body text is generous where the studio is editorial.** Here sets 20 px serif body text. The others use
   15–18 px.
4. **Line length is controlled in `ch`.** Wolff Olins ships the textbook values: 32 ch for an intro, 65 ch for
   prose.

### 1.2 What restraint looks like in one view [cap]

| Site | The first view | What it teaches |
|---|---|---|
| Collins [cap: wearecollins-com_0.jpg] https://www.wearecollins.com | One centred serif line, "Rewrite your worth." (≈72 px), and one row of award tags. The sentence covers about 4% of the screen, with ≈330 px of empty paper above it. | The confident move is to leave almost everything out. |
| JKR [cap: jkrglobal-com_1.jpg] https://www.jkrglobal.com | One paragraph at ≈62 px, a line pitch of ≈90 px (1.45), ≈30–35 characters per line, a left edge at 162 px (11% of the width). Nothing else. | A statement owns the view, set at a readable measure. |
| Koto [cap: koto-studio_1.jpg] https://koto.studio | Four lines at ≈32 px, a ≈640 px measure (≈45 characters), the second sentence in grey, ≈470 px empty below. | Two tones instead of two sizes. |
| Here [cap: heredesign-com_1.jpg] https://www.heredesign.com | A film, then one centred two-line statement with two italic phrases. | Image, then words; never side by side and competing. |
| Perky Bros [cap: perkybros-com_0.jpg] https://perkybros.com | One full-bleed photograph in an 18 px frame and one caption row ("Public Pool · Lounging Goods for Pool Days · 01 of 06"). | The work is the hero; the chrome is a caption. |
| Little Plains [cap: littleplains-com_1.jpg] https://www.littleplains.com | A label in a narrow left column, content starting at 28% of the width, and a 4-column logo grid on a 160 px pitch. | Asymmetry makes space without making emptiness. |
| Mythology [cap: mythology-com_0.jpg] https://www.mythology.com | One word, "WE", centred on black. | A sentence can be spread across screens. |
| Heure Bleue [cap: heurebleue-studio_1.jpg] https://heurebleue.studio | Two lines of giant serif on a colour field. | Scale is a form of restraint when there is only one thing. |

In every one of these, the first view holds one focal element and at most two supporting elements, not counting
the navigation.

### 1.3 Line length and leading

| Source | Rule |
|---|---|
| Butterick, *Practical Typography* [docs] https://practicaltypography.com/line-length.html | "Aim for an average line length of 45–90 characters, including spaces." |
| WCAG 2.2 SC 1.4.8 (AAA) [docs] https://www.w3.org/WAI/WCAG22/Understanding/visual-presentation.html | Width no more than 80 characters; line spacing at least 1.5 within paragraphs; paragraph spacing at least 1.5× the line spacing; no justified text. |
| Wolff Olins [CSS] | Intro 32 ch, prose 65 ch. |

Statements at display size run 25–45 characters a line (JKR ≈30–35, Koto ≈45) [cap].

### 1.4 How the restraint is achieved: the rules behind the numbers

1. **One idea per view.** One focal element (a sentence, a picture, a spread), at most two supporting ones (a
   label, an action), nothing that moves on its own except the focal element.
2. **The proximity ladder.** The gap between a label and its title is smaller than the gap between the title and
   its body. That is smaller than the gap between the body and its actions, which is much smaller than the gap
   between sections. Here: 2–3 rem inside a block, 6–12 rem between blocks [CSS].
3. **Few spacing values, far apart.** About five steps from the inside of a component to a chapter break.
4. **Asymmetry instead of centring everything.** Content starts on column 2–4 of 12 and leaves a quiet side
   (Little Plains at 28%, JKR at 11%).
5. **Small chrome.** Navigation, clocks and labels at 11–14 px. The space they don't take is given to the work.
6. **A motion budget.** One staggered list per view and one moving thing per screen. This is already
   `BRAND_DESIGN.md` §9.1.

### 1.5 Proposed spacing scale for Kavalu

The aim is Utopia-style fluid steps between 360 and 1440 px, capped above that, plus two rhythm tokens tied to the
viewport's height as well as its width. Utopia's own default space scale uses multipliers of 0.25, 0.5, 0.75, 1,
1.5, 2, 3, 4 and 6 of its base step [docs] https://utopia.fyi/space/calculator/.

**Inside components**

| Token | Value | 360 | 768 | 1440+ | Use |
|---|---|---|---|---|---|
| `--s-3xs` | `0.25rem` | 4 | 4 | 4 | hairline gaps, icon to text |
| `--s-2xs` | `0.5rem` | 8 | 8 | 8 | label to value, chip padding |
| `--s-xs` | `0.75rem` | 12 | 12 | 12 | caption to print |
| `--s-s` | `clamp(1rem, 0.917rem + 0.37vw, 1.25rem)` | 16 | 18 | 20 | lines in a group; pill gaps |
| `--s-m` | `clamp(1.25rem, 1rem + 1.11vw, 2rem)` | 20 | 25 | 32 | eyebrow to title |
| `--s-l` | `clamp(2rem, 1.5rem + 2.22vw, 3.5rem)` | 32 | 41 | 56 | title to body; body to actions |
| `--s-xl` | `clamp(3rem, 2.167rem + 3.7vw, 5.5rem)` | 48 | 63 | 88 | between blocks inside a section |
| `--s-2xl` | `clamp(4rem, 2.667rem + 5.93vw, 8rem)` | 64 | 88 | 128 | a statement to its supporting copy |

**Rhythm between sections** (heights depend on the screen)

| Token | Value | 390×844 | 768×1024 | 1280×720 | 1440×900 | 1920×1080 |
|---|---|---|---|---|---|---|
| `--section-y` | `clamp(5rem, min(14vh, 9vw) + 2rem, 11rem)` | 80 px | 101 px | 133 px | 158 px (18%) | 176 px |
| `--chapter-y` | `clamp(7rem, min(26vh, 16vw) + 1rem, 16rem)` | 112 px | 139 px | 203 px | 246 px (27%) | 256 px |
| `--stage` | `min-height: 100svh` | — | — | — | — | — |

- **`--section-y`** is the padding at the top and bottom of every section.
- **`--chapter-y`** is the gap at a chapter change: hero → spreads, spreads → statement, statement → roads, roads
  → founder, before the footer.
- **`--stage`** is reserved for one-idea views only: the intro, the statement and the first view of a case study.

`min(…vh, …vw)` keeps a short, wide laptop from getting phone-sized gaps, and a tall phone from getting desktop-sized
ones. The results sit inside the measured band: Here, JKR, Koto and Wolff Olins all fall between 128 and 256 px.

**Measures**

| Token | Value | Use |
|---|---|---|
| `--measure-body` | `62ch` | Body copy: about 600 px of 18 px Switzer, inside Butterick's 45–90 and WCAG's 80 |
| `--measure-lead` | `36ch` | Lead paragraphs (Wolff Olins uses 32 ch) |
| `--measure-caption` | `44ch` | Typed captions on strips |
| `--measure-statement` | `30ch` at display size | The brand line in 3–4 lines on desktop |

Keep `--margin` (16 → 72 px), `--gutter` and `--max` (1680 px) as they are. All three are inside the measured band.

**What changes from today**

- `BRAND_DESIGN.md` §8.3 says "about one screen of breathing room between chapters". Measured studios don't do
  this. A whole screen between every chapter makes a long page feel empty rather than spacious.
- Replace it with `--chapter-y`, about a quarter of the screen. Keep a full `--stage` for the two or three
  one-idea views.

### 1.6 The clutter audit

Run this on every section at 1440×900 and 390×844 (it belongs in the Q20 pass).

| Count in one view | Limit |
|---|---|
| Focal elements | 1 |
| Supporting elements (label, action, caption) | 2 |
| Type sizes | 3 (an eyebrow, a display step, body) |
| Things moving on their own | 1 (and pausable) |
| Scrapbook ephemera (tape, clips, stickers, notes) outside the hero collage and the footer desk | 2 |
| Mount types on one print | 1 (already a rule) |
| Distinct spacing values between siblings | 1 (always a token) |
| Lines in a heading | 4 at most |
| Buttons side by side | 2 |

A section that fails two of these is cluttered, whatever it looks like in isolation.

---

## 2. Typographic hierarchy and scale

### 2.1 Measured systems

| Studio | Families | Body | Display steps on desktop | Display ÷ body | Line height (display / body) | Display tracking |
|---|---|---|---|---|---|---|
| **Here** [CSS] | New Baskerville (text), Baskerville Display (h1, h2), Untitled Sans (labels) | 20 px serif | 148 (h1), 68 (h2), 40 (large body, quotes) | 7.4× | h2 1.088 / body 1.136 | −0.01em |
| **JKR** [CSS] | not readable | 18 px | 144 (h1), 72 (data), 64 (h2, h4), 36 (h3), 27 (h5) | 8× | 1em / 1.2em | −0.03em on data |
| **Wolff Olins** [CSS] | Untitled Serif (headlines) + Monument Grotesk (interface) | 16 px (20 px prose) | 64 (80 at ≥1536), 55, 45, 35, 30 | 4–5× | 1.07–1.2em / 1.5 | −0.0275em |
| **Koto** [CSS] | GT Kotoheim (sans, mono, condensed): one superfamily | 16 px | 64, 48, 44, 38, 36, 32 | 4× | 1.1–1.2 / 1.25 | −0.02em |
| **Present** [CSS] | Syllabus, roman and italic: one face | 15 px | 50, 34, 28 | 3.3× | 1.12 / 1.33 | +0.01em body; +0.05em caps |
| **Collins** [CSS, base tokens] | Portrait Text (serif) + Graphik (sans) | 18 px | 48 (xl), 29 (primary) | 2.7× (mobile base) | 1 / 1.35 | −0.02em |
| **November** [CSS] | Delegate, its own face | 16 px | 65 at weight 100 | 4× | 1.2 / 1.2 | — |

How many sizes in all, including tiny labels:

| Studio | Sizes |
|---|---|
| Here | 9 semantic sizes, 12 with utilities |
| Collins | 8 |
| Present | 10 |
| Wolff Olins | 14 |
| Koto | 18 (Tailwind utility sprawl) |

### 2.2 The patterns

1. **One or two families.** Studios with their own type use a single family for everything: Koto, November,
   Present.
2. **Two speeds.**
   - A tight text scale (14, 16, 18, 20, 24, about 1.125–1.2 apart), then a jump to two to four display sizes
     about 1.5–2.2 apart.
   - Examples: Here goes 24 → 40 → 68 → 148; Wolff Olins goes 30 → 45 → 64.
   - Hierarchy comes from big jumps, not many steps.
3. **Display is 4–8× the body on desktop.** The bigger the display, the fewer display sizes.
4. **Display is tight, body is open.** Display line height 1.0–1.1 and tracking −0.01 to −0.03em. Body 1.2–1.4 at
   16–20 px.
   - Kavalu's 1.55 for 18 px Switzer is right: WCAG 1.4.8 asks for 1.5, and a grotesk at that size wants it.
5. **Display stops growing at 1440–1536 px.**
   - JKR fixes its h1 at 9 rem from 1440 up. Wolff Olins steps to 5 rem only at 1536. Here caps its h1 at 148 px.
6. **Labels are capitals with +0.05–0.1em tracking.** Present uses 0.05em, JKR 0.08em. Kavalu already uses
   0.08em.

### 2.3 Kavalu today

- **Fifteen sizes, ten of them display.** Measured at 1440: 155, 117, 97, 89, 79, 67, 57, 53, 42 and 34 px.
  Several neighbours are only 5–9% apart (97 and 89, 57 and 53). A step that small doesn't read as a different
  level; it reads as a mistake.
- **Four tokens break the zoom rule.** Their `clamp()` maximum is more than 2.5× the minimum:

  | Token | Max ÷ min |
  |---|---|
  | `--t-mega` | 3.24 |
  | `--t-spread` | 2.71 |
  | `--t-1` | 2.79 |
  | `--t-manifesto` | 2.68 |

  Maxwell Barvian's rule: "If the maximum font size is less than or equal to 2.5 times the minimum font size", the
  text always passes WCAG 1.4.4 in modern browsers, which zoom to 500% [docs]
  https://www.smashingmagazine.com/2023/11/addressing-accessibility-concerns-fluid-type/. Adrian Roselli shows
  the failure itself: vw-sized text that "starts at 64px tall, at 200% zoom has only increased to 68px" [docs]
  https://adrianroselli.com/2019/12/responsive-type-and-zoom.html.

### 2.4 Proposed scale

Six display steps. Each step is linear between 360 and 1440 px and capped, with a maximum of 2.5× the minimum or
less. The ratio between steps is about 1.4 on desktop (√2) and about 1.25 on phones (a major third), which is
Utopia's principle of a gentler scale on small screens.

| New token | `clamp()` | 360 | 768 | 1024 | 1440+ | Max ÷ min | Line height | Tracking | Replaces |
|---|---|---|---|---|---|---|---|---|---|
| `--d1` mega | `clamp(4rem, 2rem + 8.89vw, 10rem)` | 64 | 100 | 123 | 160 | 2.50 | 0.9 | −0.035em | `--t-mega` |
| `--d2` title | `clamp(3.25rem, 2rem + 5.56vw, 7rem)` | 52 | 75 | 89 | 112 | 2.15 | 0.95 | −0.03em | `--t-spread`, `--t-1` |
| `--d3` statement | `clamp(2.5rem, 1.583rem + 4.07vw, 5.25rem)` | 40 | 57 | 67 | 84 | 2.10 | 1.04 | −0.022em | `--t-hero`, `--t-manifesto` |
| `--d4` section | `clamp(2rem, 1.417rem + 2.59vw, 3.75rem)` | 32 | 43 | 49 | 60 | 1.88 | 1.08 | −0.018em | `--t-2` |
| `--d5` sub | `clamp(1.625rem, 1.333rem + 1.3vw, 2.5rem)` | 26 | 31 | 35 | 40 | 1.54 | 1.15 | −0.012em | `--t-quote`, `--t-sheet`, `--t-3` |
| `--h` card | `clamp(1.375rem, 1.25rem + 0.556vw, 1.75rem)` | 22 | 24 | 26 | 28 | 1.27 | 1.2 | −0.01em | `--t-4` |
| `--lead` | `clamp(1.125rem, 1rem + 0.37vw, 1.375rem)` | 18 | 19 | 20 | 22 | 1.22 | 1.45 | 0 | (new) lead paragraphs |
| `--t-body` | unchanged | 16 | 17 | 17 | 18 | 1.12 | 1.55 | 0 | — |
| `--t-small`, `--t-label`, `--t-tiny` | unchanged (14 / 11 / 10) | | | | | | | | — |

- **Fewer sizes.** That gives 11 sizes instead of 15; drop `--t-micro` (12 px) into `--t-label` or `--t-small`.
- **Steps at 1440.**
  - The display steps go 160 → 112 → 84 → 60 → 40 → 28, and the text steps 22 → 18.
  - Between neighbours that is ×1.43, 1.33, 1.40, 1.50, 1.43, 1.27 and 1.22.
- **How a page uses them.** A page uses at most three display steps: D2 or D3 for its title, D4 for sections, D5
  for quotes. D1 is only for a case-study title or the intro name.
- **Kept:** one italic phrase per heading (`BRAND_DESIGN.md` §5.4). Here sometimes uses two in one sentence;
  Kavalu's one is stricter and better.

### 2.5 For the font change (Q14)

- **The faces may change; the scale does not.** These sizes assume a display face with an x-height near
  Gambetta's. If Q14 picks a face with a smaller x-height (a classic Didone), raise D3–D5 by one step of about
  6–8% instead of adding tokens. If it picks a larger one (a wide grotesk), lower them.
- **Re-check the measure after the change.** The `ch`-based measures in §1.5 need checking against the final
  face, because `ch` is the width of its "0".

---

## 3. Surfaces and texture

The client: "the background should be a texture rather than solid colours." What the research says about doing
that without hurting legibility or speed:

### 3.1 How tactile sites build paper

| Site | Technique | Numbers |
|---|---|---|
| **Digital Stamp Collection** https://marijanapav.com/stamps (source: https://github.com/buka-studio/www-marijanapav) [src] | An SVG of fractal noise lit by `feDiffuseLighting`, so it reads as fibres with relief rather than salt-and-pepper. A second set of filters adds grain, grainy distortion and a hand-drawn squiggle. | Paper SVG is 537 bytes: `feTurbulence` fractalNoise, `baseFrequency 0.1`, `numOctaves 3`; diffuse light `surfaceScale 2`, azimuth 45, elevation 60; drawn at **7.5% opacity**. The in-page `paperFilter` uses frequency 0.8 with 5 octaves; the grain filter 1.45 with 3 octaves; `grainyDistortFilter` displacement scale 7. |
| **Working Stiff Films** https://stiff.madebybuzzworthy.com [CSS] [cap: stiff-madebybuzzworthy-com_0.jpg] | A fixed 140vw × 140vh overlay of a transparent PNG (`noise-min.png`, alpha baked in, no blend mode), jittered by a 1 s, 10-step `translate` loop. This is film grain, not paper. | `opacity: 1`, offset −20vw / −20vh, steps ±20vw / ±20vh |
| **Lynn Fisher** https://lynnandtonic.com [cap: lynnandtonic-com_0.jpg] | Sparse light specks on near-black: a "dark paper" that stays quiet. | — |
| **Immersive Garden** https://immersive-g.com [cap: immersive-g-com_1.jpg] | Embossed paper relief rendered in WebGL; the paper is the hero. | — |
| **Studio N°7** https://www.studionumberseven.com [cap: studionumberseven-com_0.jpg] | A photographed sheet with fold lines, stains and specks. This is the friend's studio, so **Kavalu must not look like this**: no scanned folds or stains. | — |
| **CSS-Tricks, "Grainy gradients"** https://css-tricks.com/grainy-gradients/ [docs] | `feTurbulence` fractalNoise at `baseFrequency 0.65`, 3 octaves, `stitchTiles`. A gradient is layered over it, then `filter: contrast(170%) brightness(1000%)` and a blend mode, inside `isolation: isolate`. | A reader's comment says it costs performance. |

### 3.2 Legibility: how strong the grain may be

Contrast was computed with the WCAG 2.2 relative-luminance formula, at the *darkest speck* of the texture (where
contrast is lowest), for the palette's text tokens:

| Light paper, `multiply` speck | Cream as is | 3% darker | **6% darker** | 9% darker | 12% darker |
|---|---|---|---|---|---|
| `--ink` (body) | 15.89 | 14.92 | 13.87 | 12.98 | 12.13 |
| `--plum` (headings) | 14.91 | 14.01 | 13.02 | 12.19 | 11.39 |
| `--ink-soft` (labels) | 7.34 | 6.89 | 6.40 | 5.99 | 5.60 |
| `--ink-faint` (small labels, 4.5 : 1 needed) | 5.42 | 5.09 | **4.73** | 4.43 ✗ | 4.14 ✗ |

| Dark paper, `screen` speck | As is | +3% | **+6%** | +9% |
|---|---|---|---|---|
| Cream on deep plum | 16.70 | 15.81 | 14.68 | 13.59 |
| Cream at 60% (the legal line) on deep plum | 6.38 | 6.04 | 5.61 | 5.19 |
| Powder blue on deep plum | 11.06 | 10.47 | 9.71 | 9.00 |
| Cream on oxblood | 12.85 | 11.87 | 10.83 | 9.97 |

**Rule.**

- **Under text of any size,** the darkest speck of a light paper is at most 6% darker than the paper. On
  `multiply` that means a texture value of 0.94 or more (`#F0F0F0` and lighter). At 9%, `--ink-faint` labels
  fail AA.
- **Behind display type only,** the darkest speck may go to 12% darker.
- **On dark paper,** the light speck stays at +6% or less.
- **Test with the texture,** never against the flat hex.

### 3.3 Speed

- **Bake the texture into each surface's own background.** Use
  `background-image: url(fibre), url(grain); background-blend-mode: multiply` on the section, not a fixed
  full-screen layer with `mix-blend-mode`.
- **Why not a fixed blend layer.** The reports show the risk: a blended layer was the main cause of poor
  scrolling in Chrome on a Mac (Webflow forum), animations stuttered in Chromium under a blended element (GreenSock
  forum), and fixed elements can force full-screen repaints (WebKit bug 72078). These are anecdotal reports; no
  benchmark was found, so measure with paint flashing before shipping any fixed overlay. Kavalu's `body` already
  does the right thing (`background-blend-mode: multiply` on the body's own background).
- **Never `background-attachment: fixed`.** It repaints on every scroll (measured at about 10 fps on one site),
  and iOS ignores it (Four Kitchens) https://fourkitchens.com/?p=1517.
- **A live `filter: url(#noise)` on a large element repaints.** An SVG used as a *background image* is drawn once
  per tile and cached, which is why the Stamp Collection's 537-byte paper is cheap. Live full-screen
  `feTurbulence` is not cheap ([catalog] technique 36).
- **Tiles and files.**
  - Grain: a 256 px CSS tile from a 512 px file, so it stays sharp on 2× screens.
  - Fibre: a 512 px CSS tile from a 1024 px file.
  - Use WebP or AVIF: under 40 KB for grain and under 60 KB for fibre, under 150 KB for all textures together.
  - Today `grain-alpha.png` (108 KB), `paper-grain.png` (44 KB) and `worn-light.png` (36 KB) total 188 KB as
    PNG; WebP would roughly halve that [unverified estimate].
- **Hide the repeat.**
  - Layer two textures whose tile sizes don't share factors, such as 256 and 373 px. Together they repeat only
    every 95,488 px.
  - Shift each section's `background-position`, so neighbouring sheets never line up.

### 3.4 Dark sheets and colour fields

- **`multiply` grain is invisible on deep plum and oxblood.** Use a separate light-speck tile (alpha PNG or WebP)
  with `background-blend-mode: screen` (or `soft-light`) at +3–6%. An optional `multiply` fibre at 3% adds depth.
- **Mid-tone project colours** (Anokhi `#9F4A30`, Not-So-Onam `#A11F5B`): use `soft-light` at 6–8%, which
  lightens and darkens evenly.
- **Grain on paper never moves.** Working Stiff's 1 s jitter is film grain. On paper it reads as television
  static, and it is a perpetual motion that WCAG 2.2.2 would want paused.
- **Film is the exception.** A film section may have film grain at 8–12 fps (`steps(4)`), paused off-screen and
  under reduced motion.

### 3.5 Proposal: a material for each kind of surface

| Surface | Where | Texture recipe | Strength |
|---|---|---|---|
| **Album page** | Cream page background | Fibre (low frequency, 0.04–0.1; diffuse-lit like the Stamp Collection) + fine grain (0.8–0.9, 3–4 octaves), `multiply` | Darkest speck 5–6% |
| **Bright paper** | Prints, stamps, polaroids, typed strips | Grain only, `multiply` | Half the page's strength (≈3%): paper you hold is smoother than the page |
| **Note paper** | Ruled sheets, the letter, notes | Grain + faint fibre | 4–5% |
| **Desk board** | Deep plum footer and desk | Light specks, `screen` + 3% `multiply` fibre | +4–6% |
| **Warm board** | Oxblood sections and cards | As the desk board | +4–6% |
| **Project fields** | A project's own spread and hero | `soft-light` grain | 6–8% |
| **Kraft** | The onboarding envelope | Stronger fibre, `multiply` | Up to 10% (no small text on it) |
| **Never** | Photographs (they keep their own grain), the logo (`BRAND_DESIGN.md` §3.7), type | — | 0 |

This gives the scrapbook a hierarchy of materials (page, sheet, note, board, kraft) without adding a colour.

---

## 4. Custom cursors

The brand book currently forbids custom cursors (`BRAND_DESIGN.md` §1.6, §9.8). Brief 3 asks for "cursor design …
on hover and in general … cursor changes on specific section". The client's rule wins, so the job is to do it
without the gimmicks the old rule was guarding against.

### 4.1 What studio sites do

| Site | What the cursor does | Numbers | Evidence |
|---|---|---|---|
| **Cuberto** https://cuberto.com, and its library https://github.com/Cuberto/mouse-follower | A dot (a 48 px element scaled to 0.2, ≈10 px) that *shrinks* to 0.15 on links. It grows to 1.7 (≈82 px) with a text label, 1.5 with an icon, and opens a 400 px media box scaled to 0.696 (≈278 px) for image or video previews. Optional skew with speed; "inverse" and "exclusion" states. | Follow `speed: 0.55`, `ease: 'expo.out'`. State change 0.25 s ease-in-out on transform; label 0.3–0.4 s; hides 300 ms after the pointer leaves. | [src]; these are the library's defaults, and cuberto.com's own settings are [unverified] |
| **Heure Bleue** https://heurebleue.studio | The **native cursor is kept**. A 10 px orange dot rides beside it, and a 27 px-tall label with a 1 px border, rotated 5°, **straightens to 0°** when it shows text. Hidden below 1024 px. | 0.3 s on a custom ease | [CSS] [cap: heurebleue-studio_1.jpg] |
| **Dennis Snellenberg** https://dennissnellenberg.com | In the work list, a ≈396 px card of the project follows the pointer, an 80 px blue "View" disc sits on the hotspot, and the other rows dim to grey. | — | [cap: dennissnellenberg-com_1.jpg] |
| **Exo Ape** https://exoape.com | In the hero only, the cursor is a ≈84 px dark translucent disc reading "Scroll": a state that belongs to one section. | — | [cap: exoape-com_1.jpg] |
| **Perky Bros** https://perkybros.com | Over the full-bleed lead image, the cursor becomes the words "View Project". | — | [cap: perkybros-com_0.jpg] |
| **DixonBaxi** https://www.dixonbaxi.com | A small black dot of about 8 px. | — | [cap: dixonbaxi-com_0.jpg]; whether the native cursor is hidden is [unverified] |
| **Osmo, velocity cursor** https://www.osmo.supply/resource/velocity-based-custom-cursor | An arrow-shaped SVG that tracks the pointer exactly (no lerp) and tilts with horizontal speed. | Rotation = speed × 100, clamped to ±70°, eased 0.1 per frame, decaying 0.05 per frame. Hidden on `(hover: none) and (pointer: coarse)`. No reduced-motion handling. | [docs] |
| **14islands** https://www.14islands.com | States for a hover label, scroll progress, the loader and media following. A rAF loop writes normalised CSS variables and stops when the mouse is idle. | Warns that a lerp "speed" close to 0 "could provide rendering lag". | [docs] https://v3.14islands.com/blog/developing-a-performant-custom-cursor |
| **Lux Expression** https://luxexpression.com · **Waaarhol** http://waaarhol.com · **Typography Principles** (Obys) https://typographyprinciples.obys.agency | A small yellow dot that echoes the site's infographics; a circle that inverts what it covers; a grey circle. | — | Awwwards' cursor article https://www.awwwards.com/customize-your-mouse-cursor-inspirational-examples-implementation-tricks.html; sites [unverified] |
| **LAX Space** https://www.laxspace.co | The pointer unrolls a strip of duct tape along a smoothed path: a paper-native idea. | — | [catalog] §5b |

**What the numbers converge on**

| Part | Range seen |
|---|---|
| Dot | 8–10 px |
| Labels | either small tags (27 px tall, Heure Bleue) or discs of 72–84 px (Cuberto, Snellenberg, Exo Ape) |
| Media previews | 278–400 px |
| Follow speed | a direct pointer for the dot (Osmo, Heure Bleue's dot); 0.3–0.55 s for the floating part (Cuberto) |
| State changes | 0.25–0.4 s |

### 4.2 Accessibility and engineering rules

1. **The native cursor carries user settings.** Enlarged pointer size, high contrast, macOS shake-to-find: a
   replacement loses them. Hide the native cursor "only after the follower has mounted and confirmed it is
   running" [docs] https://21st.dev/blog/custom-cursor-react.
2. **A JS cursor can fall behind.** "Low battery mode can limit the frame rate" of a fake cursor (CSSWG issue
   #9813) [docs] https://lists.w3.org/Archives/Public/public-css-archive/2024Jan/0474.html. Lenis documents
   Safari's cap at 60 fps, and 30 fps in Low Power Mode [docs]. **So the dot must never lag:** only the label may
   ease.
3. **Fine pointers only, decided by input as well as media query.** `(hover: hover) and (pointer: fine)` describes
   only the *primary* pointer, so a touchscreen laptop passes it. Show the follower only after a `pointermove` with
   `pointerType === "mouse"`; hide it on any touch or pen `pointerdown`.
4. **Text and fields keep their native cursors.** Children inherit a custom `cursor` from `body`, so restore it
   explicitly: `input, textarea, select, [contenteditable] { cursor: auto }`; the onboarding drawer is all
   native; long selectable copy shows the I-beam (`cursor: text`).
5. **Dialogs and the top layer.** A fixed-position cursor sits under `<dialog>` and popovers (CSSWG #9813), so
   hide it whenever the drawer or a dialog is open.
6. **Reduced motion.** "Drop the interpolation and either pin the element to the exact pointer position or skip
   rendering it" [docs] (21st.dev). Under WCAG 2.3.3, motion triggered by interaction should be possible to turn
   off [docs] https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html.
7. **Forced colours.** Under `@media (forced-colors: active)`, remove the custom cursor and restore `cursor: auto`.
8. **The information lives in the element, not the cursor.** Labels are decorative (`aria-hidden`); the link text
   already says what happens. Keyboard focus never triggers cursor states.
9. **Native cursor images, if used.** Browsers cap them at 128×128 px; MDN recommends 32×32. A keyword fallback
   is mandatory. PNG and SVG with a natural size are supported [docs]
   https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/cursor.
10. **Performance.**
    - One passive `pointermove` on `window`; transforms written in the GSAP ticker.
    - No `getBoundingClientRect` inside `pointermove`: cache rects on `pointerenter`.
    - `pointer-events: none` and `will-change: transform` on the cursor layer.

### 4.3 What reads as slop

- **Big lazy shapes.** A large blurred blob with `mix-blend-mode: difference` trailing 200 ms or more behind the
  pointer.
  - On Kavalu, `difference` also produces colours outside the palette, such as green on plum.
- **"VIEW" on everything.** A view bubble on every image, including ones that aren't links.
- **Covering the work.** A centred 100 px+ disc over the very picture it invites you to open.
- **Magnetism and trails.** Magnetic pull on every link; trails, sparkles and particles; velocity squash and
  stretch on every move.
- **Cursors that break basics.**
  - The I-beam replaced over text and fields.
  - A dot left stranded on touch screens.
  - The cursor hidden over video.
- **The scrapbook trap.** A pencil, washi-tape or sticker cursor everywhere is twee. Paper motifs belong in the
  labels; the pointer itself stays a precise dot.

### 4.4 Proposed Kavalu cursor system

**Concept:** an ink dot and typed tags. The dot is the pen's point, exact and never late. When something can be
done, a small typed paper tag appears beside the dot, tilted, and straightens as it lands, the way Kavalu's
pieces already straighten when you point at them (`BRAND_DESIGN.md` §6.4). This is Heure Bleue's move, in
Kavalu's own materials.

| State | When | Look | Size | Motion |
|---|---|---|---|---|
| **Dot** | The page, on a fine pointer | Plum `#390D26` dot with a 1.5 px cream ring | 8 px (11 px with the ring) | Exactly on the pointer, no lerp |
| Dot on dark | `data-tone="dark"`: deep plum, oxblood, the footer | Cream dot, plum ring | 8 px | Colour swap 180 ms (`--d-quick`) |
| Dot on a project | Inside a project's own spread or hero | The project's ink colour (`--p-ink`) | 8 px | Swap 180 ms. The work changes the room, and the cursor is part of the room. |
| **Ring** | Navigation, pills, standalone "→" links | Dot + a 36 px ring, 1.25 px plum stroke, no fill | 36 px | Scale 0.5 → 1, 0.24 s `settle`; follows with `quickTo` 0.18 s `power3` |
| **Text** | Paragraphs, captions, anything selectable | The native I-beam; follower hidden | system | — |
| **Field** | Inputs, selects, the drawer, any dialog | The native cursor; follower hidden | system | — |
| **OPEN tag** | Stamps, spreads, work cards, next project, the hero stamp | "OPEN →" typed on bright paper: Courier Prime capitals 10 px, +0.08em, plum, a 1 px `--rule-strong` border, a small shadow. It sits +14 / +14 px off the hotspot, so it never covers the work. | 22 px tall | In: scale 0.9 → 1 and rotate −4° → 0°, 0.3 s `settle`. Out: 0.18 s. Position: `quickTo` 0.25 s `power3`. |
| **DRAG tag** | The album row, the desk | "← DRAG →". While dragging, the tag hides and the dot shrinks to 6 px. | 22 px | As OPEN |
| **MOVE tag** | Desk pins | "MOVE" | 22 px | As OPEN |
| **PLAY / PAUSE tag** | Films and reels | "PLAY" / "PAUSE" | 22 px | As OPEN |
| **ROAD tag** | The statement's four clauses (§7, proposal A) | "ROAD 02 · OPEN →" | 22 px | As OPEN |
| **Preview** | /work index rows | The existing tilted stamp that follows the cursor (catalog technique 23). Never shown together with a tag. | as built | as built |
| **Hidden** | Iframes, the drawer, dialogs, a window losing focus, touch input | — | — | Fade 0.15 s |

**Rules**

- **States come from markup.** Use `data-cursor="open | drag | move | play | road"` and `data-cursor-tone`, read on
  `pointerover` with `closest()`. Never hit-test every frame.
- **Tags are sheets of paper.**
  - On blue paper (service cards, tickets), the tag turns cream; on a dark sheet it is powder blue with deep plum
    text (11.1 : 1).
  - The arrow comes from the system font (§5.7 of the brand book).
- **Magnetic pull on three controls only:** "Start a project" in the header and the hero, and "Send the letter".
  The pill moves at most 4 px and its label 6 px, at 0.25× the pointer's offset. It returns in 0.5 s
  `power3.out` and never moves on keyboard focus.
- **Reduced motion.** The dot stays: its position is not an animation. Tags and the ring appear and disappear
  with no scale or rotation, and track the pointer exactly.
- **Off below 900 px, and on any touch input,** whatever the width.

**Note on the current v3 build** (`research/working-shots/v3/cursor/states.jpg`, 24 Oct)

- **Keep.** The dot, the link ring and the cream dot on dark already match this.
- **Change.** The DRAG and OPEN states are blue discs of about 110 px, centred on the hotspot. They cover the
  middle of the picture they invite you to open. Replace them with the offset tag, or at least shrink them to
  72 px or less and move them off the hotspot.

---

## 5. Parallax and smooth scroll

### 5.1 What the libraries default to, and what their makers ship

| Library / site | Setting | What it means | Evidence |
|---|---|---|---|
| **Lenis** (default) | `lerp 0.1`, `duration 1.2` (ignored when lerp is set), `wheelMultiplier 1`, `touchMultiplier 1`, `smoothWheel true`, `syncTouch false`, `syncTouchLerp 0.075`, `touchInertiaExponent 1.7` | The frame-rate-independent `damp(x, y, lerp × 60, dt) = lerp(x, y, 1 − e^(−λ·dt))`. It snaps when both values round to the same pixel. | [src] https://github.com/darkroomengineering/lenis (README, `packages/core/src/maths.ts`, `animate.ts`) |
| **Darkroom's satus starter** (the Lenis authors' own) | `wheel.lerp 0.125`, `programmatic.lerp 0.125` (Lenis 2.0 option groups), `autoRaf false` (their tempus loop drives it) | A little snappier than the default | [src] https://github.com/darkroomengineering/satus/blob/main/components/layout/lenis/index.tsx |
| **Locomotive Scroll v5** (built on Lenis 1.3.17) | `lerp 0.1`, `duration 1.2`, `wheelMultiplier 1`, `touchMultiplier 2`, `smoothTouch false` | — | [docs] https://scroll.locomotive.ca/docs/documentation/options |
| **GSAP ScrollSmoother** | `smooth` defaults to 0.8 s of catch-up. Smoothing on touch is off by default (0.1 s suggested). | Not used with Lenis | [docs] https://gsap.com/docs/v3/Plugins/ScrollSmoother/ |

**Lenis lerp turned into time**, computed from its own `damp` formula and the same at any refresh rate:

| `lerp` | 95% of the way | 99% | A 100 px wheel step snaps at | Feel |
|---|---|---|---|---|
| 0.06 | 0.83 s | 1.28 s | 1.47 s | Ice: the catalog's anti-list already bans this |
| 0.08 | 0.62 s | 0.96 s | 1.10 s | Floaty: the lowest acceptable value |
| 0.09 | 0.55 s | 0.85 s | 0.98 s | Soft |
| **0.10** | **0.50 s** | **0.77 s** | **0.88 s** | **Kavalu today; the Lenis and Locomotive default** |
| 0.125 | 0.40 s | 0.61 s | 0.71 s | Darkroom's own choice |
| 0.15 | 0.33 s | 0.51 s | 0.59 s | Close to native |

### 5.2 Tasteful parallax intensities

| Source | Guidance |
|---|---|
| **Locomotive** [docs] https://scroll.locomotive.ca/docs/documentation/attributes | `data-scroll-speed` is relative to the container: displacement = progress × containerSize × speed. "Start with small values like 0.1 to 0.5 for subtle effects." Speed 0.1 moves an element 0.2× the container height in total, about 180 px on a 900 px screen. **Parallax is off on touch devices by default.** |
| **Osmo, global parallax** [docs] https://www.osmo.supply/resource/global-parallax-setup | Defaults run from +20% to −20% (`yPercent`) between `top bottom` and `bottom top`, with `scrub: true`. For an image inside a frame, it uses a target 120% tall inside `overflow: hidden`. Can be turned off per breakpoint (tablet 991 px, mobile 767 / 479 px). |
| **GSAP ScrollSmoother** [docs] | `data-speed="0.5"` is half the scroll speed. `"auto"` computes how far a larger child can move inside its `overflow: hidden` parent. `clamp()` keeps elements above the fold at their natural place. `data-lag="0.5"` catches up in 0.5 s. |
| **Kavalu's catalog** [catalog] technique 2 | `yPercent` −6 to +6 on images inside frames; 20–60 px on stickers. |

Kavalu should sit **below** Locomotive's "subtle" floor. Its 0.1 already moves 180 px; Kavalu's maximum is 80 px.
That is the brand's "felt, not watched".

### 5.3 Where premium sites use parallax

- **A picture drifting inside its frame.** The frame stays on the grid and only the picture moves. This is the
  safest form, because nothing changes position relative to the text. Osmo's 120% target is this pattern; Exo
  Ape's photography is the common reference [unverified amplitude].
- **Layered collage depth.** Paper layers at two or three speeds: 14islands' cut-out collage
  [cap: 14islands-com_1.jpg], Ponpon Mania's illustration planes [catalog].
- **The footer uncover.** The last section lifts away from a footer that sits underneath (Osmo's footer parallax)
  [catalog] technique 41. Kavalu's wordmark arrival is already a version of this.
- **Not on everything.** "Parallax on every image" is on the catalog's dated-tropes list [catalog] §7.

### 5.4 Pitfalls

1. **Vestibular triggers.**
   - "Exaggerated parallax and scrolljacking animations are highly likely to be triggering". Motion in the
     direction opposite to the scroll is "a nasty surprise", and trouble grows with how much of the viewport moves
     (Val Head, A List Apart, 2015, updated 2020) [docs]
     https://alistapart.com/article/designing-safer-web-animation-for-motion-sensitivity/.
   - web.dev names parallax and zooming as triggers of "dizziness, nausea, and migraine headaches" [docs]
     https://web.dev/articles/prefers-reduced-motion.
   - **So:** small amplitudes, same direction as the scroll, never on large areas, off under reduced motion
     (WCAG 2.3.3 names parallax).
2. **Double smoothing.** Lenis smooths the scroll, so a `scrub` of 1 or more on top of it lags twice and feels
   like mush. Use `scrub: true` for parallax and 0.3 or less for scenes that are read.
3. **Edges.** A picture that drifts ±A needs 2A of overscan: ±5% means the image is 110–112% of its frame.
4. **Layout breaks.** Never transform an ancestor of a `position: sticky` element, or of a fixed one (a transform
   makes it the containing block). Transforms only, so there is no CLS.
5. **Text in moving layers** reads badly and invites motion sickness, so text never moves.
6. **iOS.** `background-attachment: fixed` is ignored; the address bar resizes the viewport (use
   `ScrollTrigger.config({ ignoreMobileResize: true })` and `svh` units); momentum scroll plus transforms can jitter.
   Turn parallax off on touch, as Locomotive does.
7. **Too many moving layers** cost frames. At most 8 parallax elements in a viewport.
8. **CSS scroll-driven animations** (`animation-timeline: view()`) follow native scroll, which Lenis drives. They
   work, but unsmoothed, so keep them for small flourishes [catalog] technique 3.

### 5.5 Proposal for Kavalu

**Lenis** (one file, so the move to Lenis 2.0 stays a one-file change)

```js
new Lenis({
  lerp: 0.1,                  // 95% in 0.50 s, 99% in 0.77 s, at any refresh rate
  smoothWheel: true,
  wheelMultiplier: 1,         // never amplify the wheel: trackpads already send large deltas
  syncTouch: false,           // native momentum on phones and tablets
  touchMultiplier: 1,
  anchors: { offset: -76 },   // the 4.75rem header
  stopInertiaOnNavigate: true,
  autoRaf: false,             // the GSAP ticker drives Lenis (as now)
  // respectReducedMotion: true is the default: keep it
})
```

- **If the client wants it "smoother",** try 0.09 on a Mac trackpad *and* a Windows wheel mouse, which sends
  100 px steps and is where smoothing shows. Never go below 0.08.
- **Use `data-lenis-prevent`** on the drawer and any nested scroller, and call `lenis.stop()` while the drawer is
  open.

**Parallax map** (≥ 900 px, fine pointer, no reduced motion, no Save-Data)

| Where | Layer | Travel over one pass of the section at 1440×900 | How |
|---|---|---|---|
| Hero album page | Paper ground | 0 | — |
| | The centre stamp | 0. It anchors the composition, and the client's rule keeps the collage intact. | — |
| | Prints and the second stamp | −24 to −40 px | `y`, `scrub: true`, `ease: "none"` |
| | Ephemera: sticker, clip, tape, the hand note, the ಕವಲು card | −48 to −70 px | as above |
| Project spreads | Photographs inside frames | ±5% of the frame height (image 112% tall, offset −6%) | `yPercent` −5 → 5 |
| | Mounted prints and notes | ±24 px | `y` |
| Founder | The duotone portrait behind its paper frame | 30 px | `y` |
| Case studies | Full and wide images inside frames | ±5% | `yPercent` |
| | Pairs | The same direction, different amounts (12 and 24 px), never opposite | `y` |
| Footer | The wordmark arrival | As built | — |
| **Never** | Text, buttons, the logo, textures and backgrounds, pinned scenes, the work grid, forms, the desk (it has drag) | 0 | — |

- **Ceiling.** Nothing travels more than 80 px in one pass of its section, about 9% of a 900 px screen. Images
  move ±5% at most.
- **Direction.** Everything moves in the scroll's direction; only the amount differs.

---

## 6. Intros and preloaders

The brief: "like the hero section in this make a intro hero section -> https://www.nvmbr.in/ … make it sort of like
marvel intro theme, where all the photos are coming each ms and then they get zoomed out and then the name appears
and after that the current hero section."

### 6.1 What nvmbr.in actually does [CSS] [cap: nvmbr-in_0/1/2.jpg]

Read from its markup and inline CSS through the W3C validator on 24 Oct, so the structure is confirmed. The motion
was not watched.

1. **A white full-screen preloader.** `div#ga-preloader` is fixed at 100% height with an inline z-index of
   10000000000 and `background-color: white`. It holds `.ga-loader` (100vh, `overflow: hidden`, contents
   centred), which holds `.ga-loader-media` with an empty `<span>`. Scripts fill it at run time, so whatever the
   loader shows could not be read [unverified].
2. **A fixed full-screen reel.** `#fixed-banner { height: 100vh; position: fixed; top: 0; width: 100% }` holds
   `<video autoplay loop muted playsinline src="https://nvmbr.b-cdn.net/Home%20Page/Nov_Reel_10secs_RR.mp4">`
   with `object-fit: cover` and a "↓" (`#ga-arrow`, 1.5vw, 1.1vw from the bottom). By its file name, the reel is a
   10-second cut of their work.
3. **A white sheet that scrolls over the reel.** `.ga-index-split { background: #fff; border-radius: 1.6vw;
   margin-top: 100vh; padding: var(--main-gap) }` opens with the studio statement (h2, 65 px, weight 100, line
   height 120%), then rows of project tiles (two to four columns, `--col-gap: 1vw`). Its first tile, Designyatra
   2023, is an identity of "controlled, deliberate chaos" in many display typefaces. The captures, taken about a
   second apart, show three different typographic treatments in that tile.
   https://www.nvmbr.in/projects/designyatra-2023

**What the client saw**

- **The "every ms" feeling** is a rapid-cut reel of the studio's work, full screen, then the page arriving over it
  as a sheet.
- **The Marvel part** (the pull-back and the name) is the client's own addition.
- **November also shows** a live brand object: its NOVEMBER logo is a clock face whose hands move between
  captures.

### 6.2 What a "Marvel intro" is, structurally

| Version | What happens | Source |
|---|---|---|
| **2002** (Imaginary Forces) | A flipbook of comic pages, "to pay homage to the company's origins". | https://peoplesgdarchive.org/item/8177/marvel-intro-2000 [docs] |
| **2013** (Imaginary Forces) | Rebuilt "in 3D stereoscopic … combined with hundreds of images from the Marvel archives", keeping "the feel of the original flip book animation". | https://imaginaryforces.com/project/marvel-studios [docs] |
| **2016** (Perception) | A "vault": footage plays on the inside walls of the MARVEL letters; debuted at Comic-Con on 23 July 2016. | https://experienceperception.com/marvel-studios-rebrand.html [the page refused the connection; from a search summary] |
| **2025** (Imaginary Forces, *Thunderbolts\**) | Thousands of comic images projected onto a drifting 3D wordmark; the camera moves through each letter. | https://www.cgw.com/Press-Center/Web-Exclusives/2025/Imaginary-Forces-brings-iconic-Marvel-Studios-lo.aspx [from a search summary] |

The common grammar has four beats:

1. Images cut faster and faster.
2. They turn out to be *inside* something.
3. The camera pulls back to reveal that something.
4. The name resolves and holds.

No version publishes its frame counts.

### 6.3 Other studio intros worth knowing

| Intro | What happens | Timing, where known | Evidence |
|---|---|---|---|
| **Obys** https://obys.agency | On black: a small stack of greyscale project images (≈175×215 px at 1440×900, about 3% of the screen), a counter at the right edge (it read "76") and a 2.5 px top progress bar. It resolves into the home's vertical film strip with a bracket "viewfinder" that turns the framed image to colour. | Not readable. CSS: `#preloader` fixed at z 9996; `#prg` 2.5 px bar; `#preloader-prg` counter at 50% height with `mix-blend-mode: difference`. | [cap: obys-agency_0/1/2.jpg] [CSS] |
| **Codrops, Rapid Image Layers** (2020) https://tympanus.net/Development/RapidLayersAnimation/ | Full-screen image layers slide in one after another; each wrapper and its image move in opposite directions. The last slides out to reveal the page, and the content rises. | 1 s per layer, 0.15 s apart, `power2.inOut`. Last layer out over 1 s `expo.inOut`. Grid items 2 s `expo.out` from 100–500 px. With 5 layers, 3.6 s. | [src] https://github.com/codrops/RapidLayersAnimation |
| **Osmo, "Willem" loading animation** (by Dennis Snellenberg) https://www.osmo.supply/resource/willem-loading-animation | The name's letters rise; a box opens inside the name; three images inside it swap; the box expands to fill the screen; the header rises. | Letters 1.25 s `expo.inOut`, 0.025 s apart. Box 1.25 s. Image cuts every 0.5 s (0.05 s fades). Expansion 2 s `expo.inOut`. About 6.5 s in all. Scroll locked with `:has()`. No reduced-motion handling. | [docs] |
| **Mathijs Hanenkamp** https://mathijshanenkamp.com | A loader bar fills, the cover lifts, and the first photograph settles from scale 1.08 while the cover is still leaving: "the first photograph is already settling into place before the loader clears". | `expo.inOut`, 1 s. Hero image starts 0.15 s after the lift, text 0.2 s after, 0.05 s apart. | [docs] https://www.hontran.dev/blog/mathijs-hanenkamp-photography-portfolio-case-study |
| **Codrops, Image Stack Intro** (2020) https://tympanus.net/codrops/2020/11/24/image-stack-intro-animation/ | A stack of images moves into a row or a grid. | — | [from a search summary] |
| **Adovasio** https://adovasio.it · **Ana Blagojevic** https://anablagojevic.com · **Loftgarten** https://loftgarten.co | Photographic intros listed on Awwwards. Adovasio's markup shows a `HomeIntro` stack of pictures sized `25vw` (`20vw` on phones): a small central frame. | — | Adovasio [CSS]; the others [unverified] |

**The warning sign: these are now template products.** The Framer marketplace sells "Haytham Preloader" (name,
then images cycling inside the text, then a full-screen takeover), "Image GSAP Preloader", "Zoom Images Preload",
"Gallery Preloader", "Words Preloader" and "Greeting Loader". The "hello in many languages" loader is a commodity
too. Kavalu's intro is only not slop if it is specific: her stamp, her figure numbers, her lettering, and an
ending in her real hero.

### 6.4 The science and the safety

- **"Each ms" in practice.**
  - A browser paints once per display refresh: 16.7 ms at 60 Hz (`research/motion_frames/sites/NOTES.md`).
  - A one-frame image risks never painting when a frame is dropped. **Three frames (50 ms) is the practical
    floor.**
  - At 50 ms people still catch the gist of each picture. Potter, Wyble, Hagmann and McCourt found detection above
    chance at every duration from 13 to 80 ms, improving with duration (*Attention, Perception, &
    Psychophysics*, 2014) https://pubmed.ncbi.nlm.nih.gov/24374558/.
- **Flashing is the real constraint (WCAG 2.3.1, Level A).**
  - The rule: nothing may flash more than three times in a second unless it stays below the thresholds.
  - A *general flash* is "a pair of opposing changes in relative luminance of 10% or more of the maximum relative
    luminance (1.0) where the relative luminance of the darker image is below 0.80".
  - A *red flash* involves "saturated red", which means R/(R+G+B) ≥ 0.8 plus a chromaticity change of more than 0.2.
  - Small areas are safe: the threshold is a combined area of 341×256 CSS px (87,296 px²) per 10° of vision.
  - Sources: https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html and
    https://www.w3.org/TR/WCAG22/ [docs].
- **What that means for a full-colour montage.** It swings from near-black to bright paper with strong reds
  (Shoot stills, Not-So-Onam). At 20 cuts a second over an area larger than 341×256 px, it would fail.
- **How Kavalu makes it safe by construction.** Run the fast frames as **plum duotone** between deep plum
  `#270617` (L = 0.0062) and dusty plum `#7A4A5E` (L = 0.0984).
  - The largest possible change is 0.092 relative luminance, which is under 0.10. No pair of frames can ever be a
    general flash, at any size and any speed.
  - R/(R+G+B) is 0.57 and 0.42, which is under 0.8, so there is no red flash either.
  - The paper around the stamp never changes.
  - Only the last frame develops into full colour, and that is one change, not a flash.
  - Check a screen recording in Trace Center's PEAT before launch https://trace.umd.edu/?p=719. Its guide says it
    runs on Windows and Firefox; check the current version.
- **LCP.** web.dev: Chromium ignores "elements with an opacity of 0" and "elements that cover the full viewport".
  Size and position changes don't create new candidates [docs] https://web.dev/articles/lcp. So:
  - render the hero underneath at full opacity from the first paint;
  - never `opacity: 0` the hero while the intro plays;
  - let the intro's frames be what it is: a transform on the real stage.
  The target is LCP under 2.5 s at the 75th percentile.
- **Patience.** Nielsen: 1 s is "about the limit" for the user's flow of thought to stay uninterrupted; past 10 s
  you lose them [docs] https://www.nngroup.com/articles/response-times-3-important-limits/.
  - An intro is a deliberate break in the flow. It earns about 3 s on a first visit, and only if it can be skipped
    and nothing waits for the network.

### 6.5 First visit, skip and reduced motion

| Situation | Behaviour |
|---|---|
| First landing on `/` this session | Play. Keep the current `sessionStorage` flag; optionally also a `localStorage` date, so it replays only after 30 days. |
| Arriving through navigation inside the site, a deep link (`/#…`, `?road=`), or a back/forward cache restore | Skip |
| `prefers-reduced-motion: reduce` | No intro at all, as now. The montage is never shown. |
| `navigator.connection.saveData`, or an effective type of 2g or 3g | Skip: the montage needs 14 extra images |
| Any `pointerdown`, `keydown`, `wheel` or `touchstart`, or the "Skip intro" button | `tl.timeScale(8)`: the rest plays out in about 0.4 s. Never a hard cut, which would itself be a flash. |
| Images not decoded within 900 ms of `DOMContentLoaded` | Drop the montage and run only the pull-back and the name (1.6 s). Never wait on the network. |
| While it runs | The overlay parts are `aria-hidden`; `main` gets `aria-busy="true"`; the "Skip intro" button (Courier capitals, `--t-label`, a 44 px target, bottom right) is the only focusable thing; scroll is locked with `lenis.stop()` |

### 6.6 Kavalu's intro: the storyboard

**The idea:** a stamp album opened by a camera. Her prints cut inside the album's centre stamp: fast, plum,
cinematic. The camera pulls back, and the stamp turns out to sit in her album page, which is the hero. Her name
appears, then becomes the header logo, and the hero's headline rises.

There is no separate overlay full of copied images: the intro *is* the hero's album stage (`[data-stage]`), seen
through a camera.

**Set-up**

- The hero renders under everything from the first paint (it is the LCP).
- A cream paper veil, the same textured page, covers the left column (headline, body, buttons) and the header
  until the hand-off.
- The camera is a transform on the stage's *outer* wrapper. The pieces keep their tilts on their inner layer
  (`BRAND_DESIGN.md` §6.4), so the motion never fights the rest angles.
- All the collage pieces are present the whole time, just outside the frame at the start. That respects the
  client's rule that the collage keeps every photo.

**Desktop (≥ 900 px), at 60 Hz**

| t (s) | What you see | Motion | Easing |
|---|---|---|---|
| **0.00** | Cream paper fills the screen. At its centre, the perforated 4:5 stamp at 1.6× its hero size (roughly 60% of the screen height at 1440×900; measure it in the build), showing frame 1 in plum duotone. Below it, typed in Courier: "FIG. 03". Bottom right: "Skip intro". | Camera at scale 1.6, centred on the stamp | — |
| **0.00–1.23** | 14 of her prints cut inside the stamp, in plum duotone. They hold for 12, 10, 8, 7, 6, 5, 4, 4, 3, 3, 3, 3, 3 and 3 frames: 200 ms falling to 50 ms, 74 frames in all. The typed figure number changes with each cut (tabular figures, no shift). | The camera drifts 1.6 → 1.5, like a held camera breathing out | `power1.in`: it gathers speed with the cuts |
| **1.23** | The cuts stop on the hero's first project, still in duotone. The caption types its real label: "FIG. 06 · STUDIO ANOKHI". | — | — |
| **1.23–1.53** | **Develop:** the print turns from duotone to full colour. | A duotone copy on top fades from opacity 1 to 0 over 0.30 s | `power2.out` |
| **1.30–2.20** | **Pull back:** the album page comes into frame around the stamp: the second stamp, the अ stamp, the polaroid on its clip, the ಕವಲು card, the sticker, each at its tilt. | Stage scale 1.5 → 1 and translate to rest, 0.9 s. Ephemera add a 1.5° settle over 0.6 s. | `settle`, `cubic-bezier(0.16, 1, 0.3, 1)` |
| **1.90–2.48** | **The name:** her STUDIO / KAVALU lettering (the lockup's words, as SVG) appears in the left column where the headline will be, about as wide as the headline block, plum on paper. STUDIO comes first, KAVALU 0.08 s later; each rises out of a mask on its baseline. | `yPercent` 100 → 0, 0.5 s each | `expo.out` |
| **2.48–2.80** | Hold. Nothing moves. | — | — |
| **2.80–3.30** | **Hand-off:** the name shrinks and travels into the header, where it becomes the header lockup; the K mark fades in beside it as it lands. The veil over the left column lifts. Pointer input is live from here. | FLIP translate and scale, 0.5 s. Veil opacity 1 → 0 over 0.4 s. | `travel`, `cubic-bezier(0.65, 0, 0.35, 1)` |
| **2.90–4.00** | **The current hero takes over:** the headline lines rise out of their masks (the existing arrival, 1.1 s, 0.08 s apart), the body and buttons arrive at 3.2 s, the scribble under "road." draws, and her notes write themselves in. | Existing hero code | `settle` |

- **How long it takes.** The hero is usable at 2.8 s and fully settled at about 4.0 s. The last second is the
  hero's own arrival, which plays today anyway.
- **What it replaces.** The current intro (the road that draws, ಕವಲು, the sheet that lifts).
- **Why the figure number.** The typed figure number replaces a percentage counter, which the catalog's anti-list
  bans. It is Kavalu's own label (`FIG. NN`), and it is what a contact sheet would show.

**Phones and tablets (< 900 px)**

- The stamp starts at 1.5× its hero size.
- Ten cuts: 8, 7, 6, 5, 4, 4, 3, 3, 3 and 3 frames, 0.77 s in all.
- The pull-back runs from 1.5 to 1 over 0.8 s.
- The name appears centred under the stamp at about 78vw wide, then hands off to the header.
- About 2.6 s in all.

**Assets**

- 14 frames, pre-rendered at build time with `sharp` as plum duotone WebP: 640×800 px at quality 55, about
  35 KB each, about 0.5 MB in all.
- First visit only. Preload them with `fetchpriority="low"` after the hero's own images, and `decode()` them before
  starting.
- At 50–200 ms a frame, the slight softness at 1.5× on 2× screens is invisible.
- If fewer than 10 are ready by 900 ms, drop the montage (§6.5).

**What makes it not slop**

- It ends in the real hero instead of wiping away to reveal it.
- The images are her work.
- The counter is her own typed figure label.
- The name is her own lettering, which becomes the header logo.
- The montage is safe by design, not by luck.
- It plays once and can be skipped.

**Brand-book amendment needed**

- §3.6 says the lockup "never moves" and the wordmark appears "only" in the footer.
- The intro needs one exception: on the first visit, the lockup's words appear once, at rest, never tilted or
  distorted, and travel into the header.
- Ananya should approve this (§10).

---

## 7. Presenting the brand statement

"A brand is a set of choices; what it says, how it looks, where it shows up, who it speaks to." The client asked
to "remove this way of representing it", which is today's ink-in words and inline image pills, and to give it
"good animations with motion design … subtle not some slop".

### 7.1 How leading studios present a one-sentence belief

| Studio | Presentation | Motion | Evidence |
|---|---|---|---|
| **Collins** https://www.wearecollins.com | "Rewrite your worth.", one centred serif line, alone in the first view | None visible | [cap: wearecollins-com_0.jpg] |
| **Here** https://www.heredesign.com | "We design *brand ecosystems* with a *cultural purpose*.": centred, two italic phrases, under a film | None visible | [cap: heredesign-com_1.jpg] |
| **JKR** https://www.jkrglobal.com | A two-paragraph statement in large grotesk that "lights up" as you read. Read words are white; the next 2–3 words grade from mid-grey to near-black. | A scrubbed opacity per word. The CSS ships `text-white/10` to `/40` utilities, so unread words sit at about 1.3–2.5 : 1. | [cap: jkrglobal-com_1/2.jpg] [CSS] |
| **Pearlfisher** https://www.pearlfisher.com | A bold statement whose words turn from grey to white on scroll, with a grey paragraph under it | Scrubbed, per word | [cap: pearlfisher-com_1.jpg] |
| **Koto** https://koto.studio | A four-line paragraph: the claim in white, the context ("Find us in Los Angeles…") in grey | Static two-tone | [cap: koto-studio_1.jpg] |
| **Wolff Olins** https://www.wolffolins.com | "We create transformative brands that move businesses, people and the world forward.": a serif statement with three underlined key words and an inline "Our Ambition" label | Underlines; whether the words are links is [unverified]. Its CSS animates `text-decoration-color` over 0.15–0.5 s on links [CSS]. | [cap: wolffolins-com_1.jpg] |
| **Pentagram** https://www.pentagram.com | The sentence is the work filter: "We design [everything] for [everyone]", with 15 disciplines and 18 sectors as its two slots | The capture caught the discipline slot mid-roll ("Brand Strategy" rolling in); whether it rolls by itself is [unverified] | [cap: pentagram-com_0.jpg] [CSS: r.jina.ai render] |
| **Present** https://www.presentstudio.co | A serif statement beside "(Our Services)", a numbered list of services in italics | Static | [cap: presentstudio-co_0.jpg] |
| **Mythology** https://www.mythology.com | One word per screen: "WE" | A scroll sequence [unverified beyond the first word] | [cap: mythology-com_0.jpg] |
| **Heure Bleue** https://heurebleue.studio | "du beau et du bon": two lines of giant serif between films | — | [cap: heurebleue-studio_1.jpg] |

### 7.2 Tasteful against slop

**Tasteful (the research):**

- The sentence is given a whole view and stays still (Collins, Here, Heure Bleue, Mythology).
- Emphasis comes from one change (italic, a second tone, an underline), never three.
- The sentence *does* something: Pentagram's is the filter; Wolff Olins' key words carry the underline.
- Services sit beside the statement as a short numbered list (Present).
- Motion, if any, happens once and uses the brand's own gesture.

**Slop (now off the shelf):**

- **Words inking in from grey as you scroll.** This is today's Kavalu treatment. It is now a drop-in component:
  Framer's "Animated Text Reveal", "Text Reveal" and "TextFluxUnveil", and 21st.dev's "Scroll Reveal Text" ("Apple
  keynote-style … from dimmed and blurred to sharp").
- **Inline image pills inside a sentence.** This is the other half of today's treatment. Framer sells "Inline
  Images", "Inline Img with Text" and "Editorial Story".
- **Other tricks:**
  - per-letter splits;
  - blur-to-sharp on every word;
  - scramble or "decrypt" effects;
  - a rotating keyword typewriter ("we make [brands | feeds | films]");
  - the sentence on a marquee;
  - gradient or outline text.
- **Unread words below 3 : 1.** JKR's 10–40% greys, and today's 13% start (1.30 : 1), fall into this.

**Contrast floor for dimmed display text on cream** (plum, computed):

| Opacity | Contrast | |
|---|---|---|
| 100% | 14.91 | |
| 70% | 6.10 | |
| 60% | 4.44 | |
| 55% | 3.81 | |
| 50% | 3.28 | the lowest allowed |
| 45% | 2.83 | fails |
| 40% | 2.48 | fails |

Large text needs 3 : 1, so **50% is the lowest a dimmed word may go.**

### 7.3 Three proposals

The four clauses are the four roads: what it says → **Branding**, how it looks → **Visual identity**, where it
shows up → **Social media**, who it speaks to → **Film & photography** (`site.ts`). Each proposal makes that
mapping visible.

#### Proposal A: the sentence is the index (recommended)

**Layout**

- **A stage.** The section is `--stage` (100svh), with `--chapter-y` above it and nothing else in the first view
  except the typed eyebrow "THE HOUSE VIEW" (`--s-m` above the sentence).
- **The sentence.** It is set at `--d3` (84 px at 1440, 40 px at 360), measure about 30 ch, line height 1.04,
  tracking −0.022em, starting on column 2 of 12. Plum on the album page. It is never split, faded or moved.
- **Line breaks by design** (desktop), with `text-wrap: balance` as the fallback:
  ```
  A brand is a set of choices;
  what it says, how it looks,
  where it shows up,
  who it speaks to.
  ```
- **Clauses are links.** Each of the four clauses is a link, to its card in the Four roads section below, or to
  `/studio#road-0N` (Ananya's call).
- **Index numbers.** After each clause's last word, a typed superscript index ("01"–"04", Courier at
  `--t-label`, `--ink-faint`) works like a footnote mark and reflows with the text.
- **Roads under the clauses.**
  - Each clause has a hairline road under it: 1.25 px plum, round caps, with a ±0.6 px hand wobble.
  - Each road ends in the 9×6 px fork tick from the navigation.
  - The paths are built from the clause's `getClientRects()`, one per line box, and re-measured on resize and
    after fonts load.
- **Below the sentence,** at `--s-2xl`, the supporting copy ("Studio Kavalu is a branding and content house…")
  stays in two columns.
- **Merge with the roads.** The Four roads section loses its own heading and starts directly under this, as the
  sentence's continuation. One less title on the page is the spaciousness the client asked for.

**Motion** (once, when the sentence's top crosses 70% of the screen; `ScrollTrigger once: true`)

| Part | What | Timing | Easing |
|---|---|---|---|
| Roads | Draw under the four clauses in reading order | 0.7 s each, starting 0.22 s apart, 1.36 s in all | `power2.inOut` (the brand's line-drawing curve) |
| Fork ticks | Press on at the end of each road | Scale 0.6 → 1, 0.25 s | `back.out(1.6)` (paper pressed) |
| Index numbers | Type on with their road | 24 ms a character | — |
| Text | Never moves | — | — |

**Hover and focus** (`:focus-visible` matches every hover)

- **The active clause.** Its road thickens from 1.25 to 2 px and runs 24 px past the clause, where the service
  name types on in Courier capitals: "→ BRANDING" (18 ms a character).
- **The other three** dim to 50% opacity (3.28 : 1, the floor) over 240 ms `settle`, and come back in 180 ms.
- **One print in the margin.** A mounted print of that road's work appears in the right-hand column, outside the
  measure and never inside the text: taped, tilted −2°, rising 12 px with opacity, 420 ms `settle`. Moving to
  another clause swaps it with a 160 ms crossfade.
- **The cursor tag** reads "ROAD 02 · OPEN →" (§4.4).

**Touch, reduced motion and accessibility**

- **Touch.** There is no hover, so the service names show under each clause at all times (`--t-tiny`), and the
  four prints sit as a row of small stamps under the sentence.
- **Reduced motion.** Roads, ticks and numbers are drawn from the start; dimming has no transition; prints appear
  without movement.
- **Accessibility.** The sentence stays one `<h2>` in reading order. The links are inside it and keep their
  visible underline (the road). The SVG roads are `aria-hidden`.

**Why it's right**

- It is functional, like Pentagram's sentence.
- The type stays still, like Collins, Here and JKR at rest.
- Its motion is Kavalu's own Draw and Stamp, done once, with nothing looping.
- It respects the contrast floor, and it removes a section heading.

#### Proposal B: one choice at a time (pinned; uses the page's single pin)

**Where**

- Desktop at 1100 px and wider only.
- Pin with `start: "top top", end: "+=150%"`: 1.5 screens of scroll, inside the anti-list's limit of about two.
  `scrub: 0.3`, `anticipatePin: 1`.

**Layout**

- **Left (columns 1–7):** the whole sentence at `--d3`. The lead clause and the active clause are at 100%; the
  other clauses at 50%.
- **Right (columns 9–12):** one perforated stamp (4:5, about 30vh tall) with a typed caption: "ROAD 01 ·
  BRANDING · FIG. 03".
- **Left margin:** a vertical road (1.25 px) with a junction at each clause's baseline, and a small traveller dot
  that moves down the road with the scroll, echoing the onboarding's progress road.

**Timeline**

| Scroll progress | State |
|---|---|
| 0–0.08 | Lead-in: all four clauses at 50% |
| 0.08–0.30 | Clause 1 active |
| 0.30–0.52 | Clause 2 |
| 0.52–0.74 | Clause 3 |
| 0.74–0.92 | Clause 4 |
| 0.92–1.00 | All clauses return to 100%. The stamp fans into four small stamps (Flip, 0.6 s `settle`, played once, reversed on the way back up). |

**Motion**

- **Clause activation.** Opacity 0.5 ↔ 1, scrubbed over 4% of the progress, so the edges are soft and there is
  never a hard switch.
- **The stamp change is triggered, not scrubbed.** At each boundary (an index change in `onUpdate`): a 180 ms
  crossfade, the tilt goes from −2° to +1.5° (420 ms `settle`), and the caption retypes at 18 ms a character.

**Below 1100 px, reduced motion, and the risk**

- **Below 1100 px.** No pin. The four clauses stack, each followed by its small stamp at about 30vw. Static.
- **Reduced motion.** No pin; every clause at 100%; four stamps in a row.
- **The risk.** This takes the home page's only pinned scene. Scroll-linked dimming is a cousin of the
  commodity reveal, so it only stays tasteful while the 50% floor holds and the sentence is fully legible from
  the start.

#### Proposal C: the fork (the sentence drawn as a crossroads)

**Layout**

- **The stem.** The lead clause, "A brand is a set of choices;", sits at `--d3` on the left (columns 1–5),
  centred vertically.
- **The fork.** A road leaves its last word and forks into four branches across columns 6–12.
- **The branches.** At the end of each branch sits one clause at `--d5` (40 px), with its service typed under it
  in Courier capitals (`--t-label`):
  - "what it says, / BRANDING"
  - "how it looks, / VISUAL IDENTITY"
  - "where it shows up, / SOCIAL MEDIA"
  - "who it speaks to. / FILM & PHOTOGRAPHY"
- **Branch geometry.** Angles of 18° or less. Clauses stay horizontal. Branches are 22vw long or shorter, so
  reading doesn't stall.
- **Semantics.** One `<h2>` holds the sentence in order; grid placement does the layout; the SVG road is
  `aria-hidden`; the service names are a list of links to the roads.

**Motion** (once, at 70%; the section's one staggered list)

| Part | What | Timing | Easing |
|---|---|---|---|
| Stem | The road draws | 0.6 s | `power2.inOut` |
| Fork | Splits into four branches | 0.5 s each, 0.12 s apart | `power2.out` |
| Clauses | Each arrives along its branch: x from −16 px to 0, opacity 0 to 1 | 0.7 s, 0.12 s apart | `settle` |
| Service names | Type on after their clause | 18 ms a character | — |
| In all | | About 1.8 s | |

**Hover, below 900 px, reduced motion**

- **Hover.** The branch thickens, and a stamp of that service slides 24 px out from behind the clause like a pulled
  tab (420 ms `settle`).
- **Below 900 px.** The fork turns into a vertical road: the stem at the top, four stops down the page (like the
  process road). The road draws with the scroll (`scrub: 0.3`, the section's only scrub); clauses at `--d5`.
- **Reduced motion.** The fork is drawn and the clauses are at rest.

**Strength and risk**

- **Strength.** It makes the name visible (Kavalu is a crossroads, and the four roads leave one choice), and
  nothing like it appeared in the research.
- **Risk.** Splitting one sentence across five places slows reading on wide screens, so keep the branches short.

**Recommendation**

- **A by default.** It carries the least risk and also tidies the page.
- **C if Ananya wants the statement to be a signature moment.**
- **B only if no other pin remains on the home page.**
- **All three drop the ink-in and the pills.**

---

## 8. Responsive craft, 320–1920 px

### 8.1 What the measured sites do [CSS]

| Studio | Breakpoints | Margins | How type adapts | Above the design width |
|---|---|---|---|---|
| Here | 390, 712, 820, 1024, 1112, 1342, 1512 (set by the content) | 16 → 24 (≥ 820) → 32 (≥ 1512) | Stepped at 712 and 1112; h1 is fluid, `min(10vw, 148px)` | Capped at 1824 px |
| Koto | 834, 1194, 1440 | about 32 → 56 | Stepped only; no `clamp()` | **The root scales** with `html { font-size: .925926vw }` at ≥ 1728, so 1920+ screens get a proportionally larger layout. It stays zoom-safe, because zooming drops the CSS width below 1728. |
| Wolff Olins | 375, 400, 640, 768, 1024, 1280, 1536 | 24 → 32 (≥ 375) → 62 (≥ 1024) | Stepped (intro 35 → 45 → 55 → 64 px) | 80 px display only at ≥ 1536 |
| JKR | 640, 768, 1024, 1280, 1440 | — | Fluid, then fixed at 1440: h1 is `max(4.375rem, 10vw)`, then 9 rem. That makes 70 px on a 320 px phone, which is large. | Fixed |
| Present | 640, 768, 1024, 1400, 1536 | 20 px | Stepped at 640 and 768 | Container up to 1536 px |

**Patterns**

- Two layout breakpoints matter: about 768–834 and about 1024–1194.
- Type either steps at those or runs fluid with caps.
- Display sizes stop growing between 1440 and 1536.
- Containers cap between 1536 and 1824.
- Above the design width, Koto scales everything rather than leaving a sea of margin.

### 8.2 Rules

1. **Reflow at 320 CSS px with no sideways scroll** (WCAG 1.4.10). It is already a Kavalu rule; it is also what
   400% zoom on a 1280 px screen produces.
2. **Fluid type in `rem` plus `vw`, with the maximum at 2.5× the minimum or less** (§2.3). Never pure `vw`. Test
   at 200% and at 400% zoom.
3. **Phones.**
   - Body text at least 16 px.
   - Statements at 18–24 characters a line: the brand line at `--d3` 40 px runs about 5–6 lines at 360 px, which
     is fine.
   - Headings 4 lines at most.
4. **Targets at least 24×24 CSS px** (WCAG 2.5.8, AA). Kavalu's own floor stays at 40 px.
5. **Stage heights in `svh`** (Here uses `80svh`; Koto `100svh` and `100lvh`). Never `100vh` for a mobile hero: the
   address bar resizes it.
6. **Hover is an enhancement.**
   - Every hover effect sits behind `(hover: hover) and (pointer: fine)`.
   - Every hover-only piece of information also shows on touch: the service names in §7, the tags in §4.
7. **Art direction for images.** Use `<picture>` with portrait crops below 640 px, and exact `sizes` (Adovasio's
   intro uses `25vw` and `20vw` [CSS]).
8. **The hero collage keeps every piece at every width** (client rule). Below 900 px, scale it as one unit with
   container units (`cqw`), instead of moving pieces around. The composition then survives intact.
9. **Container queries for components that live at two sizes,** for example a road card in the grid and in the
   desk strip.
10. **Above 1680 px.** Either keep the centred `--max` (at 1920 that leaves margins of about 120 px, which is
    acceptable), or scale the root as Koto does. For Kavalu that would be `@media (min-width: 1680px) { html {
    font-size: calc(100vw / 105) } }`, which gives 18.3 px at 1920. Test both side by side. Zooming takes you
    back below 1680, so the scaling switches off.

### 8.3 Test matrix for Q22

| Check | Widths and conditions |
|---|---|
| Widths | 320, 360, 390, 414, 768, 834, 1024, 1280, 1440, 1680, 1920 |
| Zoom | 200% and 400% at 1280 px |
| Short laptop | 1280×720 |
| Orientation | Landscape phone (844×390) |
| Motion and data | Reduced motion; Save-Data |

At every width, record:

- sideways overflow (must be zero);
- the number of lines in each heading;
- the clutter audit from §1.6;
- the tap targets;
- that the intro and the statement still fit their stages.

---

## 9. Reference URLs to record frame by frame

For the persistent browser when it is free (Q15–Q17 and Q19), with `research/tools/motion_study.py`:

| # | URL | Record | Look for |
|---|---|---|---|
| 1 | https://www.nvmbr.in/ | Load, 0–4 s, then scroll for two screens | What `.ga-loader-media` shows; the reel's cut rate (frames a shot); how the white `ga-index-split` sheet (`margin-top: 100vh`, 1.6vw radius) rides over the fixed reel |
| 2 | https://obys.agency/ | Load, 0–6 s | How fast the image stack cuts in the small window; counter speed; how the stack turns into the film strip and the viewfinder; when colour appears |
| 3 | https://imaginaryforces.com/project/marvel-studios | Play the film | Frames per image at the start and at the fastest; when the pull-back starts against the cuts; how long the logo holds |
| 4 | https://tympanus.net/Development/RapidLayersAnimation/ | Trigger the reveal | The 0.15 s layer rhythm against the 1 s slides, as a baseline for "rapid" |
| 5 | https://www.osmo.supply/resource/willem-loading-animation (its demo) | Load | The box growing to fill the screen, which is the zoom we reverse; the 0.5 s image swaps |
| 6 | https://mathijshanenkamp.com/ | Load | The overlap: the hero photo settling from 1.08 while the cover is still lifting |
| 7 | https://www.jkrglobal.com/ | Scroll through the statement | How many words are mid-transition at once; the grey levels; how far the reveal lags the scroll |
| 8 | https://www.pearlfisher.com/ | Scroll through the statement | The grey-to-white per word, and where the reading edge sits on screen |
| 9 | https://www.wolffolins.com/ | Hover the underlined words | Whether they are links; the underline offset, thickness and colour change (0.15–0.5 s in its CSS) |
| 10 | https://www.pentagram.com/ | Load and leave it idle, then use the slots | Whether the discipline word rolls by itself; the slot animation's timing and easing |
| 11 | https://heurebleue.studio/ | Move the pointer over links and films | The dot riding beside the native cursor; the label's 5° → 0° straightening (0.3 s); its offset from the pointer |
| 12 | https://cuberto.com/ | Pointer over links, text and media | Dot sizes per state, the follow lag (0.55 s `expo.out`), the media box opening |
| 13 | https://dennissnellenberg.com/ | Hover the work list | The preview card's lag and scale-in, the "View" disc, other rows dimming, magnetic buttons |
| 14 | https://exoape.com/ | Pointer in the hero, then scroll | The "Scroll" cursor state; picture parallax inside frames (measure it in px) |
| 15 | https://perkybros.com/ | Pointer over the lead image | The "View Project" text cursor: its size, offset and fade |
| 16 | https://koto.studio/ | Load and scroll | The two-tone statement; the film hero; spacing between sections in px |
| 17 | https://www.heredesign.com/ | Scroll the home page | Measure the 8–12 rem rhythm and the 25vh gaps on screen; the italic statement under the film |
| 18 | https://marijanapav.com/stamps | Load and pointer | The paper texture at 100% zoom; handwriting stroke timing (250 ms a stroke); the typewriter cards |
| 19 | https://www.laxspace.co/ | Pointer movement | The tape trail, as the paper-native cursor idea (to judge, not to copy) |
| 20 | https://www.wearecollins.com/ | Load | How the single line arrives, if it does; how the first view is composed |

---

## 10. Edits to make in BRAND_DESIGN.md and kavalu_instructions.md

| Where | Now | Change to |
|---|---|---|
| `BRAND_DESIGN.md` §1.6, §9.8 | "no custom-cursor gimmicks", "Don't add custom cursors" | "A designed cursor system (§x): an ink dot and typed tags, on fine pointers only; never blend-mode blobs, trails or centred discs over the work." |
| §3.6 Logo motion | The lockup "never moves"; the wordmark only in the footer | Add the first-visit intro: the lockup's words appear once, at rest, never tilted, then travel into the header. *Needs Ananya's approval.* |
| §5.2 Scale | 10 display tokens | Six (`--d1`–`--d5`, `--h`) plus `--lead`; the rule "max ÷ min ≤ 2.5" |
| §6.2 Paper surfaces | grain multiply; worn texture | The material table (§3.5 here); the speck limits (6% under text, +6% on dark); textures baked into each surface, never a fixed blend overlay; no scanned folds or stains (Studio N°7's look) |
| §8.1 Tokens | margin, gutter, max, nav height | Add `--s-*`, `--section-y`, `--chapter-y`, `--stage`, `--measure-*` |
| §8.3 Rhythm | "about one screen of breathing room between chapters" | `--chapter-y` (about a quarter of the screen); full stages only for one-idea views; the clutter audit (§1.6 here) |
| §9.2 Tokens | durations and eases | Add the intro timings (§6.6), the parallax ceilings (80 px, ±5%), and Lenis lerp 0.1 = 95% in 0.50 s |
| §9.3 Vocabulary | Arrive … Morph | Add **Develop** (duotone to colour), **Pull back** (the camera zoom-out), **Point** (a cursor tag straightens and lands) |
| §9.8 Misuse | "preloaders that hold back the page (the intro is first visit only, under 1.7 s, and skippable)" | "The intro is first visit only, at most 3.3 s to a usable hero, skippable by any input, rendered over a hero that is already painted, and absent with reduced motion or Save-Data." |
| §12 Accessibility | — | Montage frames in plum duotone (ΔL < 0.10), checked with PEAT; dimmed display text never below 50% (3.28 : 1); the custom cursor removed under `forced-colors` and on touch input |
| `kavalu_instructions.md` §2 | — | Record the decisions and their reasons: duotone montage, the statement as index, cursor tags, spacing tokens |

---

## 11. Sources

**Studio sites, CSS and markup read on 24 Oct 2026**

- Here Design: https://www.heredesign.com · https://www.heredesign.com/_next/static/css/794a6149530b0d61.css
- Koto: https://koto.com · https://koto.studio · https://koto.com/_next/static/css/cfe6a2824bfb3a1e.css
- Wolff Olins: https://www.wolffolins.com · https://www.wolffolins.com/_next/static/css/def584e06038b3a0.css
- JKR: https://www.jkrglobal.com · https://www.jkrglobal.com/_next/static/immutable/chunks/3zs50k9eyiips.css
- Present: https://www.presentstudio.co · https://www.presentstudio.co/_next/static/css/8049368020bb61cf.css
- Collins: https://www.wearecollins.com
- November: https://www.nvmbr.in · https://www.nvmbr.in/projects/designyatra-2023 ·
  https://nvmbr.b-cdn.net/Home%20Page/Nov_Reel_10secs_RR.mp4
- Obys: https://obys.agency
- Heure Bleue: https://heurebleue.studio
- Working Stiff Films: https://stiff.madebybuzzworthy.com · https://stiff.madebybuzzworthy.com/css/styles.css
- Adovasio: https://adovasio.it
- Ana Blagojevic: https://anablagojevic.com
- Pentagram (sentence filter): https://www.pentagram.com
- How markup was read: the W3C Nu validator's source view (`https://validator.w3.org/nu/?doc=<url>&showsource=yes`)
  and https://r.jina.ai

**Seen in our 23 Oct captures** (`research/screens/`)

- Collins, JKR, Koto, Here, Perky Bros, Little Plains, Mythology, Heure Bleue, Pentagram, Present, DixonBaxi,
  Pearlfisher, Wolff Olins, Cuberto, Dennis Snellenberg, Exo Ape, Poch, Rejouice, 14islands, Immersive Garden,
  Obys, Working Stiff Films, Lynn Fisher, Studio N°7, nvmbr.in. The URLs are listed in `SOURCES.md` §2.

**Libraries and code**

- Lenis: https://github.com/darkroomengineering/lenis ·
  https://raw.githubusercontent.com/darkroomengineering/lenis/main/packages/core/src/animate.ts ·
  https://raw.githubusercontent.com/darkroomengineering/lenis/main/packages/core/src/maths.ts
- Darkroom satus: https://github.com/darkroomengineering/satus/blob/main/components/layout/lenis/index.tsx
- Locomotive Scroll v5: https://scroll.locomotive.ca/docs/ ·
  https://scroll.locomotive.ca/docs/documentation/options ·
  https://scroll.locomotive.ca/docs/documentation/attributes
- GSAP ScrollSmoother: https://gsap.com/docs/v3/Plugins/ScrollSmoother/
- Cuberto mouse-follower: https://github.com/Cuberto/mouse-follower ·
  https://raw.githubusercontent.com/Cuberto/mouse-follower/master/src/scss/index.scss
- Osmo:
  - https://www.osmo.supply/resource/velocity-based-custom-cursor
  - https://www.osmo.supply/resource/global-parallax-setup
  - https://www.osmo.supply/resource/lenis-smooth-scroll-setup
  - https://www.osmo.supply/resource/willem-loading-animation
- Codrops:
  - Rapid Layers https://github.com/codrops/RapidLayersAnimation ·
    https://tympanus.net/Development/RapidLayersAnimation/ ·
    https://tympanus.net/codrops/2020/04/07/rapid-image-layers-animation/
  - Image Stack Intro https://tympanus.net/codrops/2020/11/24/image-stack-intro-animation/
  - Intro Grid Motion https://github.com/codrops/IntroGridMotionTransition
- Digital Stamp Collection: https://marijanapav.com/stamps · https://github.com/buka-studio/www-marijanapav
  (`public/stamps/noise.svg`, `src/app/stamps/components/SVGFilters.tsx`)
- 14islands, custom cursor: https://v3.14islands.com/blog/developing-a-performant-custom-cursor
- Custom cursors in React: https://21st.dev/blog/custom-cursor-react
- CSSWG issue #9813 (top layer and element cursors):
  https://lists.w3.org/Archives/Public/public-css-archive/2024Jan/0474.html
- MDN `cursor`: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/cursor
- CSS-Tricks, grainy gradients: https://css-tricks.com/grainy-gradients/
- Mathijs Hanenkamp case study: https://www.hontran.dev/blog/mathijs-hanenkamp-photography-portfolio-case-study

**Standards and research**

- WCAG 2.2: https://www.w3.org/TR/WCAG22/
  - 2.3.1 https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html
  - 2.3.3 https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html
  - 1.4.8 https://www.w3.org/WAI/WCAG22/Understanding/visual-presentation.html
  - 1.4.10 https://www.w3.org/WAI/WCAG22/Understanding/reflow.html
  - 2.5.8 https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
- web.dev: LCP https://web.dev/articles/lcp · reduced motion https://web.dev/articles/prefers-reduced-motion
- Val Head, "Designing Safer Web Animation For Motion Sensitivity", A List Apart:
  https://alistapart.com/article/designing-safer-web-animation-for-motion-sensitivity/
- Jakob Nielsen, "Response Times: The 3 Important Limits":
  https://www.nngroup.com/articles/response-times-3-important-limits/
- Maxwell Barvian, "Addressing Accessibility Concerns With Using Fluid Type":
  https://www.smashingmagazine.com/2023/11/addressing-accessibility-concerns-fluid-type/
- Adrian Roselli, "Responsive Type and Zoom": https://adrianroselli.com/2019/12/responsive-type-and-zoom.html
- Utopia space calculator: https://utopia.fyi/space/calculator/
- Butterick, line length: https://practicaltypography.com/line-length.html
- Potter et al., "Detecting meaning in RSVP at 13 ms per picture" (2014): https://pubmed.ncbi.nlm.nih.gov/24374558/ ·
  https://dspace.mit.edu/handle/1721.1/107157
- PEAT (Trace Center): https://trace.umd.edu/?p=719
- Fixed backgrounds and scroll cost: https://fourkitchens.com/?p=1517 · https://bugs.webkit.org/show_bug.cgi?id=72078 ·
  https://discourse.webflow.com/t/bad-performance-scroll-animation-on-chrome/123601 ·
  https://greensock.com/forums/topic/33479-gsap-mixblendmode-chromeedge-vlow-framerate-on-all-animation/

**Marvel Studios logo**

- https://imaginaryforces.com/project/marvel-studios
- https://peoplesgdarchive.org/item/8177/marvel-intro-2000
- https://experienceperception.com/marvel-studios-rebrand.html (from a search summary; the page refused the
  connection)
- https://www.cgw.com/Press-Center/Web-Exclusives/2025/Imaginary-Forces-brings-iconic-Marvel-Studios-lo.aspx (from a
  search summary)

**Awwwards and commodity evidence**

- Awwwards cursor article: https://www.awwwards.com/customize-your-mouse-cursor-inspirational-examples-implementation-tricks.html
- Awwwards intro elements: https://www.awwwards.com/inspiration/photographic-loading-sequences ·
  https://www.awwwards.com/inspiration/preloader-intro-animation-portfolio-adovasio ·
  https://www.awwwards.com/inspiration/loftgarten-loading-intro
- Framer marketplace:
  - https://www.framer.com/marketplace/components/image-gsap-preloader/
  - https://www.framer.com/marketplace/components/zoom-images-preload/
  - https://www.framer.com/marketplace/components/haytham/
  - https://www.framer.com/marketplace/components/inline-images/
  - https://www.framer.com/marketplace/components/inline-img-with-text/
  - https://www.framer.com/marketplace/components/editorial-story/
  - https://www.framer.com/marketplace/components/animated-text-reveal/
  - https://www.framer.com/marketplace/components/words-preloader/
- 21st.dev: https://21st.dev/@dev.yadhakim/components/scroll-reveal-text.md
