"""Rebuild studio-anokhi/stationery-ochre.jpg and stationery-olive.jpg (vellum stationery mock-ups) from the sources.

Layers, all derived from the source pixels (nothing redrawn):
  1. background: the gradient + the sheets' soft shadows = source pixels outside the sheets, filled under the sheets by
     normalised convolution, smoothed lightly and enlarged (it is smooth content);
  2. back sheet: crisp 70x140 rectangle (edges from gradient peaks, sub-pixel), filled with the source enlarged 8x;
  3. dark icons on the back sheet: crisp silhouettes (continuous darkness alpha + contrast curve) in their own colours;
  4. front (vellum) sheet: crisp rectangle filled with the source enlarged 8x (the faded see-through icons and its ruled
     lines are part of its observed colours);
  5. the terracotta अ printed on the vellum: crisp silhouette in its colour;
  6. the tiny 'studio anokhi' wordmark: re-set in Arimo (the face matched in wordmark-pattern) on the measured boxes.

    python build_stationery.py ochre|olive
"""
from __future__ import annotations

import base64
import io
import json
import os
import sys

import numpy as np
from PIL import Image
from scipy import ndimage

import flatsr as F
import fontmatch as FM
import render
import trace as T

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
OUT = os.path.join(ROOT, "research", "images_hq", "html", "studio-anokhi")
which = sys.argv[1] if len(sys.argv) > 1 else "ochre"
NAME = "stationery-%s" % which
A = np.asarray(Image.open(os.path.join(ROOT, "website", "public", "work", "studio-anokhi", NAME + ".jpg")).convert("RGB")).astype(float)
H, W = A.shape[:2]
L = ndimage.gaussian_filter(A.mean(2), 0.7)


def edge(profile, approx, win=4):
    """Sub-pixel position of the strongest |gradient| near approx (parabola fit); profile = |diff| summed."""
    lo, hi = int(approx - win), int(approx + win) + 1
    i = lo + int(np.argmax(profile[lo:hi]))
    y0, y1, y2 = profile[i - 1], profile[i], profile[i + 1]
    d = 0.5 * (y0 - y2) / (y0 - 2 * y1 + y2) if (y0 - 2 * y1 + y2) != 0 else 0.0
    return i + 0.5 + d


gx = np.abs(np.diff(L, axis=1))
gy = np.abs(np.diff(L, axis=0))
APPROX = {"ochre": dict(back=(55.5, 24.5, 125.5, 164.5), front=(87.5, 77.5, 157.5, 217.5)),
          "olive": dict(back=(57.5, 23.5, 127.5, 163.5), front=(89.5, 75.5, 159.5, 215.5))}[which]
rects = {}
for k, (x0, y0, x1, y1) in APPROX.items():
    rows = slice(int(y0) + 6, int(y1) - 6)
    cols = slice(int(x0) + 6, int(x1) - 6)
    ex0 = edge(gx[rows].sum(0), x0 - 0.5)
    ex1 = edge(gx[rows].sum(0), x1 - 0.5)
    ey0 = edge(gy[:, cols].sum(1), y0 - 0.5)
    ey1 = edge(gy[:, cols].sum(1), y1 - 0.5)
    rects[k] = (ex0, ey0, ex1, ey1)
yy, xx = np.mgrid[0:H, 0:W] + 0.5


def inside(r, m=0.0):
    x0, y0, x1, y1 = r
    return (xx > x0 - m) & (xx < x1 + m) & (yy > y0 - m) & (yy < y1 + m)


back_in, front_in = inside(rects["back"]), inside(rects["front"])


def extrapolate(img, valid, steps=(1.0, 2.0, 4.0, 8.0, 16.0)):
    out = img.copy()
    v = valid.astype(float)
    for sig in steps:
        den = ndimage.gaussian_filter(v, sig)
        for ch in range(3):
            num = ndimage.gaussian_filter(img[..., ch] * v, sig)
            out[..., ch] = np.where((v == 0) & (den > 0.02), num / np.maximum(den, 1e-6), out[..., ch])
        v = np.maximum(v, (den > 0.02).astype(float))
        img = out.copy()
    return out


def uri(img_rgb_or_rgba, mode, path):
    im = Image.fromarray(np.clip(img_rgb_or_rgba, 0, 255).astype(np.uint8), mode)
    im.save(path, optimize=True)
    buf = io.BytesIO()
    im.save(buf, "PNG", optimize=True)
    return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()


