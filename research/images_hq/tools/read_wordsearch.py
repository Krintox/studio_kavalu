"""Read the 10 x 14 letter grid of studio-anokhi/word-search from the tiny source by hypothesis scoring.

Each letter is about 5 px tall in the 220x262 source, so it cannot be read by eye with certainty. For every cell and
every lowercase letter a-z, the letter is rendered (supersampled, box-reduced, Gaussian-blurred to the source's
softness) at the cell's grid position and fitted to the source pixels together with a smooth background
(per channel: c0 + c1*dx + c2*dy + k*glyph). The letter with the smallest residual wins; the margin to the runner-up
says how sure the reading is. Global parameters (font, size, baseline, blur) are fitted first on the circled word
"something" (row 3, columns 2-10), whose letters are known.

    python read_wordsearch.py [image]      # default: the source; pass a downscaled candidate to read its letters

Writes tools/wordsearch_read.json (or prints only, for a non-default image).
"""
from __future__ import annotations

import json
import os
import string
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont
from scipy import ndimage

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC = os.path.join(ROOT, "website", "public", "work", "studio-anokhi", "word-search.jpg")
FONTDIR = r"C:\Windows\Fonts"
FONTS = {
    "arial": "arial.ttf", "century-gothic": "GOTHIC.TTF", "verdana": "verdana.ttf", "tahoma": "tahoma.ttf",
    "segoe-ui": "segoeui.ttf", "segoe-ui-light": "segoeuil.ttf", "calibri": "calibri.ttf", "trebuchet": "trebuc.ttf",
    "gill-sans": "GIL_____.TTF", "franklin": "framd.ttf", "corbel": "corbel.ttf", "candara": "Candara.ttf",
    "bahnschrift": "bahnschrift.ttf", "lucida-sans": "l_10646.ttf",
}
SS = 8                      # supersampling of the glyph renders
NCOL, NROW = 10, 14
LETTERS = string.ascii_lowercase
KNOWN = {(2, c): ch for c, ch in zip(range(1, 10), "something")}     # (row, col) zero-based


def glyph_hr(fontfile, em, ch, cache={}):
    key = (fontfile, round(em * SS), ch)
    if key not in cache:
        f = ImageFont.truetype(os.path.join(FONTDIR, fontfile), round(em * SS))
        W = H = int(4 * em * SS)
        im = Image.new("L", (W, H), 0)
        ImageDraw.Draw(im).text((W / 2, H * 0.65), ch, font=f, fill=255, anchor="ms")
        cache[key] = (np.asarray(im, dtype=np.float32) / 255.0, W / 2, H * 0.65)
    return cache[key]


def place(fontfile, em, ch, X, Y, win, sigma):
    """Coverage of letter ch with its advance centre at source x=X and baseline at y=Y, sampled on window
    win=(x0, y0, w, h) of source pixels, blurred by sigma (source px)."""
    g, ax, ay = glyph_hr(fontfile, em, ch)
    x0, y0, w, h = win
    pad = 3
    canvas = np.zeros(((h + 2 * pad) * SS, (w + 2 * pad) * SS), np.float32)
    # glyph pixel (u, v) -> source x = X + (u + .5 - ax)/SS ; canvas pixel = (x - (x0 - pad)) * SS - .5
    ox = int(round((X - (x0 - pad)) * SS - ax))
    oy = int(round((Y - (y0 - pad)) * SS - ay))
    H, W = g.shape
    cy0, cx0 = max(0, oy), max(0, ox)
    cy1, cx1 = min(canvas.shape[0], oy + H), min(canvas.shape[1], ox + W)
    if cy1 > cy0 and cx1 > cx0:
        canvas[cy0:cy1, cx0:cx1] = g[cy0 - oy:cy1 - oy, cx0 - ox:cx1 - ox]
    small = canvas.reshape(h + 2 * pad, SS, w + 2 * pad, SS).mean((1, 3))
    if sigma > 0:
        small = ndimage.gaussian_filter(small, sigma)
    return small[pad:pad + h, pad:pad + w]


