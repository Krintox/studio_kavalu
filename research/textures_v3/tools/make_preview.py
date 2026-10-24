"""Previews for the v3 paper textures.

    python make_preview.py

Every panel is rendered from the decoded .webp file (what a browser shows), tiled at 1:1 over a
1440 x 900 page with the site's own type, so seams would show where the 1024 tile repeats (x = 1024).
Writes previews/<name>.jpg (one per panel), previews/tiling-*.jpg (3 x 3 repeats) and preview.jpg
(all of them stacked), plus contrast.json.
"""
from __future__ import annotations

import json
import os
import sys

import numpy as np
from PIL import Image, ImageDraw
from scipy import ndimage

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import make_textures as mt  # noqa: E402
import paperlib as pl  # noqa: E402
import preview_lib as pv  # noqa: E402

OUT = mt.OUT
PREV = os.path.join(OUT, "previews")
os.makedirs(PREV, exist_ok=True)

CREAM, INK, PLUM, DEEP, BLUE = "#F3F3E7", "#241319", "#390D26", "#270617", "#ABCDD6"
INK_SOFT = "#5D4A50"


def load(name):
    return np.asarray(Image.open(os.path.join(OUT, name)).convert("RGB"))


def blend_page(tile_name, base_hex, mode, opacity=1.0):
    t = load(tile_name)[..., 0].astype(float) / 255.0
    bg = pv.tile_bg(t)
    return np.round(pl.css_blend(pl.hex_to_rgb8(base_hex), bg, mode, opacity)).astype(np.uint8)


def local_extremes(bg):
    """Paper luminance at its darkest and lightest 0.1 %, after a 1 px blur (what sits behind a stroke)."""
    Y = pl.srgb_to_linear(bg.astype(float) / 255.0) @ pl.LUM
    Yb = ndimage.gaussian_filter(Y, 1.0, mode="wrap")
    return float(np.percentile(Yb, 0.1)), float(np.percentile(Yb, 99.9)), float(Y.mean())


def contrast_lines(bg, texts):
    lo, hi, mean = local_extremes(bg)
    out, rec = [], {}
    for label, hx in texts:
        yt = float(pl.rel_luminance_srgb8(pl.hex_to_rgb8(hx)))
        cr_mean = pl.contrast_ratio(yt, mean)
        worst_bg = hi if yt > mean else lo  # light text: lightest patch; dark text: darkest
        cr_worst = pl.contrast_ratio(yt, worst_bg)
        rec[label] = dict(text=hx, mean=round(float(cr_mean), 2), worst=round(float(cr_worst), 2))
        out.append(f"{label} {hx}: {cr_mean:.1f}:1 (worst 0.1% patch {cr_worst:.1f}:1)")
    return out, rec


def kb(name):
    return os.path.getsize(os.path.join(OUT, name)) / 1024


