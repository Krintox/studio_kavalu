# Studio Kavalu — brand design

**Version 1.0 · 24 October 2026**
**Owner:** Studio Kavalu (Ananya)
**Applies to:** the website in `website/` and anything made in its image
**Status:** describes the site as built, after the consistency pass (queue item Q9)

This is the design sense of Studio Kavalu written down: what the brand is, the rules that keep it
recognisable, and the reasons behind them. If something on the site disagrees with this document, the
site is wrong. If this document is wrong, change it first, then the site.

The client's standing rules, which outrank everything here, are in `kavalu_instructions.md`. The
research behind each decision is in `research/`, and its sources are listed in `research/SOURCES.md`.

---

## Contents

1. [The brand](#1-the-brand)
2. [Voice and words](#2-voice-and-words)
3. [Logo](#3-logo)
4. [Colour](#4-colour)
5. [Typography](#5-typography)
6. [The scrapbook kit](#6-the-scrapbook-kit)
7. [Imagery](#7-imagery)
8. [Layout and spacing](#8-layout-and-spacing)
9. [Motion](#9-motion)
10. [Components](#10-components)
11. [Onboarding](#11-onboarding)
12. [Accessibility](#12-accessibility)
13. [Beyond the website](#13-beyond-the-website)
14. [What is uniform everywhere: the checklist](#14-what-is-uniform-everywhere-the-checklist)
15. [Where each rule lives in the code](#15-where-each-rule-lives-in-the-code)
16. [How this document was made, and sources](#16-how-this-document-was-made-and-sources)
17. [Changelog](#17-changelog)

---

## 1. The brand

### 1.1 The name

**Kavalu (ಕವಲು)** is Kannada for a crossroads: *"a point where paths meet, split, and become something
new."* It is pronounced *ka·va·lu*. The studio is **Studio Kavalu**, founded and run by **Ananya** in
Bengaluru. The full name is "Studio Kavalu by Ananya", and in Kannada it is ಸ್ಟುಡಿಯೋ ಕವಲು.

### 1.2 The line

The brand line is fixed. Quote it exactly, punctuation included:

> A brand is a set of choices; what it says, how it looks, where it shows up, who it speaks to.
> Studio Kavalu is a branding and content house that makes these choices with you. We shape brands,
> feeds and persona through a design lens backed with strategy. The aim- work with a point of view
> clear enough that people recognise it, and others follow it.

Its first sentence names the four choices. They are the four roads, and they organise the whole site.

### 1.3 The four roads (services)

| Road | The question it answers | Service | Card paper |
|---|---|---|---|
| 01 | What it says | Branding | cream |
| 02 | How it looks | Visual identity | blue |
| 03 | Where it shows up | Social media | cream |
| 04 | Who it speaks to | Film & photography | blue |

The roads always appear in this order and with these names. "Not sure yet" is a fifth choice that
exists only in onboarding.

### 1.4 The idea: the crossroads album

The website is **a scrapbook, not a site with a scrapbook page**. Every project is a print or a stamp
in an album. Pictures are mounted with tape, photo corners or a paper clip; captions are typed on strips
of paper; Ananya's notes are in her hand; and the studio keeps a desk of things pinned above it, which
is the footer.

Two motifs carry the meaning:
- **The road and the fork.** A line that splits: under the active nav link, in the intro, in the
  four-roads map, the process line and the desk's pencil road.
- **Paper you could hold.** Nothing on the site is interface chrome for its own sake. If an element
  could not exist as a piece of paper, a stamp, a clip or a ticket, ask whether it should exist.

### 1.5 Attributes

| Attribute | Means | Does not mean |
|---|---|---|
| **Considered** | Every element is a choice: one emphasised phrase, one moving thing, one road at a time. | Minimal for its own sake, or empty. |
| **Tactile** | Paper, grain, tape, typed labels, a real hand. Things have weight and land. | Skeuomorphic gloss, fake 3D, textures on everything. |
| **Warm** | Bengaluru, a person who reads your brief, cream and oxblood, handwriting. | Cute, twee or casual about the work. |
| **Clear** | A point of view people recognise. Plain words, obvious next steps. | Clever copy, mystery navigation. |
| **Quiet** | Motion that is felt rather than watched; nothing loops for attention. | Static or lifeless. |

### 1.6 What Studio Kavalu is not

- **Not its friends' studios.** Studio Sorted (Bengaluru) and Studio N°7 share cream and serif, so
  Kavalu leans on what they don't have: the album system, Kannada identity, the four roads, the motion
  story, a grotesk where they set light serifs, and powder blue as the second paper.
- **Not "AI slop".** No purple gradients or gradient meshes, no glassmorphism, no identical fade-up on
  every block, no marquees, no cursor gimmicks (blend-mode blobs, trails, discs over the work; the
  designed cursor is §10.11), no words inking in from grey as you scroll, no pictures inlined in a
  sentence (both are now off-the-shelf components). No type chosen because it is the default:
  Inter, Fraunces, Instrument Serif, Playfair, Satoshi and Clash are out (`research/type/TYPE_REVIEW.md`).
- **Not a template.** No hero-plus-three-cards. Each page is a spread with its own composition.

---

## 2. Voice and words

### 2.1 Principles

1. **Speak as "we", to "you".** "We make these choices with you." Ananya speaks as "I" only when she
   signs something: the founder quote, a note, the letter in onboarding.
2. **Plain and specific.** Say what happens: "Five short steps, about three minutes, read by Ananya."
3. **Short sentences, one idea each.** A colon or semicolon is welcome where the brand line uses one.
4. **The crossroads metaphor, sparingly.** Roads, choices and paths are the brand's own language. Use
   it at most once per section, and never stretch it: no "journeys", no "destinations".
5. **Warm, not cute.** Exclamation marks are not used. Emoji are not used.

### 2.2 Words

| Use | Avoid |
|---|---|
| choose, choices, road(s), fork, crossroads | journey, destination, roadmap (as a buzzword) |
| make, shape, design, write, shoot | craft (as a verb for everything), curate, elevate |
| brand, identity, feed, persona, story | solutions, synergy, ecosystem, offerings |
| studio, house, desk, album | agency (Kavalu is a studio), team of passionate creatives |
| clear, recognisable, point of view | world-class, cutting-edge, next-level, seamless, unlock, bespoke |

### 2.3 Mechanics

- **Spelling:** British and Indian English: colour, recognise, organise, programme, centre.
- **Separators:** a spaced middle dot ( · ) between items in a line: "Pottery studio · Bengaluru ·
  2025".
- **Ranges:** an en dash with no spaces: "₹1–2.5 lakh", "1–3 months".
- **Currency:** "₹" with Indian units (lakh) for INR; "$" for USD. The rupee sign sets in Anek Kannada
  automatically (§5.6).
- **Time:** 24-hour, with the zone: "Bengaluru 14:32 IST". Dates: "24 Oct 2026"; on a postmark,
  "24 OCT 2026".
- **Numbers:** figures for counts and steps ("5 projects", "step 2 of 5"); two-digit numbering in
  lists and indexes ("01", "02").
- **Quotes:** curly quotes (" " ' '). Use the apostrophe ’ in running text.
- **Arrows:** "→" after a link that takes you somewhere ("Open the case study →"); "←" only for Back.

### 2.4 Microcopy patterns

| Kind | Pattern | Examples |
|---|---|---|
| Primary action | Verb + object | "Start a project", "Open the case study", "Pick a time for the intro call" |
| Link onward | Destination + → | "About the studio →", "All work (5) →" |
| Typed label | Short noun, capitals | CLIENT · YEAR · SERVICES, FIG. 01, ADMIT ONE |
| Typed caption | One sentence, sentence case | "Logo mark: from the pot to the letterform." |
| Hand note | Lower case, first person, under 12 words | "go on, move things around", "swipe along the desk →" |
| Errors | What happened + what to do | "Something went wrong sending this. Email the letter instead." |

### 2.5 Copy waiting for Ananya

Lines marked `// confirm` in `website/src/content/site.ts` are proposed wording, not her words: the
service lines, the process, her bio and the FAQ. Replace them with hers. Never present them as quotes.

---

## 3. Logo

### 3.1 Origin

The logo is **Ananya's own lettering**: the heavy, extended STUDIO / KAVALU of her current site, and a
K mark whose arm curves like a road. No font reproduces it. The best free match scored 0.80 IoU against
her letters, and Panchang was rejected as "really bad". So her letters were traced and refitted as clean
vector glyphs (A 0.994 IoU, S 0.974), with one shared cap line and baseline, identical A's and an
averaged U. Process and comparisons: `research/brand/wordmark_fit/`.

The glyphs are generated (`website/src/components/brand/wordmark-paths.ts`). **Never edit them by
hand, and never typeset the name in a font.** To change the logo, rerun `research/tools/wm_build.py`.

### 3.2 The three forms

| Form | What it is | Where |
|---|---|---|
| **Lockup** | The K mark beside STUDIO stacked over KAVALU | Site header; documents; anything that needs the name once |
| **Mark** | The K alone: a rounded square whose cream negative spaces draw the K | Favicon, avatar, the envelope stamp, very small spaces |
| **Wordmark** | STUDIO and KAVALU as two huge words, STUDIO from the left edge and KAVALU to the right | The end of every page (footer), and only there |

### 3.3 Construction

All measurements are in **c**, the cap height of the words in the lockup (`Wordmark.tsx`):

| Part | Value |
|---|---|
| Mark height | 2.91 c (mark aspect 100 : 112.26) |
| Gap between mark and words | 0.46 c |
| STUDIO top | 0.35 c below the top of the mark |
| Line gap between STUDIO and KAVALU | 0.19 c |
| KAVALU indent | 0.30 c, relative to STUDIO |
| Horizontal set of the words | 0.965 (the words are set 3.5% narrower than the footer wordmark) |
| Lockup aspect | 3.74 : 1 (1088.4 × 291 units) |

Counters are sub-paths drawn with `fill-rule: evenodd`, so the shapes stay true at any size.

**The footer wordmark.** STUDIO spans 89vw from 0.5vw; KAVALU spans 95vw and aligns right; the gap
between them is 1.1vw. The Kannada name ಸ್ಟುಡಿಯೋ ಕವಲು sits above STUDIO, its right edge on STUDIO's
right edge (on phones it sits below KAVALU, at the left margin).

### 3.4 Clear space and minimum size

- **Clear space:** keep at least **1 c** clear on every side of the lockup, and **0.25 × its height**
  around the mark alone. Nothing else may enter it, including tape, stickers and the edges of photos.
- **Minimum size:**
  - lockup **28 px tall** on screen (about 105 px wide), **10 mm** tall in print;
  - mark **16 px** (favicon), **6 mm** in print;
  - the footer wordmark only ever at full width.
- **In the header** the lockup is 2.3rem (36.8 px) tall.

### 3.5 Colourways

| On | Logo colour | Example |
|---|---|---|
| Cream | Plum `#390D26` | Header, documents (primary) |
| Deep plum / plum / oxblood | Cream `#F3F3E7` | Header over dark sections |
| Deep plum | Powder blue `#ABCDD6` | Footer wordmark |
| Powder blue | Deep plum `#270617` | Tickets, stickers |
| Favicon | Plum mark on a cream rounded square | `app/icon.svg` |

The logo is always one flat colour from the palette. On a photograph it needs a solid plate of
palette colour behind it.

### 3.6 Motion

The footer wordmark is the only logo that moves. As the footer arrives, STUDIO's letters come in from
the left and KAVALU's from the right, each letter travelling further the further out it sits, at 20%
opacity rising to full. They land exactly where they rest, scrubbed to the scroll
(`Footer.tsx`). With reduced motion the wordmark is simply there. The lockup and the mark never move,
tilt or animate.

### 3.7 Misuse

Don't:
1. typeset STUDIO KAVALU in any font as the logo (Panchang included), or retype it in the header or
   footer. The name as words, in running text or a typed label (a postmark, the drawer bar), is not the
   logo and is fine;
2. stretch, condense or skew the letters beyond the defined 0.965 set;
3. change the letter spacing or line gap, outside the footer arrival, which always ends at rest;
4. rearrange the mark and words, put the words beside each other on one line, or separate the K from
   the lockup in a new arrangement;
5. outline it, add shadows, gradients, textures or grain, or set it in a project colour;
6. tilt or rotate it. Paper tilts; the name never does;
7. place it on a busy photograph without a solid plate;
8. use it smaller than the minimum sizes above.

---

## 4. Colour

### 4.1 The palette (fixed)

These five colours were sampled from her existing site and are not to drift (client rule).

| Name | Hex | RGB | Token | Role |
|---|---|---|---|---|
| **Cream** | `#F3F3E7` | 243 243 231 | `--cream` | The paper. Default background; text on dark |
| **Plum** | `#390D26` | 57 13 38 | `--plum` | Ink. Headings, the logo, primary buttons |
| **Deep plum** | `#270617` | 39 6 23 | `--deep` | The dark sheet: footer, drawer bar, dark cards |
| **Oxblood** | `#491C17` | 73 28 23 | `--oxblood` | The warm dark: hover on buttons, folders, case-study accents |
| **Powder blue** | `#ABCDD6` | 171 205 214 | `--blue` | The second main colour (§4.5): the sheets laid on the desk, cards, the poster, buttons on dark, her pen mark on dark, the wordmark on the desk |

### 4.2 Supporting tones

Derived from the five, so everything stays in family:

| Token | Hex | Use |
|---|---|---|
| `--cream-2` | `#ECEADB` | A sheet laid on the cream; hover fills |
| `--cream-3` | `#E3E0CD` | Index card, mobile menu tab |
| `--blue-2` | `#C9DFE5` | Pale blue paper (service cards for identity and film, small stamps) |
| `--rust` | `#51201B` | Case-study text headings (the old site's rust) |
| `--ink` | `#241319` | Body text: plum-black, never pure black |
| `--ink-soft` | `#5D4A50` | Secondary text, labels |
| `--ink-faint` | `#6D5F62` | The lightest ink allowed for text: fig numbers, card labels |
| `--rule` / `--rule-strong` | plum at 16% / 32% | Hairlines, outlines of secondary buttons |

### 4.3 Paper and object colours

Real objects keep their real colours, which are not palette colours:

| Token | Hex | Object |
|---|---|---|
| `--paper` | `#FBFAF2` | Bright paper: prints, stamps, cards, strips, polaroids |
| `--paper-note` | `#F8F5E8` | Writing paper: notes, ruled sheets, the letter, service cards |
| `--placeholder` | `#D8D1C1` | The grey card behind an image while it loads |
| `--steel` | `#8D8A86` | Paper clips (highlight `#D7D5D0`) |
| `--corner` | `#24131A` | Photo corners |
| `--error` | `#A4201F` | Form errors only (wash `#FBEEE9`) |
| Kraft | `#EFE7D2`, `#F6EFDC`, `#EBE1C9` | The onboarding envelope |

### 4.4 Project colours

Each project has its own tones (`content/projects.ts`: `tone.bg`, `tone.ink`). They are its
**content**, like its photographs: they open its case study and its "next road" band, on cardstock
(`--tex-cardstock` in soft-light), with the project's ink at full strength for every line (some pairs
are only 5.1 : 1). They never leak into navigation, buttons outside the project, or another project.
The home page's spreads stand on powder blue; her prints carry the projects' colours there.

| Project | Background | Ink |
|---|---|---|
| Studio Anokhi | `#9F4A30` | `#FAEBCA` |
| Nivritti | `#07253D` | `#EFE9DA` |
| Not-So-Onam? | `#A11F5B` | `#F8E9EF` |
| I'm not getting the fillers yet | `#3F1B0E` | `#F6E7B6` |
| Shoot stills | `#A32D02` | `#FBE3D6` |

### 4.5 Weighting: light paper, plum as ink (brief 5)

**The rule (brief 5, replacing brief 4).** Plum (plum and deep plum) about **20%**; cream and powder
blue together **50–60%**; the remaining colours (oxblood, the projects' own colours, photographs) take
the rest. **The hero and the first sections open on light paper.**

**The arrangement.** Plum is the ink of the type, the pill buttons, one chapter and the footer's desk;
cream and powder blue are the paper:

| Ground | Where (`lib/surfaces.ts`) |
|---|---|
| **Cream** | The home hero, the house view (the torn sheet that slides over the spreads), the four roads, the work index, the case-study body, the studio's definition and questions, start, 404 |
| **Powder blue** | The project spreads (her prints on blue paper), choose your road (the cream letter on blue), the studio's roads and process |
| **Plum** | The album strip (her stamps glow on it), mid-page; the footer's desk (deep plum) |
| **Oxblood** | The founder (her blue poster on warm oxblood) |
| **The project's own colours** | Each case study's opening band and its "next road" band, on cardstock (§4.4) |

- A light opening: the first three chapters (hero, spreads, house view) carry no plum ground.
- After them the page alternates light and dark: cream, plum, cream, oxblood, blue, then the desk.
- Objects keep their papers; a blue sticker on a blue ground turns plum (`--blue-object`).
- The sheet mechanism (`SHEETS`, `[data-sheet]`) stays for any reading surface that needs one; none is
  used in this arrangement.

**Measured** (`research/tools/palette_lab.py`: every screen of home, work, studio and a case study;
0 text failures against WCAG AA):

| | Plum | Blue | Cream | Cream + blue | Oxblood | Photos and project colours |
|---|---|---|---|---|---|---|
| Desktop, 1440 × 900 | 20.8% | 25.4% | 36.5% | **61.9%** | 5.0% | 12.2% |
| Phone, 390 × 844 | 15.4% | 23.1% | 39.5% | **62.6%** | 4.5% | 17.4% |
| Home page alone, desktop | 19.2% | 32.4% | 30.2% | 62.6% | 5.9% | 12.3% |

**How it was chosen.** Brief 4's "desk" (one plum ground under blue sheets, 63% plum) was built, then
judged too plum. Six light arrangements were rendered on the real site and measured
(`research/palette_lab/`):

| Iteration | Plum | Cream + blue | Verdict |
|---|---|---|---|
| L1, cream hero, blue spreads, plum founder | 23.8% | 63.0% | Plum a little high |
| L2, blue hero, cream spreads, cream founder | 18.7% | 68.2% | Too little of anything but paper |
| L3, cream hero, a plum album, blue founder | 23.2% | 63.6% | The blue poster vanishes on blue |
| L4, as L1 with an oxblood founder | 18.6% | 63.0% | Close |
| L5, the roads on oxblood, the founder on cream | 18.6% | 61.0% | Close; two dark grounds back to back |
| **R2, a plum album strip, an oxblood founder** | **19.2%** | **62.6%** | **Chosen**: a light opening, then light and dark in turn |

### 4.6 Approved text pairs (WCAG 2.2)

| Text | On | Contrast | Use |
|---|---|---|---|
| Ink | Cream | 15.9 : 1 | Body |
| Plum | Cream | 14.9 : 1 | Headings, buttons |
| Oxblood | Cream | 12.9 : 1 | Hover, accents |
| Ink-soft | Cream | 7.3 : 1 | Secondary text, labels |
| Ink-faint | Cream / cream-3 | 5.4 / 4.6 : 1 | Small labels (AA) |
| Cream | Deep / plum / oxblood | 16.7 / 14.9 / 12.9 : 1 | Text on dark |
| Cream at 60% | Deep | 6.4 : 1 | Footer legal line (minimum opacity for text on dark) |
| Powder blue | Deep / plum / oxblood | 11.1 / 9.9 / 8.5 : 1 | Emphasis on dark |
| Deep / plum | Powder blue | 11.1 / 9.9 : 1 | Text on tickets, blue cards and blue grounds |
| `--blue-ink-soft` `#50334A` / `--blue-ink-faint` `#5E4A5E` | Powder blue | 6.5 / 4.7 : 1 | Secondary text and small labels on blue grounds |
| Cream at 78% / 62% | Plum | 9.0 / 6.0 : 1 | Secondary text and small labels on plum grounds |

### 4.7 Misuse

- **Powder blue is never text on cream** (1.5 : 1). On light, blue is a surface; it is text only on
  dark.
- **The dark tones are never text on each other.** Plum on deep is 1.1 : 1 and oxblood on plum is
  1.2 : 1. They stack as surfaces (the folder cascade) and carry cream or blue text.
- **A ground never takes a blend mode.** Each ground's paper has its colour baked in; a grain laid over
  plum in soft-light was tried and lifted it to a bright magenta.
- **Blue never vanishes into blue**: a blue object on a blue ground turns plum, or moves to plum.
- **No project colour as a ground** (§4.4).
- No new colours, no gradients between palette colours, no tints of the logo.
- No pure black (`#000`) or pure white (`#FFF`), for type or for paper.

---

## 5. Typography

### 5.1 The system

Re-chosen in v3 after the client's "this font is not good" (brief 3). A census of 195 studio sites
(`research/type/STUDIO_FONTS.md`), a guide to which kind of type suits which kind of company
(`research/type/FONT_GUIDE.md`) and a shortlist of three complete systems
(`research/type/KAVALU_FONT_SHORTLIST.md`) came first. Then all three were set in the real site,
side by side at 1440 and 390 px (`research/type/lab/`, `research/tools/type_lab.py`), and system A was
chosen:

| Role | Face | Why |
|---|---|---|
| Wordmark | **Her own lettering** (SVG) | It is the brand and the loudest letters on any page. Never a font. |
| Display and text | **Schibsted Grotesk** (Bakken & Bæck for Schibsted, SIL OFL), variable 400–900 with italics | One grotesk does every reading job, as most strong studios do (83% load a sans; 82% load one or two families). It agrees with the wordmark's monoline structure and contrasts with it in width and weight only, so the logo stays loudest. Its lightest weight is 400, so headings can't go fragile on the textures. It carries ₹. It is on none of the generated-site default lists |
| Typed paper | **Courier Prime** (OFL) | Only where the album has typed paper: captions, tickets, postmarks, footnotes, stamps' figure labels, the cursor's tags. Never the interface |
| Notes and signature | **Her own hand**, as SVG (pending: scans of her notes and signature). Until then, **Homemade Apple** and **Mrs Saint Delafield** stand in | A font repeats identical letters; her hand is the brand's one irregular voice |
| Kannada | **Anek Kannada** (Ek Type, Mumbai), with its width axis | Kannada words, matched to the grotesk by eye |

Gambetta, Switzer and the italic-word formula were dropped. A light serif headline with one italic
word, mono eyebrows over every heading, and a cream ground is now a recognised mark of a generated page
(Anthropic's own frontend-design guidance lists each of these). It is also her friend's studio's look
(cream with a light serif).

### 5.2 The scale

Six display steps (research/DESIGN_PRINCIPLES_v3.md §2.4). Each is linear from 360 to 1440 px and
capped, and never grows more than 2.5× from phone to desktop, so browser zoom always enlarges it
(WCAG 1.4.4). D3–D5 sit 6% under the research's values for Schibsted's larger x-height.

| Token | At 1440 / 360 px | Weight | Tracking | Role (old token names point here) |
|---|---|---|---|---|
| `--d1` | 160 / 64 | 500 | −0.04em | The case-study title (`--t-mega`) |
| `--d2` | 112 / 52 | 500 | −0.03em | Page titles, a project spread's title (`--t-1`, `--t-spread`) |
| `--d3` | 79 / 38 | 500 | −0.025em | The home headline, the house view (`--t-hero`, `--t-manifesto`) |
| `--d4` | 56 / 30 | 500 | −0.02em | Section titles, the founder quote (`--t-2`, `--t-quote`) |
| `--d5` | 38 / 24 | 600 | −0.01em | Headings on a sheet, sub-sections, quotes (`--t-sheet`, `--t-3`) |
| `--h` | 28 / 22 | 600 | −0.005em | Card titles (`--t-4`) |
| `--lead` | 22 / 18 | 400 | 0 | Lead paragraphs |
| `--t-body` | 18 / 16 | 400 | 0 | Body, line height 1.55 |
| `--t-small` | 14 | 500 | 0.01em | Interface text, labels, eyebrows |
| `--t-label`, `--t-tiny` | 11 / 10 | 400 | +0.08em (capitals) | Typed paper only |

A page uses at most three display steps. Weights and tracking are tokens (`--w-display`,
`--w-display-small`, `--track-d1` … `--track-h`), so every heading of one step is set alike.

### 5.3 Setting

- **Sentence case** for every heading; never display in capitals, never bold a display line.
- **Display tight, text open**: display line height 0.9–1.05, body 1.55 (WCAG 1.4.8 asks 1.5).
- **Labels** in the grotesk at 13–14 px, weight 500, sentence case: the clock, the scroll cue, the spread
  heads, the case-study meta, the work index, the footer line.
- **Eyebrows only where a heading needs one** ("The house view", "What we do", "Meet the founder"), never
  over every heading.
- **Typed capitals** (Courier Prime, +0.08em) only on paper: captions under prints, tickets, postmarks,
  card labels, the house view's footnotes.

### 5.4 Emphasis

**No italic or coloured word in a heading.** Headings are set in one weight and one colour. Emphasis,
at most once a page, is her own hand mark: the pen stroke under "road." in the hero, in oxblood on light
paper and powder blue on plum. The `<em>` in a heading renders plain (`base.css`).

### 5.5 Hand, signature and labels

- **Hand notes** are her notes and hints only, at most about 12 words, never interface text.
- **The signature** is "Ananya" and the sticker's "by Ananya", nothing else.
- **Ring text** on stickers and postmarks is sized to fit its circle (sticker 14.5 units with 2 units
  spacing, which runs 461 of the ring's 465; postmarks 9.4–9.5 px), so the line closes on itself.

### 5.6 Kannada and the rupee

Kannada is set in Anek Kannada with `lang="kn"`; Anek follows the grotesk in every stack. Schibsted
carries the ₹ itself. The studio's Kannada moments: ಕವಲು as a word (Studio page, intro, desk), ಸ್ಟುಡಿಯೋ
ಕವಲು beside the wordmark, and "Admit one · ಕವಲು" on the ticket. Kannada is never split into letters for
animation (§9.4).

### 5.7 Misuse

- No serif display; no italic or coloured word in a heading; no eyebrow over every heading.
- No more than the grotesk, the typed paper and the hand in one composition, plus the wordmark.
- No faux bold or italic; only the styles that are loaded.
- No typewriter on the desk or in the interface; no mono paragraphs; no hand lettering in the interface.
- Arrows (→ ←) come from the system font: Schibsted has no left or right arrows. Don't fake them.

### 5.8 Licences

Schibsted Grotesk, Anek Kannada, Homemade Apple and Mrs Saint Delafield come from Google Fonts through
`next/font/google` (SIL OFL), self-hosted at build time. Courier Prime is self-hosted under the SIL
OFL with its licence beside it. No Fontshare (FFL) font remains. See `website/src/fonts/LICENSE-fonts.md`.

---

## 6. The scrapbook kit

### 6.1 Principles

1. **Every piece is something you could hold.** Paper, stamps, tape, clips, tickets, envelopes.
2. **One mount per picture.** Tape, photo corners or a clip, never two kinds on one print.
3. **Paper tilts, a little, and differently.** Tilts come from short fixed lists so neighbours never
   match (§6.4). Pieces straighten when you point at them.
4. **Real objects keep real colours** (§4.3); paper is never pure white.
5. **Pieces land.** They arrive like something set down, and settle (§9).

### 6.2 The pieces

| Piece | Recipe | Where |
|---|---|---|
| **Paper surfaces** | Every ground is a sheet with its colour baked in (`--tex-cream`, `--tex-blue`, `--tex-plum`, `--tex-deep`, `--tex-oxblood`; `research/textures_v3`), one texture pixel per device pixel (`--tex-size`: 1024 px, 512 px on retina; the 512 tiles on phones), pinned to the page so one ground is one sheet. No blend mode on baked papers; `--tex-cardstock` with soft-light over any other colour | Every section, the intro, the desk, the folders |
| **Torn edge** | Mask `torn-top.svg` | Top of the manifesto sheet |
| **Ruled paper** | `--paper-note` with blue rules every 1.75–2.1rem; a red margin rule on the writing sheet | Choose your road, the letter, the contact card |
| **Perforated stamp** | Radial-gradient mask: perforation radius `--r` (3–7 px), offset −1.5r, tiled every 3r, solid centre inset 3r; `--paper` border; 4:5 window | Every project stamp (hero, album, work, spreads, case studies, desk) |
| **Polaroid** | `--paper`, 9 px border with a 2.2rem bottom; square window | Hero, spreads |
| **Tape** | Powder blue at 66% (cream tape at 62% on dark spreads), about 5 × 1.4rem, −5° to 4°, top −0.7rem | Mounted prints, notes, the definition card |
| **Photo corners** | `--corner`, 1–1.6rem triangles | Case-study prints, desk pieces |
| **Paper clip** | SVG in `--steel`, −6° to −9°, near one top corner | Polaroids, overview card, prints |
| **Map pin** | Red radial head, 0.95rem | Desk pieces (kit) |
| **Typed strip** | `--paper`, Courier Prime, small shadow, −1° | Captions under prints |
| **Hand note** | `--paper-note` (or blue or plum paper), Homemade Apple, tilted | Desk, case studies, hero |
| **Ticket** | Powder blue, a perforated stub on the left, a punched hole | "Start a project" on the desk |
| **Index card** | `--cream-3` with a folder tab | The desk's site index |
| **Postmark** | Two rings (r 54 / 32–33), mono ring text, multiply, −12° to −14° | The contact card, the envelope |
| **Sticker** | Round, ring text in mono, centre text in her signature ("by Ananya") | Hero, desk |
| **Folder tabs** | A tab with inverted corners on a coloured sheet; the cascade overlaps by 0.2rem | Footer (Home plum, Work oxblood, Studio blue, Start deep); mobile menu |
| **Envelope** | Kraft paper, a flap, a plum stamp with the K mark and the reference | Onboarding success |
| **The road** | A 1.1–1.5 px line that splits into a fork; dotted (1.5 6.5) on the desk | Intro, nav underline, four roads, process, desk |
| **Duotone** | `#duo-plum` filter: greyscale, deep shadows to blue highlights | Founder portrait |

### 6.3 Shadows

| Token | Use |
|---|---|
| `--shadow-paper` | Paper at rest on cream: prints, cards, notes, chips |
| `--shadow-lift` | Paper raised: a card on hover, the writing sheet, the overview card |
| `--shadow-desk` | Paper on the deep desk or dark spreads (a darker base, because plum shadows vanish on plum) |
| `--shadow-stamp` / `--shadow-stamp-dark` | The drop-shadow filter for perforated stamps (masked shapes need `filter: drop-shadow`), on light / on dark |

All shadows are cast in deep plum (`rgb(39 6 23)`) on light surfaces, and near-black (`rgb(10 2 6)`) on
dark ones. There are no other shadow colours.

### 6.4 Tilts

| Kind | Range | Behaviour |
|---|---|---|
| Large sheets (writing sheet, overview card, founder panel, letter) | −2° to 1.2° | Fixed |
| Grid items (album, roads, work, palette chips, prints) | −2.6° to 2.6°, from fixed lists | Straighten to 0° on hover or focus |
| Collage pieces (hero, spreads, desk) | −9° to 12° | Desk pins ease to 30% on hover, 50% on phones |
| Accents (clips, tape, notes, postmarks, signature) | −14° to 6° | Fixed |

Tilt sits on an inner layer (`rotate: var(--tilt)`); motion moves an outer one. So a piece can land,
be dragged and lean without its rest angle drifting.

### 6.5 Misuse

- Don't tilt type blocks, buttons or the logo.
- Don't stack mounts (tape and a clip) on one print, or put tape over a face in a photo.
- Don't use the kit as decoration around content that isn't her work or her words.
- Don't invent new pieces in another style (sticky notes in neon, washi with patterns, emoji stickers).

---

## 7. Imagery

1. **Only her work.** The site shows Ananya's projects, her palettes and her words. The reference images
   the brief came with are inspiration, never content (client rule).
2. **Mounted or full-bleed.**
   - Prints are mounted on paper, with one mount and a slight tilt.
   - A real photograph can run full-bleed, straight, with no border.
   - Never a bordered print that is also full-bleed.
3. **Captions** are typed strips below the print: one sentence, which types on as it arrives.
4. **Proportions:** stamps 4:5, polaroids square, prints as shot. Never crop a logo or a face.
5. **Portraits of Ananya** use the plum duotone.
6. **High quality, and the same picture.** The site's images began as low-resolution crops of the old
   site. Each is being regenerated at high quality as **the same image, never a different one**
   (brief 3): ChatGPT image generation, or an HTML recreation for flat graphics. Each is checked against
   its source, downscaled to the source's size, for framing, text, logos and faces
   (`research/images_hq/MANIFEST.md`). An output that changes anything is rejected; the Nivritti bottle
   was rejected for changing its label. Faithful ones are marked `hq` in `content/image-meta.json`,
   which turns off `placeholder`; for a cover, the full-bleed reveal then switches on by itself.
   Ananya's originals, when they arrive, replace either kind in `public/work/` under the same names.
7. **Alt text** describes what is in the picture and why it matters ("The Studio Anokhi mark on an
   ochre card"), never "image of".
8. **Art direction for new shoots:** warm light, real materials (clay, paper, fabric), hands at work, the
   brand in its place. Avoid stock, staged laptops and flat lays with props from nowhere.

---

## 8. Layout and spacing

### 8.1 Tokens

| Token | Value | Use |
|---|---|---|
| `--margin` | `clamp(1rem, −0.2rem + 4.2vw, 4.5rem)` | Page side margin |
| `--gutter` | `clamp(1rem, 0.55rem + 2vw, 2.25rem)` | Space between columns |
| `--max` | 1680 px | Widest content |
| `--nav-h` | 4.75rem | Header height |

**The ladder** (research/DESIGN_PRINCIPLES_v3.md §1.5): few steps, far apart, fluid from 360 to 1440 px.

| Token | 360 / 1440 px | Use |
|---|---|---|
| `--s-3xs` | 4 | Hairline gaps, icon to text |
| `--s-2xs` | 8 | Label to value, chip padding |
| `--s-xs` | 12 | Caption to print |
| `--s-s` | 16 / 20 | Lines in a group; pill gaps |
| `--s-m` | 20 / 32 | Label to title |
| `--s-l` | 32 / 56 | Title to body; body to actions; a sheet's side padding |
| `--s-xl` | 48 / 88 | Between blocks in a section; between case-study sheets |
| `--s-2xl` | 64 / 128 | A statement to its supporting copy; a sheet's top padding |
| `--section-y` | 80 / 158 (at 1440 × 900) | The top and bottom of every section |
| `--chapter-y` | 112 / 246 (at 1440 × 900) | Where the page changes chapter (the house view after the spreads) |

`--section-y` and `--chapter-y` follow the screen's height as well as its width
(`min(14vh, 9vw)`), so a short wide laptop never gets a phone's gaps and a tall phone never gets a
desktop's. Measures: `--measure-body` 62ch, `--measure-lead` 36ch, `--measure-caption` 44ch.

### 8.2 Breakpoints

There are three layout breakpoints, always written as `max-width` one pixel below the round number:

| Below | What changes |
|---|---|
| **1100 px** (`max-width: 1099px`) | The desk becomes stacked cards and a swipe strip; drag and parallax stop; road cards go to 2 columns |
| **900 px** (`max-width: 899px`) | The phone and tablet layout: menu button, no pinned scroll scenes, spreads become swipe rows, footer stacks |
| **640 px** (`max-width: 639px`) | One column: road cards, the work grid, the desk |

Components may add their own breakpoint when their content needs it (work grid 1200, onboarding page
960, chips 560). They do not move the page layout.

### 8.3 Rhythm

How the measured studios make space (Here, JKR, Koto, Wolff Olins, Present, Collins, November; their
own stylesheets, in `research/DESIGN_PRINCIPLES_v3.md` §1):

1. **Space is vertical.** Side margins stay modest (24–62 px). The air goes between blocks: 128–256 px on
   desktop, about a quarter of the screen's height.
2. **A short ladder.** A few spacing steps, far apart, read as calm; many close steps read as fussy.
3. **The proximity ladder.** Label to title < title to body < body to actions, all much smaller than the
   gap between sections.
4. **One idea per view.** One focal thing, at most two supporting ones (a label, an action), nothing
   moving on its own except the focal thing.
5. **Asymmetry makes space without emptiness.** Content starts on column 2–4 of 12 and leaves a quiet
   side.
6. **Small chrome.** Navigation, labels and clocks at 11–14 px; the room they don't take goes to the work.

**The clutter audit.** Every section is checked at 1440 × 900 and 390 × 844. A section that fails two of
these is cluttered, however it looks on its own:

| In one view | Limit |
|---|---|
| Focal elements | 1 |
| Supporting elements (label, action, caption) | 2 |
| Type sizes | 3 (an eyebrow, one display step, body) |
| Things moving on their own | 1, and pausable |
| Ephemera (tape, clips, stickers, notes) outside the hero collage and the footer desk | 2 |
| Lines in a heading | 4 |
| Buttons side by side | 2 |

- Sections are generous: a full screen is kept only for one-idea views (the intro, the statement, the
  first view of a case study); between other chapters the gap is about a quarter of the screen.
- A section opens with its display title; a small label sits above it only where the title needs one.
- The page is a spread: compositions are asymmetric, and type and pictures overlap a little where
  paper would.
- Pages end in the same place: the folder cascade, the desk and the wordmark.

### 8.4 Page anatomy

| Page | Structure |
|---|---|
| **Home** | Intro (first visit) → Hero (album page with the flip-book stamp) → two project spreads → manifesto sheet → the album row → four roads → founder → choose your road → footer |
| **Work** | Eyebrow "The album · NN projects" → title → filter by road → stamps grid or index table → footer |
| **Case study** | Hero in the project's colours (title, client / year / sector / services, cover) → overview card → blocks (text, image, pair, stamps, palette, note, quote) → "Building something that needs …?" → next road → footer |
| **Studio** | The dictionary entry for ಕವಲು → the four roads on oxblood → process road → founder → FAQ → choose your road → footer |
| **Start** | The onboarding form full page (also a drawer from anywhere) |
| **404** | "This road isn't on the map." with three ways back |

---

## 9. Motion

### 9.1 Principles

1. **Paper physics.** Things are set down, lifted, pressed, written and typed. They don't bounce,
   wobble or float. Bounce (a little overshoot) is allowed only for paper being pressed or dropped:
   a stamp, a postmark, a fork dot.
2. **Once.** Arrivals play once, the first time something comes into view. Reading back up doesn't
   replay them.
3. **One moving thing per screen.** At most one thing moves on its own, and it can be paused. The one
   exception is the hero, where the flip-book has a faint reel behind it (§9.4b): the reel is at 9%
   opacity, changes every 3.4 s, and the same pause button stops both (WCAG 2.2.2).
4. **Scroll is the reader's.** Scenes follow the scroll (scrubbed); the page never takes the scroll away.
   Lenis smooths the wheel, touch stays native, and there is at most one pinned scene per page.
5. **Felt, not watched.** If a motion asks to be noticed, it is too much.

### 9.2 Tokens

| Token | Value | Use |
|---|---|---|
| `--d-quick` | 180 ms | Press, colour and fill changes |
| `--d-base` | 420 ms | Lifts, tab nudges, gap changes, small moves |
| `--d-move` | 560 ms | A sheet sliding in (drawer, menu, a form step, page enter) |
| `--d-slow` | 900 ms | Arrivals of paper; image settles (also the GSAP default, 0.9 s) |
| `--e-settle` / `"settle"` | `cubic-bezier(0.16, 1, 0.3, 1)` | Arriving and lifting: things set down |
| `--e-travel` / `"travel"` | `cubic-bezier(0.65, 0, 0.35, 1)` | Moving between states, leaving, wipes |
| `--e-quick` | `cubic-bezier(0.2, 0.8, 0.2, 1)` | Presses |

Other curves, each with one job:
- `none` (linear) for anything scrubbed to the scroll;
- `power2.inOut` for lines being drawn;
- `power1.inOut` for handwriting;
- `back.out(1.4–2)` for paper pressed or dropped.

This is the same split Carbon calls productive (quick, settle) and expressive (travel, slow).

### 9.3 The vocabulary

| Verb | What happens | Where |
|---|---|---|
| **Arrive** | From a little below, slightly turned and transparent, to rest (`settle`, 0.9–1.25 s) | Hero pieces, road cards, album stamps, desk pins |
| **Lift** | Straighten to 0° and rise 6–8 px, deeper shadow (`--d-base`, settle) | Stamps, cards, tabs on hover or focus |
| **Press** | Scale to 0.97 on press (`--d-quick`, quick) | Every pill button |
| **Deal** | A pile of pictures travels to its places, scrubbed | Project spreads |
| **Uncover** | A clip-path opens from an inset frame | Case-study pictures, the hero plate |
| **Draw** | A line draws along its length | Intro road, scribble under "road.", the roads map (scrubbed while it rises through the lower half of the screen, done before the cards land), process, desk road, the house view's roads (once, in reading order, 0.7 s each, 0.22 s apart) |
| **Write** | A hand note writes itself in, word by word at pen speed; an arrow is the last stroke | Desk notes, the desk hint, case-study notes, hero notes (first visit) |
| **Type** | A typed caption types on, 24 ms a letter | Case-study captions |
| **Stamp** | A stamp or postmark presses on with a little overshoot | Desk postmark, envelope stamp and postmark |
| **Arrive at rest** | Letters close in from both sides and land, played once when the mark is well in view (its top at 72% of the screen; 1.5 s, settle). Scrubbed, it finished while only the mark's top edge was on screen, so nobody saw it | Footer wordmark |
| **Morph** | A stamp becomes the case-study cover between pages | Work → case study, next road |
| **Develop** | A picture printed in plum duotone comes up into its own colours, once, gradually | The intro's last frame |
| **Point** | A typed paper tag lands beside the pointer, straightening from −4° to 0° (300 ms, settle) | The cursor's "OPEN →" and "← DRAG →" |
| **Drift (parallax)** | The depth system (`lib/parallax.ts`, brief 6). Scrubbed to the scroll with a 0.8 s lag on top of Lenis, transforms only, every mover on its own compositor layer (on a phone only while it is on screen), off with reduced motion. Below 900 px every distance is halved, the album keeps still (a phone's strip shows two stamps at a time) and one-column rows don't stagger. **Media:** a picture sits 1.14–1.16× its window and travels 6–7% through it. **Layer:** a block drifts against the scroll at its own depth: the house view 26 px, the roads' heading 28, the letter 34, the founder's poster 64 and her quote 18. **Stagger:** neighbours in a row move at alternating speeds: the roads' four cards (46 px), the album's stamps (22), the work grid (40). **Spreads:** while a spread holds the screen its prints drift 36–130 px at their own depths and its words 34 px. **Footer:** the folders are laid down one on another (26 px apart, closing as the footer comes up) | Every page |

### 9.4 Rules for each kind

- **Arrivals** use at most three recipes, and there is one staggered list per view. Body text is
  simply there; it is never faded in.
- **Write and type** run once, put the original markup back when finished, and never split Kannada
  (shaped clusters). They are used only on her notes and typed captions, never on headings or body.
- **Hover** effects only on devices that hover; a focus state matches every hover state.
- **Page transitions** (View Transitions): the old page lifts away in 200 ms, the new one settles in over
  560 ms after 140 ms, the header never moves, and a stamp on both pages morphs (620 ms).

### 9.4b The intro (every load of the home page)

A studio ident before the hero, modelled on nvmbr.in's montage (recorded frame by frame in
`research/motion_frames/intros/`), and since brief 6 on the landing page's own cream paper, sinking into
the hero instead of lifting away. It is never a loading screen; it starts once its pictures are decoded
(at most 1.6 s).

| Beat | What happens | Timing |
|---|---|---|
| Reel | Her project pictures flash full-screen on cream paper, hard cuts that accelerate, printed in plum duotone (`#kv-reel`) at half strength | 14 cuts: 240 → 50 ms (about 1.5 s) |
| Develop | The last picture develops into its own colours as the view pulls back (scale 1.12 → 1, `expo.out`) | 1.1 s |
| Sink | The whole reel fades down until it is only a faint ground (opacity 0.5 → 0.09) | 0.85 s |
| Name | STUDIO / KAVALU (her lettering, plum) rises letter by letter where the headline will be, then "ಸ್ಟುಡಿಯೋ ಕವಲು · by Ananya" | 0.62 s, 30 ms stagger |
| Hand-over | The sheet fades out over the hero. The hero's own faint reel is already showing the same picture underneath, so the intro sinks into the hero's background; the headline rises and the album gathers round its stamp | 0.75 s |

Rules:
- Every full load of the home page, refresh included (brief 6); never when moving between pages inside
  the site, never with reduced motion or Save-Data, never with `?nointro`.
- Any click, key, wheel or touch fast-forwards to the hand-over.
- The reel uses only her own work, the same pictures the site shows.
- **Flash-safe by construction (WCAG 2.3.1).** Cuts this fast in full colour would count as flashes. Every
  cut is printed in a plum duotone held between relative luminance 0.006 and 0.098, at half strength over
  cream, so no change between two frames comes near the 10% that defines a flash, at any size or speed,
  and nothing in it is a saturated red. Only the last picture develops into colour, once and gradually.
  Measured on a frame-by-frame recording; check one in PEAT whenever the reel changes.

**The hero's faint reel.** Behind the hero, her work cross-fades at 9% opacity every 3.4 s with a slow
push-in (`Hero.module.css .reel`). It is the intro's afterglow, so it keeps its own slow time rather than
the flip-book's, and the flip-book's pause button stops it too (WCAG 2.2.2). Static under reduced motion.

### 9.4c The hero's scroll scene (desktop)

Brief 6 brought back the first version's scene, with brief 3's fix: it is scrubbed to the scroll, so it
plays backwards exactly and the whole collage scatters back when the reader scrolls up.

| Scroll (pinned for 1.5 screens, scrub 1 s) | What happens |
|---|---|
| 0–0.26 | The headline, text and buttons lift away; the faint reel fades; the centre stamp straightens |
| 0.03–0.45 | Every picture on the page glides into the centre stamp, shrinking to 42% and straightening as it tucks in (`power3.inOut`, 12 ms apart), then fades behind it |
| 0.46–0.84 | The stamp's picture takes over from the stamp and opens to the whole screen (the flip-book first snaps to the first project's cover, a full-resolution picture) |
| 0.80–1 | The picture dissolves into the powder blue of the first project spread, out of which the spread deals its prints |

Each piece has three layers (arrival, scene, resting tilt), so nothing the scene does fights the
arrival or the paper's angle, and a refresh mid-scene still measures from rest. Phones have no pin: the
pieces drift at their own depths instead.

### 9.5 Reduced motion

With `prefers-reduced-motion: reduce`:
- no intro and no smooth scrolling;
- no arrivals, scenes, writing or typing; every piece is at rest from the first frame;
- the flip-book doesn't run, and its hint and pause button are hidden;
- CSS transitions and view transitions are instant;
- arrows scroll the album without smoothing;
- dragging on the desk still works, because the user does it, but without inertia or the press
  scale.

Nothing is hidden waiting for motion that won't come. This is checked on every page
(`research/tools/site_check.py … reduced`).

### 9.6 Performance

- Animate `transform`, `opacity` and `clip-path` only, never layout properties.
- Scroll work runs on one loop (GSAP ticker drives Lenis and ScrollTrigger). Lenis `lerp` 0.085: a long,
  even glide that every scrubbed scene sits on (never below 0.08).
- Everything the scroll moves sits on its own compositor layer, so paper with masks, shadows and
  textures is drawn once and only moved; the spreads' sheet and shade too, or the slide-over repaints the
  whole screen every frame. But every layer is weighed again whenever anything repaints, so on a phone a
  mover is promoted only while it is on screen (`live()` in `lib/parallax.ts`). A desktop keeps them:
  promoting a batch as it came on screen was itself a hitch there.
- Nothing is measured on the first frame of a scroll. Scroll tweens render their starting point the
  moment they are made, and the hero scene is played to its end and back whenever the page is measured
  (it had cost 30 ms in one frame on the first scroll).
- No layout reads per frame: the nav hit-tests the ground under it only while it is showing.
- The hero's pictures re-render only when their own props change (`memo`); the flip-book ticks every
  420 ms.
- **Measured, not eyeballed.** A production build (`next start -p 3211`, cache warmed with
  `research/tools/warm.py`), traced by Chrome during a steady scroll (`research/tools/trace_scroll.py`,
  which splits the main thread's work by kind and by section) and timed frame by frame
  (`research/tools/smooth_check.py`, with a contact sheet). The dev server's numbers are inflated (a
  first visit compiles the page; React's development build renders twice), so never judge on it.
  Home page, 1440 × 900 at 144 Hz: 0.8% of frames over 20 ms, every section under 10.2 ms of main-thread
  work per frame. Phone, 390 × 844, finger drag, processor slowed 4× (`KV_CPU=4 KV_TOUCH=1 … mobile`):
  frames over 20 ms down from 66% to 29%; per section album 46 → 11 ms, hero 37 → 20, house view
  31 → 19, roads 26 → 9. Touch scrolling itself is the browser's own, off the main thread, so a slow
  phone still scrolls smoothly; only the depth updates less often.
- At most one pinned scene per page and no WebGL.
- The flip-book stops off-screen, during the scroll scene, under the drawer, and on hover or focus.

### 9.7 Where the motion came from

Motion was studied frame by frame in the browser on the researched sites, not borrowed from a library
demo. The method:
- every painted frame through screencast;
- a per-frame log of transforms;
- the browser's own records of CSS and Web Animation timings.

Results are in `research/motion_frames/`: 24 footers, the Digital Stamp Collection (hand notes drawn
stroke by stroke), Obys' Design Books (paper sheets, 500 ms ease-out lifts) and MERSI. The catalogue of
techniques and the anti-list are in `research/motion_catalog.md`.

### 9.8 Misuse

Don't add:
- fade-ups on every block;
- letter-split reveals on every heading;
- marquees, auto-rotating carousels, pulsing dots, breathing buttons;
- custom cursors, magnetic links on everything, images floating under the cursor;
- scroll-jacking, snap sections, horizontal pinned galleries;
- elastic or bouncy controls;
- preloaders that hold back the page. The intro (every load of the home page, at the client's request)
  is at most about 3.5 s to a usable hero, fast-forwarded by any input, drawn over a hero that is already
  painted, and absent with reduced motion or Save-Data;
- blur-everything, glass, liquid or RGB-split effects.

---

## 10. Components

### 10.1 Buttons (pills)

| Size | Height | Padding | Type | Use |
|---|---|---|---|---|
| **Large** | 3rem | 0 1.45rem | Schibsted 0.9375rem | Every call to action in content |
| **Small** | 2.6rem | 0 1.1rem | Schibsted `--t-small` | Header, toolbars, close, menu |

- **Shape:** fully round (`999px`).
- **Primary:** plum fill, cream text; hover oxblood. On dark: cream fill, plum text. On blue paper:
  deep fill, hover plum.
- **Secondary:** transparent with a 1px `--rule-strong` outline; hover outline plum.
- **With an arrow:** the gap widens from 0.6 to 0.95rem on hover (`--d-base`).
- **Press:** scale 0.97 (`--d-quick`, `--e-quick`), on every pill.
- **Disabled:** opacity 0.6.
- **Small controls:**
  - filter and view pills are the Small size with a typed count;
  - round icon buttons are 2.9rem (album arrows);
  - the hero pause button is the one exception, at 1.6rem on the stamp;
  - the skip link is a utility, not a pill size.
- **Measuring a pill:** a pill on tilted paper (the ticket, the writing sheet) or on a spread that is
  zooming out measures taller or shorter than its size; the size is the element's own height.

### 10.2 Links

- **Inline links** in running text are underlined, 1px, offset 3px.
- **Standalone links** with an arrow ("About the studio →") have a 1px bottom border, and their gap
  widens on hover.
- **Navigation links** carry the fork: a 9 × 6 px mark (one stem, two branches) that appears under the
  current page and on hover.

### 10.3 Header

- **Layout:** lockup left; Work and Studio in the centre; the Bengaluru clock and the Small "• Start a
  project" pill right.
- **On scroll:** it hides going down after 160 px and returns going up. Past 24 px it gets a sheet:
  cream at 86% with blur over light sections, deep plum at 62% over dark sections
  (`data-tone="dark"`).
- **Below 900 px:** a Menu button opens folder tabs. Focus moves in and is trapped; Escape closes it;
  focus returns to the button.

### 10.4 Eyebrows and labels

- **Eyebrow:** Courier Prime, `--t-micro`, capitals, +0.08em, `--ink-soft` (blue on dark). It opens
  every section.
- **Labels:** `--t-label` (captions' meta, fig labels, clock, table heads) and `--t-tiny` (small print
  on ephemera). Always capitals at +0.08em, in `--ink-soft` or `--ink-faint`.

### 10.5 Cards and paper

| Card | Spec |
|---|---|
| **Service (road) card** | `--paper-note`, or `--blue-2` for identity and film; a doodle badge; a rule under the title; lift on hover |
| **Ticket** | Powder blue, perforated stub, punched hole; kicker in `--t-tiny`; Large deep pill |
| **Contact card** | Ruled `--paper`; the email copies on click; studio, local time and clients; a postmark |
| **Index card** | `--cream-3` with a folder tab; numbered links |
| **Overview card** | Oxblood with the worn texture and a clip, −0.4°, `--shadow-lift` |
| **Palette chip** | A paint chip on `--paper`; click copies the hex |
| **Note** | `--paper-note` (or blue or plum paper); Homemade Apple; "— Ananya" in `--t-tiny` |

### 10.6 Project stamps and views

- **Stamps** are perforated, with a 4:5 window. A typed "FIG. NN" plus the title sits below.
- **Album row:** a horizontal row of every stamp. Drag with a mouse, swipe, or use the arrows.
- **Work:**
  - filter by road (Flip reflow, 0.7 s settle);
  - a Stamps view (grid on the project's tone);
  - an Index view (a table with a stamp preview that follows the cursor, only on devices that hover).
- **Morph:** a stamp morphs into the case-study cover.

### 10.7 Case-study blocks

The blocks are text, image (full, wide, inset), pair, stamps, palette, note and quote.
- **Mounts:** pictures cycle through tape, corners and clip with fixed tilts.
- **Captions:** typed strips.
- **Notes:** written in her hand.
- **Words:** they are never animated.

### 10.8 Footer

1. **Folder cascade:** Home, Work, Studio, Start a project.
2. **The desk:**
   - the ticket, the contact card and the index card are the working controls;
   - her pins: project pieces, palette chips, notes, the ಕವಲು word, the sticker;
   - a dotted pencil road that forks down to ಕವಲು, and a hand hint.
   - Desktop: drag and cursor depth. Below 1100 px: stacked cards and a swipe strip.
3. **The wordmark** arrives at rest.
4. **The legal line.**

### 10.9 Onboarding

See §11. Its pieces:
- the drawer: a right sheet, `min(44rem, 100vw)`, over blurred plum;
- the road progress line with five junctions;
- the letter, "Dear Ananya, …";
- the envelope.

### 10.11 Cursor

Researched on studio sites (`research/DESIGN_PRINCIPLES_v3.md` §4; Cuberto's follower recorded frame by
frame in `research/motion_frames/cursors/`). Two findings decided it: a dot that lags makes every click
feel late, and a disc laid over a picture covers the work it invites you to open. So the dot is exact,
and what a click will do is typed on a small paper tag beside the pointer.

The cursor is only for a fine pointer that can hover; touch, keyboard and forced-colours users keep the
system cursor. It is plum on light grounds and cream on dark ones (by `data-tone`):

| State | Looks like | When |
|---|---|---|
| default | an 8 px ink dot, exactly on the pointer | anywhere |
| link | a 36 px ring opens round it, a breath behind (0.14 s); the dot drops to 60% | any link or button |
| view | a typed paper tag, 16 px right and 18 px below the pointer: "OPEN →" or its own words ("NEXT →", "ROAD 02 →") | `data-cursor="view"` with `data-cursor-label`: work stamps, the next road, the house view's choices |
| drag | the tag "← DRAG →" | `data-cursor="drag"`: the album strip, desk pins |
| text | hidden; the native caret shows | inputs, textareas |

- The dot follows with no lag (measured: 0 px one frame after a move); the ring and tag trail by 0.14 s
  (`power3`; instant with reduced motion).
- The tag is cream paper with typed plum capitals on every ground, and lands with **Point** (§9.3).
- A press dips the dot and ring to 0.85.
- Whichever is nearer the pointer decides: a label on a link wins, and a button inside an annotated card
  is still a link.
- Never: blend-mode blobs, trails, a magnetic pull on everything, discs or pictures laid over the work.

### 10.12 The house view

The brand line is the index of the four roads (`components/home/Manifesto.tsx`; proposal A in
`research/DESIGN_PRINCIPLES_v3.md` §7, chosen over a pinned one-choice-at-a-time scene and a sentence
drawn as a fork).

- **The sentence stands still** on the torn cream sheet that slides over the spreads, set in four lines by design on desktop ("A brand is a set of choices; /
  what it says, how it looks, / where it shows up, / who it speaks to.") and flowing on phones. It is one
  `<h2>`, never split, faded or moved.
- **Each choice is a link** to its road card (`#road-branding` …), whose service is named for screen
  readers. Under it runs a hand-drawn road (1.25 px, a ±0.6 px wobble, measured from the words' line
  boxes) that forks at its end, and after it a typed footnote number (01–04).
- **The footnotes** under the sentence say which road each number is.
- **Motion, once:** the roads draw in reading order as the sentence comes up the screen, the numbers
  land with them, the footnotes follow. Nothing loops; the text never moves.
- **Pointing or focusing** on a choice quiets the other three to 50% (the contrast floor, §12),
  thickens its road to 2 px, lights its footnote, and lays one taped print of that road's work in the
  margin (desktop with a hovering pointer only, outside the measure). The cursor says "ROAD 0N →".
- **Following a choice** glides to its card, which straightens and lifts.
- **Reduced motion:** the roads are drawn from the start; changes are instant.

---

## 11. Onboarding

**Promise:** someone who likes the work can start a project immediately, from anywhere, in about three
minutes.

- **Entry:**
  - every "Start a project" opens the drawer (it is a real link to `/start` without JavaScript);
  - "Choose your road" on the home page carries the roads already picked;
  - `/start?road=` preselects a road.
- **Steps:**
  1. Road(s)
  2. Details: stage, then follow-ups per road
  3. Brand: name, link, brief, references
  4. Timing and budget: INR or USD, guessed from the time zone
  5. You: name, email, phone, best way to reach
- **The letter:** the answers are shown as a letter to Ananya as you go. The draft is kept in the
  session if you leave.
- **Sending:** the letter drops into an envelope, which is stamped and postmarked. The reference is
  "KAV-" plus five characters. What happens next: today; within one working day; a 20-minute intro
  call; a proposal within 3 working days; kick-off with a 50% advance.
- **Voice:** questions in plain words, one decision per screen, "Not sure yet" always allowed.
- **If sending fails:** offer "Email the letter" (pre-written) and "Copy my answers". Never lose
  what they typed.
- **Privacy:** spam checks flag, never reject. No secrets in the client. The keys live in server
  environment variables only.

---

## 12. Accessibility

- **Contrast:** every text pair in §4.6 meets WCAG 2.2 AA; most meet AAA.
- **Focus:** a 2px outline, offset 3px: plum on light, powder blue on dark (`.on-dark`, and every
  `data-tone="dark"` section). Light cards inside dark sections switch back to plum. Every hover has a
  matching focus style.
- **Keyboard:**
  - everything works without a mouse;
  - the drawer and the mobile menu move focus in, trap it, close on Escape and return focus;
  - the album scrolls with arrow buttons;
  - the desk's cards are ordinary controls.
- **Reduced motion:** §9.5. The flip-book also has a pause button and stops on hover or focus.
- **Flashing (2.3.1):** nothing flashes more than three times a second. The intro's fast cuts are a
  plum duotone whose frames differ by less than 10% in luminance (§9.4b), checked with PEAT.
- **Dimmed text:** display type that dims to show a state (a hovered clause, an unread line) never goes
  below 50% opacity, 3.28 : 1 on cream. Unread words at 13% (1.30 : 1) are what the house view used to do
  and are not allowed.
- **Language:** `lang="en-IN"` on the page; `lang="kn"` on every Kannada word.
- **Text alternatives:** meaningful alt text (§7); decorative paper is `aria-hidden`; animated type
  keeps its real text available to screen readers.
- **Targets:** at least 40 px for controls (the 1.6rem pause button is a stated exception, on a larger
  stamp target).
- **No horizontal scroll:** at any width from 320 px up, pieces that tilt or drift never widen the
  page (`overflow-x: clip` on `main` and `footer`).

---

## 13. Beyond the website

The same kit makes the studio's other things recognisable:
- **Social posts:** cream paper, one mounted print, a typed caption strip, one hand note, the K mark
  small in a corner (clear space respected). Project posts use that project's tones.
- **Proposals and decks:** Schibsted Grotesk titles and text, typed labels for meta (CLIENT · YEAR)
  on paper, the lockup on the cover, the wordmark on the last page.
- **Stationery and invoices:** the lockup top left, a typed reference (KAV-XXXXX), the postmark as
  a seal.
- **Packaging inserts and thank-you notes:** a ticket ("Admit one · ಕವಲು"), her signature.

---

## 14. What is uniform everywhere: the checklist

Use this to review any page (it is what queue item Q9 audits).

**Brand**
- [ ] The logo is the SVG lockup, mark or wordmark; never typed; never tilted; clear space kept.
- [ ] Copy follows §2: British/Indian spelling, " · " separators, en-dash ranges, no exclamation marks.

**Colour**
- [ ] Only palette tokens, supporting tones and the named paper/object colours appear.
- [ ] Project tones appear only inside their own project.
- [ ] No blue text on cream; no dark-on-dark text; no `#000` or `#fff`.

**Type**
- [ ] Headings are Schibsted Grotesk at a display step (`--d1`–`--h`), one weight, one colour, no italic word.
- [ ] Body and interface labels are Schibsted; Courier Prime capitals appear only on typed paper.
- [ ] Hand lettering only for notes; signature only for "Ananya"; Kannada in Anek with `lang="kn"`.

**Kit**
- [ ] One mount per picture; tilts from the fixed lists; shadows from the four tokens.

**Components**
- [ ] Pills are Large (3rem) or Small (2.6rem), press to 0.97, hover per §10.1.

**Layout and motion**
- [ ] Breakpoints are 1099 / 899 / 639 (plus allowed component breakpoints).
- [ ] Durations and easings are tokens (§9.2); at most one auto-moving thing, pausable; every motion
      has a reduced-motion state.

**Accessibility**
- [ ] Focus is visible and on-colour; dark sections carry `data-tone="dark"` and `.on-dark`.
- [ ] No horizontal page scroll at 390 px or 1440 px; no console errors.

---

## 15. Where each rule lives in the code

| Rule | File |
|---|---|
| Colour, type scale, spacing, motion, shadow and paper-texture tokens | `website/src/styles/tokens.css` |
| Base type, focus, reduced-motion CSS | `website/src/styles/base.css` |
| The grounds: each ground's paper and inks (text, rules, buttons, focus, selection) | `website/src/styles/surfaces.css` |
| Which section stands on which ground (the plum/blue proportion) | `website/src/lib/surfaces.ts` |
| Paper pinned to the page; the footer strip on the last ground | `website/src/components/GroundSheet.tsx` |
| The paper textures themselves, and how they were made and checked | `research/textures_v3/` (README) |
| Colour-proportion tests: renders, measured shares, contrast | `research/tools/palette_lab.py`, `research/palette_lab/` |
| Page transitions | `website/src/styles/transitions.css` |
| Fonts and their loading | `website/src/app/fonts.ts`, `website/src/fonts/` |
| Logo (lockup, mark, words) | `website/src/components/brand/Wordmark.tsx`, `wordmark-paths.ts` |
| GSAP setup and house curves | `website/src/lib/gsap.ts` |
| Write and type motion | `website/src/lib/handmade.ts` |
| Smooth scroll | `website/src/components/motion/SmoothScroll.tsx` |
| Ephemera (clip, sticker), doodles, scrap pieces | `components/Ephemera.tsx`, `components/Doodles.tsx`, `components/scrapbook/ScrapPiece.tsx` |
| Content (copy, projects, desk pins, onboarding) | `website/src/content/` |
| Client rules and the work queue | `kavalu_instructions.md` |

---

## 16. How this document was made, and sources

The structure follows how mature brand guidelines and design systems are written, adapted for a studio
whose brand is a website:

- **Brand guidelines.**
  - Danne & Blackburn's 1975 NASA Graphics Standards Manual (identity first, then typography, colour
    and applications).
  - The Foothill–De Anza Brand Guidelines (January 2026): logo versions, clear space and minimum size,
    misuse; colour palettes, weighting, combinations and misuse; type specimen; applications.
    https://fhda.edu/_downloads/_FHDA-Brand-Guidelines-January2026.pdf
- **Brand toolkits.** GitHub's Brand Toolkit, which runs brand identity and voice → foundations
  (accessibility, colour, logo, typography) → graphic elements → brand in action → motion identity.
  https://brand.github.com
- **Design systems.**
  - IBM Carbon's motion guidance: productive and expressive modes; duration tokens of 70, 110, 150, 240,
    400 and 700 ms; standard, entrance and exit curves; "the larger the change in distance or size, the
    longer the animation". https://carbondesignsystem.com/elements/motion/overview/
  - Atlassian's foundations: tokens, accessibility, content, spacing, grid, colour, typography,
    iconography, illustrations, logos, elevation, border, radius, motion.
    https://atlassian.design/foundations
- **The site itself.** A full inventory of every component, animation, token and inconsistency was taken
  from the code before writing (it drove the Q9 pass).

Research behind the decisions:
- `research/RESEARCH_REPORT.md` (226 sites), `research/SOURCES.md` (every link);
- `research/type/TYPE_REVIEW.md` (fonts);
- `research/motion_catalog.md` and `research/motion_frames/` (motion);
- `research/onboarding_research.md`;
- `research/brand/wordmark_fit/` (logo).

---

## 17. Changelog

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-10-24 | First edition: her wordmark rebuilt; type system Gambetta / Switzer / Courier Prime; scrapbook as the site's format; footer desk; write and type motion; consistency pass (audited on every page with `research/tools/uniformity_audit.py`). |
| 2.0 | 2026-10-24 | v3 (briefs 3, 4 and 5): light paper with plum as ink (§4.5, brief 5: plum 21%, cream and blue 62% at desktop, measured; brief 4's plum "desk" was built first and judged too plum); grounds and sheets as tokens (`styles/surfaces.css`, `lib/surfaces.ts`); paper textures baked per colour (§6.2); type re-chosen, Schibsted Grotesk with typed paper only and no italic-word device, on a six-step scale (§5); the house view as the index of the four roads (§10.12); the cursor's exact dot and paper tags (§10.11); the flash-safe duotone intro (§9.4b); space principles and the clutter audit (§8.3). |
