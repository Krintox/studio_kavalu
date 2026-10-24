"""Measure the handwork motion in the built site: per animation frame, how much of each typed label
is typed and how much of each hand note is written; plus frames cropped to follow the element."""
import base64
import io
import json
import sys
from pathlib import Path

from PIL import Image

from preview import Preview

OUT = Path("C:/shashank/shashank/fnf/ananya_residency/studio_kavalu/research/motion_frames/kavalu")
page, sel, name = sys.argv[1], sys.argv[2], sys.argv[3]

LOGGER = r"""
(() => {
  const el = document.querySelector(%s); if (!el) return 'missing';
  window.__hw = []; const t0 = performance.now();
  const tick = () => {
    if (window.__hw.length > 900) return;
    const chars = el.querySelectorAll('div div, div > div'); // SplitText words > chars
    const words = [...el.children].filter(c => c.tagName === 'DIV');
    let typed = null, written = null;
    if (words.length) {
      const leaf = [...el.querySelectorAll('div')].filter(d => !d.querySelector('div'));
      typed = leaf.filter(d => +getComputedStyle(d).opacity > 0.5).length + '/' + leaf.length;
      written = words.filter(w => { const c = getComputedStyle(w).clipPath; const m = c.match(/inset\(([^)]+)\)/); if (!m) return true; const right = m[1].split(' ')[1] || m[1].split(' ')[0]; return parseFloat(right) <= 0; }).length + '/' + words.length;
    }
    const r = el.getBoundingClientRect();
    window.__hw.push({ t: +(performance.now() - t0).toFixed(0), split: words.length > 0, typed, written, top: Math.round(r.top) });
    requestAnimationFrame(tick);
  };
  requestAnimationFrame(tick);
  return 'ok';
})()
"""


class Rec(Preview):
    def _handle(self, msg):
        if msg.get("method") == "Page.screencastFrame":
            p = msg["params"]
            self.frames.append((p["metadata"]["timestamp"], p["data"], p["metadata"].get("scrollOffsetY", 0)))
            self.ws.send(json.dumps({"id": 10_000_000 + len(self.frames), "method": "Page.screencastFrameAck", "params": {"sessionId": p["sessionId"]}}))
            return
        super()._handle(msg)


p = Rec()
p.viewport(1440, 900)
p.open(page, wait=3)
top = p.eval(f"Math.round(document.querySelector({json.dumps(sel)}).getBoundingClientRect().top + scrollY)")
p.scroll_to(max(0, top - 900 - 40), settle=1.5)
print("logger:", p.eval(LOGGER % json.dumps(sel)))
p.frames = []
p.cmd("Page.startScreencast", {"format": "jpeg", "quality": 75, "maxWidth": 1440, "maxHeight": 900, "everyNthFrame": 1})
p.pump(0.2)
p.wheel(420, 10, 0.02)
p.pump(3.6)
p.cmd("Page.stopScreencast")
log = json.loads(p.eval("JSON.stringify(window.__hw || [])"))
# summarise: first frame split, progress over time, when it reverted
changes, last = [], None
for row in log:
    key = (row["split"], row["typed"], row["written"])
    if key != last:
        changes.append(row)
        last = key
print(f"{len(log)} frames logged; state changes:")
for row in changes[:60]:
    print(f"  t={row['t']:5d}ms split={row['split']!s:5s} typed={row['typed']} written={row['written']} top={row['top']}")
# frames cropped to the element (page coordinates via each frame's scroll offset)
box = p.eval(f"(() => {{ const r = document.querySelector({json.dumps(sel)}).getBoundingClientRect(); return [r.x, r.y + scrollY, r.width, r.height]; }})()")
x, py, w, h = box
crops = []
for ts, data, sy in p.frames:
    im = Image.open(io.BytesIO(base64.b64decode(data)))
    y = py - sy
    if -h < y < 900:
        crops.append(im.crop((int(x - 40), int(y - 30), int(x + w + 40), int(y + h + 30))))
pick = crops[:: max(1, len(crops) // 16)][:16]
if pick:
    cw, chh = pick[0].size
    grid = Image.new("RGB", (cw * 2 + 30, (chh + 8) * ((len(pick) + 1) // 2) + 10), "white")
    for i, c in enumerate(pick):
        grid.paste(c, (10 + (i % 2) * (cw + 10), 10 + (i // 2) * (chh + 8)))
    grid.save(OUT / f"{name}_follow.jpg", quality=88)
print("frames", len(p.frames), "crops", len(crops))
p.close()
