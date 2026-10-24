"""The social preview card (Open Graph / X), made from the site itself.

The card is drawn in the persistent Chrome on the dev server's own origin, so it uses the site's real
fonts (Kannada shaped by the browser), paper textures and Ananya's lettering (the lockup is copied from
the live nav), then saved where Next.js picks it up as a file-based image:
  website/src/app/opengraph-image.jpg (+ .alt.txt)  and  twitter-image.jpg (+ .alt.txt)
Rendered at twice the size and scaled down, saved as a JPEG under 300 KB so WhatsApp still shows it.

usage (dev server on :3210):  python og_card.py [--preview-only]
"""
import base64
import io
import json
import re
import shutil
import sys
from pathlib import Path

from PIL import Image

from framecap import Cap

ROOT = Path(__file__).resolve().parents[2]
APP = ROOT / "website/src/app"
SHOTS = ROOT / "research/working-shots/v3/og"
BASE = "http://localhost:3210"
W, H = 1200, 630

CARD = """<!doctype html><html><head><meta charset="utf-8"><style>
%(fonts)s
:root { --g: %(grotesk)s; --m: %(mono)s; --h: %(hand)s; --k: %(kannada)s; }
* { box-sizing: border-box; }
html, body { margin: 0; width: %(W)dpx; height: %(H)dpx; overflow: hidden; }
body {
  position: relative;
  background: #f3f3e7 url(%(tex_cream)s) 0 0 / 1024px;
  color: #241319;
  font-family: var(--g);
  -webkit-font-smoothing: antialiased;
}
/* the lockup: her K mark and STUDIO / KAVALU, the largest thing on the card. Its clear space (BRAND_DESIGN
   §3.4) is one cap height of the words, 55 px at this size: nothing else comes closer. */
.lockup { position: absolute; left: 88px; top: 196px; width: 596px; color: #390d26; }
.lockup svg { display: block; width: 100%%; height: auto; }
/* what the studio is, and her signature on the same line */
.line {
  position: absolute; left: 90px; top: 414px; display: flex; align-items: baseline; gap: 18px;
  font: 500 19px/1 var(--g); letter-spacing: 0.07em; text-transform: uppercase; color: #5d4a50;
}
.sign { display: inline-block; rotate: -4deg; font: 400 26px/1 var(--h); letter-spacing: 0; text-transform: none; color: #390d26; }
/* a powder-blue note taped to the page, as the hero's definition card */
.note {
  position: absolute; right: 88px; top: 152px; width: 356px; padding: 34px 34px 32px; rotate: 3deg;
  background: #c9dfe5 url(%(tex_blue)s) 0 0 / 1024px;
  box-shadow: 0 1px 1px rgb(39 6 23 / 0.08), 0 8px 16px -6px rgb(39 6 23 / 0.24), 0 26px 44px -24px rgb(39 6 23 / 0.38);
}
.tape {
  position: absolute; top: -15px; left: 50%%; width: 118px; height: 32px; translate: -50%% 0; rotate: -5deg;
  background: rgb(243 243 231 / 0.66); box-shadow: 0 1px 2px rgb(39 6 23 / 0.12);
}
.word { display: flex; align-items: baseline; gap: 14px; }
.kn { font: 600 58px/1.05 var(--k); color: #390d26; }
.say { font: 400 19px/1 var(--m); color: #50334a; }
.def { margin: 16px 0 0; font: 400 21px/1.36 var(--g); color: #241319; text-wrap: pretty; }
</style></head><body>
<div class="lockup">%(lockup)s</div>
<div class="line"><span>Branding &amp; content house · %(city)s</span><span class="sign">by Ananya</span></div>
<div class="note"><span class="tape"></span>
  <div class="word"><span class="kn" lang="kn">%(word)s</span><span class="say">/%(say)s/</span></div>
  <p class="def">%(definition)s</p>
</div>
</body></html>"""


