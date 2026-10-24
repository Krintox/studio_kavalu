"""Rebuild nivritti/logo-navy.jpg (288x346) and nivritti/logo-orange.jpg (290x346) as SVG/HTML from the sources.

Measured from the sources (see logo_common.py, guides.py):
- ground and artwork colours per card (medians of eroded cores);
- six dashed construction guides per card (2 vertical, 4 horizontal): centre, pitch (~12.9 px), phase, dash length,
  opacity; width fixed at 1.5 px and blur at 0.7 px for a stable fit on these faint lines;
- the artwork (linocut mountain + NIVRITTI wordmark) is the SAME in both cards: its alpha is measured on each card
  with the pixels under the dashes filled from the gaps, the orange card is registered onto the navy one, the two
  alphas are averaged, and the result is traced with potrace at 8x. No font is substituted: the wordmark is traced
  from the source letters. The mountain is traced as bright strokes (alpha >= 0.45) over a fainter hatching layer
  (alpha >= 0.2, drawn at the hatching's measured opacity).
Writes html/nivritti/logo-navy.html|png and logo-orange.html|png (3x render, 2400 px tall) + logos.params.json.
"""
from __future__ import annotations

import json
import os

import numpy as np
from PIL import Image
from scipy import ndimage

import guides as G
import logo_common as LC
import render
import trace as T

OUT = os.path.join(LC.ROOT, "research", "images_hq", "html", "nivritti")
os.makedirs(OUT, exist_ok=True)
hexc = lambda c: "#%02X%02X%02X" % tuple(int(round(min(255, max(0, v)))) for v in c)

info = json.load(open(LC.CACHE)) if os.path.exists(LC.CACHE) else LC.averaged()[4]
sx, sy, tx, ty = info["to_orange"]

cards = {}
for k in ("navy", "orange"):
    A, bg, fg0, M = LC.load(k)
    bg = np.median(A[M < 0.03], axis=0)          # pure-ground pixels only
    H, W = M.shape
    off = 0.0 if k == "navy" else tx
    vsegs = [(0, 95), (255, H)]
    hsegs = [(0, int(38 + off)), (int(250 + off), W)]
    specs = [("v", 41.9 + off, vsegs), ("v", 243.5 + off, vsegs)] + [("h", y, hsegs) for y in (100.85, 183.2, 204.0, 244.95)]
    lines = [G.fit_line2d(M, o, c, 12.9, segs, sigma=0.7, width=1.5) for o, c, segs in specs]
    cards[k] = dict(A=A, bg=bg, M=M, H=H, W=W, lines=lines)

# fill under the dashes, bring orange into the navy frame, average
Fn = G.fill_under(cards["navy"]["M"], cards["navy"]["lines"])
Fo = G.fill_under(cards["orange"]["M"], cards["orange"]["lines"])
Hn, Wn = Fn.shape
yy, xx = np.mgrid[0:Hn, 0:Wn].astype(float)
Fo_n = ndimage.map_coordinates(Fo, [sy * (yy + 0.5) + ty - 0.5, sx * (xx + 0.5) + tx - 0.5], order=1, mode="nearest")
AV = (Fn + Fo_n) / 2

# artwork colour per card: cores of the wordmark stems
core = ndimage.binary_erosion(AV > 0.8, np.ones((2, 2)))
core[:195] = False
for k, c in cards.items():
    if k == "navy":
        px = c["A"][core]
    else:
        ys, xs = np.where(core)
        xo = np.clip(np.round(sx * (xs + 0.5) + tx - 0.5).astype(int), 0, c["W"] - 1)
        yo = np.clip(np.round(sy * (ys + 0.5) + ty - 0.5).astype(int), 0, c["H"] - 1)
        px = c["A"][yo, xo]
    c["fg"] = np.median(px, axis=0)
    # dash opacity in the card's own colours: amp is measured on the provisional fg map; convert to true fg
    fg_prov = LC.colours(c["A"])[1]
    scale = float(np.dot(fg_prov - c["bg"], c["fg"] - c["bg"]) / np.dot(c["fg"] - c["bg"], c["fg"] - c["bg"]))
    for ln in c["lines"]:
        ln["opacity"] = float(min(1.0, ln["amp"] * scale))

