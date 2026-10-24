"""Rebuild studio-anokhi/mark-evolution.jpg (580x294) as SVG/HTML from the source.

Measured from the source, in source pixel units (SVG viewBox = source frame):
- ground: flat (229,215,189) everywhere (checked at the four corners and the centre);
- dark shapes (pot, the '3', the अ): traced with potrace from the dark-layer alpha (8x, smoothed), as for mark-orange;
- sage pot under the '3': the source's own soft-edged shape, unmixed and enlarged 8x (flatsr.soft);
- arrows: 1.22 px shafts (integrated alpha) at y 124.9, from x 126 / 321 to the arrowhead bases, with 9 px x 5 px
  heads (tips at 222.5 / 417.5), drawn as vectors;
- 'logo mark' and the 2-line paragraph: re-set in Figtree (best match for the label: NCC 0.84 vs 0.68 for Arial; the
  paragraph scores tie), each placed so its ink box lands on the measured ink box. Wording checked by rendering
  alternatives and scoring them against the source ("It is", "mould", "notice", bold "Anokhi" in line 2).
"""
from __future__ import annotations

import json
import os

import numpy as np
from PIL import Image
from scipy import ndimage

import flatsr as F
import fontmatch as FM
import render
import trace as T

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
SRC = os.path.join(ROOT, "website", "public", "work", "studio-anokhi", "mark-evolution.jpg")
OUT = os.path.join(ROOT, "research", "images_hq", "html", "studio-anokhi")
os.makedirs(OUT, exist_ok=True)

A = np.asarray(Image.open(SRC).convert("RGB")).astype(float)
H, W = A.shape[:2]
lum = A.mean(2)
GROUND = np.median(A[ndimage.binary_erosion(np.abs(A - [230, 216, 190]).sum(2) < 18, np.ones((7, 7)))], axis=0)
DARK = np.median(A[ndimage.binary_erosion(lum < 70, np.ones((3, 3)))], axis=0)
reg = A[85:160, 235:300].reshape(-1, 3)
SAGE = np.median(reg[(np.abs(reg - GROUND).sum(1) > 40) & (reg.mean(1) > 110)], axis=0)

lay = F.layered(F.unmix(A, GROUND, [SAGE, DARK]))
sage_a, dark_a = lay[..., 0].copy(), lay[..., 1].copy()
keep = np.zeros((H, W), bool)
keep[60:175, 200:300] = True
sage_a[~keep] = 0
sage_a[sage_a < 0.12] = 0

# --- regions handled separately
ARROWS = [dict(x_start=126.0, x_base=213.0, x_tip=222.5, y=124.9), dict(x_start=321.0, x_base=408.5, x_tip=417.5, y=124.9)]
SHAFT = 1.22
HEAD_H = 5.0
PARA = (138, 192, 400, 220)
LABEL = (225, 248, 360, 290)
shapes = dark_a.copy()
shapes[116:134, 118:232] = 0
shapes[116:134, 313:427] = 0
shapes[PARA[1]:PARA[3], PARA[0]:PARA[2]] = 0
shapes[LABEL[1]:LABEL[3], LABEL[0]:LABEL[2]] = 0

# --- dark shapes: smooth potrace (thick shapes; JPEG wobble removed by the blur)
bits = T.binary(shapes, k=8, blur=0.9, thresh=0.5)
dark_paths = [c for c in T.trace_bitmap(bits, 8, alphamax=1.2, opttolerance=0.5) if c["area"] > 6]

# --- sage pot: flat shape, traced smoothly (the soft layer showed JPEG blotches); hidden part under the '3' is
#     filled from the neighbourhood by flatsr.layered and covered by the dark '3' anyway
raw = F.unmix(A, GROUND, [SAGE, DARK])
vis_sage = raw[..., 0] * keep                                  # sage share of the pixel colour, visible parts only
# sage is colour-confusable with ground + ~15% dark, so anti-aliased edges of dark shapes also read as 'sage';
# those fringes are disconnected from the real pot, so keep only the largest connected sage region
lab_, n_ = ndimage.label(vis_sage > 0.45)
core_s = lab_ == (1 + int(np.argmax(ndimage.sum(np.ones_like(vis_sage), lab_, range(1, n_ + 1)))))
vis_sage = vis_sage * ndimage.binary_dilation(core_s, iterations=1)
# the sage fills the 3's bowls up to its stroke; the 1-2 px light halo between them is an oversharpening artifact.
# union(sage core, '3'), fill the enclosed gaps, shrink 2 px so the right side stays hidden inside the stroke,
# then add the visible sage core back so the left edge is exactly the source's.
three = (raw[..., 1] > 0.5) & keep
three[:, :235] = False                                         # exclude the arrowhead
U = ndimage.binary_fill_holes(ndimage.binary_closing(core_s | three, iterations=2))
sage_fill = (ndimage.binary_erosion(U, iterations=2) | core_s).astype(float)
sage_fill = np.maximum(sage_fill, vis_sage * ndimage.binary_dilation(core_s, iterations=1))
sbits = T.binary(np.clip(sage_fill, 0, 1), k=8, blur=1.6, thresh=0.5)
lab8, n8 = ndimage.label(sbits)
if n8 > 1:
    sbits = lab8 == (1 + int(np.argmax(ndimage.sum(sbits, lab8, range(1, n8 + 1)))))
sage_paths = [c for c in T.trace_bitmap(sbits, 8, alphamax=1.2, opttolerance=0.5) if c["area"] > 20]

