"""Rebuild studio-anokhi/mark-orange.jpg as SVG/HTML from measurements of the source itself.

Layers (bottom to top), all measured from the 216x262 source in source pixel units (SVG viewBox = source frame;
the crop is stretched ~1.19x vertically - dot pitch 5.97 px on vertical guides vs 4.95 px on horizontal ones -
and that geometry is kept):
  1. ochre ground                         median of the eroded background core
  2. corner crescents (peach)             potrace of the soft mask in their own colour
  3. the अ glyph (cream)                  potrace of the soft mask, 8x bicubic enlargement
  4. dotted guides (light orange), on top  per-line 2D fit: centre, width, pitch, phase, dot length, blur
Where a guide dot covers the glyph or a crescent, the pixels under the dot are treated as missing and filled by
interpolating along the guide from the gaps between dots, so the traced edges follow what is visible there.
Writes html/studio-anokhi/mark-orange.html (+ .params.json) and renders mark-orange.png at 3x.
"""
from __future__ import annotations

import json
import os
from math import sqrt

import numpy as np
from PIL import Image
from scipy import ndimage, optimize
from scipy.special import erf

import render
import trace as T

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
SRC = os.path.join(ROOT, "website", "public", "work", "studio-anokhi", "mark-orange.jpg")
OUT_DIR = os.path.join(ROOT, "research", "images_hq", "html", "studio-anokhi")
os.makedirs(OUT_DIR, exist_ok=True)
hexc = lambda c: "#%02X%02X%02X" % tuple(int(round(min(255, max(0, v)))) for v in c)

im = Image.open(SRC).convert("RGB")
A = np.asarray(im).astype(float)
H, W = A.shape[:2]
lum = A.mean(2)
FG = np.median(A[ndimage.binary_erosion(lum > 200, np.ones((5, 5)))], axis=0)   # glyph cream
BG = np.median(A[ndimage.binary_erosion(lum < 150, np.ones((5, 5)))], axis=0)   # ochre ground
M = T.fg_map(A, BG, FG)
corner = np.zeros((H, W), bool)
corner[:51, :17] = corner[:51, 198:] = corner[212:, :17] = corner[212:, 198:] = True


def blurred_box(x, c, w, s):
    s = max(s, 0.25)
    return 0.5 * (erf((x - c + w / 2) / (sqrt(2) * s)) - erf((x - c - w / 2) / (sqrt(2) * s)))


# ---------------------------------------------------------------- dot colour (brightest dot cores, off-glyph)
cand = []
for x0, x1, rows in ((17, 21, np.r_[60:160]), (193, 197, np.r_[70:200])):
    blk = A[rows, x0:x1].reshape(-1, 3)
    cand.append(blk[np.argsort(-blk[:, 0] - blk[:, 1])[:12]])
for y0, y1, cols in ((51, 55, np.r_[24:110]), (207, 211, np.r_[112:192])):
    blk = A[y0:y1][:, cols].reshape(-1, 3)
    cand.append(blk[np.argsort(-blk[:, 0] - blk[:, 1])[:12]])
DOT = np.median(np.vstack(cand), axis=0)
DOT_AMP = float(T.fg_map(DOT[None, None], BG, FG)[0, 0])     # a fully covered dot pixel, in glyph-map units


def fit_along_init(prof, P0):
    x = np.arange(len(prof)) + 0.5
    p = prof - prof.mean()
    best = None
    for PP in np.linspace(P0 * 0.95, P0 * 1.05, 81):
        c = (p * np.cos(2 * np.pi * x / PP)).sum()
        s = (p * np.sin(2 * np.pi * x / PP)).sum()
        if best is None or np.hypot(c, s) > best[0]:
            best = (np.hypot(c, s), PP, np.arctan2(s, c))
    _, P, ang = best
    return P, (ang / (2 * np.pi) * P) % P


def fit_line2d(orient, c0, P0, seg):
    lo, hi = seg
    if orient == "v":
        x0, x1 = int(c0) - 3, int(c0) + 4
        sub = M[lo:hi, x0:x1]
        X, Y = np.meshgrid(np.arange(x0, x1) + 0.5, np.arange(lo, hi) + 0.5)
        along, cross, prof = Y, X, sub.mean(1)
    else:
        y0, y1 = int(c0) - 3, int(c0) + 4
        sub = M[y0:y1, lo:hi]
        X, Y = np.meshgrid(np.arange(lo, hi) + 0.5, np.arange(y0, y1) + 0.5)
        along, cross, prof = X, Y, sub.mean(0)
    P_, ph_ = fit_along_init(prof, P0)
    ph_ = (ph_ + lo) % P_

    def model(p):
        c, w, P, ph, L, s = p
        u = ((along - ph) / P + 0.5) % 1.0 - 0.5
        return DOT_AMP * blurred_box(cross, c, w, s) * blurred_box(u * P, 0.0, L, s)

    def cost(p):
        if not (0.8 < p[1] < 5 and 0.8 < p[4] < p[2] * 0.95 and 0.3 < p[5] < 1.5):
            return 1e9
        return ((model(p) - sub) ** 2).sum()

    best = None
    for L0 in (2.0, 2.6, 3.2):
        for s0 in (0.5, 0.8):
            r = optimize.minimize(cost, [c0, 2.3, P_, ph_, L0, s0], method="Nelder-Mead",
                                  options={"maxiter": 10000, "xatol": 1e-4, "fatol": 1e-9})
            if best is None or r.fun < best.fun:
                best = r
    c, w, P, ph, L, s = best.x
    return dict(orient=orient, centre=float(c), width=float(w), pitch=float(P), phase=float(ph % P),
                dot_len=float(L), sigma=float(s), seg=[lo, hi], rss=float(best.fun))


