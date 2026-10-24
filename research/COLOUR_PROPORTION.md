# Colour proportion: plum and powder blue

**Queue item:** Q24 (brief 4) · **Date:** 24 October 2026 · **By:** the colour-research agent
**Status:** research, plus five iterations to build and test. Nothing in `website/` was changed.
**Method:** web research (WebSearch, until the session's shared search budget ran out, then WebFetch of
known pages), and local analysis of screenshots the project had already captured
(`research/screens/`, 226 sites, 23 Oct 2026, 1440 × 900, three scroll depths each, made with
`research/tools/capture.py`). No browser was used for this work.
**New tools:** `research/tools/colour_coverage.py` measures palette coverage from screenshots (§6);
`research/tools/colour_area_model.py` reproduces the target shares in §4.

> **Brief 4 (verbatim, from `kavalu_instructions.md` Appendix D):** "the main colours to be used are
> plum and powder blue, like these both should be like 70-90% of the website depending on how it looks
> better and the rest should be the remaining percentage. see multiple iterations and multiple researches
> on how and which exact combo will look better. research and test properly, on what is the best
> proprotion and how to present it the best"

---

## Summary

- **How to count.** A colour's share is its percentage of the page area that is neither a photograph
  nor a project's own colours (her clients' tones are the work, like the photos; they are reported on
  their own). Plum means plum + deep plum + the plum inks; blue means powder blue + pale blue; cream
  means cream + the paper whites. Measure every page at 1440 and 390 px, then the site.
- **Where we are.** Today's home page measures **plum 22 · blue 9 · cream 69 · oxblood 0**, so plum
  and blue cover **31%** (desktop; 29% on a phone). Her old site measures 40%. The brief wants 70–90%.
- **The fact that decides everything.** The palette is three darks (plum L\* 11, deep plum 6,
  oxblood 17) and two lights (powder blue 80, cream 96). Darks never read on darks (1.1–1.3 : 1) and
  lights never read on lights (1.5 : 1). So "plum and blue at 70–90%" is first a choice of the
  **dark-to-light balance and which colour is the ground**; hue comes second.
- **Five iterations**, all set at 83–86% so that round 1 compares arrangement, not quantity
  (site-wide; photos and project colours left out):

  | | Iteration | Plum | Blue | Cream | Oxblood | Plum+blue | Ground switches on home |
  |---|---|---|---|---|---|---|---|
  | A | **Plum page**: plum everywhere, blue as cards, poster and type | 66 | 18 | 14 | 2 | 84% | 2 |
  | B | **Blue page**: powder blue replaces cream as the paper; plum is ink and three dark chapters | 27 | 58 | 13 | 2 | 85% | 6 |
  | C | **Alternating chapters**: full-bleed plum and blue swap at every section | 49 | 36 | 12 | 3 | 85% | 7 |
  | D | **Plum desk, blue sheets**: one plum ground that never changes; reading sections are large blue sheets laid on it | 56 | 29 | 12 | 3 | 85% | 0 |
  | E | **Two roads**: each page starts on powder blue and turns to plum at one junction | 49 | 37 | 12 | 2 | 86% | 3 |

- **Recommendation: D, then E, B, A, C.** D commits to one ground (calm, no stripes), still gives
  blue a main colour's share, puts long reading on light paper, turns the scrapbook into something
  literal (papers on a desk), and carries the brand's strongest image (the powder-blue wordmark on deep
  plum) through every page. E is the alternative if a dark first screen proves too heavy.
- **Then turn the dial.** Build the winner at about 75%, 85% and 90% by moving named surfaces between
  cream and blue (§5.2), measure each with `colour_coverage.py`, and choose with Ananya.

---

## 1. The palette in numbers

### 1.1 How to count

| Term | Meaning |
|---|---|
| **Palette share** (the Q24 target) | Plum, blue, cream and oxblood as a percentage of the page area **minus photographs and minus project-colour areas**. The four add up to 100. |
| **Project share** | Project tones (`tone.bg`) as a percentage of all non-photo area. They are allowed only in a project's spread, case-study hero and next-road band (`BRAND_DESIGN.md` §4.4), so they are content, not the site's colour. Today about 13% of the site. |
| **Ground switch** | A full-bleed change of the ground family (plum ↔ blue ↔ cream ↔ project) between consecutive sections. A sheet or card laid on a ground is not a switch. |
| **Site figure** | Pages pooled by area: home, work index, studio and three case studies. Report desktop and phone separately. |

### 1.2 Three darks and two lights

| Token | Hex | L\* | C\* | Hue | Reads as |
|---|---|---|---|---|---|
| Deep plum | `#270617` | 5.6 | 18.6 | 351° | dark |
| Ink | `#241319` | 8.2 | 9.9 | 357° | dark |
| Plum | `#390D26` | 11.3 | 25.2 | 347° | dark |
| Oxblood | `#491C17` | 17.0 | 25.2 | 34° | dark |
| Powder blue | `#ABCDD6` | 80.3 | 12.4 | 221° | light |
| Pale blue | `#C9DFE5` | 87.4 | 8.2 | 222° | light |
| Cream | `#F3F3E7` | 95.5 | 6.1 | 110° | light |
| Paper | `#FBFAF2` | 98.2 | 4.1 | 105° | light |

CIELAB values computed from the hex codes (D65). Consequences:
- **Plum, deep plum and oxblood merge.** Plum and deep plum are ΔE 8.8 apart (a gentle step, good
  for a footer that continues the page); oxblood on plum is 1.16 : 1. An oxblood card on a plum page
  has no visible edge without a light border.
- **Powder blue and cream merge as values.** Cream paper on powder blue is 1.5 : 1 and pale blue on
  powder blue 1.2 : 1. Paper on blue needs its shadow to separate.
- **Every readable pair crosses the dark/light line.** That is why the decision is about value first.

### 1.3 Contrast on each ground

