"""Minimal CDP helper for driving ONE ChatGPT tab of the persistent Chrome (port 9333).

Rules this helper follows (see the task brief):
- It never launches, closes or kills the browser, and never closes any tab (its own included).
- Its tab lives in its OWN new window (Target.createTarget newWindow=true), sized so it does not
  fully cover the other window (another agent records frames there).
- It never calls Page.bringToFront; it uses Emulation.setFocusEmulationEnabled on its own tab.
- It never types credentials.

The tab id is remembered in gpt_tab.json next to this file, so every call reuses the same tab.
"""
from __future__ import annotations

import base64
import json
import os
import time
import urllib.request

import websocket

BASE = "http://127.0.0.1:9333"
HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "gpt_tab.json")


def http_json(path: str, method: str = "GET"):
    req = urllib.request.Request(BASE + path, method=method)
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.loads(r.read().decode())


class Conn:
    """One CDP websocket (browser- or page-level) with an event buffer."""

    def __init__(self, ws_url: str, timeout: float = 60):
        self.ws = websocket.create_connection(ws_url, timeout=timeout, suppress_origin=True,
                                              enable_multithread=False)
        self.mid = 0
        self.events: list[dict] = []

    def close(self):
        try:
            self.ws.close()
        except Exception:
            pass

    def call(self, method: str, params: dict | None = None, timeout: float = 60, session: str | None = None):
        self.mid += 1
        mid = self.mid
        msg = {"id": mid, "method": method, "params": params or {}}
        if session:
            msg["sessionId"] = session
        self.ws.send(json.dumps(msg))
        end = time.time() + timeout
        while True:
            left = end - time.time()
            if left <= 0:
                raise TimeoutError(method)
            self.ws.settimeout(max(0.5, left))
            raw = self.ws.recv()
            m = json.loads(raw)
            if m.get("id") == mid:
                if "error" in m:
                    raise RuntimeError(f"{method}: {m['error']}")
                return m.get("result", {})
            if "method" in m:
                self.events.append(m)
                if len(self.events) > 2000:
                    self.events = self.events[-1000:]


def browser_conn() -> Conn:
    v = http_json("/json/version")
    return Conn(v["webSocketDebuggerUrl"])


def page_targets():
    return [t for t in http_json("/json/list") if t.get("type") == "page"]


