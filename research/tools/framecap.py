"""Frame-by-frame motion capture in the persistent Chrome (one dedicated tab).

Uses Page.startScreencast (every painted frame, ~16 ms apart at 60 fps) and, in parallel, a requestAnimationFrame
logger inside the page that records the bounding box, transform, opacity and clip-path of chosen elements on every
frame. Together they show what moves, by how much, over how long, and with what easing.

    framecap.py footer <out_dir> <url> [<url> ...]   scroll to the bottom of each page and record the footer reveal
"""
import base64
import json
import sys
import time
from pathlib import Path

import websocket
from PIL import Image, ImageDraw, ImageFont

from cdp import get_tab_info

LOGGER_JS = r"""
(() => {
  if (window.__kvlog) return;
  const pick = () => {
    const out = [];
    const f = document.querySelector('footer') || [...document.querySelectorAll('[class*="footer" i]')].pop();
    if (f) out.push(['footer', f]);
    if (f) {
      // the biggest text-ish and media children of the footer
      const kids = [...f.querySelectorAll('h1,h2,h3,p,span,a,svg,img,canvas,video,div')]
        .filter(e => { const r = e.getBoundingClientRect(); return r.width * r.height > 2000; })
        .sort((a, b) => { const ra = a.getBoundingClientRect(), rb = b.getBoundingClientRect(); return rb.width * rb.height - ra.width * ra.height; })
        .slice(0, 10);
      kids.forEach((k, i) => out.push(['f' + i + ':' + k.tagName.toLowerCase() + '.' + (k.className && k.className.baseVal === undefined ? String(k.className).split(' ')[0] : '').slice(0, 24), k]));
    }
    return out;
  };
  let els = pick();
  const t0 = performance.now();
  window.__kvlog = [];
  const tick = () => {
    if (window.__kvlog.length > 4000) return;
    if (window.__kvlog.length % 30 === 0) els = pick();
    const row = { t: +(performance.now() - t0).toFixed(1), y: Math.round(scrollY), items: {} };
    for (const [name, e] of els) {
      const r = e.getBoundingClientRect(); const cs = getComputedStyle(e);
      row.items[name] = [Math.round(r.x), Math.round(r.y), Math.round(r.width), Math.round(r.height), cs.transform === 'none' ? '' : cs.transform.slice(0, 60), +(+cs.opacity).toFixed(3), cs.clipPath === 'none' ? '' : cs.clipPath.slice(0, 40), cs.position];
    }
    window.__kvlog.push(row);
    requestAnimationFrame(tick);
  };
  requestAnimationFrame(tick);
})()
"""


class Cap:
    def __init__(self):
        info = get_tab_info()
        self.ws = websocket.create_connection(info["webSocketDebuggerUrl"], timeout=60, suppress_origin=True)
        self.mid = 0
        self.frames = []
        self.cmd("Page.enable")
        self.cmd("Runtime.enable")
        self.cmd("Page.bringToFront")
        # without focus emulation a background window never acknowledges synthetic wheel events
        self.cmd("Emulation.setFocusEmulationEnabled", {"enabled": True})
        self.cmd("Emulation.setDeviceMetricsOverride", {"width": 1440, "height": 900, "deviceScaleFactor": 1, "mobile": False})

    def _handle(self, msg):
        if msg.get("method") == "Page.screencastFrame":
            p = msg["params"]
            self.frames.append((p["metadata"]["timestamp"], p["data"]))
            self.ws.send(json.dumps({"id": 10_000_000 + len(self.frames), "method": "Page.screencastFrameAck",
                                     "params": {"sessionId": p["sessionId"]}}))

    def cmd(self, method, params=None, timeout=60):
        self.mid += 1
        mid = self.mid
        self.ws.send(json.dumps({"id": mid, "method": method, "params": params or {}}))
        end = time.time() + timeout
        while time.time() < end:
            self.ws.settimeout(max(0.2, end - time.time()))
            msg = json.loads(self.ws.recv())
            if msg.get("id") == mid:
                return msg.get("result", {})
            self._handle(msg)
        raise TimeoutError(method)

    def pump(self, secs):
        end = time.time() + secs
        while time.time() < end:
            self.ws.settimeout(max(0.05, end - time.time()))
            try:
                self._handle(json.loads(self.ws.recv()))
            except websocket.WebSocketTimeoutException:
                pass

    def eval(self, expr, timeout=20):
        r = self.cmd("Runtime.evaluate", {"expression": expr, "returnByValue": True, "awaitPromise": True}, timeout)
        return r.get("result", {}).get("value")

    def goto(self, url, wait=4.0):
        self.cmd("Page.navigate", {"url": url}, timeout=40)
        end = time.time() + 30
        while time.time() < end:
            try:
                if self.eval("document.readyState") == "complete":
                    break
            except Exception:
                pass
            time.sleep(0.4)
        time.sleep(wait)

    def wheel(self, dy, steps, pause, x=720, y=450):
        for _ in range(steps):
            self.cmd("Input.dispatchMouseEvent", {"type": "mouseWheel", "x": x, "y": y, "deltaX": 0, "deltaY": dy / steps})
            self.pump(pause)


