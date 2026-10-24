"""sheets.py SCREENS_DIR SHEETS_DIR [per_sheet] -> contact sheets of captured sites.

One row per site: a label (name, bucket, stack, fonts) above hero / scroll-1 / scroll-2.
"""
import json
import os
import sys

from PIL import Image, ImageDraw, ImageFont

src, dst = sys.argv[1], sys.argv[2]
per = int(sys.argv[3]) if len(sys.argv) > 3 else 4
os.makedirs(dst, exist_ok=True)
TW, TH, LH, GAP = 600, 375, 40, 6
font = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 17)
bold = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 19)

recs = []
seen = set()
for line in open(os.path.join(src, "results.jsonl"), encoding="utf-8"):
    r = json.loads(line)
    if r.get("ok") and r["slug"] not in seen and os.path.exists(os.path.join(src, r["slug"] + "_0.jpg")):
        seen.add(r["slug"])
        recs.append(r)


def flags(info):
    t = (info or {}).get("tech", {}) or {}
    keys = ["gsap", "scrolltrigger", "lenis", "locomotive", "three", "ogl", "pixi", "barba", "swup", "taxi",
            "framer", "webflow", "next", "nuxt", "astro", "sveltekit", "shopify", "squarespace", "wix",
            "wordpress", "cargo", "motion", "splitting"]
    on = [k for k in keys if t.get(k)]
    if t.get("canvas"):
        on.append(f"canvas{t['canvas']}")
    if t.get("video"):
        on.append(f"video{t['video']}")
    return " ".join(on)


index = []
for n in range(0, len(recs), per):
    chunk = recs[n:n + per]
    W = TW * 3 + GAP * 2
    H = len(chunk) * (TH + LH + GAP)
    sheet = Image.new("RGB", (W, H), (24, 24, 24))
    d = ImageDraw.Draw(sheet)
    for k, r in enumerate(chunk):
        y = k * (TH + LH + GAP)
        info = r.get("info") or {}
        fonts = ", ".join((info.get("fonts") or [])[:4]) if isinstance(info, dict) else ""
        d.text((8, y + 8), f"[{r['bucket']}] {r['name']}", fill=(255, 220, 120), font=bold)
        d.text((330, y + 10), f"{r['url'][:44]}  |  {flags(info)}  |  {fonts}"[:150], fill=(220, 220, 220), font=font)
        for j in range(3):
            p = os.path.join(src, f"{r['slug']}_{j}.jpg")
            if os.path.exists(p):
                im = Image.open(p).convert("RGB").resize((TW, TH), Image.LANCZOS)
                sheet.paste(im, (j * (TW + GAP), y + LH))
    name = f"sheet_{n // per + 1:02d}.jpg"
    sheet.save(os.path.join(dst, name), quality=82)
    index.append({"sheet": name, "sites": [r["name"] for r in chunk]})
json.dump(index, open(os.path.join(dst, "index.json"), "w", encoding="utf-8"), indent=1)
print(len(recs), "sites ->", len(index), "sheets")
