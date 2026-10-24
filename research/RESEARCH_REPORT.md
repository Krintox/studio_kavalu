# Studio Kavalu by Ananya: research report and redesign rationale

*Prepared 23 October 2026. Companion files in this folder: `design_direction.md`, `motion_catalog.md`
(41 techniques), `onboarding_research.md` (41 studio contact pages, 59 sources), `reference_sites.json`
(196 curated sites), `notes_screens.md`, contact sheets in `sheets/`, raw captures in `screens/`.*

---

## 1. The short version

- **What Kavalu is.** A founder-led branding and content house in Bengaluru. *Kavalu* (ಕವಲು) is Kannada
  for a crossroads: "a point where paths meet, split, and become something new". Her work is rooted in
  craft and culture (a Devanagari letter that is also a pot; a linocut Himalaya), told through strategy,
  and carried into social content and shoots.
- **What the new site does.** It treats the studio as *the crossroads album*: every project is a stamp in
  a collection, opened as a full-screen spread in its own colours, annotated by hand and filed under the
  folder tabs from the first site. A hairline road forks through the pages. The work leads; the paper
  ephemera only frame it.
- **How it was researched.** 226 studio and brand sites (225 studios; Mucho has two domains) were
  opened in a real browser and captured at three scroll depths with their stack detected (framework,
  GSAP, Lenis, WebGL, fonts) and reviewed as contact sheets; 41 motion
  techniques were catalogued from React Bits, 21st.dev, Codrops, Osmo, GSAP and award sites; 41 studio
  "start a project" pages and 59 sources were reviewed for onboarding.
- **What was built.** A Next.js 16 site in `../website`: home, work (stamps + index), five project pages,
  studio, scrapbook (draggable desk + grid), and "Choose your road", a five-step onboarding that writes
  a letter, seals it in a stamped envelope and emails the studio.

---

## 2. The brand, and the current site

### Fixed inputs
- **Palette (kept exactly):** cream `#F3F3E7`, oxblood `#491C17`, plum `#390D26`, deep plum `#270617`,
  powder blue `#ABCDD6` — sampled from the current site.
- **Line:** "A brand is a set of choices; what it says, how it looks, where it shows up, who it speaks to.
  Studio Kavalu is a branding and content house that makes these choices with you."
- **Services (her four):** Branding · Visual identity · Social media · Film & photography.
- **Online presence:** none found. `studiokavalu.com` does not resolve yet; no Instagram account
  `@studiokavalu`; no Behance or press results. The site launches the studio publicly, so it has to
  carry the whole first impression.

### What the current design gets right (kept)
- The **palette** and the warm, papery mood.
- The **folder-tab footer** — the most distinctive thing on the site. Kept as the footer and the mobile menu.
- The **tilted service cards with doodles** (clipboard, pen tool, film roll, camera) — kept as index cards.
- The **Kannada name and the crossroads definition** — promoted to a concept.
- The **oxblood overview card** on case studies, and the well-written case-study text (used verbatim).
- The **two-line STUDIO / KAVALU wordmark** in the footer.

### What holds it back (changed)
1. **The work is too small.** On the homepage collage the pictures are thumbnails; the About page
   opens with a definition box and no work at all. Her work is visual; it has to lead.
2. **No hierarchy in type.** A Helvetica-style body, a soft serif, heavy extended caps in italics and a script all
   compete. The new system: one display serif, one text face, her own lettering only for the wordmark,
   typed labels, and handwriting only for margin notes. *(v2, 24 Oct: the faces are now Gambetta,
   Switzer and Courier Prime, and the wordmark is her lettering redrawn as SVG; v1 had Fraunces, Ranade,
   Panchang and IBM Plex Mono. See `type/TYPE_REVIEW.md`.)*
3. **Case studies have no pace.** Uniform two-up grids and small images; no full-width moments, no
   sequence. The new template alternates text, full-width, pairs, stamp grids, palettes and notes.
4. **Placeholder text** ("Torem ipsum dolor sit amet…") in the founder card on About.
5. **Contact is one message box.** No structure, no expectations, no booking — the opposite of
   "instant onboarding".
6. **No index, filters, scrapbook or motion system;** the layout reads as a generic template.

---

## 3. Her work: what kind of studio this is

