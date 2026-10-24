"""Repair Gemini's packaging-box output so it shows nothing the source does not.

Gemini drew the small mountain beside NIVRITTI as a single rocky peak and invented legible gibberish for fine print
that is unreadable in the source. This script, working on the output already aligned + colour-matched to the source:
  1. returns the fine-print areas to the source's own (unreadable) pixels, enlarged and feathered;
  2. erases Gemini's mountain to the box paper and composites the REAL NIVRITTI mark (the averaged logo artwork from
     nivritti/logo-navy/orange) with the similarity transform fitted to the source's blurry mark (angle, scale, centre).

    python fix_packaging.py <aligned.png> <out.png>
"""
from __future__ import annotations

import json
import math
import os
import sys

import numpy as np
from matplotlib.path import Path as MPath
from PIL import Image
from scipy import ndimage

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(ROOT, "website", "public", "work", "nivritti", "packaging-box.jpg")
LOGO = os.path.join(ROOT, "research", "images_hq", "html", "nivritti")

# fine print to return to the source (polygons in source px)
FINE_PRINT = [
    [(188, 104), (206, 98), (258, 160), (252, 180), (232, 182)],           # lines right of NIVRITTI on the cream box
    [(0, 222), (40, 222), (52, 288), (0, 290)],                            # invented words on the left box (above "ML / 35")
    [(118, 255), (163, 248), (166, 300), (122, 308)],                      # vertical fine print on the cream box's end
]
MARK_POLY = [(143, 145), (172, 141), (186, 168), (196, 192), (150, 196), (141, 175)]   # Gemini's rocky peak (no letters)
MARK_FIT = dict(angle_deg=236.15, scale=0.04114, cx=162.43, cy=172.06)                 # fitted to the source's blurry mark


def poly_mask(poly, W, H, sx, sy):
    yy, xx = np.mgrid[0:H, 0:W]
    pts = np.c_[(xx.ravel() + 0.5) / sx, (yy.ravel() + 0.5) / sy]
    return MPath(poly).contains_points(pts).reshape(H, W)


def mountain_alpha():
    P = json.load(open(os.path.join(LOGO, "logos.params.json")))
    MX0, MY0, MX1, MY1 = P["artwork_box"]
    a = np.asarray(Image.open(os.path.join(LOGO, "logo-navy.artwork.png")))[..., 3].astype(float) / 255
    K = a.shape[1] / (MX1 - MX0)
    mt = a[:int((196 - MY0) * K)]
    ys, xs = np.where(mt > 0.1)
    return mt[ys.min():ys.max() + 1, xs.min():xs.max() + 1]


def main():
    aligned, out = sys.argv[1], sys.argv[2]
    base = np.asarray(Image.open(aligned).convert("RGB")).astype(float)
    H, W = base.shape[:2]
    src = Image.open(SRC).convert("RGB")
    sx, sy = W / src.width, H / src.height
    up = np.asarray(src.resize((W, H), Image.BICUBIC)).astype(float)
    res = base.copy()

    # 1. fine print -> source pixels (feathered)
    for poly in FINE_PRINT:
        m = ndimage.gaussian_filter(poly_mask(poly, W, H, sx, sy).astype(float), 1.2 * sx)[..., None]
        res = m * up + (1 - m) * res

    # 2a. erase Gemini's mark: paper field from non-ink pixels around it
    mk = poly_mask(MARK_POLY, W, H, sx, sy)
    # never touch the NIVRITTI letters: keep >6 px (source) from the text's centre line (163,133)->(210,188)
    yy0, xx0 = np.mgrid[0:H, 0:W]
    Xs, Ys = (xx0 + 0.5) / sx, (yy0 + 0.5) / sy
    p0, p1 = np.array([163.0, 133.0]), np.array([210.0, 188.0])
    dv = (p1 - p0) / np.linalg.norm(p1 - p0)
    dist = np.abs((Xs - p0[0]) * dv[1] - (Ys - p0[1]) * dv[0])
    mk &= dist > 6.0
    lum = res.mean(2)
    ring = ndimage.binary_dilation(mk, iterations=int(4 * sx)) & ~mk
    paper_lum = np.median(lum[ring])
    valid = (~mk) & (lum > paper_lum - 18)
    v = valid.astype(float)
    fill = res.copy()
    todo = mk.copy()
    for sig in (2, 4, 8, 16, 32):
        den = ndimage.gaussian_filter(v, sig)
        ok = todo & (den > 0.05)
        for ch in range(3):
            num = ndimage.gaussian_filter(res[..., ch] * v, sig)
            fill[..., ch] = np.where(ok, num / np.maximum(den, 1e-6), fill[..., ch])
        todo &= ~ok
    hf = res - ndimage.gaussian_filter(res, (2, 2, 0))
    sd = hf[ring & valid].std(0)
    noise = ndimage.gaussian_filter(np.random.default_rng(1).standard_normal(res.shape), (0.7, 0.7, 0)) * (sd / 0.5)
    soft = ndimage.gaussian_filter(mk.astype(float), 1.0 * sx)[..., None]
    res = soft * (fill + noise) + (1 - soft) * res

    # 2b. composite the real NIVRITTI mark in the box's ink colour
    mt = mountain_alpha()
    mh, mw = mt.shape
    th, s, cx, cy = math.radians(MARK_FIT["angle_deg"]), MARK_FIT["scale"], MARK_FIT["cx"], MARK_FIT["cy"]
    pre = max(0.0, 0.5 / (s * sx) - 0.5)                      # anti-alias before sampling at output scale
    mt_s = ndimage.gaussian_filter(mt, pre) if pre > 0 else mt
    yy, xx = np.mgrid[0:H, 0:W]
    X, Y = (xx + 0.5) / sx, (yy + 0.5) / sy
    c, si = math.cos(th), math.sin(th)
    dx, dy = X - cx, Y - cy
    u = (c * dx + si * dy) / s + mw / 2
    v_ = (-si * dx + c * dy) / s + mh / 2
    alpha = ndimage.map_coordinates(mt_s, [v_, u], order=1, cval=0.0)
    alpha = np.clip(alpha * 0.85, 0, 1)[..., None]           # the source mark is light and sketchy
    # ink: the darkest pixels of the NIVRITTI letters next to the mark
    band = poly_mask([(160, 128), (172, 126), (214, 186), (204, 192)], W, H, sx, sy)
    lt = base[band].reshape(-1, 3)
    ink = np.median(lt[np.argsort(lt.mean(1))[: max(20, len(lt) // 12)]], axis=0)
    res = alpha * ink + (1 - alpha) * res

    Image.fromarray(np.clip(res, 0, 255).astype(np.uint8)).save(out)
    print(json.dumps({"ink": ink.round().tolist(), "paper_lum": round(float(paper_lum), 1), "mark_pixels": int((alpha[..., 0] > 0.3).sum())}))


if __name__ == "__main__":
    main()
