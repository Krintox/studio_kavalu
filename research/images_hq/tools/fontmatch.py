"""Rank candidate fonts against a word in a source image.

Each candidate (Google Fonts family + weight, optionally letter-spacing, or a local font) is rendered black on white
in our render tab; only faces that actually loaded are scored (no faux bold: font-synthesis is off). The word's ink
box is cropped, resized to the target word's ink box, lightly blurred like the source, and scored by normalised
cross-correlation with the target alpha (0..1). Used so recreations use the real letterforms, not a stand-in.
"""
from __future__ import annotations

import os
import re
import urllib.parse

import numpy as np
from PIL import Image, ImageDraw
from scipy import ndimage

import render

HERE = os.path.dirname(os.path.abspath(__file__))
WORKDIR = os.path.join(HERE, "_fontmatch")
os.makedirs(WORKDIR, exist_ok=True)

FACES_JS = """(async () => { await document.fonts.ready; await new Promise(r => setTimeout(r, 300));
  return [...document.fonts].map(f => [f.family.replace(/["']/g, ''), f.weight, f.style, f.status]); })()"""


def ink_box(a: np.ndarray, thr: float = 0.35):
    ys, xs = np.where(a > thr)
    return xs.min(), ys.min(), xs.max() + 1, ys.max() + 1


def gf_links(cands: list[dict]) -> str:
    out = []
    cands = [c for c in cands if c.get("family") and not str(c["family"]).startswith(("Arial", "L "))]
    fs = sorted({(c["fs"], c.get("weight", 400)) for c in cands if c.get("fs")})
    for slug, w in fs:
        out.append('<link rel="stylesheet" href="https://api.fontshare.com/v2/css?f[]=%s@%s&display=block">' % (slug, w))
    for fam, w in sorted({(c["family"], c.get("weight", 400)) for c in cands if not c.get("local") and not c.get("fs")}):
        q = urllib.parse.quote(fam).replace("%20", "+")
        out.append('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=%s:wght@%s&display=block">' % (q, w))
    return "".join(out)


def local_faces(cands: list[dict]) -> str:
    css = []
    for c in cands:
        if c.get("local"):
            url = "file:///" + c["local"].replace("\\", "/")
            css.append("@font-face{font-family:'%s';src:url('%s');font-weight:%s;}" % (c["family"], url, c.get("weight", 400)))
    return "".join(css)


