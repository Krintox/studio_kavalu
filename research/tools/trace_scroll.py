"""Where the slow frames come from, from Chrome's own trace: scroll a page steadily while tracing
(devtools.timeline), then sum our renderer's main-thread work by kind (self time), list the longest tasks
with what was inside them and where the page was, and total the raster threads.

usage: trace_scroll.py <path> [from-fraction]   e.g.  trace_scroll.py /work 0.0
"""
import json
import sys
from collections import Counter, defaultdict

import os
BASE = os.environ.get("KV_BASE", "http://localhost:3210")
from framecap import Cap


class TraceCap(Cap):
    def __init__(self):
        self.trace = []
        self.done = False
        super().__init__()

    def _handle(self, msg):
        m = msg.get("method")
        if m == "Tracing.dataCollected":
            self.trace.extend(msg["params"]["value"])
            return
        if m == "Tracing.tracingComplete":
            self.done = True
            return
        super()._handle(msg)


path = sys.argv[1] if len(sys.argv) > 1 else "/"
frm = float(sys.argv[2]) if len(sys.argv) > 2 else 0.0
cap = TraceCap()
sep = "&" if "?" in path else "?"
mob = "mobile" in sys.argv
if mob:
    cap.cmd("Emulation.setDeviceMetricsOverride", {"width": 390, "height": 844, "deviceScaleFactor": 1, "mobile": True})
cap.goto(f"{BASE}{path}{sep}nointro", wait=4.5)
if frm > 0:
    # jump most of the way down with the wheel (fast), then let everything settle before tracing
    target = cap.eval(f"Math.round(document.documentElement.scrollHeight * {frm})")
    while cap.eval("scrollY") < target - 50:
        cap.cmd("Input.dispatchMouseEvent", {"type": "mouseWheel", "x": 720, "y": 450, "deltaX": 0, "deltaY": 400})
        cap.pump(0.02)
    cap.pump(3.0)
secs = cap.eval("[...document.querySelectorAll('main section, main [data-section], footer')].map(e => [e.dataset.section || String(e.className).split(' ')[0].slice(0, 20), Math.round(e.getBoundingClientRect().top + scrollY), Math.round(e.getBoundingClientRect().bottom + scrollY)])")
cats = ",".join([
    "devtools.timeline", "disabled-by-default-devtools.timeline", "disabled-by-default-devtools.timeline.frame",
    "toplevel", "v8.execute", "blink.user_timing",
] + (["disabled-by-default-devtools.timeline.invalidationTracking"] if "inv" in sys.argv else []))
to = float(sys.argv[4]) if len(sys.argv) > 4 and sys.argv[4] not in ("inv", "mobile") else 1.0
cap.cmd("Tracing.start", {"categories": cats, "transferMode": "ReportEvents"})
# every animation frame leaves a mark in the trace with the scroll position
cap.eval("""(() => { window.__kvt = true; const tick = () => { console.timeStamp('kv y=' + Math.round(scrollY)); if (window.__kvt) requestAnimationFrame(tick); }; requestAnimationFrame(tick); })()""")
height = cap.eval("document.documentElement.scrollHeight")
steps = 0
touch = os.environ.get("KV_TOUCH") == "1"
cpu = float(os.environ.get("KV_CPU", "1"))
if cpu > 1:
    cap.cmd("Emulation.setCPUThrottlingRate", {"rate": cpu})
if touch:
    cap.cmd("Emulation.setTouchEmulationEnabled", {"enabled": True, "maxTouchPoints": 5})
while cap.eval("scrollY + innerHeight") < height * to - 4 and steps < 900:
    if touch:
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
if cpu > 1:
    cap.cmd("Emulation.setCPUThrottlingRate", {"rate": 1})
if touch:
    cap.cmd("Emulation.setTouchEmulationEnabled", {"enabled": False})
cap.pump(1.5)
cap.eval("window.__kvt = false")
cap.cmd("Tracing.end")
if mob:
    cap.cmd("Emulation.clearDeviceMetricsOverride")
for _ in range(400):
    if cap.done:
        break
    cap.pump(0.25)
cap.ws.close()

ev = cap.trace
names = {(e["pid"], e["tid"]): e["args"]["name"] for e in ev if e.get("ph") == "M" and e.get("name") == "thread_name"}
marks = [e for e in ev if e.get("name") == "TimeStamp" and str(e.get("args", {}).get("data", {}).get("message", "")).startswith("kv y=")]
if not marks:
    sys.exit("no marks in the trace")
