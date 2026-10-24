"""Re-set the letter grid of studio-anokhi/word-search on Gemini's upscaled photo.

Gemini's upscale kept the photo, the grid and the circled word, but its letters are not the source's:
  * 9 of the 140 letters differ from the source (found by fitting every letter a-z to the source's ~5 px letters with
    read_wordsearch.py and checked with pixel profiles: ascenders, descenders, closed bowls, a missing middle stem);
  * they are ~13 % too large (best-fitting Arial em: 9.5-10 source px for the source, 11.0 for Gemini's) and sit
    slightly low;
  * after the global colour match they are a dim pinkish grey, while the source letters are white (on neutral black
    the source letter cores are neutral grey-white, and their contrast is ~1.45x Gemini's).
So this script keeps Gemini's photo and replaces the whole letter layer:
  1. every Gemini letter is erased by copying nearby photo texture into it (exemplar fill; letters and the circle are
     never used as a texture source);
  2. the circle around "something" keeps Gemini's shape but is recoloured to the same white;
  3. all 140 letters (the source's letters) are set in Arial (Helvetica-like, as Gemini drew them) at the source's
     size, on the source's grid (column centres and baselines fitted to the source), in white.

    python fix_wordsearch.py <aligned.png> <out.png> [--debug panel.png]
"""
from __future__ import annotations

import json
import os
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont
from scipy import ndimage, optimize

HERE = os.path.dirname(os.path.abspath(__file__))
FONT = r"C:\Windows\Fonts\arial.ttf"
SRC_W, SRC_H = 220, 262
GEM = """o x h y i a f o g j
h a n s u s e r j t
g s o m e t h i n g
d h s m n u z k q a
y s l i w d w u s b
f r m w t i r s j u
k e x v g c f h y m
a s h o e n g k n i
l y w r l u n x z o
u o m u s f j l n u
l u l d q p l o t g
l s g s w l k n k o
a w d l b u q b g r
c s o m i n g k s j""".split("\n")
GEM = [r.split() for r in GEM]
# (row, col) 1-based -> the letter the source shows where Gemini drew another
FIXES = {(1, 5): "j", (4, 4): "n", (4, 5): "m", (7, 6): "o", (8, 4): "c", (8, 7): "o", (10, 1): "q", (13, 7): "u", (13, 8): "q"}
FINAL = [row[:] for row in GEM]
for (_r, _c), _ch in FIXES.items():
    FINAL[_r - 1][_c - 1] = _ch
EM_SRC = 9.75                 # Arial em size in source px that best fits the source letters
STROKE_EM = 0.0125            # extra outline (fraction of em) that matches the weight Gemini drew (source can't tell)
WHITE = np.array([248.0, 246.0, 244.0])
SS = 4


def render(ch, size, stroke, cx, by, shape, ox=0, oy=0):
    h, w = shape
    f = ImageFont.truetype(FONT, max(1, int(round(size * SS))))
    im = Image.new("L", (w * SS, h * SS), 0)
    ImageDraw.Draw(im).text(((cx - ox) * SS, (by - oy) * SS), ch, font=f, fill=255, anchor="ms",
                            stroke_width=int(round(stroke * SS)), stroke_fill=255)
    return np.asarray(im.resize((w, h), Image.BOX), dtype=np.float64) / 255.0


