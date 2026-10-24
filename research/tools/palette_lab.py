"""Q24 palette lab: render colour-proportion iterations on the real site and measure them.

For each iteration, every section is stood on a ground (the same data-surface / data-tone attributes that
lib/surfaces.ts sets), the page is scrolled through a screen at a time as a visitor sees it, and every
pixel of every screen is sorted to the nearest palette family (CIE Lab). The share of plum + blue is
what brief 4 asks to keep at 70-90%. A contrast probe checks every line of text against what is really
behind it, so no iteration is chosen that would fail AA somewhere.

    palette_lab.py <iteration|all> [desktop|mobile|both] [path ...]
Output: research/palette_lab/<iteration>/<device>/ (screens, strip.jpg, result.json) and summary.json
Needs the dev server on localhost:3210 and the persistent Chrome on 9333 (the research tab only).
"""
import base64
import io
import json
import sys
import time
from pathlib import Path

import numpy as np
from PIL import Image

sys.path.insert(0, "C:/Users/YB-TSR/AppData/Local/Temp/claude/C--shashank-shashank-fnf-ananya-residency-studio-kavalu/a3bb7160-284a-4262-8b39-11e03e34435c/scratchpad")
from framecap import Cap  # noqa: E402  the research tab's CDP client

ROOT = Path(__file__).resolve().parents[1] / "palette_lab"
SITE = "http://localhost:3210"

FAMILIES = {
    "plum": ["#390d26", "#270617", "#241319"],
    "blue": ["#abcdd6", "#c9dfe5"],
    "cream": ["#f3f3e7", "#eceadb", "#e3e0cd", "#fbfaf2", "#f8f5e8"],
    "oxblood": ["#491c17", "#51201b"],
}
# a spread in its project's own colours, or the palette's (ground, ink)
PROJECT = None
SECTIONS = ["hero", "spread", "manifesto", "album", "roads", "founder", "choose", "footer",
            "studioHero", "studioRoads", "process", "faq", "work", "case", "caseHero", "caseNext", "start", "notFound"]

