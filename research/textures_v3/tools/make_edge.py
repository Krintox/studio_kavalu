"""A torn-paper edge for CSS masks (improves on website/public/textures/torn-top.svg).

    python make_edge.py

Writes, in research/textures_v3/:
  torn-edge-top.png / .webp      alpha mask, 2048 x 96 px drawn at 2x (use mask-size: 1024px 48px);
                                 periodic in x, so it repeats with no seam; fully opaque below row 72
  torn-edge-bottom.png / .webp   the same edge flipped for the bottom of a sheet
  torn-rim-top.png / .webp       the torn zone only (the thin, lighter, fibrous band just inside the
                                 edge), for an optional lighter layer, see README
  previews/torn-edge.jpg         cream sheet torn over deep plum at 1x and a 2x crop, old SVG for reference

How the edge is built (all periodic over the tile width):
  - the tear line: three octaves of 1-D noise (undulation ~ 230 px, ragged ~ 30 px, crumb ~ 7 px at
    1x), the middle octave folded through abs() so the line has the small cusps of torn fibre, not a
    smooth wave;
  - the torn zone: a 3-6 px band inside the line where the sheet is thinner (alpha ~ 0.82-0.97);
  - fibres: ~2,600 short strands rooted in the torn zone, most pointing out of the sheet, fading
    toward their tips, so the edge is feathered rather than cut.
"""
from __future__ import annotations

import os
import sys

import numpy as np
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import paperlib as pl  # noqa: E402
import preview_lib as pv  # noqa: E402

OUT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
W, H = 2048, 96  # drawn at 2x: 1024 x 48 CSS px
BASE = 34  # mean tear line, rows from the top (2x)


def noise1d(n, rng, sigma, hp=None):
    f = np.fft.fftfreq(n)
    F = np.fft.fft(rng.standard_normal(n)) * np.exp(-2 * np.pi**2 * sigma**2 * f**2)
    if hp:
        F *= 1 - np.exp(-(f * hp) ** 2)
    F[0] = 0
    x = np.fft.ifft(F).real
    return x / x.std()


