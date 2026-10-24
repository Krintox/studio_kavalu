"""Align, crop and score a high-resolution candidate against its tiny source image.

    python fidelity.py gpt  <rel> <raw.png> [--tag base]   # register + crop to source framing, write gpt/<rel>.png
    python fidelity.py html <rel> <render.png>             # score an HTML render (already source framing)
    python fidelity.py score <rel> <candidate.png> --method X --out-name Y   # score any file as-is

Fidelity = the candidate downscaled to the source size, compared with the source:
  ssim      greyscale SSIM (Gaussian window, sigma 1.5) at source size
  ssim_half the same at half the source size (less sensitive to the source's own blur)
  ncc       normalised cross-correlation of greyscale
  dE        mean CIE76 colour difference (Lab), plus the mean signed RGB bias
A side-by-side sheet goes to research/images_hq/compare/<basename>.jpg and the numbers to <basename>.json.
"""
from __future__ import annotations

import argparse
import json
import os
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont
from scipy import ndimage, optimize

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
SRC_DIR = os.path.join(ROOT, "website", "public", "work")
HQ = os.path.join(ROOT, "research", "images_hq")
CMP = os.path.join(HQ, "compare")


# ---------------------------------------------------------------- metrics
def grey(a: np.ndarray) -> np.ndarray:
    return a[..., 0] * 0.299 + a[..., 1] * 0.587 + a[..., 2] * 0.114


def ssim(a: np.ndarray, b: np.ndarray, sigma: float = 1.5, L: float = 255.0) -> float:
    a = a.astype(np.float64)
    b = b.astype(np.float64)
    C1, C2 = (0.01 * L) ** 2, (0.03 * L) ** 2
    mu_a, mu_b = ndimage.gaussian_filter(a, sigma), ndimage.gaussian_filter(b, sigma)
    saa = ndimage.gaussian_filter(a * a, sigma) - mu_a ** 2
    sbb = ndimage.gaussian_filter(b * b, sigma) - mu_b ** 2
    sab = ndimage.gaussian_filter(a * b, sigma) - mu_a * mu_b
    m = ((2 * mu_a * mu_b + C1) * (2 * sab + C2)) / ((mu_a ** 2 + mu_b ** 2 + C1) * (saa + sbb + C2))
    return float(m.mean())


def ncc(a: np.ndarray, b: np.ndarray, mask: np.ndarray | None = None) -> float:
    if mask is not None:
        a, b = a[mask], b[mask]
    a = a.astype(np.float64).ravel()
    b = b.astype(np.float64).ravel()
    a = a - a.mean()
    b = b - b.mean()
    d = np.sqrt((a * a).sum() * (b * b).sum())
    return float((a * b).sum() / d) if d > 0 else 0.0


def srgb_to_lab(rgb: np.ndarray) -> np.ndarray:
    c = rgb.astype(np.float64) / 255.0
    c = np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    M = np.array([[0.4124564, 0.3575761, 0.1804375],
                  [0.2126729, 0.7151522, 0.0721750],
                  [0.0193339, 0.1191920, 0.9503041]])
    xyz = c @ M.T / np.array([0.95047, 1.0, 1.08883])
    f = np.where(xyz > (6 / 29) ** 3, np.cbrt(xyz), xyz / (3 * (6 / 29) ** 2) + 4 / 29)
    L = 116 * f[..., 1] - 16
    A = 500 * (f[..., 0] - f[..., 1])
    B = 200 * (f[..., 1] - f[..., 2])
    return np.stack([L, A, B], -1)


