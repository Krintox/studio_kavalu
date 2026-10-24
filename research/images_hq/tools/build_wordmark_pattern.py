"""Rebuild studio-anokhi/wordmark-pattern.jpg (580x320) as SVG/HTML from the source.

Measured from the source (source pixel units; SVG viewBox = source frame):
- top page strip (cream) and the terracotta panel below it; the panel's soft mottled texture is the source panel itself
  with the cream elements inpainted out (normalised convolution) and enlarged 4x bicubic (it is low-frequency);
- 'studio anokhi' wordmarks (3 stacked, 2 single-line 'studioanokhi'): re-set in Arimo (Arial design; best of ~60
  fonts tested, NCC 0.85; weight ~480 from matching ink). Each line is placed so its ink box lands on the measured
  ink box. The exact original typeface (Helvetica-class) cannot be confirmed at this resolution;
- the two अ marks: smooth potrace of the source alpha;
- 'MOLDING MUD, / CREATING LOVE': re-set in Oswald 500 on the measured boxes (font evidence is weak at 8 px caps);
- the two tiny taglines (~4 px caps) are illegible, so they are kept from the source pixels, not re-set;
- everything else that is cream in the source (side dashes etc.) is kept as a soft 8x enlargement of the leftover
  source alpha, so nothing from the source is dropped.
"""
from __future__ import annotations

import base64
import io
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
SRC = os.path.join(ROOT, "website", "public", "work", "studio-anokhi", "wordmark-pattern.jpg")
OUT = os.path.join(ROOT, "research", "images_hq", "html", "studio-anokhi")
os.makedirs(OUT, exist_ok=True)

A = np.asarray(Image.open(SRC).convert("RGB")).astype(float)
H, W = A.shape[:2]
lum = A.mean(2)

# ---------------------------------------------------------------- strip / panel boundary and colours
rowl = lum.mean(1)
edge = int(np.argmax(rowl[:40] < (rowl[2:12].mean() + rowl[30:40].mean()) / 2))
# sub-pixel boundary: interpolate where the row mean crosses the midpoint
mid = (rowl[2:12].mean() + rowl[30:40].mean()) / 2
y_edge = edge - 1 + (rowl[edge - 1] - mid) / max(rowl[edge - 1] - rowl[edge], 1e-6)
STRIP = np.median(A[2:max(3, edge - 3)].reshape(-1, 3), axis=0)
PANEL = np.median(A[edge + 3:][A[edge + 3:].mean(2) < 140], axis=0)
M0 = T.fg_map(A, PANEL, [255, 218, 189])
CREAM = np.median(A[ndimage.binary_erosion(M0 > 0.85, np.ones((2, 2))) & (np.arange(H)[:, None] > edge + 2)], axis=0)
M = T.fg_map(A, PANEL, CREAM)
M[:edge + 2] = 0


def box(r0, r1, c0, c1, thr=0.5):
    x0, y0, x1, y1 = FM.ink_box(M[r0:r1, c0:c1], thr)
    return (float(x0 + c0), float(y0 + r0), float(x1 + c0), float(y1 + r0))


def lines_in(r0, r1, c0, c1, thr=0.5, min_gap=1):
    """Split a region into text lines by gaps in the row projection; returns ink boxes."""
    rows = (M[r0:r1, c0:c1] > thr).sum(1)
    out, start = [], None
    for i, v in enumerate(list(rows) + [0]):
        if v > 0 and start is None:
            start = i
        if v == 0 and start is not None:
            out.append((r0 + start, r0 + i))
            start = None
    return [box(a, b, c0, c1, thr) for a, b in out if b - a >= 3]


# ---------------------------------------------------------------- element boxes (regions picked from the overview)
WM = []   # (text, box)
# centre stacked: 'studio' / 'anokhi' (tight leading: split at the measured baseline row 163)
WM += [("studio", box(130, 163, 228, 352)), ("anokhi", box(163, 194, 228, 352))]
# top-left and top-right stacked (tight leading: split at the projection minimum, row 95)
for c0, c1 in ((38, 140), (452, 556)):
    WM += [("studio", box(68, 95, c0, c1)), ("anokhi", box(95, 120, c0, c1))]
