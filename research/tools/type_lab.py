"""Q14: the three type systems of research/type/KAVALU_FONT_SHORTLIST.md set in the real site, side by side.

Each system is switched with html[data-type] (styles/type-lab.css), and the same views are captured at
desktop and phone: the hero with the lockup, a project spread, the house view, the four roads, the founder,
the letter and the footer desk. Output: research/type/lab/<system>_<device>_<view>.jpg and a sheet per
device, research/type/lab/compare_<device>.jpg.
    type_lab.py [systems=now,A,B,C] [devices=desktop,mobile]
"""
import base64
import io
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, "C:/Users/YB-TSR/AppData/Local/Temp/claude/C--shashank-shashank-fnf-ananya-residency-studio-kavalu/a3bb7160-284a-4262-8b39-11e03e34435c/scratchpad")
from framecap import Cap  # noqa: E402

OUT = Path(__file__).resolve().parents[1] / "type" / "lab"
OUT.mkdir(parents=True, exist_ok=True)
SYSTEMS = (sys.argv[1] if len(sys.argv) > 1 else "now,A,B,C").split(",")
DEVICES = (sys.argv[2] if len(sys.argv) > 2 else "desktop,mobile").split(",")
# (name, how to get there): a selector scrolled to the top of the screen, plus an offset
VIEWS = [
    ("hero", None, 0),
    ("spread", "[data-section=spread]", 0.62),
    ("houseview", "[data-section=manifesto]", 0.12),
    ("roads", "[data-section=roads]", 0.05),
    ("founder", "[data-section=founder]", 0.1),
    ("letter", "[data-section=choose]", 0.05),
    ("desk", "footer [data-tone=dark]", 0.0),
]


def go(cap, sel, frac, h):
    if sel is None:
        cap.eval("window.scrollTo(0, 0)")
    else:
        cap.eval(f"(() => {{ const e = document.querySelector('{sel}'); const y = e.getBoundingClientRect().top + scrollY; window.scrollTo(0, Math.round(y + {frac} * e.offsetHeight)); }})()")
    cap.pump(2.2)


def main():
    cap = Cap()
    try:
        for dev in DEVICES:
            w, h = (1440, 900) if dev == "desktop" else (390, 844)
            cap.cmd("Emulation.setDeviceMetricsOverride", {"width": w, "height": h, "deviceScaleFactor": 1, "mobile": dev == "mobile"})
            cap.cmd("Emulation.setTouchEmulationEnabled", {"enabled": dev == "mobile"})
            for sysname in SYSTEMS:
                cap.eval("try { sessionStorage.setItem('kv-intro', '1') } catch (e) {}")
                cap.goto("http://localhost:3210/", wait=3.0)
                cap.eval(f"document.documentElement.dataset.type = '{'' if sysname == 'now' else sysname}'; document.fonts.ready.then(() => window.dispatchEvent(new Event('resize')))")
                cap.pump(1.5)
                # walk down once so every arrival has played, then shoot each view
                for _ in range(16):
                    cap.wheel(900, 4, 0.02)
                cap.pump(1.0)
                for name, sel, frac in VIEWS:
                    go(cap, sel, frac, h)
                    shot = cap.cmd("Page.captureScreenshot", {"format": "jpeg", "quality": 84})
                    Image.open(io.BytesIO(base64.b64decode(shot["data"]))).save(OUT / f"{sysname}_{dev}_{name}.jpg", quality=86)
                print(sysname, dev, "done", flush=True)
    finally:
        cap.cmd("Emulation.clearDeviceMetricsOverride")
        cap.cmd("Emulation.setTouchEmulationEnabled", {"enabled": False})
        cap.ws.close()
    font = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 26)
    for dev in DEVICES:
        tw = 480 if dev == "desktop" else 200
        imgs = {(s, v): Image.open(OUT / f"{s}_{dev}_{v}.jpg") for s in SYSTEMS for v, _, _ in VIEWS}
        th = int(next(iter(imgs.values())).height * tw / next(iter(imgs.values())).width)
        sheet = Image.new("RGB", (120 + len(VIEWS) * (tw + 8), len(SYSTEMS) * (th + 8) + 8), (32, 26, 30))
        d = ImageDraw.Draw(sheet)
        for r, s in enumerate(SYSTEMS):
            d.text((20, 8 + r * (th + 8) + th // 2 - 13), s, fill=(243, 243, 231), font=font)
            for c, (v, _, _) in enumerate(VIEWS):
                sheet.paste(imgs[(s, v)].resize((tw, th)), (120 + c * (tw + 8), 8 + r * (th + 8)))
        sheet.save(OUT / f"compare_{dev}.jpg", quality=84)
        print(OUT / f"compare_{dev}.jpg")


if __name__ == "__main__":
    main()