def exemplar_fill(img, m, avoid, span, step=3, max_offsets=400):
    """Fill hole m from nearby texture: offsets are ranked by how well the shifted surroundings match the ring
    around the hole (after a brightness correction); each hole pixel takes the best-ranked offset whose source pixel
    is clean (not a letter, not the circle, not in the hole), so narrow gaps between letters can still be used."""
    H, W = m.shape
    ys, xs = np.where(m)
    ring = ndimage.binary_dilation(m, iterations=12) & ~m
    ry, rx = np.where(ring)
    cands = []
    for oy in range(-span, span + 1, step):
        for ox in range(-span, span + 1, step):
            if abs(ox) < 6 and abs(oy) < 6:
                continue
            ty, tx = ry + oy, rx + ox
            inb = (ty >= 0) & (ty < H) & (tx >= 0) & (tx < W)
            if inb.mean() < 0.9:
                continue
            ok = inb.copy()
            ok[inb] = ~avoid[ty[inb], tx[inb]] & ~m[ty[inb], tx[inb]]
            if ok.mean() < 0.6:
                continue
            d = img[ty[ok], tx[ok]] - img[ry[ok], rx[ok]]
            bias = d.mean(0)
            cands.append((float(((d - bias) ** 2).mean() + 0.3 * (bias ** 2).sum()), oy, ox, bias))
    cands.sort(key=lambda t: t[0])
    # each hole pixel: median of the first K clean samples from the best-ranked offsets (robust to odd samples)
    K = 5
    n = len(ys)
    stack = np.zeros((K, n, 3))
    count = np.zeros(n, int)
    used = 0
    for _, oy, ox, bias in cands[:max_offsets]:
        ty, tx = ys + oy, xs + ox
        idx = np.where((count < K) & (ty >= 0) & (ty < H) & (tx >= 0) & (tx < W))[0]
        if len(idx) == 0:
            if (count >= K).all():
                break
            continue
        clean = ~avoid[ty[idx], tx[idx]] & ~m[ty[idx], tx[idx]]
        idx = idx[clean]
        if len(idx):
            stack[count[idx], idx] = img[ty[idx], tx[idx]] - bias
            count[idx] += 1
            used += 1
        if (count >= K).all():
            break
    if (count == 0).any():
        return None
    out = img.copy()
    vals = np.empty((n, 3))
    for k in range(1, K + 1):
        sel = count == k
        if sel.any():
            vals[sel] = np.median(stack[:k, sel], axis=0)
    out[ys, xs] = vals
    return out, used