# single-line at the top (rows 31-52) and bottom (rows 273-294)
WM += [("studioanokhi", box(26, 57, 196, 378)), ("studioanokhi", box(268, 298, 196, 378))]

CAPS = [("MOLDING MUD,", box(208, 220, 479, 542, 0.25)), ("CREATING LOVE", box(221, 233, 479, 542, 0.25))]
TAG = []
for r0, r1, c0, c1 in ((123, 131, 50, 125), (299, 308, 220, 372)):
    TAG.append(("MOLDING MUD, CREATING LOVE", box(r0, r1, c0, c1, 0.3)))

# ---------------------------------------------------------------- text placement
def placed(items, family, weight, ls=0.0):
    mets = FM.text_metrics([{"family": family, "weight": weight, "ls": ls, "html": t} for t, _ in items])
    out = []
    for (t, b), m in zip(items, mets):
        pl = FM.place(m, b)
        out.append(dict(text=t, box=b, **pl))
    return out


WM_W, CAPS_W = 480, 500
wm_p = placed(WM, "Arimo", WM_W)
# the two tiny taglines (~4 px cap height) cannot be read with certainty, so they are NOT re-set as text: they stay
# in the soft leftover layer made from the source pixels (as indistinct as in the source, nothing invented)
caps_p = placed(CAPS, "Oswald", CAPS_W)

# ---------------------------------------------------------------- अ marks: smooth trace
glyph_boxes = [(196, 262, 50, 125), (196, 240, 440, 481)]
gmask = np.zeros((H, W), bool)
for r0, r1, c0, c1 in glyph_boxes:
    gmask[r0:r1, c0:c1] = True
Ga = np.where(gmask, M, 0)
# the right glyph touches the caps text at x~479: cut there
Ga[:, 480:] = np.where(gmask[:, 480:], 0, Ga[:, 480:])
gbits = T.binary(Ga, k=8, blur=0.8, thresh=0.5)
glyph_paths = [c for c in T.trace_bitmap(gbits, 8, alphamax=1.2, opttolerance=0.4) if c["area"] > 8]

# ---------------------------------------------------------------- leftover cream (side dashes etc.): soft layer
covered = np.zeros((H, W), bool)
for p in wm_p + caps_p:
    x0, y0, x1, y1 = p["box"]
    covered[int(y0) - 2:int(np.ceil(y1)) + 2, int(x0) - 2:int(np.ceil(x1)) + 2] = True
covered |= ndimage.binary_dilation(gmask & (M > 0.2), iterations=2)
left = np.where(covered, 0, M)
left[left < 0.3] = 0                      # the panel texture itself stays below ~0.2
for _, (x0, y0, x1, y1) in TAG:           # tiny taglines: keep their faint source pixels too
    sl = (slice(int(y0) - 1, int(np.ceil(y1)) + 1), slice(int(x0) - 1, int(np.ceil(x1)) + 1))
    left[sl] = np.where(M[sl] > 0.15, M[sl], 0)
left8 = F.soft(left, 8, normalise=False, lo=0.1, hi=0.95)   # keep the faintness of these tiny marks
uri_left = F.png_uri(left8, CREAM, os.path.join(OUT, "wordmark-pattern.leftover.png"))

# ---------------------------------------------------------------- panel texture: inpaint cream, enlarge 4x
# cream elements only (texture stays below ~0.2), plus a 4 px ring: the source has dark oversharpening halos next to
# its bright text, which would otherwise be smeared into the fill as a drop shadow
hole = ndimage.binary_dilation(M > 0.25, iterations=4)
hole[:edge + 1] = False
valid = (~hole).astype(float)
valid[:edge + 1] = 0
panel_src = A.copy()
panel_src[:edge + 1] = PANEL
todo = hole.copy()
for sig in (3, 6, 12, 24):                                    # normalised convolution, growing radius for big holes
    den = ndimage.gaussian_filter(valid, sig)
    ok = todo & (den > 0.05)
    for ch in range(3):
        num = ndimage.gaussian_filter(A[..., ch] * valid, sig)
        panel_src[..., ch] = np.where(ok, num / np.maximum(den, 1e-6), panel_src[..., ch])
    todo &= ~ok