# Each iteration names the ground of every section; spreads take a list (one per project, repeating).
ITERATIONS = {
    "now": {"note": "today's site: cream grounds, project colours on the spreads",
            "hero": "cream", "spread": [PROJECT], "manifesto": "cream", "album": "cream", "roads": "cream",
            "founder": "cream", "choose": "cream", "footer": "deep", "studioHero": "cream", "studioRoads": "oxblood",
            "process": "cream", "faq": "cream", "work": "cream", "case": "cream", "caseHero": PROJECT, "caseNext": PROJECT},
    # brief 5: plum about 20%, cream and blue 50-60%, a light hero and opening
    "L1_cream_open": {"note": "cream hero, prints on blue spreads, the torn cream sheet, blue roads and letter, one plum founder",
                      "noSheets": True, "hero": "cream", "spread": ["blue", "blue"], "manifesto": "cream", "album": "cream",
                      "roads": "blue", "founder": "plum", "choose": "blue",
                      "studioHero": "cream", "studioRoads": "plum", "process": "blue", "faq": "cream", "work": "cream",
                      "case": "cream", "caseHero": "blue", "caseNext": "plum", "start": "cream", "notFound": "cream"},
    "L2_blue_open": {"note": "blue hero, prints on cream spreads, blue house view, cream album, blue roads, cream founder",
                     "noSheets": True, "hero": "blue", "spread": ["cream", "cream"], "manifesto": "blue", "album": "cream",
                     "roads": "blue", "founder": "cream", "choose": "blue",
                     "studioHero": "blue", "studioRoads": "cream", "process": "blue", "faq": "cream", "work": "cream",
                     "case": "cream", "caseHero": "blue", "caseNext": "blue", "start": "cream", "notFound": "cream"},
    "L3_light_one_plum": {"note": "cream hero, blue and cream spreads, blue house view, plum album (the one plum chapter), cream roads, blue founder",
                          "noSheets": True, "hero": "cream", "spread": ["blue", "cream"], "manifesto": "blue", "album": "plum",
                          "roads": "cream", "founder": "blue", "choose": "cream",
                          "studioHero": "cream", "studioRoads": "plum", "process": "cream", "faq": "blue", "work": "cream",
                          "case": "cream", "caseHero": "blue", "caseNext": "plum", "start": "cream", "notFound": "cream"},
    "L4_cream_open_oxblood": {"note": "as L1, with the founder on oxblood (the warm accent) instead of plum",
                              "noSheets": True, "hero": "cream", "spread": ["blue", "blue"], "manifesto": "cream", "album": "cream",
                              "roads": "blue", "founder": "oxblood", "choose": "blue",
                              "studioHero": "cream", "studioRoads": "oxblood", "process": "blue", "faq": "cream", "work": "cream",
                              "case": "cream", "caseHero": "blue", "caseNext": "blue", "start": "cream", "notFound": "cream"},
    "L5_cream_open_oxblood_roads": {"note": "cream hero, prints on blue spreads, the torn cream sheet, the four roads on oxblood, the founder on cream, the letter on blue",
                                    "noSheets": True, "hero": "cream", "spread": ["blue", "blue"], "manifesto": "cream", "album": "cream",
                                    "roads": "oxblood", "founder": "cream", "choose": "blue",
                                    "studioHero": "cream", "studioRoads": "oxblood", "process": "blue", "faq": "cream", "work": "cream",
                                    "case": "cream", "caseHero": "blue", "caseNext": "blue", "start": "cream", "notFound": "cream"},
    "R2_plum_album_oxblood_founder": {"note": "light opening; the album strip on plum mid-page, the roads on cream, the founder on oxblood, the letter on blue",
                                      "hero": "cream", "spread": ["blue", "blue"], "manifesto": "cream", "album": "plum",
                                      "roads": "cream", "founder": "oxblood", "choose": "blue"},
    # the site as built: every ground from lib/surfaces.ts, nothing overridden
    "site": {"note": "the site as built (lib/surfaces.ts: G, the alternating album pages)"},
    # plum is the album, blue the two quiet sheets between (about 60 / 25 / 15)
    "A_plum_album": {"note": "plum album: dark grounds throughout, blue for the manifesto and the roads",
                     "hero": "plum", "spread": ["deep", "plum"], "manifesto": "blue", "album": "plum", "roads": "blue",
                     "founder": "plum", "choose": "deep"},
    # the inverse: powder blue carries the page, plum frames the work
    "B_blue_album": {"note": "blue album: powder-blue grounds, the work and the roads on plum",
                     "hero": "blue", "spread": ["plum", "deep"], "manifesto": "blue", "album": "blue", "roads": "plum",
                     "founder": "blue", "choose": "blue"},
    # a walk from day into evening: blue at the top, plum by the desk
    "C_dusk": {"note": "dusk: blue for the first half of the page, plum for the second",
               "hero": "blue", "spread": ["blue", "plum"], "manifesto": "blue", "album": "plum", "roads": "plum",
               "founder": "deep", "choose": "plum"},
    # pictures on plum (photos glow on dark), words on blue
    "D_pictures_words": {"note": "pictures on plum, words on blue",
                         "hero": "blue", "spread": ["plum", "deep"], "manifesto": "blue", "album": "plum", "roads": "blue",
                         "founder": "blue", "choose": "blue"},
    # plum nearly everywhere, one blue moment and the blue sheet to start a project
    "E_plum_frame": {"note": "plum frame: deep and plum grounds, blue only for the manifesto and the start sheet",
                     "hero": "deep", "spread": ["plum", "deep"], "manifesto": "blue", "album": "deep", "roads": "plum",
                     "founder": "plum", "choose": "blue"},
    # album pages that alternate: words on blue, pictures on plum, the founder's blue poster on plum
    "G_alternate": {"note": "alternating pages: blue hero, plum spreads, blue statement, plum album, blue roads, plum founder, blue start",
                    "hero": "blue", "spread": ["deep", "plum"], "manifesto": "blue", "album": "plum", "roads": "blue",
                    "founder": "plum", "choose": "blue",
                    "studioHero": "blue", "studioRoads": "plum", "process": "blue", "faq": "blue", "work": "plum",
                    "case": "blue", "caseHero": "deep", "caseNext": "plum", "start": "blue", "notFound": "blue"},
    # the same pages, opening on plum
    "H_alternate_plum": {"note": "as G, but the hero is plum",
                         "hero": "plum", "spread": ["deep", "plum"], "manifesto": "blue", "album": "plum", "roads": "blue",
                         "founder": "plum", "choose": "blue",
                         "studioHero": "plum", "studioRoads": "deep", "process": "blue", "faq": "blue", "work": "plum",
                         "case": "blue", "caseHero": "deep", "caseNext": "plum", "start": "blue", "notFound": "blue"},
    # the colour research's first choice (research/COLOUR_PROPORTION.md §4.4): one plum desk that never
    # changes, reading laid on it as large blue sheets, the four road cards in blue
    "D2_desk_sheets": {"note": "plum desk with blue sheets (colour research, recommendation D)",
                       "hero": "plum", "spread": ["deep", "plum"], "manifesto": "plum", "album": "deep", "roads": "plum",
                       "founder": "plum", "choose": "plum",
                       "studioHero": "plum", "studioRoads": "plum", "process": "deep", "faq": "plum", "work": "plum",
                       "case": "plum", "caseHero": "deep", "caseNext": "plum", "start": "plum", "notFound": "plum",
                       "sheets": {"manifesto": "blue", "studioHero": "blue", "faq": "blue2"},
                       "sheetSel": {"[data-section=case] > section[class*='text']": "blue2"},
                       "cards": ["var(--blue)", "var(--blue-2)", "var(--blue)", "var(--blue-2)"]},
    # D refined: the same desk, with the four roads also laid on one large blue sheet (their cards cream
    # and pale blue on it), so blue keeps a main colour's share without a full-width switch
    "D4_desk_two_sheets": {"note": "plum desk; the house view and the four roads on large blue sheets",
                           "hero": "plum", "spread": ["deep", "plum"], "manifesto": "plum", "album": "deep", "roads": "plum",
                           "founder": "plum", "choose": "plum",
                           "studioHero": "plum", "studioRoads": "plum", "process": "deep", "faq": "plum", "work": "plum",
                           "case": "plum", "caseHero": "deep", "caseNext": "plum", "start": "plum", "notFound": "plum",
                           "sheets": {"manifesto": "blue", "roads": "blue", "studioHero": "blue", "faq": "blue2", "process": "blue"},
                           "sheetSel": {"[data-section=case] > section[class*='text']": "blue2"}},
    # its second choice (§4.5): blue first, then plum from the house view on
    "E2_two_roads": {"note": "two roads: blue first, plum after the house view (colour research, E)",
                     "hero": "blue", "spread": ["deep", "plum"], "manifesto": "blue", "album": "deep", "roads": "plum",
                     "founder": "plum", "choose": "plum",
                     "studioHero": "blue", "studioRoads": "blue", "process": "blue", "faq": "plum", "work": "blue",
                     "case": "blue", "caseHero": "deep", "caseNext": "plum", "start": "blue", "notFound": "blue",
                     "cards": ["var(--blue)", "var(--blue-2)", "var(--blue)", "var(--blue-2)"]},
    # blue nearly everywhere, plum for the manifesto and the founder
    "F_blue_frame": {"note": "blue frame: blue grounds, plum for the manifesto and the founder",
                     "hero": "blue", "spread": ["blue"], "manifesto": "plum", "album": "blue", "roads": "blue",
                     "founder": "plum", "choose": "blue"},
}


