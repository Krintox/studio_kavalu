# Studio Kavalu — instructions and rules

**Read this file first, every time.** It holds every rule the client (the user, for his friend
Ananya) has given for the Studio Kavalu website. These rules override any default, any skill and
any earlier decision. When a rule here conflicts with something already built, the build changes.

- Project folder: `C:\shashank\shashank\fnf\ananya_residency\studio_kavalu`
- Site code: `website/` · Research: `research/` · Brand design doc: `BRAND_DESIGN.md`
- Sources of every reference: `research/SOURCES.md`

---

## 1. Rules (from the client, grouped)

### 1.1 What the site is
- A **website redesign** for **Studio Kavalu by Ananya**, a design studio: "a branding and content
  house". The existing design exists but "we don't like it".
- It must be a **proper global, professional-level brand website for a design studio**, "everything a
  design studio website should look like in 2026/27": **subtle, elegant, aesthetic**.
- Work as a **design-studio website designer with 10–15 years of experience**. "Make sure that it is
  really good."
- **Do not make it look like AI slop.**
- **Do not make it like her friends' studios** (Studio Number Seven, Studio Sorted), even though "that
  is how studio websites are".

### 1.2 Brand inputs (fixed)
- **Keep the colour palette the same as now**: cream `#F3F3E7`, oxblood `#491C17`, plum `#390D26`,
  deep plum `#270617`, powder blue `#ABCDD6` (sampled from her current site).
- **The brand line**, as given: "A brand is a set of choices; what it says, how it looks, where it shows
  up, who it speaks to. Studio Kavalu is a branding and content house that makes these choices with
  you. We shape brands, feeds and persona through a design lens backed with strategy. The aim- work with
  a point of view clear enough that people recognise it, and others follow it."
- **The wordmark font is the one she gave**: the heavy, wide STUDIO / KAVALU lettering of her current
  site (custom K whose arm curves like a road). *Not* a substitute that "looks close" (Panchang was
  rejected as "really bad").
