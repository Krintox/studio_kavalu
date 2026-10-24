"""Build Studio Kavalu's paper textures (v3).

    python make_textures.py                 # build everything into research/textures_v3/
    python make_textures.py --only cream    # rebuild some textures (comma list of names)
    python make_textures.py --sizes 1024    # one size only

Outputs (each at 1024 and 512 px, as .webp and .png) in research/textures_v3/:
  paper-neutral-light-<n>     greyscale tile for `multiply` on any light colour
  paper-neutral-strong-<n>    the same sheet, slightly stronger
  paper-<colour>-<n>          baked colour paper: cream, writing-paper, powder-blue, plum, oxblood,
                              deep-plum; mean colour on its hex (dE00 < 0.3, PNG and decoded WebP)
  cardstock-overlay-<n>       mid-grey tile for `overlay` on any mid or dark colour
and metrics.json: mean-colour accuracy, strength, seam scores, detail kept by the WebP encoder,
file sizes, and the CSS compensation colours for the neutral tiles.

The paper is built in perceptual lightness (CIE L*) as a sum of periodic components:
  formation   soft cloud-like mottling at three scales (blobs of roughly 120, 40 and 12 px),
              domain-warped so the clouds are not round, with small denser (slightly darker) flocs;
  fibre mat   ~200k very short, faint, randomly oriented fibres: the fine fibrous body of the sheet;
  fibres      ~3,000 short strands and ~280 longer ones, slightly curved, tapered, fading in and out
              along their length (they dip under other fibres), some lighter, some darker;
  tooth       a gentle relief (bumps + fibres) lit from the top left;
  grain       a very fine, band-limited grain.
Light papers use all of it. Dark papers use their own recipe (DARK): quieter formation, almost no
grain, and fibres that are mostly lighter than the sheet, like dyed-through cardstock.

Every component is periodic on the tile, so the tiles repeat with no seam (checked in metrics.json and
by the 3 x 3 previews).
"""
from __future__ import annotations

import argparse
import io
import json
import os
import sys
import time

import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paperlib as pl  # noqa: E402

OUT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

PALETTE = {
    "cream": "#F3F3E7",
    "cream-2": "#ECEADB",
    "cream-3": "#E3E0CD",
    "plum": "#390D26",
    "deep-plum": "#270617",
    "oxblood": "#491C17",
    "powder-blue": "#ABCDD6",
    "writing-paper": "#F8F5E8",
    "bright-paper": "#FBFAF2",
}
PROJECT = {  # spread colour, its ink (website/src/content/projects.ts)
    "rust": ("#9F4A30", "#FAEBCA"),
    "ink-blue": ("#07253D", "#EFE9DA"),
    "magenta": ("#A11F5B", "#F8E9EF"),
    "cocoa": ("#3F1B0E", "#F6E7B6"),
    "vermilion": ("#A32D02", "#FBE3D6"),
}

# ---------------------------------------------------------------------------------------------
# recipes (amplitudes in L* units at strength 1.0; counts are per 1024 x 1024 and scale with area)
# ---------------------------------------------------------------------------------------------

LIGHT = dict(
    m1=dict(sigma=46, hp=400, aniso=1.12, amp=0.44),
    m2=dict(sigma=15, hp=240, aniso=1.12, amp=0.32, warp=7.0),
    m3=dict(sigma=4.6, hp=90, aniso=1.08, amp=0.20, skew=0.12),
    clip=1.6,  # clouds are soft-clipped at 1.6 sigma: no single cloud stands out, so the repeat hides
    mat=dict(count=200_000, length=6.5, spread=0.45, lrange=(2.0, 18.0), bend=0.08, width=0.42,
             mean_abs=0.24, light=0.5, vis=0.6),
    med=dict(count=3_400, length=15.0, spread=0.5, lrange=(5.0, 55.0), bend=0.12, width=0.52,
             mean_abs=1.0, light=0.45, cap=2.8, vis=0.75),
    long=dict(count=300, length=32.0, spread=0.35, lrange=(14.0, 85.0), bend=0.15, width=0.58,
              mean_abs=1.15, light=0.45, cap=3.0, vis=0.8),
    floc_fibres=0.55,  # fibre centres follow the mid-scale formation (flocculation)
    relief=dict(amp=0.26, bump_sigma=6.0, bump=1.0, fibre=0.55, tooth_sigma=1.8, tooth=0.25),
    grain=dict(sigma=0.62, amp=0.14),
    kappa=0.35,  # slight machine-direction (x) bias of the fibres
)