pid = Counter(e["pid"] for e in marks).most_common(1)[0][0]
main = next(k for k, v in names.items() if k[0] == pid and v == "CrRendererMain")
marks.sort(key=lambda e: e["ts"])
mark_ts = [e["ts"] for e in marks]
mark_y = [int(e["args"]["data"]["message"].split("=")[1]) for e in marks]


def section_at(ts):
    import bisect
    i = max(0, bisect.bisect_right(mark_ts, ts) - 1)
    mid = mark_y[i] + 450
    return next((n for n, a, b in secs if a <= mid < b), "?")


def complete(events):
    """B/E pairs and X events as (ts, dur, name, args), on one thread."""
    out, stack = [], []
    for e in sorted(events, key=lambda e: e["ts"]):
        ph = e.get("ph")
        if ph == "X" and "dur" in e:
            out.append((e["ts"], e["dur"], e["name"], e.get("args", {})))
        elif ph == "B":
            stack.append(e)
        elif ph == "E" and stack:
            b = stack.pop()
            out.append((b["ts"], e["ts"] - b["ts"], b["name"], b.get("args", {})))
    return sorted(out, key=lambda t: (t[0], -t[1]))


def self_times(spans):
    selfs = [d for _, d, _, _ in spans]
    stack = []  # indices
    for i, (ts, dur, _, _) in enumerate(spans):
        while stack and spans[stack[-1]][0] + spans[stack[-1]][1] <= ts:
            stack.pop()
        if stack:
            selfs[stack[-1]] -= dur
        stack.append(i)
    return selfs


t0, t1 = mark_ts[0], mark_ts[-1]
spans = [s for s in complete([e for e in ev if (e["pid"], e["tid"]) == main]) if t0 <= s[0] <= t1]
selfs = self_times(spans)
by = Counter()
for (ts, dur, name, _), s in zip(spans, selfs):
    by[name] += max(0, s)
wall = (t1 - t0) / 1000
print(f"{path}  traced {wall:.0f} ms, {len(marks)} frames, main thread busy (self time by kind, ms):")
print("  " + ", ".join(f"{n} {v / 1000:.0f}" for n, v in by.most_common(14)))

# the longest top-level tasks, what was inside, and where the page was
tops = [s for s in spans if s[2] == "ThreadControllerImpl::RunTask"] or [s for s in spans if s[2] == "RunTask"]
longest = sorted(tops, key=lambda s: -s[1])[:int(sys.argv[3]) if len(sys.argv) > 3 else 8]
print("longest tasks:")
for ts, dur, _, _ in longest:
    inner = Counter()
    for (ts2, d2, n2, _), s2 in zip(spans, selfs):
        if ts <= ts2 < ts + dur and n2 not in ("RunTask", "ThreadControllerImpl::RunTask"):
            inner[n2] += max(0, s2)
    print(f"  {dur / 1000:6.1f} ms at {section_at(ts):12s} +{(ts - t0) / 1000:6.0f} ms  " + ", ".join(f"{n} {v / 1000:.1f}" for n, v in inner.most_common(4)))
    for ts2, d2, n2, a2 in spans:
        if ts <= ts2 < ts + dur and n2 == "UpdateLayoutTree" and d2 > 4000:
            print(f"           UpdateLayoutTree {d2 / 1000:.1f} ms, {a2.get('elementCount', '?')} elements")
            # what invalidated style since the previous frame
            prev = max([m for m in mark_ts if m < ts2] or [t0])
            why = Counter()
            for e in ev:
                if e["pid"] == pid and "invalidationTracking" in e.get("cat", "") and prev - 20000 <= e["ts"] <= ts2:
                    d = e.get("args", {}).get("data", {})
                    why[f"{e['name'].replace('InvalidationTracking', '')}: {d.get('reason') or d.get('invalidationSet', {}) and 'set' or ''} {d.get('nodeName', '')[:40]} {str(d.get('changedClass') or d.get('changedAttribute') or d.get('changedId') or d.get('changedPseudo') or '')[:30]}"] += 1
            for w, c in why.most_common(6):
                print(f"             {c:4d} x {w}")
    um = Counter(e["name"] for e in ev if e["pid"] == pid and e.get("cat") == "blink.user_timing" and ts <= e["ts"] < ts + dur)
    if um:
        print("           user timing: " + ", ".join(f"{n[:40]} x{c}" for n, c in um.most_common(8)))
    for ts2, d2, n2, a2 in spans:
        if ts <= ts2 < ts + dur and n2 in ("FunctionCall", "TimerFire", "FireAnimationFrame", "EventDispatch") and d2 > 4000:
            d = a2.get("data", {})
            where = f"{d.get('functionName') or ''} {str(d.get('url') or '').split('/')[-1][:60]}:{d.get('lineNumber', '')}" if n2 == "FunctionCall" else d.get("type", "")
            print(f"           {n2} {d2 / 1000:.1f} ms  {where}")