- **The proportion (brief 5, replacing brief 4's 70–90% plum and blue):** "the current website has
  too much plum".
  - **Plum about 20%**; **cream and powder blue together 50–60%**; the remaining colours take the rest.
  - **The hero and the first sections must not have much plum**: they open on light paper.
  - "Plum" means the plum family: plum `#390D26` and deep plum `#270617`.
  - Found, as before, by testing arrangements in the real site and measuring them.
- *Brief 4 (superseded by brief 5):* plum and powder blue as the main colours at 70–90% of the
  website. Built as "the desk" on 24 Oct and judged too plum by the client.

### 1.3 Projects and the scrapbook
- **Her projects need more visibility**: most of her work is visual.
- **Analyse her projects** to understand what kind of work she does.
- **The scrapbook is the format of the website, not a page.** "The project format … should look like a
  scrapbook. The website idea should be like a scrapbook." **No separate scrapbook page.**
- **Never show the reference pictures as content.** The reference images the client gave are
  inspiration for the look, not material to publish (they are other people's work).
- She will share a **list of projects with notes**, **reference videos** and a **folder of scrapbook
  references** (still pending — use them when they arrive).
- **The hero's scroll scene** (brief 6, refining brief 3): as you scroll, **all the hero's images merge
  into the centre image, it expands, and the next section appears from it**, as the first version did.
  **Scrolling back up must scatter every image back** to the full collage, never leave just one.
  It must be really smooth.
- **Images must be high quality** (brief 3): regenerate **the same images** at high quality, never
  different ones, with ChatGPT image generation in the persistent browser (`/converse-with-gpt`). If the
  GPT limit is reached, **recreate the image in HTML/code and screenshot it**.
- **"Right now the images are really bad"** (brief 6): download every image already generated in the
  ChatGPT chats (6–7 of them), generate more with ChatGPT **or Gemini**, and replace the site's images
  with good, high-quality ones.

### 1.4 Motion
- **Good, subtle and smooth scroll animations**: zoom in, zoom out, expand, and any other animations that
  suit the site. **Keep the existing animations**; add subtle motion design where it helps.
- **Footer wordmark**: when scrolling to the footer, **"STUDIO" comes in from the left and "KAVALU"
  from the right**, and they then **sit exactly where and how they are now**.
- **More motion graphics in the footer** if possible.
- **"What we pin above the desk" goes in the footer** (Ananya's wish; how is for us to work out and
  research).
- **Motion design references must be real and researched**: look at how the researched websites do
  motion; use the persistent browser to **capture frame-by-frame screenshots** (as close together as
  possible) to see how a motion is made. "Not some random motion design."
- Tech references welcome: **21st.dev, React Bits** and similar libraries.
- **An intro before the hero, like a Marvel studio intro** (brief 3, reference https://www.nvmbr.in/):
  - her photos come one after another, very fast;
  - they zoom out;
  - the name appears;
  - then the current hero, which stays.
- **The intro, refined** (brief 6):
  - it plays **every time the home page loads, refresh included** (not only the first visit);
  - its colours **match the landing page** (not plum);
  - the transition into the hero must be smooth: the reel **becomes less opaque and merges into the
    background**, staying on as **a very light, low-opacity moving background of the hero**; the hero
    itself stays as it is.
- **"The house view"** ("A brand is a set of choices; what it says, how it looks, where it shows up, who
  it speaks to."): remove the current way of representing it, research how to represent it properly,
  and give it good, subtle motion design ("not some slop"). (brief 3)
- **Everything smooth and subtle**, the scroll and everything else; **subtle smooth transition and
  scroll animations only**. (brief 3)
- **Parallax** as well. (brief 3)
- **Proper, professional, really smooth scroll and parallax effects** across the site, "not just some
  formality" (brief 6).
- **Cursor design**: a designed cursor in general and on hover, and **the cursor changes on specific
  sections**. (brief 3)

### 1.5 Typography
- **Keep the fonts good.** Use the references to decide which fonts suit work like this.
- **Keep the design sense the same throughout the website** (one consistent system).
- **"This font is not good"** (brief 3), after v2's Gambetta / Switzer / Courier Prime:
  - make a **list of fonts used by studios all over the world**;
  - write **a doc of which type of font to use for which type of project/company website**
    (`research/type/FONT_GUIDE.md`);
  - research the fonts properly before choosing again.

### 1.6 Onboarding
- **Instant client onboarding**: someone who likes the work can start a project immediately.
- **The Close button on the project request must work** (reported broken in brief 3).

### 1.7 Research and documentation
- **Research properly** how studio websites are designed: **at least 100–150 website references**.
- Research the brand's **online presence**.
- Use the **persistent browser** (CDP on port 9333) for anything web search can't give (images, frames).
- **All scraped and ideated website sources go in a separate file with links** → `research/SOURCES.md`.
- **A proper, in-depth brand design doc** (Markdown) covering the full design sense and everything that is
  uniform across the site → `BRAND_DESIGN.md`. Research how such brand documents are made first.
- **This file** (`kavalu_instructions.md`) holds all the rules. It is a priority task. "Store everything
  there."
- **Research before every decision** (brief 3): see how top brand designers and web designers build
  websites for a brand with good design sense, and add whatever is relevant and useful to this file and
  to `BRAND_DESIGN.md`.

### 1.8 Working method
- **Use `/loop` for each task** and keep prompting yourself until the work is done.
- Standing rules from the client's global setup: never commit or push to git unless asked in the
  current message; persistent-browser etiquette (one dedicated tab, never close the user's tabs, never
  type passwords, skip bot walls).

### 1.9 Space, surfaces and quality (brief 3)
- **Spacious, never cluttered.** Every section has proper breathing space; no cluttered sections at all.
- **Backgrounds are textures, not solid colours.**
- **Responsive everywhere.**
- **Match everything to the brand theme. Really professional, really high quality.**

---

## 2. Decisions taken under these rules (and why)

| Decision | Rule it serves |
|---|---|
| Concept "the crossroads album": every project is a stamp/print in an album; spreads, tape, clips, labels, hand notes | 1.3 scrapbook is the format |
| Palette locked to the five hex values above; project colours only inside a project's own spread | 1.2 |
| Reference images removed from the site entirely; scrapbook material = her own work, palettes, notes | 1.3 |
| `/scrapbook` page removed; its desk becomes the footer pinboard | 1.3, 1.4 |
| Wordmark rebuilt from her current lettering (font identified from her site, custom K redrawn) | 1.2 |
| Every motion has a reduced-motion version; one auto-moving thing per screen, pausable | 1.4 subtle, 1.1 not slop |
| Type: her lettering as the wordmark; Gambetta (display), Switzer (text), Courier Prime (typed labels), Homemade Apple (notes), Anek Kannada. Fraunces, Ranade and Plex Mono dropped. Evidence in `research/type/TYPE_REVIEW.md` | 1.5 fonts from the references, 1.1 not slop |
| Every section stands on a named ground (`data-surface`: cream, blue, plum, deep, oxblood) set from one table, `website/src/lib/surfaces.ts`. Its text, rules, buttons, focus ring and selection take that ground's inks (`styles/surfaces.css`); paper objects keep their own. So the plum/blue proportion is changed in one place and every page follows | 1.2 plum + blue 70–90%, 1.5 one consistent system |
| **Light paper, plum as ink** (brief 5, replacing the desk below): the page opens on cream; her prints on powder-blue spreads; the torn cream house-view sheet; the album strip as the one plum chapter; the founder on oxblood; the letter on blue; the footer's deep-plum desk; each case study opens in its project's own colours. Measured plum 21%, cream and blue 62% | brief 5 |
| *(superseded by brief 5)* **The site is her desk** (brief 4): one plum ground that never changes (deep plum where the work is shown); everything to be read is a large powder-blue or pale-blue sheet laid on it (the house view, the four roads, the studio's definition and process, the questions, case-study text); pictures sit on the desk as prints; the cream letter is the brightest paper, so the eye goes to the action; powder-blue italics on plum are the signature. Chosen over nine other arrangements rendered and measured on the real site; the colour research ranked it first, and an arrangement that alternated plum and blue at every section read as stripes | 1.2 plum + blue 70–90%, 1.1 subtle and elegant, 1.9 spacious |
| Each ground is its own sheet of paper: a seamless texture with the colour baked in (`research/textures_v3`, within dE 0.1 of the flat colour, so contrast holds). A soft-light grain over plum was tried and rejected: it lifted plum to a bright magenta | 1.9 textures not flat, 1.2 palette fixed |
| The intro's fast cuts are a plum duotone (luminance 0.006–0.098), and only the last picture develops into colour: full-colour cuts at 50–240 ms would fail WCAG 2.3.1 (flashing). No intro under reduced motion or Save-Data | 1.4 the Marvel-like intro, 1.1 professional |
| The house view becomes the index of the four roads: a still sentence whose four choices are links with hand-drawn roads, typed footnote numbers and one print in the margin on hover (research proposal A). The ink-in words and the inline pictures are dropped: both are now stock components | 1.4 the house view, 1.1 not slop |
| The cursor's dot is exact, and what a click does is said on a small typed paper tag beside the pointer, not on a disc laid over the work; the system cursor stays in forced-colours mode | 1.4 cursor, 1.1 not slop |
| Type v3: Schibsted Grotesk does every reading job; the typewriter only on typed paper; her hand for notes and the signature; no italic or coloured word in headings and no eyebrow over every heading (both recognised marks of a generated page); six display steps. Set against two other complete systems in the real site before choosing | 1.5 "this font is not good", 1.1 not slop |

---

## 3. Work queue (the `/loop` runs through this, top to bottom)

- [x] **Q1 — This instructions file.** Rules from both briefs, verbatim copies in the appendix.
- [x] **Q2 — Sources file** `research/SOURCES.md`: every site captured (226) with links, grouped, with
      what was taken from each; plus motion, onboarding, font and image sources.
      → Done: 226 sites in 7 buckets with link, detected stack and notes; an "idea → sources" table;
      brand, motion (catalog §9), onboarding (§8) and font sources. Regenerate with
      `scratchpad/make_sources.py` (copied to `research/tools/`) when sources are added.
- [x] **Q3 — Wordmark font**: identify her current site's STUDIO / KAVALU face by side-by-side tests in the
      browser; rebuild the wordmark (incl. the custom curved K); use it in the footer and the header logo.
      → Done: no free font matched her lettering (best IoU 0.80, Panchang rejected), so her own STUDIO /
      KAVALU and mark were traced and refitted as SVG glyphs (A 0.994, S 0.974 IoU; shared cap line and
      baseline). `components/brand/Wordmark.tsx` (+ generated `wordmark-paths.ts`) now draws the nav lockup,
      footer wordmark, favicon and envelope stamp. Panchang removed. Work in `research/brand/wordmark_fit/`.
- [x] **Q4 — Footer v2**: STUDIO slides in from the left, KAVALU from the right, settling where they are
      now; more (subtle) motion graphics; "What we pin above the desk" moved into the footer as a
      pinboard of her own material (research how footers do this first).
      → Done after studying 24 footers frame by frame (`research/motion_frames/footers/`): letters scrub in
      from both sides and land at rest (verified S −1812→7, U 3076→1186). The desk is the footer: working
      ticket / contact card / index, her pins, a dotted road that forks down to ಕವಲು, a postmark press,
      drag + cursor depth on desktop, and a swipe strip on phones. Checked at 1440 / 820 / 390 and with
      reduced motion; no sideways overflow; the nav gets a deep-plum sheet over dark sections.
- [x] **Q5 — Scrapbook as the site format**: delete the `/scrapbook` page and every link to it; remove
      the reference images from the site; make the project format (spreads, case studies, work index)
      read as scrapbook pages, consistently.
      → Done: `/scrapbook`, its desk and every link to it are gone (`/scrapbook` 404s; sitemap updated);
      `public/` holds only her four projects and our generated textures. A crawl resolved every link
      and all 309 image URLs. Case studies mount pictures as taped, cornered or clipped prints with
      typed captions, checked on the built site at 1440 and 390 px (`research/working-shots/v2/`).
- [x] **Q6 — Type system review**: research font pairings in the references and the strongest captured
      sites; set one consistent, non-generic system that includes the wordmark face.
      → Done: Gambetta / Switzer / Courier Prime around her wordmark, chosen from the 8 references, her
      current site, a 226-site census and in-browser specimens (`research/type/TYPE_REVIEW.md`).
      Checked on every page at desktop, mobile and reduced motion: no overflow, no font gaps (₹ falls
      to Anek Kannada; the sticker ring was refitted to the wider Courier).
- [x] **Q7 — Motion design research + additions**: record frame sequences of motion on the best
      researched sites in the persistent browser, analyse how each is made, and add the ones that fit
      (subtle), keeping existing animations.
      → Done: frame-by-frame studies of 4 more sites (`research/motion_frames/sites/NOTES.md`), with the
      browser's own animation timings. Added `lib/handmade.ts`: her hand notes write themselves in
      (word by word, pen speed; the hero hint's arrow is drawn last) and typed captions type on
      (24 ms a letter). Both run once, put the markup back, and are off under reduced motion.
      Measured per frame on the built site.
- [x] **Q8 — Brand design doc** `BRAND_DESIGN.md`: research how brand guidelines / design-system docs are
      structured; write the full, in-depth design sense of the site.
      → Done: structure taken from the NASA 1975 manual, FHDA 2026 guidelines, GitHub's brand toolkit,
      IBM Carbon motion and Atlassian foundations. 17 chapters: brand, voice, logo (construction,
      clear space, minimum size, misuse), colour (contrast-checked pairs), type, the scrapbook kit,
      imagery, layout, motion (tokens, vocabulary, reduced motion), components, onboarding,
      accessibility, applications, a uniformity checklist and a code map. Written from a full
      inventory of the code.
- [x] **Q9 — Consistency pass**: audit every page against `BRAND_DESIGN.md`; fix every deviation.
      → Done: every deviation the code inventory found was fixed. Colours, the type ladder, labels,
      shadows, pills (two sizes), breakpoints (1099 / 899 / 639) and durations now come from tokens
      (`research/tools/consistency_pass.py`). Also fixed:
        - the mobile menu now traps focus like the drawer;
        - focus is blue on every dark section and plum on light cards;
        - project colours renamed `--p-bg` / `--p-ink` (they were shadowing `--ink`);
        - duplicate sticker id; snapshot links; reduced-motion gaps;
        - copy read from `content/site.ts`.
      Audited with computed styles on every page (`uniformity_audit.py`); the only differences left
      are documented exceptions.
- [x] **Q10 — Final checks**: type check, production build, browser checks (desktop, mobile, reduced
      motion, onboarding flow end to end); update README, research report and notes; report back.
      → Done:
        - tsc and `next build` pass (15 pages);
        - every page checked at 1440 and 390 px and with reduced motion: no errors, no sideways
          scroll, nothing left hidden;
        - the mobile menu passes a keyboard test;
        - onboarding runs end to end in the browser (drawer, five steps, validation, letter,
          envelope). The API answer was supplied by the preview, so server-side sending still wants
          one test on a running server with the inbox connected;
        - README, research report, notes and sources updated.

### v3 queue (brief 3, 24 Oct)

How it runs: one `/loop` drives this list. **Background agents** work in parallel on the long research
and production tasks, and the loop checks their output each iteration. I build, integrate and verify.
Agents never edit `website/`. They write to `research/`, and their results are integrated here.

| Task | Owner |
|---|---|
| Q12 fixes | me |
| Q13 how top designers build brand sites (incl. manifesto, intro, cursor, parallax, surfaces) | **agent: design research** (web), then me |
| Q14 fonts: studio font list, `FONT_GUIDE.md`, shortlist | **agent: font research** (web), then me (specimens in the real site, choice, build) |
| Q15 intro | me (persistent-browser frame study of nvmbr.in, then build) |
| Q16 the house view | me, using the design-research findings |
| Q17 cursor | me, using the design-research findings |
| Q18 surfaces | **agent: textures** (procedural, seamless, high quality), then me |
| Q19 smooth and parallax | me |
| Q20 space | me |
| Q21 images | **agent: images** (ChatGPT in the persistent browser, HTML recreation as fallback), then me |
| Q22 responsive | me |
| Q23 docs and final checks | me |
| Q24 colour proportion: plum + powder blue at 70–90% | **agent: colour research** (web), then me (iterations in the real site, measured coverage, choice, build) |

- [x] **Q11 — Brief 3 recorded**: rules in §1 (tagged "brief 3"), the message verbatim in Appendix C,
      this queue.
      → Done: new rules in §1.3, 1.4, 1.5, 1.6, 1.7 and a new §1.9 (space, surfaces, quality).
- [x] **Q12 — Fixes**:
  - the request drawer's Close button;
  - the hero collage keeps every photo while scrolling, both ways: no scene that reduces it to one.
      → Done:
        - **Hero:** the pinned scroll scene (pieces flying off, one photo opening to full screen, the
          flip-book snapping to one project) is removed. It keeps all 6 pieces and 4 photos at the top,
          part-way down and back at the top (measured live).
        - **Close:** could not be reproduced. Real-mouse tests from every entry point (header, hero,
          choose-your-road, road cards, desk ticket, desk index, case study), at 1025 / 1440 / 390 px,
          three cycles in a row and with Escape all closed it, with no console errors. Hardened anyway:
          the bar is above the body, taps register immediately, and the button has a full label.
- [x] **Q13 — How top designers build brand websites**: research spacing, restraint, rhythm, type
      scale, surfaces, cursor and parallax on the strongest brand and studio sites; write the findings
      into `BRAND_DESIGN.md` and the rules.
      → Done: `research/DESIGN_PRINCIPLES_v3.md` (stylesheets of Here, Koto, Wolff Olins, JKR, Present;
      markup of nvmbr.in, Obys, Heure Bleue, Collins). Written into BRAND_DESIGN §8.3 (space is vertical,
      one idea per view, the clutter audit), §9.4b and §12 (flash-safe intro, dimmed-text floor), §10.11
      (cursor), §10.12 (the house view), §6.2 and §4.5 (paper and grounds). Its type scale and spacing
      tokens land with Q14 and Q20.
- [x] **Q14 — Fonts, properly**:
  - a list of the fonts studios use worldwide;
  - `research/type/FONT_GUIDE.md`: which kind of font for which kind of project or company website;
  - re-choose Kavalu's faces with specimens set in the real site, then apply them.
      → Done: `research/type/STUDIO_FONTS.md` (195 studios), `FONT_GUIDE.md` (by kind of company, and
      what makes type read as generated), `KAVALU_FONT_SHORTLIST.md` (three systems). All three were set
      in the real site at 1440 and 390 px (`research/type/lab/`); system A won: Schibsted Grotesk for
      display and text, Courier Prime only on typed paper, no italic or coloured word in headings,
      labels in the grotesk, a six-step display scale within WCAG's zoom limit. Gambetta and Switzer
      removed. Her own handwriting and signature (as SVG) are pending from Ananya; stand-ins until then.
- [x] **Q15 — The intro**: study nvmbr.in's hero and Marvel-style intros frame by frame, then build the
      intro (photos flash → zoom out → the name → the current hero). First visit only, skippable, none
      under reduced motion.
      → Done: nvmbr.in recorded (581 frames; cuts measured accelerating from about 450 to about
      100 ms, then the name). The new `Intro`:
        - her pictures flash on deep-plum paper (14 cuts, 240 → 50 ms, matched within a few ms);
        - the last one zooms out into a perforated stamp, and STUDIO / KAVALU rises under it;
        - the sheet lifts onto the hero, whose flip-book opens on that same picture.
      Checked at 1440 and 390 px. The pictures sharpen when Q21 delivers.
      → Revised in v3 after the design research: the cuts are a plum duotone (flash-safe by WCAG 2.3.1).
      Measured on a frame-by-frame recording: no change between two painted frames reaches 0.1 in
      relative luminance (largest 0.08 at the 95th percentile, 0.1% of the screen). The recording also
      caught her name showing before the reel while the pictures decoded; it now waits hidden from the
      first paint (`research/motion_frames/intros/kavalu-v3-duotone2/`). No intro with reduced motion or
      Save-Data (checked).
- [x] **Q16 — "The house view"**: research how studios present a manifesto or brand statement; replace the
      current pills and inking words with a proper representation and subtle motion design.
      → Done: the sentence is the index of the four roads (research proposal A). It stands still on a
      taped powder-blue sheet; each choice links to its road card, with a hand-drawn road that forks and a
      typed footnote; the roads draw once in reading order; pointing quiets the other choices to 50% and
      lays one print in the margin. Checked live at 1440 and 390 px, with hover, focus and the glide to the
      card (`research/working-shots/v3/houseview/`).
- [x] **Q17 — Cursor**: study cursor design on studio sites; build a cursor system (default, hover
      states, per-section states) for fine pointers only, with the native cursor kept wherever text is
      typed.
      → Done: Cuberto's follower recorded (dot about 10 px growing to about 72 px, trailing up to 77 px).
      `components/Cursor.tsx`:
        - default dot, link ring, "OPEN" / "NEXT" view disc, "← DRAG →" disc;
        - plum on light, cream on dark sections;
        - the native caret in fields;
        - fine pointers only, instant under reduced motion.
      All five states verified live, with crops in `research/working-shots/v3/cursor/`.
      → Revised after the design research (v3 §4): the dot is exact (0 px lag, measured) and what a click
      does is a typed paper tag beside the pointer ("OPEN →", "← DRAG →", "ROAD 02 →"), not a disc over
      the work; the system cursor stays in forced-colours mode. Crops in `working-shots/v3/cursor2/`.
- [x] **Q18 — Surfaces**: high-quality paper textures for every background, light and dark, never flat.
      → Done: `research/textures_v3` (seamless papers with each palette colour baked in, checked for
      colour, contrast and seams). Every ground, sheet, the intro, the folders and the desk use them, one
      texture pixel per device pixel (1024 px tiles, 512 px on retina, 512 tiles on phones), pinned to the
      page so one ground is one sheet. A soft-light grain over plum was tried first and rejected (it
      turned plum magenta).
- [x] **Q19 — Smooth and parallax**: tune the scroll, add subtle parallax, and make every transition
      subtle and consistent.
      → Done:
        - `lib/parallax.ts`: hero pieces drift at their own depth (11–52 px at 625 px of scroll,
          measured), back to exactly 0 at the top; case-study pictures travel ±4% inside their mounts;
          off under reduced motion.
        - Lenis lerp 0.1 → 0.09.
        - The hero's pinned scene is gone (Q12), so no section takes the scroll away.
- [x] **Q20 — Space**: a spacing system, and a pass over every section so it is spacious with no clutter.
      → Done: the research's ladder (`--s-3xs` … `--s-2xl`) and rhythm (`--section-y` 158 px, `--chapter-y`
      246 px at 1440 × 900, following the screen's height as well as its width) in `tokens.css`; every
      section and sheet padded from them; two labels that only repeated their heading removed (the album,
      the desk). Reviewed at 1440 and 390 px on home, studio, work and a case study
      (`research/working-shots/v3/review/`). BRAND_DESIGN §8.1 and §8.3.
- [ ] **Q21 — Images**: the same images at high quality (ChatGPT in the persistent browser; HTML
      recreation if the limit is reached).
      → In progress: 12 of 21 regenerated, checked against their sources and in the site
      (`research/images_hq/MANIFEST.md`: 4 by ChatGPT, 8 recreated in HTML; `image-meta.json` marks them
      `hq`, so the Anokhi case study now opens on its full-width cover). Rejected: the Nivritti cleanser
      bottle (ChatGPT changed its label and logo). Still needed: 8 photographs of people and products,
      which can't be recreated in code without inventing them. ChatGPT's free plan allows 5 images a day;
      the quota resets 25 Oct, 13:14 IST, then the images agent continues (Ananya's portrait last). The
      originals from Ananya would replace all of this. The old screenshot crops are kept in
      `research/images_hq/originals/`.
- [x] **Q22 — Responsive**: check and fix every page from 320 to 1920 px.
      → Done: 4 pages × 9 widths (320, 375, 414, 768, 834, 1024, 1280, 1536, 1920) with no page
      overflow and nothing loose past the edge. Fixed the cramped 320 px header (36 px now between the
      lockup and the Start pill). Re-swept in Q23 after the font, texture and spacing work.
- [ ] **Q23 — Docs and final checks**: `BRAND_DESIGN.md`, rules and sources updated; type check, build and
      browser checks; report back.
      → So far (24 Oct): BRAND_DESIGN 2.0 and the rules are up to date with briefs 3–5. Type check
      passes. Every page at 9 widths (320–1920 px) has no overflow and nothing past the edge. Reduced
      motion: no intro, no smooth scroll, nothing left hidden, on all four pages. Contrast: 0 AA failures
      on every page at desktop and phone (palette lab). Still to run: the production build, which needs
      about 2 GB of free memory (the machine had 1.4 GB), and a last pass once Q21's images are in.
- [x] **Q26 — The hero's scroll scene back** (brief 6): the images merge into the centre image, it
      expands, the next section appears from it; scrolling back re-scatters every image; really smooth.
      → Done: rebuilt from the first version (recovered from the session transcript): pinned 1.5 screens,
      scrubbed (1 s), the pictures glide into the centre stamp, its picture opens to full screen and
      dissolves into the first spread's blue, which deals its prints out of it. Recorded down and back up:
      every piece returns to its place and the flip-book resumes (`working-shots/v3/hero_scene/`).
- [x] **Q27 — The intro, refined** (brief 6): every load of the home page; the landing page's colours;
      the reel dims into a very light moving background of the hero; a smooth hand-over.
      → Done: plays on every load of `/` (refresh included); cream paper; flash-safe duotone cuts at half
      strength; the last picture develops; the reel sinks to 9% while her name rises in plum; the sheet
      fades into the hero, whose own faint reel shows the same picture underneath (no wipe). Recorded
      frame by frame (`motion_frames/intros/kavalu-v4-cream/`). BRAND_DESIGN §9.4b.
- [x] **Q28 — Scroll and parallax, properly** (brief 6): a real, professional, smooth depth system across
      every page, verified frame by frame.
      → Done: `lib/parallax.ts` (media, layer, stagger), applied to the spreads, the house view, the album,
      the roads, the founder, the letter, the footer folders, the work grid and the case studies; Lenis
      0.085 with a 0.8 s scrub on every layer. Measured on the production build with Chrome traces:
      0.8% of frames over 20 ms on desktop; on a phone with its processor slowed 4×, 29% (from 66%).
      BRAND_DESIGN §9.3, §9.6.
- [ ] **Q29 — Images, round 2** (brief 6; agent): download every image from the ChatGPT chats, generate the
      rest with Gemini (and ChatGPT when its quota returns), check each against its source, then replace.
      → Paused at the user's request (24 Oct). The chats held nothing new (5 project chats of 200). Now
      in the site (19 of 21 pictures high quality; the old files in research/images_hq/originals/):
      cleanser-bottle, business-cards and packaging-box, checked by eye against their sources; and, at
      the user's choice, four with parts redrawn by AI: red-room-portrait (passed the check),
      not-so-onam and red-saree-portrait (faces rebuilt from about 10 px, so they may not look like the
      real people; the not-so-onam title sits a little right) and word-search (letters re-set in Arial).
      Swap all four for Ananya's originals before launch. Not done: fillers-not-yet (Gemini refused a
      public figure; ChatGPT's quota returns 25 Oct 13:14 IST) and the Ananya portrait.
      images_hq/MANIFEST.md is out of date for round 2.
      Gotcha: Next's image optimiser keeps its resizes for 4 hours, so a replaced picture still looked
      old. `research/tools/purge_image_cache.py` drops only the resizes made from the replaced files
      (matched by source size and time), safe while the dev server runs; run it after every swap.
- [x] **Q25 — Less plum** (brief 5): plum about 20%, cream and blue 50–60%, the rest for the remaining
      colours; the hero and the first sections light. Render arrangements in the real site, measure them
      at desktop and mobile, choose, rebuild the grounds, update BRAND_DESIGN §4.5.
      → Done: six light arrangements rendered and measured (L1–L5, R2); R2 built. The page opens on
      cream; her prints sit on powder-blue spreads; the house view is the torn cream sheet; the album
      strip is the one plum chapter mid-page; the founder stands on oxblood; the letter on blue; each case
      study opens in its project's own colours. Measured over four pages: plum 20.8%, cream + blue 61.9%,
      oxblood 5%, photographs and project colours 12% at desktop (15.4% / 62.6% on a phone), 0 AA
      failures. BRAND_DESIGN §4.4–4.5.
- [x] **Q24 — Colour proportion** (brief 4): plum and powder blue together cover 70–90% of the site.
      → Done: the site is her desk (one plum ground, statements and reading on large powder-blue sheets,
      the cream letter as the action). Ten arrangements were rendered and measured on the real site with
      `research/tools/palette_lab.py`, and compared with the colour research. Built: plum + blue are
      89.7% of the site's own colour at desktop and 77.9% on a phone (82.5% and 66% of the screen,
      photographs included), with 0 AA contrast failures. BRAND_DESIGN §4.5.
  - Research how brands and studios build a site on a dominant pair of colours: proportion rules,
    colour blocking, alternating sections, ink and paper roles.
  - Build several iterations in the real site (different proportions and arrangements).
  - Measure each one's actual colour coverage from screenshots at desktop and mobile, check contrast,
    then compare and choose.
  - Rebuild the site's colours on semantic surface tokens, so the chosen proportion holds on every
    page.
  - Record the result in `BRAND_DESIGN.md` §4.

### Log
- 2026-10-24 — Q1 written.
- 2026-10-24 — Q2 sources file (226 sites) written.
- 2026-10-24 — Q3 her wordmark rebuilt from her own lettering and used everywhere the name appears.
- 2026-10-24 — Q4 footer v2 built and checked. Gotcha recorded: GSAP turns a CSS `translate: -50% -50%`
  into pixels when an element's half-height doesn't round evenly, so pins are centred by a wrapper
  that GSAP never animates.
- 2026-10-24: Q5 crawl found case-study pages returning 500. Cause: the long-running dev server's
  render workers had died ("Jest worker encountered 2 child process exceptions"), not the code;
  `next build` renders all five. The server was stopped to restart it, but the restart was declined by
  the permission check, so the user needs to start it (`cd website && npm run dev -- -p 3210`).
- 2026-10-24: Q6 type system built.
- 2026-10-24: with the dev server down, checks run on the production build, served from disk into
  the persistent Chrome tab through the DevTools Fetch domain (no server process, no port):
  `research/tools/preview.py`. Found and fixed during the checks: Courier is 10% wider, so the
  sticker ring text was refitted; a `display: table` caption dropped the spaces between split words;
  the desk postmark overhung a phone screen by 8 px.
- 2026-10-24: Q5, Q6, Q7 ticked after checks at 1440 / 390 px and with reduced motion.
- 2026-10-24: Q8 `BRAND_DESIGN.md` written; Q9 consistency pass applied and audited; Q10 final checks
  passed. The queue is complete. Still open: Ananya's pending material (project list and notes,
  reference videos and folder, original images, her bio, logo vectors if any), the inbox keys, and a
  dev-server restart by the user (see the Q5 entry above).
- 2026-10-24 (v3): never edit `website/` while a browser measurement runs on the dev server. A save hot-reloads
  the page under the script (the palette lab once captured 4 screens of 14 and measured the wrong page);
  `research/tools/palette_lab.py` now detects a reload and re-applies the iteration.

- 2026-10-24 (v3, client feedback): the four roads' map drew too late (still 83% drawn with its top a quarter
  of the way down the screen), so it now draws as it rises through the lower half and finishes before the
  cards land. The footer wordmark "was not working": a frame recording showed its scrubbed arrival
  finished while only the mark's top edge was on screen. It now plays once, by itself, when the mark is
  well in view (`research/working-shots/v3/footer_watch/`).
- 2026-10-24 (v3, brief 6 smoothness): judged on Chrome traces of the production build, not on the dev
  server, whose numbers are inflated (a first visit compiles; React's development build renders twice) and
  noisy (the persistent browser's other tabs share its processes). The traces named six causes, all fixed:
  the spreads' sheet and shade repainted the whole screen every frame of a slide-over; the nav hit-tested
  the page every frame; the hero re-rendered every picture on each flip-book tick; the hero scene and the
  parallax measured the page on the first frame of a scroll (30 ms in one frame); about 220 permanent
  layers made every re-layering slow on a phone; and a phone moved all 21 album stamps for depth no one
  could see. Tools: `research/tools/trace_scroll.py`, `smooth_check.py`, `warm.py` (BRAND_DESIGN §9.6).
  Gotcha: `will-change` is not free. Each layer is weighed again whenever anything repaints, so add one
  only to what moves, and on a phone only while it is on screen.
- 2026-10-24 (v3, request): "add a social preview for this. like using logo and the name". Added the
  social preview card (BRAND_DESIGN §3.8): her lockup on cream paper with the line and "by Ananya", and a
  powder-blue note defining ಕವಲು, made from the site by `research/tools/og_card.py` (85 KB JPEG, every
  page; case studies with a sharp wide cover show that instead). Checked in the production build: every
  page's og:image and twitter:image are absolute on https://studiokavalu.com. Gotcha: the persistent
  Chrome keeps localhost:3210 at 90% zoom, which scales emulated screens (a 1440 px emulation is really
  1600 CSS px); og_card.py measures the zoom and compensates.
---

## Appendix A — the client's first brief (verbatim)

> I want a website redesign for a brand. it is a design studio named studio kavalu by my friend. the
> website design is ready but we dont like it. I will give some reference videos as well. what I need is
> research on other studio websites and other like minded brands. like some of here friend's brands are
> studionumberseven, studio sorted etc. the website should not be like that but that is how studio
> websites are. make a proper global and professional level brand website for design studios. make sure
> that you research properly on how these websites are designed. use persistant browser for any data that
> you cant get from web search like an image or anything. make sure you act as a 10-15yr expereince design
> studio website designer. she wants good subtle and smooth scroll zoom in zoom out expand etc animations
> as well. not just these animations but any more animations you have which will be good for this add
> those as well. take reference about how animations are in this. take atleast 100-150 websites design
> reference and see how can this be done. lets say for tech people use 21st dev, react bits etc. so use and
> see something like those. make sure that it is really good. the name is studio kavalu by ananya.
> research about this brand as well if there is any online presence. I'll share a list of projects she has
> worked on as well and something about them. also she wants that the website should have more visibolity
> around her projects because most of her projects are visual. she wants it to be a scrapebook as well, I
> will give the folder wiht all the references as well. make sure that you analyze her projects as well to
> see what kinds of work she does. keep the colour pallet same as now. make sure it should be like instant
> client onboard as well. it should be subtle, elegant, aesthetic and everything a design studio website
> should look like in 2026/27. A brand is a set of choices; what it says, how it looks, where it shows up,
> who it speaks to. Studio Kavalu is a branding and content house that makes these choices with you. We
> shape brands, feeds and persona through a design lens backed with strategy. The aim- work with a point of
> view clear enough that people recognise it, and others follow it. here is the reference path ->
> C:\Shashank\Shashank\fnf\ananya_residency\studio_kavalu. here are some additional links ->
> https://in.pinterest.com/pin/681873199876372589/ (a landing page ref),
> https://in.pinterest.com/pin/681873199876372589/

## Appendix B — the client's second brief (verbatim)

> [screenshot of the footer] the bottom logo/text should be in such a way that when we are scrolling to
> footer "studio" comes from left side and "kavalu" comes from right side and then they sit where and how
> they are right now. and also the font is really bad, use the font I gave you not this one. keep design
> sense same throughout the website. and make a proper doc about the design sense. make an md file of full
> design sense and how what all are uniform throguhout the website. proper brand design doc. see how this
> is made, research that how such things are made and make an in depth doc using that. for each task use
> /loop and keep on prompting yourself and make this. make sure that you do not make it look like AI slop.
> keep the fonts good. either use the reference and see what sort of fonts look best for work like this.
> if you can use some more motion graphics in the footer. ananays was telling me she wants to use this
> "what we pin on our desk" on the footer but she didnt tell me how. so figure out that as well, and see
> how can this be done. research about it how such things can be put on footer. [screenshot of the "What
> we pin above the desk" section]. also dont make a separate page for scrapebook. we said that the project
> format or something whatever I told you in the previous prompt -> that part/idea should look like a
> scrapebook. the website idea should be like a scrapebook. not a separate page which has the exact
> picture which are references I gave you. make a kavalu_instructions.md file and add the rules which I
> told you there. keep this as a priority task. store everything there. all the website sources which you
> scraped and from where you ideated, make a separate file for that with the links of the websites. add
> some good motion desing graphics, research about them and add them. use persistant browser to take
> frames screenshot each 1ms or any time apart and see how can that be made. take reference from good
> motion design that would go good with this. not some random motion design, see if any of the researched
> websites had motion design. keep the existing animations but if you want you can add subtle motion
> designs

## Appendix C — the client's third brief (verbatim)

> [screenshot of the hero collage] at all times keep this many photos only. right now when scrolling it
> is changing to one even if I scroll back up. remove this way of representing it see how you can
> represent this research properly and see if you can add some good animations with motion design to
> represent this section but they should be subtle not some slop -> "The house view
>
> A brand is a set of choices; what it says,  how it looks,  where it shows up,  who it speaks to. ".
> also the close button when requesting a project is not working. also this font is not good. make a
> list of fonts used by the studios all over the world and make a doc of what type of font to use for
> what type of project/comapny's website. see properly and research on the font as well it is not
> lokking good right now. add some cursor design as well. on hover and in general as well. cursor
> changes on specific section. also make everything smooth and subtle the scroll everything. the
> background should be a texture rather than solid colours. there should be parallax effect as well.
> and make everything responsive. also keep this in rules, that everything should be spacious, there
> should not be any cluttered sections or anything. there should be proper breathing space. like the
> hero section in this make a intro hero section -> https://www.nvmbr.in/, keep the current hero
> section as well, but make it sort of like marvel intro theme, where all the photos are coming each ms
> and then they get zoomed out and then the name appears and after that the current hero section. see
> if you can do something like this. match evertyhign to our design brand theme. add subtle smooth
> transition scroll animations only. it should be really professional and really high quality. use
> persistant browsers /converse-with-gpt skill to get some images generated and use high quality
> images, right now the images are really bad. but generate the same ones but in high quality, dont
> generate any different images. and if GPT limit is over, use HTML to make that image using code and
> screenshot it and then use it in the website. do proper research on everything before making every
> decision, see how top brand designers + web desingers make websites acc to the brand and good design
> sense. see how it works, add everything to the rules book and brand design whatever is relevant and
> useful.

## Appendix D — the client's fourth brief (verbatim)

> also add into the todo list and add to the context, that the main colours to be used are plum and
> powder blue, like these both should be like 70-90% of the website depending on how it looks better and
> the rest should be the remaining percentage. see multiple iterations and multiple researches on how
> and which exact combo will look better. research and test properly, on what is the best proprotion
> and how to present it the best

---

## Appendix E — the client's fifth brief (verbatim, 24 Oct)

> can you swithc the agents to the current org. becuase right now we have the usage limit after I
> changed accounts. also the current website has too much plum. make the proprotion, 20% plum, 50-60%
> cream and blue and the remaining rest. also make sure the hero and first sections does not have that
> much plum.

---

## Appendix F — the client's sixth brief (verbatim, 24 Oct)

> in the first section, it used to be like -> as you scroll, the all the images would merge to a center
> image and then expand and then the next section would appear from it as we scroll. make ut like that
> the one you did initially. but keep the fixes i.e. when scrolled back up all the images should be
> scattered and not just one. also the smooth effect should be really smooth. right now the images are
> also really bad. fix those. download from the gpt chats (if not already done). and ask it to generate
> some more as well(if not already done). or you can ask gemini as well, it can also generate images(if
> not already done). take good high quality images, download them adn replace them in the website(if not
> already done). there are 6-7 chats already in chatgpt that has the images generated. download them(if
> not already done). also make proper parallax and scrol effects, it should be really smooth. not just
> some formality task or shit. do it properly and it should be really good and professional not just
> some scroll effect. proper professional smooth, scroll and parallax effect. also when the site is
> loaded for the first then only the video and bit by bit 1ms apart image series is being shown, the rest
> of the time even if I refresh only the hero section comes. also match the colours of the initial video
> like right now it is plum make it the same as landing page. also the that transition is also not that
> smooth. to make it smooth do one thing, make it less opaque and then merge it into the BG make it a low
> opaque background for the hero section. keep the current hero section with the above changes I
> mentioned but with the video as bg but very light transparecy.