| Project | What she did | What it shows |
|---|---|---|
| **Studio Anokhi** (2025), pottery studio, Bengaluru | Brand identity, visual identity, social media strategy | A rounded, stacked wordmark; a mark drawn from the Hindi letter **अ** whose silhouette is also a pot; terracotta / red-oxide / earthy-green / yellow / ivory palette from the clay and floors; hand-drawn clay illustrations; stationery and a word-search motif. |
| **Nivritti** (2023), Ayurvedic hemp de-addiction brand, Delhi NCR | Logo, visual identity, packaging | A linocut-style Himalaya (where hemp grows; Shiva and Vijaya); a bold high-contrast serif; navy / forest / burnt orange to stand apart from beige Ayurveda shelves; cards, boxes, bottles, signage — "premium without feeling exclusive" for 18–30 urban buyers. |
| **Not-So-Onam?** | Festive social content (details to confirm) | Playful festive concept with bold type over fashion photography. |
| **"I'm not getting the fillers yet"** | Social content / reel (details to confirm) | Humour and a quotable line; yellow display type over celebration footage. |
| **Shoot stills** | Film & photography (details to confirm) | Strong reds, warm light, editorial portraiture. |

**Pattern.** Identity work that starts from a *cultural or material source* (a letterform, a mountain,
clay), turned into a *system* (palette, illustration, packaging), and then carried into *content* with
wit. That is a rarer mix than "branding studio" suggests, and it is what the site should make obvious:
the spreads show many pieces per project, the case studies keep her "where it came from" writing, and
the four services are framed as the four choices in her own line.

---

## 4. Her friends' studios, and why Kavalu must look different

| Studio | What their site does | Kavalu's difference |
|---|---|---|
| **Studio Sorted** (studiosorted.com), Bengaluru; founder Abhishek Durani; Forbes 30 Under 30 India 2024 / Asia 2025 (per its DesignRush listing) | Loud yellow, hand-drawn mascot, "Branding for the Seriously Fun.", "Planet Sorted" sticker badges, food & drink case cards; clients named on its site include Theka Coffee, MG Motor, WeWork, Sony Music and Mokobara. Webflow. | Quiet, warm and editorial instead of loud; plum/oxblood instead of yellow; craft and culture instead of fun. |
| **Studio N°7** (studionumberseven.com, @studionumberseven_) — *exact-name match; that this is the friend's studio is not confirmed* | Currently a "being thoughtfully rebuilt" page: a condensed serif wordmark on cream, press logos (Forbes, Grazia, Vogue, Bazaar), a ceramics still life. Earlier: premium lifestyle branding and social templates. | Shares cream and serif, so Kavalu leans on what N°7 doesn't have: the stamp/album system, Kannada identity, the four-roads structure, the motion story, and project spreads in each client's colours. |

---

## 5. What 226 studio and brand sites taught us

Captured in the persistent Chrome at 1440×900, three scroll depths each (`sheets/sheet_01–57.jpg`,
notes in `notes_screens.md`). By bucket: boutique/founder-led studios 46, Indian studios 24,
established agencies 31, motion-led studios 35, tactile/collage/scrapbook 36, like-minded lifestyle
and craft brands 29, portfolios 25.

**How they are built** (detected at runtime, so bundled libraries are a floor, not a ceiling):
video on 48% of sites, a WebGL/canvas layer on 22%, Next.js 21%, Lenis smooth scroll 17%,
WordPress 14%, Nuxt 12%, GSAP 11%+, Shopify 9%, Webflow 5%, Framer 3%. Award-level studio sites are
overwhelmingly custom-coded (Next/Nuxt + GSAP + Lenis), which is why Kavalu's site is built the same
way rather than on a template builder.

### What the best ones share
1. **The work leads.** Pentagram, Base, Porto Rocha, Gretel and Koto reach the work within one scroll;
   Base and Porto Rocha even lead with *volume* (feed, index, archive).