def main():
    with open(os.path.join(OUT, "metrics.json"), encoding="utf-8") as fh:
        M = json.load(fh)
    panels, contrast = [], {}

    def add(key, bg, colours, label, texts, extra):
        lines, rec = contrast_lines(bg, texts)
        contrast[key] = rec
        img = pv.panel(bg, colours, label, extra + ["  ".join(lines)])
        img.save(os.path.join(PREV, f"{key}.jpg"), quality=93, subsampling=0)
        panels.append((key, img))

    light_cols = dict(heading=PLUM, body=INK, soft=INK_SOFT, accent=PLUM)
    dark_cols = dict(heading=CREAM, body=CREAM, soft=BLUE, accent=BLUE)

    for key, hx, cols, texts in (
        ("cream", CREAM, light_cols, [("ink", INK), ("plum", PLUM)]),
        ("writing-paper", "#F8F5E8", light_cols, [("ink", INK), ("plum", PLUM)]),
        ("powder-blue", BLUE, dict(heading=PLUM, body=PLUM, soft="#390D26", accent=PLUM), [("plum", PLUM), ("ink", INK)]),
        ("deep-plum", DEEP, dark_cols, [("cream", CREAM), ("blue", BLUE)]),
        ("plum", PLUM, dark_cols, [("cream", CREAM), ("blue", BLUE)]),
        ("oxblood", "#491C17", dark_cols, [("cream", CREAM), ("blue", BLUE)]),
    ):
        name = f"paper-{key}-1024"
        m = M[name]
        bg = pv.tile_bg(load(name + ".webp"))
        extra = [
            f"paper-{key}-1024.webp {m['webp_kb']} KB (q{m['webp_quality']})  png {m['png_kb']} KB  |  "
            f"512: webp {M[f'paper-{key}-512']['webp_kb']} KB, png {M[f'paper-{key}-512']['png_kb']} KB",
            f"mean colour vs {hx}: dE00 {m['webp']['mean_srgb']['dE00']} (webp), {m['png']['mean_srgb']['dE00']} (png)  "
            f"L* std {m['webp']['L_std']}  background-size: 1024px",
        ]
        add(f"paper-{key}", bg, cols, f"Studio Kavalu paper v3  /  {key.replace('-', ' ')}  {hx}  /  baked", texts, extra)

    for label, base_key in (("light", "cream-2"), ("strong", "cream-3")):
        name = f"paper-neutral-{label}-1024"
        m = M[name]
        comp = m["compensation"][base_key]
        bg = blend_page(name + ".webp", comp["base"], "multiply")
        extra = [
            f"{name}.webp {m['webp_kb']} KB  png {m['png_kb']} KB  |  tile mean {m['tile_mean']}  |  "
            f"background-color {comp['base']} (= {mt.PALETTE[base_key]} / mean) + multiply",
            f"mean colour vs {mt.PALETTE[base_key]}: dE00 {comp['dE00_compensated']} (compensated), "
            f"{comp['dE00_uncompensated']} if the plain hex is used  L* std {comp['L_std']}",
        ]
        add(f"neutral-{label}-on-{base_key}", bg, light_cols,
            f"neutral {label} (multiply)  on  {base_key} {mt.PALETTE[base_key]}", [("ink", INK), ("plum", PLUM)], extra)

    # the cardstock overlay on every project colour: one panel of five bands, then a full page on rust
    t = load("cardstock-overlay-1024.webp")[..., 0].astype(float) / 255.0
    band_h = pv.H // 5
    page = np.zeros((pv.H, pv.W, 3), np.uint8)
    half = pv.W // 2
    for i, (pk, (bgc, ink)) in enumerate(mt.PROJECT.items()):
        tb = pv.tile_bg(t, pv.W, band_h, 0, i * band_h)
        base = pl.hex_to_rgb8(bgc)
        sl = np.round(pl.css_blend(base, tb, "soft-light")).astype(np.uint8)
        ov = np.round(pl.css_blend(base, tb, "overlay")).astype(np.uint8)
        page[i * band_h:(i + 1) * band_h, :half] = sl[:, :half]
        page[i * band_h:(i + 1) * band_h, half:] = ov[:, half:]
    img = Image.fromarray(page)
    d = ImageDraw.Draw(img)
    rec = {}
    for i, (pk, (bgc, ink)) in enumerate(mt.PROJECT.items()):
        y = i * band_h
        band = page[y:y + band_h, :half]
        lines, r = contrast_lines(band, [("ink", ink)])
        rec[pk] = r
        s_sl = M["cardstock-overlay-1024"]["on_colours"][f"{pk}/soft-light"]
        s_ov = M["cardstock-overlay-1024"]["on_colours"][f"{pk}/overlay"]
        col = pv.hexrgb(ink)
        d.text((72, y + 26), f"{pk.replace('-', ' ').title()} spread", font=pv.font("display", 44, 340), fill=col)
        body = pv.font("text", 16, 400)
        d.text((72, y + 86), "A brand is a set of choices; what it says, how it looks.", font=body, fill=col)
        d.text((72, y + 110), "We shape brands, feeds and persona through a design lens.", font=body, fill=col)
        mono = pv.font("mono", 11)
        pv.text_spaced(d, (72, y + 148), f"SOFT-LIGHT  {bgc}  dE00 {s_sl['dE00']}  L* std {s_sl['L_std']}  {lines[0]}", mono, col, 0.03)
        d.text((half + 72, y + 86), "A brand is a set of choices; what it says, how it looks.", font=body, fill=col)
        d.text((half + 72, y + 110), "We shape brands, feeds and persona through a design lens.", font=body, fill=col)
        pv.text_spaced(d, (half + 72, y + 148), f"OVERLAY  {bgc}  dE00 {s_ov['dE00']}  L* std {s_ov['L_std']}", mono, col, 0.03)
    contrast["cardstock-on-projects"] = rec
    img.save(os.path.join(PREV, "cardstock-overlay-on-projects.jpg"), quality=93, subsampling=0)
    panels.append(("cardstock-overlay-on-projects (left half soft-light, right half overlay)", img))

    m = M["cardstock-overlay-1024"]
    bg = blend_page("cardstock-overlay-1024.webp", "#9F4A30", "soft-light")
    add("cardstock-on-rust", bg, dict(heading="#FAEBCA", body="#FAEBCA", soft="#FAEBCA", accent="#FAEBCA"),
        "cardstock overlay (soft-light)  on  a project spread  #9F4A30", [("ink", "#FAEBCA")],
        [f"cardstock-overlay-1024.webp {m['webp_kb']} KB (q{m['webp_quality']})  png {m['png_kb']} KB  |  tile mean "
         f"{m['tile_mean_webp']} (127.5 = neutral)  background-blend-mode: soft-light",
         f"on #9F4A30: dE00 {m['on_colours']['rust/soft-light']['dE00']} soft-light, {m['on_colours']['rust/overlay']['dE00']} overlay"])
    bg = blend_page("cardstock-overlay-1024.webp", DEEP, "soft-light")
    add("cardstock-on-deep-plum", bg, dark_cols, "cardstock overlay (soft-light)  on  deep plum  #270617  (compare the baked deep plum)",
        [("cream", CREAM), ("blue", BLUE)],
        [f"cardstock-overlay-1024.webp, soft-light on {DEEP}: dE00 {m['on_colours']['deep-plum/soft-light']['dE00']}  "
         f"L* std {m['on_colours']['deep-plum/soft-light']['L_std']}"])

    # 3 x 3 tiling checks: the tiles as they are and with their contrast raised to expose any seam
    tiles = []
    for name, enh, note in (
        ("paper-cream-1024.webp", 1.0, "as delivered"),
        ("paper-cream-1024.webp", 6.0, "contrast x6"),
        ("paper-deep-plum-1024.webp", 8.0, "contrast x8"),
        ("paper-neutral-strong-1024.webp", 6.0, "contrast x6"),
        ("cardstock-overlay-1024.webp", 2.5, "contrast x2.5"),
        ("paper-cream-512.webp", 6.0, "contrast x6 (512 tile)"),
    ):
        im = pv.tiling_check(load(name), enh)
        key = f"tiling-{name.replace('.webp', '')}-x{enh:g}"
        strip = pv.label_strip(f"3 x 3 tiling check  /  {name}  /  {note}  /  tile boundaries at thirds")
        both = pv.stack([strip, im])
        both.save(os.path.join(PREV, f"{key}.jpg"), quality=90, subsampling=0)
        tiles.append((key, both))

    # retina: what a 2x screen shows with the recommended sizes (1024 tile at 512 CSS px = one texture
    # pixel per device pixel), text at 2x; a 1440 x 600 device-pixel crop
    for key, tile, hx, ink in (("retina-cream", "paper-cream-1024.webp", CREAM, INK),
                               ("retina-deep-plum", "paper-deep-plum-1024.webp", DEEP, CREAM)):
        bg = pv.tile_bg(load(tile), 1440, 600)
        img = Image.fromarray(bg)
        d = ImageDraw.Draw(img)
        d.text((64, 60), "Every brand hits a", font=pv.font("display", 120, 340), fill=pv.hexrgb(ink if key != "retina-cream" else PLUM))
        y = 250
        for line in pv.wrap(pv.BRAND_LINE, pv.font("text", 32, 400), 1100):
            d.text((64, y), line, font=pv.font("text", 32, 400), fill=pv.hexrgb(ink))
            y += 50
        pv.text_spaced(d, (64, 540), f"2x screen, 1:1 device px: {tile} at background-size 512px; 16 px text",
                       pv.font("mono", 22), pv.hexrgb(ink), 0.06)
        img.save(os.path.join(PREV, f"{key}.jpg"), quality=93, subsampling=0)
        panels.append((key + " (2x device-pixel crop)", img))
    # phones: the 512 tiles at background-size 256px, 2x device pixels (1:1), two 360 x 450 CSS px crops
    halves = []
    for tile, hx, head, ink in (("paper-cream-512.webp", CREAM, PLUM, INK), ("paper-deep-plum-512.webp", DEEP, CREAM, CREAM)):
        bg = pv.tile_bg(load(tile), 720, 900)
        im = Image.fromarray(bg)
        d = ImageDraw.Draw(im)
        d.text((40, 70), "Every brand", font=pv.font("display", 88, 340), fill=pv.hexrgb(head))
        d.text((40, 160), "hits a crossroads.", font=pv.font("display", 88, 340), fill=pv.hexrgb(head))
        y = 320
        for line in pv.wrap(pv.BRAND_LINE, pv.font("text", 32, 400), 640):
            d.text((40, y), line, font=pv.font("text", 32, 400), fill=pv.hexrgb(ink))
            y += 50
        pv.text_spaced(d, (40, 850), f"phone 2x: {tile} at 256px", pv.font("mono", 20), pv.hexrgb(ink), 0.04)
        halves.append(np.asarray(im))
    img = Image.fromarray(np.concatenate(halves, 1))
    img.save(os.path.join(PREV, "phone-512-tiles.jpg"), quality=93, subsampling=0)
    panels.append(("phone (2x device-pixel crops of a 390 px wide screen, 512 tiles)", img))
    edge = os.path.join(PREV, "torn-edge.jpg")
    if os.path.exists(edge):
        panels.append(("torn edge (optional)", Image.open(edge).convert("RGB")))

    blocks = []
    for key, img in panels:
        blocks.append(pv.label_strip(key))
        blocks.append(img)
    for key, img in tiles:
        blocks.append(img)
    sheet = pv.stack(blocks)
    sheet.save(os.path.join(OUT, "preview.jpg"), quality=90, subsampling=0, optimize=True)
    with open(os.path.join(OUT, "contrast.json"), "w", encoding="utf-8") as fh:
        json.dump(contrast, fh, indent=1)
    print("preview.jpg", sheet.size, f"{os.path.getsize(os.path.join(OUT, 'preview.jpg')) / 1024 / 1024:.1f} MB")


if __name__ == "__main__":
    main()
