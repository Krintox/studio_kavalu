"""look.py URL OUT.jpg [width height] [scrollY] [wait] -> screenshot of the dev site, plus console errors."""
import json, sys, time
from cdp import Tab
url, out = sys.argv[1], sys.argv[2]
w = int(sys.argv[3]) if len(sys.argv) > 3 else 1440
h = int(sys.argv[4]) if len(sys.argv) > 4 else 900
sy = int(sys.argv[5]) if len(sys.argv) > 5 else 0
wait = float(sys.argv[6]) if len(sys.argv) > 6 else 3
t = Tab(); t.front(); t.viewport(w, h, mobile=w < 600)
t.call("Log.enable")
t.goto(url, wait=wait, timeout=60)
if sy:
    t.wheel(sy, x=w // 2, y=h // 2, steps=max(6, sy // 120), pause=0.05)
    time.sleep(1.8)
t.shot(out, quality=85)
errs = t.eval("(window.__errs || []).slice(0, 10)")
print("scrollY", t.eval("Math.round(scrollY)"), "| docH", t.eval("document.documentElement.scrollHeight"))
t.close_ws()