def fit_cell(img, win, glyph):
    """Least-squares fit of the luminance to a background ramp + k*glyph; returns SSE and k."""
    x0, y0, w, h = win
    sub = img[y0:y0 + h, x0:x0 + w].reshape(-1, img.shape[2])
    yy, xx = np.mgrid[0:h, 0:w]
    A = np.c_[np.ones(h * w), (xx.ravel() - w / 2) / w, (yy.ravel() - h / 2) / h, glyph.ravel()]
    coef, res, rank, _ = np.linalg.lstsq(A, sub, rcond=None)
    pred = A @ coef
    sse = float(((sub - pred) ** 2).sum())
    return sse, float(coef[3].mean())


def background_sse(img, win):
    x0, y0, w, h = win
    sub = img[y0:y0 + h, x0:x0 + w].reshape(-1, img.shape[2])
    yy, xx = np.mgrid[0:h, 0:w]
    A = np.c_[np.ones(h * w), (xx.ravel() - w / 2) / w, (yy.ravel() - h / 2) / h]
    coef, *_ = np.linalg.lstsq(A, sub, rcond=None)
    return float(((sub - A @ coef) ** 2).sum())


def cell_geom(P, r, c):
    X = P["X"][c] if "X" in P else P["x0"] + c * P["px"]
    Y = P["Y"][r] if "Y" in P else P["y0"] + r * P["py"]           # baseline
    win = (int(round(X)) - 7, int(round(Y)) - 9, 14, 13)
    return X, Y, win


def best_letter(img, P, r, c, letters, shifts):
    X, Y, win = cell_geom(P, r, c)
    x0, y0, w, h = win
    H, W = img.shape[:2]
    if x0 < 0 or y0 < 0 or x0 + w > W or y0 + h > H:      # clip the window at the image edge
        nx0, ny0 = max(0, x0), max(0, y0)
        w, h = min(W, x0 + w) - nx0, min(H, y0 + h) - ny0
        win = (nx0, ny0, w, h)
    out = {}
    for ch in letters:
        best = None
        for dx in shifts:
            for dy in shifts:
                g = place(P["font"], P["em"], ch, X + dx, Y + dy, win, P["sigma"])
                sse, k = fit_cell(img, win, g)
                if k <= 0:
                    sse = background_sse(img, win)
                if best is None or sse < best[0]:
                    best = (sse, k, dx, dy)
        out[ch] = best
    return out, background_sse(img, win)


def fit_globals(img):
    """Pick font / em / sigma / grid on the known letters."""
    # grid from the letter-ness profiles (centres of the x-height band); baseline sits below the centre
    base = dict(x0=22.0, px=19.2, yc0=5.0, py=19.1)
    results = []
    fonts = [f for f in FONTS.values() if f in os.environ.get("WS_FONTS", ",".join(FONTS.values())).split(",")]
    for font in fonts:
        for em in np.arange(7.0, 11.01, 0.5):
            for sigma in (0.8, 1.0, 1.2, 1.4):
                for boff in (1.5, 2.0, 2.5, 3.0):
                    P = dict(font=font, em=float(em), sigma=sigma, x0=base["x0"], px=base["px"], y0=base["yc0"] + boff, py=base["py"])
                    tot = 0.0
                    for (r, c), ch in KNOWN.items():
                        o, bg = best_letter(img, P, r, c, ch, (-0.5, 0.0, 0.5))
                        tot += o[ch][0] / bg
                    results.append((tot, font, float(em), sigma, boff))
        best = min(r for r in results if r[1] == font)
        print("  %-16s best rel-SSE %.3f em %.1f sigma %.1f baseline+%.1f" % (font, best[0], best[2], best[3], best[4]), flush=True)
    results.sort()
    tot, font, em, sigma, boff = results[0]
    P = dict(font=font, em=em, sigma=sigma, x0=base["x0"], px=base["px"], y0=base["yc0"] + boff, py=base["py"])
    # refine the grid (x0, px, y0, py) on the known letters with the chosen font
    def cost(v):
        Q = dict(P, x0=v[0], px=v[1], y0=v[2], py=v[3])
        t = 0.0
        for (r, c), ch in KNOWN.items():
            o, bg = best_letter(img, Q, r, c, ch, (0.0,))
            t += o[ch][0] / bg
        return t
    from scipy.optimize import minimize
    r = minimize(cost, [P["x0"], P["px"], P["y0"], P["py"]], method="Nelder-Mead", options=dict(xatol=0.02, fatol=1e-4, maxiter=400))
    P.update(x0=float(r.x[0]), px=float(r.x[1]), y0=float(r.x[2]), py=float(r.x[3]))
    return P


