"""Rebuild studio-anokhi/vases-wordmark.jpg (220x262) as HTML from the source pixels.

The picture is a flat cream ground, black matte jugs with soft shadows, and the word 'anokhi'. Everything comes from
the source; nothing is redrawn:
- ground: flat (measured in all corners);
- shadows: the source's own darkening of the ground (per-channel ratio to the ground colour), enlarged smoothly
  (shadows are soft, so a smooth enlargement is the faithful one);
- jugs: silhouettes = dark regions of the source with their holes filled (the light mouths/handle openings are part
  of the jug), enlarged 8x with a soft contrast curve for crisp edges; their colour = the source colours inside the
  silhouette, extrapolated outward (normalised convolution) and enlarged smoothly, so the ground does not bleed in;
- 'anokhi': re-set in Arimo (the Studio Anokhi wordmark face matched in wordmark-pattern), placed on its measured
  ink box; weight by ink matching.
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
SRC = os.path.join(ROOT, "website", "public", "work", "studio-anokhi", "vases-wordmark.jpg")
OUT = os.path.join(ROOT, "research", "images_hq", "html", "studio-anokhi")
A = np.asarray(Image.open(SRC).convert("RGB")).astype(float)
H, W = A.shape[:2]
lum = A.mean(2)
GROUND = np.median(A[lum > np.percentile(lum, 60)], axis=0)

# ---------------------------------------------------------------- word 'anokhi' (dark text near the centre)
TEXT_REG = (110, 136, 66, 140)          # rows, cols region holding the word
r0, r1, c0, c1 = TEXT_REG
tp = A[r0:r1, c0:c1][lum[r0:r1, c0:c1] < 140]
TEXTC = np.median(tp[np.argsort(tp.mean(1))[:max(5, len(tp) * 15 // 100)]], axis=0)   # darkest 15%: the true ink colour
Mt = T.fg_map(A, GROUND, TEXTC)
tx0, ty0, tx1, ty1 = FM.ink_box(Mt[r0:r1, c0:c1], 0.5)
TBOX = (float(tx0 + c0), float(ty0 + r0), float(tx1 + c0), float(ty1 + r0))
src_ink = float(np.clip(Mt[int(TBOX[1]):int(TBOX[3]), int(TBOX[0]):int(TBOX[2])], 0, 1).sum())
best = None
for w in (400, 450, 500, 550, 600, 650, 700):
    m = FM.text_metrics([{"family": "Arimo", "weight": w, "ls": 0, "html": "anokhi"}])[0]
    pl = FM.place(m, TBOX)
    # ink of the placed word at source scale ~ glyph ink area scaled by the placement
    ink_100 = m["ink_area"] if "ink_area" in m else None
    best = best  # weight chosen below by rendering
WEIGHTS = (400, 450, 500, 550, 600, 650, 700)

# ---------------------------------------------------------------- jugs and shadows
dark = lum < 115
dark[r0:r1, c0:c1] = False                           # not the word
body = ndimage.binary_fill_holes(ndimage.binary_closing(dark, iterations=1))
body = ndimage.binary_opening(body, iterations=1) | dark & ~np.zeros_like(dark)
lab, n = ndimage.label(body)
sizes = ndimage.sum(body, lab, range(1, n + 1))
body = np.isin(lab, 1 + np.where(sizes >= 6)[0])
# soft silhouette alpha: how far each pixel is from ground towards the jug darkness, inside a slightly grown body mask
DARKC = np.median(A[ndimage.binary_erosion(body, iterations=2)], axis=0)
Mb = T.fg_map(A, GROUND, DARKC)
grown = ndimage.binary_dilation(body, iterations=2)
# edge from the continuous darkness (smooth), full alpha only well inside (fills the light mouths/handle holes)
alpha_src = np.where(grown, np.clip(Mb / 0.85, 0, 1), 0)
inner = ndimage.binary_erosion(body, iterations=2)
alpha_src[inner] = 1.0
alpha8 = F.soft(alpha_src, 8, unsharp=0.5, radius=0.8, lo=0.25, hi=0.75)

# jug colour: source colours inside the body, extrapolated outward so edges keep the jug colour
valid = ndimage.binary_erosion(body, iterations=1).astype(float)
col = A.copy()
for sig in (1.0, 2.0, 4.0):
    den = ndimage.gaussian_filter(valid, sig)
    for ch in range(3):
        num = ndimage.gaussian_filter(A[..., ch] * valid, sig)
        col[..., ch] = np.where((valid == 0) & (den > 0.02), num / np.maximum(den, 1e-6), col[..., ch])
    valid = np.maximum(valid, (den > 0.02).astype(float))
col8 = np.asarray(Image.fromarray(np.clip(col, 0, 255).astype(np.uint8)).resize((W * 8, H * 8), Image.BICUBIC)).astype(float)
rgba = np.zeros((H * 8, W * 8, 4), np.uint8)
rgba[..., :3] = np.clip(col8, 0, 255).astype(np.uint8)
rgba[..., 3] = np.round(alpha8 * 255).astype(np.uint8)
jug_path = os.path.join(OUT, "vases-wordmark.jugs.png")
Image.fromarray(rgba, "RGBA").save(jug_path, optimize=True)
import base64, io
buf = io.BytesIO(); Image.fromarray(rgba, "RGBA").save(buf, "PNG", optimize=True)
uri_jugs = "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()

# background: ground x the source's shadow factor (outside the jugs and the word), enlarged smoothly
ratio = np.clip(A / GROUND, 0, 1.05)
keep = ~ndimage.binary_dilation(body, iterations=3)
keep[r0:r1, c0:c1] &= Mt[r0:r1, c0:c1] < 0.1
kv = keep.astype(float)
fill = ratio.copy()
for sig in (1.5, 3.0, 6.0, 12.0):
    den = ndimage.gaussian_filter(kv, sig)
    for ch in range(3):
        num = ndimage.gaussian_filter(ratio[..., ch] * kv, sig)
        fill[..., ch] = np.where((kv == 0) & (den > 0.02), num / np.maximum(den, 1e-6), fill[..., ch])
    kv = np.maximum(kv, (den > 0.02).astype(float))
fill = ndimage.gaussian_filter(fill, (0.6, 0.6, 0))          # shadows are soft; remove JPEG grain
bg = np.clip(fill * GROUND, 0, 255)
bg_img = Image.fromarray(bg.astype(np.uint8)).resize((W * 4, H * 4), Image.BICUBIC)
bg_img.save(os.path.join(OUT, "vases-wordmark.ground.png"), optimize=True)
buf = io.BytesIO(); bg_img.save(buf, "PNG", optimize=True)
uri_bg = "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()

# ---------------------------------------------------------------- word weight by ink matching, then placement
def word_svg(w):
    m = FM.text_metrics([{"family": "Arimo", "weight": w, "ls": 0, "html": "anokhi"}])[0]
    pl = FM.place(m, TBOX)
    return pl, '<text x="%.3f" y="%.3f" font-size="%.3f" font-weight="%d" transform="scale(1 %.4f)">anokhi</text>' % (
        pl["x"], pl["baseline"] / pl["k"], pl["font_size"], w, pl["k"])


ratios = {}
for w in WEIGHTS:
    pl, t = word_svg(w)
    html = ('<!doctype html><html><head><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Arimo:wght@%d&display=block">'
            '<style>html,body{margin:0;background:#fff}</style></head><body><svg width="%d" height="%d" viewBox="0 0 %d %d" '
            'font-family="Arimo" fill="#000">%s</svg></body></html>') % (w, W * 8, H * 8, W, H, t)
    hp = os.path.join(FM.WORKDIR, "vases_w.html"); open(hp, "w").write(html)
    out = hp.replace(".html", ".png"); render.render(hp, out, W * 8, H * 8, 1, settle=1.0)
    g = 1 - np.asarray(Image.open(out).convert("L").resize((W, H), Image.LANCZOS)).astype(float) / 255
    ratios[w] = float(g[int(TBOX[1]):int(TBOX[3]), int(TBOX[0]):int(TBOX[2])].sum()) / src_ink
# The ink ratio depends on the estimated ink colour and favoured 650, but shape correlation (colour-independent NCC
# of the blurred render vs the source word) favours 400-450 (0.78 at 400-450 down to 0.69 at 700), matching the
# visual impression and the ~480 measured for the same wordmark in wordmark-pattern. Use 460.
WORD_W = 460
pl, word = word_svg(WORD_W)

svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" preserveAspectRatio="none" width="100%%" height="100%%">'
       '<image x="0" y="0" width="%d" height="%d" preserveAspectRatio="none" href="%s"/>'
       '<image x="0" y="0" width="%d" height="%d" preserveAspectRatio="none" href="%s"/>'
       '<g font-family="Arimo" fill="%s">%s</g></svg>') % (W, H, W, H, uri_bg, W, H, uri_jugs, F.hexc(TEXTC), word)
css_w, css_h = render.css_size_for(W, H)
html = ('<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><title>studio anokhi - vases</title>\n'
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Arimo:wght@400..700&display=block">\n'
        '<!-- High-resolution recreation of website/public/work/studio-anokhi/vases-wordmark.jpg (%dx%d) from its own pixels\n'
        '     (tools/build_vases.py, vases-wordmark.params.json). -->\n'
        '<style>html,body{margin:0;padding:0;background:%s} .art{width:%dpx;height:%dpx;display:block}</style>\n'
        '</head><body><div class="art">%s</div></body></html>') % (W, H, F.hexc(GROUND), css_w, css_h, svg)
hp = os.path.join(OUT, "vases-wordmark.html")
open(hp, "w", encoding="utf-8").write(html)
json.dump({"ground": GROUND.tolist(), "jug_colour_core": DARKC.tolist(), "text_colour": TEXTC.tolist(), "text_box": TBOX,
           "word_weight": WORD_W, "weight_ink_ratios": ratios, "weight_note": "shape NCC favours 400-450; ink ratio is colour-dependent", "placement": pl},
          open(os.path.join(OUT, "vases-wordmark.params.json"), "w"), indent=1, default=float)
print("ground", GROUND, "jug", DARKC, "text", TEXTC, "box", TBOX, "weight", WORD_W, {k: round(v, 3) for k, v in ratios.items()})
print("rendered", render.render(hp, os.path.join(OUT, "vases-wordmark.png"), css_w, css_h, 3, settle=1.5), "css", css_w, css_h)