def render_candidates(text: str, cands: list[dict], size: int = 120, batch: int = 36):
    """Return [(cand, ink array of its cell)] for candidates whose face loaded."""
    cell_h = int(size * 1.9)
    W = int(size * max(4, len(text) * 1.1))
    res = []
    for b0 in range(0, len(cands), batch):
        chunk = cands[b0:b0 + batch]
        rows = []
        for i, c in enumerate(chunk):
            style = "top:%dpx;font-family:'%s','Fallback Nope';font-weight:%s;letter-spacing:%sem;font-style:%s" % (
                i * cell_h, c["family"], c.get("weight", 400), c.get("ls", 0), c.get("style", "normal"))
            rows.append('<div class="c" style="%s">%s</div>' % (style, text))
        Hh = cell_h * len(chunk)
        html = ('<!doctype html><html><head><meta charset="utf-8">%s<style>%s html,body{margin:0;background:#fff}'
                '.c{position:absolute;left:%dpx;height:%dpx;line-height:%dpx;font-size:%dpx;color:#000;white-space:nowrap;'
                'font-kerning:normal;font-synthesis:none}</style></head><body style="width:%dpx;height:%dpx">%s</body></html>') % (
            gf_links(chunk), local_faces(chunk), size // 3, cell_h, cell_h, size, W, Hh, "".join(rows))
        hp = os.path.join(WORKDIR, "cands_%04d.html" % b0)
        open(hp, "w", encoding="utf-8").write(html)
        out = hp.replace(".html", ".png")
        _, faces = render.render(hp, out, W, Hh, 1, settle=1.0, js=FACES_JS)
        loaded = {(f[0], str(f[1])) for f in faces if f[3] == "loaded"}
        g = np.asarray(Image.open(out).convert("L")).astype(float) / 255.0
        for i, c in enumerate(chunk):
            if c.get("local") or (c["family"], str(c.get("weight", 400))) in loaded:
                res.append((c, 1.0 - g[i * cell_h:(i + 1) * cell_h, :]))
    return res


def score(target: np.ndarray, cell: np.ndarray, blur: float = 0.6):
    if cell.max() < 0.3:
        return -1.0, None
    x0, y0, x1, y1 = ink_box(cell, 0.5)
    crop = cell[y0:y1, x0:x1]
    th, tw = target.shape
    c = np.asarray(Image.fromarray((crop * 255).astype(np.uint8)).resize((tw, th), Image.LANCZOS)).astype(float) / 255.0
    c = ndimage.gaussian_filter(c, blur)
    a = target - target.mean()
    b = c - c.mean()
    return float((a * b).sum() / np.sqrt((a * a).sum() * (b * b).sum())), c


def rank(target: np.ndarray, text: str, cands: list[dict], top_sheet: str | None = None, n_show: int = 8):
    scored = []
    for c, cell in render_candidates(text, cands):
        s, img = score(target, cell)
        scored.append((s, c, img))
    scored.sort(key=lambda t: -t[0])
    if top_sheet:
        th, tw = target.shape
        k = max(1, int(round(120 / max(th, 1))))
        rows = [("target", target)] + [("%.4f %s %s ls%s" % (s, c["family"], c.get("weight", 400), c.get("ls", 0)), img)
                                       for s, c, img in scored[:n_show] if img is not None]
        sheet = Image.new("L", (tw * k + 20, (th * k + 30) * len(rows)), 255)
        d = ImageDraw.Draw(sheet)
        for i, (lab, img) in enumerate(rows):
            y = i * (th * k + 30)
            d.text((10, y + 2), lab, fill=0)
            sheet.paste(Image.fromarray((255 - img * 255).clip(0, 255).astype(np.uint8)).resize((tw * k, th * k), Image.LANCZOS),
                        (10, y + 20))
        sheet.save(top_sheet)
    return scored


def text_metrics(items: list[dict], size: int = 100) -> list[dict]:
    """items: [{family, weight, ls, html, fs?}] -> ink box of each, relative to x=10 / baseline=1.5*size, at `size` px.
    Lets a recreation place SVG <text> so its ink lands exactly on a measured ink box in the source."""
    cell = int(size * 2.2)
    base = int(size * 1.5)
    W = int(size * 40)
    blocks = []
    for i, it in enumerate(items):
        blocks.append('<svg style="position:absolute;left:0;top:%dpx" width="%d" height="%d"><text x="10" y="%d" '
                      'font-family="%s" font-weight="%s" font-size="%d" letter-spacing="%sem" fill="#000">%s</text></svg>'
                      % (i * cell, W, cell, base, it["family"], it.get("weight", 400), size, it.get("ls", 0), it["html"]))
    ws = set()
    for it in items:
        ws.add((it["family"], it.get("weight", 400), it.get("fs")))
        for w in re.findall(r'font-weight="(\d+)"', it["html"]):
            ws.add((it["family"], int(w), it.get("fs")))
    links = gf_links([{"family": f, "weight": w, "fs": fs} for f, w, fs in ws])
    html = ('<!doctype html><html><head><meta charset="utf-8">%s<style>html,body{margin:0;background:#fff}</style></head>'
            '<body style="width:%dpx;height:%dpx">%s</body></html>') % (links, W, cell * len(items), "".join(blocks))
    hp = os.path.join(WORKDIR, "metrics.html")
    open(hp, "w", encoding="utf-8").write(html)
    out = hp.replace(".html", ".png")
    render.render(hp, out, W, cell * len(items), 1, settle=1.2)
    g = 1 - np.asarray(Image.open(out).convert("L")).astype(float) / 255
    res = []
    for i, it in enumerate(items):
        x0, y0, x1, y1 = ink_box(g[i * cell:(i + 1) * cell], 0.5)
        res.append({**it, "size": size, "ink_left": x0 - 10, "ink_right": x1 - 10, "ink_top": y0 - base, "ink_bottom": y1 - base})
    return res


def place(m: dict, box: tuple[float, float, float, float]) -> dict:
    """Given text_metrics() output and a target ink box (x0, top, x1, bottom) in source px, return SVG placement:
    font_size, x, baseline y and vertical stretch k (apply as transform scale(1 k) with y/k)."""
    x0, top, x1, bottom = box
    sx = (x1 - x0) / (m["ink_right"] - m["ink_left"])
    sy = (bottom - top) / (m["ink_bottom"] - m["ink_top"])
    fs = m["size"] * sx
    k = sy / sx
    x = x0 - m["ink_left"] * sx
    baseline = top - m["ink_top"] * sy
    return {"font_size": fs, "x": x, "baseline": baseline, "k": k}