lines = {
    "left": fit_line2d("v", 19.0, 5.97, (56, 160)),
    "right": fit_line2d("v", 194.6, 5.97, (70, 206)),
    "top": fit_line2d("h", 52.9, 4.95, (22, 112)),
    "bottom": fit_line2d("h", 209.0, 4.95, (112, 193)),
}


def dot_centres(ln):
    total = H if ln["orient"] == "v" else W
    t = ln["phase"] - ln["pitch"] * np.ceil(ln["phase"] / ln["pitch"])
    out = []
    while t < total + ln["pitch"]:
        out.append(float(t))
        t += ln["pitch"]
    return out


# ---------------------------------------------------------------- fill the pixels under the dots
yy, xx = np.mgrid[0:H, 0:W] + 0.5


def dot_cov(ln):
    D = np.zeros((H, W))
    s = ln["sigma"]
    for t in dot_centres(ln):
        if ln["orient"] == "v":
            D = np.maximum(D, blurred_box(xx, ln["centre"], ln["width"], s) * blurred_box(yy, t, ln["dot_len"], s))
        else:
            D = np.maximum(D, blurred_box(xx, t, ln["dot_len"], s) * blurred_box(yy, ln["centre"], ln["width"], s))
    return D


def fill_under_dots(F: np.ndarray) -> np.ndarray:
    F = F.copy()
    for ln in lines.values():
        miss = dot_cov(ln) > 0.06
        if ln["orient"] == "h":
            for r in np.where(miss.any(1))[0]:
                m = miss[r]
                if m.all():
                    continue
                F[r, m] = np.interp(np.where(m)[0], np.where(~m)[0], F[r, ~m])
        else:
            for c in np.where(miss.any(0))[0]:
                m = miss[:, c]
                if m.all():
                    continue
                F[m, c] = np.interp(np.where(m)[0], np.where(~m)[0], F[~m, c])
    return F


GLYPH_BLUR = 0.95   # source px; removes JPEG wobble from the traced outline (corners stay within ~1 px)
Mf = fill_under_dots(M)
Mf[corner] = 0
bits = T.binary(Mf, k=8, blur=GLYPH_BLUR, thresh=0.5)
lab, nlab = ndimage.label(bits)
if nlab > 1:
    sizes = ndimage.sum(bits, lab, range(1, nlab + 1))
    bits = lab == (1 + int(np.argmax(sizes)))
glyph = [c for c in T.trace_bitmap(bits, 8, alphamax=1.25, opttolerance=0.6) if c["area"] > 30]
glyph.sort(key=lambda c: -c["area"])

# corner crescents = four identical construction circles centred outside the frame, fitted jointly
ARC = np.median(A[ndimage.binary_erosion(corner & (M > 0.55), np.ones((3, 3)))], axis=0)
KSTR = lines["left"]["pitch"] / ((lines["top"]["pitch"] + lines["bottom"]["pitch"]) / 2)   # vertical stretch
Mr = fill_under_dots(M)
# corner cells are bounded by the guide centre lines; the circles are clipped to these cells in the source
GXL, GXR = lines["left"]["centre"], lines["right"]["centre"]
GYT, GYB = lines["top"]["centre"], lines["bottom"]["centre"]
yy0, xx0 = np.mgrid[0:H, 0:W] + 0.5
cellmask = ((xx0 < GXL) | (xx0 > GXR)) & ((yy0 < GYT) | (yy0 > GYB))
far = (np.abs(xx0 - GXL) > 1.6) & (np.abs(xx0 - GXR) > 1.6) & (np.abs(yy0 - GYT) > 1.6) & (np.abs(yy0 - GYB) > 1.6)
reg_mask = cellmask & far
ys_r, xs_r = np.where(reg_mask)
Px, Py = xs_r + 0.5, ys_r + 0.5
target = Mr[reg_mask]


def ring_model(p):
    xl, xr, yt, yb, r, w, amp = p
    cov = np.zeros(len(Px))
    for cx in (xl, xr):
        for cy in (yt, yb):
            d = np.sqrt((Px - cx) ** 2 + ((Py - cy) / KSTR) ** 2) - r     # signed radial offset (unstretched units)
            c = 0.5 * (erf((w / 2 - d) / (sqrt(2) * 0.6)) + erf((w / 2 + d) / (sqrt(2) * 0.6)))
            cov = np.maximum(cov, c)
    return amp * cov


