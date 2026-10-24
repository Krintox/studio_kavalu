"""Q7 motion study: record how a reference site's motion is made, frame by frame.

For one site and a scripted scenario (scroll / hover / click), it captures:
  * every painted frame (Page.startScreencast, ~16 ms apart),
  * a per-frame log, from requestAnimationFrame, of the page position, size, scale, rotation and
    opacity of up to 140 candidate elements,
  * CSS transitions / animations / Web Animations the browser starts (Animation domain), with their
    real duration, delay and easing.
Then it finds the elements that moved, and fits each motion's progress curve against standard eases
to estimate its duration and easing. Outputs go to research/motion_frames/sites/<slug>/.

    motion_study.py <slug> <url> <scenario-json>
scenario: a list of steps, e.g. [["wait",2],["wheel",900,30,0.03],["hover",720,450],["click",720,450],["pump",2]]
"""
import json
import math
import sys
import time
from pathlib import Path

from framecap import Cap, contact_sheet

OUT_ROOT = Path("C:/shashank/shashank/fnf/ananya_residency/studio_kavalu/research/motion_frames/sites")

SAMPLER = r"""
(() => {
  const H = innerHeight;
  const all = [...document.querySelectorAll('img,video,canvas,svg,figure,picture,h1,h2,h3,p,a,button,li,article,[class*=card i],[class*=item i],[class*=stamp i],[class*=sheet i],[class*=tile i],[class*=project i],[style*=transform]')];
  const vis = all.map(e => [e, e.getBoundingClientRect()]).filter(([e, r]) => r.width * r.height > 900 && r.bottom > -H && r.top < 2.2 * H);
  vis.sort((a, b) => b[1].width * b[1].height - a[1].width * a[1].height);
  const els = vis.slice(0, 140).map(([e]) => e);
  const name = e => (e.tagName.toLowerCase() + (e.id ? '#' + e.id : '') + (typeof e.className === 'string' && e.className ? '.' + e.className.trim().split(/\s+/).slice(0, 2).join('.') : '')).slice(0, 70);
  window.__ms = { t0: performance.now(), names: els.map(name), frames: [] };
  const dec = m => { // a, b from matrix(a,b,c,d,e,f) -> scale, rotation
    if (!m || m === 'none') return [1, 0];
    const v = m.match(/matrix(3d)?\(([^)]+)\)/); if (!v) return [1, 0];
    const n = v[2].split(',').map(Number); const a = n[0], b = n[1];
    return [+(Math.hypot(a, b)).toFixed(4), +(Math.atan2(b, a) * 180 / Math.PI).toFixed(2)];
  };
  const tick = () => {
    if (!window.__ms || window.__ms.frames.length > 1500) return;
    const sy = scrollY;
    window.__ms.frames.push({ t: +(performance.now() - window.__ms.t0).toFixed(1), sy: Math.round(sy),
      e: els.map(e => { const r = e.getBoundingClientRect(); const cs = getComputedStyle(e); const [s, rot] = dec(cs.transform);
        return [Math.round(r.x), Math.round(r.y + sy), Math.round(r.width), Math.round(r.height), +(+cs.opacity).toFixed(3), s, rot]; }) });
    requestAnimationFrame(tick);
  };
  requestAnimationFrame(tick);
  return els.length;
})()
"""

EASES = {
    "linear": lambda x: x,
    "power1.out (quad)": lambda x: 1 - (1 - x) ** 2,
    "power2.out (cubic)": lambda x: 1 - (1 - x) ** 3,
    "power3.out (quart)": lambda x: 1 - (1 - x) ** 4,
    "power4.out (quint)": lambda x: 1 - (1 - x) ** 5,
    "expo.out": lambda x: 1 if x >= 1 else 1 - 2 ** (-10 * x),
    "sine.inOut": lambda x: -(math.cos(math.pi * x) - 1) / 2,
    "power2.inOut": lambda x: 4 * x ** 3 if x < 0.5 else 1 - (-2 * x + 2) ** 3 / 2,
    "power3.inOut": lambda x: 8 * x ** 4 if x < 0.5 else 1 - (-2 * x + 2) ** 4 / 2,
    "expo.inOut": lambda x: 0 if x <= 0 else 1 if x >= 1 else (2 ** (20 * x - 10) / 2 if x < 0.5 else (2 - 2 ** (-20 * x + 10)) / 2),
    "back.out(1.7)": lambda x: 1 + 2.70158 * (x - 1) ** 3 + 1.70158 * (x - 1) ** 2,
}


def fit_ease(ts, ps):
    """ts in ms (start at 0), ps progress 0..1 -> (best ease, duration ms, rms)."""
    dur = ts[-1] - ts[0] or 1
    xs = [(t - ts[0]) / dur for t in ts]
    best = None
    for name, f in EASES.items():
        err = math.sqrt(sum((f(x) - p) ** 2 for x, p in zip(xs, ps)) / len(xs))
        if best is None or err < best[2]:
            best = (name, round(dur), round(err, 3))
    return best


