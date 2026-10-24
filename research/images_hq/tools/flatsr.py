"""Layered super-resolution for flat-colour graphics, derived only from the source pixels.

unmix():   each pixel = ground + sum_i a_i * (colour_i - ground), solved by least squares, clipped to a valid mix.
layered(): converts the mix into stacked layers (bottom -> top), un-premultiplying lower layers where an upper
           layer covers them (pixels fully covered get the lower layer's neighbourhood value, which is hidden anyway).
soft():    enlarges one alpha 8x (bicubic), applies a mild unsharp mask and a smoothstep contrast curve. Optional
           local-peak normalisation keeps thin strokes (blurred to a lower peak) as solid as thick ones.
png_uri(): RGBA PNG (layer colour + alpha) as a data URI for an <image> in the recreation's SVG.
Nothing is redrawn or invented: shapes come from the source alpha, so they stay exactly where the source has them.
"""
from __future__ import annotations

import base64
import io

import numpy as np
from PIL import Image
from scipy import ndimage

import trace as T


def unmix(A: np.ndarray, ground, colours) -> np.ndarray:
    g = np.asarray(ground, float)
    D = np.stack([np.asarray(c, float) - g for c in colours], 1)          # 3 x n
    P = (A.reshape(-1, 3) - g) @ np.linalg.pinv(D).T                        # N x n
    P = np.clip(P, 0, 1)
    s = P.sum(1, keepdims=True)
    P = np.where(s > 1, P / np.maximum(s, 1e-9), P)
    return P.reshape(A.shape[:2] + (len(colours),))


def layered(alphas: np.ndarray) -> np.ndarray:
    """alphas[..., i] from unmix (i = 0 bottom ... n-1 top) -> per-layer coverage for source-over stacking."""
    out = alphas.copy()
    n = alphas.shape[-1]
    for i in range(n - 1):
        above = alphas[..., i + 1:].sum(-1)
        free = 1 - above
        cov = np.where(free > 0.15, alphas[..., i] / np.maximum(free, 1e-6), np.nan)
        hidden = np.isnan(cov)
        if hidden.any():
            filled = ndimage.maximum_filter(np.nan_to_num(cov, nan=0.0), size=5)
            cov = np.where(hidden, filled, cov)
        out[..., i] = np.clip(cov, 0, 1)
    return out


def soft(alpha: np.ndarray, k: int = 8, unsharp: float = 0.8, radius: float = 0.8, lo: float = 0.08, hi: float = 0.72,
         normalise: bool = False, norm_floor: float = 0.45, win: int = 5) -> np.ndarray:
    up = T.upsample(alpha, k)
    if unsharp > 0:
        up = up + unsharp * (up - ndimage.gaussian_filter(up, radius * k))
    if normalise:
        lm = T.upsample(ndimage.maximum_filter(alpha, size=win), k)
        up = up / np.clip(lm, norm_floor, 1.0)
    t = np.clip((up - lo) / (hi - lo), 0, 1)
    return t * t * (3 - 2 * t)


def png_uri(alpha8: np.ndarray, colour, save_path: str | None = None) -> str:
    rgba = np.zeros(alpha8.shape + (4,), np.uint8)
    rgba[..., :3] = np.round(np.clip(colour, 0, 255)).astype(np.uint8)
    rgba[..., 3] = np.round(np.clip(alpha8, 0, 1) * 255).astype(np.uint8)
    im = Image.fromarray(rgba, "RGBA")
    if save_path:
        im.save(save_path, optimize=True)
    buf = io.BytesIO()
    im.save(buf, "PNG", optimize=True)
    return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()


def hexc(c) -> str:
    return "#%02X%02X%02X" % tuple(int(round(min(255, max(0, v)))) for v in c)