def ring_cost(p):
    if not (5 < p[4] < 60 and 2 < p[5] < 16):
        return 1e9
    return ((ring_model(p) - target) ** 2).sum()


best = None
for r0 in (20.0, 24.0, 28.0):
    for w0 in (6.0, 8.0):
        r_ = optimize.minimize(ring_cost, [-11.0, 227.0, 27.0, 236.0, r0, w0, 0.68], method="Powell",
                               options={"maxiter": 20000, "xtol": 1e-3, "ftol": 1e-7})
        if best is None or r_.fun < best.fun:
            best = r_
xl, xr, yt, yb, RR, WW, AMP = [float(v) for v in best.x]
rings = {"centres": [[xl, yt], [xr, yt], [xl, yb], [xr, yb]], "r": RR, "stroke": WW, "amp": AMP,
         "vertical_stretch": KSTR, "rss": float(best.fun)}
print("rings", {k: (round(v, 3) if isinstance(v, float) else v) for k, v in rings.items()})
params = {"ground": BG.tolist(), "glyph_colour": FG.tolist(), "ring_colour": ARC.tolist(), "dot_colour": DOT.tolist(),
          "dot_amp_in_glyph_units": DOT_AMP, "lines": lines, "rings": rings, "glyph_blur": GLYPH_BLUR,
          "glyph_bbox": glyph[0]["bbox"] if glyph else None, "n_glyph_curves": len(glyph)}
json.dump(params, open(os.path.join(OUT_DIR, "mark-orange.params.json"), "w"), indent=1)
for k, v in lines.items():
    print(f"{k:6s} c {v['centre']:.2f} w {v['width']:.2f} | P {v['pitch']:.3f} ph {v['phase']:.2f} "
          f"dot {v['dot_len']:.2f} sig {v['sigma']:.2f} rss {v['rss']:.3f}")
print("ground", BG, "glyph", FG, "crescent", ARC, "dot", DOT.round(), "dot amp", round(DOT_AMP, 3))
print("glyph bbox", params["glyph_bbox"])

# ---------------------------------------------------------------- SVG / HTML
dots = []
for ln in lines.values():
    for t in dot_centres(ln):
        if ln["orient"] == "v":
            x, y, w_, h_ = ln["centre"] - ln["width"] / 2, t - ln["dot_len"] / 2, ln["width"], ln["dot_len"]
        else:
            x, y, w_, h_ = t - ln["dot_len"] / 2, ln["centre"] - ln["width"] / 2, ln["dot_len"], ln["width"]
        r = min(w_, h_) * 0.42
        dots.append(f'<rect x="{x:.2f}" y="{y:.2f}" width="{w_:.2f}" height="{h_:.2f}" rx="{r:.2f}"/>')
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" preserveAspectRatio="none" width="100%" height="100%">
  <rect width="{W}" height="{H}" fill="{hexc(BG)}"/>
  <defs><clipPath id="cells"><rect x="0" y="0" width="{GXL:.3f}" height="{GYT:.3f}"/><rect x="{GXR:.3f}" y="0" width="{W - GXR:.3f}" height="{GYT:.3f}"/><rect x="0" y="{GYB:.3f}" width="{GXL:.3f}" height="{H - GYB:.3f}"/><rect x="{GXR:.3f}" y="{GYB:.3f}" width="{W - GXR:.3f}" height="{H - GYB:.3f}"/></clipPath></defs>
  <g clip-path="url(#cells)"><g transform="scale(1 {KSTR:.5f})" fill="none" stroke="{hexc(ARC)}" stroke-width="{WW:.3f}">{''.join(f'<circle cx="{cx:.3f}" cy="{cy / KSTR:.3f}" r="{RR:.3f}"/>' for cx, cy in rings["centres"])}</g></g>
  <path fill="{hexc(FG)}" fill-rule="evenodd" d="{' '.join(c['d'] for c in glyph)}"/>
  <g fill="{hexc(DOT)}">{''.join(dots)}</g>
</svg>'''
css_w, css_h = render.css_size_for(W, H)
html = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>studio anokhi - mark (orange)</title>
<!-- High-resolution recreation of website/public/work/studio-anokhi/mark-orange.jpg ({W}x{H}).
     Every shape and colour is measured from that source (tools/build_mark_orange.py, mark-orange.params.json);
     nothing is redesigned. The SVG viewBox is the source frame. -->
<style>html,body{{margin:0;padding:0;background:{hexc(BG)}}} .art{{width:{css_w}px;height:{css_h}px;display:block}}</style>
</head><body><div class="art">{svg}</div></body></html>'''
hp = os.path.join(OUT_DIR, "mark-orange.html")
open(hp, "w", encoding="utf-8").write(html)
out = os.path.join(OUT_DIR, "mark-orange.png")
print("rendered", render.render(hp, out, css_w, css_h, 3), "css", css_w, css_h)
