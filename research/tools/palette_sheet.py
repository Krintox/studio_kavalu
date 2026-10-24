"""Side-by-side sheet of the palette lab's iterations: the same screens of the home page for each one,
with its measured shares. palette_sheet.py <desktop|mobile> <it1,it2,...> [screen indexes]
Output: research/palette_lab/compare_<device>.jpg"""
import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1] / "palette_lab"
dev = sys.argv[1]
names = sys.argv[2].split(",")
picks = [int(x) for x in sys.argv[3].split(",")] if len(sys.argv) > 3 else None

font = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 22)
small = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 17)
rows = []
for nm in names:
    shots = sorted((ROOT / nm / dev).glob("home_*.jpg"))
    sel = [shots[i] for i in picks if i < len(shots)] if picks else shots
    res = json.loads((ROOT / nm / "result.json").read_text(encoding="utf-8"))["devices"][dev]
    rows.append((nm, res, [Image.open(p) for p in sel]))

tw = 420 if dev == "desktop" else 190
th = int(rows[0][2][0].height * tw / rows[0][2][0].width)
cols = max(len(r[2]) for r in rows)
label_w = 300
W = label_w + cols * (tw + 10) + 10
H = len(rows) * (th + 16) + 16
sheet = Image.new("RGB", (W, H), (32, 26, 30))
d = ImageDraw.Draw(sheet)
for r, (nm, res, imgs) in enumerate(rows):
    y = 16 + r * (th + 16)
    s = res["share_all"]
    d.text((14, y + 6), nm, fill=(243, 243, 231), font=font)
    d.text((14, y + 40), f"plum   {s['plum']:5.1f}%", fill=(214, 160, 190), font=small)
    d.text((14, y + 62), f"blue   {s['blue']:5.1f}%", fill=(171, 205, 214), font=small)
    d.text((14, y + 84), f"cream  {s['cream']:5.1f}%", fill=(243, 243, 231), font=small)
    d.text((14, y + 106), f"photo  {s['other']:5.1f}%", fill=(160, 150, 150), font=small)
    d.text((14, y + 134), f"P+B {res['plum_blue_all']:4.1f}% of screen", fill=(243, 243, 231), font=small)
    d.text((14, y + 156), f"P+B {res['plum_blue_own']:4.1f}% of own colour", fill=(243, 243, 231), font=small)
    for k, im in enumerate(imgs):
        sheet.paste(im.resize((tw, th)), (label_w + k * (tw + 10), y))
out = ROOT / f"compare_{dev}.jpg"
sheet.save(out, quality=86)
print(out, sheet.size)