def analyse(log):
    frames, names = log["frames"], log["names"]
    if len(frames) < 3:
        return []
    out = []
    for i, nm in enumerate(names):
        rows = [(f["t"], f["sy"], f["e"][i]) for f in frames if i < len(f["e"])]
        # per channel: page x, page y, w, opacity, scale, rotation
        chans = {"x": [r[2][0] for r in rows], "y": [r[2][1] for r in rows], "w": [r[2][2] for r in rows],
                 "opacity": [r[2][4] for r in rows], "scale": [r[2][5] for r in rows], "rot": [r[2][6] for r in rows]}
        ts = [r[0] for r in rows]
        moved = {}
        for k, v in chans.items():
            lo, hi = min(v), max(v)
            thr = {"x": 6, "y": 6, "w": 6, "opacity": 0.08, "scale": 0.02, "rot": 0.8}[k]
            if hi - lo < thr:
                continue
            # active window: first and last frame where it differs from its neighbours
            ch = [j for j in range(1, len(v)) if abs(v[j] - v[j - 1]) > thr / 20]
            if not ch:
                continue
            a, b = ch[0] - 1, ch[-1]
            seg_t, seg_v = ts[a:b + 1], v[a:b + 1]
            span = seg_v[-1] - seg_v[0]
            if abs(span) < thr:
                moved[k] = {"from": seg_v[0], "to": seg_v[-1], "range": [lo, hi], "start_ms": round(seg_t[0]), "note": "oscillates / returns"}
                continue
            ps = [(x - seg_v[0]) / span for x in seg_v]
            ease, dur, rms = fit_ease(seg_t, ps)
            moved[k] = {"from": seg_v[0], "to": seg_v[-1], "start_ms": round(seg_t[0]), "duration_ms": dur, "ease_fit": ease, "rms": rms}
        if moved:
            out.append({"el": nm, "moves": moved})
    return out


def main():
    slug, url, scenario = sys.argv[1], sys.argv[2], json.loads(sys.argv[3])
    out = OUT_ROOT / slug
    out.mkdir(parents=True, exist_ok=True)
    cap = Cap()
    anims = []
    orig = cap._handle

    def handle(msg):  # keep the Animation domain events alongside the screencast frames
        if msg.get("method") == "Animation.animationStarted":
            a = msg["params"]["animation"]
            src = a.get("source") or {}
            anims.append({"type": a.get("type"), "name": a.get("name"), "duration": src.get("duration"), "delay": src.get("delay"),
                          "easing": src.get("easing"), "iterations": src.get("iterations"), "target": (src.get("backendNodeId"))})
        return orig(msg)

    cap._handle = handle
    cap.goto(url, wait=5)
    cap.cmd("Animation.enable")
    title = cap.eval("document.title")
    print("page:", title)
    n = cap.eval(SAMPLER)
    print("sampling", n, "elements")
    cap.frames = []
    cap.cmd("Page.startScreencast", {"format": "jpeg", "quality": 60, "maxWidth": 960, "maxHeight": 600, "everyNthFrame": 1})
    for step in scenario:
        kind = step[0]
        if kind == "wait" or kind == "pump":
            cap.pump(step[1])
        elif kind == "wheel":
            cap.wheel(step[1], step[2], step[3])
        elif kind in ("hover", "click"):
            x, y = step[1], step[2]
            for k in range(8):  # glide there, so hover effects see a real approach
                cap.cmd("Input.dispatchMouseEvent", {"type": "mouseMoved", "x": x - (8 - k) * 12, "y": y})
                cap.pump(0.02)
            if kind == "click":
                cap.cmd("Input.dispatchMouseEvent", {"type": "mousePressed", "x": x, "y": y, "button": "left", "clickCount": 1})
                cap.cmd("Input.dispatchMouseEvent", {"type": "mouseReleased", "x": x, "y": y, "button": "left", "clickCount": 1})
        elif kind == "eval":
            cap.eval(step[1])
        cap.pump(0.05)
    cap.cmd("Page.stopScreencast")
    log = json.loads(cap.eval("JSON.stringify(window.__ms || {frames: [], names: []})") or "{}")
    moves = analyse(log)
    (out / "log.json").write_text(json.dumps(log), encoding="utf-8")
    (out / "analysis.json").write_text(json.dumps({"url": url, "title": title, "scenario": scenario, "moves": moves, "css_web_animations": anims[:300]}, indent=1), encoding="utf-8")
    contact_sheet(cap.frames, out / "sheet.jpg", 16, 4, f"{title[:60]} — {len(cap.frames)} frames")
    contact_sheet(cap.frames, out / "sheet_all.jpg", min(48, len(cap.frames)), 8, f"{slug} — all frames (sampled)")
    print("frames:", len(cap.frames), "| moving elements:", len(moves), "| CSS/WAAPI animations:", len(anims))
    for m in moves[:14]:
        print("  ", m["el"][:60], {k: (v.get("duration_ms"), v.get("ease_fit"), v.get("from"), v.get("to")) if "duration_ms" in v else v.get("note") for k, v in m["moves"].items()})
    seen = {}
    for a in anims:
        key = (a["type"], a["name"], a["duration"], a["easing"])
        seen[key] = seen.get(key, 0) + 1
    for (t, nme, d, e), c in sorted(seen.items(), key=lambda kv: -kv[1])[:12]:
        print(f"   {c:3d} x {t} {nme} {d}ms {e}")
    cap.ws.close()


if __name__ == "__main__":
    main()
