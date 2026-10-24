"""Fit straight dotted/dashed guide lines in a soft alpha map, and fill the pixels under them.

A guide = periodic boxes (dash length L, pitch P, phase) of width w across the line, blurred by a Gaussian (sigma),
with amplitude amp (its colour as a fraction of the way from ground to artwork colour). fit_line2d() fits all of
these jointly on a clean stretch of the line. fill_under() treats pixels covered by the fitted dashes as missing
and interpolates them along the guide from the gaps between dashes, so artwork touching a guide can be traced as
it looks between the dashes.
"""
from __future__ import annotations

from math import sqrt

import numpy as np
from scipy import optimize
from scipy.special import erf


def blurred_box(x, c, w, s):
    s = max(s, 0.25)
    return 0.5 * (erf((x - c + w / 2) / (sqrt(2) * s)) - erf((x - c - w / 2) / (sqrt(2) * s)))


def _period_phase(prof, P0):
    x = np.arange(len(prof)) + 0.5
    p = prof - prof.mean()
    best = None
    for PP in np.linspace(P0 * 0.8, P0 * 1.2, 161):
        c = (p * np.cos(2 * np.pi * x / PP)).sum()
        s = (p * np.sin(2 * np.pi * x / PP)).sum()
        if best is None or np.hypot(c, s) > best[0]:
            best = (np.hypot(c, s), PP, np.arctan2(s, c))
    _, P, ang = best
    return P, (ang / (2 * np.pi) * P) % P


def fit_line2d(M: np.ndarray, orient: str, c0: float, P0: float, seg, half: int = 3,
               amp: float | None = None, sigma: float | None = None, width: float | None = None) -> dict:
    segs = [seg] if isinstance(seg[0], (int, np.integer)) else list(seg)
    subs, alongs, crosses = [], [], []
    for lo, hi in segs:
        if orient == "v":
            x0, x1 = int(round(c0)) - half, int(round(c0)) + half + 1
            sub = M[lo:hi, x0:x1]
            X, Y = np.meshgrid(np.arange(x0, x1) + 0.5, np.arange(lo, hi) + 0.5)
            along, cross = Y, X
        else:
            y0, y1 = int(round(c0)) - half, int(round(c0)) + half + 1
            sub = M[y0:y1, lo:hi]
            X, Y = np.meshgrid(np.arange(lo, hi) + 0.5, np.arange(y0, y1) + 0.5)
            along, cross = X, Y
        subs.append(sub.ravel()); alongs.append(along.ravel()); crosses.append(cross.ravel())
    sub, along, cross = np.concatenate(subs), np.concatenate(alongs), np.concatenate(crosses)
    # period/phase from a cosine fit on the along-line coordinate (all segments together)
    order = np.argsort(along)
    pts, vals = along[order], sub[order]
    best = None
    v0 = vals - vals.mean()
    for PP in np.linspace(P0 * 0.85, P0 * 1.15, 241):
        c = (v0 * np.cos(2 * np.pi * pts / PP)).sum()
        s_ = (v0 * np.sin(2 * np.pi * pts / PP)).sum()
        if best is None or np.hypot(c, s_) > best[0]:
            best = (np.hypot(c, s_), PP, np.arctan2(s_, c))
    _, P_, ang = best
    ph_ = (ang / (2 * np.pi) * P_) % P_
    lo, hi = segs[0][0], segs[-1][1]

    def unpack(p):
        c, w, P, ph, L = p[:5]
        if width is not None:
            w = width
        a = amp if amp is not None else p[5]
        s = sigma if sigma is not None else p[-1]
        return c, w, P, ph, L, a, s

    def model(p):
        c, w, P, ph, L, a, s = unpack(p)
        u = ((along - ph) / P + 0.5) % 1.0 - 0.5
        return a * blurred_box(cross, c, w, s) * blurred_box(u * P, 0.0, L, s)

    def cost(p):
        c, w, P, ph, L, a, s = unpack(p)
        if not (0.5 < w < 5 and 0.6 < L < P * 0.97 and 0.3 < s < 1.6 and 0.02 < a < 1.2):
            return 1e9
        return ((model(p) - sub) ** 2).sum()

    best = None
    for L0 in (0.35 * P_, 0.55 * P_, 0.75 * P_):
        p0 = [c0, 1.6, P_, ph_, L0]
        if amp is None:
            p0.append(max(0.05, float(sub.max()) * 1.1))
        if sigma is None:
            p0.append(0.6)
        r = optimize.minimize(cost, p0, method="Nelder-Mead", options={"maxiter": 12000, "xatol": 1e-4, "fatol": 1e-9})
        if best is None or r.fun < best.fun:
            best = r
    c, w, P, ph, L, a, s = unpack(best.x)
    return dict(orient=orient, centre=float(c), width=float(w), pitch=float(P), phase=float(ph % P), dash=float(L),
                amp=float(a), sigma=float(s), segs=[list(map(int, g)) for g in segs], rss=float(best.fun))


def dash_centres(ln: dict, total: int) -> list[float]:
    t = ln["phase"] - ln["pitch"] * np.ceil(ln["phase"] / ln["pitch"])
    out = []
    while t < total + ln["pitch"]:
        out.append(float(t))
        t += ln["pitch"]
    return out


def coverage(ln: dict, H: int, W: int) -> np.ndarray:
    yy, xx = np.mgrid[0:H, 0:W] + 0.5
    D = np.zeros((H, W))
    s = ln["sigma"]
    total = H if ln["orient"] == "v" else W
    for t in dash_centres(ln, total):
        if ln["orient"] == "v":
            D = np.maximum(D, blurred_box(xx, ln["centre"], ln["width"], s) * blurred_box(yy, t, ln["dash"], s))
        else:
            D = np.maximum(D, blurred_box(xx, t, ln["dash"], s) * blurred_box(yy, ln["centre"], ln["width"], s))
    return D


def fill_under(F: np.ndarray, lines: list[dict], thr: float = 0.06) -> np.ndarray:
    F = F.copy()
    H, W = F.shape
    for ln in lines:
        miss = coverage(ln, H, W) > thr
        if ln["orient"] == "h":
            for r in np.where(miss.any(1))[0]:
                m = miss[r]
                if not m.all():
                    F[r, m] = np.interp(np.where(m)[0], np.where(~m)[0], F[r, ~m])
        else:
            for c in np.where(miss.any(0))[0]:
                m = miss[:, c]
                if not m.all():
                    F[m, c] = np.interp(np.where(m)[0], np.where(~m)[0], F[~m, c])
    return F


def svg_dashes(ln: dict, H: int, W: int, rx_frac: float = 0.3) -> str:
    out = []
    total = H if ln["orient"] == "v" else W
    for t in dash_centres(ln, total):
        if ln["orient"] == "v":
            x, y, w_, h_ = ln["centre"] - ln["width"] / 2, t - ln["dash"] / 2, ln["width"], ln["dash"]
        else:
            x, y, w_, h_ = t - ln["dash"] / 2, ln["centre"] - ln["width"] / 2, ln["dash"], ln["width"]
        out.append('<rect x="%.2f" y="%.2f" width="%.2f" height="%.2f" rx="%.2f"/>' % (x, y, w_, h_, min(w_, h_) * rx_frac))
    return "".join(out)