K = 8
# 1. background: everything outside both sheets (1 px margin so the sheet edge blur is not used)
bg_valid = ~(inside(rects["back"], 1.0) | inside(rects["front"], 1.0))
bg = extrapolate(A, bg_valid)
bg = ndimage.gaussian_filter(bg, (0.6, 0.6, 0))
uri_bg = uri(np.asarray(Image.fromarray(np.clip(bg, 0, 255).astype(np.uint8)).resize((W * 4, H * 4), Image.BICUBIC)), "RGB",
             os.path.join(OUT, NAME + ".background.png"))

# 2./4. sheet fills: the sheet's own pixels (1 px inside the edge), extrapolated outward, enlarged 8x
def sheet_fill(r, valid_extra=None):
    v = inside(r, -1.0)
    if valid_extra is not None:
        v &= valid_extra
    return extrapolate(A, v)


back_fill = sheet_fill(rects["back"], ~inside(rects["front"], 1.0))
front_fill = sheet_fill(rects["front"])
up = lambda img: np.asarray(Image.fromarray(np.clip(img, 0, 255).astype(np.uint8)).resize((W * K, H * K), Image.BICUBIC)).astype(float)
uri_back = uri(up(back_fill), "RGB", os.path.join(OUT, NAME + ".back.png"))
uri_front = uri(up(front_fill), "RGB", os.path.join(OUT, NAME + ".front.png"))

# 3. dark icons on the visible part of the back sheet: crisp silhouettes in their own colours
visible_back = back_in & ~inside(rects["front"], 0.5)
paper = np.median(A[visible_back & (A.mean(2) > 200)], axis=0)
WORD_REG = (int(rects["back"][1]) + 2, int(rects["back"][1]) + 34, int(rects["back"][0]) + 4, int(rects["back"][2]) - 4)
dark = visible_back & (A.mean(2) < 150)
wr0, wr1, wc0, wc1 = WORD_REG
dark[wr0:wr1, wc0:wc1] = False                       # the wordmark is re-set as text
ink_core = np.median(A[ndimage.binary_erosion(dark, iterations=1)], axis=0) if ndimage.binary_erosion(dark, iterations=1).any() else np.array([40.0, 30, 25])
Mi = T.fg_map(A, paper, ink_core)
grown = ndimage.binary_dilation(dark, iterations=2) & visible_back
ia = np.where(grown, np.clip(Mi / 0.85, 0, 1), 0)
ia[ndimage.binary_erosion(dark, iterations=1)] = 1.0
ink8 = F.soft(ia, K, unsharp=0.4, radius=1.0, lo=0.15, hi=0.85)   # tiny icons: smooth edges, no hard blobs
ink_col = up(extrapolate(A, ndimage.binary_erosion(dark, iterations=1) | (dark & (Mi > 0.8))))
rgba = np.zeros((H * K, W * K, 4))
rgba[..., :3] = ink_col
rgba[..., 3] = ink8 * 255
# clip the ink to the visible back sheet (it is hidden under the vellum)
vis8 = np.asarray(Image.fromarray((visible_back * 255).astype(np.uint8)).resize((W * K, H * K), Image.NEAREST)) > 0
rgba[..., 3] *= vis8
uri_ink = uri(rgba, "RGBA", os.path.join(OUT, NAME + ".ink.png"))

# 5. terracotta अ on the vellum: saturated warm pixels inside the front sheet
fr = front_in & ~inside(rects["front"], -1.0) == False
sat = A.max(2) - A.min(2)
terr = inside(rects["front"], -1.0) & (A.mean(2) < 140)
glyph_svg = ""
if terr.sum() > 6:
    vellum = np.median(A[front_in & (A.mean(2) > 200)], axis=0)
    gcol = np.median(A[terr], axis=0)
    Mg = T.fg_map(A, vellum, gcol)
    ga = np.where(ndimage.binary_dilation(terr, iterations=2) & front_in, np.clip(Mg / 0.85, 0, 1), 0)
    ga[ndimage.binary_erosion(terr, iterations=1)] = 1.0
    g8 = F.soft(ga, K, unsharp=0.4, radius=1.0, lo=0.15, hi=0.85)
    gc = up(extrapolate(A, terr))
    grgba = np.zeros((H * K, W * K, 4)); grgba[..., :3] = gc; grgba[..., 3] = g8 * 255
    glyph_svg = '<image x="0" y="0" width="%d" height="%d" preserveAspectRatio="none" href="%s"/>' % (
        W, H, uri(grgba, "RGBA", os.path.join(OUT, NAME + ".glyph.png")))
    # take the glyph out of the vellum fill so it is not doubled: paint the vellum colour under it
    front_fill_g = front_fill.copy()
    gm = ndimage.binary_dilation(terr, iterations=2)
    front_fill_g[gm] = extrapolate(A, inside(rects["front"], -1.0) & ~gm)[gm]
    uri_front = uri(up(front_fill_g), "RGB", os.path.join(OUT, NAME + ".front.png"))
