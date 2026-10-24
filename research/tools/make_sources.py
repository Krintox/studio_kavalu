"""Build research/SOURCES.md from the capture log, the curated list, review notes and the research files."""
import json
import re
from pathlib import Path

R = Path("C:/shashank/shashank/fnf/ananya_residency/studio_kavalu/research")
SCR = Path(__file__).parent

BUCKETS = {
    "A": "Boutique and founder-led studios",
    "B": "Indian design studios",
    "C": "Established branding agencies",
    "D": "Motion-led and award-winning studios",
    "E": "Tactile, collage, scrapbook and editorial sites",
    "F": "Like-minded lifestyle, food and craft brands",
    "G": "Portfolios of designers, art directors and photographers",
}

# --- captures (one record per slug, last one wins) ---
caps = {}
for line in open(R / "screens/results.jsonl", encoding="utf-8"):
    r = json.loads(line)
    caps[r["slug"]] = r

# --- notes: curation agent's notes, then my own review notes (mine win) ---
notes = {}
curated = json.load(open(R / "reference_sites.json", encoding="utf-8"))
loc = {}
for c in curated:
    notes[c["url"].rstrip("/").lower()] = c.get("notes", "")
    loc[c["url"].rstrip("/").lower()] = c.get("location", "")

mine = {}
for line in open(R / "notes_screens.md", encoding="utf-8"):
    m = re.match(r"- \*\*(.+?)\*\*\s*(?:\([^)]*\))?\s*-\s*(.+)", line.strip())
    if m:
        for name in m.group(1).split(" / "):
            mine[name.strip().lower()] = m.group(2).strip()

TECH_KEYS = ["next", "nuxt", "astro", "sveltekit", "webflow", "framer", "wordpress", "shopify", "squarespace",
             "wix", "cargo", "gsap", "scrolltrigger", "lenis", "locomotive", "barba", "swup", "taxi", "three",
             "pixi", "motion", "splitting"]


def stack(rec):
    t = ((rec.get("info") or {}).get("tech") or {})
    on = [k for k in TECH_KEYS if t.get(k)]
    if t.get("canvas"):
        on.append("canvas")
    if t.get("video"):
        on.append("video")
    return ", ".join(on) or "—"


def esc(s):
    return (s or "").replace("|", "/").replace("\n", " ").strip()


rows = {}
for rec in caps.values():
    rows.setdefault(rec.get("bucket") or "?", []).append(rec)