DARK = dict(
    m1=dict(sigma=46, hp=400, aniso=1.12, amp=0.30),
    m2=dict(sigma=15, hp=240, aniso=1.12, amp=0.22, warp=7.0),
    m3=dict(sigma=4.6, hp=90, aniso=1.08, amp=0.12, skew=0.10),
    clip=1.6,
    mat=dict(count=200_000, length=6.5, spread=0.45, lrange=(2.0, 18.0), bend=0.08, width=0.42,
             mean_abs=0.12, light=0.75, vis=0.6),
    med=dict(count=2_600, length=15.0, spread=0.5, lrange=(5.0, 55.0), bend=0.12, width=0.52,
             mean_abs=1.0, light=0.9, cap=3.0, vis=0.75),
    long=dict(count=250, length=32.0, spread=0.35, lrange=(14.0, 85.0), bend=0.15, width=0.58,
              mean_abs=1.3, light=0.92, cap=3.4, vis=0.8),
    floc_fibres=0.55,
    relief=dict(amp=0.16, bump_sigma=6.0, bump=1.0, fibre=0.7, tooth_sigma=1.8, tooth=0.2),
    grain=dict(sigma=0.62, amp=0.05),
    kappa=0.35,
)
RECIPES = {"light": LIGHT, "dark": DARK}

# what gets built. strength scales the whole recipe; weights scale single components.
BAKED = {
    "cream": dict(hex="#F3F3E7", recipe="light", seed=11, strength=1.6, chroma_k=0.02, warm=0.05),
    "writing-paper": dict(hex="#F8F5E8", recipe="light", seed=12, strength=1.6, chroma_k=0.02, warm=0.04,
                          weights=dict(m1=0.8, m2=0.75, m3=0.5, relief=0.6, grain=0.7, med=0.9, long=0.8)),
    "powder-blue": dict(hex="#ABCDD6", recipe="light", seed=13, strength=1.35, chroma_k=0.02, warm=0.0),
    "deep-plum": dict(hex="#270617", recipe="dark", seed=23, strength=1.75, chroma_k=-0.02, warm=0.0),
    "plum": dict(hex="#390D26", recipe="dark", seed=24, strength=1.6, chroma_k=-0.02, warm=0.0),
    "oxblood": dict(hex="#491C17", recipe="dark", seed=25, strength=1.65, chroma_k=-0.02, warm=0.0),
}
# The 512 tiles are meant to be shown at 256 CSS px on phones, where a 512 px period would let the
# largest clouds form a visible grid. They keep the same fibres and grain but calm the big clouds.
SMALL = dict(weights=dict(m1=0.35, m2=0.75, med=1.15, mat=1.1), strength=1.08)


def size_weights(n, weights=None):
    w = dict(weights or {})
    if n < 1024:
        for k, v in SMALL["weights"].items():
            w[k] = w.get(k, 1.0) * v
    return w


def size_strength(n, strength):
    return strength * (SMALL["strength"] if n < 1024 else 1.0)


NEUTRAL = dict(seed=31, ref="#F3F3E7", strengths={"light": 1.2, "strong": 1.75}, knee=(1.2, 1.7))
OVERLAY = dict(seed=41, strength=1.4, gain=10.0)  # tile levels per L* of the dark field; for soft-light (or overlay)
# WebP quality, chosen by measurement (metrics.json "webp_detail"): at q80 the encoder erases the fibre
# mat of these low-contrast sheets (fibre-scale correlation 0.47 on deep plum), so the light papers use
# q95, the dark ones q98 and the higher-contrast cardstock tile q90; every file stays far under 150 KB.
WEBP_Q = {"default": 95, "deep-plum": 98, "plum": 98, "oxblood": 98, "overlay": 90, "neutral": 95}


