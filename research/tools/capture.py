"""capture.py SITES.json OUTDIR

For every {name, url, bucket} entry: load in the dedicated research tab at 1440x900,
detect stack/fonts, then capture the hero and two scroll depths using real wheel events
(so Lenis / Locomotive / ScrollTrigger animations fire like they do for a person).
Appends one JSON line per site to OUTDIR/results.jsonl and skips sites already done.
"""
import json
import os
import re
import sys
import time

from cdp import Tab, get_tab_info

sites = json.load(open(sys.argv[1], encoding="utf-8"))
out = sys.argv[2]
os.makedirs(out, exist_ok=True)
res_path = os.path.join(out, "results.jsonl")
done = set()
if os.path.exists(res_path):
    for line in open(res_path, encoding="utf-8"):
        try:
            done.add(json.loads(line)["slug"])
        except Exception:
            pass


def slugify(u):
    u = re.sub(r"^https?://(www\.)?", "", u).rstrip("/")
    return re.sub(r"[^a-z0-9]+", "-", u.lower()).strip("-")[:60]


tab = Tab()
tab.front()
tab.viewport(1440, 900)
for i, s in enumerate(sites):
    slug = slugify(s["url"])
    if slug in done:
        continue
    rec = {"slug": slug, "name": s.get("name", slug), "url": s["url"], "bucket": s.get("bucket", "")}
    t0 = time.time()
    try:
        tab.goto(s["url"], wait=5.0, timeout=30)
        tab.move(720, 450)
        rec["info"] = tab.detect()
        tab.shot(os.path.join(out, f"{slug}_0.jpg"))
        tab.wheel(900, steps=12, pause=0.06)
        time.sleep(2.2)
        tab.shot(os.path.join(out, f"{slug}_1.jpg"))
        tab.wheel(1500, steps=16, pause=0.06)
        time.sleep(2.2)
        tab.shot(os.path.join(out, f"{slug}_2.jpg"))
        rec["ok"] = True
    except Exception as e:  # keep going; one bad site must not stop the batch
        rec["ok"] = False
        rec["error"] = str(e)[:200]
        try:
            tab.close_ws()
        except Exception:
            pass
        try:
            tab = Tab(get_tab_info())
            tab.front()
            tab.viewport(1440, 900)
        except Exception as e2:
            rec["error"] += " | reconnect: " + str(e2)[:100]
    rec["secs"] = round(time.time() - t0, 1)
    with open(res_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(i, "OK" if rec["ok"] else "FAIL", slug, rec["secs"], flush=True)
tab.close_ws()
print("DONE")