# frames: the gap between consecutive marks; long ones by section and by what the main thread did
long_by_sec, long_work = Counter(), Counter()
for a, b in zip(mark_ts, mark_ts[1:]):
    if b - a > 20_000:
        long_by_sec[section_at(a)] += 1
        for (ts2, d2, n2, _), s2 in zip(spans, selfs):
            if a <= ts2 < b:
                long_work[n2] += max(0, s2)
gaps = [b - a for a, b in zip(mark_ts, mark_ts[1:])]
print(f"frames over 20 ms: {sum(1 for g in gaps if g > 20_000)} of {len(gaps)}; by section: {long_by_sec.most_common()}")
print("  main-thread work inside them (ms): " + ", ".join(f"{n} {v / 1000:.0f}" for n, v in long_work.most_common(8)))

raster = defaultdict(float)
for e in ev:
    if e["pid"] == pid and e.get("ph") == "X" and t0 <= e["ts"] <= t1:
        th = names.get((e["pid"], e["tid"]), "?")
        if th != "CrRendererMain" and e["name"] in ("RasterTask", "ImageDecodeTask", "Decode Image", "Rasterize"):
            raster[(th.rstrip("0123456789/"), e["name"])] += e["dur"] / 1000
print("other threads (ms): " + ", ".join(f"{t}:{n} {v:.0f}" for (t, n), v in sorted(raster.items(), key=lambda kv: -kv[1])[:6]))


paints = Counter()
sample = None
for ts, dur, name, args in spans:
    if name == "Paint":
        d = args.get("data", {})
        sample = sample or d
        paints[(d.get("nodeName") or str(d.get("nodeId")), d.get("layerId"))] += 1
print("paint sample args:", json.dumps(sample)[:300])
print("most repainted:", [(k, v) for k, v in paints.most_common(12)])
lay = [a.get("elementCount", 0) for ts, d, n, a in spans if n == "UpdateLayoutTree"]
print("style recalcs:", len(lay), "elements per recalc (median, p90):", sorted(lay)[len(lay)//2] if lay else 0, sorted(lay)[int(len(lay)*0.9)] if lay else 0)

if "inv" in sys.argv:
    inv = Counter()
    kinds = Counter()
    for e in ev:
        if e["pid"] == pid and "invalidationTracking" in e.get("cat", "") and t0 <= e["ts"] <= t1:
            kinds[e["name"]] += 1
            if e["name"] in ("PaintInvalidationTracking", "LayoutInvalidationTracking", "StyleRecalcInvalidationTracking"):
                d = e.get("args", {}).get("data", {})
                why = d.get("reason", "") or ""
                ex = d.get("extraData") or ""
                inv[(e["name"][:6], str(d.get("nodeName", ""))[:58], f"{why} {str(ex)[:40]}".strip())] += 1
    print("invalidation events:", kinds.most_common(8))
    print("paint invalidations by node and reason:")
    for (k, n, r), c in inv.most_common(30):
        print(f"  {c:5d} {k} {r[:60]:60s} {n}")

# main-thread cost per frame, section by section
frames_in = Counter(section_at(m) for m in mark_ts)
busy_in = Counter()
kind_in = defaultdict(Counter)
for (ts2, d2, n2, _), s2 in zip(spans, selfs):
    sec = section_at(ts2)
    if n2 in ("ThreadControllerImpl::RunTask",):
        busy_in[sec] += d2
    kind_in[sec][n2] += max(0, s2)
print("per section: frames, main-thread ms per frame, top kinds (ms per frame)")
for sec, n in frames_in.most_common():
    tops = ", ".join(f"{k} {v / 1000 / n:.1f}" for k, v in kind_in[sec].most_common(5) if k != "ThreadControllerImpl::RunTask")
    print(f"  {sec:12s} {n:5d}  {busy_in[sec] / 1000 / n:5.1f}  {tops}")
