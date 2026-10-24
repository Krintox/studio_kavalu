"""Walk the built site in the preview: per page and viewport, overflow + errors + a contact sheet of
viewport shots at several depths. Usage: site_check.py <tag> [reduced] [paths...]"""
import io
import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw

from preview import Preview

OUT = Path("C:/shashank/shashank/fnf/ananya_residency/studio_kavalu/research/working-shots/v2")
tag = sys.argv[1]
reduced = len(sys.argv) > 2 and sys.argv[2] == "reduced"
paths = [a for a in sys.argv[3 if reduced else 2:]] or ["/", "/work", "/studio", "/work/studio-anokhi", "/work/nivritti", "/work/not-so-onam"]
VIEWS = {"desktop": (1440, 900, False, 1), "mobile": (390, 844, True, 2)}
w, h, mob, dpr = VIEWS[tag.split("-")[0]]
OUT.mkdir(parents=True, exist_ok=True)

p = Preview()
p.viewport(w, h, mob, dpr)
p.reduced(reduced)
report = {}
for path in paths:
    p.errors.clear()
    p.open(path, wait=3)
    p.walk(steps=34, dy=1000, x=w // 2, y=h // 2)  # every trigger fires, as for a reader
    p.pump(2.5)
    total = p.eval("document.documentElement.scrollHeight")
    info = json.loads(p.eval("""JSON.stringify({ docW: document.documentElement.scrollWidth, vw: innerWidth,
      wide: [...document.querySelectorAll('body *')].filter(e => { const r = e.getBoundingClientRect(); return r.right > innerWidth + 1 && r.width < innerWidth * 3 && getComputedStyle(e).position !== 'fixed'; })
        .slice(0, 6).map(e => e.tagName.toLowerCase() + '.' + String(e.className).slice(0, 40) + ' r=' + Math.round(e.getBoundingClientRect().right)),
      hidden: [...document.querySelectorAll('[data-written], [data-typed], [data-pin], [data-reveal]')].filter(e => +getComputedStyle(e).opacity < 0.98).length })"""))
    shots = []
    stops = [0, 0.2, 0.4, 0.6, 0.8, 1.0]
    for f in stops:
        p.scroll_to(int((total - h) * f), settle=1.6)
        name = OUT / f"{tag}{'-rm' if reduced else ''}_{path.strip('/').replace('/', '_') or 'home'}_{int(f * 100)}.jpg"
        p.shot(str(name), quality=78)
        shots.append(name)
    # contact sheet: 3 x 2
    ims = [Image.open(s) for s in shots]
    cw = 640 if not mob else 300
    ims = [im.resize((cw, int(im.height * cw / im.width))) for im in ims]
    ch = max(im.height for im in ims)
    sheet = Image.new("RGB", (3 * cw + 4 * 8, 2 * (ch + 22) + 8), "white")
    d = ImageDraw.Draw(sheet)
    for i, (im, f) in enumerate(zip(ims, stops)):
        x, y = 8 + (i % 3) * (cw + 8), 8 + (i // 3) * (ch + 22)
        d.text((x, y), f"{path} @ {int(f * 100)}%", fill="black")
        sheet.paste(im, (x, y + 14))
    sheet_name = OUT / f"sheet_{tag}{'-rm' if reduced else ''}_{path.strip('/').replace('/', '_') or 'home'}.jpg"
    sheet.save(sheet_name, quality=80)
    errs = [e for e in p.errors if "runtime.lastError" not in e]
    report[path] = {"height": total, **info, "errors": errs}
    print(f"{path:22s} h={total:6d} docW={info['docW']} vw={info['vw']} hiddenAfterWalk={info['hidden']} wide={info['wide'][:3]} errors={errs[:3]}")
print("missing files:", sorted(set(p.missing))[:12])
(OUT / f"report_{tag}{'-rm' if reduced else ''}.json").write_text(json.dumps(report, indent=1), encoding="utf-8")
p.close()