# --- text: measure the source ink boxes, then place Figtree text on them
M = T.fg_map(A, GROUND, DARK)


def ink(r0, r1, c0, c1, thr):
    x0, y0, x1, y1 = FM.ink_box(M[r0:r1, c0:c1], thr)
    return (float(x0 + c0), float(y0 + r0), float(x1 + c0), float(y1 + r0))


# weights chosen by matching total ink in each box at source scale (Figtree is variable 300-900):
#   paragraph line 1: 500 -> 0.94, 600 -> 1.03 of the source ink => ~570; label: 400 -> 0.92, 500 -> 1.07 => ~450
TEXTS = [
    dict(html="It is more than a studio; Anokhi is where time passes without notice,", box=ink(193, 207, 120, 470, 0.2), weight=570, ls=0),
    dict(html='where memories are shaped and you mould something as <tspan font-weight="760">Anokhi</tspan> as you.',
         box=ink(206, 220, 120, 470, 0.3), weight=570, ls=0),
    dict(html="logo mark", box=ink(245, 292, 180, 400, 0.3), weight=450, ls=-0.04),
]
mets = FM.text_metrics([{"family": "Figtree", "weight": t["weight"], "ls": t["ls"], "html": t["html"]} for t in TEXTS])
svg_text = []
for i, (t, m) in enumerate(zip(TEXTS, mets)):
    pl = FM.place(m, t["box"])
    extra = ""
    if i == 1:
        # same size and stretch as line 1 (its ink box picks up JPEG noise rows); baseline from its own ink top,
        # width pinned to the measured line width
        ref = TEXTS[0]["placement"]
        sy = ref["font_size"] * ref["k"] / m["size"]
        pl = {"font_size": ref["font_size"], "k": ref["k"], "x": t["box"][0] - m["ink_left"] * ref["font_size"] / m["size"],
              "baseline": t["box"][1] - m["ink_top"] * sy}
        extra = ' textLength="%.2f" lengthAdjust="spacing"' % (t["box"][2] - t["box"][0] + (m["ink_left"]) * ref["font_size"] / m["size"])
    t["placement"] = pl
    svg_text.append('<text x="%.3f" y="%.3f" font-size="%.3f" letter-spacing="%sem" font-weight="%d" transform="scale(1 %.4f)"%s>%s</text>'
                    % (pl["x"], pl["baseline"] / pl["k"], pl["font_size"], t["ls"], t["weight"], pl["k"], extra, t["html"]))

# --- arrows
arrow_svg = []
for a in ARROWS:
    arrow_svg.append('<rect x="%.2f" y="%.3f" width="%.2f" height="%.3f"/>' % (a["x_start"], a["y"] - SHAFT / 2, a["x_base"] - a["x_start"] + 0.5, SHAFT))
    arrow_svg.append('<polygon points="%.2f,%.2f %.2f,%.2f %.2f,%.2f"/>' % (a["x_base"], a["y"] - HEAD_H / 2, a["x_tip"], a["y"], a["x_base"], a["y"] + HEAD_H / 2))

params = {"ground": GROUND.tolist(), "dark": DARK.tolist(), "sage": SAGE.tolist(), "arrows": ARROWS, "shaft": SHAFT,
          "head_height": HEAD_H, "texts": [{"html": t["html"], "box": t["box"], **t["placement"]} for t in TEXTS],
          "font": "Figtree (Google Fonts)", "n_dark_paths": len(dark_paths)}
json.dump(params, open(os.path.join(OUT, "mark-evolution.params.json"), "w"), indent=1)

svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" preserveAspectRatio="none" width="100%%" height="100%%">'
       '<rect width="%d" height="%d" fill="%s"/>'
       '<path fill="%s" fill-rule="evenodd" d="%s"/>'
       '<g fill="%s"><path fill-rule="evenodd" d="%s"/>%s</g>'
       '<g font-family="Figtree, sans-serif" fill="%s">%s</g></svg>') % (
    W, H, W, H, F.hexc(GROUND), F.hexc(SAGE), " ".join(c["d"] for c in sage_paths), F.hexc(DARK),
    " ".join(c["d"] for c in dark_paths), "".join(arrow_svg), F.hexc(DARK), "".join(svg_text))
css_w, css_h = render.css_size_for(W, H)
html = ('<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><title>studio anokhi - logo mark evolution</title>\n'
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Figtree:wght@300..900&display=block">\n'
        '<!-- High-resolution recreation of website/public/work/studio-anokhi/mark-evolution.jpg (%dx%d), measured from\n'
        '     the source (tools/build_mark_evolution.py, mark-evolution.params.json). -->\n'
        '<style>html,body{margin:0;padding:0;background:%s} .art{width:%dpx;height:%dpx;display:block}</style>\n'
        '</head><body><div class="art">%s</div></body></html>') % (W, H, F.hexc(GROUND), css_w, css_h, svg)
hp = os.path.join(OUT, "mark-evolution.html")
open(hp, "w", encoding="utf-8").write(html)
for t in TEXTS:
    print("%-12s box %s -> fs %.2f k %.3f" % (t["html"][:12], [round(v, 1) for v in t["box"]], t["placement"]["font_size"], t["placement"]["k"]))
print("rendered", render.render(hp, os.path.join(OUT, "mark-evolution.png"), css_w, css_h, 3, settle=1.5), "dark paths", len(dark_paths))