def build(seed=7):
    rng = np.random.default_rng(seed)
    x = np.arange(W)
    big = noise1d(W, rng, 90, hp=1100) * 5.5
    rag = 0.35 + 0.65 / (1 + np.exp(-1.6 * noise1d(W, rng, 70)))  # some stretches tear raggeder
    mid = np.abs(noise1d(W, rng, 11)) * 4.6 * rag
    mid -= mid.mean()
    crumb = noise1d(W, rng, 2.2) * 1.3
    line = BASE + big + mid + crumb  # y of the tear at each x (2x px); paper is below the line

    yy = np.arange(H)[:, None].astype(float)
    # anti-aliased body: coverage of each pixel by "below the line"
    body = np.clip(yy + 0.5 - line[None, :], 0, 1)

    # the torn zone just inside the line: thinner, fibrous paper
    zone_w = 6 + 4 * (0.5 + 0.5 * noise1d(W, rng, 40))
    depth = yy - line[None, :]
    zone = np.clip(1 - depth / zone_w[None, :], 0, 1) * (depth > 0)
    grain = rng.standard_normal((H, W))
    grain = np.real(np.fft.ifft2(np.fft.fft2(grain) * np.exp(-2 * np.pi**2 * 0.9**2 * (
        np.fft.fftfreq(H)[:, None] ** 2 + np.fft.fftfreq(W)[None, :] ** 2))))
    grain /= grain.std()
    thin = 1 - zone * (0.07 + 0.05 * grain)  # the zone is a little translucent and uneven
    alpha = body * np.clip(thin, 0.75, 1.0)

    # fibres rooted in the torn zone, mostly pointing out of the sheet (up), fading to their tips
    nf = 1100
    # the fringe clumps: some stretches of the tear pulled more fibre out than others
    dens = np.exp(1.3 * noise1d(W, rng, 45))
    fx = rng.choice(W, size=nf, p=dens / dens.sum()) + rng.uniform(0, 1, nf)
    root = np.interp(fx, x, line, period=W) + rng.uniform(0.0, 4.0, nf)
    ang = -np.pi / 2 + rng.normal(0, 0.9, nf)  # mostly out of the sheet, many lying along the edge
    length = np.clip(np.exp(rng.normal(np.log(4.5), 0.5, nf)), 1.5, 18)
    strength = np.clip(rng.normal(0.42, 0.15, nf), 0.12, 0.8)
    bend = rng.normal(0, 0.25, nf)
    step = 0.3
    m = np.maximum(3, np.ceil(length / step)).astype(int)
    idx = np.repeat(np.arange(nf), m)
    starts = np.cumsum(m) - m
    t = (np.arange(m.sum()) - np.repeat(starts, m) + 0.5) / np.repeat(m, m)
    ux, uy = np.cos(ang), np.sin(ang)
    vx, vy = -uy, ux
    L = length[idx]
    px = fx[idx] + ux[idx] * L * t + vx[idx] * bend[idx] * L * t * t
    py = root[idx] + uy[idx] * L * t + vy[idx] * bend[idx] * L * t * t
    w = strength[idx] * (1 - t) ** 0.8 * step
    acc = np.zeros(H * W)
    x0 = np.floor(px)
    y0 = np.floor(py)
    ax, ay = px - x0, py - y0
    for dx, dy, ww in ((0, 0, (1 - ax) * (1 - ay)), (1, 0, ax * (1 - ay)), (0, 1, (1 - ax) * ay), (1, 1, ax * ay)):
        xi = (x0.astype(int) + dx) % W
        yi = y0.astype(int) + dy
        ok = (yi >= 0) & (yi < H)
        acc += np.bincount(yi[ok] * W + xi[ok], weights=(w * ww)[ok], minlength=H * W)
    fib = acc.reshape(H, W)
    # soften to a 1 px strand (periodic in x)
    k = np.exp(-0.5 * (np.arange(-3, 4) / 0.55) ** 2)
    k /= k.sum()
    fib = sum(np.roll(fib, s, 1) * k[i] for i, s in enumerate(range(-3, 4)))
    fib = sum(np.pad(fib, ((3, 3), (0, 0)), mode="edge")[3 + s : 3 + s + H] * k[i] for i, s in enumerate(range(-3, 4)))
    fib = np.clip(fib * 2.2, 0, 1)

    alpha = np.maximum(alpha, fib * (1 - body))  # fibres only add where there is no paper yet
    alpha[BASE + 38 :] = 1.0  # well below the deepest part of the tear: solid
    assert alpha[-1].min() == 1.0
    rim = np.clip(np.maximum(zone * body * (0.6 + 0.25 * grain.clip(-1, 1)), fib * (1 - body) * 0.7), 0, 1)
    return alpha, rim, line


def save_mask(a, name):
    a8 = np.clip(np.round(a * 255), 0, 255).astype(np.uint8)
    la = np.dstack([np.full_like(a8, 0), a8])  # black + alpha: works as a mask (alpha) and as a shape
    Image.fromarray(la, "LA").save(os.path.join(OUT, name + ".png"), optimize=True)
    rgba = Image.fromarray(np.dstack([np.zeros_like(a8)] * 3 + [a8]), "RGBA")
    rgba.save(os.path.join(OUT, name + ".webp"), lossless=True, quality=100, method=6)
    return a8


def old_svg_mask(width, height=40):
    pts = []
    import re
    svg = open(os.path.join(OUT, "..", "..", "website", "public", "textures", "torn-top.svg"), encoding="utf-8").read()
    for a, b in re.findall(r"([\d.]+),([\d.]+)", svg):
        pts.append((float(a) * width / 1440, float(b) * height / 40))
    im = Image.new("L", (width * 4, height * 4), 0)
    ImageDraw.Draw(im).polygon([(p[0] * 4, p[1] * 4) for p in pts], fill=255)
    return np.asarray(im.resize((width, height), Image.LANCZOS)).astype(float) / 255