out = []
w = out.append
w("# Studio Kavalu — sources")
w("")
w("*Every website, page and document the research and design drew on, with links. Built 2026-10-24 from the")
w("capture log (`screens/results.jsonl`), the curated list (`reference_sites.json`), the review notes")
w("(`notes_screens.md`), `motion_catalog.md` and `onboarding_research.md`.*")
w("")
w("- **226 websites** were opened in the persistent Chrome (CDP, port 9333) at 1440×900 and captured at three")
w("  scroll depths: `screens/<slug>_0/1/2.jpg`, contact sheets `sheets/sheet_01–57.jpg`. (Mucho appears")
w("  under two domains, so 225 distinct studios.)")
w("- \"Stack\" is what the page exposed at runtime (framework, GSAP, Lenis, WebGL canvas, video). Bundled")
w("  libraries can hide, so treat it as a floor.")
w("")
w("## 1. Where each idea on the site came from")
w("")
w("| Idea on the Kavalu site | Sources it was drawn from |")
w("|---|---|")
ideas = [
    ("Stamp motif (perforated frames, colour stamp + duotone twin, flip-book)",
     "[Jacob Hutch — Stamp Series (the client's Pinterest pin)](https://in.pinterest.com/pin/681873199876372589/), "
     "[jacobhutch.com](https://www.jacobhutch.com), [Niccolò Miranda — The Paper Portfolio](https://www.niccolomiranda.com/), "
     "[Digital Stamp Collection](https://marijanapav.com/stamps)"),
    ("Work first; several views of one collection (stamps ↔ index, filters)",
     "[Pentagram](https://www.pentagram.com), [Base Design](https://www.basedesign.com), [Porto Rocha](https://portorocha.com), "
     "[Obys](https://obys.agency), [Olivier Larose](https://www.olivierlarose.com), [Studio Feixen](https://www.studiofeixen.ch/)"),
    ("One confident serif statement with italic emphasis",
     "[Collins](https://www.wearecollins.com), [Here Design](https://www.heredesign.co.uk), [Perky Bros](https://perkybros.com/), "
     "[Present](https://www.presentstudio.co/), [Heure Bleue](https://heurebleue.studio/), [Little Plains](https://www.littleplains.com/)"),
    ("Folder tabs (footer, menu)", "Her current site's footer; [Mother Design](https://www.motherdesign.com) (desktop toolbar)"),
    ("Live Bengaluru clock in the chrome", "[Koto](https://koto.studio), [Porto Rocha](https://portorocha.com), [Boc.Studio](https://boc.studio/), "
     "[Commission Studio](https://www.commission.studio/) (live temperature)"),
    ("Torn paper edges, paper as a premium material", "[Commission Studio](https://www.commission.studio/), [14islands](https://www.14islands.com), "
     "[Immersive Garden](https://immersive-g.com)"),
    ("Pinboard / desk of pinned material (footer)", "[LRNCE](https://lrnce.com/) (moodboard hero), [Studio Namma](https://studionamma.com/) "
     "(cut-outs + stickers), [Mother Design](https://www.motherdesign.com) (sticky note), "
     "[Mr. Panda's Paper Portfolio](https://www.mr-pandas-psychologically-safe-portfolio.com/), [Collage Department](https://collagedepartment.com/)"),
    ("Project spreads in each client's own colours", "[Koto](https://koto.studio), [Collins](https://www.wearecollins.com), "
     "[Wolff Olins](https://www.wolffolins.com) (case cards), [Perky Bros](https://perkybros.com/)"),
    ("Palette chips with names on case studies", "[East Fork — The Palette](https://eastfork.com/)"),
    ("Typewriter / mono captions and bracketed labels", "[Quatrième Étage](https://quatriemeetage.studio/), [Odds Studio](https://odds-studio.com/), "
     "[Lundgren+Lindqvist](https://lundgrenlindqvist.se)"),
    ("Kannada used as a brand script", "[Subko](https://subko.coffee) (multi-script marquee incl. ಸಬ್ಕೊ)"),
    ("Hero stamp expanding to full screen on scroll", "[React Bits — scroll expand](https://reactbits.dev/animations/scroll-expand), "
     "[Exo Ape](https://exoape.com), [Rejouice](https://www.rejouice.com)"),
    ("Pictures dealing out of a pile into a collage", "[Codrops — entrance animation for images](https://tympanus.net/Development/EntranceAnimationForImages/)"),
    ("Spreads zooming out as the next stacks over", "[Codrops — sticky sections](https://tympanus.net/Development/StickySections/)"),
    ("Manifesto words inking in", "[Codrops — on-scroll text highlight](https://tympanus.net/Development/OnScrollTextHighlight/), "
     "[JKR](https://www.jkrglobal.com)"),
    ("Stamp → case-study cover morph, page transitions", "[Next.js — view transitions guide](https://nextjs.org/docs/app/guides/view-transitions), "
     "[React ViewTransition](https://react.dev/reference/react/ViewTransition)"),
    ("Draggable desk with inertia", "[Codrops — infinite parallax grid](https://tympanus.net/codrops/2025/06/11/building-an-infinite-parallax-grid-with-gsap-and-seamless-tiling/), "
     "[Osmo — draggable stickers](https://www.osmo.supply/resource/draggable-stickers)"),
    ("Letter that folds into a stamped envelope", "[Paperlab](https://paperlab.nawwara.studio/), [Digital Stamp Collection](https://marijanapav.com/stamps) (postcard form)"),
    ("\"Start a project\" in the nav; booking + WhatsApp", "[Perky Bros](https://perkybros.com/), [Poch](https://poch.studio/), "
     "[Wishbox](https://wishboxstudio.in/), [Confetti](https://www.confetti.design/), and `onboarding_research.md` §8"),
    ("Restraint rules (what not to do)", "Discount pop-ups on [Fishwife](https://eatfishwife.com), [Brightland](https://brightland.co), "
     "[Ghia](https://drinkghia.com); preloaders on [Locomotive](https://locomotive.ca), [Made Thought](https://www.madethought.com); "
     "`motion_catalog.md` §7 anti-list"),
]
for a, b in ideas:
    w(f"| {a} | {b} |")