def main():
    preview_only = "--preview-only" in sys.argv
    SHOTS.mkdir(parents=True, exist_ok=True)
    cap = Cap()
    cap.cmd("Emulation.setDeviceMetricsOverride", {"width": 1440, "height": 900, "deviceScaleFactor": 1, "mobile": False})
    cap.goto(f"{BASE}/?nointro", wait=3)
    # everything the card borrows from the live site
    got = json.loads(cap.eval("""JSON.stringify((() => {
      const css = [];
      for (const sheet of document.styleSheets) {
        // font files are named relative to their stylesheet; the card page lives elsewhere, so make them absolute
        const base = sheet.href || location.href;
        try {
          for (const r of sheet.cssRules) if (r.type === CSSRule.FONT_FACE_RULE)
            css.push(r.cssText.replace(/url\\((['"]?)([^'")]+)\\1\\)/g, (m, q, u) => 'url("' + new URL(u, base).href + '")'));
        } catch (e) {}
      }
      const root = getComputedStyle(document.documentElement);
      const v = (n) => root.getPropertyValue(n).trim();
      const svg = document.querySelector('svg[role="img"][aria-label="Studio Kavalu"]');
      const url = (n) => (v(n).match(/url\\(["']?([^"')]+)/) || [])[1];
      return { fonts: css.join('\\n'), grotesk: v('--font-grotesk'), mono: v('--font-mono'), hand: v('--font-hand'),
               kannada: v('--font-kannada'), lockup: svg ? svg.outerHTML : '', tex_cream: url('--tex-cream'), tex_blue: url('--tex-blue') };
    })())"""))
    assert got["lockup"] and got["fonts"] and got["tex_cream"], {k: bool(v) for k, v in got.items()}
    # the words come from the site's own copy
    site = (ROOT / "website/src/content/site.ts").read_text(encoding="utf-8")

    def field(name):
        return re.search(rf'^\s*{name}:\s*"([^"]*)"', site, re.M).group(1)

    html = CARD % {
        "fonts": got["fonts"], "grotesk": got["grotesk"], "mono": got["mono"], "hand": got["hand"],
        "kannada": got["kannada"], "lockup": got["lockup"], "tex_cream": got["tex_cream"], "tex_blue": got["tex_blue"],
        "W": W, "H": H, "city": field("city"), "word": field("word"), "say": field("say"), "definition": field("definition"),
    }
    # a same-origin page with no app on it, so the site's fonts and textures load and nothing re-renders
    cap.goto(f"{BASE}/robots.txt", wait=0.5)
    # Chrome keeps a zoom level per site (this one has localhost at 90%), and it scales the emulated
    # screen; measure it and size the screen so the page is exactly W x H CSS pixels at 2 device pixels each
    cap.cmd("Emulation.setDeviceMetricsOverride", {"width": W, "height": H, "deviceScaleFactor": 2, "mobile": False})
    zoom = W / cap.eval("innerWidth")
    if abs(zoom - 1) > 0.005:
        cap.cmd("Emulation.setDeviceMetricsOverride",
                {"width": round(W * zoom), "height": round(H * zoom), "deviceScaleFactor": 2 / zoom, "mobile": False})
    size = cap.eval("[innerWidth, innerHeight, devicePixelRatio]")
    assert abs(size[0] - W) <= 1 and abs(size[1] - H) <= 1, size
    cap.eval(f"document.open(); document.write({json.dumps(html)}); document.close();")
    cap.eval("""(async () => {
      await Promise.all([...document.fonts].map((f) => f.load().catch(() => null)));
      await document.fonts.ready;
      const urls = [...document.querySelectorAll('*')].map(e => getComputedStyle(e).backgroundImage)
        .flatMap(b => [...b.matchAll(/url\\(["']?([^"')]+)/g)].map(m => m[1]));
      await Promise.all(urls.map(u => new Promise(r => { const i = new Image(); i.onload = i.onerror = r; i.src = u; })));
      return true;
    })()""")
    cap.pump(0.8)
    if "--debug" in sys.argv:
        print(cap.eval("""JSON.stringify({ iw: innerWidth, ih: innerHeight, dpr: devicePixelRatio, vv: visualViewport.scale,
          body: document.body.getBoundingClientRect().toJSON(), lockup: document.querySelector('.lockup').getBoundingClientRect().toJSON(),
          svg: document.querySelector('.lockup svg').getBoundingClientRect().toJSON(),
          note: document.querySelector('.note').getBoundingClientRect().toJSON(), sign: document.querySelector('.sign').getBoundingClientRect().toJSON(),
          line: document.querySelector('.line').getBoundingClientRect().toJSON(),
          sw: document.documentElement.scrollWidth })"""))
    shot = cap.cmd("Page.captureScreenshot", {"format": "png", "captureBeyondViewport": False})
    cap.cmd("Emulation.clearDeviceMetricsOverride")
    cap.cmd("Page.navigate", {"url": "about:blank"})
    cap.ws.close()

    big = Image.open(io.BytesIO(base64.b64decode(shot["data"]))).convert("RGB")
    big.save(SHOTS / "og_card@2x.png")
    card = big.resize((W, H), Image.LANCZOS)
    out = SHOTS / "opengraph-image.jpg"
    for q in (88, 84, 80, 76):
        card.save(out, "JPEG", quality=q, progressive=True, optimize=True)
        if out.stat().st_size < 290_000:
            break
    print(f"card {card.size}, {out.stat().st_size // 1024} KB at quality {q} -> {out}")
    if preview_only:
        return
    for name in ("opengraph-image", "twitter-image"):
        shutil.copy(out, APP / f"{name}.jpg")
        # the description lives in site.ts (cardAlt), where the case studies that show the card read it too
        (APP / f"{name}.alt.txt").write_text(field("cardAlt"), encoding="utf-8")
    print("written to", APP)


if __name__ == "__main__":
    main()