panel_src[todo] = PANEL
panel_img = Image.fromarray(np.clip(panel_src, 0, 255).astype(np.uint8)).resize((W * 4, H * 4), Image.BICUBIC)
panel_img.save(os.path.join(OUT, "wordmark-pattern.panel.png"), optimize=True)
buf = io.BytesIO()
panel_img.save(buf, "JPEG", quality=92)
uri_panel = "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()

# ---------------------------------------------------------------- SVG
def text_svg(ps, family, weight):
    out = []
    for p in ps:
        out.append('<text x="%.3f" y="%.3f" font-size="%.3f" transform="scale(1 %.4f)">%s</text>'
                   % (p["x"], p["baseline"] / p["k"], p["font_size"], p["k"], p["text"]))
    return '<g font-family="%s" font-weight="%d" fill="%s">%s</g>' % (family, weight, F.hexc(CREAM), "".join(out))


svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" preserveAspectRatio="none" width="100%%" height="100%%">'
       '<image x="0" y="0" width="%d" height="%d" preserveAspectRatio="none" href="%s"/>'
       '<rect x="0" y="0" width="%d" height="%.3f" fill="%s"/>'
       '<image x="0" y="0" width="%d" height="%d" preserveAspectRatio="none" href="%s"/>'
       '<path fill="%s" fill-rule="evenodd" d="%s"/>%s%s</svg>') % (
    W, H, W, H, uri_panel, W, y_edge, F.hexc(STRIP), W, H, uri_left, F.hexc(CREAM),
    " ".join(c["d"] for c in glyph_paths), text_svg(wm_p, "Arimo", WM_W), text_svg(caps_p, "Oswald", CAPS_W))
css_w, css_h = render.css_size_for(W, H)
html = ('<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><title>studio anokhi - wordmark pattern</title>\n'
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Arimo:wght@400..700&family=Oswald:wght@200..700&display=block">\n'
        '<!-- High-resolution recreation of website/public/work/studio-anokhi/wordmark-pattern.jpg (%dx%d), measured from the\n'
        '     source (tools/build_wordmark_pattern.py, wordmark-pattern.params.json). -->\n'
        '<style>html,body{margin:0;padding:0;background:%s} .art{width:%dpx;height:%dpx;display:block}</style>\n'
        '</head><body><div class="art">%s</div></body></html>') % (W, H, F.hexc(PANEL), css_w, css_h, svg)
hp = os.path.join(OUT, "wordmark-pattern.html")
open(hp, "w", encoding="utf-8").write(html)
params = {"strip": STRIP.tolist(), "panel": PANEL.tolist(), "cream": CREAM.tolist(), "strip_edge_y": float(y_edge),
          "wordmarks": wm_p, "caps_and_taglines": caps_p, "fonts": {"wordmark": "Arimo %d" % WM_W, "caps": "Oswald %d" % CAPS_W},
          "n_glyph_paths": len(glyph_paths)}
json.dump(params, open(os.path.join(OUT, "wordmark-pattern.params.json"), "w"), indent=1, default=float)
for p in wm_p + caps_p:
    print("%-28s box %s fs %.2f k %.3f" % (p["text"], [round(v, 1) for v in p["box"]], p["font_size"], p["k"]))
print("strip edge %.2f strip %s panel %s cream %s glyph paths %d" % (y_edge, STRIP, PANEL, CREAM, len(glyph_paths)))
print("rendered", render.render(hp, os.path.join(OUT, "wordmark-pattern.png"), css_w, css_h, 3, settle=1.5), "css", css_w, css_h)
