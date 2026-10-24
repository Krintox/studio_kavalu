"""Remove Gemini's visible sparkle watermark (a small light four-point star near the bottom-right corner).

    python dewatermark.py <in.png> <out.png> [--debug mask.png]

The star is not in the source images, so leaving it would add content. It is found as a compact bright blob in the
bottom-right corner region (difference against a median-filtered copy), dilated, and filled from the surrounding
pixels (multi-scale normalised convolution) plus fine grain matched to the surrounding texture, so the patch does not
look smoothed. Only the star's few hundred pixels change.
"""
from __future__ import annotations

import json
import sys

import numpy as np
from PIL import Image
from scipy import ndimage


def astroid(h, w, cy, cx, r):
    yy, xx = np.mgrid[0:h, 0:w]
    dy, dx = np.abs(yy + 0.5 - cy) / r, np.abs(xx + 0.5 - cx) / r
    return (dx ** (2 / 3) + dy ** (2 / 3)) <= 1.0


def find_star(a: np.ndarray):
    """Gemini's sparkle is a four-point astroid star (~95 px across on ~1.8-1.9k px images) centred ~112.5 px from the
    right and bottom edges. Fit its size and position near there by template contrast against the local background."""
    H, W = a.shape[:2]
    lum = a.astype(float).mean(2)
    best = None
    # the sparkle has a fixed pixel size/margin on the images seen so far; also try a width-scaled hypothesis
    hyps = sorted({1.0, round(W / 1800.0, 3)})
    for k in hyps:
      for r in np.linspace(38, 60, 12) * k:
        for oy in np.arange(-14, 15, 2) * k:
            for ox in np.arange(-14, 15, 2) * k:
                cy, cx = H - 112.5 * k + oy, W - 112.5 * k + ox
                y0, y1 = int(cy - 2 * r), int(cy + 2 * r) + 1
                x0, x1 = int(cx - 2 * r), int(cx + 2 * r) + 1
                if y0 < 0 or x0 < 0 or y1 > H or x1 > W:
                    continue
                sub = lum[y0:y1, x0:x1]
                inner = astroid(y1 - y0, x1 - x0, cy - y0, cx - x0, r)
                outer = astroid(y1 - y0, x1 - x0, cy - y0, cx - x0, r * 1.6) & ~astroid(y1 - y0, x1 - x0, cy - y0, cx - x0, r * 1.15)
                c = sub[inner].mean() - sub[outer].mean()
                # penalise variance inside (the star is flat) so textured bright areas do not win
                score = c - 0.5 * sub[inner].std()
                if best is None or score > best[0]:
                    best = (score, c, cy, cx, r)
    if best is None or best[1] < 5:
        return None
    _, c, cy, cx, r = best
    return astroid(H, W, cy, cx, r * 1.08)


def clone_fill(a: np.ndarray, m: np.ndarray):
    """Exemplar fill: copy the patch at the offset whose surroundings best match the ring around the mask."""
    out = a.astype(float)
    ys, xs = np.where(m)
    y0, y1, x0, x1 = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
    size = max(y1 - y0, x1 - x0)
    ring = ndimage.binary_dilation(m, iterations=10) & ~m
    ry, rx = np.where(ring)
    H, W = m.shape
    best = None
    for dy in range(-int(2.2 * size), int(0.8 * size) + 1, max(2, size // 8)):
        for dx in range(-int(2.2 * size), int(0.8 * size) + 1, max(2, size // 8)):
            if abs(dx) < 1.1 * size and abs(dy) < 1.1 * size:
                continue                                         # the shifted patch must not overlap the star
            sy, sx = ry + dy, rx + dx
            if sy.min() < 0 or sx.min() < 0 or sy.max() >= H or sx.max() >= W:
                continue
            if (ys + dy).min() < 0 or (xs + dx).min() < 0 or (ys + dy).max() >= H or (xs + dx).max() >= W:
                continue
            if m[ys + dy, xs + dx].any():
                continue
            ssd = ((out[sy, sx] - out[ry, rx]) ** 2).mean()
            if best is None or ssd < best[0]:
                best = (ssd, dy, dx)
    if best is None:
        return None
    _, dy, dx = best
    res = out.copy()
    res[ys, xs] = out[ys + dy, xs + dx]
    # match the mean colour of the ring (removes a small brightness step) and feather
    corr = out[ry, rx].mean(0) - out[ry + dy, rx + dx].mean(0)
    res[ys, xs] += corr
    return res, (int(dy), int(dx))


def fill(a: np.ndarray, mask: np.ndarray, seed: int = 0) -> np.ndarray:
    m = ndimage.binary_dilation(mask, iterations=max(3, int(min(a.shape[:2]) * 0.004)))
    cf = clone_fill(a, m)
    if cf is not None:
        res, off = cf
        soft = ndimage.gaussian_filter(m.astype(float), 2.0)[..., None]
        res = soft * res + (1 - soft) * a.astype(float)
        return np.clip(res, 0, 255).astype(np.uint8), m
    out = a.astype(float).copy()
    valid = (~m).astype(float)
    filled = np.zeros_like(out)
    todo = m.copy()
    for sig in (2, 4, 8, 16, 32):
        den = ndimage.gaussian_filter(valid, sig)
        ok = todo & (den > 0.05)
        for ch in range(3):
            num = ndimage.gaussian_filter(out[..., ch] * valid, sig)
            filled[..., ch] = np.where(ok, num / np.maximum(den, 1e-6), filled[..., ch])
        todo &= ~ok
    # grain: match the high-frequency std of a ring around the patch
    ring = ndimage.binary_dilation(m, iterations=12) & ~m
    hf = out - ndimage.gaussian_filter(out, (2, 2, 0))
    sd = hf[ring].std(0) if ring.any() else np.zeros(3)
    rng = np.random.default_rng(seed)
    noise = ndimage.gaussian_filter(rng.standard_normal(out.shape), (0.8, 0.8, 0)) * (sd / 0.45)
    res = out.copy()
    res[m] = filled[m] + noise[m]
    # feather the edge of the patch
    soft = ndimage.gaussian_filter(m.astype(float), 1.5)[..., None]
    res = soft * res + (1 - soft) * out
    return np.clip(res, 0, 255).astype(np.uint8), m


def main():
    src, dst = sys.argv[1], sys.argv[2]
    a = np.asarray(Image.open(src).convert("RGB"))
    mask = find_star(a)
    if mask is None:
        Image.fromarray(a).save(dst)
        print(json.dumps({"watermark": False}))
        return 0
    res, m = fill(a, mask)
    Image.fromarray(res).save(dst)
    ys, xs = np.where(mask)
    info = {"watermark": True, "bbox": [int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max())], "pixels_changed": int(m.sum())}
    if "--debug" in sys.argv:
        dbg = sys.argv[sys.argv.index("--debug") + 1]
        x0, y0, x1, y1 = info["bbox"]
        pad = 40
        crop = lambda im: im[max(0, y0 - pad):y1 + pad, max(0, x0 - pad):x1 + pad]
        Image.fromarray(np.concatenate([crop(a), crop(res)], 1)).resize(
            (2 * (x1 - x0 + 2 * pad) * 3, (y1 - y0 + 2 * pad) * 3), Image.NEAREST).save(dbg)
    print(json.dumps(info))
    return 0


if __name__ == "__main__":
    sys.exit(main())
