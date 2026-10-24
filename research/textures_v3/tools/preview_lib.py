"""Preview helpers: render a texture as a 1440 x 900 page background with the site's own type
(Gambetta, Switzer, Courier Prime from website/src/fonts), a 2x loupe over the body text, and
3 x 3 tiling checks."""
from __future__ import annotations

import os

import numpy as np
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.abspath(os.path.join(HERE, "..", "..", "..", "website", "src", "fonts"))

W, H = 1440, 900


def font(name, size, weight=None):
    path = {
        "display": "Gambetta-Variable.woff2",
        "display-italic": "Gambetta-VariableItalic.woff2",
        "text": "Switzer-Variable.woff2",
        "mono": "CourierPrime-Regular.woff2",
    }[name]
    f = ImageFont.truetype(os.path.join(FONTS, path), size)
    if weight is not None:
        try:
            f.set_variation_by_axes([weight])
        except Exception:
            pass
    return f


def tile_bg(tile: np.ndarray, w=W, h=H, ox=0, oy=0) -> np.ndarray:
    """Repeat a tile over w x h starting at offset (ox, oy) inside the tile."""
    th, tw = tile.shape[:2]
    reps_y = (h + oy) // th + 2
    reps_x = (w + ox) // tw + 2
    big = np.tile(tile, (reps_y, reps_x, 1) if tile.ndim == 3 else (reps_y, reps_x))
    return big[oy : oy + h, ox : ox + w]


def hexrgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i : i + 2], 16) for i in (0, 2, 4))


def text_spaced(draw, xy, s, f, fill, tracking=0.0):
    x, y = xy
    for ch in s:
        draw.text((x, y), ch, font=f, fill=fill)
        x += f.getlength(ch) + tracking * f.size
    return x


def wrap(text, f, width):
    words = text.split()
    lines, cur = [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if f.getlength(t) <= width:
            cur = t
        else:
            lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


BRAND_LINE = (
    "A brand is a set of choices; what it says, how it looks, where it shows up, who it speaks to. "
    "Studio Kavalu is a branding and content house that makes these choices with you. We shape "
    "brands, feeds and persona through a design lens backed with strategy."
)
BRAND_AIM = (
    "The aim- work with a point of view clear enough that people recognise it, and others follow "
    "it. Every project begins with a conversation and a brief we read properly, then a road we "
    "choose together."
)


def panel(bg: np.ndarray, c: dict, label: str, info: list[str], loupe=True) -> Image.Image:
    """bg: (H, W, 3) uint8 page background. c: colours {heading, body, soft, accent}."""
    img = Image.fromarray(bg.astype(np.uint8), "RGB")
    d = ImageDraw.Draw(img)
    mono = font("mono", 13)
    eyebrow_col = hexrgb(c.get("soft", c["body"]))
    text_spaced(d, (72, 64), label.upper(), mono, eyebrow_col, 0.08)

    h1 = font("display", 84, 340)
    h1i = font("display-italic", 84, 300)
    y = 140
    x = 68
    d.text((x, y), "Every brand hits a", font=h1, fill=hexrgb(c["heading"]))
    y += 90
    xi = x
    d.text((xi, y), "crossroads.", font=h1i, fill=hexrgb(c.get("accent", c["heading"])))
    xi += h1i.getlength("crossroads. ")
    d.text((xi, y), "We help", font=h1, fill=hexrgb(c["heading"]))
    y += 90
    d.text((x, y), "you choose the road.", font=h1, fill=hexrgb(c["heading"]))

    body = font("text", 16, 400)
    lh = 25  # 16 px at line-height ~1.55
    y0 = 490
    for i, para in enumerate((BRAND_LINE, BRAND_AIM)):
        xx = 72 + i * 540
        yy = y0
        for line in wrap(para, body, 460):
            d.text((xx, yy), line, font=body, fill=hexrgb(c["body"]))
            yy += lh

    small = font("text", 15, 450)
    d.text((72, 680), "Start a project", font=small, fill=hexrgb(c["heading"]))
    ax = 72 + small.getlength("Start a project") + 10
    ay = 691
    d.line((ax, ay, ax + 16, ay), fill=hexrgb(c["heading"]), width=1)
    d.line((ax + 11, ay - 4, ax + 16, ay), fill=hexrgb(c["heading"]), width=1)
    d.line((ax + 11, ay + 4, ax + 16, ay), fill=hexrgb(c["heading"]), width=1)
    d.text((270, 680), "See the work", font=small, fill=hexrgb(c["heading"]))
    text_spaced(d, (72, 740), "FIG. 10  NIVRITTI  —  BENGALURU 19:46 IST", mono, eyebrow_col, 0.08)

    info_f = font("mono", 12)
    yy = H - 26 - 16 * len(info)
    for line in info:
        text_spaced(d, (72, yy), line, info_f, eyebrow_col, 0.02)
        yy += 16

    if loupe:
        # a 2x loupe over a patch of 16 px body text, framed, at the top right
        sx, sy, sw, sh = 72, y0 - 4, 210, 104
        crop = img.crop((sx, sy, sx + sw, sy + sh)).resize((sw * 2, sh * 2), Image.NEAREST)
        lx, ly = W - 72 - sw * 2, 140
        img.paste(crop, (lx, ly))
        d.rectangle((lx - 1, ly - 1, lx + sw * 2, ly + sh * 2), outline=eyebrow_col, width=1)
        text_spaced(d, (lx, ly + sh * 2 + 10), "2x loupe: 16 px body text on the paper", font("mono", 11), eyebrow_col, 0.06)
    return img


def tiling_check(tile: np.ndarray, enhance=1.0, out_w=1440) -> Image.Image:
    """3 x 3 repeat of a tile, optionally contrast-enhanced around its mean, scaled to out_w."""
    t = tile.astype(float)
    if enhance != 1.0:
        m = t.reshape(-1, t.shape[-1]).mean(0) if t.ndim == 3 else t.mean()
        t = np.clip(m + (t - m) * enhance, 0, 255)
    big = np.tile(t, (3, 3, 1) if t.ndim == 3 else (3, 3)).astype(np.uint8)
    im = Image.fromarray(big)
    if im.mode != "RGB":
        im = im.convert("RGB")
    s = out_w / im.width
    return im.resize((out_w, int(round(im.height * s))), Image.LANCZOS)


def label_strip(text, w=W, h=56, bg=(36, 19, 25), fg=(243, 243, 231)):
    im = Image.new("RGB", (w, h), bg)
    d = ImageDraw.Draw(im)
    text_spaced(d, (24, 20), text.upper(), font("mono", 14), fg, 0.08)
    return im


def stack(images, gap=0, bg=(36, 19, 25)):
    w = max(i.width for i in images)
    h = sum(i.height for i in images) + gap * (len(images) - 1)
    out = Image.new("RGB", (w, h), bg)
    y = 0
    for i in images:
        out.paste(i, (0, y))
        y += i.height + gap
    return out