def metrics(src: Image.Image, cand: Image.Image) -> dict:
    s = np.asarray(src.convert("RGB"), dtype=np.float64)
    c_small = cand.convert("RGB").resize(src.size, Image.LANCZOS)
    c = np.asarray(c_small, dtype=np.float64)
    hw = (max(8, src.width // 2), max(8, src.height // 2))
    s2 = np.asarray(src.convert("RGB").resize(hw, Image.LANCZOS), dtype=np.float64)
    c2 = np.asarray(cand.convert("RGB").resize(hw, Image.LANCZOS), dtype=np.float64)
    dE = np.sqrt(((srgb_to_lab(s) - srgb_to_lab(c)) ** 2).sum(-1))
    return {
        "ssim": round(ssim(grey(s), grey(c)), 4),
        "ssim_half": round(ssim(grey(s2), grey(c2)), 4),
        "ncc": round(ncc(grey(s), grey(c)), 4),
        "dE_mean": round(float(dE.mean()), 2),
        "dE_p95": round(float(np.percentile(dE, 95)), 2),
        "rgb_bias": [round(float(x), 1) for x in (c - s).reshape(-1, 3).mean(0)],
    }, c_small


# ---------------------------------------------------------------- global colour match (GPT outputs)
def _feats(rgb: np.ndarray) -> np.ndarray:
    r, g, b = rgb[:, 0], rgb[:, 1], rgb[:, 2]
    return np.stack([np.ones_like(r), r, g, b, r * r, g * g, b * b, r * g, r * b, g * b], 1)


def colour_fit(src: Image.Image, cand_small: Image.Image, blur: float = 1.2, iters: int = 6) -> np.ndarray:
    """Second-order polynomial RGB transform mapping the aligned, downscaled candidate onto the source.
    Fitted on blurred images with Huber-style reweighting, so local content differences do not drive it."""
    S = ndimage.gaussian_filter(np.asarray(src.convert("RGB"), dtype=np.float64) / 255, (blur, blur, 0)).reshape(-1, 3)
    C = ndimage.gaussian_filter(np.asarray(cand_small.convert("RGB"), dtype=np.float64) / 255, (blur, blur, 0)).reshape(-1, 3)
    X = _feats(C)
    w = np.ones(len(X))
    coef = np.zeros((10, 3))
    for _ in range(iters):
        for ch in range(3):
            Wx = X * w[:, None]
            coef[:, ch] = np.linalg.lstsq(Wx, S[:, ch] * w, rcond=None)[0]
        res = np.abs(X @ coef - S).sum(1)
        d = 0.04
        w = np.where(res <= d, 1.0, d / np.maximum(res, 1e-9))
    return coef


def colour_apply(im: Image.Image, coef: np.ndarray) -> Image.Image:
    a = np.asarray(im.convert("RGB"), dtype=np.float64) / 255
    flat = a.reshape(-1, 3)
    out = np.empty_like(flat)
    step = 400000
    for i in range(0, len(flat), step):
        out[i:i + step] = _feats(flat[i:i + step]) @ coef
    out = np.clip(out.reshape(a.shape) * 255 + 0.5, 0, 255).astype(np.uint8)
    return Image.fromarray(out)


# ---------------------------------------------------------------- registration
def _prep(im: Image.Image, blur: float) -> np.ndarray:
    g = grey(np.asarray(im.convert("RGB"), dtype=np.float64))
    return ndimage.gaussian_filter(g, blur) if blur > 0 else g


def register(src: Image.Image, gen: Image.Image) -> dict:
    """Find gen_xy = (sx*x + tx, sy*y + ty) for source pixel (x, y) that maximises NCC."""
    ws, hs = src.size
    Wg, Hg = gen.size
    # work with gen reduced so that it is ~1.5x the source scale (cheap, still precise)
    red = max(1.0, min(Wg / ws, Hg / hs) / 1.5)
    gsmall = gen.resize((round(Wg / red), round(Hg / red)), Image.LANCZOS)
    G = _prep(gsmall, 0.8)
    S = _prep(src, 0.8)
    yy, xx = np.mgrid[0:hs, 0:ws].astype(np.float64)

    def warp(p):
        sx, sy, tx, ty = p
        X = (sx * xx + tx) / red
        Y = (sy * yy + ty) / red
        inside = (X >= 0) & (X <= G.shape[1] - 1) & (Y >= 0) & (Y <= G.shape[0] - 1)
        v = ndimage.map_coordinates(G, [Y, X], order=1, mode="nearest")
        return v, inside

    def cost(p):
        v, inside = warp(p)
        frac = inside.mean()
        if frac < 0.5:
            return 2.0
        return -ncc(S, v, inside) + 2.0 * (1 - frac)

    guesses = []
    fx, fy = Wg / ws, Hg / hs
    guesses.append((fx, fy, 0.0, 0.0))                                   # stretched to fill
    s = max(fx, fy)
    guesses.append((s, s, (Wg - s * ws) / 2, (Hg - s * hs) / 2))          # cover, centred
    s = min(fx, fy)
    guesses.append((s, s, (Wg - s * ws) / 2, (Hg - s * hs) / 2))          # contain, centred
    best = None
    for g in guesses:
        # coarse grid around the guess
        cands = []
        for ds in (0.92, 0.96, 1.0, 1.04, 1.08):
            for dt_x in (-0.06, -0.03, 0, 0.03, 0.06):
                for dt_y in (-0.06, -0.03, 0, 0.03, 0.06):
                    p = (g[0] * ds, g[1] * ds, g[2] + dt_x * Wg, g[3] + dt_y * Hg)
                    cands.append((cost(p), p))
        cands.sort(key=lambda t: t[0])
        for c0, p0 in cands[:3]:
            r = optimize.minimize(cost, np.array(p0), method="Nelder-Mead",
                                  options={"xatol": 0.05, "fatol": 1e-5, "maxiter": 1500,
                                           "initial_simplex": None})
            if best is None or r.fun < best[0]:
                best = (r.fun, r.x)
    sx, sy, tx, ty = [float(v) for v in best[1]]
    v, inside = warp(best[1])
    return {"sx": sx, "sy": sy, "tx": tx, "ty": ty, "ncc_reg": round(-best[0], 4),
            "coverage": round(float(inside.mean()), 4), "anisotropy": round(sx / sy, 4)}


def crop_to_source(gen: Image.Image, src: Image.Image, reg: dict) -> tuple[Image.Image, dict]:
    ws, hs = src.size
    x0, y0 = reg["tx"], reg["ty"]
    x1, y1 = reg["tx"] + reg["sx"] * ws, reg["ty"] + reg["sy"] * hs
    info = {"box": [round(x0, 1), round(y0, 1), round(x1, 1), round(y1, 1)]}
    W, H = gen.size
    miss = {"left": max(0.0, -x0), "top": max(0.0, -y0), "right": max(0.0, x1 - W), "bottom": max(0.0, y1 - H)}
    info["missing_px"] = {k: round(v, 1) for k, v in miss.items()}
    cw = x1 - x0
    out_w = round(cw)
    out_h = round(out_w * hs / ws)
    # PIL crop pads outside areas with black; edge-extend instead so a 1-3 px overshoot does not draw a line
    pad = int(np.ceil(max(miss.values()))) + 2
    g = gen.convert("RGB")
    if pad > 2:
        arr = np.asarray(g)
        arr = np.pad(arr, ((pad, pad), (pad, pad), (0, 0)), mode="edge")
        g = Image.fromarray(arr)
        x0, y0, x1, y1 = x0 + pad, y0 + pad, x1 + pad, y1 + pad
    out = g.resize((out_w, out_h), Image.LANCZOS, box=(x0, y0, x1, y1))
    info["out_size"] = [out_w, out_h]
    return out, info


# ---------------------------------------------------------------- sheet
def _font(sz: int):
    for f in ("C:/Windows/Fonts/segoeui.ttf", "C:/Windows/Fonts/arial.ttf"):
        if os.path.exists(f):
            return ImageFont.truetype(f, sz)
    return ImageFont.load_default()


def sheet(src: Image.Image, cand: Image.Image, cand_small: Image.Image, title: str, lines: list[str], path: str):
    ar = src.width / src.height
    if ar >= 1.25:
        pw = 1100
        ph = round(pw / ar)
        vertical = True
    else:
        ph = 820
        pw = round(ph * ar)
        vertical = False
    panels = [
        ("source (enlarged)", src.convert("RGB").resize((pw, ph), Image.LANCZOS)),
        ("candidate downscaled to source size (enlarged the same way)", cand_small.resize((pw, ph), Image.LANCZOS)),
        (f"candidate full ({cand.width}x{cand.height})", cand.convert("RGB").resize((pw, ph), Image.LANCZOS)),
    ]
    s = np.asarray(src.convert("RGB"), dtype=np.float64)
    c = np.asarray(cand_small, dtype=np.float64)
    d = np.abs(grey(s) - grey(c))
    d = np.clip(d * 3, 0, 255).astype(np.uint8)
    heat = Image.fromarray(d).convert("L").resize((pw, ph), Image.NEAREST)
    heat = Image.merge("RGB", (heat, Image.new("L", heat.size, 0), Image.new("L", heat.size, 40)))
    panels.append(("|grey difference| x3 at source size", heat))
    head = 40 + 24 * len(lines)
    lab = 26
    if vertical:
        W = pw + 20
        H = head + len(panels) * (ph + lab + 10)
    else:
        W = len(panels) * (pw + 10) + 10
        H = head + ph + lab + 10
    img = Image.new("RGB", (W, H), (250, 248, 242))
    dr = ImageDraw.Draw(img)
    dr.text((10, 8), title, fill=(20, 20, 20), font=_font(22))
    for i, ln in enumerate(lines):
        dr.text((10, 38 + 24 * i), ln, fill=(60, 60, 60), font=_font(17))
    for i, (name, im) in enumerate(panels):
        if vertical:
            x, y = 10, head + i * (ph + lab + 10)
        else:
            x, y = 10 + i * (pw + 10), head
        dr.text((x, y + 2), name, fill=(40, 40, 40), font=_font(16))
        img.paste(im, (x, y + lab))
    img.save(path, quality=90)


# ---------------------------------------------------------------- main
def src_path(rel: str) -> str:
    return os.path.join(SRC_DIR, rel.replace("/", os.sep) + ".jpg")


def run_score(rel: str, cand: Image.Image, method: str, out_path: str, extra: dict, name: str | None = None) -> dict:
    src = Image.open(src_path(rel)).convert("RGB")
    m, small = metrics(src, cand)
    base = name or os.path.basename(rel)
    res = {"rel": rel, "method": method, "output": os.path.relpath(out_path, ROOT).replace("\\", "/"),
           "size": list(cand.size), "src_size": list(src.size), **m, **extra}
    lines = [f"method: {method}   output: {res['output']}   {cand.width}x{cand.height} (source {src.width}x{src.height})",
             f"SSIM {m['ssim']}  SSIM(half) {m['ssim_half']}  NCC {m['ncc']}  mean dE {m['dE_mean']}  p95 dE {m['dE_p95']}  RGB bias {m['rgb_bias']}"]
    if "registration" in extra:
        r = extra["registration"]
        lines.append(f"registration: sx {r['sx']:.3f} sy {r['sy']:.3f} (anisotropy {r['anisotropy']}) tx {r['tx']:.1f} ty {r['ty']:.1f} coverage {r['coverage']} missing {extra.get('crop', {}).get('missing_px')}")
    os.makedirs(CMP, exist_ok=True)
    sheet(src, cand, small, f"{rel}  [{method}]", lines, os.path.join(CMP, base + ".jpg"))
    with open(os.path.join(CMP, base + ".json"), "w", encoding="utf-8") as f:
        json.dump(res, f, indent=2)
    return res


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["gpt", "gemini", "html", "score"])
    ap.add_argument("rel")
    ap.add_argument("cand")
    ap.add_argument("--tag", default="")
    ap.add_argument("--method", default="")
    ap.add_argument("--out-name", default=None)
    ap.add_argument("--no-colour", action="store_true", help="skip the global colour match")
    a = ap.parse_args()
    src = Image.open(src_path(a.rel)).convert("RGB")
    cand = Image.open(a.cand).convert("RGB")
    if a.mode in ("gpt", "gemini"):
        reg = register(src, cand)
        out, info = crop_to_source(cand, src, reg)
        out_path = os.path.join(HQ, a.mode, a.rel.replace("/", os.sep) + ".png")
        if a.out_name:
            out_path = os.path.join(HQ, a.mode, "_work", a.rel.replace("/", os.sep), a.out_name + ".png")
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        work = os.path.join(HQ, a.mode, "_work", a.rel.replace("/", os.sep))
        os.makedirs(work, exist_ok=True)
        aligned_path = os.path.join(work, (a.out_name or a.tag or "base") + ".aligned.png")
        out.save(aligned_path, optimize=True)
        m0, small0 = metrics(src, out)
        extra = {"registration": reg, "crop": info, "raw": os.path.relpath(a.cand, ROOT).replace("\\", "/"),
                 "raw_size": list(cand.size), "aligned": os.path.relpath(aligned_path, ROOT).replace("\\", "/"),
                 "before_colour_match": m0}
        if not a.no_colour:
            coef = colour_fit(src, small0)
            out = colour_apply(out, coef)
            extra["colour_match"] = "2nd-order RGB polynomial fitted to the source (robust), applied globally"
        out.save(out_path, optimize=True)
        res = run_score(a.rel, out, a.method or f"{a.mode}{('-' + a.tag) if a.tag else ''}", out_path, extra,
                        name=(os.path.basename(a.rel) + (f".{a.out_name}" if a.out_name else "")))
    elif a.mode == "html":
        res = run_score(a.rel, cand, a.method or "html", a.cand, {})
    else:
        res = run_score(a.rel, cand, a.method or "score", a.cand, {}, name=a.out_name)
    print(json.dumps(res, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
