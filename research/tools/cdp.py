"""Drive ONE dedicated research tab of the persistent Chrome (port 9333) over raw CDP.

The tab is created once with /json/new and its id remembered in tab_id.txt, so every
script reuses the same tab and the user's own tabs are never touched or closed.
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
STATE = os.path.join(HERE, "tab_id.txt")

DETECT_JS = r"""
(() => {
  const srcs = [...document.scripts].map(s => s.src || '').filter(Boolean);
  const inline = [...document.scripts].filter(s => !s.src).map(s => s.textContent.slice(0, 4000)).join('\n');
  const html = document.documentElement.outerHTML.slice(0, 400000);
  const has = re => srcs.some(u => re.test(u)) || re.test(inline);
  const fonts = [...new Set([...document.fonts].filter(f => f.status === 'loaded').map(f => f.family.replace(/["']/g, '')))].slice(0, 10);
  const vis = el => { const r = el.getBoundingClientRect(); return r.width > 0 && r.height > 0; };
  const h1 = [...document.querySelectorAll('h1,h2')].filter(vis)[0];
  return {
    title: document.title,
    url: location.href,
    height: document.documentElement.scrollHeight,
    bg: getComputedStyle(document.body).backgroundColor,
    fg: getComputedStyle(document.body).color,
    fonts,
    h1: h1 ? h1.innerText.slice(0, 120) : '',
    h1font: h1 ? getComputedStyle(h1).fontFamily.split(',')[0] + ' ' + getComputedStyle(h1).fontSize : '',
    tech: {
      gsap: !!window.gsap || has(/gsap|greensock|TweenMax/i),
      scrolltrigger: !!window.ScrollTrigger || has(/ScrollTrigger/),
      lenis: !!window.lenis || !!window.Lenis || document.documentElement.classList.contains('lenis') || has(/lenis/i),
      locomotive: has(/locomotive/i) || !!document.querySelector('[data-scroll-container]'),
      three: !!window.THREE || has(/three(\.module)?(\.min)?\.js|three@/i) || /three\.js|THREE\./.test(inline),
      ogl: has(/[\/@]ogl[@\/.]|\bogl\.(module\.)?js|from ?["']ogl["']/i),
      pixi: !!window.PIXI || has(/pixi/i),
      barba: !!window.barba || has(/barba/i),
      swup: has(/swup/i),
      taxi: has(/taxi/i),
      framer: !!document.querySelector('#__framer-badge-container, [data-framer-name], [data-framer-component-type]') || /framerusercontent|framer\.com\/m\//.test(html),
      webflow: !!document.documentElement.getAttribute('data-wf-site') || /webflow/i.test(html.slice(0, 20000)),
      next: !!window.__NEXT_DATA__ || !!window.next || /\/_next\//.test(html),
      nuxt: !!window.__NUXT__ || /\/_nuxt\//.test(html),
      astro: /astro-island|\/_astro\//.test(html),
      sveltekit: /__sveltekit|_app\/immutable/.test(html),
      shopify: !!window.Shopify,
      squarespace: /squarespace/i.test(html.slice(0, 50000)),
      wix: /wix\.com|wixstatic/i.test(html.slice(0, 50000)),
      wordpress: /wp-content|wp-includes/.test(html),
      cargo: /cargo\.site|cargocollective/i.test(html.slice(0, 50000)),
      motion: /framer-motion|motion\.dev|data-projection-id/.test(html) || has(/framer-motion/i),
      splitting: has(/splitting|SplitText|split-type/i),
      canvas: document.querySelectorAll('canvas').length,
      video: document.querySelectorAll('video').length,
      img: document.images.length,
      customCursor: !!document.querySelector('[class*="cursor" i]'),
    }
  };
})()
"""


def _req(path: str, method: str = "GET"):
    req = urllib.request.Request(BASE + path, method=method)
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.loads(r.read().decode())


def get_tab_info(new: bool = False):
    tabs = _req("/json/list")
    if not new and os.path.exists(STATE):
        tid = open(STATE).read().strip()
        for t in tabs:
            if t.get("id") == tid and t.get("type") == "page":
                return t
    t = _req("/json/new?about:blank", method="PUT")
    with open(STATE, "w") as f:
        f.write(t["id"])
    return t


class Tab:
    def __init__(self, info=None):
        self.info = info or get_tab_info()
        self.ws = websocket.create_connection(
            self.info["webSocketDebuggerUrl"], timeout=90, suppress_origin=True
        )
        self.mid = 0
        self.call("Page.enable")
        self.call("Runtime.enable")

    def close_ws(self):
        try:
            self.ws.close()
        except Exception:
            pass

    def call(self, method, params=None, timeout=60):
        self.mid += 1
        mid = self.mid
        self.ws.send(json.dumps({"id": mid, "method": method, "params": params or {}}))
        end = time.time() + timeout
        while True:
            left = end - time.time()
            if left <= 0:
                raise TimeoutError(method)
            self.ws.settimeout(max(0.5, left))
            msg = json.loads(self.ws.recv())
            if msg.get("id") == mid:
                if "error" in msg:
                    raise RuntimeError(f"{method}: {msg['error']}")
                return msg.get("result", {})

    def eval(self, expr, timeout=30):
        r = self.call(
            "Runtime.evaluate",
            {"expression": expr, "returnByValue": True, "awaitPromise": True, "timeout": timeout * 1000},
            timeout=timeout + 5,
        )
        if "exceptionDetails" in r:
            return {"__error": str(r["exceptionDetails"].get("exception", {}).get("description", r["exceptionDetails"].get("text")))[:300]}
        return r.get("result", {}).get("value")

    def front(self):
        self.call("Page.bringToFront")
        try:
            self.call("Emulation.setFocusEmulationEnabled", {"enabled": True})
        except Exception:
            pass

    def viewport(self, w=1440, h=900, mobile=False, dpr=1):
        self.call(
            "Emulation.setDeviceMetricsOverride",
            {"width": w, "height": h, "deviceScaleFactor": dpr, "mobile": mobile},
        )
        if mobile:
            self.call("Emulation.setTouchEmulationEnabled", {"enabled": True, "maxTouchPoints": 5})
        else:
            self.call("Emulation.setTouchEmulationEnabled", {"enabled": False})

    def goto(self, url, wait=3.0, timeout=35):
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

    def shot(self, path, quality=70, full=False, clip=None):
        params = {"format": "jpeg", "quality": quality}
        if full:
            params["captureBeyondViewport"] = True
        if clip:
            params["clip"] = clip
        r = self.call("Page.captureScreenshot", params, timeout=60)
        with open(path, "wb") as f:
            f.write(base64.b64decode(r["data"]))
        return path

    def wheel(self, dy, x=720, y=450, steps=10, pause=0.05):
        for _ in range(steps):
            self.call(
                "Input.dispatchMouseEvent",
                {"type": "mouseWheel", "x": x, "y": y, "deltaX": 0, "deltaY": dy / steps},
            )
            time.sleep(pause)

    def move(self, x, y):
        self.call("Input.dispatchMouseEvent", {"type": "mouseMoved", "x": x, "y": y})

    def detect(self):
        return self.eval(DETECT_JS, timeout=20)