def contact_sheet(frames, out, n=16, cols=4, label=""):
    if not frames:
        return
    idx = [round(i * (len(frames) - 1) / (n - 1)) for i in range(n)] if len(frames) >= n else list(range(len(frames)))
    t0 = frames[0][0]
    ims = []
    font = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 18)
    for i in idx:
        ts, data = frames[i]
        im = Image.open(__import__("io").BytesIO(base64.b64decode(data))).convert("RGB")
        im = im.resize((480, int(480 * im.size[1] / im.size[0])))
        d = ImageDraw.Draw(im)
        d.rectangle((0, 0, 170, 26), fill=(255, 230, 0))
        d.text((6, 2), f"#{i}  {1000 * (ts - t0):.0f} ms", fill="black", font=font)
        ims.append(im)
    w, h = ims[0].size
    rows = (len(ims) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * w + (cols - 1) * 4, rows * h + (rows - 1) * 4 + 30), (20, 20, 20))
    ImageDraw.Draw(sheet).text((8, 4), label, fill="white", font=font)
    for k, im in enumerate(ims):
        sheet.paste(im, ((k % cols) * (w + 4), 30 + (k // cols) * (h + 4)))
    sheet.save(out, quality=82)


def study_footer(cap, url, out_dir):
    slug = url.split("//")[1].split("/")[0].replace("www.", "").replace(".", "-")
    cap.goto(url, wait=4)
    H = cap.eval("innerHeight")
    total = cap.eval("document.documentElement.scrollHeight")
    # jump close to the end (two screens above it), let lazy content settle
    FT = """(() => { const f = document.querySelector('footer') || [...document.querySelectorAll('[class*="footer" i]')].pop();
      return f ? Math.round(f.getBoundingClientRect().top) : null; })()"""
    cap.eval(f"window.scrollTo(0, Math.max(0, {total} - {H} * 2.6))")
    time.sleep(0.6)
    # virtual-scroll sites ignore scrollTo: wheel quickly until the footer is about two screens away
    for _ in range(80):
        top = cap.eval(FT)
        if top is None or top < H * 2.4:
            break
        cap.wheel(min(1600, top - H * 2.2), 4, 0.03)
    time.sleep(1.6)
    cap.eval(LOGGER_JS)
    cap.frames = []
    cap.cmd("Page.startScreencast", {"format": "jpeg", "quality": 60, "maxWidth": 960, "maxHeight": 600, "everyNthFrame": 1})
    cap.pump(0.4)
    cap.wheel(H * 3.2, 40, 0.06)     # ~2.4 s of steady wheel scrolling to the very bottom
    cap.pump(2.2)                     # let reveals / easing settle
    cap.cmd("Input.dispatchMouseEvent", {"type": "mouseMoved", "x": 900, "y": 640})   # hover once, in case the footer reacts
    cap.pump(1.2)
    cap.cmd("Page.stopScreencast")
    log = cap.eval("JSON.stringify(window.__kvlog || [])") or "[]"
    info = cap.eval("""(() => { const f = document.querySelector('footer') || [...document.querySelectorAll('[class*="footer" i]')].pop();
      if (!f) return {found: false};
      const cs = getComputedStyle(f); const r = f.getBoundingClientRect();
      return {found: true, tag: f.tagName, position: cs.position, z: cs.zIndex, h: Math.round(r.height), canvas: f.querySelectorAll('canvas').length,
              video: f.querySelectorAll('video').length, imgs: f.querySelectorAll('img').length, svgs: f.querySelectorAll('svg').length,
              text: (f.innerText || '').replace(/\\s+/g, ' ').slice(0, 400)}; })()""")
    frames = list(cap.frames)
    sub = out_dir / slug
    sub.mkdir(parents=True, exist_ok=True)
    # focus the sheet on the reveal: frames from when the footer's top enters the screen until it stops moving
    try:
        rows = json.loads(log)
        tops = [(r["t"], r["items"].get("footer", [0, None])[1]) for r in rows if r["items"].get("footer")]
        enter = next((t for t, y in tops if y is not None and y < H), None)
        last_move = enter
        for (t1, y1), (t2, y2) in zip(tops, tops[1:]):
            if y1 is not None and y2 is not None and abs(y2 - y1) > 0.5:
                last_move = t2
        if enter is not None:
            t0 = frames[0][0]
            ms = lambda f: 1000 * (f[0] - t0)
            log_t0 = rows[0]["t"]
            # screencast and rAF clocks start within a few ms of each other; align on the first sample
            win = [f for f in frames if enter - log_t0 - 250 <= ms(f) <= last_move - log_t0 + 900]
            if len(win) >= 8:
                frames_for_sheet = win
            else:
                frames_for_sheet = frames
        else:
            frames_for_sheet = frames
    except Exception:
        frames_for_sheet = frames
    contact_sheet(frames_for_sheet, sub / "sheet.jpg", 16, 4, f"{url} — {len(frames)} frames (sheet: footer reveal)")
    contact_sheet(frames, sub / "sheet_all.jpg", 12, 4, f"{url} — all")
    (sub / "log.json").write_text(log, encoding="utf-8")
    (sub / "info.json").write_text(json.dumps(info, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{slug}: {len(frames)} frames, footer={info.get('position') if info else None} h={info.get('h') if info else None} "
          f"canvas={info.get('canvas') if info else None} :: {(info or {}).get('text', '')[:110]}", flush=True)


if __name__ == "__main__":
    mode, out = sys.argv[1], Path(sys.argv[2])
    out.mkdir(parents=True, exist_ok=True)
    cap = Cap()
    cap.cmd("Page.bringToFront")
    cap.cmd("Emulation.setDeviceMetricsOverride", {"width": 1440, "height": 900, "deviceScaleFactor": 1, "mobile": False})
    for url in sys.argv[3:]:
        try:
            if mode == "footer":
                study_footer(cap, url, out)
        except Exception as e:
            print("FAIL", url, str(e)[:120], flush=True)
            try:
                cap.ws.close()
            except Exception:
                pass
            cap = Cap()
    cap.ws.close()