w("")
w("## 2. All 226 captured websites")
w("")
for key in "ABCDEFG":
    recs = sorted(rows.get(key, []), key=lambda r: r["name"].lower())
    if not recs:
        continue
    w(f"### {key}. {BUCKETS[key]} ({len(recs)})")
    w("")
    w("| Site | Link | Stack | Notes |")
    w("|---|---|---|---|")
    for r in recs:
        url = r["url"]
        n = mine.get(r["name"].lower()) or notes.get(url.rstrip("/").lower(), "")
        place = loc.get(url.rstrip("/").lower(), "")
        name = esc(r["name"]) + (f" ({esc(place)})" if place else "")
        w(f"| {name} | {url} | {stack(r)} | {esc(n)} |")
    w("")

w("## 3. Brand, client and friends' studios")
w("")
for line in [
    "- Client's landing-page reference (Pinterest pin, Jacob Hutch, *Stamp Series // Visual Experiment 01*): https://in.pinterest.com/pin/681873199876372589/",
    "- Studio Sorted: https://www.studiosorted.com/ · DesignRush profile: https://www.designrush.com/agency/profile/studio-sorted",
    "- Studio N°7 (Studio Number Seven): https://www.studionumberseven.com/ (archived About page via the Wayback Machine, July 2025)",
    "- Online-presence checks for Studio Kavalu: `studiokavalu.com` (no DNS), Instagram `@studiokavalu` (no such account), Behance search, DuckDuckGo and web search (no results).",
    "- Her current website: screenshots in `../current_website/` (palette, wordmark, case-study copy).",
]:
    w(line)
w("")

w("## 4. Motion research sources")
w("")
w("From `motion_catalog.md` §9 (41 techniques catalogued; see the catalog for which source backs which technique).")
w("")
mc = (R / "motion_catalog.md").read_text(encoding="utf-8")
sec = mc[mc.index("## 9. Sources index"):]
sec = sec.split("\n", 1)[1]
w(sec.strip())
w("")

w("## 5. Onboarding research sources")
w("")
w("From `onboarding_research.md` §8 (41 studio contact pages surveyed in §2 of that file).")
w("")
ob = (R / "onboarding_research.md").read_text(encoding="utf-8")
s8 = ob[ob.index("## 8. Sources"):]
s8 = s8.split("\n", 1)[1]
if "## 9." in s8:
    s8 = s8[: s8.index("## 9.")]
w(s8.strip())
w("")

w("## 6. Fonts, licences and tools")
w("")
for line in [
    "- Gambetta, Switzer (Indian Type Foundry) via Fontshare — https://www.fontshare.com/fonts/gambetta · https://www.fontshare.com/fonts/switzer · ITF Free Font License: https://www.fontshare.com/licenses/itf-ffl",
    "- Courier Prime (SIL OFL) — https://fonts.google.com/specimen/Courier+Prime · https://github.com/quoteunquoteapps/CourierPrime",
    "- Homemade Apple, Mrs Saint Delafield, Anek Kannada: Google Fonts (SIL OFL) — https://fonts.google.com",
    "- Compared in the type review (specimens in `research/type/`): Fraunces, Erode, Sentient, Zodiak, Boska, Bespoke Serif, Newsreader; Ranade, Author, Hanken Grotesk; IBM Plex Mono, Cutive Mono, Xanh Mono; Nothing You Could Do, La Belle Aurore, Reenie Beanie, Kalam",
    "- v1 faces, replaced in v2: Fraunces, IBM Plex Mono (Google Fonts); Ranade, Panchang (Fontshare)",
    "- How brand documents are structured: NASA Graphics Standards Manual (Danne & Blackburn, 1975); Foothill–De Anza Brand Guidelines (Jan 2026) https://fhda.edu/_downloads/_FHDA-Brand-Guidelines-January2026.pdf · GitHub Brand Toolkit https://brand.github.com · IBM Carbon motion https://carbondesignsystem.com/elements/motion/overview/ · Atlassian foundations https://atlassian.design/foundations",
    "- Motion studied frame by frame (`research/motion_frames/sites/NOTES.md`): Digital Stamp Collection https://marijanapav.com/stamps · MERSI https://www.mersi-architecture.com · Obys' Design Books https://library.obys.agency/ · The Lookback https://tlb.betteroff.studio/ (did not render in capture)",
    "- Next.js 16 docs (bundled in `website/node_modules/next/dist/docs/`), GSAP docs https://gsap.com/docs/v3/, Lenis https://github.com/darkroomengineering/lenis",
]:
    w(line)
w("")
(R / "SOURCES.md").write_text("\n".join(out), encoding="utf-8")
print("sites:", sum(len(v) for v in rows.values()), "| lines:", len(out))