def fit_grid(img, P, letters=LETTERS):
    """Letter-agnostic grid: each row's baseline and each column's centre is chosen where the best-fitting letter of
    every cell fits best (sum over the row / column), then a straight line is fitted through them (the grid is regular)."""
    from scipy.optimize import minimize_scalar
    def tot(Q, cells):
        t = 0.0
        for r, c in cells:
            o, bg = best_letter(img, Q, r, c, letters, (0.0,))
            t += min(v[0] for v in o.values()) / bg
        return t
    base = dict(P)
    Ys, Xs = [], []
    for r in range(NROW):
        y0 = base["y0"] + r * base["py"]
        offs = np.arange(-1.5, 1.51, 0.25)
        sc = [tot(dict(base, Y=[y0 + d] * NROW), [(r, c) for c in range(NCOL)]) for d in offs]
        Ys.append(y0 + offs[int(np.argmin(sc))])
    for c in range(NCOL):
        x0 = base["x0"] + c * base["px"]
        offs = np.arange(-1.5, 1.51, 0.25)
        sc = [tot(dict(base, Y=Ys, X=[x0 + d] * NCOL), [(r, c) for r in range(NROW)]) for d in offs]
        Xs.append(x0 + offs[int(np.argmin(sc))])
    ry = np.polyfit(np.arange(NROW), Ys, 1); rx = np.polyfit(np.arange(NCOL), Xs, 1)
    print("  row baselines:", np.round(Ys, 2).tolist(), "-> pitch %.3f" % ry[0])
    print("  col centres:  ", np.round(Xs, 2).tolist(), "-> pitch %.3f" % rx[0])
    return dict(P, x0=float(rx[1]), px=float(rx[0]), y0=float(ry[1]), py=float(ry[0]))


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else SRC
    im = Image.open(path).convert("RGB")
    if im.size != (220, 262):
        im = im.resize((220, 262), Image.LANCZOS)
    img = np.asarray(im, dtype=np.float64)
    img = (img @ np.array([0.299, 0.587, 0.114]))[..., None]          # luminance only
    pfile = os.path.join(HERE, "wordsearch_params.json")
    if path == SRC or not os.path.exists(pfile):
        P = fit_globals(img)
    else:
        P = json.load(open(pfile))
    P = fit_grid(img, P)
    if path == SRC:
        json.dump(P, open(pfile, "w"), indent=1)
    print("params:", json.dumps(P), flush=True)
    grid, rows = [], []
    for r in range(NROW):
        row = []
        for c in range(NCOL):
            o, bg = best_letter(img, P, r, c, LETTERS, (-0.5, -0.25, 0.0, 0.25, 0.5))
            ranked = sorted(o.items(), key=lambda kv: kv[1][0])
            (b1, v1), (b2, v2), (b3, v3) = ranked[:3]
            row.append(dict(r=r, c=c, best=b1, second=b2, third=b3, rel1=v1[0] / bg, rel2=v2[0] / bg, rel3=v3[0] / bg,
                            margin=(v2[0] - v1[0]) / bg, k=v1[1], dx=v1[2], dy=v1[3]))
        grid.append(row)
        rows.append(" ".join(x["best"] for x in row))
        print("row %2d: %s   | margins %s" % (r + 1, rows[-1], " ".join("%s%.2f" % (x["second"], x["margin"]) for x in row)), flush=True)
    if path == SRC:
        json.dump(dict(params=P, rows=rows, cells=grid), open(os.path.join(HERE, "wordsearch_read.json"), "w"), indent=1)


if __name__ == "__main__":
    main()