def _scaled(count, n):
    return int(round(count * (n / 1024) ** 2))


def components(n: int, seed: int, P: dict) -> dict:
    """All periodic components of one sheet, each in L* units at strength 1."""
    rng = np.random.default_rng(seed)
    c = {}
    clip = P.get("clip")

    def calm(f):  # soft-clip a unit field so no cloud is far darker or lighter than the rest
        return pl.normalise(clip * np.tanh(f / clip)) if clip else f

    hp_max = n / 2.4  # nothing larger than ~40 % of the tile: no slow gradient that shows the repeat
    m1 = P["m1"]
    c["m1"] = calm(pl.band_noise(n, rng, m1["sigma"], min(m1["hp"], hp_max), m1["aniso"])) * m1["amp"]
    m2 = P["m2"]
    f2 = pl.band_noise(n, rng, m2["sigma"], min(m2["hp"], hp_max), m2["aniso"])
    wx = pl.band_noise(n, rng, 28) * m2["warp"]
    wy = pl.band_noise(n, rng, 28) * m2["warp"]
    f2 = calm(pl.normalise(pl.warp(f2, wx, wy)))
    c["m2"] = f2 * m2["amp"]
    m3 = P["m3"]
    f3 = pl.band_noise(n, rng, m3["sigma"], m3["hp"], m3["aniso"])
    a = m3["skew"]  # > 0: monotonic negative skew, i.e. small denser (darker) flocs in a calmer sheet
    if a:
        f3 = pl.normalise((1 - np.exp(-a * f3)) / a)
    c["m3"] = f3 * m3["amp"]

    dens = np.exp(P["floc_fibres"] * f2)
    heights = {}
    for key in ("mat", "med", "long"):
        q = P[key]
        cnt = _scaled(q["count"], n)
        strengths = pl.signed_strengths(rng, cnt, q["mean_abs"], q["light"], q.get("cap"))
        alb, hgt = pl.fibres(
            n, rng, cnt, q["length"], q["spread"], q["lrange"], q["bend"], q["width"], strengths,
            vis_mod=q["vis"], angle_kappa=P["kappa"], density=dens,
        )
        c[key] = alb
        heights[key] = hgt

    r = P["relief"]
    bump = pl.band_noise(n, rng, r["bump_sigma"])
    tooth = pl.band_noise(n, rng, r["tooth_sigma"])
    fh = heights["mat"] * 0.6 + heights["med"] + heights["long"]
    fh = fh / (fh.std() + 1e-9)
    h = r["bump"] * bump + r["fibre"] * fh + r["tooth"] * tooth
    c["relief"] = pl.normalise(pl.shade(h)) * r["amp"]
    g = P["grain"]
    c["grain"] = pl.band_noise(n, rng, g["sigma"]) * g["amp"]
    return c


def combine(c: dict, strength=1.0, weights=None) -> np.ndarray:
    w = weights or {}
    return sum(c[k] * w.get(k, 1.0) for k in c) * strength


def field(n, recipe, seed, strength=1.0, weights=None):
    return combine(components(n, seed, RECIPES[recipe]), strength, weights)


# ---------------------------------------------------------------------------------------------
# mapping a field to pixels
# ---------------------------------------------------------------------------------------------


def tpdf(shape, rng):
    return rng.uniform(-0.5, 0.5, shape) + rng.uniform(-0.5, 0.5, shape)


def quantise8(x, rng):
    """Round to 8-bit with a small triangular dither, so slow clouds never band."""
    return np.clip(np.round(x + tpdf(x.shape, rng) * 0.5), 0, 255).astype(np.uint8)