2. **One confident sentence.** Collins ("Rewrite your worth."), Here ("We design *brand ecosystems* with a
   *cultural purpose*."), Wolff Olins, JKR — a serif line with italic emphasis is the house style of
   premium studios, and fits Kavalu's line.
3. **One signature interaction.** Obys' viewfinder that "selects" images as you scroll, Pentagram's
   sentence-as-filter, Mother Design's desktop toolbar and sticky note, DixonBaxi's prompt hero,
   14islands' paper cut-outs. Kavalu's is the crossroads: a stamp that opens into a project, pieces that
   deal out like paths splitting.
4. **Restraint in chrome.** Tiny navigation, mono labels, generous space; a live local clock is common
   (Koto, Porto Rocha, Boc.Studio) and suits a Bengaluru studio working worldwide.
5. **Several views of one collection.** Grid ↔ index ↔ archive (Base, Obys, Olivier Larose, Studio
   Feixen).

### Closest in spirit
Happy Happy Creative ("Brand and Content for Founder-led Brands": warm palette, polaroid flatlays),
Studio OL (cream, serif, editorial lifestyle), Perky Bros (a serif statement, "Start a project" in
the nav), Present (a serif statement over warm photography), Goodside (serif wordmark over a scattered
collage of real objects), Odds
(typewriter copy, a charming mark), Lotta Nieminen (image-first, founder-led), Immersive Garden
(paper as a premium material), Niccolò Miranda's Paper Portfolio (newsprint plus a perforated stamp
with his name — the stamp motif, independently), LRNCE (a pinned-moodboard hero), Collage Department
(collage and picture research for brands' feeds), and — from the motion catalog, not captured — the Digital Stamp
Collection (marijanapav.com/stamps: stamps, binder tabs and typewriter cards on the same Next.js +
Lenis stack).

### Indian context
- **Brands:** Subko runs a multi-script marquee (Kannada included), proof that Indian scripts read
  as premium. Bombay Sweet Shop, Nicobar and Good Earth show warm, crafted Indian lifestyle branding.
  Most Indian brand sites carry a WhatsApp button.
- **Studios (24 reviewed):**
  - *Dense project grids:* Codesign, Studio Bigfat and November.
  - *Dark statement heroes:* Lopez ("Dare to be authentic") and Elephant ("We Design Digital
    Experiences").
  - *Common features:* client-logo walls, "Book a call" / "Start a project" buttons and floating
    WhatsApp buttons (Wishbox, Confetti, Beyondesign).
  - *Playful colour:* Studio Ping Pong (Bengaluru/Kolkata) and November.
  - *Closest in tone to Kavalu:* designmill (cream, italic serif).
  - *Pattern:* very few Indian studio sites are warm and editorial *and* lead with the work. That gap
    is Kavalu's opening.

### What to avoid (seen repeatedly)
Pop-ups on arrival (Fishwife, Brightland, Ghia, Diaspora Co, Bombay Perfumery, Kama Ayurveda and
Apartamento all open with a discount or newsletter modal), cookie banners over the hero (B&B, Nido,
Present, Bureau Borsche, Good Earth), preloaders and enter-gates that hold back the first screen
(Locomotive, Made Thought, Unseen, Utsubo), WebGL showpieces that hide the work (Active Theory,
Lusion, Bruno Simon), the same fade-up on every block, and loud
playful systems that would make Kavalu look like Studio Sorted.

---

## 6. Motion: what was researched and what was used

Full catalog: `motion_catalog.md` (41 techniques; React Bits, 21st.dev, Aceternity, Magic UI, Motion
Primitives, Osmo, Codrops 2023–26, GSAP, Lenis; package versions checked on npm).

**Weighting.** Jakub Krehel's production polish first, Jhey Tompkins' play for the scrapbook and the
envelope, Emil Kowalski's restraint for navigation and forms.

**Used on the site**
- Lenis smooth scroll on GSAP's ticker (lerp 0.1), ScrollTrigger scrubs of 0.3–0.5.
- **Hero:** the album page settles in; on scroll it pins, the headline lifts, satellites drift apart
  along their own paths and the centre stamp **expands to the full screen** in the first project's
  colour (clip-path inset, measured).
- **Spreads:** each project's pictures **deal out from a pile** into a collage; as the next project
  slides over, the previous one **zooms out** and dims (CSS sticky + scrubbed scale).
- **Manifesto:** words ink in on scroll; tiny image pills grow after each of the four choices.
- **Four roads:** one line draws and forks into four; index cards are dealt onto the page.
- **Scrapbook:** *(v2: the scrapbook is the site's format, not a page.)* Pieces fall onto the footer
  desk and can be pushed around with inertia on desktop; on phones the desk is a swipe strip. Her
  notes write themselves in and typed captions type on (`motion_frames/sites/NOTES.md`).
- **Work:** filters reflow with GSAP Flip; the index view shows a tilted stamp following the cursor;
  stamps **morph into case-study covers** with React's `<ViewTransition>`; pages lift out and settle in
  with the header held still.
- **Small, tactile moments:** a pen scribble under "road.", the flip-book stamp (pausable), the
  signature writing itself, the envelope folding and being stamped, the footer wordmark rising.
- **First visit:** the road draws up the page, forks, ಕವಲು appears, the sheet lifts (≈1.6 s,
  skippable, once per session, never with reduced motion).

**Rules kept** (from the catalog's anti-list): one auto-moving element per page and it pauses; no
pop-ups; body copy is not animated; no scroll-jacked horizontal case studies; every effect has a
`prefers-reduced-motion` path (no pinning, no scrub, no intro, grid scrapbook, instant page swaps).

---

## 7. "Instant client onboarding"

Full research: `onboarding_research.md`.

- **The flow, "Choose your road":** five short steps (road → details → brand → timing & budget → you),
  about three minutes, eight required answers. The letter to Ananya writes itself from the answers and
  becomes the review step; on send it folds into an envelope stamped with a reference (KAV-XXXXX), then
  "what happens next", a prefilled call booking and WhatsApp.
- **Why questions and not a fill-in-the-blank letter:** the famous 25–40% lift for sentence forms comes
  from a confounded 2010 test, and accessibility testing found real failures; labelled questions keep the
  charm in the letter without the cost.
- **Instant, everywhere:** every "Start a project" opens the flow as a drawer on the page you're on
  (no navigation), service cards and case studies pre-select their road, and the homepage carries the
  first step inline.
- **Evidence-led details:** short steps with the easy question first; budget late, as ranges with "Not
  sure yet"; chips built from real radios/checkboxes; errors on blur; no percentage bar; honeypot +
  signed timer (+ optional Turnstile) instead of a CAPTCHA; a reply promise and a call booking on the
  thank-you screen (speed of response is the strongest lever in the evidence).
- **Backend:** a Next.js route that emails the studio and the client via Resend (free tier), optionally
  logs to a Google Sheet; works with nothing configured (local file in development, an honest
  "email it instead" in production).

---

## 8. Design decisions

| Decision | Why |
|---|---|
| Concept: the crossroads album (road · stamp · folder tab) | Grows from her name, her current footer and her landing-page reference (the Stamp Series); distinct from both friends' studios. |
| ~~Fraunces (variable) for display~~ → **Gambetta** (v2) | A serif continues her heading serif; v2 chose Gambetta over Fraunces after specimens, because Fraunces' soft wonky italic is the generated-site default (1 of 226 researched sites use it). |
| ~~Ranade + Panchang~~ → **Switzer** + her own lettering (v2), Anek Kannada (Ek Type) | Indian-made type for an Indian studio. Panchang was rejected by the client; her STUDIO / KAVALU was redrawn from her own lettering. Switzer is the grotesk register of 85% of the researched sites and of the references. |
| ~~IBM Plex Mono~~ → **Courier Prime** labels (v2), Homemade Apple notes | The typewriter voice of the references (typed cards) is now literal; handwriting only for margin notes. |
| Project colours on spreads and case-study heroes | "The work changes the room" — each client's palette is part of how the work is shown. |
| Placeholder-aware images | Stand-ins stay small inside stamps (never blurry); real files automatically go full-bleed. |
| Credits on every scrapbook reference | The scrapbook shows other people's work; it must be attributed. |

---

## 9. What is needed from Ananya

1. **Logo files** (SVG/AI/PDF) — the site uses a redrawn stand-in.
2. **Original project images** (all current pictures are cut from screenshots), plus a **portrait**.
3. **The project list and notes** promised (and details for the three content projects).
4. **Her bio**, and confirmation of the proposed copy marked `confirm` (service one-liners, process, FAQ).
5. **Business decisions for onboarding:** budget ranges and minimum, "starts at" prices, reply and
   proposal promises, advance %, booking-from month.
6. **Accounts:** domain DNS, Resend, Cal.com, WhatsApp Business, optional Turnstile and Google Sheet, and
   hosting (Vercel Pro or Netlify).
7. **The scrapbook folder** and the **reference videos** mentioned, plus sources for uncredited references.
