"""A static preview of the production build inside the persistent Chrome tab.

No server process and no port: the DevTools Fetch domain pauses every request to http://kavalu.preview
and answers it from disk. Pages come from .next/server/app/*.html (RSC payloads from *.rsc), assets
from .next/static, public files from public/, and next/image requests get the original file. Dynamic
routes (/start, /api/*) are not prerendered, so they 404 here; everything else is the real build.
"""
import base64
import json
import mimetypes
import time
import urllib.parse
from pathlib import Path

from framecap import Cap

SITE = Path("C:/shashank/shashank/fnf/ananya_residency/studio_kavalu/website")
APP = SITE / ".next" / "server" / "app"
ORIGIN = "http://kavalu.preview"
TYPES = {".html": "text/html; charset=utf-8", ".rsc": "text/x-component", ".js": "application/javascript",
         ".css": "text/css", ".woff2": "font/woff2", ".svg": "image/svg+xml", ".jpg": "image/jpeg",
         ".png": "image/png", ".json": "application/json", ".txt": "text/plain", ".xml": "application/xml"}


class Preview(Cap):
    def __init__(self):
        # set before Cap.__init__: its first commands already pump events through _handle
        self.fid = 50_000_000
        self.served = 0
        self.missing = []
        self.errors = []
        super().__init__()
        self.cmd("Fetch.enable", {"patterns": [{"urlPattern": ORIGIN + "/*", "requestStage": "Request"}]})
        self.cmd("Log.enable")

    # ---------- serving ----------
    def _resolve(self, url, headers):
        u = urllib.parse.urlsplit(url)
        path = urllib.parse.unquote(u.path)
        q = urllib.parse.parse_qs(u.query)
        if path.startswith("/_next/image"):
            return SITE / "public" / q.get("url", [""])[0].lstrip("/")
        if path.startswith("/_next/static/"):
            return SITE / ".next" / "static" / path[len("/_next/static/"):]
        name = "index" if path in ("", "/") else path.strip("/")
        if any(k.lower() == "rsc" for k in headers) or "_rsc" in q:
            return APP / f"{name}.rsc"
        for cand in (APP / f"{name}.html", APP / f"{name}.body", SITE / "public" / path.lstrip("/")):
            if cand.is_file():
                return cand
        return None

    def _fulfil(self, request_id, code, body, ctype):
        self.fid += 1
        self.ws.send(json.dumps({"id": self.fid, "method": "Fetch.fulfillRequest", "params": {
            "requestId": request_id, "responseCode": code,
            "responseHeaders": [{"name": "Content-Type", "value": ctype}, {"name": "Cache-Control", "value": "no-store"}],
            "body": base64.b64encode(body).decode()}}))

    def _handle(self, msg):
        m = msg.get("method")
        if m == "Fetch.requestPaused":
            p = msg["params"]
            req = p["request"]
            f = self._resolve(req["url"], req.get("headers", {}))
            if f is not None and f.is_file():
                suffix = Path(f.name.removesuffix(".body")).suffix
                self._fulfil(p["requestId"], 200, f.read_bytes(), TYPES.get(suffix) or mimetypes.guess_type(f.name)[0] or "application/octet-stream")
                self.served += 1
            else:
                self.missing.append(req["url"].replace(ORIGIN, ""))
                doc = p.get("resourceType") == "Document"
                body = (APP / "_not-found.html").read_bytes() if doc else b""
                self._fulfil(p["requestId"], 404, body, "text/html; charset=utf-8" if doc else "text/plain")
            return
        if m == "Runtime.exceptionThrown":
            d = msg["params"]["exceptionDetails"]
            self.errors.append("exception: " + (d.get("exception", {}).get("description") or d.get("text", ""))[:300])
        elif m == "Runtime.consoleAPICalled" and msg["params"].get("type") in ("error", "assert"):
            self.errors.append("console: " + " ".join(str(a.get("value", a.get("description", ""))) for a in msg["params"]["args"])[:300])
        elif m == "Log.entryAdded" and msg["params"]["entry"].get("level") == "error":
            e = msg["params"]["entry"]
            if "kavalu.preview" in (e.get("url") or "") or e.get("source") != "network":
                self.errors.append("log: " + e.get("text", "")[:300])
        super()._handle(msg)

    # ---------- driving ----------
    def viewport(self, w=1440, h=900, mobile=False, dpr=1):
        self.cmd("Emulation.setDeviceMetricsOverride", {"width": w, "height": h, "deviceScaleFactor": dpr, "mobile": mobile})
        self.cmd("Emulation.setTouchEmulationEnabled", {"enabled": mobile, **({"maxTouchPoints": 5} if mobile else {})})

    def reduced(self, on):
        self.cmd("Emulation.setEmulatedMedia", {"features": [{"name": "prefers-reduced-motion", "value": "reduce" if on else "no-preference"}]})

    def open(self, path, wait=3.0, intro_seen=True):
        if intro_seen:
            self.cmd("Page.addScriptToEvaluateOnNewDocument", {"source": "try{sessionStorage.setItem('kv-intro','1')}catch(e){}"})
        self.cmd("Page.navigate", {"url": ORIGIN + path}, timeout=40)
        end = time.time() + 30
        while time.time() < end:
            try:
                if self.eval("document.readyState", timeout=5) == "complete":
                    break
            except Exception:
                pass
            self.pump(0.3)
        self.pump(wait)

    def shot(self, path, quality=82, full=False):
        params = {"format": "jpeg", "quality": quality}
        if full:
            params["captureBeyondViewport"] = True
        r = self.cmd("Page.captureScreenshot", params, timeout=60)
        Path(path).write_bytes(base64.b64decode(r["data"]))
        return path

    def scroll_to(self, y, settle=1.2):
        self.eval(f"window.scrollTo(0, {y})")
        self.pump(settle)

    def walk(self, steps=40, dy=1100, x=720, y=450):
        """Wheel through the whole page so every scroll trigger fires, like a reader would."""
        for _ in range(steps):
            self.wheel(dy, 6, 0.03, x, y)
            self.pump(0.1)

    def close(self):
        try:
            self.cmd("Fetch.disable")
            self.reduced(False)
            self.cmd("Emulation.setDeviceMetricsOverride", {"width": 1440, "height": 900, "deviceScaleFactor": 1, "mobile": False})
        finally:
            self.ws.close()