def preview(alpha, rim):
    cream = np.asarray(Image.open(os.path.join(OUT, "paper-cream-1024.webp")).convert("RGB")).astype(float)
    deep = np.asarray(Image.open(os.path.join(OUT, "paper-deep-plum-1024.webp")).convert("RGB")).astype(float)
    bright = np.array([251, 250, 242.0])
    Wp, Hp = 1440, 300

    def sheet(scale):
        # page: deep plum, a cream sheet from y=90 down whose top is the torn edge (mask-size 1024 x 48)
        w, h = Wp * scale, Hp * scale
        bg = pv.tile_bg(deep.astype(np.uint8), w, h).astype(float) if scale == 1 else \
            np.asarray(Image.fromarray(pv.tile_bg(deep.astype(np.uint8), Wp, Hp)).resize((w, h), Image.BILINEAR)).astype(float)
        cr = pv.tile_bg(cream.astype(np.uint8), w, h).astype(float) if scale == 1 else \
            np.asarray(Image.fromarray(pv.tile_bg(cream.astype(np.uint8), Wp, Hp)).resize((w, h), Image.BILINEAR)).astype(float)
        a_t = alpha if scale == 2 else np.asarray(Image.fromarray((alpha * 255).astype(np.uint8)).resize((W // 2, H // 2), Image.LANCZOS)) / 255
        r_t = rim if scale == 2 else np.asarray(Image.fromarray((rim * 255).astype(np.uint8)).resize((W // 2, H // 2), Image.LANCZOS)) / 255
        top = 90 * scale
        mask = np.zeros((h, w))
        mask[top + a_t.shape[0]:] = 1
        reps = int(np.ceil(w / a_t.shape[1])) + 1
        mask[top:top + a_t.shape[0]] = np.tile(a_t, (1, reps))[:, :w]
        rimm = np.zeros((h, w))
        rimm[top:top + a_t.shape[0]] = np.tile(r_t, (1, reps))[:, :w]
        # a soft shadow of the sheet on the plum (the site's box-shadow 0 -30px 60px rgb(10 2 6 / .25))
        sh = np.roll(mask, -6 * scale, 0)
        from scipy import ndimage
        sh = ndimage.gaussian_filter(sh, (14 * scale, 14 * scale), mode="nearest") * 0.35
        page = bg * (1 - sh[..., None]) + np.array([10, 2, 6.0]) * sh[..., None]
        paper = cr * (1 - 0.35 * rimm[..., None]) + bright * 0.35 * rimm[..., None]
        out = page * (1 - mask[..., None]) + paper * mask[..., None]
        return np.clip(out, 0, 255).astype(np.uint8)

    one = sheet(1)
    two = sheet(2)[120:120 + 300, 0:1440]
    old = old_svg_mask(Wp)
    o = pv.tile_bg(deep.astype(np.uint8), Wp, 180).astype(float)
    c = pv.tile_bg(cream.astype(np.uint8), Wp, 180).astype(float)
    m = np.zeros((180, Wp))
    m[60:100] = old
    m[100:] = 1
    oldimg = (o * (1 - m[..., None]) + c * m[..., None]).astype(np.uint8)
    blocks = [
        pv.label_strip("new torn edge at 1x: torn-edge-top (mask-size 1024px 48px) + torn-rim-top, cream sheet over deep plum"),
        Image.fromarray(one),
        pv.label_strip("the same at 2x (retina), 1440 x 300 device px crop"),
        Image.fromarray(two),
        pv.label_strip("for reference: the old torn-top.svg (polygon, stretched to the width)"),
        Image.fromarray(oldimg),
    ]
    img = pv.stack(blocks)
    os.makedirs(os.path.join(OUT, "previews"), exist_ok=True)
    img.save(os.path.join(OUT, "previews", "torn-edge.jpg"), quality=93, subsampling=0)
    return img


def main():
    alpha, rim, line = build()
    a8 = save_mask(alpha, "torn-edge-top")
    save_mask(alpha[::-1], "torn-edge-bottom")
    save_mask(rim, "torn-rim-top")
    # a mask is flat except along the tear, so compare the step across the wrap with the steps between
    # every other pair of neighbouring columns: a seam would sit far out in the tail
    a = a8.astype(float)
    steps = np.abs(np.diff(a, axis=1)).mean(0)
    wrap = np.abs(a[:, 0] - a[:, -1]).mean()
    print(f"wrap step {wrap:.2f} vs interior median {np.median(steps):.2f}; "
          f"{(steps > wrap).mean() * 100:.0f}% of interior column pairs step more (a seam would be ~0%)",
          "| tear line min/max (2x px):", round(line.min(), 1), round(line.max(), 1))
    for n in ("torn-edge-top", "torn-edge-bottom", "torn-rim-top"):
        for ext in ("png", "webp"):
            print(f"{n}.{ext}: {os.path.getsize(os.path.join(OUT, f'{n}.{ext}')) / 1024:.1f} KB")
    preview(alpha, rim)


if __name__ == "__main__":
    main()
