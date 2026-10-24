"""Warm the production server's image cache: load each page and run down it quickly, desktop then phone."""
import os
import sys
from framecap import Cap
BASE = os.environ.get("KV_BASE", "http://localhost:3211")
cap = Cap()
for mob in (False, True):
    cap.cmd("Emulation.setDeviceMetricsOverride", {"width": 390 if mob else 1440, "height": 844 if mob else 900, "deviceScaleFactor": 1, "mobile": mob})
    for path in sys.argv[1:] or ["/"]:
        cap.goto(f"{BASE}{path}?nointro", wait=2)
        h = cap.eval("document.documentElement.scrollHeight")
        for y in range(0, h, 500):
            cap.eval(f"window.lenis ? window.lenis.scrollTo({y}, {{immediate: true}}) : window.scrollTo(0, {y})")
            cap.pump(0.12)
cap.cmd("Emulation.clearDeviceMetricsOverride")
cap.ws.close()
print("warm")