def lab_ramp(levels, L0, a0, b0, chroma_k, warm):
    """Colours for lightness offsets `levels`: L* = L0 + d; chroma x (1 - chroma_k d) (darker is a
    touch richer); a* warms by `warm` per L* darker. Returns float sRGB 0..255."""
    d = np.asarray(levels, float)
    C0, h0 = np.hypot(a0, b0), np.arctan2(b0, a0)
    C = C0 * np.clip(1 - chroma_k * d, 0.5, 1.5)
    lab = np.stack([L0 + d, C * np.cos(h0) - warm * d, C * np.sin(h0)], -1)
    return pl.linear_to_srgb(pl.lab_to_linear(lab)) * 255


class Baked:
    """A colour paper as an index image (lightness steps) plus a colour ramp: the colour is a function
    of one value, so the PNG is an exact palette image and the codec sees no chroma noise."""

    def __init__(self, dL, hex_colour, chroma_k=0.02, warm=0.0, step=0.04, seed=5):
        rng = np.random.default_rng(seed)
        lo, hi = np.percentile(dL, [0.002, 99.998])
        self.step = step
        K = int(np.ceil((hi - lo) / step)) + 1
        if K > 4096:
            raise ValueError("field range too large")
        self.levels = lo + step * np.arange(K)
        self.idx = np.clip(np.round((dL - lo) / step + tpdf(dL.shape, rng) * 0.5), 0, K - 1).astype(np.int32)
        self.hex = hex_colour
        self.chroma_k, self.warm = chroma_k, warm
        self.counts = np.bincount(self.idx.ravel(), minlength=K)
        self.lab0 = pl.srgb8_to_lab(pl.hex_to_rgb8(hex_colour))

    def ramp8(self, lab_base):
        return np.clip(np.round(lab_ramp(self.levels, *lab_base, self.chroma_k, self.warm)), 0, 255)

    def solve(self, target_lab=None, iters=8, mean_fn=None):
        """Find the base Lab whose ramp gives the image a mean colour on target (sRGB-encoded mean)."""
        tgt = self.lab0 if target_lab is None else np.asarray(target_lab, float)
        base = tgt.copy()
        w = self.counts / self.counts.sum()
        for _ in range(iters):
            ramp = self.ramp8(base)
            mean = (ramp * w[:, None]).sum(0) if mean_fn is None else mean_fn(ramp)
            base = base + (tgt - pl.srgb8_to_lab(mean))
        return base

    def image(self, base):
        return self.ramp8(base)[self.idx].astype(np.uint8)


def multiply_tile(dL, ref_hex, knee, limit, seed=3):
    """Greyscale tile s in (0, 1] such that ref * s (CSS multiply) has L* = L*ref + dL. The light
    side is compressed softly above `knee` L* so the tile's mean stays close to 1 (the base colour
    is then lifted by 1/mean to keep the brand colour; see metrics.json)."""
    rng = np.random.default_rng(seed)
    ref = pl.hex_to_rgb8(ref_hex) / 255.0
    s_grid = np.linspace(0.80, 1.06, 5201)
    # encoded values may pass 1 here (the tile is rescaled to <= 1 below); the sRGB curve extends fine
    L_grid = pl.linear_to_lab(pl.srgb_to_linear(ref[None, :] * s_grid[:, None]))[:, 0]
    L0 = pl.srgb8_to_lab(ref * 255)[0]
    d = pl.soft_knee(dL, knee, limit)
    s = np.interp(L0 + d, L_grid, s_grid)
    s = s / s.max()
    return quantise8(s * 255, rng)


def overlay_tile(dD, gain, seed=4):
    """Mid-grey tile for CSS `overlay`: overlay is linear in the tile value, so a tile whose mean is
    exactly 127.5 leaves the mean colour of any base untouched."""
    rng = np.random.default_rng(seed)
    s = 127.5 + dD * gain
    s = s - (s.mean() - 127.5)
    q = quantise8(s, rng).astype(np.int32)
    err = q.mean() - 127.5
    k = int(round(abs(err) * q.size))
    if k:
        flat = q.ravel()
        cand = np.flatnonzero((flat > 0) & (flat < 255))
        idx = rng.choice(cand, size=k, replace=False)
        flat[idx] -= int(np.sign(err))
    return np.clip(q, 0, 255).astype(np.uint8)


