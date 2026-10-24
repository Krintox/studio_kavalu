"""Render a local HTML file to PNG in our OWN render target of the persistent Chrome (port 9333).

    python render.py <page.html> <out.png> <css_w> <css_h> [dpr=3]

The render target is created once (hidden target if Chrome supports it, otherwise its own small new window)
and remembered in render_tab.json. It is never closed, and no other tab is touched.
"""
from __future__ import annotations

import base64
import json
import os
import pathlib
import sys
import time

import cdp_gpt

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "render_tab.json")


class SessionPage:
    """Page-like wrapper over a flattened Target.attachToTarget session (works for hidden targets)."""

    def __init__(self, target_id: str):
        self.b = cdp_gpt.browser_conn()
        r = self.b.call("Target.attachToTarget", {"targetId": target_id, "flatten": True})
        self.sid = r["sessionId"]
        for m in ("Page.enable", "Runtime.enable"):
            self.call(m)

    def call(self, method, params=None, timeout=60):
        return self.b.call(method, params, timeout=timeout, session=self.sid)

    def eval(self, expr, timeout=30):
        r = self.call("Runtime.evaluate", {"expression": expr, "returnByValue": True, "awaitPromise": True,
                                           "timeout": int(timeout * 1000)}, timeout=timeout + 10)
        if "exceptionDetails" in r:
            raise RuntimeError(str(r["exceptionDetails"])[:500])
        return r.get("result", {}).get("value")

    def goto(self, url, wait=0.3, timeout=60):
        try:
            self.call("Page.navigate", {"url": url}, timeout=timeout)
        except TimeoutError:
            pass
        end = time.time() + timeout
        while time.time() < end:
            try:
                if self.eval("document.readyState", timeout=5) == "complete":
                    break
            except Exception:  # noqa: BLE001
                pass
            time.sleep(0.3)
        time.sleep(wait)

    def close(self):
        try:
            self.call("Target.detachFromTarget", {"sessionId": self.sid})
        except Exception:  # noqa: BLE001
            pass
        self.b.close()


def target_alive(tid: str) -> bool:
    b = cdp_gpt.browser_conn()
    try:
        infos = b.call("Target.getTargets").get("targetInfos", [])
        return any(t["targetId"] == tid for t in infos)
    finally:
        b.close()


def ensure_render_tab() -> str:
    st = json.load(open(STATE)) if os.path.exists(STATE) else {}
    if st.get("targetId") and target_alive(st["targetId"]):
        return st["targetId"]
    b = cdp_gpt.browser_conn()
    try:
        mode = "window"
        r = b.call("Target.createTarget", {"url": "about:blank", "newWindow": True, "background": True})
        try:
            w = b.call("Browser.getWindowForTarget", {"targetId": r["targetId"]})
            b.call("Browser.setWindowBounds", {"windowId": w["windowId"], "bounds": {"windowState": "normal"}})
            b.call("Browser.setWindowBounds", {"windowId": w["windowId"], "bounds": {
                "left": 40, "top": 60, "width": 640, "height": 560}})
        except Exception as e2:  # noqa: BLE001
            print("bounds:", e2)
        st = {"targetId": r["targetId"], "mode": mode, "created": time.strftime("%Y-%m-%d %H:%M:%S")}
        json.dump(st, open(STATE, "w"), indent=2)
        return r["targetId"]
    finally:
        b.close()


def render(html: str, out: str, css_w: int, css_h: int, dpr: float = 3, settle: float = 0.8, js: str | None = None):
    tid = ensure_render_tab()
    p = SessionPage(tid)
    try:
        p.call("Emulation.setDeviceMetricsOverride", {"width": int(css_w), "height": int(css_h),
                                                      "deviceScaleFactor": dpr, "mobile": False})
        url = pathlib.Path(os.path.abspath(html)).as_uri() + f"?t={int(time.time() * 1000)}"
        p.goto(url, wait=0.3, timeout=60)
        p.eval("document.fonts.ready.then(() => true)", timeout=60)
        p.eval("Promise.all([...document.images].map(i => i.complete ? 1 : new Promise(r => { i.onload = i.onerror = r; })))",
               timeout=60)
        time.sleep(settle)
        r = p.call("Page.captureScreenshot", {"format": "png", "captureBeyondViewport": True,
                                              "clip": {"x": 0, "y": 0, "width": css_w, "height": css_h, "scale": 1}},
                   timeout=120)
        data = base64.b64decode(r["data"])
        os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
        with open(out, "wb") as f:
            f.write(data)
        from PIL import Image
        size = Image.open(out).size
        if js:
            return size, p.eval(js, timeout=60)
        return size
    finally:
        p.close()


def css_size_for(src_w: int, src_h: int, dpr: float = 3, min_long: int = 2400) -> tuple[int, int]:
    long_css = -(-min_long // dpr)  # ceil
    if src_w >= src_h:
        w = int(long_css)
        h = round(w * src_h / src_w)
    else:
        h = int(long_css)
        w = round(h * src_w / src_h)
    return w, h


if __name__ == "__main__":
    html, out, w, h = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
    dpr = float(sys.argv[5]) if len(sys.argv) > 5 else 3
    print(render(html, out, w, h, dpr))
