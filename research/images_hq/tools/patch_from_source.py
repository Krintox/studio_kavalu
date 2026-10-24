"""Replace a small region of an aligned output with the (enlarged) source pixels, feathered.

Used where a generator made something legible that is illegible in the source (e.g. tiny contact lines on a business
card): rather than keep invented text, the region goes back to exactly what the source shows (soft, unreadable).

    python patch_from_source.py <rel> <aligned.png> <out.png> band <x0> <y0> <angle_deg> <t0> <t1> <d0> <d1> [feather_px]
      band: points p = (x0, y0) + t*(cos a, sin a) + d*(-sin a, cos a), t in [t0, t1], d in [d0, d1] (source px)
"""
from __future__ import annotations

import json
import math
import os
import sys

import numpy as np
from PIL import Image
from scipy import ndimage

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
SRC_DIR = os.path.join(ROOT, "website", "public", "work")


def main():
    rel, aligned, out, kind = sys.argv[1:5]
    src = Image.open(os.path.join(SRC_DIR, rel.replace("/", os.sep) + ".jpg")).convert("RGB")
    cand = Image.open(aligned).convert("RGB")
    W, H = cand.size
    sx, sy = W / src.width, H / src.height
    up = np.asarray(src.resize((W, H), Image.BICUBIC)).astype(float)
    c = np.asarray(cand).astype(float)
    yy, xx = np.mgrid[0:H, 0:W]
    X, Y = (xx + 0.5) / sx, (yy + 0.5) / sy          # source coordinates of each output pixel
    if kind != "band":
        raise SystemExit("only 'band' is implemented")
    x0, y0, ang, t0, t1, d0, d1 = [float(v) for v in sys.argv[5:12]]
    feather = float(sys.argv[12]) if len(sys.argv) > 12 else 1.0
    a = math.radians(ang)
    t = (X - x0) * math.cos(a) + (Y - y0) * math.sin(a)
    d = -(X - x0) * math.sin(a) + (Y - y0) * math.cos(a)
    m = ((t >= t0) & (t <= t1) & (d >= d0) & (d <= d1)).astype(float)
    m = ndimage.gaussian_filter(m, feather * sx)[..., None]
    res = m * up + (1 - m) * c
    Image.fromarray(np.clip(res, 0, 255).astype(np.uint8)).save(out)
    print(json.dumps({"patched_pixels": int((m[..., 0] > 0.5).sum()), "out": out}))


if __name__ == "__main__":
    main()