# ---------------------------------------------------------------------------------------------
# encoding and checks
# ---------------------------------------------------------------------------------------------


def webp_bytes(rgb: np.ndarray, quality):
    buf = io.BytesIO()
    Image.fromarray(rgb.astype(np.uint8), "RGB").save(buf, "WEBP", quality=quality, method=6)
    return buf.getvalue()


def decode(b: bytes) -> np.ndarray:
    return np.asarray(Image.open(io.BytesIO(b)).convert("RGB"))


def png_bytes(arr: np.ndarray):
    """Greyscale -> 8-bit L PNG. Colour -> palette PNG with the palette sorted by lightness (the index
    image is then as smooth as a greyscale one and compresses like it); RGB if > 256 colours."""
    buf = io.BytesIO()
    if arr.ndim == 2:
        Image.fromarray(arr, "L").save(buf, "PNG", optimize=True)
        return buf.getvalue()
    flat = arr.reshape(-1, 3)
    uniq, inv = np.unique(flat, axis=0, return_inverse=True)
    if len(uniq) <= 256:
        L = pl.srgb8_to_lab(uniq.astype(float))[:, 0]
        order = np.argsort(L, kind="stable")
        rank = np.empty_like(order)
        rank[order] = np.arange(len(order))
        idx = rank[inv.ravel()].reshape(arr.shape[:2]).astype(np.uint8)
        im = Image.fromarray(idx, "P")
        im.putpalette(uniq[order].astype(np.uint8).ravel().tolist())
        im.save(buf, "PNG", optimize=True)
        assert np.array_equal(np.asarray(Image.open(io.BytesIO(buf.getvalue())).convert("RGB")), arr)
        return buf.getvalue()
    Image.fromarray(arr, "RGB").save(buf, "PNG", optimize=True)
    return buf.getvalue()


def _L(rgb):
    return pl.linear_to_lab(pl.srgb_to_linear(np.asarray(rgb, float) / 255.0))[..., 0]


def detail_kept(src_rgb, dec_rgb):
    """How much of the paper's structure survives the encoder, as correlations of L* bands:
    fine (< 1.5 px), fibre scale (1.5-6 px) and clouds (> 6 px)."""
    a, b = _L(src_rgb), _L(dec_rgb)
    out = {}
    pa = [a - pl.gblur(a, 1.5), pl.gblur(a, 1.5) - pl.gblur(a, 6), pl.gblur(a, 6)]
    pb = [b - pl.gblur(b, 1.5), pl.gblur(b, 1.5) - pl.gblur(b, 6), pl.gblur(b, 6)]
    for name, x, y in zip(("fine", "fibre", "clouds"), pa, pb):
        out[name] = round(float(np.corrcoef(x.ravel(), y.ravel())[0, 1]), 3)
    return out


def save(name, png: bytes, webp: bytes):
    for ext, data in (("png", png), ("webp", webp)):
        with open(os.path.join(OUT, f"{name}.{ext}"), "wb") as fh:
            fh.write(data)


