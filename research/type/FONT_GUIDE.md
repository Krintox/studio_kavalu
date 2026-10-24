# Font guide: which type for which kind of website

*24 October 2026 · research for Studio Kavalu (brief 3: "make a doc of what type of font to use for what
type of project/company's website")*

**What this is.** A working guide for choosing type for a client's website, by kind of company. Part 1
holds the rules that apply everywhere: roles, pairing, the settings that read premium or cheap,
licences, what makes type look AI-generated, and free alternatives to the paid favourites. Part 2 goes
through thirteen kinds of company: what works and why, the roles, the mistakes, and real examples
with their faces and a source for each. Part 3 is a one-table summary.

**Where the examples come from.** Every "X uses Y" is linked to where it is stated or observable: our
own browser census of 226 sites (24 Oct 2026, `research/screens/results.jsonl`), Fonts In Use,
Typewolf's Site of the Day, foundry pages, agency case studies and design press. "Identity" means the
source documents the brand's identity rather than its website. The studio list behind §2.7 is in
`STUDIO_FONTS.md`.

---

## Contents

1. [Rules for every website](#1-rules-for-every-website)
2. [By kind of company](#2-by-kind-of-company)
3. [Quick reference](#3-quick-reference)
4. [Sources](#4-sources)

---

## 1. Rules for every website

### 1.1 Choose by role, not by mood

A website has three typographic jobs. Choose the face for each, in this order:

1. **Text**: body copy at 16–20 px and interface text at 13–15 px. Most of the reading happens here, so
   it decides legibility, tone and page weight. Choose it first.
2. **Display**: headings from about 32 px. Often it is the text family set larger, heavier and tighter.
   If it is a second family, it should contrast with the text on *one* axis (structure, width or
   weight), not on all of them at once.
3. **Label**: captions, metadata, prices and navigation at 10–14 px. Usually the text face; sometimes a
   monospaced face with a specific job (data, captions, codes).

A logo is none of these jobs. A strong custom wordmark wants quiet type around it, so the mark stays
the loudest letters on the page.

### 1.2 Pairing rules

- **One or two families.** "Most documents can tolerate a second font. Few can tolerate a third.
  Almost none can tolerate four or more" ([Butterick, *Practical Typography*](https://practicaltypography.com/mixing-fonts.html)).
  Apple's guidelines say the same: "Minimize the number of typefaces you use"
  ([Apple HIG](https://developer.apple.com/design/human-interface-guidelines/typography)). Among the
  studios in `STUDIO_FONTS.md`, about four in five (82%) load one or two families (§5.8 there).
- **Give each face a consistent role.** "Font mixing is most successful when each font has a
  consistent role in the document" ([Butterick](https://practicaltypography.com/mixing-fonts.html)).
- **Contrast on one axis, agree on the rest.** A serif display with a grotesk text works when their
  x-heights, widths and weights are close at text size. A light, narrow, calligraphic serif beside a
  heavy, wide, geometric logo contrasts on every axis at once and reads as two brands.
- **Superfamilies are the safest pair**: a sans with its mono, or a serif with its sans, drawn by the
  same hands. Studios do this constantly: Basis Grotesque + Basis Mono at
  [Mother Design](https://www.motherdesign.com), Founders Grotesk + Founders Grotesk Mono at
  [Turner Duckworth](https://www.turnerduckworth.com/), GT America + GT America Mono at
  [Toormix](https://toormix.com/) (all from the census).
- **Never pair near-twins.** Two neo-grotesks, or two geometric sans, look like a mistake.
- **Scripts and handwriting are moments, never interface.** Real handwriting beats a handwriting
  font: fonts repeat identical letters, and OpenType's workarounds cycle alternates in a predictable
  order ([Glyphs tutorial](https://glyphsapp.com/learn/features-part-3-advanced-contextual-alternates)).
- **Indic scripts need a partner drawn for them**: a family designed across scripts (Anek, Mukta, Hind,
  Noto, Tiro) or an Indic face matched by eye in weight, x-height and colour (§2.13).

### 1.3 Settings that read premium, and settings that read cheap

| | Reads premium | Reads cheap |
|---|---|---|
| How many faces | One or two families; a label face with one job | Four or more; a new face per section |
| Display weight | Regular to Medium at large sizes; one bold moment per page | Everything bold, or hairline Light on photographs and paper textures |
| Scale | Few sizes on a clear ratio, with a big step from text to display | Many near-identical sizes (34 / 36 / 38 / 40 px) |
| Tracking | Slightly negative on big display (−1% to −4%); +5–12% only on short capitals | Letterspaced lowercase; default spacing on a 120 px heading, which looks loose |
| Line height | Display 0.9–1.05; text 1.4–1.6 | Display at 1.5; text at 1.2 |
| Measure | 45–75 characters, about 66 ideal | Paragraphs running the full width of a 1440 px screen |
| Case | Sentence case for headings; capitals only for short labels | Capitalised paragraphs; Title Case For Everything |
| Emphasis | Real italics for titles of works and quotations | Faux italics; one italic or coloured word in every heading |
| Figures | Tabular figures for prices, times and tables | Proportional figures that jiggle in a live clock |
| Colour | Near-black ink on off-white paper, one accent, AA contrast | Grey body text at 3 : 1; gradient-filled headings |
| Effects | None | Outline text, shadows, glitch, every heading split into letters and animated |
| Hand | Real handwriting, scanned | A handwriting font for "personality" |

The numbers have sources. Line length: "45–90 characters"
([Butterick](https://practicaltypography.com/summary-of-key-rules.html)), "anything from 45 to 75
characters … The 66-character line … is widely regarded as ideal"
([Bringhurst, via Rutter](https://webtypography.net/2.1.2)). Body size: "On the web, 15–25 pixels"
([Butterick](https://practicaltypography.com/typography-in-ten-minutes.html)), "at least … 16px"
([USWDS](https://designsystem.digital.gov/components/typography/)). Line height: "120–145% of the point
size" ([Butterick](https://practicaltypography.com/summary-of-key-rules.html)), and long texts "at least
1.5" ([USWDS](https://designsystem.digital.gov/components/typography/)). Capitals: "always add 5–12%
extra letterspacing to text in all caps or small caps", while "lowercase letters don't ordinarily need
letterspacing" ([Butterick](https://practicaltypography.com/letterspacing.html)). Accessibility: text
contrast of at least 4.5 : 1, or 3 : 1 for large text
([WCAG 2.2, 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)), and layouts that
survive 1.5 line height and 0.12 em letter spacing
([WCAG 2.2, 1.4.12](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html)). Optical sizes:
with an `opsz` axis, browsers apply optical sizing by default
([MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/font-optical-sizing)).

### 1.4 Licences, in practice

| Licence | What it allows on a website | Where you meet it |
|---|---|---|
| **Open** (SIL OFL, Apache, GUST) | Commercial use; self-host, subset and convert; keep the licence with the files. A *Reserved Font Name* (Mona Sans has one) means a modified file must be renamed ([OFL FAQ](https://openfontlicense.org/ofl-faq/)) | Google Fonts, Velvetyne, Collletttivo, most GitHub releases |
| **Free, proprietary** (Indian Type Foundry's FFL on Fontshare) | Commercial web use from your own site, but subsetting or format conversion counts as a derivative work and needs ITF's written consent, and no redistribution, public repositories included (`website/src/fonts/LICENSE-fonts.md`; [FFL](https://www.fontshare.com/licenses/itf-ffl)) | Fontshare: Satoshi, Clash, Switzer, Gambetta… |
| **Free for personal use only** | Not a commercial website. Pangram Pangram: "free to try for personal use as long as it is not used in a commercial project" ([FAQ](https://pangrampangram.com/pages/faq)); its paid licences last "one year … after which the License must be renewed" ([EULA §2.1](https://pangrampangram.com/pages/eula)) | Pangram Pangram, many trial downloads |
| **Paid retail, perpetual** | One-time fee, self-hosted, priced by traffic or company size: Klim ([licences](https://klim.co.nz/licences/)), Grilli Type ([information](https://www.grillitype.com/information)), Commercial Type ([FAQ](https://commercialtype.com/faqs)), Dinamo, which allows self-hosting and subsetting with no traffic limit ([licences](https://abcdinamo.com/licenses)), Displaay ([licences](https://displaay.net/help/licenses)) | The independent foundries most studios buy from |
| **Adobe Fonts** | Included with Creative Cloud and "cleared for both personal and commercial use"; for websites you "Create a Web Project", and self-hosting is a separate purchase from the foundry ([Adobe Fonts](https://fonts.adobe.com/fonts/prestige-elite)) | Neue Haas Grotesk, Aktiv Grotesk, Acumin, Freight, Futura PT… |

Rough prices for a website: Commercial Type's Graphik is US$400 a family, $1,300 the whole collection,
perpetual ([Commercial Type](https://commercialtype.com/catalog/graphik)); Colophon's Apercu is US$768
for the family at the entry licence ([MyFonts](https://www.myfonts.com/collections/apercu-font-colophon-foundry));
Neue Haas Grotesk's family pack is US$344.99 ([MyFonts](https://www.myfonts.com/collections/neue-haas-grotesk-font-linotype));
Displaay's Roobert family is €264–660 ([Displaay](https://displaay.net/typeface/roobert/)); Pangram
Pangram's Neue Montreal family is US$430–1,710 a year ([Pangram Pangram](https://pangrampangram.com/products/neue-montreal.json)).
For a small studio site, budget a few hundred dollars a family.

### 1.5 What makes type read as AI-generated

It is rarely one font. It is a default font plus a default pattern.

**The evidence.**
- Anthropic, on its own model: asked for a landing page without guidance, an LLM "will almost always
  conform to Inter fonts, purple gradients on white backgrounds, and minimal animations", because "safe
  design choices … dominate web training data"
  ([Claude blog, Nov 2025](https://www.claude.com/blog/improving-frontend-design-through-skills)).
- The starter kits ship the defaults: Next.js's `create-next-app` and shadcn/ui's template load Geist
  ([Next.js template](https://raw.githubusercontent.com/vercel/next.js/canary/packages/create-next-app/templates/app-tw/ts/app/layout.tsx),
  [shadcn/ui template](https://raw.githubusercontent.com/shadcn-ui/ui/main/templates/next-app/app/layout.tsx)),
  and v0 builds on shadcn/ui ([v0 docs](https://v0.app/docs/design-systems)).
- The second wave came from the fix. Anthropic's prompting cookbook banned "Inter, Roboto, Open Sans,
  Lato" and recommended, among others, "Playfair Display, Crimson Pro, Fraunces", "Clash Display,
  Satoshi, Cabinet Grotesk" and "Bricolage Grotesque, Obviously, Newsreader"
  ([cookbook](https://raw.githubusercontent.com/anthropics/claude-cookbooks/main/coding/prompting_for_frontend_aesthetics.ipynb)).
  Those are now the faces generated sites converge on.
- Design-review tools now list them. Impeccable's ban list: "Fraunces · Newsreader · Lora · Crimson ·
  Crimson Pro · Crimson Text · Playfair Display · Cormorant · Cormorant Garamond · Syne · IBM Plex Mono
  · IBM Plex Sans · IBM Plex Serif · Space Mono · Space Grotesk · Inter · DM Sans · DM Serif Display · DM
  Serif Text · Outfit · Plus Jakarta Sans · Instrument Sans · Instrument Serif"
  ([Impeccable](https://raw.githubusercontent.com/pbakaus/impeccable/b210dd71e73e1b289b1e2f2407ad3b1458dc632e/skill/reference/brand.md)).
  The Taste skill bans "Fraunces and Instrument_Serif (the two LLM-favorite display serifs)"
  ([Taste skill](https://raw.githubusercontent.com/Leonxlnx/taste-skill/3c7017d636c3a4aad378433ea6d0cfa6c921da4a/skills/taste-skill/SKILL.md)).
- The patterns, in Anthropic's current frontend-design skill, "the commonest tells of a generated
  page": "Accenting just a single word or phrase in a headline, like putting one word in italic/bold or
  a different color", "a tracked-out ALL-CAPS eyebrow label above every heading", "a monospace face for
  small data labels", and "a warm cream background (near #F4F1EA) with a high-contrast serif display"
  ([frontend-design SKILL.md](https://raw.githubusercontent.com/anthropics/skills/main/skills/frontend-design/SKILL.md)).
  Impeccable calls "an oversized italic serif headline … a familiar shortcut to an editorial look"
  ([Impeccable](https://impeccable.style/slop)).

**How common those faces are.** Google Fonts ranks its 1,950 families by use
([metadata](https://fonts.google.com/metadata/fonts), saved 23 Oct 2026). Against that, how many of the
185 studio sites in `STUDIO_FONTS.md` load each face:

| Face | Google Fonts rank | Studios loading it | Note |
|---|---|---|---|
| Inter | 5 | 8 | 4 of them Indian studios; also Linear's product face ([Linear](https://linear.app/now/how-we-redesigned-the-linear-ui)) |
| Montserrat | 7 | 2 | |
| Poppins | 8 | 5 | 3 Indian studios |
| DM Sans | 20 | 1 | |
| Playfair Display | 22 | 0 | |
| Manrope | 28 | 1 | |
| Outfit | 30 | 0 | |
| Plus Jakarta Sans | 32 | 2 | |
| Space Grotesk | 48 | 0 | |
| Bricolage Grotesque | 55 | 0 | |
| Cormorant Garamond | 59 | 0 | |
| Instrument Serif | 71 | 1 | Instrument, which made it |
| Fraunces | 74 | 0 | Bombay Sweet Shop, a brand, uses it |
| Geist | 79 | 1 | Basement Studio, which co-made it |
| Satoshi, Clash, Cabinet Grotesk (Fontshare) | not on Google | 2, 1, 1 | Studio Sorted loads Satoshi and Cabinet |

Only 14% of the studios load any of these faces, and 7% of the global agencies: Pearlfisher (Inter)
and Instrument, which drew Instrument Sans and Serif itself. Among Indian studios it is 35%
(`STUDIO_FONTS.md` §5.9). The fonts that make a site look generated are, by and large, the fonts the
leading studios don't use.

**The cure is not a stranger font.** It is fewer fonts, each chosen for a reason the brand can state,
set with care, and real artefacts (a founder's handwriting, a custom wordmark, real photographs) where
a template would put decoration.

### 1.6 Free alternatives to the paid favourites

Published "alternative" lists measure category, not character: FontAlternatives puts Inter first for
eight of nine paid grotesks it lists ([e.g. Söhne](https://fontalternatives.com/alternatives/sohne/),
[method](https://fontalternatives.com/methodology/)), and Typewolf sells its list
([Typewolf](https://www.typewolf.com/free-fonts)). So the right-hand column below is a type director's
judgement, checked for licence (all OFL unless noted) and for not being on the AI-default lists in §1.5.

| Paid favourite | Free stand-in | How close | Note |
|---|---|---|---|
| Helvetica / Neue Haas Grotesk | TeX Gyre Heros (GUST) | Close in shape | URW's Nimbus Sans is the better-made clone ([FontAlternatives: 92%](https://fontalternatives.com/alternatives/helvetica/)), but it is on Adobe Fonts, not free |
| Söhne, Akkurat, Suisse Int'l | Schibsted Grotesk | Same register | Drawn by the studio Bakken & Bæck for Schibsted; ₹ included ([Fonts In Use](https://fontsinuse.com/typefaces/245321/schibsted-grotesk)) |
| GT America, Franklin Gothic | Libre Franklin; Archivo | Close in genre | Libre Franklin reinterprets Benton's 1912 Franklin Gothic ([Google](https://fonts.google.com/metadata/fonts/Libre%20Franklin)); Archivo is "reminiscent of late 19th-century American typefaces", with widths 62–125 ([Google](https://fonts.google.com/metadata/fonts/Archivo)) |
| Founders Grotesk | Familjen Grotesk | Same spirit | Weights 400–700 only |
| ABC Diatype Expanded, Aktiv Grotesk Extended | Archivo or Mona Sans at wdth 112–125 | Close | Mona Sans reads as GitHub's typeface ([Fonts In Use](https://fontsinuse.com/typefaces/216927/mona-sans)) |
| Graphik | Schibsted Grotesk | Same register | |
| Circular, Futura | Jost | Close in genre | Futura-like geometric; avoid Poppins and Montserrat (§1.5) |
| Tiempos, Lyon | Source Serif 4; Literata | Same job | Both have optical sizes; Newsreader and Lora are on the ban lists |
| Clarendon, Sentinel | Besley | Close | "An antique slab serif inspired by Robert Besley's Clarendon" ([Google](https://fonts.google.com/metadata/fonts/Besley)) |
| Martina Plantijn, Plantin | EB Garamond (loosely) | Distant | No free Plantin of the same quality |
| Canela, GT Sectra, Editorial New, Ogg | No honest free match | — | The free "matches" offered are Fraunces and Playfair ([e.g.](https://fontalternatives.com/alternatives/canela/)), the two most generated-looking serifs |
| GT Alpina Typewriter, Pitch | Courier Prime | Genre only | "A more refined version of IBM's 1956 Courier" ([Google](https://fonts.google.com/metadata/fonts/Courier%20Prime)) |
| Söhne Mono, Diatype Mono | Fragment Mono | Close | "Derived from Nimbus Sans, itself based on Helvetica" ([Google](https://fonts.google.com/metadata/fonts/Fragment%20Mono)) |

### 1.7 The classes, in one line each

| Class | What it looks like | Examples (paid → free) |
|---|---|---|
| Neo-grotesk | The Helvetica family tree: closed apertures, even colour, neutral | Neue Haas Grotesk, Suisse Int'l, Neue Montreal, Akkurat, Unica77, ABC Diatype → TeX Gyre Heros, Schibsted Grotesk |
| Grotesque | Older 19th-century grotesks: uneven widths, more character | Founders Grotesk, Söhne, ABC Monument Grotesk, Theinhardt, Basis → Archivo, Familjen Grotesk |
| American gothic | Franklin and News Gothic lineage: sturdy, printed-ephemera warmth | GT America, Benton Sans, Franklin Gothic → Libre Franklin, Public Sans |
| Humanist sans | Calligraphic skeleton, open apertures, friendlier | Whitney, Frutiger, FF Meta → Fira Sans, Source Sans 3 |
| Geometric sans | Circle-and-line letters (Futura lineage) | Futura, Circular, Brandon, Avenir → Jost |
| DIN / industrial | Engineered, squared curves | DIN 2014, FF DIN → D-DIN, Barlow |
| Condensed / extended | Width as the voice: posters, mastheads, labels | Druk, Founders Grotesk X-Condensed / Diatype Expanded, Aktiv Grotesk Extended → Archivo, Mona Sans, Anek (width axes) |
| Old-style (Garalde) serif | Renaissance book faces: diagonal stress, low contrast | Plantin, Martina Plantijn, Sabon, Caslon → EB Garamond, Libre Caslon |
| Transitional serif | 18th-century: vertical stress, crisper | Baskerville, Times, Untitled Serif → Source Serif 4, Libre Baskerville |
| Contemporary editorial serif | Modern serifs drawn for magazines and screens | Tiempos, Portrait, Lyon, GT Sectra, Freight → Literata, Source Serif 4 |
| Didone / high-contrast | Hairline-and-thick fashion serifs | Didot, Bodoni, Saol, Canela, Editorial New → Bodoni Moda |
| Slab / Clarendon | Heavy bracketed or square serifs, Victorian printing | Sentinel, Clarendon, Archer → Besley, Zilla Slab |
| Soft serif | Rounded, Cooper-like, playful | Cooper, Recoleta, Quincy → Young Serif |
| Grotesk mono | A grotesk drawn monospaced: the technical-label voice | Diatype Mono, Founders Grotesk Mono, Söhne Mono → Fragment Mono, Martian Mono |
| Typewriter | Slab-serifed monospace | GT Alpina Typewriter, Pitch, Prestige Elite → Courier Prime, Cutive Mono |
| Script / handwriting | Pen or brush letters | Better drawn by a person than typeset |

---

## 2. By kind of company

### 2.1 Luxury and fashion

**What works.** Restraint. The house's logo carries the identity and the site's type stays small,
quiet and widely spaced: a geometric sans or a neo-grotesk for navigation and product data, often the
plainest face available, and at most one sharp or high-contrast serif used very large and very rarely
(a campaign word, a masthead, a jewellery collection). The top houses commission their own sans.
**Why:** luxury signals that it does not need to shout; the photography sells.

**In the examples.** Geometric sans is the house voice of fashion sites (Jacquemus, ALAÏA, Céline's
custom face, Nicobar's Euclid Flex); restraint itself reads as luxury (Balenciaga's plain Arial, Raw
Mango's Assistant with D-DIN); serifs appear as heritage or couture signals rather than text (Carolina
Bucci, Nicobar's Didone); at the top end the mark, and often the type, is custom.

**Roles.** Display: the wordmark, plus an occasional sharp serif at 80 px and up. Text: a geometric or
neo-grotesk sans at 12–15 px with generous leading. Labels: the same sans in capitals, +8–12%.

**Premium vs cheap.** Premium is small type, big margins, few words and one family. Cheap is a
"luxury" script, gold gradients, Playfair or Cormorant everywhere, and bold capitals shouting prices.

**Avoid.** Playfair Display, Cormorant, Cinzel and Bodoni Moda as shortcuts to "elegant"; Montserrat
in capitals.

| Brand | Faces | Classes | Source |
|---|---|---|---|
| Jacquemus (Paris) | Futura PT | geometric sans | [census](https://www.jacquemus.com) |
| ALAÏA (Paris) | TT Norms throughout | geometric sans | [The Brand Identity](https://the-brandidentity.com/project/akqa-paris-sculpts-ala%C3%AFas-digital-flagship-around-couture-precision) |
| Céline, 2008–18 | Custom geometric sans after Semplicità (Hannes Famira) | custom geometric sans | [Fonts In Use](https://fontsinuse.com/uses/32996/celine-2008-18) (identity) |
| Balenciaga, 2017 site | Arial, deliberately plain | neo-grotesk (system) | [Fonts In Use](https://fontsinuse.com/uses/16468/balenciaga-website-2017) |
| Carolina Bucci (jewellery, London) | Cardinal, Portrait, Neue Haas Unica | serifs + neo-grotesk | [Typewolf](https://www.typewolf.com/site-of-the-day/carolina-bucci) |
| Nicobar (New Delhi) | Euclid Flex, NewParis Text | geometric sans + Didone | [census](https://www.nicobar.com) |
| Raw Mango (New Delhi) | Assistant, D-DIN | gothic + DIN | [census](https://www.rawmango.com) |

**Free alternatives.** Futura → Jost. Helvetica → TeX Gyre Heros. A Didone for a rare display word →
Bodoni Moda, which has optical sizes, used large and never for text.

### 2.2 Beauty and wellness

**What works.** Clinical trust with warmth: a neo-grotesk or grotesk for ingredient-heavy text, with
a refined or slightly odd serif for product names, or a flared, Optima-like face. Apothecary brands use
typed labels. **Why:** people read ingredient lists and instructions at 12–14 px; the text face must
be legible and calm, and the display face gives the product its character.

**In the examples.** The commonest pairing is a serif display over a grotesk text face
([Dior](https://fontsinuse.com/uses/63917/dior-fragrance-and-beauty), [Jo
Malone](https://fontsinuse.com/uses/46125/jo-malone-2019-brand-overhaul), Flamingo Estate, Kulfi Beauty,
Namaskar Ayurved, Kama Ayurveda). Brands positioned as modern or clinical go all-sans (Glossier,
Ceremonia), and Basis Grotesque recurs as the text face. Ayurveda brands in India reach for sharp or
transitional serifs to signal tradition.

**Roles.** Display: a characterful serif or flared sans for names and campaigns. Text: neo-grotesk or
grotesk. Labels: capitals or a typewriter on packaging-style labels.

**Premium vs cheap.** Premium sets ingredient lists like a pharmacy label: small, clear, aligned.
Cheap is thin geometric capitals, pastel script logos and the 2020 direct-to-consumer recipe of a soft
serif with a rounded sans.

**Avoid.** Montserrat Light in capitals, Cormorant, Playfair, script logos.

| Brand | Faces | Classes | Source |
|---|---|---|---|
| Aesop (Melbourne) | Suisse Int'l, Zapf Humanist (Optima-style) | neo-grotesk + flared humanist | [census](https://www.aesop.com) |
| Glossier, 2016 site | Apercu | grotesk | [Typewolf](https://www.typewolf.com/site-of-the-day/glossier) |
| Ceremonia (haircare) | Nimbus Sans, Basis Grotesque | neo-grotesk + grotesk | [Typewolf](https://www.typewolf.com/site-of-the-day/ceremonia) |
| Flamingo Estate | Ortica (open-source serif), Maison Neue | serif + neo-grotesk | [Typewolf](https://www.typewolf.com/site-of-the-day/flamingo-estate-2023) |
| Kulfi Beauty (South Asian-inspired) | Flecha, Basis Grotesque | broad-nib serif + grotesk | [Typewolf](https://www.typewolf.com/site-of-the-day/kulfi-beauty) |
| Namaskar Ayurved (India) | Voyage, Galano Grotesque, Basis Grotesque | display serif + sans | [Fonts In Use](https://fontsinuse.com/uses/51806/namaskar-ayurved) |
| Kama Ayurveda (New Delhi) | Bell MT, Barlow | transitional serif + DIN-like sans | [census](https://www.kamaayurveda.com) |

**Free alternatives.** Apercu or Basis Grotesque → Familjen Grotesk or Archivo. Optima → no close free
face; leave it.

### 2.3 Food, drink, craft and lifestyle

**What works.** Personality is allowed: condensed or soft serifs, American gothics, extended
grotesques, typewriters, lettering lifted from the packaging, over one sturdy text face. **Why:** these
brands sell taste and provenance; the display type can carry flavour as long as the text stays plain.

**In the examples.** Soft, retro serifs over friendly geometric sans are this category's signature in
the census ([Bombay Sweet Shop](https://bombaysweetshop.com), [Fishwife](https://eatfishwife.com), East
Fork, [Blue Tokai](https://bluetokaicoffee.com), [Diaspora Co.](https://www.diasporaco.com)), which is
exactly why the look now feels generic. The stronger brands hold one sharper voice: Graza's typewriter,
Heath Ceramics' extended grotesque, The Whole Truth's Obviously. Indian brands plan for Indian scripts
too: [Manam Chocolate](https://thehardcopy.co/brand-case-study-manam-chocolates/) pairs its Latin faces
with Anek.

**Roles.** Display: the characterful face, large. Text: a sturdy grotesk, gothic or text serif.
Labels: a typewriter or gothic capitals, like a shop label.

**Premium vs cheap.** Premium has one flavourful face and the rest quiet. Cheap is two or three novelty
faces, a handwriting font for "homemade", and the 2019–22 DTC look (Recoleta or Cooper with a rounded
sans, or Fraunces).

**Avoid.** Fraunces, Recoleta-by-default, Patrick Hand-style handwriting fonts.

| Brand | Faces | Classes | Source |
|---|---|---|---|
| Graza (olive oil, US) | GT Alpina Typewriter, ITC Garamond Condensed, Apercu | typewriter + condensed Garalde + grotesk | [census](https://www.graza.co) |
| Heath Ceramics (Sausalito) | Grotesque MT Bold Extended, Benton Sans, Century Schoolbook | extended grotesque + gothic + schoolbook | [census](https://www.heathceramics.com) |
| East Fork (pottery) | Quincy, Galano Classic | soft serif + geometric | [census](https://eastfork.com) |
| Subko (Mumbai) | Dashiell Bright, IBM Plex Sans; Kannada in its multi-script marquee | display + grotesk | [census](https://subko.coffee) |
| The Bombay Canteen (Mumbai) | Murden, Soleil | display + geometric | [census](https://www.thebombaycanteen.com) |
| The Whole Truth (Mumbai) | Obviously, Obviously Narrow, IBM Plex Mono | width-family grotesque + mono | [census](https://thewholetruthfoods.com) |
| Dosa Coffee (India) | Modified Rustica logo, Basic Sans | custom display + sans | [Fonts In Use](https://fontsinuse.com/uses/64170/dosa-coffee-identity-and-packaging) (identity) |

**Free alternatives.** GT Alpina Typewriter → Courier Prime. An extended grotesque → Archivo at wdth
112–125. Century Schoolbook → TeX Gyre Schola (GUST).

### 2.4 Architecture and interiors

**What works.** Neo-grotesks and grotesques at small sizes on a strict grid, lots of white, often one
weight and one size; sometimes a refined text serif for essays; occasionally a face drawn from the
practice's own material (stone, typewriter, drawings). **Why:** the work is visual and spatial; type
should behave like a drawing's title block.

**In the examples.** Practices favour single-family sans systems at light weights and small sizes
(Barrault Pressacco, Field Office, Nickl & Partner, Feilden Fowles); interiors and home brands add a
serif for warmth and material (In Common With, [Hannun](https://fontsinuse.com/uses/75981/hannun),
[Heath Ceramics](https://www.heathceramics.com)); and type is often drawn from the building or the
archive (Feilden Fowles's stone-cut cues, Frank Lloyd Wright's typewriter).

**Roles.** Display: often none, or the text face larger. Text: neo-grotesk or grotesk. Labels: the same,
small.

**Premium vs cheap.** Premium is one family, two sizes, a grid you can feel. Cheap is ultra-thin
geometric capitals, Futura-for-architects clichés and display type competing with the photographs.

| Practice | Faces | Classes | Source |
|---|---|---|---|
| Barrault Pressacco (France) | Union, one weight, one size (9.2 pt) | neo-grotesk | [The Brand Identity](https://the-brandidentity.com/project/republique-studios-identity-architecture-firm-barrault-pressacco-masterclass-brutalism) (identity) |
| Field Office Architecture (Australia) | ABC Monument Grotesk throughout | grotesque | [The Brand Identity](https://the-brandidentity.com/project/spgd-creates-subliminal-subtle-sophisticated-identity-system-field-office-architecture) (identity) |
| Feilden Fowles (UK) | Piloti, custom by A Practice for Everyday Life | custom sans | [Fonts In Use](https://fontsinuse.com/uses/78012/feilden-fowles) |
| Nickl & Partner (Germany) | Neue Frutiger | humanist sans | [Fonts In Use](https://fontsinuse.com/uses/74039/nickl-and-partner-architekten-website) |
| In Common With (lighting) | Stanley, Calibre | Times-derived serif + grotesk | [Typewolf](https://www.typewolf.com/site-of-the-day/in-common-with) |
| Frank Lloyd Wright Building Conservancy | Reply, after Wright's typewriter (Order) | typewriter-derived geometric | [The Brand Identity](https://the-brandidentity.com/project/order-turns-frank-lloyd-wrights-red-square-into-a-symbol-of-community) (identity) |

**Free alternatives.** Monument Grotesk or Union → Archivo or Schibsted Grotesk. Frutiger → Source Sans
3 or Fira Sans.

### 2.5 Editorial and media

**What works.** A text serif with optical sizes for long reading, a display cut or a contrasting serif
for headlines, a grotesk for navigation, bylines and data. **Why:** comfort over thousands of words,
and authority.

**In the examples.** Long-read sites use three voices: a headline face, a text serif and a small sans
for details (The Free Press, The Juggernaut, [AFAR](https://www.typewolf.com/site-of-the-day/afar)).
Newspapers commission their own families (the FT, The Guardian) or adopt a news serif (Mid-Day's
Sindelar). Art and design titles go sans-led and let the pictures speak ([Flash
Art](https://www.typewolf.com/site-of-the-day/flash-art),
[Apartamento](https://www.apartamentomagazine.com), It's Nice That).

**Roles.** Display: a serif display cut, or a grotesk for news. Text: an editorial or transitional text
serif at 18–21 px. Labels: a grotesk or gothic.

**Premium vs cheap.** Premium is a measure of 60–70 characters, real italics and small caps, and
consistent figures. Cheap is long reads in a light sans at 15 px, 90-character lines, and a display serif
with no text-size companion.

| Publication | Faces | Classes | Source |
|---|---|---|---|
| The Guardian | Guardian Egyptian, Guardian Text Egyptian, Guardian Sans | slab + sans superfamily | [Commercial Type](https://commercialtype.com/catalog/guardian_egyptian) (identity) |
| Financial Times | Financier Display and Text | editorial serif | [Klim](https://klim.co.nz/blog/financier-design-information/) (identity) |
| The Free Press | Galaxie Copernicus, Tiempos Text, American Grotesk | editorial serifs + gothic | [Typewolf](https://www.typewolf.com/site-of-the-day/the-free-press) |
| It's Nice That | Labil Grotesk, Bradford | grotesk + text serif | [Typewolf](https://www.typewolf.com/site-of-the-day/its-nice-that-2020) |
| The Juggernaut (South Asian media) | Custom display by Shiva Nallaperumal (November, Bombay), Sentient, Oli Grotesk | custom display + text serif + grotesk | [Pentagram](https://www.pentagram.com/work/the-juggernaut/story) |
| Hole & Corner | GT Super, Sabon, GT America | Didone + Garalde + gothic | [census](https://www.holeandcorner.com) |
| Mid-Day (Mumbai) | Sindelar, Benton Sans | newspaper serif + gothic | [Fonts In Use](https://fontsinuse.com/uses/17297/mid-day) (identity) |

**Free alternatives.** Tiempos or Lyon → Source Serif 4 or Literata. Guardian Egyptian → Besley.

### 2.6 Culture, arts and museums

**What works.** A strong grotesk or a custom institutional face with many weights and wide language
support, used as a flexible base; exhibitions and programmes add their own display faces on top.
**Why:** the institution must stay recognisable while its programme changes every season.

**In the examples.** Institutions own bespoke faces (KNMA, the Philadelphia Museum of Art, MoMA,
[Tate](https://fontsinuse.com/typefaces/240671/tatenew)); serif plus grotesk is the common pairing
(PAMM, [The Huntington](https://fontsinuse.com/uses/77683/the-huntington), [Jhaveri
Contemporary](https://the-brandidentity.com/project/sthuthi-ramesh-rebrands-jhaveri-contemporary-utmost-consideration-context-detail),
whose type draws on Sudhakar Nadkarni's hand-lettered milk kiosks), and MAP Bengaluru reverses it with a
geometric sans first. India has the richest verified set in this category: MAP, KNMA,
[CSMVS](https://thehardcopy.co/refreshing-the-visual-identity-for-csmvs-earlier-prince-of-wales-museum/),
Jhaveri Contemporary and Khoj.

**Roles.** Display: the institutional face or a per-exhibition face. Text: the same family, or a plain
companion. Labels: the institutional face, small.

**Premium vs cheap.** Premium is a system that can carry a new artist every month. Cheap is an "arty"
decorative face as the base, and English-only coverage in a multilingual city.

| Institution | Faces | Classes | Source |
|---|---|---|---|
| Museum of Art & Photography (MAP), Bengaluru | Geometria, Leitura News | geometric sans + news serif | [The Hard Copy](https://thehardcopy.co/designing-the-brand-identity-for-a-contemporary-museum/) (identity) |
| Kiran Nadar Museum of Art, New Delhi | KNMA Zubtrak, bespoke and jali-inspired | custom stencil serif | [KNMA](https://www.knma.org/about/brand-story/) (identity) |
| MoMA | MoMA Sans (Commercial Type) | custom gothic | [type.today](https://type.today/en/journal/moma_sans) (identity) |
| Philadelphia Museum of Art | Fairmount Serif (custom), ES Klarheit Grotesk, rotating display faces | custom serif + grotesk | [Fonts In Use](https://fontsinuse.com/uses/73911/philadelphia-museum-of-art-identity) (identity) |
| Pérez Art Museum Miami | GT Alpina, Neue Haas Grotesk | serif + neo-grotesk | [Typewolf](https://www.typewolf.com/site-of-the-day/pamm) |
| Khoj Studios, New Delhi | Roobert, Cooper | geometric grotesk + soft serif | [Typewolf](https://www.typewolf.com/site-of-the-day/khoj-studios) |
| Factory International, Manchester | Gräbenbach Mono, capitals for headlines | grotesk mono | [Fonts In Use](https://fontsinuse.com/uses/67815/factory-international-in-manchester) |

**Free alternatives.** Neue Haas Grotesk → TeX Gyre Heros. A custom-feeling grotesk → Schibsted
Grotesk or Archivo with its widths.

### 2.7 Branding and design studios

**What works.** One well-made grotesk family does almost everything, often with its monospaced
sibling for labels; about a fifth pair it with a serif; the biggest agencies commission their own
faces. **Why:** a studio's site frames its portfolio. The work must be the loudest thing on the page,
and the type shows judgement through restraint and craft.

**Roles.** Display: the grotesk, big and tight, or a serif for one voice. Text: the grotesk. Labels: the
grotesk small, or its mono.

**Premium vs cheap.** Premium is a paid or carefully chosen free face, two weights, the work given the
room. Cheap is a template face, mono for everything, marquee type and the italic-word hero.

**The numbers** (`STUDIO_FONTS.md` §5): 83% of 185 studios load a sans, 46% a neo-grotesk, 30% a serif,
14% a mono, 2% a script or handwriting. 82% load one or two families. 72% load at least one paid face;
14% load one of the AI-default faces.

| Studio | Faces | Classes | Source |
|---|---|---|---|
| Pentagram | Plain | neo-grotesk | [census](https://www.pentagram.com) |
| Collins | Portrait, Graphik | editorial serif + neo-grotesk | [census](https://www.wearecollins.com) |
| Koto | GT Kotoheim, Condensed and Mono (custom) | custom geometric + mono | [census](https://koto.com/) |
| Ragged Edge | ABC Diatype, ABC Diatype Expanded | neo-grotesk + extended | [census](https://www.raggededge.com/) |
| Mother Design | Basis Grotesque, Basis Grotesque Mono | grotesque + mono | [census](https://www.motherdesign.com) |
| Codesign (Gurugram) | Sentinel, Whitney | slab + humanist sans | [census](https://www.codesign.in/) |
| Locopopo (Mumbai) | Aktiv Grotesk, Aktiv Grotesk Extended | neo-grotesk + extended | [census](https://locopopo.com/) |
| November (Mumbai) | Delegate and Delegate Mono, drawn by November's Shiva Nallaperumal for Commercial Type | American gothic + mono | [census](https://www.nvmbr.in/), [Commercial Type](https://commercialtype.com/catalog/delegate) |

**Free alternatives.** See §1.6; for a studio, Schibsted Grotesk or Archivo with Courier Prime or
Fragment Mono.

### 2.8 Tech, SaaS and AI

**What works.** A neo-grotesk or grotesque that renders well at 13–15 px, with tabular figures and a
mono for code and data. AI companies increasingly add a serif for warmth. **Why:** interfaces need
legibility, alignment and a technical voice.

**In the examples.** AI companies' signature is a bookish serif display over a grotesque text face
(Claude, OpenAI, [Kin](https://www.typewolf.com/site-of-the-day/kin-ai),
[Delphi](https://www.typewolf.com/site-of-the-day/delphi-ai)), and that look is now itself on the list
of generated-page tells (§1.5). Developer tools keep to one grotesque, often their own (Stripe, Linear,
Vercel, [Retool](https://www.typewolf.com/site-of-the-day/retool)). Indian tech either licenses a
display face over Inter (Razorpay) or owns a custom face (Zoho Puvi).

**Roles.** Display: the grotesk, or a serif for marketing pages. Text: the grotesk. Labels: the grotesk
or its mono.

**Premium vs cheap.** Premium is a custom or paid grotesk tuned for the product. Cheap is Inter or Geist
because the template shipped with them, a purple gradient, Space Grotesk, and the serif-italic hero.

| Company | Faces | Classes | Source |
|---|---|---|---|
| Stripe | Söhne | grotesque | [Fonts In Use](https://fontsinuse.com/uses/35338/stripe-website-2020) |
| OpenAI | Signifier, Söhne | serif + grotesque | [Typewolf](https://www.typewolf.com/site-of-the-day/openai) |
| Claude (Anthropic) | Galaxie Copernicus, Tiempos Text, Styrene | serifs + geometric sans | [Typewolf](https://www.typewolf.com/site-of-the-day/claude) |
| Linear | Inter Display, Inter | neo-grotesk | [Linear](https://linear.app/now/how-we-redesigned-the-linear-ui) |
| Vercel | Geist Sans, Geist Mono | neo-grotesk + mono | [Vercel](https://vercel.com/font) |
| Razorpay (Bengaluru) | TASA Orbiter, Inter | grotesque + neo-grotesk | [Razorpay Blade tokens](https://raw.githubusercontent.com/razorpay/blade/master/packages/blade/src/tokens/global/fontFamily/fontFamily.web.ts) |
| Zoho (Chennai) | Zoho Puvi (custom) | custom sans | [Zoho](https://www.zoho.com/blog/general/introducing-puvi-from-zoho.html) |

**Free alternatives.** Söhne → Schibsted Grotesk; Söhne Mono → Fragment Mono; Signifier or Tiempos →
Source Serif 4.

### 2.9 Finance and legal

**What works.** Transitional or contemporary serifs for trust and seriousness, a neo-grotesk for the
product, tabular lining figures wherever numbers matter. Newer fintechs use one confident custom sans.
**Why:** credibility, and numbers that line up.

**In the examples.** Large institutions commission a custom sans and add a classical serif for gravitas
(Goldman Sachs, Robinhood, Wise); neobanks run one family everywhere (Revolut). Fintech start-ups copy
the AI-site formula of serif headline, grotesk text and mono figures (Vesto,
[Origin](https://www.typewolf.com/site-of-the-day/use-origin)), common enough now to read as "Silicon
Valley". Law firms pair a contemporary serif with a Swiss grotesque (Haavind, [Cross Border
Legalis](https://fontsinuse.com/uses/57457/cross-border-legalis)).

**Roles.** Display: a serif or a custom sans. Text: neo-grotesk. Labels: the sans with tabular figures.

**Premium vs cheap.** Premium is a sober serif, generous space, figures that align. Cheap is rounded
friendly sans on serious products, bank-blue with Montserrat, and proportional figures in tables.

| Firm | Faces | Classes | Source |
|---|---|---|---|
| Robinhood | Martina Plantijn, Robinhood Phonic (custom, Porto Rocha) | old-style serif + custom sans | [Porto Rocha](https://www.portorocha.com/robinhood) |
| Wise | Wise Sans (custom), Inter | custom display + neo-grotesk | [Type-01](https://type-01.com/wise-sans-the-font-update-shaping-wises-visual-identity/) |
| Revolut | Aeonik Pro | neo-grotesk | [Fonts In Use](https://fontsinuse.com/uses/61484/revolut) |
| Goldman Sachs | Goldman Sans (custom), Sabon | custom sans + Garalde | [Print](https://www.printmag.com/branding-identity-design/the-curious-case-of-goldman-sans/) |
| Haavind (law, Oslo) | STK Bureau Serif, ABC Diatype | serif + neo-grotesk | [Fonts In Use](https://fontsinuse.com/uses/63604/haavind) |
| Vesto (treasury) | Tiempos Headline, Lausanne | editorial serif + neo-grotesk | [Typewolf](https://www.typewolf.com/site-of-the-day/get-vesto) |
| AMU Leasing (India) | Komet, Arpona Sans, Anek for Indian scripts | display + humanist + Indic | [Fonts In Use](https://fontsinuse.com/uses/62597/amu-leasing-identity-and-website) |
| Navi (Bengaluru) | Navi Sans (custom) | custom sans | [Design Stack](https://designstack.com/project/navi/) (identity) |

**Free alternatives.** Tiempos → Source Serif 4; Lausanne or Diatype → Schibsted Grotesk.

### 2.10 Kids and education

**What works.** Rounded, humanist or clear geometric sans with large x-heights; for early readers,
"infant" forms (single-storey a and g); body at 18 px and up; complete coverage of the scripts the
learners read. **Why:** legibility for learners, warmth for parents, and inclusion.

**In the examples.** Consumer learning brands use a chunky, rounded display face over a rounded
interface sans (Duolingo, LEGO Duplo). Learning platforms choose plain humanist sans and plan for many
scripts (Khan Academy, StoryWeaver). Universities use open-source superfamilies so every department can
install them free (Stanford).

**Roles.** Display: a friendly rounded or chunky face. Text: a humanist sans. Labels: the same.

**Premium vs cheap.** Premium is one friendly display face and a calm text face. Cheap is Comic Sans or
its cousins, ten colours and five faces a page, and Latin-only fonts for multilingual learners.

| Organisation | Faces | Classes | Source |
|---|---|---|---|
| Duolingo | Feather Bold (custom), DIN Next Rounded | rounded display + rounded sans | [Fonts In Use](https://fontsinuse.com/uses/59497/duolingo-app) |
| Khan Academy | Lato, Noto Sans and Noto Serif for other scripts, Inconsolata | humanist + Noto + mono | [Khan Academy tokens](https://raw.githubusercontent.com/Khan/wonder-blocks/main/packages/wonder-blocks-tokens/src/theme/primitive/font.ts) |
| LEGO Duplo | Tobi | rounded display | [Fonts In Use](https://fontsinuse.com/uses/40731/lego-duplo) (identity) |
| Stanford University | Source Serif 4, Source Sans 3 | open-source superfamily pair | [Stanford identity](https://identity.stanford.edu/design-elements/typography/) |
| StoryWeaver (Pratham Books, Bengaluru) | Bree Serif, Raleway, Noto Sans for Kannada and nine other South Asian scripts | slab + geometric + Noto | [StoryWeaver source](https://raw.githubusercontent.com/PrathamBooks/sw-web/master/src/scss/_design-tokens.scss) |
| Baboró festival for children | Obviously, Halyard | wide display + geometric | [Fonts In Use](https://fontsinuse.com/uses/41568/baboro-festival-website) |

**Free alternatives.** DIN Next Rounded → Nunito (overexposed) or Baloo 2 (Ek Type); a humanist text
face → Fira Sans or Source Sans 3; Indian scripts → Noto, Anek, Mukta, Baloo.

### 2.11 Hospitality and travel

**What works.** A characterful display (a serif or a condensed face) that says *place*, often drawn
from local signage, the building or the property's history, with a clean grotesk for booking. **Why:**
a hotel or restaurant sells a mood and a location; the booking flow must stay plain.

**In the examples.** Boutique hotels and stays pair a soft, calligraphic or high-contrast serif with a
quiet sans (Narai, Emerald Stay, Hotel Europejski). Big travel brands build custom families that cover
more than one script (Korean Air). Indian luxury hospitality pairs custom lettering with an Indian Type
Foundry sans (The Leela), and Indian café chains go warm and rounded with Ek Type's Latin faces
(Barista).

**Roles.** Display: the characterful serif or custom lettering. Text: a grotesk. Labels: the grotesk.

**Premium vs cheap.** Premium is one place-specific display voice over plain text. Cheap is a script
for "elegance", Cormorant with Montserrat (the template hotel), and generic Didone luxury.

| Business | Faces | Classes | Source |
|---|---|---|---|
| The Leela Palaces, Hotels and Resorts (India) | Custom engraved-style lettering, Kohinoor (Indian Type Foundry) | custom serif lettering + humanist sans | [Indian Type Foundry](https://www.indiantypefoundry.com/customfonts/leela) (identity) |
| Hotel Europejski (Warsaw) | IvyMode, Aktiv Grotesk | high-contrast serif + neo-grotesk | [Fonts In Use](https://fontsinuse.com/uses/45023/hotel-europejski-website) |
| Narai Hospitality Group | Nib, IBM Plex Sans | calligraphic serif + grotesk | [Typewolf](https://www.typewolf.com/site-of-the-day/narai-hospitality-group) |
| Emerald Stay (villas) | Louize, Acumin | soft serif + grotesk | [Typewolf](https://www.typewolf.com/site-of-the-day/emerald-stay) |
| Korean Air | Korean Air Sans (Dalton Maag) with Hangul by Sandoll | custom sans, bilingual | [Dalton Maag](https://www.daltonmaag.com/portfolio/custom-fonts/korean-air-sans.html) (identity) |
| Barista Coffee (India) | Baloo, Mukta (Ek Type) | rounded display + humanist | [Fonts In Use](https://fontsinuse.com/uses/33890/barista-coffee) |

**Free alternatives.** IvyMode or Louize → Literata or Young Serif at display sizes; Aktiv Grotesk or
Acumin → Schibsted Grotesk.

### 2.12 NGOs and non-profits

**What works.** Reach and legibility over flourish: one characterful grotesque, or a warm display face
over a stock text face, with strong weights for campaigns, accessible sizes and contrast, and full
coverage of the languages the audience reads. **Why:** clarity is the brand; the audience is broad,
often multilingual, often on slow phones.

**In the examples.** Big digital non-profits choose reach over flourish: Wikipedia loads no web fonts at
all. Charity identities take one characterful grotesque (One for the World, WWF Market) or a warm serif
with a mono (Ayuda en Acción). Their text faces are often stock (Population Foundation of India's Open
Sans), so the character has to come from the display face.

**Roles.** Display: the one face with character. Text: a highly legible humanist or grotesk sans, or
the system stack. Labels: the text face.

**Premium vs cheap.** Premium is one confident face used consistently from poster to form field. Cheap
is a decorative face, light weights over photographs, capitalised paragraphs, and local scripts left to
whatever the phone falls back to.

| Organisation | Faces | Classes | Source |
|---|---|---|---|
| Wikipedia (Wikimedia) | No web fonts: Linux Libertine or Georgia headings, the device's system sans, Menlo / Consolas | serif headings + system sans | [Wikimedia Codex tokens](https://raw.githubusercontent.com/wikimedia/design-codex/main/packages/codex-design-tokens/src/themes/wikimedia-ui.json) |
| Mozilla | Mozilla Headline, Mozilla Text (custom) | custom family | [Mozilla Protocol](https://protocol.mozilla.org/docs/fundamentals/typography) |
| WWF Market | NN Nouvelle Grotesk | grotesque | [Fonts In Use](https://fontsinuse.com/uses/42674/wwf-market) |
| One for the World | Forma DJR | grotesque | [Fonts In Use](https://fontsinuse.com/uses/50622/one-for-the-world-visual-identity) (identity) |
| Ayuda en Acción (Spain) | Bogart, DM Mono | soft serif + mono | [Fonts In Use](https://fontsinuse.com/uses/42930/ayuda-en-accion-rebranding) |
| Population Foundation of India (Lopez Design) | Sharp Grotesk, Open Sans; only Latin credited | grotesque + humanist | [Fonts In Use](https://fontsinuse.com/uses/46109/population-foundation-of-india) |
| StoryWeaver (Pratham Books) | Bree Serif, Raleway, Noto Sans for ten South Asian scripts | slab + geometric + Noto | [StoryWeaver source](https://raw.githubusercontent.com/PrathamBooks/sw-web/master/src/scss/_design-tokens.scss) |

**Free alternatives.** Forma DJR or NN Nouvelle Grotesk → Archivo or Schibsted Grotesk. For Indian
scripts, a family with a designed sibling (Anek, Mukta, Hind, Noto) rather than a Latin face with
fallbacks.

### 2.13 Indian and bilingual brands (Devanagari, Kannada)

**What works.** Two routes, both visible in Indian practice:
- **Route A, one family drawn across scripts.** Ek Type's Mukta (Devanagari, Gurmukhi, Gujarati,
  Tamil, Latin) and Anek (ten scripts, Kannada included, each with weight *and width* axes) make the
  scripts look like one voice for free.
- **Route B, a bespoke Indic face matched to an existing Latin one.** Indian Type Foundry drew
  Starbucks India's Devanagari with Landor Paris, tuning terminals, conjunct joins and letter height to
  the Latin's visual weight; Tiro drew Nirmala UI's 14 Indian scripts to sit with Segoe.

Indic letters carry vowel signs above and below the line, so they need more line height, and usually
a slightly larger size, than the Latin beside them. The deepest Indian-script type work is in news and
broadcast; many consumer brands still publish Latin-only type and leave Indian scripts to chance.

**Roles.** Display and text in matched pairs, one per script. Labels: the same pair, smaller.

**Premium vs cheap.** Premium is real words in the local script, set in a face drawn for it and
matched by eye. Cheap is "Indian-looking" Latin display fonts that imitate Devanagari strokes, Poppins
for everything, and Kannada left to the system fallback.

| Brand | Faces | Scripts | Source |
|---|---|---|---|
| Biergarten Karnataka food festival (Bengaluru) | Bungee, P22 Underground, and Anek Kannada to "anchor this in local context" | Latin + Kannada | [Fonts In Use](https://fontsinuse.com/uses/73798/biergarten-karnataka-food-festival-2024) (identity) |
| Prajavani (Bengaluru Kannada daily) | Prajavani Text and Headline, custom by Indian Type Foundry; the Headline reverses Kannada's traditional contrast so it can be condensed | Kannada | [Indian Type Foundry](https://www.indiantypefoundry.com/customfonts/prajavani) (identity) |
| Trolley Times (farmers' newspaper) | Mukta, Mukta Mahee, Mukta Latin | Devanagari + Gurmukhi + Latin | [Fonts In Use](https://fontsinuse.com/uses/47673/trolley-times) (identity) |
| Maharashtra Covid campaign | Mukta, Mukta Latin | Devanagari + Latin | [Fonts In Use](https://fontsinuse.com/uses/47914/maharashtra-covid-campaign) (identity) |
| Starbucks India | Custom Devanagari logotype matched to the Latin (ITF with Landor Paris) | Latin + Devanagari | [Indian Type Foundry](https://www.indiantypefoundry.com/customfonts/starbucks) (identity) |
| Lokmat (Marathi daily) | Sama Devanagari (Ek Type) | Devanagari | [Fonts In Use](https://fontsinuse.com/uses/47502/lokmat-newspaper) (identity) |
| Air India, 2023 (FutureBrand) | Air India Sans; Indian-script coverage not stated | Latin | [FutureBrand](https://www.futurebrand.com/work/air-india) (identity) |
| AMU Leasing | Komet, Arpona Sans, Anek for "all scripts" | Latin + Indic | [Fonts In Use](https://fontsinuse.com/uses/62597/amu-leasing-identity-and-website) |

**Kannada faces.** Free: Anek Kannada (Ek Type; variable weight 100–800 and width 75–125), Noto Sans
Kannada and Noto Serif Kannada (Google), Baloo Tamma 2 (Ek Type; rounded), Tiro Kannada (Tiro
Typeworks; a literary serif), Hind Mysuru (Indian Type Foundry). Axes and scripts are from Google
Fonts' metadata ([fonts.google.com/metadata/fonts](https://fonts.google.com/metadata/fonts)). Paid
Kannada retail faces also exist, among them Indian Type Foundry's Kohinoor Kannada and Mota Italic's Fit
Kannada (unverified here).

---

## 3. Quick reference

| Kind of company | Display | Text | Labels | Free starting points | Avoid |
|---|---|---|---|---|---|
| Luxury and fashion | The wordmark; rare sharp or Didone serif, very large | Geometric or neo-grotesk, 12–15 px | Capitals, +8–12% | Jost, TeX Gyre Heros; Bodoni Moda for display only | Playfair, Cormorant, Cinzel, "luxury" scripts |
| Beauty and wellness | Refined serif or flared sans for product names | Neo-grotesk or grotesk | Capitals or a typewriter | Literata or Source Serif 4 with Schibsted Grotesk or Archivo | Montserrat Light capitals, Cormorant, script logos |
| Food, drink, craft | One characterful face: condensed serif, gothic, extended, typewriter | Sturdy grotesk, gothic or text serif | Typewriter or gothic capitals | Archivo (widths), Libre Franklin, Young Serif, Courier Prime | Fraunces, Recoleta by default, handwriting fonts |
| Architecture and interiors | The text face larger, or none | Neo-grotesk or grotesk | Same, small | Schibsted Grotesk, Archivo; Source Serif 4 for essays | Thin geometric capitals, display that competes with photos |
| Editorial and media | Serif display cut, or a grotesk for news | Text serif with optical sizes, 18–21 px | Grotesk or gothic | Source Serif 4, Literata, Besley, with Libre Franklin | Long reads in a light sans; 90-character lines |
| Culture, arts, museums | Strong grotesk or custom face; a display face per show | Same family | Same | Archivo, Schibsted Grotesk; Noto for other scripts | "Arty" decorative base; English only |
| Branding and design studios | The grotesk, big and tight, or one serif voice | The grotesk | The grotesk small, or its mono | Schibsted Grotesk or Archivo, with Fragment Mono or Courier Prime | Satoshi, Clash, Space Grotesk, Syne; the italic-word hero |
| Tech, SaaS, AI | Grotesk; a serif on marketing pages | Grotesk with tabular figures | Mono | Schibsted Grotesk with Fragment Mono; Source Serif 4 | Inter or Geist by default; purple gradients; Space Grotesk |
| Finance and legal | Transitional or editorial serif, or a custom sans | Neo-grotesk | Sans with tabular figures | Source Serif 4 with Schibsted Grotesk | Rounded friendly sans; Montserrat; proportional figures |
| Kids and education | Rounded or chunky display | Humanist sans, 18 px and up | Same | Baloo 2 (Ek Type), Fira Sans, Source Sans 3; Noto, Anek, Mukta for scripts | Comic Sans clones; novelty text faces; Latin-only fonts |
| Hospitality and travel | A place-specific serif, condensed face or custom lettering | Grotesk | Grotesk | Literata or Young Serif for display, Schibsted Grotesk | A script for "elegance"; Cormorant with Montserrat |
| NGOs and non-profits | One characterful grotesque | Humanist or grotesk sans, or the system stack | Same | Archivo, Schibsted Grotesk; Noto, Anek, Mukta | Decorative faces; light weights over photos |
| Indian and bilingual | Matched pair per script | Matched pair per script | Same | Anek (Latin with Kannada or Devanagari), Mukta, Hind, Noto, Tiro | Faux-Devanagari Latin; Poppins everywhere; system fallback |

---

## 4. Sources

**Our own data**
- CSS census of 226 sites, 24 Oct 2026: `research/screens/results.jsonl`; the studio list built from it:
  `research/type/STUDIO_FONTS.md`.
- The verified example tables behind Part 2 (about 160 rows with sources, more than shown here):
  `research/type/data/industries_a.tsv`, `industries_b.tsv`; pattern notes `patterns_a.txt`,
  `patterns_b.txt`; AI-default and setting references `ai_defaults_and_setting.txt`.
- Google Fonts metadata (popularity rank, axes, scripts): https://fonts.google.com/metadata/fonts,
  saved 23 Oct 2026.

**Where faces were verified**
- Fonts In Use: https://fontsinuse.com · Typewolf: https://www.typewolf.com/site-of-the-day
- The Brand Identity: https://the-brandidentity.com · The Hard Copy: https://thehardcopy.co
- Foundries: Klim https://klim.co.nz · Commercial Type https://commercialtype.com · Grilli Type
  https://www.grillitype.com · Dinamo https://abcdinamo.com · Pangram Pangram https://pangrampangram.com
  · Displaay https://displaay.net · Swiss Typefaces https://www.swisstypefaces.com · Indian Type Foundry
  https://www.indiantypefoundry.com · Ek Type https://ektype.in · Tiro Typeworks https://www.tiro.com ·
  Adobe Fonts https://fonts.adobe.com

**Setting and accessibility**
- Matthew Butterick, *Practical Typography*: https://practicaltypography.com
- Richard Rutter, *Web Typography* (Bringhurst applied to the web): https://webtypography.net/2.1.2
- US Web Design System, typography: https://designsystem.digital.gov/components/typography/
- WCAG 2.2, 1.4.3 and 1.4.12: https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html,
  https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html
- Apple Human Interface Guidelines, typography: https://developer.apple.com/design/human-interface-guidelines/typography
- MDN, `font-optical-sizing`: https://developer.mozilla.org/en-US/docs/Web/CSS/font-optical-sizing

**AI defaults**
- Anthropic, "Improving frontend design through skills": https://www.claude.com/blog/improving-frontend-design-through-skills
- Anthropic, frontend-design skill (current): https://raw.githubusercontent.com/anthropics/skills/main/skills/frontend-design/SKILL.md
- Anthropic cookbook, frontend aesthetics: https://raw.githubusercontent.com/anthropics/claude-cookbooks/main/coding/prompting_for_frontend_aesthetics.ipynb
- Impeccable: https://impeccable.style/slop · Taste skill: https://github.com/Leonxlnx/taste-skill
- Next.js and shadcn/ui starter templates (Geist): see §1.5.

**Licences**
- SIL Open Font License FAQ: https://openfontlicense.org/ofl-faq/ · ITF Free Font License:
  https://www.fontshare.com/licenses/itf-ffl · Pangram Pangram EULA: https://pangrampangram.com/pages/eula ·
  Klim: https://klim.co.nz/licences/ · Dinamo: https://abcdinamo.com/licenses · Commercial Type:
  https://commercialtype.com/faqs · Grilli Type: https://www.grillitype.com/information
