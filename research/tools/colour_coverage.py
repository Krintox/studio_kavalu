"""colour_coverage.py - how much of a page each palette colour covers (queue item Q24).

Written for research/COLOUR_PROPORTION.md (section 6). Reads screenshots; never touches the site.

usage:
  python -I colour_coverage.py [--masks masks.json] [--scale 2] [--viewport 900] [--de 12]
                               [--strip strip.png] [--json out.json] SHOT [SHOT ...]

SHOT is a full-page screenshot of one page (several SHOTs are pooled: pass all pages of one
iteration to get the site figure, or one page at a time). Every 4x4 block of pixels (which removes
the paper grain) is matched to the nearest site token in CIELAB; a block further than --de from every
token is "unassigned" (photos, project colours, or a colour that should not be there). Families:
  plum    = plum, deep plum, ink, ink-soft, ink-faint, the blue-ground soft inks, photo corners
  blue    = powder blue, pale blue, tape on cream
  cream   = cream, cream-2, cream-3, paper, paper-note
  oxblood = oxblood, rust
  project = each project's tone.bg (project inks are left out on purpose: Nivritti's #EFE9DA is
            dE 1.5 from cream-2 and would steal cream). Use masks for exact project areas.

masks.json (optional; strongly recommended) holds page rectangles in CSS px, per shot file name:
  {"home-1440.png": {"photo": [[x, y, w, h], ...], "project": [[x, y, w, h], ...]}}
Collect them in the same browser session as the screenshot, at scroll 0, with:
  JSON.stringify({
    photo: [...document.querySelectorAll('img, video, canvas, picture')]
      .map(e => e.getBoundingClientRect()).filter(r => r.width * r.height > 400)
      .map(r => [r.left + scrollX, r.top + scrollY, r.width, r.height].map(Math.round)),
    project: [...document.querySelectorAll('[style*="--p-bg"]')]
      .map(e => e.getBoundingClientRect())
      .map(r => [r.left + scrollX, r.top + scrollY, r.width, r.height].map(Math.round)),
  })
Photo rectangles leave the denominator; project rectangles are counted as "project".

Output: each family's share of the non-photo area; plum+blue as a share of the palette area (the
Q24 target: photos and project colours excluded); the ground switches (a run of one dominant family
must last half a viewport to count); and optionally a scroll strip PNG (one row per 40 CSS px,
coloured by that band's dominant family; white = photo).
"""
import argparse
import json
import os

import numpy as np
from PIL import Image

TOKENS = {
    'plum': ['#390D26', '#270617', '#241319', '#5D4A50', '#6D5F62', '#50334A', '#5E4A5E', '#24131A'],
    'blue': ['#ABCDD6', '#C9DFE5', '#C4DADC'],
    'cream': ['#F3F3E7', '#ECEADB', '#E3E0CD', '#FBFAF2', '#F8F5E8'],
    'oxblood': ['#491C17', '#51201B'],
    'project': ['#9F4A30', '#07253D', '#A11F5B', '#3F1B0E', '#A32D02'],
}
FAMILIES = ['plum', 'blue', 'cream', 'oxblood', 'project', 'unassigned']
SWATCH = {'plum': (57, 13, 38), 'blue': (171, 205, 214), 'cream': (243, 243, 231), 'oxblood': (73, 28, 23),
          'project': (159, 74, 48), 'unassigned': (128, 128, 128), 'photo': (255, 255, 255)}


def to_lab(rgb):
    c = rgb / 255.0
    lin = np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    m = np.array([[0.4124564, 0.3575761, 0.1804375], [0.2126729, 0.7151522, 0.0721750],
                  [0.0193339, 0.1191920, 0.9503041]])
    t = (lin @ m.T) / np.array([0.95047, 1.0, 1.08883])
    d = 6 / 29
    f = np.where(t > d ** 3, np.cbrt(t), t / (3 * d * d) + 4 / 29)
    return np.stack([116 * f[..., 1] - 16, 500 * (f[..., 0] - f[..., 1]), 200 * (f[..., 1] - f[..., 2])], -1)


def hexlab(h):
    return to_lab(np.array([[int(h[i:i + 2], 16) for i in (1, 3, 5)]], dtype=float))[0]