def build_baked(key, spec, n, report):
    t0 = time.time()
    dL = field(n, spec["recipe"], spec["seed"] + (0 if n == 1024 else 100), size_strength(n, spec["strength"]),
               size_weights(n, spec.get("weights")))
    bk = Baked(dL, spec["hex"], spec["chroma_k"], spec.get("warm", 0.0))
    base = bk.solve()
    img = bk.image(base)
    png = png_bytes(img)
    q = WEBP_Q.get(key, WEBP_Q["default"])
    # WebP's YUV 4:2:0 conversion moves the mean a little, and its coarse chroma steps make the
    # decoded mean jump rather than converge: take damped steps and keep the best file
    tgt = bk.lab0.copy()
    base_w = base.copy()
    best = None
    for _ in range(8):
        webp_try = webp_bytes(bk.image(base_w), q)
        m = pl.srgb8_to_lab(decode(webp_try).reshape(-1, 3).mean(0))
        de = pl.delta_e2000(tgt, m)
        if best is None or de < best[0]:
            best = (de, webp_try)
        if de < 0.1:
            break
        base_w = base_w + 0.6 * (tgt - m)
    if best[0] > 0.2:
        # still off: search a small grid of a*/b* offsets around the base (the codec moves chroma in
        # steps, so the right answer is found by trying, not by stepping)
        for da in np.linspace(-0.9, 0.9, 7):
            for db in np.linspace(-0.9, 0.9, 7):
                trial = base + np.array([0.0, da, db])
                webp_try = webp_bytes(bk.image(trial), q)
                m = pl.srgb8_to_lab(decode(webp_try).reshape(-1, 3).mean(0))
                de = pl.delta_e2000(tgt, m)
                if de < best[0]:
                    best = (de, webp_try)
    webp = best[1]
    dec = decode(webp)
    name = f"paper-{key}-{n}"
    save(name, png, webp)
    rec = dict(
        hex=spec["hex"], recipe=spec["recipe"], strength=spec["strength"], webp_quality=q,
        png_kb=round(len(png) / 1024, 1), webp_kb=round(len(webp) / 1024, 1),
        png=pl.mean_colour_report(img, spec["hex"]), webp=pl.mean_colour_report(dec, spec["hex"]),
        seam_png=pl.seam_score(img), seam_webp=pl.seam_score(dec), seam_rank_png=pl.seam_rank(img),
        seam_rank_webp=pl.seam_rank(dec), webp_detail=detail_kept(img, dec),
        secs=round(time.time() - t0, 1),
    )
    report[name] = rec
    print(f"{name}: png {rec['png_kb']} KB, webp {rec['webp_kb']} KB, dE00 png {rec['png']['mean_srgb']['dE00']} "
          f"webp {rec['webp']['mean_srgb']['dE00']}, L* std {rec['png']['L_std']}, detail {rec['webp_detail']}")
    return name


def build_neutral(n, report):
    t0 = time.time()
    c = components(n, NEUTRAL["seed"] + (0 if n == 1024 else 100), LIGHT)
    names = []
    for label, st in NEUTRAL["strengths"].items():
        dL = combine(c, size_strength(n, st), size_weights(n))
        knee, limit = NEUTRAL["knee"]
        tile = multiply_tile(dL, NEUTRAL["ref"], knee * st / 1.2, limit * st / 1.2)
        png = png_bytes(tile)
        q = WEBP_Q.get("neutral", WEBP_Q["default"])
        rgb = np.repeat(tile[..., None], 3, -1)
        webp = webp_bytes(rgb, q)
        dec = decode(webp)
        name = f"paper-neutral-{label}-{n}"
        save(name, png, webp)
        m = tile.astype(float).mean() / 255.0
        m_webp = dec.astype(float).mean() / 255.0
        comp = {}
        for pk, hx in PALETTE.items():
            rgb8 = pl.hex_to_rgb8(hx)
            base = np.clip(rgb8 / m, 0, 255)
            res = pl.css_blend(base, tile.astype(float) / 255.0, "multiply")
            raw = pl.css_blend(rgb8, tile.astype(float) / 255.0, "multiply")
            comp[pk] = dict(
                base=pl.rgb8_to_hex(np.round(base)),
                dE00_compensated=pl.mean_colour_report(res, hx)["mean_srgb"]["dE00"],
                dE00_uncompensated=pl.mean_colour_report(raw, hx)["mean_srgb"]["dE00"],
                L_std=pl.mean_colour_report(res, hx)["L_std"],
            )
        report[name] = dict(
            blend="multiply", strength=st, tile_mean=round(m, 4), tile_mean_webp=round(m_webp, 4),
            tile_min_max=[int(tile.min()), int(tile.max())],
            png_kb=round(len(png) / 1024, 1), webp_kb=round(len(webp) / 1024, 1), webp_quality=q,
            seam_png=pl.seam_score(tile), seam_webp=pl.seam_score(dec), seam_rank_png=pl.seam_rank(tile),
            seam_rank_webp=pl.seam_rank(dec), webp_detail=detail_kept(rgb, dec), compensation=comp, secs=round(time.time() - t0, 1),
        )
        print(f"{name}: png {len(png)/1024:.1f} KB, webp {len(webp)/1024:.1f} KB, mean {m:.4f}, "
              f"cream L* std {comp['cream']['L_std']}, detail {report[name]['webp_detail']}")
        names.append(name)
    return names


