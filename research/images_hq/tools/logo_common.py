"""Shared measurements for the two NIVRITTI logo cards (nivritti/logo-navy.jpg 288x346, nivritti/logo-orange.jpg 290x346).

Both cards carry the same artwork (linocut mountain + NIVRITTI wordmark) and the same dashed guides, so the
artwork's alpha (0 = ground, 1 = cream) is measured on both, the orange card is registered onto the navy one
(scale + offset per axis, maximising correlation of the alphas), and the two alphas are averaged in the navy frame.
That halves the JPEG noise before tracing. `to_orange` maps navy-frame coordinates into the orange frame.
"""
from __future__ import annotations

import json
import os

import numpy as np
from PIL import Image
from scipy import ndimage, optimize

import trace as T

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
SRC = {k: os.path.join(ROOT, "website", "public", "work", "nivritti", f"logo-{k}.jpg") for k in ("navy", "orange")}
CACHE = os.path.join(ROOT, "research", "images_hq", "html", "nivritti", "logo_common.json")


def colours(A: np.ndarray):
    lum = A.mean(2)
    bg = np.median(A[ndimage.binary_erosion(lum < np.percentile(lum, 60), np.ones((5, 5)))], axis=0)
    fg = np.median(A[lum > np.percentile(lum, 99.3)], axis=0)
    return bg, fg


def load(k: str):
    A = np.asarray(Image.open(SRC[k]).convert("RGB")).astype(float)
    bg, fg = colours(A)
    return A, bg, fg, T.fg_map(A, bg, fg)


def register_alpha(Mn: np.ndarray, Mo: np.ndarray, box=(30, 85, 262, 260)) -> np.ndarray:
    """Find (sx, sy, tx, ty) with orange(x', y') = navy(x, y) for x' = sx*x + tx, y' = sy*y + ty."""
    x0, y0, x1, y1 = box
    yy, xx = np.mgrid[y0:y1, x0:x1].astype(float)
    tgt = ndimage.gaussian_filter(Mn, 0.7)[y0:y1, x0:x1]
    G = ndimage.gaussian_filter(Mo, 0.7)

    def cost(p):
        sx, sy, tx, ty = p
        v = ndimage.map_coordinates(G, [sy * (yy + 0.5) + ty - 0.5, sx * (xx + 0.5) + tx - 0.5], order=1)
        a = tgt - tgt.mean()
        b = v - v.mean()
        return -(a * b).sum() / np.sqrt((a * a).sum() * (b * b).sum())

    best = None
    for tx0 in (-2, 0, 2):
        for ty0 in (-2, 0, 2):
            r = optimize.minimize(cost, [Mo.shape[1] / Mn.shape[1], 1.0, tx0, ty0], method="Nelder-Mead",
                                  options={"maxiter": 4000, "xatol": 1e-4, "fatol": 1e-8})
            if best is None or r.fun < best.fun:
                best = r
    return best.x, -best.fun


def averaged():
    An, bgn, fgn, Mn = load("navy")
    Ao, bgo, fgo, Mo = load("orange")
    p, score = register_alpha(Mn, Mo)
    sx, sy, tx, ty = p
    H, W = Mn.shape
    yy, xx = np.mgrid[0:H, 0:W].astype(float)
    Mo_in_n = ndimage.map_coordinates(Mo, [sy * (yy + 0.5) + ty - 0.5, sx * (xx + 0.5) + tx - 0.5], order=1, mode="nearest")
    avg = (Mn + Mo_in_n) / 2
    info = {"to_orange": [float(v) for v in p], "ncc": float(score), "navy": {"bg": bgn.tolist(), "fg": fgn.tolist()},
            "orange": {"bg": bgo.tolist(), "fg": fgo.tolist()}}
    os.makedirs(os.path.dirname(CACHE), exist_ok=True)
    json.dump(info, open(CACHE, "w"), indent=1)
    return avg, Mn, Mo, Mo_in_n, info


if __name__ == "__main__":
    avg, Mn, Mo, Moi, info = averaged()
    print(json.dumps(info, indent=1))
    d = np.abs(Mn - Moi)[85:260, 30:262]
    print("mean |navy - orange(registered)| in artwork box:", round(float(d.mean()), 4))
