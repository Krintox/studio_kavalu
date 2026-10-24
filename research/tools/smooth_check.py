"""How smooth is the scroll, measured: scroll a page at a steady trackpad-like pace while a
requestAnimationFrame logger records every frame's duration; report long frames and the worst ones, and
save a contact sheet of the screencast."""
import json
import sys
from pathlib import Path

import os
BASE = os.environ.get("KV_BASE", "http://localhost:3210")
from framecap import Cap, contact_sheet

path = sys.argv[1] if len(sys.argv) > 1 else "/"
OUT = Path("C:/shashank/shashank/fnf/ananya_residency/studio_kavalu/research/working-shots/v3/smooth")
OUT.mkdir(parents=True, exist_ok=True)
cap = Cap()
mob = "mobile" in sys.argv
cap.cmd("Emulation.setDeviceMetricsOverride", {"width": 390 if mob else 1440, "height": 844 if mob else 900, "deviceScaleFactor": 1, "mobile": mob})
sep = "&" if "?" in path else "?"
cpu = float(os.environ.get("KV_CPU", "1"))
if mob:
    cap.cmd("Emulation.setTouchEmulationEnabled", {"enabled": True, "maxTouchPoints": 5})
cap.goto(f"{BASE}{path}{sep}nointro", wait=4.5)
if cpu > 1:
    cap.cmd("Emulation.setCPUThrottlingRate", {"rate": cpu})
    cap.pump(1.5)
cap.eval("""(() => { window.__ft = []; let last = performance.now();
  const tick = t => { window.__ft.push([+(t - last).toFixed(2), Math.round(scrollY)]); last = t; if (window.__ft.length < 20000) requestAnimationFrame(tick); };
  requestAnimationFrame(tick); })()""")
cap.frames.clear()
cap.cmd("Page.startScreencast", {"format": "jpeg", "quality": 55, "maxWidth": 640, "maxHeight": 400, "everyNthFrame": 3})
height = cap.eval("document.documentElement.scrollHeight")
steps = 0
touch = os.environ.get("KV_TOUCH") == "1"
while cap.eval("scrollY + innerHeight") < height - 4 and steps < 900:
    if touch:
        # a finger drag: the browser scrolls natively (off the main thread), as on a phone
        cap.cmd("Input.dispatchTouchEvent", {"type": "touchStart", "touchPoints": [{"x": 195, "y": 640}]})
        for k in range(1, 25):
            cap.cmd("Input.dispatchTouchEvent", {"type": "touchMove", "touchPoints": [{"x": 195, "y": 640 - 400 * k / 24}]})
            cap.pump(0.016)
        cap.cmd("Input.dispatchTouchEvent", {"type": "touchEnd", "touchPoints": []})
        cap.pump(0.05)
    else:
        cap.cmd("Input.dispatchMouseEvent", {"type": "mouseWheel", "x": 720, "y": 450, "deltaX": 0, "deltaY": 60})
        cap.pump(0.033)
    steps += 1
    if steps % 50 == 0:
        height = cap.eval("document.documentElement.scrollHeight")
cap.pump(1.5)
cap.cmd("Page.stopScreencast")
ft = cap.eval("window.__ft.slice(5)")
cap.pump(0.2)
contact_sheet(cap.frames, OUT / ("scroll" + (path.strip("/").replace("/", "_") or "home") + ("_mobile" if mob else "_desktop") + ".jpg"), n=30, cols=6, label=f"steady scroll {path} {"mobile" if mob else ""}")
secs = cap.eval("[...document.querySelectorAll('main section, main [data-section], footer')].map(e => [e.dataset.section || e.tagName.toLowerCase() + '.' + String(e.className).split(' ')[0].slice(0, 20), Math.round(e.getBoundingClientRect().top + scrollY), Math.round(e.getBoundingClientRect().bottom + scrollY)])")
times = [f[0] for f in ft]
long = [f for f in ft if f[0] > 20]
print(json.dumps({"page": path, "cpu": cpu, "mobile": mob, "touch": touch, "frames": len(ft), "median_ms": sorted(times)[len(times) // 2], "over_20ms": len(long), "over_34ms": sum(1 for t in times if t > 34),
                  "share_over_20ms": round(100 * len(long) / max(1, len(ft)), 1), "worst": sorted(times)[-8:], "wheel_steps": steps}))
from collections import Counter
where = Counter()
for t, y in long:
    mid = y + 450
    name = next((n for n, a, b in secs if a <= mid < b), "?")
    where[name] += 1
print("long frames by section (viewport middle):", where.most_common())
cap.cmd("Emulation.setCPUThrottlingRate", {"rate": 1})
if mob:
    cap.cmd("Emulation.setTouchEmulationEnabled", {"enabled": False})
cap.cmd("Emulation.clearDeviceMetricsOverride")
cap.ws.close()