def main():
    src_path, out_path = sys.argv[1], sys.argv[2]
    debug = sys.argv[sys.argv.index("--debug") + 1] if "--debug" in sys.argv else None
    img = np.asarray(Image.open(src_path).convert("RGB"), dtype=np.float64)
    H, W = img.shape[:2]
    sx, sy = W / SRC_W, H / SRC_H
    P = json.load(open(os.path.join(HERE, "wordsearch_params.json")))
    lum = img @ np.array([0.299, 0.587, 0.114])
    sat = img.max(2) - img.min(2)

    def cell(r, c):
        return (P["x0"] + (c - 1) * P["px"]) * sx, (P["y0"] + (r - 1) * P["py"]) * sy

    letter_like = (lum > 150) & (sat < 60)
    boxes, cellmask = {}, np.zeros((H, W), bool)
    for r in range(1, 15):
        for c in range(1, 11):
            X, Y = cell(r, c)
            x0, x1 = max(0, int(X - 5.5 * sx)), min(W, int(X + 5.5 * sx))
            y0, y1 = max(0, int(Y - 9.5 * sy)), min(H, int(Y + 3.0 * sy))
            boxes[(r, c)] = (x0, y0, x1, y1)
            cellmask[y0:y1, x0:x1] = True
    colour = np.median(img[letter_like & cellmask], axis=0)
    # colour-similarity "alpha": Gemini's letters are a flat pinkish white; the wheel's bluish streaks and the
    # skin are not, so they stay out of the letter masks
    dist = np.sqrt(((img - colour) ** 2).sum(2))
    acol = np.clip((90.0 - dist) / 70.0, 0, 1)

    # 1. locate each of Gemini's letters exactly: its own letter in Arial (size/weight fitted earlier: em 95.1 px,
    #    +1.19 px outline) fitted to the colour map; the erase mask is that glyph, slightly grown
    GSIZE, GSTROKE = 95.12, 1.19
    holes = {}
    for (r, c), (x0, y0, x1, y1) in boxes.items():
        X, Y = cell(r, c)
        bx0, by0, bx1, by1 = max(0, x0 - 20), max(0, y0 - 20), min(W, x1 + 20), min(H, y1 + 20)
        tgt = acol[by0:by1, bx0:bx1]
        ch = GEM[r - 1][c - 1]
        def cost(p):
            g = render(ch, GSIZE, GSTROKE, X + p[0], Y + p[1], tgt.shape, bx0, by0)
            return ((g - tgt) ** 2).sum()
        best = min((cost((dx, dy)), dx, dy) for dx in np.arange(-8, 8.1, 2) for dy in np.arange(-4, 12.1, 2))
        x0_ = np.array([best[1], best[2]])
        res = optimize.minimize(cost, x0_, method="Nelder-Mead",
                                options=dict(xatol=0.2, fatol=1e-2, maxiter=60, initial_simplex=np.array([x0_, x0_ + [1.5, 0], x0_ + [0, 1.5]])))
        g = render(ch, GSIZE, GSTROKE, X + res.x[0], Y + res.x[1], tgt.shape, bx0, by0)
        core = g > 0.03
        m = np.zeros((H, W), bool)
        m[by0:by1, bx0:bx1] = ndimage.binary_dilation(core, iterations=3) | (
            (dist[by0:by1, bx0:bx1] < 55) & ndimage.binary_dilation(core, iterations=8))
        holes[(r, c)] = m
    allholes = np.zeros((H, W), bool)
    for m in holes.values():
        allholes |= m

    # the circle around "something": letter-coloured line work outside the letters, between rows 2 and 4
    _, y2 = cell(2, 1)
    _, y4 = cell(4, 1)
    band = np.zeros((H, W), bool)
    band[int(y2 + 2.5 * sy):int(y4 - 7.0 * sy), :] = True
    circle = band & (acol > 0.02) & ~ndimage.binary_dilation(allholes, iterations=2)
    circle = ndimage.binary_opening(circle, iterations=1) | (circle & (acol > 0.5))

    out = img.copy()
    avoid = ndimage.binary_dilation(allholes | circle, iterations=4)
    fills = 0
    for (r, c), m in holes.items():
        m = m & ~ndimage.binary_dilation(circle, iterations=3)
        if not m.any():
            continue
        res = exemplar_fill(out, m, avoid, int(12 * sx))
        if res is None:                                   # fallback: smooth fill from the surroundings
            vv = (~m & ~avoid).astype(float)
            filled = out.copy()
            dd = ndimage.gaussian_filter(vv, 1.5 * sx)
            for ch in range(3):
                filled[..., ch] = np.where(m, ndimage.gaussian_filter(out[..., ch] * vv, 1.5 * sx) / np.maximum(dd, 1e-6), out[..., ch])
            print("fallback fill at", (r, c))
        else:
            filled, _ = res
        soft = np.clip(ndimage.gaussian_filter(m.astype(float), 1.5) * 1.6, 0, 1)[..., None]
        ys, xs = np.where(ndimage.binary_dilation(m, iterations=int(sx)))
        Y0, Y1, X0, X1 = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
        out[Y0:Y1, X0:X1] = soft[Y0:Y1, X0:X1] * filled[Y0:Y1, X0:X1] + (1 - soft[Y0:Y1, X0:X1]) * out[Y0:Y1, X0:X1]
        fills += 1
    # 2. the circle in white (shape kept)
    ca = (acol * circle)[..., None]
    out = out + ca * (WHITE - colour)
    # 3. the source's letters, source size and grid, white
    size = EM_SRC * sx
    stroke = STROKE_EM * size
    for r in range(1, 15):
        for c in range(1, 11):
            X, Y = cell(r, c)
            x0, y0 = max(0, int(X - 6 * sx)), max(0, int(Y - 10 * sy))
            x1, y1 = min(W, int(X + 6 * sx)), min(H, int(Y + 4 * sy))
            cov = render(FINAL[r - 1][c - 1], size, stroke, X, Y, (y1 - y0, x1 - x0), x0, y0)
            cov = ndimage.gaussian_filter(cov, 0.6)[..., None]
            out[y0:y1, x0:x1] = cov * WHITE + (1 - cov) * out[y0:y1, x0:x1]
    Image.fromarray(np.clip(out, 0, 255).astype(np.uint8)).save(out_path)
    print(json.dumps({"gemini_letter_colour": colour.round(1).tolist(), "letters_erased": fills, "em_px": round(size, 2),
                      "stroke_px": round(stroke, 2), "circle_px": int(circle.sum()), "letters": [" ".join(r) for r in FINAL]}))
    if debug:
        crops = []
        for r0 in (1, 4, 8, 13):
            _, Ya = cell(r0, 1)
            y0, y1 = max(0, int(Ya - 10 * sy)), min(H, int(Ya + 24 * sy))
            a = Image.fromarray(img[y0:y1].astype(np.uint8)); b = Image.fromarray(np.clip(out[y0:y1], 0, 255).astype(np.uint8))
            crops += [a, b]
        tw = crops[0].width
        panel = Image.new("RGB", (tw, sum(cr.height + 6 for cr in crops)), (255, 255, 255))
        yy = 0
        for cr in crops:
            panel.paste(cr, (0, yy)); yy += cr.height + 6
        panel.resize((panel.width // 2, panel.height // 2), Image.LANCZOS).save(debug)


if __name__ == "__main__":
    main()