else:
    gcol = None

# 6. wordmark lines on the back sheet
Mw = T.fg_map(A, paper, ink_core)
rowsum = (Mw[wr0:wr1, wc0:wc1] > 0.35).sum(1)
lines, start = [], None
for i, v in enumerate(list(rowsum) + [0]):
    if v > 0 and start is None:
        start = i
    if v == 0 and start is not None:
        lines.append((wr0 + start, wr0 + i))
        start = None
lines = [ln for ln in lines if ln[1] - ln[0] >= 3]
texts = []
if len(lines) >= 2:
    # tight leading: if the two lines touched they came out as one band; split it at its middle minimum
    for (a, b), word in zip(lines[:2], ("studio", "anokhi")):
        x0, y0, x1, y1 = FM.ink_box(Mw[a:b, wc0:wc1], 0.35)
        texts.append((word, (float(x0 + wc0), float(y0 + a), float(x1 + wc0), float(y1 + a))))
elif len(lines) == 1:
    a, b = lines[0]
    prof = (Mw[a:b, wc0:wc1] > 0.35).sum(1)
    mid = a + 2 + int(np.argmin(prof[2:-2]))
    for (aa, bb), word in zip(((a, mid), (mid, b)), ("studio", "anokhi")):
        x0, y0, x1, y1 = FM.ink_box(Mw[aa:bb, wc0:wc1], 0.35)
        texts.append((word, (float(x0 + wc0), float(y0 + aa), float(x1 + wc0), float(y1 + aa))))
WM_W = 420   # crisp letters read heavier than the blurred source at this tiny size
mets = FM.text_metrics([{"family": "Arimo", "weight": WM_W, "ls": 0, "html": t} for t, _ in texts]) if texts else []
text_svg = ""
placements = []
for (t, b), m in zip(texts, mets):
    pl = FM.place(m, b)
    placements.append({"text": t, "box": b, **pl})
    text_svg += '<text x="%.3f" y="%.3f" font-size="%.3f" transform="scale(1 %.4f)">%s</text>' % (pl["x"], pl["baseline"] / pl["k"], pl["font_size"], pl["k"], t)
# remove the wordmark pixels from the back-sheet fill (they are drawn as text): paint the paper colour there
if texts:
    wmask = np.zeros((H, W), bool)
    for _, (x0, y0, x1, y1) in texts:
        wmask[int(y0) - 1:int(np.ceil(y1)) + 1, int(x0) - 1:int(np.ceil(x1)) + 1] = True
    bf = back_fill.copy()
    bf[wmask] = extrapolate(A, inside(rects["back"], -1.0) & ~wmask & ~inside(rects["front"], 1.0))[wmask]
    uri_back = uri(up(bf), "RGB", os.path.join(OUT, NAME + ".back.png"))

# the faint side dashes of the wordmark lockup: darker-than-paper pixels in the wordmark's rows, outside the letters
if texts:
    ya = int(min(b[1] for _, b in texts)); yb = int(np.ceil(max(b[3] for _, b in texts)))
    band = np.zeros((H, W), bool); band[ya:yb, wc0 - 6:wc1 + 6] = True
    letters = np.zeros((H, W), bool)
    for _, (x0, y0, x1, y1) in texts:
        letters[int(y0) - 1:int(np.ceil(y1)) + 1, int(x0) - 2:int(np.ceil(x1)) + 2] = True
    marks = band & ~letters & visible_back & (A.mean(2) < 228)          # very faint in the source (lum 215-228)
    if marks.sum() >= 2:
        Mm = T.fg_map(A, paper, ink_core)
        ia2 = np.where(ndimage.binary_dilation(marks, iterations=1) & band & ~letters, np.clip(Mm / 0.85, 0, 1), 0)
        mk8 = F.soft(ia2, K, unsharp=0.4, radius=1.0, lo=0.15, hi=0.85)
        rgba[..., 3] = np.maximum(rgba[..., 3], mk8 * 255 * vis8)
        rgba[..., :3] = np.where((mk8 > 0.01)[..., None], up(extrapolate(A, marks))[..., :3], rgba[..., :3])
        uri_ink = uri(rgba, "RGBA", os.path.join(OUT, NAME + ".ink.png"))
        dark = dark | marks