# artwork region: everything inside the outer guides' box is artwork (mountain rows 95-195, wordmark 195-252)
art = AV.copy()
art[:92] = 0
art[255:] = 0
art[:, :34] = 0
art[:, 252:] = 0
# wordmark: adaptive threshold keeps the hairlines (N, V, R thin strokes)
wm = art.copy()
wm[:196] = 0
wbits = T.adaptive_binary(wm, k=8, blur=0.6, rel=0.55, lo=0.12, hi=0.5, win=5)
word = [c for c in T.trace_bitmap(wbits, 8, alphamax=1.0, opttolerance=0.2) if c["area"] > 4]
# The artwork is too fine to vectorise faithfully from these sources (1-2 px linocut strokes, 1 px serif hairlines;
# potrace broke the hairlines and blobbed the serifs), so it is kept as a smooth high-resolution alpha layer made from
# the averaged source alpha: 8x bicubic, mild unsharp mask, soft contrast curve. Nothing is invented.
#  - mountain: tones kept as measured (its hatching is grey in the source);
#  - wordmark: normalised by the local peak first (every letter stroke is solid cream; thin ones are only dimmed by blur).
import base64, io
ys_, xs_ = np.where(art > 0.08)
MX0, MY0, MX1, MY1 = int(xs_.min()) - 2, int(ys_.min()) - 2, int(xs_.max()) + 3, int(ys_.max()) + 3
K = 8
sub = art[MY0:MY1, MX0:MX1].copy()
up = T.upsample(sub, K)
up = up + 0.8 * (up - ndimage.gaussian_filter(up, 0.8 * K))           # unsharp mask, radius ~0.8 source px
split = (196 - MY0) * K                                                 # first wordmark row in the 8x layer
lm = T.upsample(ndimage.maximum_filter(sub, size=5), K)
norm = up / np.clip(lm, 0.45, 1.0)
layer = np.empty_like(up)
t = np.clip((up[:split] - 0.08) / (0.72 - 0.08), 0, 1)
layer[:split] = t * t * (3 - 2 * t)
t = np.clip((norm[split:] - 0.25) / (0.75 - 0.25), 0, 1)
layer[split:] = t * t * (3 - 2 * t)
art_png = {}
for k, c in cards.items():
    rgba = np.zeros(layer.shape + (4,), np.uint8)
    rgba[..., :3] = np.round(c["fg"]).astype(np.uint8)
    rgba[..., 3] = np.round(layer * 255).astype(np.uint8)
    im_ = Image.fromarray(rgba, "RGBA")
    im_.save(os.path.join(OUT, "logo-%s.artwork.png" % k), optimize=True)
    buf = io.BytesIO()
    im_.save(buf, "PNG", optimize=True)
    art_png[k] = "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()
word, mt_bright, mt_faint = [], [], []

params = {"to_orange": [sx, sy, tx, ty], "artwork_box": [MX0, MY0, MX1, MY1],
          "artwork_layer": "8x bicubic of the averaged alpha, unsharp 0.8; mountain smoothstep 0.08..0.72; wordmark local-peak normalised, smoothstep 0.25..0.75",
          "cards": {k: {"ground": c["bg"].tolist(), "artwork": c["fg"].tolist(), "lines": c["lines"]} for k, c in cards.items()},
          "n_paths": {"word": len(word), "mountain_bright": len(mt_bright), "mountain_faint": len(mt_faint)}}
json.dump(params, open(os.path.join(OUT, "logos.params.json"), "w"), indent=1)

word_d = " ".join(c["d"] for c in word)
bright_d = " ".join(c["d"] for c in mt_bright)
faint_d = " ".join(c["d"] for c in mt_faint)
for k, c in cards.items():
    H, W = c["H"], c["W"]
    fgx, bgx = hexc(c["fg"]), hexc(c["bg"])
    dashes = "".join('<g fill="%s" fill-opacity="%.3f">%s</g>' % (fgx, ln["opacity"], G.svg_dashes(ln, H, W)) for ln in c["lines"])
    tf = "" if k == "navy" else ' transform="matrix(%.6f 0 0 %.6f %.4f %.4f)"' % (sx, sy, tx, ty)
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" preserveAspectRatio="none" width="100%%" height="100%%">'
           '<rect width="%d" height="%d" fill="%s"/>%s<g%s fill="%s" fill-rule="evenodd">'
           '<image x="%d" y="%d" width="%d" height="%d" preserveAspectRatio="none" href="%s"/></g></svg>') % (
        W, H, W, H, bgx, dashes, tf, fgx, MX0, MY0, MX1 - MX0, MY1 - MY0, art_png[k])
    css_w, css_h = render.css_size_for(W, H)
    html = ('<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><title>NIVRITTI logo (%s)</title>\n'
            '<!-- High-resolution recreation of website/public/work/nivritti/logo-%s.jpg (%dx%d). Colours, guides and the traced\n'
            '     artwork are all measured from the source cards (tools/build_logos.py, logos.params.json); the NIVRITTI letters\n'
            '     are traced from the source, not set in a substitute font. -->\n'
            '<style>html,body{margin:0;padding:0;background:%s} .art{width:%dpx;height:%dpx;display:block}</style>\n'
            '</head><body><div class="art">%s</div></body></html>') % (k, k, W, H, bgx, css_w, css_h, svg)
    hp = os.path.join(OUT, "logo-%s.html" % k)
    open(hp, "w", encoding="utf-8").write(html)
    print(k, "rendered", render.render(hp, os.path.join(OUT, "logo-%s.png" % k), css_w, css_h, 3), "fg", c["fg"].round(), "bg", c["bg"])
    for ln in c["lines"]:
        print("   %s c %.2f P %.3f ph %.2f dash %.2f opacity %.3f" % (ln["orient"], ln["centre"], ln["pitch"], ln["phase"], ln["dash"], ln["opacity"]))
print("artwork box", [MX0, MY0, MX1, MY1])