def build_overlay(n, report):
    t0 = time.time()
    dD = field(n, "dark", OVERLAY["seed"] + (0 if n == 1024 else 100), size_strength(n, OVERLAY["strength"]), size_weights(n))
    tile = overlay_tile(dD, OVERLAY["gain"])
    png = png_bytes(tile)
    q = WEBP_Q.get("overlay", WEBP_Q["default"])
    rgb = np.repeat(tile[..., None], 3, -1)
    webp = webp_bytes(rgb, q)
    dec = decode(webp)
    name = f"cardstock-overlay-{n}"
    save(name, png, webp)
    sims = {}
    targets = {k: v for k, v in PALETTE.items() if k in ("deep-plum", "plum", "oxblood")}
    targets.update({k: v[0] for k, v in PROJECT.items()})
    for k, hx in targets.items():
        for mode in ("overlay", "soft-light"):
            res = pl.css_blend(pl.hex_to_rgb8(hx), dec[..., 0].astype(float) / 255.0, mode)
            r = pl.mean_colour_report(res, hx)
            sims[f"{k}/{mode}"] = dict(dE00=r["mean_srgb"]["dE00"], L_std=r["L_std"], L_p01_p99=r["L_p01_p99"])
    report[name] = dict(
        blend="overlay", tile_mean=round(float(tile.mean()), 3), tile_mean_webp=round(float(dec[..., 0].mean()), 3),
        tile_std=round(float(tile.std()), 3), tile_min_max=[int(tile.min()), int(tile.max())],
        png_kb=round(len(png) / 1024, 1), webp_kb=round(len(webp) / 1024, 1), webp_quality=q,
        seam_png=pl.seam_score(tile), seam_webp=pl.seam_score(dec), seam_rank_png=pl.seam_rank(tile),
        seam_rank_webp=pl.seam_rank(dec), webp_detail=detail_kept(rgb, dec), on_colours=sims, secs=round(time.time() - t0, 1),
    )
    print(f"{name}: png {len(png)/1024:.1f} KB, webp {len(webp)/1024:.1f} KB, mean {tile.mean():.3f} "
          f"(webp {dec[..., 0].mean():.3f}), std {tile.std():.2f}, detail {report[name]['webp_detail']}")
    return name


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="", help="comma list: cream,...,neutral,overlay")
    ap.add_argument("--sizes", default="1024,512")
    args = ap.parse_args()
    only = set(filter(None, args.only.split(",")))
    sizes = [int(s) for s in args.sizes.split(",")]
    path = os.path.join(OUT, "metrics.json")
    report = {}
    if os.path.exists(path):
        with open(path, encoding="utf-8") as fh:
            report = json.load(fh)
    t0 = time.time()
    for n in sizes:
        for key, spec in BAKED.items():
            if not only or key in only:
                build_baked(key, spec, n, report)
        if not only or "neutral" in only:
            build_neutral(n, report)
        if not only or "overlay" in only:
            build_overlay(n, report)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(report, fh, indent=1, sort_keys=True)
    print(f"done in {time.time() - t0:.0f} s -> {path}")


if __name__ == "__main__":
    main()