def hex2rgb(h):
    h = h.lstrip("#")
    return [int(h[i:i + 2], 16) for i in (0, 2, 4)]


def to_lab(rgb):
    c = np.asarray(rgb, dtype=np.float64) / 255.0
    c = np.where(c > 0.04045, ((c + 0.055) / 1.055) ** 2.4, c / 12.92)
    m = np.array([[0.4124, 0.3576, 0.1805], [0.2126, 0.7152, 0.0722], [0.0193, 0.1192, 0.9505]])
    xyz = c @ m.T / np.array([0.95047, 1.0, 1.08883])
    f = np.where(xyz > 0.008856, np.cbrt(xyz), 7.787 * xyz + 16 / 116)
    return np.stack([116 * f[..., 1] - 16, 500 * (f[..., 0] - f[..., 1]), 200 * (f[..., 1] - f[..., 2])], axis=-1)


PAL_NAMES, PAL_LAB = [], []
for fam, cols in FAMILIES.items():
    for c in cols:
        PAL_NAMES.append(fam)
        PAL_LAB.append(to_lab(hex2rgb(c)))
PAL_LAB = np.array(PAL_LAB)
FAM_LIST = list(FAMILIES) + ["other"]


def classify(img):
    """Share of each palette family in a screen; pixels far from every palette colour are 'other' (photos)."""
    a = np.asarray(img.convert("RGB").resize((img.width // 2, img.height // 2)), dtype=np.float64)
    lab = to_lab(a.reshape(-1, 3))
    d = np.linalg.norm(lab[:, None, :] - PAL_LAB[None, :, :], axis=-1)
    near = d.argmin(axis=1)
    far = d.min(axis=1) > 16
    counts = {f: 0 for f in FAM_LIST}
    names = np.array(PAL_NAMES)[near]
    for f in FAMILIES:
        counts[f] = int(((names == f) & ~far).sum())
    counts["other"] = int(far.sum())
    return counts


APPLY_JS = r"""((it) => {
  const dark = s => s === 'plum' || s === 'deep' || s === 'oxblood';
  const inks = { cream: 'var(--ink)', blue: 'var(--deep)', plum: 'var(--cream)', deep: 'var(--cream)', oxblood: 'var(--cream)' };
  let spreadN = 0;
  for (const el of document.querySelectorAll('[data-section]')) {
    const key = el.dataset.section; let s = it[key];
    if (Array.isArray(s)) s = s[spreadN++ % s.length];
    if (s === undefined) continue;
    if (key === 'spread' || key === 'caseHero' || key === 'caseNext') {
      if (s === null) continue;  // the project's own colours
      el.style.setProperty('--p-bg', `var(--${s === 'cream' ? 'cream' : s})`);
      el.style.setProperty('--p-ink', inks[s]);
      el.dataset.surface = s; el.dataset.tone = dark(s) ? 'dark' : 'light';
      continue;
    }
    if (key === 'footer') continue;  // the footer is its own deep-plum desk
    el.dataset.surface = s; el.dataset.tone = dark(s) ? 'dark' : 'light';
  }
  // no sheets: every reading surface stands straight on its section's ground (brief 5 iterations)
  if (it.noSheets) for (const el of document.querySelectorAll('[data-sheet]')) { el.removeAttribute('data-sheet'); el.removeAttribute('data-surface'); el.removeAttribute('data-tone'); }
  // sheets: a section's reading surface laid on its ground as a large paper sheet (iteration D)
  for (const [key, s] of Object.entries(it.sheets || {})) {
    for (const sec of document.querySelectorAll(`[data-section=${key}]`)) {
      const inner = sec.querySelector(':scope > .container, :scope > div > .container') || sec.firstElementChild;
      if (!inner) continue;
      inner.dataset.surface = s; inner.dataset.sheet = ''; inner.dataset.tone = dark(s) ? 'dark' : 'light';
    }
  }
  for (const [sel, s] of Object.entries(it.sheetSel || {})) {
    for (const el of document.querySelectorAll(sel)) { el.dataset.surface = s; el.dataset.sheet = ''; el.dataset.tone = dark(s) ? 'dark' : 'light'; }
  }
  // the four road cards' papers
  if (it.cards) document.querySelectorAll('[data-section=roads] [data-card]').forEach((c, i) => c.style.setProperty('--paper', it.cards[i % it.cards.length]));
  // the strip above the footer's folders takes the last section's ground (as GroundSheet does)
  const grounds = document.querySelectorAll('main [data-surface]');
  const last = grounds.length ? grounds[grounds.length - 1].dataset.surface : 'cream';
  const foot = document.querySelector("footer[data-section='footer']");
  if (foot) { foot.dataset.surface = last; foot.dataset.tone = dark(last) ? 'dark' : 'light'; }
  window.dispatchEvent(new Event('scroll'));
  window.__kvlab = 1;  // gone after a reload (a hot reload of the dev server), so the lab re-applies
  return spreadN;
})"""

CONTRAST_JS = r"""(() => {
  const lum = c => { const v = c.map(x => { x /= 255; return x <= 0.04045 ? x / 12.92 : ((x + 0.055) / 1.055) ** 2.4; }); return 0.2126 * v[0] + 0.7152 * v[1] + 0.0722 * v[2]; };
  const parse = s => { const m = s.match(/[\d.]+/g); return m ? m.map(Number) : [0, 0, 0, 0]; };
  const bgOf = el => {
    for (let e = el; e; e = e.parentElement) {
      const cs = getComputedStyle(e); const c = parse(cs.backgroundColor);
      if ((c[3] === undefined || c[3] > 0.6) && cs.backgroundColor !== 'rgba(0, 0, 0, 0)') return [c, e];
    }
    return [[243, 243, 231], document.body];
  };
  const bad = [];
  let n = 0;
  for (const el of document.querySelectorAll('body *')) {
    if (!el.childNodes.length || ![...el.childNodes].some(k => k.nodeType === 3 && k.textContent.trim())) continue;
    const r = el.getBoundingClientRect(); if (!r.width || !r.height) continue;
    // text waiting for its arrival animation (opacity 0 for now) is still checked: that is how it will look
    const cs = getComputedStyle(el); if (cs.visibility === 'hidden' || cs.display === 'none') continue;
    if (el.closest('[aria-hidden="true"], .sr-only, [data-intro]')) continue;
    const fg = parse(cs.color); const [bg, host] = bgOf(el);
    const a = fg[3] === undefined ? 1 : fg[3];
    const mix = fg.slice(0, 3).map((v, i) => v * a + bg[i] * (1 - a));
    const L1 = lum(mix), L2 = lum(bg.slice(0, 3)); const ratio = (Math.max(L1, L2) + 0.05) / (Math.min(L1, L2) + 0.05);
    const size = parseFloat(cs.fontSize), bold = +cs.fontWeight >= 600; const large = size >= 24 || (size >= 18.66 && bold);
    n++;
    if (ratio < (large ? 3 : 4.5)) bad.push({ text: el.textContent.trim().slice(0, 40), ratio: +ratio.toFixed(2), fg: cs.color, bg: `rgb(${bg.slice(0, 3).join(' ')})`,
      on: (host.className && String(host.className).split(' ')[0] || host.tagName).slice(0, 34), section: el.closest('[data-section]')?.dataset.section || '' });
  }
  return { checked: n, bad: bad.slice(0, 40), failures: bad.length };
})()"""


def screens(cap, path, it, dev, out):
    w, h = (1440, 900) if dev == "desktop" else (390, 844)
    cap.cmd("Emulation.setDeviceMetricsOverride", {"width": w, "height": h, "deviceScaleFactor": 1, "mobile": dev == "mobile"})
    cap.cmd("Emulation.setTouchEmulationEnabled", {"enabled": dev == "mobile"})
    cap.eval("try { sessionStorage.setItem('kv-intro', '1') } catch (e) {}")
    cap.goto(SITE + path, wait=3.0)
    cap.eval(APPLY_JS + "(" + json.dumps(it) + ")")
    cap.pump(0.6)
    total = {f: 0 for f in FAM_LIST}
    frames, contrast = [], {"checked": 0, "failures": 0, "bad": []}
    height = cap.eval("document.documentElement.scrollHeight")
    y, k = 0, 0
    while True:
        if not cap.eval("!!window.__kvlab"):
            print(f"  ! {path} reloaded at screen {k}: the iteration is re-applied", flush=True)
            cap.pump(2.0)
            cap.eval(APPLY_JS + "(" + json.dumps(it) + ")")
        cap.eval(f"window.scrollTo(0, {y})")
        cap.pump(0.9)
        shot = cap.cmd("Page.captureScreenshot", {"format": "jpeg", "quality": 82})
        img = Image.open(io.BytesIO(base64.b64decode(shot["data"])))
        c = classify(img)
        for f in FAM_LIST:
            total[f] += c[f]
        frames.append(img)
        img.save(out / f"{path.strip('/').replace('/', '_') or 'home'}_{k:02d}.jpg", quality=80)
        if k % 2 == 0:
            cr = cap.eval(CONTRAST_JS)
            contrast["checked"] += cr["checked"]
            contrast["failures"] += cr["failures"]
            seen = {b["text"] for b in contrast["bad"]}
            contrast["bad"] += [b for b in cr["bad"] if b["text"] not in seen][:10]
        k += 1
        height = cap.eval("document.documentElement.scrollHeight")
        if y + h >= height - 2 or k > 80:
            break
        y = min(y + h, height - h)
    if len(frames) < 6:
        print(f"  ! only {len(frames)} screens on {path} ({dev}): measurement suspect", flush=True)
    return total, frames, contrast


def strip(frames, out, cols):
    tw = 360 if frames[0].width > 800 else 150
    th = int(frames[0].height * tw / frames[0].width)
    rows = (len(frames) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * tw + (cols + 1) * 8, rows * th + (rows + 1) * 8), (40, 34, 38))
    for i, f in enumerate(frames):
        sheet.paste(f.resize((tw, th)), (8 + (i % cols) * (tw + 8), 8 + (i // cols) * (th + 8)))
    sheet.save(out, quality=84)


def run(name, devices, paths):
    it = {k: v for k, v in ITERATIONS[name].items() if k != "note"}
    result = {"iteration": name, "note": ITERATIONS[name].get("note", ""), "devices": {}}
    cap = Cap()
    try:
        for dev in devices:
            out = ROOT / name / dev
            out.mkdir(parents=True, exist_ok=True)
            agg = {f: 0 for f in FAM_LIST}
            frames_all, pages = [], {}
            for p in paths:
                t, frames, contrast = screens(cap, p, it, dev, out)
                for f in FAM_LIST:
                    agg[f] += t[f]
                n = sum(t.values())
                pages[p] = {"share": {f: round(100 * t[f] / n, 1) for f in FAM_LIST}, "screens": len(frames), "contrast": contrast}
                frames_all += frames
                strip(frames, out / f"strip_{p.strip('/').replace('/', '_') or 'home'}.jpg", 6 if dev == "desktop" else 10)
            n = sum(agg.values())
            own = n - agg["other"]
            share = {f: round(100 * agg[f] / n, 1) for f in FAM_LIST}
            result["devices"][dev] = {
                "share_all": share,
                "plum_blue_all": round(share["plum"] + share["blue"], 1),
                # of the pixels the site paints itself (photos and project colours left out)
                "plum_blue_own": round(100 * (agg["plum"] + agg["blue"]) / own, 1) if own else 0,
                "pages": pages,
            }
            print(f"{name:12s} {dev:7s} plum {share['plum']:5.1f}  blue {share['blue']:5.1f}  cream {share['cream']:5.1f}  "
                  f"ox {share['oxblood']:4.1f}  other {share['other']:5.1f}  | plum+blue {result['devices'][dev]['plum_blue_all']:5.1f}% "
                  f"(of own colour {result['devices'][dev]['plum_blue_own']:5.1f}%)  contrast fails "
                  f"{sum(pg['contrast']['failures'] for pg in pages.values())}")
    finally:
        cap.cmd("Emulation.clearDeviceMetricsOverride")
        cap.cmd("Emulation.setTouchEmulationEnabled", {"enabled": False})
        cap.ws.close()
    (ROOT / name / "result.json").write_text(json.dumps(result, indent=1), encoding="utf-8")
    return result


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "now"
    dv = sys.argv[2] if len(sys.argv) > 2 else "both"
    devices = ["desktop", "mobile"] if dv == "both" else [dv]
    paths = sys.argv[3:] or ["/"]
    names = list(ITERATIONS) if which == "all" else which.split(",")
    summary_path = ROOT / "summary.json"
    summary = json.loads(summary_path.read_text(encoding="utf-8")) if summary_path.exists() else {}
    for nm in names:
        r = run(nm, devices, paths)
        summary.setdefault(nm, {})
        for dev, d in r["devices"].items():
            summary[nm][dev + " " + ",".join(paths)] = {"plum_blue_all": d["plum_blue_all"], "plum_blue_own": d["plum_blue_own"], "share": d["share_all"]}
    ROOT.mkdir(parents=True, exist_ok=True)
    summary_path.write_text(json.dumps(summary, indent=1), encoding="utf-8")
