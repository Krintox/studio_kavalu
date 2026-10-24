import json, sys
from collections import Counter
recs = {}
for line in open(sys.argv[1], encoding="utf-8"):
    r = json.loads(line)
    if r.get("ok") and r.get("info"):
        recs[r["slug"]] = r
n = len(recs)
c = Counter()
fonts = Counter()
for r in recs.values():
    t = (r["info"] or {}).get("tech") or {}
    for k in ["gsap", "scrolltrigger", "lenis", "locomotive", "three", "pixi", "barba", "swup", "taxi", "framer", "webflow", "next", "nuxt", "astro", "sveltekit", "shopify", "squarespace", "wix", "wordpress", "cargo", "motion", "splitting"]:
        if t.get(k): c[k] += 1
    if (t.get("canvas") or 0) > 0: c["canvas"] += 1
    if (t.get("video") or 0) > 0: c["video"] += 1
    for f in (r["info"].get("fonts") or [])[:3]:
        fonts[f.split("_")[0].split(" Fallback")[0]] += 1
print(f"{n} sites with stack data")
for k, v in c.most_common():
    print(f"  {k:14s} {v:4d}  {100*v/n:5.1f}%")
print("top fonts:", ", ".join(f"{f} ({v})" for f, v in fonts.most_common(18)))
