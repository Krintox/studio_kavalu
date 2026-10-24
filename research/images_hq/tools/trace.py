"""Vectorise flat-colour shapes from a small raster source, for the HTML/SVG recreations.

The source is turned into a soft foreground map (projection of each pixel onto the line between a background
and a foreground colour), enlarged smoothly (bicubic, factor k), lightly blurred, thresholded at 0.5 and traced
with potrace. Edges therefore land with sub-pixel accuracy, and the SVG path comes back in SOURCE pixel units,
so it drops straight into an <svg viewBox="0 0 W H"> that matches the source frame.
"""
from __future__ import annotations

import numpy as np
import potrace
from PIL import Image
from scipy import ndimage


def fg_map(rgb: np.ndarray, bg, fg) -> np.ndarray:
    bg = np.asarray(bg, dtype=np.float64)
    fg = np.asarray(fg, dtype=np.float64)
    d = fg - bg
    t = ((rgb.astype(np.float64) - bg) @ d) / float(d @ d)
    return np.clip(t, 0.0, 1.0)


def upsample(m: np.ndarray, k: int) -> np.ndarray:
    im = Image.fromarray(m.astype(np.float32), mode="F")
    return np.asarray(im.resize((m.shape[1] * k, m.shape[0] * k), Image.BICUBIC), dtype=np.float64)


def binary(m: np.ndarray, k: int = 8, blur: float = 0.6, thresh: float = 0.5) -> np.ndarray:
    big = upsample(m, k)
    if blur > 0:
        big = ndimage.gaussian_filter(big, blur * k)
    return big > thresh


def _fmt(v: float) -> str:
    s = f"{v:.2f}".rstrip("0").rstrip(".")
    return s if s not in ("-0", "") else "0"


def trace_bitmap(bits: np.ndarray, k: int, ox: float = 0.0, oy: float = 0.0, turdsize: int | None = None,
                 alphamax: float = 1.0, opttolerance: float = 0.2) -> list[dict]:
    """Return a list of {d, area, bbox} per top-level shape (holes included in d), in source units."""
    # potracer inverts its input (it traces "dark" = False pixels), so hand it the inverted foreground
    bm = potrace.Bitmap(~bits.astype(bool))
    path = bm.trace(turdsize=turdsize if turdsize is not None else 2 * k * k, alphamax=alphamax,
                    opticurve=True, opttolerance=opttolerance)
    # potracer flips nothing: coordinates are (x=col, y=row) in bitmap pixels
    def P(pt):
        return _fmt(pt.x / k + ox) + " " + _fmt(pt.y / k + oy)

    curves = []
    for curve in path.curves:
        parts = ["M" + P(curve.start_point)]
        xs, ys = [curve.start_point.x], [curve.start_point.y]
        for seg in curve.segments:
            if seg.is_corner:
                parts.append("L" + P(seg.c) + "L" + P(seg.end_point))
                xs += [seg.c.x, seg.end_point.x]
                ys += [seg.c.y, seg.end_point.y]
            else:
                parts.append("C" + P(seg.c1) + " " + P(seg.c2) + " " + P(seg.end_point))
                xs += [seg.end_point.x]
                ys += [seg.end_point.y]
        parts.append("Z")
        bbox = [min(xs) / k + ox, min(ys) / k + oy, max(xs) / k + ox, max(ys) / k + oy]
        area = (bbox[2] - bbox[0]) * (bbox[3] - bbox[1])
        curves.append({"d": "".join(parts), "bbox": [round(v, 2) for v in bbox], "area": round(area, 2)})
    return curves


def trace_region(img: Image.Image, bg, fg, box=None, k: int = 8, blur: float = 0.6, thresh: float = 0.5,
                 mask_fn=None, **kw) -> list[dict]:
    rgb = np.asarray(img.convert("RGB"), dtype=np.float64)
    ox = oy = 0
    if box:
        x0, y0, x1, y1 = box
        rgb = rgb[y0:y1, x0:x1]
        ox, oy = x0, y0
    m = fg_map(rgb, bg, fg)
    if mask_fn is not None:
        m = mask_fn(m)
    bits = binary(m, k=k, blur=blur, thresh=thresh)
    return trace_bitmap(bits, k, ox, oy, **kw)


def dominant_colours(img: Image.Image, n: int = 2, iters: int = 20, box=None) -> list[list[int]]:
    """Tiny k-means on RGB; returns cluster centres sorted by size (largest first)."""
    a = np.asarray(img.convert("RGB"), dtype=np.float64)
    if box:
        x0, y0, x1, y1 = box
        a = a[y0:y1, x0:x1]
    X = a.reshape(-1, 3)
    rng = np.random.default_rng(0)
    C = X[rng.choice(len(X), n, replace=False)]
    for _ in range(iters):
        lab = ((X[:, None, :] - C[None]) ** 2).sum(-1).argmin(1)
        C = np.array([X[lab == i].mean(0) if (lab == i).any() else C[i] for i in range(n)])
    counts = np.bincount(lab, minlength=n)
    order = np.argsort(-counts)
    return [[int(round(v)) for v in C[i]] for i in order]


def adaptive_binary(m: np.ndarray, k: int = 8, blur: float = 0.45, rel: float = 0.75, lo: float = 0.12,
                    hi: float = 0.5, win: int = 5, min_peak: float = 0.0) -> np.ndarray:
    """Threshold each pixel at clip(rel * local max, lo, hi): thick strokes keep their 0.5 edges while thin, blurred
    hairlines (peak alpha < 1) are kept at a width close to their true width instead of vanishing."""
    lm = ndimage.maximum_filter(m, size=win)
    t = np.clip(rel * lm, lo, hi)
    big = upsample(m, k)
    tb = upsample(t, k)
    if blur > 0:
        big = ndimage.gaussian_filter(big, blur * k)
    out = big > tb
    if min_peak > 0:
        out &= upsample(lm, k) >= min_peak
    return out
