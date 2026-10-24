# Studio Kavalu: font shortlist

*24 October 2026 · for brief 3 ("this font is not good … research on the font as well") and queue item
Q14. It draws on `STUDIO_FONTS.md` (195 studios), `FONT_GUIDE.md`, the client's eight references, her
old site and the current build.*

## The answer

**Rank 1: System A, "studio grotesk, typed".** Schibsted Grotesk does every reading job, from the
hero to the footer. A typewriter appears only where the album has typed paper: Courier Prime as now,
tested against Compagnon. Her real handwriting and signature are drawn as SVG, and Anek Kannada carries
Kannada. It is free (all SIL OFL), loads through `next/font/google`, and has the ₹ the current faces lack.

**Gambetta, Switzer, Homemade Apple and Mrs Saint Delafield go. Courier Prime leaves the interface**
and keeps, at most, the one job it is right for: captions typed on paper. Anek Kannada stays and takes a
bigger role.

Systems B ("wide and bilingual") and C ("letterpress serif") are complete alternatives, ranked second
and third. Section 6 gives the ranking and the reasoning; Section 7 lists what to test in the real site
before building.

---

## 1. Should Gambetta, Switzer and Courier Prime stay? No.

The client is right, and the reason is bigger than any one face.

### 1.1 The formula is the template; only the face changed
The v1 site used Fraunces, and v2 swapped it for Gambetta. Both times the setting was the same: a big,
light (weight 300–320) serif headline in sentence case with one italic word ("Every brand hits a
*crossroads.*"), small tracked monospace labels around it, and a handwriting font for the human touch.
The Q6 review compared eight serifs in exactly that setting (`research/type/specimen_display.jpg`) and
never tested a headline that wasn't a light serif. So it found the best face for the formula, not
whether the formula was right.

That formula is now a recognised tell. Anthropic's own frontend-design skill lists, as "the commonest
tells of a generated page", "accenting just a single word or phrase in a headline, like putting one word
in italic", "a tracked-out ALL-CAPS eyebrow label above every heading", "a monospace face for small data
labels" and "a warm cream background (near #F4F1EA) with a high-contrast serif display"
([SKILL.md](https://raw.githubusercontent.com/anthropics/skills/main/skills/frontend-design/SKILL.md)).
Kavalu's cream is fixed at #F3F3E7 and can't change, so the type is what has to move. Design-review tools
ban Fraunces and Instrument Serif by name as "the two LLM-favorite display serifs"
([Taste skill](https://raw.githubusercontent.com/Leonxlnx/taste-skill/3c7017d636c3a4aad378433ea6d0cfa6c921da4a/skills/taste-skill/SKILL.md)),
and Impeccable describes "an italic Fraunces / Recoleta / Newsreader headline … lowercase track-spaced
metadata" as a fingerprint of the look
([Impeccable](https://raw.githubusercontent.com/pbakaus/impeccable/b210dd71e73e1b289b1e2f2407ad3b1458dc632e/skill/reference/brand.md)).
Any serif poured into that formula reads the same way.

### 1.2 It has no relationship with the wordmark
Her wordmark is heavy, extended, monoline, geometric capitals. Gambetta at 320 is light, of normal
width, calligraphic, in lower case. The heading contradicts the logo in weight, width, structure and
case at once. A pairing contrasts on one of those and agrees on the rest; four contrasts read as two
brands sharing a page (`research/working-shots/preview_home_top.jpg`). Fontshare itself tags Gambetta
for "Newspapers, Text, Books, Magazines": it is a text serif being used as display
([Fontshare API](https://api.fontshare.com/v2/fonts)).

### 1.3 Too many voices
The home screen alone shows six: the wordmark, Gambetta in roman and italic, Switzer, Courier Prime,
Homemade Apple and Anek Kannada. Mrs Saint Delafield joins elsewhere. Among the 185 studios in
`STUDIO_FONTS.md` with identified faces, 82% load one or two families (§5.8 there).

### 1.4 The hand is a stranger's
Homemade Apple (Font Diner, 2011) and Mrs Saint Delafield (Sudtipos, 2012) are stock Google scripts
standing in for Ananya's notes and signature. A font repeats identical letters, and even OpenType's
workaround cycles its alternates in a fixed order
([Glyphs](https://glyphsapp.com/learn/features-part-3-advanced-contextual-alternates)), while
BRAND_DESIGN promises "a real hand" (§1.5). Script or handwriting faces appear on only 2% of the studio
sites (§5.4 there).

### 1.5 Cream and a light serif is her friend's look
Studio N°7 is cream paper with a texture and a light serif in capitals: its headline file reads Editorial
New Ultralight ([Studio N°7's font file](https://static.wixstatic.com/ufonts/ef2f9f_b4e8ad21f8f74098860e9ca3304d1cbd/ttf/file.ttf)
per our recheck; screenshots `research/screens/studionumberseven-com_0.jpg`, `_1.jpg`). BRAND_DESIGN §1.6
says Kavalu must not look like it.

### 1.6 Thin strokes fight the textures
Brief 3 asks for textured backgrounds everywhere (rule 1.9). Hairlines at 300–320 lose contrast first on
paper grain and on plum; sturdier strokes hold up. (Type director's judgement.)

### 1.7 Practical faults
- No ₹ in Gambetta, Switzer or Courier Prime; Anek Kannada fills in today
  ([Courier Prime coverage](https://fonts.google.com/metadata/fonts/Courier%20Prime); TYPE_REVIEW §2).
- The Fontshare licence treats subsetting or converting the files as a derivative work that needs
  ITF's written consent, and forbids keeping them in a public repository
  (`website/src/fonts/LICENSE-fonts.md`; [FFL](https://www.fontshare.com/licenses/itf-ffl)).
- Courier Prime's capitals are short for its body, so it runs at `size-adjust: 110%`; and it does
  interface work (clock, eyebrows, scroll hint, figure labels) as well as captions.

### Verdict

| Face | Verdict | Why |
|---|---|---|
| **Gambetta** | **Goes** | The template formula; no relationship with the wordmark; too light on texture; cream-and-serif like Studio N°7; no ₹ |
| **Switzer** | **Goes**, but is an acceptable fallback | Competent but anonymous; no ₹; the FFL limits; nothing ties it to the wordmark. Keep it only if Schibsted Grotesk fails the specimen |
| **Courier Prime** | **Leaves the interface** | Right idea, wrong places. Typed captions on paper keep a typewriter: Courier Prime or Compagnon, decided in the specimen |
| **Homemade Apple** | **Goes** | Her real handwriting, as SVG |
| **Mrs Saint Delafield** | **Goes** | Her real signature, as SVG |
| **Anek Kannada** | **Stays, and grows** | Indian-made (Ek Type, Mumbai), variable in weight *and* width, carries ₹ |

---

## 2. What Kavalu's type has to do

1. **Let the wordmark be the loudest letters.** Type around it agrees with it on structure (sans,
   monoline) and contrasts on one thing only.
2. **Keep one typed voice for the album**, and only on paper: caption strips, tickets, postmarks, figure
   numbers. Not eyebrows over every section, not the nav, not the clock.
3. **Be human where a human was**: her notes and her signature in her own hand.
4. **Be bilingual**: ಕವಲು and other Kannada words in a face matched to the Latin, and ₹ in the Latin face
   itself.
5. **Avoid three lookalikes**: the generated-site look (cream, light serif display, one italic word,
   mono eyebrows); Studio N°7 (cream, texture, light serif capitals); Studio Sorted (Satoshi, Cabinet
   Grotesk, Apfel Grotezk, per the census).
6. **Hold up on texture**: no hairline weights for reading type.
7. **Two families, three faces with jobs at most**, plus the wordmark, Kannada and her hand.
8. **Free to self-host on the studio's site** (OFL first); paid only as an upgrade.

---

## 3. System A (rank 1): studio grotesk, typed

**The idea.** One well-made grotesk carries the whole site in two weights, the way most of the studios
in the census work. The scrapbook supplies the warmth: paper, tape, stamps, photographs, her hand. Type
does not have to.

| Role | Face | Setting |
|---|---|---|
| Wordmark | Her lettering (SVG), unchanged | — |
| Display | **Schibsted Grotesk** Medium 500; Semibold 600 below 40 px | Sentence case. Tracking −0.04em at 120 px and up, −0.03em at 80–119 px, −0.02em at 48–79 px, −0.01em at 34–47 px. Line height 0.92–1.0 |
| Text | **Schibsted Grotesk** Regular 400; Medium 500 for interface | 17–18 px / 1.55; measure 60–70 characters; tabular figures for the clock and prices |
| Interface labels | Schibsted Grotesk 500, sentence case, 13–14 px | No eyebrow above every heading. Capitals only on ephemera (tickets, stamps, postmarks), +6–8% |
| Typed captions | **Courier Prime**, or **Compagnon** Roman if it wins the specimen | Paper strips, tickets and postmarks only; 12–13 px; sentence case |
| Notes | **Her handwriting**, scanned and traced as SVG | 10–15 notes of up to 12 words; drawn on with a stroke or mask, never typeset |
| Signature | **Her signature**, scanned and traced as SVG | "Ananya" only |
| Kannada | **Anek Kannada**: wdth 100 in running text, 112–125 and heavy for ಕವಲು as a display word | Match weight to Schibsted by eye |
| Emphasis | No italic word in headings | At most once a page, a word circled or underlined in her own hand (SVG), as in reference 8 |

**Why it suits Kavalu.**
- *The census:* 83% of the studios load a sans and 46% a neo-grotesk; where the display face is known,
  it is a sans in 72 of 105 cases; and 82% use one or two families (`STUDIO_FONTS.md` §5).
- *Her references:* reference 8 is Studio Ambre, whose site sets its text in TWK Continental, with a
  custom "Ambre" cut for tags ([style.css](https://www.studioambre.com/style.css)); reference 5 sets its
  strips in a grotesk; reference 2 is typed; references 3 and 7 are handwritten. System A is those four
  voices, nothing more.
- *The wordmark:* a grotesque at normal width and medium weight agrees with her heavy extended capitals
  on structure and contrasts on width and weight, so the logo stays the loudest thing.
- *Not a lookalike:* no serif display on cream, no italic word, no mono eyebrows; not Satoshi or Cabinet
  (Studio Sorted); not Studio N°7's light serif.
- *Her own instinct:* her old site's hero was bold grotesk capitals (`current_website/`). This is that
  instinct, set with care.

**Why Schibsted Grotesk.** It was drawn by the studio Bakken & Bæck (Henrik Kongsvoll) for the media
group Schibsted, open-sourced in 2023 under the OFL, with weights 400–900 and true italics; it includes
₹; it has two uses on Fonts In Use and is not on Typewolf's list of the 40 best Google fonts, so it isn't
overexposed ([Fonts In Use](https://fontsinuse.com/typefaces/245321/schibsted-grotesk),
[GitHub](https://github.com/schibsted/schibsted-grotesk),
[Google Fonts coverage](https://fonts.google.com/metadata/fonts/Schibsted%20Grotesk)). Its lightest
weight is 400, which rules out the fragile light headings the client rejected. It is on none of the
AI-default lists in `FONT_GUIDE.md` §1.5.

**Rejected on the way.** Host Grotesk "modifies and extends Poppins", the eighth most used font on
Google Fonts ([Element Type](https://github.com/Element-Type/HostGrotesk)). Hanken Grotesk and Funnel
Sans have no ₹ ([Hanken](https://fonts.google.com/metadata/fonts/Hanken%20Grotesk),
[Funnel](https://fonts.google.com/metadata/fonts/Funnel%20Sans)). Inter, Geist, DM Sans, Manrope, Plus
Jakarta Sans and Instrument Sans are AI defaults (§1.5 of the guide). Mona Sans is excellent but reads as
GitHub's (and Dribbble's) typeface ([Fonts In Use](https://fontsinuse.com/typefaces/216927/mona-sans)).

**Typed captions: Courier Prime or Compagnon.** Courier Prime is "a more refined version of IBM's 1956
Courier" ([Google Fonts](https://fonts.google.com/metadata/fonts/Courier%20Prime)), with true italics,
made for screenplays ([Quote-Unquote Apps](https://quoteunquoteapps.com/courierprime/)): clean, a little
anonymous, no ₹.
Compagnon (Velvetyne, OFL) is a 2018 master's project from EESAB Rennes drawn from "the online archives of
Typewriter Database specimens", with oldstyle figures and no ₹; its five styles were drawn by different
students, so use only Roman or Light, and only if it stays crisp at 12–13 px
([README](https://gitlab.com/velvetyne/compagnon/-/raw/master/README.md)). TT2020, the "realistic"
typewriter, is out: its textured styles weigh 0.85–31.6 MB each
([repository](https://api.github.com/repos/ctrlcctrlv/TT2020/contents/dist)), and its author's history
(he founded 8chan, per [Wikipedia](https://en.wikipedia.org/wiki/Fredrick_Brennan)) is a reputational
risk for a brand.

**Real studios working this way.** One grotesk family carrying the whole site:
[Pentagram](https://www.pentagram.com) (Plain), [Base Design](https://www.basedesign.com) (Muoto),
[Bibliothèque](https://www.bibliothequedesign.com) (Unica77), [Lundgren+Lindqvist](https://lundgrenlindqvist.se)
(Px Grotesk), all from the census; [NB Studio](https://nbstudio.co.uk/wp-content/themes/nb/style.css)
(Noi Grotesk) and [Siegel+Gale](https://www.siegelgale.com/app/themes/simplicity/dist/styles/main_cc33d236.css) (Suisse). A typed voice
beside a grotesk: [Graza](https://www.graza.co) (GT Alpina Typewriter with Apercu, census);
[Snask](https://www.snask.com) loads Lacrima Senza, drawn from an IBM Golfball typewriter specimen,
beside Apercu (census; [Typewolf](https://www.typewolf.com/lacrima-senza)); and [Order](https://order.design/)
sets its whole site in Klim's monospaced Pitch Sans (census; [Klim](https://klim.co.nz/fonts/pitch-sans/)).

**Availability and licence.** Schibsted Grotesk, Courier Prime and Anek Kannada are on Google Fonts
under the SIL OFL and in Next.js 16.4.2's `next/font/google` list, so they self-host at build time with
subsetting allowed. Compagnon is OFL from Velvetyne's GitLab and would be self-hosted from `src/fonts`.
Her handwriting and signature are her own, with no licence question. Cost: nothing.

**Paid upgrade** (perpetual licences unless noted). Söhne or Founders Grotesk with their monos (Klim;
priced by traffic; price not captured, mid to high class) ([Klim licences](https://klim.co.nz/licences/)).
Or GT America with GT Alpina Typewriter (Grilli Type; one-time, priced by monthly visitors; tiers not
published, mid to high class) ([Grilli](https://www.grillitype.com/information)). If the studio already
pays for Creative Cloud: Neue Haas Grotesk with Prestige Elite on Adobe Fonts, at no extra cost but
served by Adobe, not self-hosted, and only while the plan lasts
([Neue Haas Grotesk](https://fonts.adobe.com/fonts/neue-haas-grotesk), [Prestige Elite](https://fonts.adobe.com/fonts/prestige-elite)).

**Risks.**
- Set timidly, any grotesk looks corporate. It needs real scale contrast (hero against body is about
  5 : 1), the paper kit and her hand.
- Schibsted's news-media origin shows in its compact proportions; check long headlines and Indian
  English place names for awkward breaks.
- Google's coverage data for Schibsted lists ↑ and ↓ but not ← or →
  ([coverage](https://fonts.google.com/metadata/fonts/Schibsted%20Grotesk)), so arrows keep coming from
  the system font, as today. Confirm with `research/tools` glyph checks.
- Typed captions must stay rare, or the album turns into a terminal.

---

## 4. System B (rank 2): wide and bilingual

**The idea.** Width is the system. One grotesque family with a real width axis runs from condensed to
extended: the extended cut rhymes with her wordmark for a few big moments, the normal width reads, and
the condensed cut stamps labels like a rubber stamp. Anek Kannada has the same width axis, so English
and ಕವಲು can be set at matching widths.

| Role | Face | Setting |
|---|---|---|
| Display | **Archivo** at wdth 112–125, weight 500–600 | Sentence case for headings; −0.02em; line height 0.95. One extended, heavy word per page at most, never in the same view as the wordmark |
| Text | **Archivo** at wdth 100, weight 400 | 17–18 px / 1.55 |
| Stamps and labels | **Archivo** at wdth 62–75, weight 600, capitals, +4% | Postmarks, tickets, figure labels, the clock |
| Captions | **Fragment Mono** 12 px, sentence case | Data-like captions under prints; has ₹ and small caps |
| Notes, signature | Her hand (SVG) | As System A |
| Kannada | **Anek Kannada** at the width of the Latin beside it (100 with 100, 125 with 125) | One axis for both scripts |

**Why it suits Kavalu.** It builds on her strongest asset, the extended wordmark, and her old site's
heavy-extended "SERVICES" heading. It is the census's "superfamily with widths" pattern:
[Ragged Edge](https://www.raggededge.com/) (ABC Diatype with Diatype Expanded), [Locopopo](https://locopopo.com/)
in Mumbai (Aktiv Grotesk with Aktiv Grotesk Extended), [Koto](https://koto.com/) (GT Kotoheim with its
Condensed and Mono), [The Whole Truth](https://thewholetruthfoods.com) (Obviously with Obviously Narrow),
all from the census. Matching Kannada to Latin by width is the bilingual route Indian practice now takes:
Bengaluru's Biergarten Karnataka festival set Kannada in Anek Kannada to "anchor this in local context"
([Fonts In Use](https://fontsinuse.com/uses/73798/biergarten-karnataka-food-festival-2024)).

**Faces.** Archivo (Omnibus-Type, Buenos Aires; OFL) is a grotesque "reminiscent of late 19th-century
American typefaces" with width 62–125, weight 100–900, italics and ₹
([Google](https://fonts.google.com/metadata/fonts/Archivo)). Fragment Mono (Wei Huang with URW; OFL) is
"derived from Nimbus Sans, itself based on Helvetica", with ₹ and small caps
([Google](https://fonts.google.com/metadata/fonts/Fragment%20Mono)). Anek Kannada (Ek Type; OFL) has width
75–125 and weight 100–800 and carries ₹ ([Google](https://fonts.google.com/metadata/fonts/Anek%20Kannada)).

**Alternates.** Mona Sans (GitHub with Degarism; OFL; width 75–125) is the more refined drawing, but it is
GitHub's and Dribbble's typeface and has a Reserved Font Name, so modified files must be renamed
([Fonts In Use](https://fontsinuse.com/typefaces/216927/mona-sans),
[OFL FAQ](https://openfontlicense.org/ofl-faq/)). Anek Latin makes the whole system Ek Type, one design in
both scripts, but it has no italics and its showcase is the IPL and CoForge
([Ek Type](https://ektype.in/anek-family.html)).

**Paid upgrade.** ABC Diatype with Diatype Expanded and Diatype Mono (Dinamo: priced by company size,
perpetual, self-hosting and subsetting allowed, "no limit on the amount of web traffic"; mid class)
([Dinamo](https://abcdinamo.com/licenses)). Or Aktiv Grotesk with Aktiv Grotesk Extended on Adobe Fonts
if the studio has Creative Cloud ([Adobe Fonts](https://fonts.adobe.com/fonts/aktiv-grotesk-extended)).

**Risks.** It is the loudest of the three; wide headings can compete with the wordmark and fight the
client's "subtle, elegant". Archivo is already on two Indian studio sites, Animal and Confetti (census). No
typewriter, so the typed-label language of the references becomes a stamped one. Needs strict rules
about where the extended cut may appear.

---

## 5. System C (rank 3): letterpress serif

**The idea.** If Kavalu wants a serif voice, make it sturdy and printed, not light and fashionable: a
Clarendon slab for headings, an American gothic for text and a typewriter for captions. Those are the
faces of tickets, labels and letterpress ephemera, the real objects of a scrapbook. Extended gothics and
Clarendons were both staple display faces of 19th-century wood-type printing
([Rob Roy Kelly collection: Gothic](https://rrk.finearts.utexas.edu/woodtype/gothic/),
[Antique and Clarendon](https://rrk.finearts.utexas.edu/woodtype/antique/)), so her extended wordmark has a
historical partner here.

| Role | Face | Setting |
|---|---|---|
| Display | **Besley** at 500–600, never 400 | Sentence case; −0.01em; line height 1.0–1.05; no size above about 100 px |
| Text | **Libre Franklin** 400; 500–600 for interface | 17 px / 1.6 |
| Labels | Libre Franklin 600, capitals, +8% | Ephemera only |
| Captions | **Courier Prime**, 12–13 px | A slab typewriter beside a slab serif belongs |
| Notes, signature | Her hand (SVG) | As System A |
| Kannada | **Tiro Kannada** for Kannada in serif settings; Anek Kannada for interface | |

**Why it suits Kavalu.** It is the most local and the most tactile: Tiro Kannada "grew from a Murty
Classical Library typeface" drawing on the 19th-century Basel Mission Press Kannada types
([Google Fonts](https://fonts.google.com/metadata/fonts/Tiro%20Kannada)), the letterpress lineage of
printed Kannada. It continues her own instinct: her old site set its headings in a sturdy bold serif, and
her Nivritti case study describes "a bold serif typeface with contrasting stroke weights"
(`current_website/`). Studios with a slab or Clarendon voice: [Codesign](https://www.codesign.in/) in
Gurugram (Sentinel with Whitney), [Hello Monday](https://hellomonday.com) (Clarendon with NB International),
[Kontrapunkt](https://www.kontrapunkt.com) (its own Tomo Slab), [Perky Bros](https://perkybros.com/)
(Quadrant Text, a contemporary ionic, with Dada Grotesk), all from the census; *The Guardian*'s Egyptian
and Sans is the classic pairing ([Commercial Type](https://commercialtype.com/catalog/guardian_egyptian)).
No source we found ties Clarendon specifically to Indian sign painting, so that link is not claimed here.
For Kannada lettering itself, the best reference is Pooja Saxena's *India Street Lettering* (Blaft, 2025),
which grew out of her documenting "expressive Kannada lettering signs" in Bengaluru
([STIR](https://www.stirworld.com/think-books-and-movies-india-street-lettering-explores-a-visual-art-that-is-always-looked-at-hardly-ever-seen)).

**Faces.** Besley (Owen Earl; OFL) is "an antique slab serif inspired by Robert Besley's Clarendon",
weights 400–900 with italics, but **no ₹** ([Google](https://fonts.google.com/metadata/fonts/Besley)).
Libre Franklin (Impallari Type; OFL) reinterprets Benton's 1912 Franklin Gothic, with ₹
([Google](https://fonts.google.com/metadata/fonts/Libre%20Franklin)). Tiro Kannada (Tiro Typeworks: John
Hudson, Fiona Ross; OFL) has Kannada and Latin, an italic and ₹.

**Paid upgrade.** Sentinel (Hoefler&Co., the face Codesign uses; price not captured), or GT Alpina with
GT Alpina Typewriter (Grilli Type: one family covering both the serif and the typed captions; mid to high
class) ([Grilli](https://www.grillitype.com/information)).

**Risks.** It is the third serif-led system after two the client rejected (Fraunces, then Gambetta), and a
serif display on cream is the tell named in §1.1. Clarendon tips easily into retro, craft-beer or
Western-saloon. Besley lacks ₹, so set ₹ in the text face, or let Tiro Kannada supply it. Libre Franklin
is popular (#7 on Typewolf's 40 best Google fonts, [Typewolf](https://www.typewolf.com/google-fonts)).

---

## 6. The ranking, and why

**1. System A.** A type director's first rule around a strong custom wordmark is to keep everything else
quieter and better made. Kavalu's personality is already strong: the wordmark, the palette, the paper
kit, the Kannada name, her hand. The type's job is to stop competing with them. System A answers every
item in Section 2, matches what the strongest studios actually do (one grotesk; 82% use one or two
families), uses exactly the voices of her references (grotesk, typed, handwritten), and removes every
generated-site tell from the type. It is also the lowest-risk build: one family, free, with ₹.

**2. System B.** It is the most *on-brand* system, because it grows from the wordmark's width, and the most
genuinely bilingual. It ranks second because it is louder than her brief ("subtle, elegant") and asks for
discipline the site may not keep: one extended word too many and the headings fight the logo. Choose it if
the specimen of A looks too reserved next to her work.

**3. System C.** It is the most local and the most crafted, with a historically right partner for an
extended wordmark and a Kannada serif with letterpress roots. But it is the third serif-led system after two
rejections, a serif display on cream is the very tell to avoid, and Clarendon can tip into nostalgia. Keep it
for a later identity project, or for her editorial pieces, not for the studio's website.

---

## 7. What to test in the real site before building

Set A, B and C on the same three screens (home hero with the collage, a project spread, the footer desk),
at 1440 and 390 px, on cream with paper grain and on deep plum, using `research/tools/type_specimens.py`
and the preview tooling:
1. The lockup and the hero headline in one view: does the type agree with the wordmark?
2. Typed captions at 12–13 px on a paper strip: Courier Prime against Compagnon Roman.
3. "Under ₹1 lakh" in body text and in a heading (₹ from the face, not the fallback).
4. ಕವಲು inline and as a display word beside the Latin, weight and width matched by eye.
5. A long Indian-English heading ("Studio Anokhi, a pottery studio in Bengaluru") for line breaks.
6. The Bengaluru clock with tabular figures (`font-variant-numeric: tabular-nums`), and arrows (← →).
7. Her notes: a first scan of three real notes, traced, beside the type.

**What would change in the build** (for whoever builds it): `website/src/app/fonts.ts` (the faces),
`styles/tokens.css` (stacks, weights, tracking), and the emphasis and label rules in BRAND_DESIGN §5.3–5.5
(no italic-word device, no eyebrow over every heading, typed captions on paper only). The FFL-licensed files
leave `src/fonts`.

---

## Sources

The studio data, frequency tables and face index are in `STUDIO_FONTS.md`; the evidence on AI defaults,
licences and setting is in `FONT_GUIDE.md` Part 1. Facts about each candidate face (licence, ₹, axes,
users) were checked against Google Fonts' per-family metadata
(`https://fonts.google.com/metadata/fonts/<Family>`), the faces' repositories and foundry pages linked
above, and are tabled in `research/type/data/candidates.tsv`.