# paper flattening: on the visible back sheet, everything that is not an icon is plain paper; replace it by a smooth
# paper field (keeps the sheet's gentle shading, drops the JPEG/oversharpening halos)
wm_big = np.zeros((H, W), bool)
for _, (x0, y0, x1, y1) in texts:
    wm_big[int(y0) - 3:int(np.ceil(y1)) + 3, int(x0) - 3:int(np.ceil(x1)) + 3] = True
paper_px = visible_back & (A.mean(2) > 150) & ~ndimage.binary_dilation(dark, iterations=3) & ~wm_big
pf = extrapolate(A, paper_px)
pf = ndimage.gaussian_filter(pf, (4, 4, 0))
bf2 = (bf if texts else back_fill).copy()
flat = visible_back & ~ndimage.binary_dilation(dark, iterations=1)
bf2[flat] = pf[flat]
uri_back = uri(up(bf2), "RGB", os.path.join(OUT, NAME + ".back.png"))


def rect_clip(cid, r):
    x0, y0, x1, y1 = r
    return '<clipPath id="%s"><rect x="%.3f" y="%.3f" width="%.3f" height="%.3f"/></clipPath>' % (cid, x0, y0, x1 - x0, y1 - y0)


svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" preserveAspectRatio="none" width="100%%" height="100%%">'
       '<defs>%s%s</defs>'
       '<image x="0" y="0" width="%d" height="%d" preserveAspectRatio="none" href="%s"/>'
       '<image clip-path="url(#back)" x="0" y="0" width="%d" height="%d" preserveAspectRatio="none" href="%s"/>'
       '<image x="0" y="0" width="%d" height="%d" preserveAspectRatio="none" href="%s"/>'
       '<g font-family="Arimo" font-weight="420" fill="%s">%s</g>'
       '<image clip-path="url(#front)" x="0" y="0" width="%d" height="%d" preserveAspectRatio="none" href="%s"/>'
       '%s</svg>') % (W, H, rect_clip("back", rects["back"]), rect_clip("front", rects["front"]),
                      W, H, uri_bg, W, H, uri_back, W, H, uri_ink, F.hexc(ink_core), text_svg, W, H, uri_front, glyph_svg)
css_w, css_h = render.css_size_for(W, H)
html = ('<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><title>studio anokhi - stationery (%s)</title>\n'
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Arimo:wght@400..700&display=block">\n'
        '<!-- High-resolution recreation of website/public/work/studio-anokhi/%s.jpg (%dx%d) from its own pixels\n'
        '     (tools/build_stationery.py, %s.params.json). -->\n'
        '<style>html,body{margin:0;padding:0;background:#000} .art{width:%dpx;height:%dpx;display:block}</style>\n'
        '</head><body><div class="art">%s</div></body></html>') % (which, NAME, W, H, NAME, css_w, css_h, svg)
hp = os.path.join(OUT, NAME + ".html")
open(hp, "w", encoding="utf-8").write(html)
json.dump({"rects": rects, "paper": paper.tolist(), "ink": ink_core.tolist(), "glyph_colour": None if gcol is None else gcol.tolist(),
           "wordmark": placements}, open(os.path.join(OUT, NAME + ".params.json"), "w"), indent=1, default=float)
print(which, "rects", {k: [round(v, 2) for v in r] for k, r in rects.items()}, "paper", paper, "ink", ink_core, "glyph", gcol,
      "wordmark", [(p["text"], [round(v, 1) for v in p["box"]], round(p["font_size"], 2)) for p in placements])
print("rendered", render.render(hp, os.path.join(OUT, NAME + ".png"), css_w, css_h, 3, settle=1.5), "css", css_w, css_h)