def load_state() -> dict:
    if os.path.exists(STATE):
        with open(STATE, encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_state(st: dict):
    with open(STATE, "w", encoding="utf-8") as f:
        json.dump(st, f, indent=2)


def ensure_tab(url: str = "https://chatgpt.com/", bounds: dict | None = None) -> str:
    """Return the id of our own ChatGPT tab, creating it in a NEW WINDOW if needed."""
    st = load_state()
    alive = {t["id"] for t in page_targets()}
    if st.get("targetId") in alive:
        return st["targetId"]
    b = browser_conn()
    try:
        r = b.call("Target.createTarget", {"url": url, "newWindow": True})
        tid = r["targetId"]
        try:
            w = b.call("Browser.getWindowForTarget", {"targetId": tid})
            wid = w["windowId"]
            # normal state first, then a size/position that leaves part of the other window uncovered
            b.call("Browser.setWindowBounds", {"windowId": wid, "bounds": {"windowState": "normal"}})
            b.call("Browser.setWindowBounds", {"windowId": wid, "bounds": bounds or {
                "left": 520, "top": 10, "width": 1000, "height": 800}})
        except Exception as e:  # noqa: BLE001
            wid = None
            print("window bounds not set:", e)
        st = {"targetId": tid, "windowId": wid, "created": time.strftime("%Y-%m-%d %H:%M:%S")}
        save_state(st)
        return tid
    finally:
        b.close()


class Page(Conn):
    def __init__(self, target_id: str | None = None, timeout: float = 90):
        self.target_id = target_id or ensure_tab()
        super().__init__(f"ws://127.0.0.1:9333/devtools/page/{self.target_id}", timeout=timeout)
        self.call("Page.enable")
        self.call("Runtime.enable")
        self.call("DOM.enable")
        try:
            self.call("Emulation.setFocusEmulationEnabled", {"enabled": True})
        except Exception:
            pass

    # ---- JS -------------------------------------------------------------------------------
    def eval(self, expr: str, timeout: float = 30, await_promise: bool = True):
        r = self.call("Runtime.evaluate", {
            "expression": expr, "returnByValue": True, "awaitPromise": await_promise,
            "timeout": int(timeout * 1000), "userGesture": True,
        }, timeout=timeout + 10)
        if "exceptionDetails" in r:
            d = r["exceptionDetails"]
            raise RuntimeError("JS error: " + str(d.get("exception", {}).get("description", d.get("text")))[:800])
        return r.get("result", {}).get("value")

    # ---- navigation -----------------------------------------------------------------------
    def goto(self, url: str, wait: float = 3.0, timeout: float = 45):
        try:
            self.call("Page.navigate", {"url": url}, timeout=timeout)
        except TimeoutError:
            pass
        end = time.time() + timeout
        while time.time() < end:
            try:
                if self.eval("document.readyState", timeout=5) == "complete":
                    break
            except Exception:
                pass
            time.sleep(0.5)
        time.sleep(wait)

    # ---- screenshots ----------------------------------------------------------------------
    def shot(self, path: str, fmt: str = "png", quality: int = 80, full: bool = False):
        params = {"format": fmt}
        if fmt == "jpeg":
            params["quality"] = quality
        if full:
            params["captureBeyondViewport"] = True
        r = self.call("Page.captureScreenshot", params, timeout=90)
        with open(path, "wb") as f:
            f.write(base64.b64decode(r["data"]))
        return path

    # ---- input ----------------------------------------------------------------------------
    def insert_text(self, text: str):
        self.call("Input.insertText", {"text": text})

    def key(self, key: str = "Enter", code: str | None = None, vk: int | None = None, mods: int = 0):
        code = code or key
        vk = vk or {"Enter": 13, "Escape": 27, "Tab": 9, "Backspace": 8}.get(key, 0)
        base = {"key": key, "code": code, "windowsVirtualKeyCode": vk, "nativeVirtualKeyCode": vk, "modifiers": mods}
        if key == "Enter":
            base["text"] = "\r"
        self.call("Input.dispatchKeyEvent", {"type": "keyDown", **base})
        base.pop("text", None)
        self.call("Input.dispatchKeyEvent", {"type": "keyUp", **base})

    def click_xy(self, x: float, y: float):
        for t in ("mouseMoved", "mousePressed", "mouseReleased"):
            p = {"type": t, "x": x, "y": y}
            if t != "mouseMoved":
                p.update({"button": "left", "clickCount": 1})
            self.call("Input.dispatchMouseEvent", p)
            time.sleep(0.05)

    def center_of(self, selector: str):
        js = f"""(() => {{ const el = document.querySelector({json.dumps(selector)});
            if (!el) return null; el.scrollIntoView({{block:'center'}}); const r = el.getBoundingClientRect();
            return [r.left + r.width/2, r.top + r.height/2, r.width, r.height]; }})()"""
        return self.eval(js)

    def click_sel(self, selector: str) -> bool:
        c = self.center_of(selector)
        if not c or c[2] == 0:
            return False
        self.click_xy(c[0], c[1])
        return True

    def set_files(self, selector: str, paths: list[str]) -> int:
        doc = self.call("DOM.getDocument", {"depth": -1, "pierce": True})
        root = doc["root"]["nodeId"]
        q = self.call("DOM.querySelectorAll", {"nodeId": root, "selector": selector})
        ids = q.get("nodeIds", [])
        if not ids:
            raise RuntimeError(f"no element for {selector}")
        self.call("DOM.setFileInputFiles", {"files": [os.path.abspath(p) for p in paths], "nodeId": ids[0]})
        return len(ids)

    # ---- downloads ------------------------------------------------------------------------
    def fetch_b64(self, url: str, timeout: float = 120) -> tuple[bytes, str]:
        """Fetch a URL inside the page (with its cookies) and return (bytes, content-type)."""
        js = f"""(async () => {{
            const r = await fetch({json.dumps(url)}, {{credentials: 'include'}});
            const ct = r.headers.get('content-type') || '';
            const buf = new Uint8Array(await r.arrayBuffer());
            let s = ''; const CH = 0x8000;
            for (let i = 0; i < buf.length; i += CH) s += String.fromCharCode.apply(null, buf.subarray(i, i + CH));
            return {{status: r.status, ct, b64: btoa(s)}};
        }})()"""
        r = self.eval(js, timeout=timeout)
        if not r or r.get("status") != 200:
            raise RuntimeError(f"fetch failed: {r and r.get('status')}")
        return base64.b64decode(r["b64"]), r.get("ct", "")