WCAG 2 ratio, then APCA Lc (positive: dark text on light; negative: light on dark). Computed with
the WCAG relative-luminance formula and APCA-W3 0.0.98G-4g. WCAG 2.2 AA asks 4.5 : 1 for text and
3 : 1 for large text (18.5 px bold or 24 px) and for the parts of a control that identify it
([SC 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html),
[SC 1.4.11](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html)). APCA, the
candidate method for WCAG 3 and still a draft, asks Lc 75 at minimum and Lc 90 preferred for
body-text columns, Lc 60 for other content text and Lc 45 for headlines
([APCA in a Nutshell](https://git.apcacontrast.com/documentation/APCA_in_a_Nutshell.html)).

| Text ↓ on ground → | Deep plum | Plum | Oxblood | Powder blue | Pale blue | Cream |
|---|---|---|---|---|---|---|
| Cream | 16.7 · −98.6 | 14.9 · −97.2 | 12.9 · −95.3 | **1.5** | **1.2** | – |
| Cream at 90% | 13.5 · −84.0 | 12.2 · −83.4 | 10.7 · −82.5 | – | – | – |
| Powder blue | 11.1 · −71.9 | 9.9 · −70.6 | 8.5 · −68.7 | – | **1.2** | **1.5** |
| Pale blue | 13.5 · −83.9 | 12.0 · −82.6 | 10.4 · −80.7 | **1.2** | – | **1.2** |
| Deep plum | – | **1.1** | **1.3** | 11.1 · 72.6 | 13.5 · 83.8 | 16.7 · 97.2 |
| Plum | **1.1** | – | **1.2** | 9.9 · 70.9 | 12.0 · 82.1 | 14.9 · 95.5 |
| Ink | **1.1** | **1.1** | **1.2** | 10.5 · 72.3 | 12.8 · 83.4 | 15.9 · 96.8 |
| Oxblood | **1.3** | **1.2** | – | 8.5 · 68.5 | 10.4 · 79.7 | 12.9 · 93.1 |
| Ink-soft `#5D4A50` | 2.3 | 2.0 | 1.8 | 4.9 · 56.1 | 5.9 · 67.3 | 7.3 · 80.7 |
| Ink-faint `#6D5F62` | 3.1 | 2.7 | 2.4 | **3.6** · 48.1 | 4.4 · 59.2 | 5.4 · 72.7 |
| Blue soft ink `#50334A` | – | – | – | 6.5 · 63.1 | 7.9 · 74.2 | – |
| Blue faint ink `#5E4A5E` | – | – | – | 4.75 · 55.6 | 5.8 · 66.7 | – |

What the table says:
1. **Body text on powder blue falls just short of APCA's body-text minimum.** Deep plum on `#ABCDD6`
   is AAA by WCAG (11.1 : 1) but Lc 72.6, under Lc 75. On pale blue `#C9DFE5` it is Lc 83.8. Long
   reading belongs on pale blue or paper; powder blue carries display type, short copy and controls.
2. **Blue on plum is for display, emphasis and labels, not paragraphs** (9.9 : 1 but Lc −70.6).
3. **Cream on plum is very strong (Lc −97).** For paragraphs, cream at 90% (Lc −83) keeps well above
   the body minimum and glows less (see §2.4).
4. **Ink-faint is not allowed on powder blue** (3.6 : 1 fails AA). On blue the soft inks are the two
   blue-ground tokens already in `tokens.css`.

**Tints used for rules and control borders** (the current values in `styles/surfaces.css`):

| Tint | On | Ratio | Verdict |
|---|---|---|---|
| Cream 16% (`--line` on dark) | plum / deep | 1.55 / 1.51 | fine for decorative hairlines |
| Cream 34% (`--line-strong` on dark) | plum / deep | **2.77 / 2.81** | fails SC 1.4.11 where the border is what identifies an input; use **40%** (3.36 / 3.45) |
| Deep 18% (`--line` on blue) | powder blue | 1.45 | fine for decorative hairlines |
| Deep 36% (`--line-strong` on blue) | powder blue | **2.22** | fails for input borders; use **50%** (3.17) |
| Plum 32% (`--rule-strong` on cream) | cream | **2.03** | fails for input borders; use 50% or more |

A text-labelled button needs no border at all under SC 1.4.11; a custom focus ring must reach 3 : 1
([SC 1.4.11](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html)). Blue rings on
dark (8.5–11.1 : 1) and plum rings on light (9.9–14.9 : 1) pass everywhere.

**The muddy middle.** Plum and powder blue mixed half and half give `#726D7E` (L\* 47, C\* 10), a grey
mauve that is 3.3 : 1 against plum and 3.0 : 1 against blue. Any crossfade, gradient or translucent
overlay between the two passes through it. See §2.3.7.

**Her project colours against the two grounds** (WCAG ratio and CIELAB ΔE):

| Project tone | vs plum | vs powder blue |
|---|---|---|
| Nivritti navy `#07253D` | **1.1 : 1** · ΔE 29 | 9.3 : 1 · ΔE 68 |
| Fillers brown `#3F1B0E` | **1.1 : 1** · ΔE 24 | 9.0 : 1 · ΔE 75 |
| Studio Anokhi terracotta `#9F4A30` | 2.8 : 1 · ΔE 49 | 3.6 : 1 · ΔE 70 |
| Not-So-Onam? magenta `#A11F5B` | 2.3 : 1 · ΔE 40 | 4.3 : 1 · ΔE 78 |
| Shoot stills red `#A32D02` | 2.3 : 1 · ΔE 64 | 4.2 : 1 · ΔE 91 |

Her work separates from powder blue far better than from plum. On any plum page, a project area needs
a light edge (a paper border, a deckled or perforated strip).

### 1.4 Today, measured

Measured with `research/tools/colour_coverage.py` on the latest captures that cover whole pages:
the v2 build of 24 Oct 03:39 (`research/working-shots/v2/`, six viewports at 0–100% of each page,
no photo masks, so photos fall partly into "unassigned") and her current live site
(`current_website/`, three full-page captures).

| Page | Plum | Blue | Cream | Oxblood | Plum+blue |
|---|---|---|---|---|---|
| Home, 1440 px | 22 | 9 | 69 | 0 | **31%** |
| Home, 390 px | 18 | 10 | 71 | 0 | 29% |
| Work index | 41 | 9 | 48 | 2 | 50% (the deep-plum footer is half of this short page) |
| Studio | 20 | 6 | 57 | 17 | 26% |
| Case study (Nivritti) | 33 | 9 | 54 | 4 | 42% |
| Her current live site | 34 | 6 | 42 | 18 | 40% |

The footer (folder tabs, the deep-plum desk and the blue wordmark band, about 2,400 px at 1440) is
already the largest plum-and-blue area of every page: about 22% of the home page and 62% of the work
index.

---

## 2. Findings

### 2.1 Proportion frameworks

**The 60-30-10 rule.** A dominant colour on about 60% of the surface, a secondary on about 30%, an
accent on about 10%. Mintos's brand site puts it plainly: "Use colors in a 60–30–10 ratio for
balance": 60% neutrals "for backgrounds and base layers", 30% brand greens "for main elements", 10%
accents "for highlights", with "the darker green used for text"
([Mintos](https://brand.mintos.com/color)). Applied to websites: 60% "usually the background or the
main visual part", 30% "used for text and important features", 10% "on key elements like
call-to-action buttons", and it is "just a guide, not a rule"
([Pixpa](https://www.pixpa.com/blog/60-30-10-rule-in-web-design)). The rule is said to come from
interior design; no documented origin was found (**unverified**).

**How brand guidelines set a dominant pair.**

| Source | What it sets | Lesson for Kavalu |
|---|---|---|
| [Texas A&M](https://marcomm.tamu.edu/creative-platform/visual-style/brand-colors) | "Primary colors of maroon and white should be used **75%** of the time" (secondary 20%, accent 5%) for audiences less familiar with the university; **60/30/10** for familiar, on-campus audiences. Aggie Maroon is `#500000`. | The closest documented analogue to "plum and blue at 70–90%": a deep wine plus a light colour as a two-colour primary at 75%. And the less known the brand, the more its primary pair should dominate. A young studio sits at the high end. |
| [University of Chicago](https://creative.uchicago.edu/color-system) | "Within the primary palette itself, Maroon should always be the dominant color"; colours at 100%, "Tints should never be used." | Inside the pair, one colour leads. |
| [Colt](https://docs.colt.net/brand/visual-system/colours) | "Colt teal and Black should be the dominant colours in any layouts"; "individual pieces may vary", but "the cumulative effect keeps the overall brand balance." | Two colours can share dominance; judge the balance over the whole site, not per section. |
| [University at Buffalo](https://www.buffalo.edu/brand/creative/color/color-ratios.html) | Blue and white "predominant"; "Ratios on individual pages, spreads, layouts and even full communications can vary"; view everything together and apply the "squint test". | Measure per page, decide on the site, and squint at the result (§6). |
| [University of Wollongong](https://www.uow.edu.au/brand/brand-system/colour/) | White gets "a greater proportion"; for events and campaigns, "bolder colours ... can be increased" for "impact". | A standard proportion and an impact mode can coexist. |
| [National Wildlife Federation](https://brandguide.nwf.org/brand-palette/color-proportions/) | "Primary and secondary colors should carry most of the visual weight"; accents "used sparingly". | Plum and blue carry the weight; cream and oxblood are the minor colours. |
| [Designit](https://designit.com/brand/guidelines/introduction/colour-palette) | An "approximate ratio" chart; "Don't put colour on colour"; "if you layout starts looking like a rainbow, you've probably gone too far." | Kavalu's dark-on-dark and light-on-light failures are the same rule. |
| [Mailchimp](https://mailchimp.com/about/brand-assets/) | "Cavendish Yellow is Mailchimp's hero color." "We use Peppercorn for accents." | A light colour can be the hero with a dark one as accent: the inverse is also a valid brand. |
| [Pentagram for Slack](https://www.pentagram.com/work/slack) | The identity "retains Slack's distinctive aubergine purple as an accent color"; four primaries instead of eleven. | A deep purple brand colour is often kept small. Kavalu is choosing the opposite on purpose, so the dark colour must be made to feel generous rather than heavy. |
| [Tiffany Blue](https://en.wikipedia.org/wiki/Tiffany_Blue) | `#81D8D0`, a registered colour trademark since 1998, "used ... extensively on promotional materials like boxes and bags". | A pale blue becomes a signature by living on objects. Kavalu's blue tickets, cards and posters work the same way. |

**How a 70–90% pair usually splits** (the shares follow the 60-30-10 roles above; the feel of each
split is design judgement):

| Split (dominant / second + rest) | How it reads | Iteration |
|---|---|---|
| 65 / 18 + 17 | One colour, with the second as an accent. Under about 20% the second colour stops reading as "main". | A |
| 55 / 30 + 15 | One clear ground, the second as large pieces. The classic 60-30 with the accent role taken by the minor colours. | D |
| 50 / 35 + 15 in two fields | Two grounds, each dominant in its half of the page. | E |
| 45 / 40 + 15 interleaved | Near even. Needs strict structure or it reads undecided. | C |
| 28 / 58 + 14 | The light colour leads; the dark is ink and punctuation. | B |

### 2.2 Real sites built on a dominant pair

**What the 226 captured sites open on.** The first screen of every captured site, classed by its
largest flat region (computed for this report from `research/screens/*_0.jpg`):

| First screen | Sites | Share |
|---|---|---|
| White, off-white or cream | 84 | 37% |
| Dark ground | 67 | 30% |
| Led by an image (no flat region over 30%) | 39 | 17% |
| Light tint (pastel) | 19 | 8% |
| Mid-tone or saturated colour | 17 | 8% |

Of the 67 dark grounds, only **5 are coloured** (C\* ≥ 8): Ghia's wine, Bruno Simon's aubergine,
and the navies or olives of Squadron 14, Utsubo and Whoamama. The other 62 are black or charcoal,
among them Base Design, Bibliothèque, JKR, Locomotive, Mucho, Order, OK-RM, Porto Rocha, Studio
Dumbar and Two Times Elliott. **A dark shell is a familiar way for studios to show work, and a
coloured dark shell like plum is rare.**

**Sites built on a dominant colour or pair.** Measured from the captures with k-means clustering in
CIELAB; percentages are of the captured screen area (1440 × 900, three screens per site). "Captures"
means `research/screens/<site>_0–2.jpg`, 23 Oct 2026.

| Site | Page (ground) | Ink | Blocks | Sections alternate? | Minor colours | Evidence |
|---|---|---|---|---|---|---|
| [Ghia](https://drinkghia.com) (aperitif) | Wine `#651B32`, 83–87% | Cream condensed capitals | Pink `#E4656D` pills, red accents | Not observable: all three captures show its welcome overlay | Pink and red ≈ 6–9% | Captures; the project's note: "Oxblood/plum palette" (`research/reference_sites.json`) |
| [Bruno Simon](https://bruno-simon.com) (portfolio) | Aubergine `#230B39`–`#2A0C44`, 57–63% | White and violet light | Violet light ≈ 30% | One 3D scene | Violet ≈ 30% | Captures |
| [Fishwife](https://eatfishwife.com) (tinned fish) | Sky blue `#A0DAFE`, 72% | Near-black `#32231F` | Coral frame `#D8483F` 7–8%, yellow buttons 4–8% | Not observable (overlay) | Coral and yellow ≈ 15% | Captures |
| [Noomo](https://noomoagency.com/) (studio) | Periwinkle `#CCD6EB`, 78–92% | Black | 3D objects | No switch in three screens | Under 10% | Captures |
| [Chrissie Abbott](https://chrissieabbott.com/) (art director) | Pale aqua `#D6E6E7`, 57% of the first screen | Black wordmark | A grid of client work in its own colours | No; the aqua stays as gutters | Client colours ≈ 40% | Captures |
| [Robot Food](https://www.robot-food.com/) (branding agency) | White `#FCFBFA` | Black | Pale aqua `#D3F1F6` rounded blocks, 38–47% of screens 2–3 | Two switches: image → white with aqua blocks → black footer (43% of screen 3) | Black 15–43% by screen | Captures |
| [Pearlfisher](https://www.pearlfisher.com) (branding agency) | Black `#060606` frame | White | One pale aqua panel `#CBEBF0`, 65% of the first screen; then client tiles | The black frame is constant | Client colours in tiles | Captures |
| [Katrine Mehl](https://katrinemehl.com/) (designer) | Pink `#FACDE4`, 41–80% | White italic, set on the blue sheet | A photographed sheet of cobalt paper `#5B79BC`, 38–51% of screens 1–2 | No; the ground is constant and the sheet is the block | Cobalt ≈ 40% at the top, then little | Captures |
| [Hicard Studio, Scrapbook](https://scrapbook.hicard.studio/) | Black | Small white type | One pale aqua printed piece, centred | No | The print ≈ 20% | Captures. A scrapbook on a dark page with a pale-blue paper object. |
| [Happy Happy Creative](https://www.happyhappycreative.com/) ("Brand and Content for Founder-led Brands") | No single ground: butter `#FBE397` (56% of screen 1), olive `#706729` (56% of screen 2), grey-blue `#B4CECE` (25% of screen 3), cream between | Tomato and brown | Full-bleed bands | Yes: three ground changes in about 3,300 px | Each band leads its screen | Captures |
| [Agence Foudre](https://www.agencefoudre.com/) (social agency) | A new full-bleed colour per screen: green `#01512C` 71% → magenta `#DA3C8B` 70% → blue `#2885BB` 46% | Cream-pink, white | – | Yes, every screen | No dominant colour | Captures; listed in `research/SOURCES.md` as "the 'fun' direction to avoid" |
| [Bielke&Yang](https://bielkeyang.com/) (studio) | Off-white `#FEFDF9` 67% → navy-black `#0F1628` 45–62% | Dark serif on light, white on navy | Photographs | One switch: light first, a dark work section | – | Captures |
| [Fiddle.Digital](https://fiddle.digital/) (studio) | Lilac grey `#C9C1CE` 80% → black 57% | Black on lilac, white on black | A deep-red case image `#50090C` | One or two switches | – | Captures |
| [Order](https://order.design/) (studio) | Charcoal `#151515`, 45–86% | Light grey | Client work as tiles (Chapter's blue 24% of one screen) | The dark shell is constant | Client colours inside tiles | Captures |
| [Base Design](https://www.basedesign.com) (studio) | Black | White | A dense grid of client work in its own colours | Constant | Client colours inside tiles | Captures |
| [Graza](https://www.graza.co) (olive oil) | Cream `#F6E6D9` | Dark green | One lime block `#9FEE80`, 45% of screen 2 | No; one block on a constant ground | Lime ≈ 15% overall | Captures |
| [Good Earth](https://www.goodearth.in) (Indian lifestyle) | Light | Dark | Wine `#6F1B3D` header bar and buttons, 8–12% | No | Wine as the accent | Captures (a cookie overlay dims the page) |
| [Studio Sorted](https://www.studiosorted.com/) (her friend's studio) | Yellow `#FDCD02`, 88% of the first screen | Black | Photographs, then cream with yellow | Yes | – | Captures |

**Documented brands built on a dark-and-light pair** (no capture; what the source says):

| Brand | The pair | How it is used | Source |
|---|---|---|---|
| Aston Villa (and West Ham, Burnley, Scunthorpe, Trabzonspor) | Claret and sky blue | "a claret shirt with sky blue sleeves": the dark colour takes the body, the light blue frames it | [Wikipedia](https://en.wikipedia.org/wiki/Aston_Villa_F.C.) |
| Texas A&M | Maroon `#500000` and white | 75% together for less familiar audiences | [Texas A&M](https://marcomm.tamu.edu/creative-platform/visual-style/brand-colors) |
| Colt | Teal and black | Both "dominant ... in any layouts" | [Colt](https://docs.colt.net/brand/visual-system/colours) |
| Mailchimp | Cavendish Yellow and Peppercorn | Yellow the hero, Peppercorn the accent | [Mailchimp](https://mailchimp.com/about/brand-assets/) |
| Slack | Aubergine and four primaries | Aubergine kept as an accent | [Pentagram](https://www.pentagram.com/work/slack) |
| Tiffany & Co. | Tiffany Blue | The colour of the box and bag | [Wikipedia](https://en.wikipedia.org/wiki/Tiffany_Blue) |

**What the examples show:**
1. **Calm sites keep one ground and give the second colour a few large pieces**: Katrine Mehl's paper
   sheet, Pearlfisher's aqua panel, Robot Food's aqua cards, Graza's lime block, Hicard's aqua print.
2. **Full-bleed alternation brings energy but no dominant colour.** Happy Happy Creative changes ground
   three times in three screens; Agence Foudre on every screen.
3. **Work in many colours sits best in a constant frame**: Base Design, Order, Pearlfisher and
   Chrissie Abbott keep one ground and let the clients' colours live inside tiles.
4. **Light first, dark later** is a common two-part structure (Bielke&Yang, Fiddle.Digital).
5. **Wine grounds are rare** (Ghia), which is an opportunity: a plum site would be recognisable in its
   category.

### 2.3 How to present it

#### 2.3.1 Colour blocking versus one ground with blocks
- **Perception.** In figure–ground perception "the background tends to continue as one color behind
  potentially multiple foreground figures", and "smaller regions are often (but not always) figures"
  ([Wikipedia: Figure–ground](https://en.wikipedia.org/wiki/Figure%E2%80%93ground_(perception))).
  A continuous plum ground with blue sheets on it therefore reads as "a plum page with blue papers"
  even when blue covers 30–40%. Alternating full-bleed bands make every band its own ground, so the
  page has stripes and no ground.
- **The kit agrees.** The scrapbook is papers on a page: a sheet is the natural form for the second
  colour (`BRAND_DESIGN.md` §1.4: "If an element could not exist as a piece of paper ... ask whether
  it should exist").
- **Depth.** Lighter sheets on a darker ground also follow NN/g's dark-interface advice to "use the
  darkest colors for the page elements on the bottom" and lighter ones on top
  ([NN/g](https://www.nngroup.com/articles/dark-mode-users-issues/)).
- **Use full-bleed changes for chapters only**: the project spreads, a case-study hero, the footer.

#### 2.3.2 Dark first or light first
- 30% of the 226 captured sites open dark; most of the strongest identity studios among them
  (§2.2). Dark first says "gallery"; it is how studios show work.
- For reading, light grounds win for most people: "in users with normal vision, light mode leads to
  better performance most of the time", and "the smaller the font, the better it is for users to see
  the text in light mode" ([NN/g](https://www.nngroup.com/articles/dark-mode/)).
- The intro is already deep plum. On a plum page (A, D) it lands on the same desk; on a blue page
  (B, E) its last frame lifts to reveal light paper, a "lights on" moment.
- Resolution: **dark first for showing, light sheets for reading** (D), or **light first, then dark**
  (E).

#### 2.3.3 Type colour on each ground
- **On plum**, text is cream, never pure white: web.dev avoids pure white "to prevent glowing and
  bleeding against the surrounding dark content" ([web.dev](https://web.dev/articles/prefers-color-scheme)).
  Set paragraphs in cream at 90% (12.2 : 1, Lc −83) and headings at 100%.
- **Light type looks heavier on dark.** A light area looks larger than an identical dark one (the
  irradiation illusion, [Wikipedia](https://en.wikipedia.org/wiki/Irradiation_illusion)), and NN/g
  notes that light text on dark looks bolder, that thick fonts "bleed" and thin ones get "swallowed"
  ([NN/g](https://www.nngroup.com/articles/dark-mode-users-issues/)). The project's own type review
  found hairlines vanishing on plum at light weights (`research/type/TYPE_REVIEW.md`, Boska). So on
  plum: keep Gambetta at display sizes only (`--t-3` and up), test 330–350 against today's 320, and keep
  Switzer body at 400. Judge in the browser.
- **Blue on plum is the emphasis colour**: the italic phrase, eyebrows, the wordmark. Lc −70.6 suits
  display and labels, not paragraphs (§1.3).
- **On powder blue**, deep plum for text, plum for headings, oxblood or deep plum for labels, never
  ink-faint. Paragraphs longer than about three lines move onto a pale-blue or paper sheet.
- **One ink per ground, at opacities.** NN/g recommends "one color with different levels of opacity"
  rather than fixed colours that suit some grounds and not others
  ([NN/g](https://www.nngroup.com/articles/dark-mode-users-issues/)). `styles/surfaces.css` already
  does this with `--on`, `--on-soft` and `--on-faint`.

#### 2.3.4 Photography and client colours
- Colours change with their surroundings: "we do not see colors as they really are. In our perception
  they alter one another" (Albers; [Wikipedia](https://en.wikipedia.org/wiki/Josef_Albers)). Her
  photographs will look different on plum and on blue, so judge each iteration with the real images.
- Her flat project colours separate from powder blue by ΔE 68–91 and from plum by only ΔE 24–64,
  with navy and brown at 1.1 : 1 (§1.3). "Highly saturated colors on dark backgrounds have poor
  visibility" ([NN/g](https://www.nngroup.com/articles/dark-mode-users-issues/)). On plum, every
  project area gets a light edge: the paper border of a print, or a deckled or perforated cream strip
  where a project band meets the plum.
- Do not dim or filter her work for a dark page. web.dev reports that people prefer "slightly less
  vibrant" images in dark mode ([web.dev](https://web.dev/articles/prefers-color-scheme)), but these
  are portfolio pieces: mount them instead.
- The current pictures are low-resolution stand-ins (Q21). Repeat the photo check when the originals
  arrive.

#### 2.3.5 Texture on dark grounds
- Keep every ground a paper texture (brief 3). The v3 textures are baked "within dE 0.1 of the flat
  colour, so text contrast holds" (`website/src/styles/surfaces.css`).
- Never put a gradient between plum and blue. Colour banding appears in "gradual gradients" and is
  fixed with dithering ([Wikipedia](https://en.wikipedia.org/wiki/Colour_banding)), and a plum-to-blue
  gradient also crosses the muddy middle.
- Grain shows more on dark. Keep its contrast lower on plum and deep plum than on cream, and quieter
  still behind body text (judgement; check at 100% zoom on a phone).

#### 2.3.6 Rhythm: how many switches
- From the captures: Noomo, Fishwife and Order show no switch in three screens; Bielke&Yang one;
  Robot Food two; Happy Happy Creative three; Agence Foudre one per screen. Today's home has three
  (cream → project spreads → cream → plum footer).
- Guidance (judgement): **at most one full-bleed ground change for every two to three screens**,
  so no more than four on the 11,000 px home page. Never two changes inside one screen. Sheets and
  cards do not count. Keep related sections on one ground.
- Judge the balance over the page, not per section (the Buffalo squint test; Colt's "cumulative
  effect").

#### 2.3.7 Moving between grounds
- **No crossfades between plum and blue.** A fade passes through `#726D7E` (§1.3). Change grounds the
  way paper moves: a sheet slides over, a page turns, a wipe follows the scroll. This also fits the kit
  ("Pieces land", `BRAND_DESIGN.md` §6.1).
- The header's tone (`data-tone`) should switch at the boundary, not fade. Hover states should not
  animate opacity from one ground colour to the other.

#### 2.3.8 Pitfalls
| Pitfall | Where it bites | Avoid it by |
|---|---|---|
| **Zebra**: too many full-bleed switches | C (7 on home), B (6) | ≤ 4 per long page; use sheets |
| **Monotony and dark fatigue**: 11,000 px of plum with no light | A | Large light sheets for reading (D) or a light first half (E) |
| **The muddy middle** | Gradients, crossfades, translucent overlays of one ground on the other | Opaque paper, wipes and slides |
| **Losing the accent**: blue objects vanish on a blue ground | B, E (the blue half) | Recolour tape, stickers, tickets, the cursor's view disc |
| **Dark-on-dark edges**: oxblood, navy, brown on plum (1.1–1.3 : 1) | A, D, E (plum half) | A light paper edge on every dark object |
| **Light-on-light edges**: cream on blue (1.5 : 1), pale blue on blue (1.2 : 1) | B, E (blue half) | `--shadow-paper` on every paper object |
| **Blue confetti**: many small blue pieces at 30%+ | Any iteration with blue in small bits | Few, large blue pieces |
| **Reading on mid-light blue** (Lc 72.6) | B, C, E | Long text on pale blue (Lc 83.8) or paper |

### 2.4 Accessibility and comfort
- **Long text on plum or on blue?** NN/g: light mode is better for most readers with normal vision,
  and more so as text gets smaller; dark mode helped readers with cloudy ocular media such as
  cataract ([NN/g](https://www.nngroup.com/articles/dark-mode/)). So long reading goes on light paper;
  plum carries display type, image sections and short text.
- **Recommended text colours** (all pass WCAG 2.2 AAA for body text, 7 : 1):

  | Ground | Paragraphs | Short copy and UI | Headings | Small labels (10–12 px) |
  |---|---|---|---|---|
  | Deep plum / plum | cream at 90% (13.5 / 12.2 : 1; Lc −84 / −83) | cream | cream | cream, or cream at 78% (Lc −68) |
  | Powder blue | move to a pale-blue or paper sheet | deep plum (11.1 : 1; Lc 72.6) | plum | deep plum |
  | Pale blue sheet | ink or deep plum (12.8 / 13.5 : 1; Lc 83) | deep plum | plum | `--blue-ink-soft` (7.9 : 1) |
  | Cream / paper | ink (15.9 : 1; Lc 97) | ink | plum | ink-soft (7.3 : 1) |
  | Oxblood | cream at 90% (10.7 : 1; Lc −83) | cream | cream | cream at 78% |

- **Small labels.** APCA's body-text sizes start at 14 px (Lc 90) and 18 px (Lc 75)
  ([APCA](https://git.apcacontrast.com/documentation/APCA_in_a_Nutshell.html)). The 10–12 px typed
  labels sit below its reading sizes, so give them the strongest ink of their ground and keep them to
  a few words. The footer's legal line at cream 60% (6.4 : 1, Lc −45) passes WCAG but is weak by
  APCA; 72% gives Lc −60.
- **Line length and spacing.** WCAG's AAA presentation criterion: lines no wider than 80 characters,
  line spacing at least 1.5, paragraph spacing 1.5 times the line spacing
  ([SC 1.4.8](https://www.w3.org/WAI/WCAG22/Understanding/visual-presentation.html)). On plum, use
  about 62 characters and 1.6–1.65 line height (judgement, to offset the heavier look of light type).
- **Astigmatism and halation.** Light text on dark is widely reported to blur or glow for readers with
  astigmatism. **Unverified**: no source could be fetched; NN/g's article does not cover it. It is one
  more reason to keep paragraphs on light paper.

---

## 3. Ground kits: the inks for each ground

Every iteration uses these kits. Names follow `styles/surfaces.css` (`--on`, `--on-strong`,
`--on-soft`, `--on-faint`, `--line`, `--line-strong`, `--btn-*`, `--on-accent`, `--focus`). Ratios
are WCAG 2; Lc is APCA.

| | K1 Deep plum | K2 Plum | K3 Powder blue | K4 Pale blue sheet (new surface) | K5 Cream and paper | K6 Oxblood | K7 Project |
|---|---|---|---|---|---|---|---|
| Ground | `#270617` | `#390D26` | `#ABCDD6` | `#C9DFE5` | `#F3F3E7`, `#FBFAF2`, `#F8F5E8` | `#491C17` | `tone.bg` |
| Body text | cream 90% `#DFDBD2` · 13.5 · Lc −84 | cream 90% `#E0DCD4` · 12.2 · Lc −83 | deep plum · 11.1 · Lc 73 (≤ 3 lines) | ink `#241319` · 12.8 · Lc 83 | ink · 15.9 · Lc 97 | cream 90% `#E2DED2` · 10.7 · Lc −83 | `tone.ink` (5.1–12.9 : 1) |
| Headings | cream · 16.7 | cream · 14.9 | plum · 9.9 | plum · 12.0 | plum · 14.9 | cream · 12.9 | `tone.ink` |
| Italic emphasis | powder blue · 11.1 | powder blue · 9.9 | plum (the italic shape carries it) | plum | plum | powder blue · 8.5 | `tone.ink` italic |
| Labels, eyebrows | powder blue (≥ 12 px) or cream | powder blue (≥ 12 px) or cream | oxblood · 8.5, or deep plum | `--blue-ink-soft` · 7.9, or oxblood · 10.4 | ink-soft · 7.3 | powder blue · 8.5 | `tone.ink` |
| Secondary text | cream 78% · 10.3 | cream 78% · 9.4 | `--blue-ink-soft` `#50334A` · 6.5 | `--blue-ink-soft` · 7.9 | ink-soft · 7.3 | cream 78% · 8.4 | `tone.ink` 80% |
| Rules | cream 16% (decorative); cream **40%** for control borders · 3.45 | cream 16%; cream **40%** · 3.36 | deep 18%; deep **50%** · 3.17 | plum 16% ruled lines; oxblood margin rule | plum 16%; plum **50%** for controls | cream 16%; cream 40% · 3.25 | `tone.ink` 20% |
| Primary button | powder-blue pill, deep text · 11.1; hover cream | same | plum pill, cream text · 14.9; hover deep | same as K3 | plum pill, cream text; hover oxblood (today) | powder-blue pill, deep text | cream pill, `tone.bg` text (5.4–14.0 : 1) |
| Secondary button | cream 40% outline, cream text; hover outline blue | same | deep 50% outline, deep text | same as K3 | plum outline (today) | as K1 | `tone.ink` outline |
| Links | cream, 1 px underline offset 3 px; hover blue | same | deep plum underline; hover plum | same as K3 | ink underline; hover oxblood | as K1 | `tone.ink` underline |
| Focus ring | 2 px powder blue · 11.1 | 2 px powder blue · 9.9 | 2 px plum · 9.9 | 2 px plum · 12.0 | 2 px plum · 14.9 | 2 px powder blue · 8.5 | powder blue (3.6–9.3 : 1) |
| Selection | blue ground, deep text | same | plum ground, cream text | same | plum, cream (today) | as K1 | cream, `tone.bg` |
| Shadows | `--shadow-desk` | `--shadow-desk` | `--shadow-paper` | `--shadow-paper` | `--shadow-paper` | `--shadow-desk` | `--shadow-desk` |

**Fixes to today's `surfaces.css`, whichever iteration wins:**
1. `--line-strong` on dark grounds: 34% → 40% where it bounds a field or control (2.77 → 3.36 : 1).
2. `--line-strong` on blue: 36% → 50% for field borders (2.22 → 3.17 : 1); keep 36% for decorative rules.
3. On dark grounds, `--on-faint` (cream 62%: 6.35 : 1 but Lc −48.5) is for large or non-essential
   text only. Small labels use `--on-soft` or `--on`.
4. On blue, `--on-faint` (`#5E4A5E`: 4.75 : 1, Lc 55.6) is large text only; labels use `--on` or `--on-accent`.
5. Add a `blue2` surface (K4) for reading sheets.
6. The footer legal line: cream 60% → 72%.

---

## 4. The five iterations

**Fixed in all five:**
- **Intro**: deep plum, unchanged (first visit only).
- **Footer**: the folder tabs (plum · oxblood · blue · deep) and the wordmark band (deep plum with
  the powder-blue STUDIO / KAVALU, which "sit exactly where and how they are now", client rule 1.4)
  stay. Only the desk's ground changes, in B.
- **Project colours** stay inside their own spread, case-study hero and next-road band.
- **Paper objects keep real colours** (prints, polaroids and strips on `--paper`, notes on
  `--paper-note`). They are most of each iteration's cream.
- **Shared keys.** `founder` and `choose` in `lib/surfaces.ts` serve both the home and the studio
  page, so each iteration gives them one ground.

Targets come from `research/tools/colour_area_model.py`: section heights from the v2 build (home
11,248 px at 1440, studio 6,811, work 3,402, case studies 4,386–7,708) and an estimated composition of
each section. The model reproduces today's home within about 5 points of the measurement (36% against
31% measured). Treat targets as ±5 points until measured.

### 4.1 A · Plum page (plum-dominant, dark first)

**Idea.** One night-coloured album: every page is plum, with deep plum for the album strip, the process
and the footer desk. Blue is the second paper (the service cards, the founder poster, the ticket) and
the emphasis colour (italics, eyebrows, the primary button, the wordmark). Cream appears only where
white paper would: prints, notes, strips, the definition card and the choose-your-road letter.

**Targets.** Site plum **66** · blue **18** · cream **14** · oxblood **2** = **84%**. Home 62 · 19 ·
16 · 3 (81%); work 90%; case study 83%; studio 85%. Ground switches: home 2 (the project spreads),
case study 3, studio 0.

```ts
// lib/surfaces.ts GROUNDS, iteration A
hero: "plum", manifesto: "deep", album: "deep", roads: "plum", founder: "plum", choose: "plum",
studioHero: "plum", studioRoads: "plum", process: "deep", faq: "plum",
work: "plum", case: "plum", start: "plum", notFound: "plum",
```

| Section | Ground | On it | Kit |
|---|---|---|---|
| Intro | deep | as now | K1 |
| Hero | plum | the collage as now; headline cream, italics blue; lead cream 90%; primary pill blue with deep text, secondary cream outline; the blue sticker and tape stay | K2 |
| Two project spreads | project colours, full-bleed | as now, plus a 6–10 px deckled cream edge top and bottom (navy and brown are 1.1 : 1 against plum) | K7 |
| The house view | deep | the statement in cream, the four choices in blue italic; no sheet | K1 |
| Album strip | deep | stamps glow on the dark; captions cream 78%; arrows as cream-outline buttons | K1 |
| Four service cards | plum | all four on blue paper: branding and social on powder blue, identity and film on pale blue | K2; cards K3 / K4 |
| Founder | plum | the blue poster panel; quote cream, italic blue | K2 |
| Choose your road | plum | the ruled cream letter (as now), the brightest paper on the page where the action is | K2; letter K5 |
| Footer | tabs → deep desk → wordmark band | as now | K1 |
| Work index | plum | stamps with paper borders; filter pills cream outline, the active one blue; index table in cream with blue rules | K2 |
| Case study | project hero (with the edge) → plum | overview card becomes cream paper with a clip (oxblood is 1.16 : 1 on plum); text in cream 90% at 62 characters, 1.65 leading; pictures as prints; call-to-action band plum; next road in project colours (with the edge) | K7, K2, K5 |
| Studio | plum and deep | ಕವಲು in cream with the definition in blue italic; the four roads as blue cards (an oxblood band would vanish); process on deep with a blue road line; founder as on home; questions in cream with blue +; the cream letter | K2, K1 |

**Changes to objects:** the oxblood overview card → cream; the studio's oxblood roads band → blue
cards; the cream service cards → blue.

**Why it could win.** The strongest single mood. The footer's signature, blue on deep plum, becomes the
whole site. It is the furthest from her friends' cream-and-serif studios (`BRAND_DESIGN.md` §1.6), and
photographs and stamps glow.

**Risks.** Blue at 18% reads as an accent, not as one of two main colours. 11,000 px of dark.
Case-study reading on dark. Oxblood loses its job. Dark project colours need edges everywhere.

**Look for:** whether the home feels heavy by the album strip; a full case study read on a phone at
half brightness; whether anyone would call blue a main colour.

### 4.2 B · Blue page (blue-dominant, light first)

**Idea.** Swap cream for powder blue as the paper of the whole site. Plum becomes the ink and three
dark moments: the house view, the studio's four roads and the footer's wordmark band. Cream stays
for prints, notes, two service cards and the letter.

**Targets.** Site plum **27** · blue **58** · cream **13** · oxblood **2** = **85%**. Home 28 · 50 ·
19 · 2 (78%); work 91%; case study 87%; studio 84%. Ground switches: home 6, case study 5, studio 5.

```ts
// iteration B (and the footer desk on blue; the wordmark band stays deep)
hero: "blue", manifesto: "deep", album: "blue", roads: "blue", founder: "blue", choose: "blue",
studioHero: "blue", studioRoads: "plum", process: "blue", faq: "blue",
work: "blue", case: "blue", start: "blue", notFound: "blue",
```

| Section | Ground | On it | Kit |
|---|---|---|---|
| Intro | deep | its last frame lifts to reveal blue paper | K1 |
| Hero | blue | headline plum, italics plum (same colour); lead deep plum; plum primary pill (hover deep), deep 50% outline secondary; the sticker → cream with plum ring text; the tape → cream at 62% | K3 |
| Project spreads | project colours, full-bleed | as now; they separate well from blue (navy 9.3 : 1, brown 9.0 : 1) | K7 |
| The house view | deep (the one dark chapter on the page) | statement cream, choices in blue italic | K1 |
| Album strip | blue | stamps keep their shadow (paper on blue is 1.6 : 1); captions deep plum | K3 |
| Service cards | blue | branding and social on cream paper; identity and film as plum cards with cream text and blue italics | K3; K5, K2 |
| Founder | blue | a plum poster (the duotone portrait in plum and blue) | K3; K2 |
| Choose your road | blue | the cream ruled letter | K3; K5 |
| Footer | tabs → blue desk → deep wordmark band | pins on blue; the ticket becomes cream with a plum stub; the contact card stays paper | K3, K1 |
| Work index | blue | stamps; plum pills; the index table in deep plum with deep 18% rules | K3 |
| Case study | project hero → blue | overview as a plum card; reading columns on pale-blue sheets (Lc 84); prints; call-to-action band blue; next road in project colours | K7, K3, K4 |
| Studio | blue, one plum chapter | ಕವಲು in plum; the four roads on plum with cream text, blue italics and blue rules (replacing oxblood); process on blue with a plum road line; founder as on home; questions on a cream sheet; the cream letter | K3, K2, K5 |

**Changes to objects:** everything blue that would sit on blue: the sticker, the tape, the ticket, the
pale-blue cards, the cursor's view disc (→ a plum disc with a cream label) and the focus ring (→ plum).

**Why it could win.** The most comfortable reading. Warm work pops on the cool blue. It is the
closest to today's light site, so the smallest change for the client.

**Risks.** Blue stops being the precious accent and its objects must be recoloured. The brand's
signature (blue on plum) shrinks to three moments. A pastel page reads more like a lifestyle brand
(Fishwife, Noomo) than a studio. Six switches on the home page. Light-on-light objects need shadows.

**Look for:** whether it still looks like Kavalu with the logo covered; whether the stickers and
tickets lose their charm in cream.

### 4.3 C · Alternating chapters (an even split, full-bleed)

**Idea.** Classic colour blocking: full-bleed plum and blue sections alternate down every page and
the inks flip with each one. On the home page the two colours are nearly even. Its site proportion
matches E, so C against E compares rhythm alone.

**Targets.** Site plum **49** · blue **36** · cream **12** · oxblood **3** = **85%**. Home 45 · 34 ·
19 · 2 (79%); work 91%; case study 86%; studio 87%. Ground switches: home **7**, case study 4,
studio 5.

```ts
// iteration C (case studies add a "caseChapter" key, plum, for picture chapters)
hero: "plum", manifesto: "blue", album: "deep", roads: "blue", founder: "plum", choose: "blue",
studioHero: "blue", studioRoads: "plum", process: "blue", faq: "blue",
work: "blue", case: "blue", start: "blue", notFound: "plum",
```

| Section | Ground | On it | Kit |
|---|---|---|---|
| Intro | deep | as now | K1 |
| Hero | plum | as in A | K2 |
| Project spreads | project colours | with the edge where they meet plum | K7 |
| The house view | blue | statement in deep plum, italics plum | K3 |
| Album strip | deep | as in A | K1 |
| Service cards | blue | two cream cards, two plum cards | K3; K5, K2 |
| Founder | plum | the blue poster | K2 |
| Choose your road | blue | the cream letter | K3; K5 |
| Footer | deep | as now | K1 |
| Work index | blue | stamps; plum pills | K3 |
| Case study | project hero → blue | overview as a plum card on blue; then chapters alternate: text on blue, pictures on a plum band; call-to-action band plum; next road | K7, K3, K2 |
| Studio | alternating | ಕವಲು on blue → the four roads on plum → process on blue → founder on plum → questions on blue → the letter on blue | K3, K2 |

**Changes to objects:** stickers, tape and tickets take the opposite colour of whatever ground they
land on; the cursor and focus ring flip at every section.

**Why it could win.** Energy; each section gets its own identity; both colours read as equal.

**Risks.** No dominant colour, so it reads undecided. Seven jumps between L\* 11 and L\* 80 on the
home page is the zebra pitfall. Buttons, header, cursor and focus ring flip constantly. It is the
furthest from "subtle" (client rule 1.1).

**Look for:** whether scrolling feels like a slideshow; whether the colours still feel like a brand.

### 4.4 D · Plum desk, blue sheets (one ground with large blue blocks)

**Idea.** The whole site is the studio's desk: one plum ground (deep plum for the album strip, the
process and the footer) that never changes. Everything to be read is a large paper sheet laid on it:
powder blue for the house view and the studio's definition, pale blue for questions and case-study
text, cream for the letter. Pictures sit straight on the desk as prints. Her projects become large
mounted sheets in their own colours instead of full-bleed bands. The page alternates between "on the
desk" (dark, image-led) and "on a sheet" (light, text-led) without ever changing its ground.

**Targets.** Site plum **56** · blue **29** · cream **12** · oxblood **3** = **85%**. Home 57 · 25 ·
15 · 3 (82%); work 90%; case study 87%; studio 85%. Ground switches: home **0**, case study 3 (the
project hero and next road), studio 0. On a phone the sheets fill the width, so expect blue to read
3–6 points higher there (estimate).

```ts
// iteration D: every ground is plum or deep ...
hero: "plum", manifesto: "plum", album: "deep", roads: "plum", founder: "plum", choose: "plum",
studioHero: "plum", studioRoads: "plum", process: "deep", faq: "plum",
work: "plum", case: "plum", start: "plum", notFound: "plum",
// ... and a new sheet layer (a paper element with its own data-surface, tone and shadow)
export const SHEETS = {
  manifesto: "blue",    // the house view on a large powder-blue sheet
  studioHero: "blue",   // the dictionary entry for ಕವಲು
  faq: "blue2",         // questions (reading)
  caseText: "blue2",    // case-study text blocks (reading)
  caseOverview: "blue", // the overview card
  workIndex: "blue",    // the Index view's table
  choose: "cream",      // the letter: the brightest paper marks the action
  start: "cream",
} as const;
```

| Section | Ground | On it | Kit |
|---|---|---|---|
| Intro | deep | lands on the same desk, so the stamp settles where the hero begins | K1 |
| Hero | plum | the collage; headline cream with blue italics; blue primary pill | K2 |
| Project spreads | plum (no full-bleed band) | each project as a large mounted sheet (content width, about 92vw) in its own colours, with a cream paper border; its prints and title inside as now | K2; sheet K7 |
| The house view | plum | a large powder-blue sheet, about 80% wide, a deckled top edge and two strips of cream tape; the statement in deep plum Gambetta, the four choices in plum italic; the sheet stays straight (type does not tilt) | K2; sheet K3 |
| Album strip | deep | stamps glow on the desk | K1 |
| Four service cards | plum | four blue cards on the desk, powder blue and pale blue alternating, deep ink | K2; cards K3 / K4 |
| Founder | plum | the blue poster on the desk | K2; poster K3 |
| Choose your road | plum | the cream ruled letter | K2; letter K5 |
| Footer | tabs → deep desk → wordmark band | the desk continues the page; the folder tabs mark the arrival | K1 |
| Work index | plum | the stamps grid on the desk; the Index view on a blue sheet | K2; K3 |
| Case study | project hero (full-bleed, with a paper edge) → plum desk | overview as a blue card with a clip; text blocks on pale-blue sheets (Lc 84); pictures as prints on the desk; call-to-action band on plum; next road in project colours (with the edge) | K7, K2, K3, K4 |
| Studio | plum and deep | ಕವಲು on a blue sheet; the four roads as blue cards; process on deep with a blue road line; founder as on home; questions on a pale-blue sheet; the cream letter | K2, K1, K3, K4, K5 |

**Changes to objects:** a new sheet component (a straight paper panel, deckled or torn top edge,
tape, `--shadow-desk`, its own `data-surface` and `data-tone`, so the header and cursor read it as
light); the spreads as mounted project sheets; the overview card blue; the oxblood roads band as
blue cards.

**Why it could win.** One ground, many papers. See §5.

**Risks.** A dark first screen. A new component to build. Mounted project sheets are a little less
immersive than full-bleed bands, so make them large.

**Look for:** whether the blue sheets feel like paper on a desk rather than boxes on a dark page
(edges, tape, shadow, slight overlap); whether the home still feels spacious; how the spreads compare
mounted and full-bleed.

### 4.5 E · Two roads (blue first, then plum)

**Idea.** Kavalu is a crossroads, "a point where paths meet, split, and become something new". Each
page starts on powder blue and turns to plum once, at a junction. On the home page the junction is
inside the house view: "A brand is a set of choices;" sits on blue, and as you scroll a plum sheet
rises like a turning page so that "what it says, how it looks, where it shows up, who it speaks to"
lands on plum. Everything after it is on the desk.

**Targets.** Site plum **49** · blue **37** · cream **12** · oxblood **2** = **86%**. Home 51 · 30 ·
16 · 3 (82%); work 91%; case study 87%; studio 85%. Ground switches: home 3 (the spreads and the
junction), case study 4, studio 1.

```ts
// iteration E ("junction" = a blue ground with a plum sheet that turns over it on scroll)
hero: "blue", manifesto: "blue" /* junction */, album: "deep", roads: "plum", founder: "plum", choose: "plum",
studioHero: "blue", studioRoads: "blue", process: "blue" /* junction */, faq: "plum",
work: "blue", case: "blue", start: "blue", notFound: "blue",
// case studies: the call-to-action band is the junction (plum), then the next road and the footer
```

| Section | Ground | On it | Kit |
|---|---|---|---|
| Intro | deep | its last frame lifts to reveal blue paper | K1 |
| Hero | blue | as in B | K3 |
| Project spreads | project colours | as now | K7 |
| The house view | blue → plum (the junction) | as above; the turn is a sheet sliding, never a fade | K3 → K2 |
| Album strip | deep | stamps glow | K1 |
| Service cards | plum | four blue cards | K2; K3 / K4 |
| Founder | plum | the blue poster | K2 |
| Choose your road | plum | the cream letter | K2; K5 |
| Footer | deep | as now | K1 |
| Work index | blue | stamps; this short page turns at the footer | K3 |
| Case study | project hero → blue | overview as a plum card and the text on blue (reading in daylight); the call-to-action band is plum (the junction); next road; footer | K7, K3, K4, K2 |
| Studio | blue → plum | ಕವಲು and the four roads on blue (the roads as plum cards); the process line is the junction, drawn from blue into plum; founder, questions and the letter on plum | K3 → K2 |

**Changes to objects:** in the blue half, as B (cream sticker and tape, plum focus ring); in the plum
half, as D (blue cards, paper edges).

**Why it could win.** It tells the brand's own story (day into evening; the road that splits). Its
first screen is friendly and the first half reads comfortably. The blue-on-plum signature carries
the second half. Only three switches.

**Risks.** Two halves can feel like two sites if the junction is not designed with care. Every page
needs its junction placed. Both halves' object changes apply.

**Look for:** whether the junction feels meaningful or arbitrary; whether visitors who stop halfway
ever see plum.

---

## 5. Recommendation

### 5.1 Ranking

**1 · D, Plum desk with blue sheets.** The reasons a senior brand designer would give:
1. **Commit to one ground.** Dominance reads as confidence, and an even split reads as indecision
   (§2.1). D has a single ground and no stripes, which is the calmest rhythm of the five (0 switches on
   the home page) and the most in keeping with "subtle, elegant" and "spacious, never cluttered"
   (client rules 1.1 and 1.9).
2. **Both colours are main colours.** Blue holds 29% of the site in a few large pieces, enough to read
   as one of two main colours, which A's 18% is not. Because the plum ground is continuous, plum
   still leads (§2.3.1).
3. **Value before hue, and reading on light.** Long text sits on pale blue (Lc 84) or cream (Lc 97);
   plum carries display type and pictures. This is the NN/g and APCA advice applied (§2.4).
4. **The brightest paper marks the action.** The cream letter (choose your road, the onboarding form)
   is the lightest object on a dark desk, so the eye goes to it.
5. **The scrapbook becomes literal.** Papers on a desk, lighter sheets above a darker ground (NN/g's
   layering advice), and "What we pin above the desk" already lives in the footer. Hicard's Scrapbook
   (a pale-aqua print on a dark page) shows the effect.
6. **The signature runs everywhere.** The powder-blue wordmark on deep plum, the strongest image of
   both her old site and this one, becomes the language of every page rather than a finale.
7. **Distinct in its category.** 5 of 226 captured sites open on a coloured dark ground; none on plum.
   It also moves furthest from her friends' cream studios.
8. **Her work stays mounted.** Every project gets the paper edge that plum demands (§2.3.4), which
   is also the scrapbook's own rule (one mount per picture).
9. **The audience argument.** A young studio benefits from a dominant signature pair at the high end
   of the range (Texas A&M's 75% for unfamiliar audiences).

**2 · E, Two roads.** The best alternative, and the one to fall back on if D's dark first screen
proves too heavy in testing. It has the same proportion as C but in two calm fields, a junction that
means something, and comfortable reading in its first half. Ranked below D because it is harder to
build well and its blue half loses blue's accent role.

**3 · B, Blue page.** The safest option: comfortable, close to today's site, and good for her warm
work. Ranked third because blue stops being precious, the brand's signature shrinks to three moments,
and a pastel page reads more lifestyle than studio.

**4 · A, Plum page.** The boldest mood, and it shows what full commitment to plum feels like. Ranked
fourth because blue at 18% under-delivers "both" main colours and it asks for long reading on dark.
If the client loves A, D gives her that mood with comfortable reading.

**5 · C, Alternating chapters.** Worth building only to confirm the principle. Seven full-bleed jumps
and no dominant colour make it the noisiest and least elegant of the five.

### 5.2 Round 2: turn the dial on the winner

Round 1 holds every iteration at 83–86% so that the comparison is about arrangement. Round 2 builds
the winner at three totals by moving named surfaces (estimates from `colour_area_model.py`):

| Variant | What moves | Site share (plum · blue · cream · oxblood) | Plum+blue |
|---|---|---|---|
| **D-75**, warmer | the house-view sheet and the questions sheet become cream paper; the case overview a cream card; case text on paper | 56 · 19 · 21 · 4 | **75%** |
| **D-85**, as specified | – | 56 · 29 · 12 · 3 | **85%** |
| **D-90**, cooler and purer | the letter on pale-blue ruled paper with an oxblood margin; notes and the definition card on blue paper; only prints and strips stay cream | 56 · 34 · 7 · 3 | **90%** |

Expected outcome (judgement): D-85. D-75 brings back the cream look of her friends' studios; D-90
loses the bright letter that marks the action. If E wins round 1, dial it the same way (cream
letter ↔ pale-blue letter; cream ↔ blue reading sheets).

### 5.3 What would change the ranking
- **The hi-res images (Q21).** If her photographs look dull on plum, E or B moves up.
- **Ananya's taste.** If she wants light, run E against B; if dark, D against A.
- **Mobile.** If a dark first screen reads badly on phones outdoors, E moves up.

---

## 6. Measuring the real coverage

**Tool:** `research/tools/colour_coverage.py` (tested on the v2 captures and her live site, §1.4).

1. **Build each iteration as a switch**: one `GROUNDS` map (and `SHEETS` for D) per iteration in
   `lib/surfaces.ts`, chosen by an environment variable or a query parameter, so that all five run from
   one build and nothing else differs.
2. **Capture full pages** of `/`, `/work`, `/studio` and the three case studies at 1440 × 900 and
   390 × 844, at device scale 2, with reduced motion on (so pieces are at rest and the intro is skipped),
   after one slow scroll to the bottom and back (lazy images and reveals).
   - With the dev server down, use the production build through `research/tools/preview.py`.
   - Use `Page.captureScreenshot` with `captureBeyondViewport` and the full content size. If pinned
     or smooth-scrolled content draws wrongly, stitch viewport shots taken every 900 px, with the
     header hidden after the first.
3. **Collect masks in the same session**, at scroll 0, with the snippet in the tool's docstring: the
   rectangles of `img`, `video`, `canvas` and `picture` (photos, left out of the denominator) and of
   elements styled with `--p-bg` (project colours, reported apart). Save them as
   `masks.json`, keyed by screenshot file name.
4. **Measure:**
   ```bash
   python -I research/tools/colour_coverage.py --masks masks.json --scale 2 --viewport 900 \
     --strip D-home-1440.png --json D-home-1440.json D-home-1440.png
   ```
   It matches each 4 × 4 block (removing the paper grain) to the nearest token in CIELAB, rolls tokens
   up into plum, blue, cream, oxblood, project and unassigned, and reports:
   - each family's share of the non-photo area;
   - the **palette share** (photos and project colours out), the Q24 target;
   - ground switches (runs of at least half a viewport);
   - a scroll strip PNG: one row per 40 px, coloured by the dominant family, so rhythm can be seen.
   Pass all pages of one iteration together for the site figure.
5. **Check the unassigned share.** Outside photos it should stay under about 3%. More means a colour
   outside the palette has crept in (a hover wash, a blend, a gradient); find it.
6. **Squint test.** Blur each full-page shot (Gaussian radius about 20 px), view it at thumbnail size
   and put the five side by side. The ground should be obvious at a glance
   ([University at Buffalo](https://www.buffalo.edu/brand/creative/color/color-ratios.html)).
7. **Contrast audit.** Run `research/tools/uniformity_audit.py` on each iteration. Every text node's
   colour and ground must be a pair from §3, and every field border must reach 3 : 1.
8. **Real conditions.** Look at each on a phone outdoors at half brightness and on a laptop at night,
   and read one whole case study on each.
9. **Record and decide.** One table per iteration:

   | Page · width | Plum | Blue | Cream | Oxblood | Plum+blue | Project | Unassigned | Switches |
   |---|---|---|---|---|---|---|---|---|

   An iteration passes when every page (not only the average) lands within 70–90%, there are no
   unapproved text pairs, the home page has at most four switches, and Ananya prefers it. Then run
   round 2 (§5.2) on the winner and record the result in `BRAND_DESIGN.md` §4.5.

---

## 7. Limits and unverified points
- **Search budget.** The session's shared web-search budget ran out early in this work. The
  remaining research used direct fetches of known pages and the project's 226 captured sites.
  Real-site examples therefore come mostly from the captures (three screens per site, 23 Oct 2026),
  not from whole pages.
- **Overlays.** Ghia's and Fishwife's captures show welcome overlays; their measured grounds are the
  overlay's.
- **Estimates.** Section heights and compositions in `colour_area_model.py` are estimates (calibrated
  within about 5 points against today's measured home page). The real figures come from §6.
- **Baseline captures.** The §1.4 baseline uses six viewport samples per page without photo masks, so
  photos fall partly into "unassigned" and partly into the nearest palette colour.
- **Unverified:** the origin of the 60-30-10 rule; halation for readers with astigmatism. Both are
  marked where they appear.
- **APCA** is a draft (the WCAG 3 candidate); WCAG 2.2 remains the standard to pass.
- **Judgement, not fact:** the feel of each split (§2.1), the switch guidance (§2.3.6), type weights on
  plum (§2.3.3) and the ranking (§5). Each is labelled.

---

## 8. Sources

**Proportion and brand guidelines**
- Mintos brand, colour: https://brand.mintos.com/color
- Pixpa, the 60-30-10 rule in web design: https://www.pixpa.com/blog/60-30-10-rule-in-web-design
- Texas A&M, brand colours and ratios: https://marcomm.tamu.edu/creative-platform/visual-style/brand-colors
- University of Chicago, colour system: https://creative.uchicago.edu/color-system
- Colt, colours: https://docs.colt.net/brand/visual-system/colours
- University at Buffalo, colour ratios: https://www.buffalo.edu/brand/creative/color/color-ratios.html
- University of Wollongong, colour: https://www.uow.edu.au/brand/brand-system/colour/
- National Wildlife Federation, colour proportions: https://brandguide.nwf.org/brand-palette/color-proportions/
- Designit, colour palette: https://designit.com/brand/guidelines/introduction/colour-palette
- Mailchimp, brand assets: https://mailchimp.com/about/brand-assets/
- Pentagram, Slack: https://www.pentagram.com/work/slack
- Tiffany Blue: https://en.wikipedia.org/wiki/Tiffany_Blue
- Aston Villa F.C. (claret and blue): https://en.wikipedia.org/wiki/Aston_Villa_F.C.

**Perception, presentation and dark interfaces**
- Figure–ground perception: https://en.wikipedia.org/wiki/Figure%E2%80%93ground_(perception)
- Josef Albers, Interaction of Color: https://en.wikipedia.org/wiki/Josef_Albers
- Irradiation illusion: https://en.wikipedia.org/wiki/Irradiation_illusion
- Colour banding: https://en.wikipedia.org/wiki/Colour_banding
- NN/g, Dark mode vs light mode: https://www.nngroup.com/articles/dark-mode/
- NN/g, Dark mode issues: https://www.nngroup.com/articles/dark-mode-users-issues/
- web.dev, prefers-color-scheme: https://web.dev/articles/prefers-color-scheme

**Accessibility**
- WCAG 2.2, SC 1.4.3 Contrast (Minimum): https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html
- WCAG 2.2, SC 1.4.11 Non-text Contrast: https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html
- WCAG 2.2, SC 1.4.8 Visual Presentation: https://www.w3.org/WAI/WCAG22/Understanding/visual-presentation.html
- APCA in a Nutshell: https://git.apcacontrast.com/documentation/APCA_in_a_Nutshell.html

**Sites (captured 23 Oct 2026 in `research/screens/`)**
- Ghia https://drinkghia.com · Bruno Simon https://bruno-simon.com · Fishwife https://eatfishwife.com
- Noomo https://noomoagency.com/ · Chrissie Abbott https://chrissieabbott.com/ · Robot Food https://www.robot-food.com/
- Pearlfisher https://www.pearlfisher.com · Katrine Mehl https://katrinemehl.com/ · Hicard Studio Scrapbook https://scrapbook.hicard.studio/
- Happy Happy Creative https://www.happyhappycreative.com/ · Agence Foudre https://www.agencefoudre.com/ · Bielke&Yang https://bielkeyang.com/
- Fiddle.Digital https://fiddle.digital/ · Order https://order.design/ · Base Design https://www.basedesign.com
- Graza https://www.graza.co · Good Earth https://www.goodearth.in · Studio Sorted https://www.studiosorted.com/

**Project files**
- `kavalu_instructions.md` (brief 4, the rules), `BRAND_DESIGN.md` §1.4, §1.6, §4, §6
- `website/src/lib/surfaces.ts`, `website/src/styles/surfaces.css`, `website/src/styles/tokens.css` (read only)
- `research/type/TYPE_REVIEW.md`, `research/reference_sites.json`, `research/SOURCES.md`
- `research/tools/colour_coverage.py` and `research/tools/colour_area_model.py` (new)