def classify(img, de):
    a = np.asarray(img.convert('RGB'), dtype=float)
    h, w = (a.shape[0] // 4) * 4, (a.shape[1] // 4) * 4
    a = a[:h, :w].reshape(h // 4, 4, w // 4, 4, 3).mean((1, 3))
    lab = to_lab(a)
    labs, fams = [], []
    for fam, hexes in TOKENS.items():
        for hx in hexes:
            labs.append(hexlab(hx))
            fams.append(FAMILIES.index(fam))
    labs = np.array(labs)
    out = np.empty(lab.shape[:2], dtype=int)
    for y0 in range(0, lab.shape[0], 256):  # in slices, so a 20,000 px page stays light on memory
        d = np.sqrt(((lab[y0:y0 + 256, :, None, :] - labs[None, None]) ** 2).sum(-1))
        f = np.array(fams)[d.argmin(-1)]
        f[d.min(-1) > de] = FAMILIES.index('unassigned')
        out[y0:y0 + 256] = f
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('shots', nargs='+')
    ap.add_argument('--masks')
    ap.add_argument('--scale', type=float, default=1.0, help='screenshot pixels per CSS px (DPR)')
    ap.add_argument('--de', type=float, default=12.0, help='max CIELAB distance to a token')
    ap.add_argument('--viewport', type=int, default=900, help='viewport height in CSS px')
    ap.add_argument('--strip')
    ap.add_argument('--json')
    a = ap.parse_args()
    masks = json.load(open(a.masks, encoding='utf-8')) if a.masks else {}
    tot = np.zeros(len(FAMILIES))
    photo_cells = 0
    strips, switches = [], 0
    for shot in a.shots:
        fam = classify(Image.open(shot), a.de)
        keep = np.ones(fam.shape, bool)
        k = a.scale / 4.0  # CSS px -> 4x4 cell
        m = masks.get(os.path.basename(shot), {})
        for x, y, w, h in m.get('photo', []):
            keep[int(y * k):int((y + h) * k) + 1, int(x * k):int((x + w) * k) + 1] = False
        for x, y, w, h in m.get('project', []):
            fam[int(y * k):int((y + h) * k) + 1, int(x * k):int((x + w) * k) + 1] = FAMILIES.index('project')
        photo_cells += int((~keep).sum())
        for i in range(len(FAMILIES)):
            tot[i] += ((fam == i) & keep).sum()
        band = max(1, int(round(40 * k)))
        rows = []
        for y0 in range(0, fam.shape[0], band):
            f, kp = fam[y0:y0 + band], keep[y0:y0 + band]
            rows.append(int(np.bincount(f[kp], minlength=len(FAMILIES)).argmax()) if kp.any() else -1)
        min_run = max(1, int(0.5 * a.viewport / 40))
        runs, cur, n = [], None, 0
        for r in rows:
            if r == cur:
                n += 1
            else:
                if cur is not None:
                    runs.append((cur, n))
                cur, n = r, 1
        runs.append((cur, n))
        long_runs = [r for r in runs if r[1] >= min_run and r[0] >= 0]
        switches += sum(1 for p, q in zip(long_runs, long_runs[1:]) if p[0] != q[0])
        strips.append(rows)
    denom = tot.sum()
    palette = tot[:4].sum()
    result = {f: round(float(tot[i] / denom * 100), 1) for i, f in enumerate(FAMILIES)}
    result['plum_blue_of_palette'] = round(float((tot[0] + tot[1]) / palette * 100), 1)
    for i, f in enumerate(FAMILIES[:4]):
        result[f + '_of_palette'] = round(float(tot[i] / palette * 100), 1)
    result['switches'] = switches
    print(f"cells: {int(denom)} measured, {photo_cells} photo cells left out")
    for f in FAMILIES:
        print(f"  {f:10s} {result[f]:5.1f}% of non-photo area")
    print("  palette share (photos and project colours out): " +
          "  ".join(f"{f} {result[f + '_of_palette']:.0f}%" for f in FAMILIES[:4]) +
          f"  ->  plum+blue {result['plum_blue_of_palette']:.0f}%")
    print(f"  ground switches (runs of half a viewport or more): {switches}")
    if a.json:
        json.dump(result, open(a.json, 'w', encoding='utf-8'), indent=1)
    if a.strip:
        w = 60
        hgt = max(len(s) for s in strips) * 2
        im = Image.new('RGB', (w * len(strips) + 6 * (len(strips) - 1), hgt), (255, 255, 255))
        px = im.load()
        for j, rows in enumerate(strips):
            for y, r in enumerate(rows):
                col = SWATCH['photo'] if r < 0 else SWATCH[FAMILIES[r]]
                for yy in (2 * y, 2 * y + 1):
                    for x in range(w):
                        px[j * (w + 6) + x, yy] = col
        im.save(a.strip)


if __name__ == '__main__':
    main()
