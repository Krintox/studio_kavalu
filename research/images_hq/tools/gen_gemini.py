"""Generate a same-content, higher-resolution version of one source image with Gemini (gemini.google.com).

    python gen_gemini.py <rel> [--mode "3.1 Pro"] [--strict] [--tag t] [--timeout 600] [--dry]

Runs in our single Gemini tab (gemini_tab.json, its own window) of the persistent Chrome on port 9333:
new chat -> optional model -> 'Create image' tool -> upload (file chooser intercepted over CDP, no native dialog)
-> precise 'keep everything identical' prompt -> wait for the finished image -> save the largest image the page
offers. Never signs in; stops if a sign-in prompt appears. Nothing in website/ is touched.
"""
from __future__ import annotations

import argparse
import base64
import json
import os
import re
import sys
import time

import websocket
from PIL import Image

import cdp_gpt

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SRC_DIR = os.path.join(ROOT, "website", "public", "work")
WORK = os.path.join(ROOT, "research", "images_hq", "gemini", "_work")
STATE = os.path.join(HERE, "gemini_tab.json")
DETAILS = json.load(open(os.path.join(HERE, "details.json"), encoding="utf-8"))
EXTRA = {
    "nivritti/packaging-box": "The small mountain drawing beside the NIVRITTI wordmark on the cream box is the NIVRITTI logo: two "
                              "peaks, a tall left peak and a lower right peak, drawn as a sketchy linocut; keep it exactly as in the "
                              "input, do not redraw it as one rocky peak. Tiny printed text that cannot be read in the input must "
                              "stay faint and unreadable: do not invent any words, letters or numbers. Only the words that are "
                              "readable in the input may be legible: NIVRITTI on the cream box, the large outlined NIVRITTI on the "
                              "dark box, and on the green panel 'WITH COLD-PRESSED HEMP SEED', 'GENTLE FORMULA CLEANSE', "
                              "'LEAVING SKIN' and 'AND BALANCED'.",
    "nivritti/cleanser-bottle": "The label text must read exactly as in the input: 'NIVRITTI' in serif capitals and, below it, the "
                                "second line 'HEMP CLEANSER' (cut off by the bottom edge exactly as in the input). The mountain "
                                "logo above NIVRITTI is the two-peak NIVRITTI mark: a tall left peak and a lower right peak, drawn "
                                "as a sketchy linocut; do not redraw it with three peaks. Keep the dark leafy plant illustration "
                                "on the left of the label as it is.",
}

BASE_PROMPT = (
    "Upscale this image to a high resolution. It must stay exactly the same image: same framing and crop, same aspect "
    "ratio ({ar}), same colours and lighting, the same people with exactly the same faces, identity and expressions, every "
    "object in the same place, and all text and logos letter for letter. Do not add, remove, restyle or reinterpret anything; "
    "only remove blur and compression and make it sharp and detailed."
)


def aspect_text(w, h):
    from math import gcd
    g = gcd(w, h)
    orient = "portrait" if h > w else ("landscape" if w > h else "square")
    return f"{orient}, width:height = {w // g}:{h // g}"


def ensure_tab() -> str:
    st = json.load(open(STATE)) if os.path.exists(STATE) else {}
    alive = {t["id"] for t in cdp_gpt.page_targets()}
    if st.get("targetId") in alive:
        return st["targetId"]
    b = cdp_gpt.browser_conn()
    try:
        r = b.call("Target.createTarget", {"url": "https://gemini.google.com/app", "newWindow": True})
        try:
            w = b.call("Browser.getWindowForTarget", {"targetId": r["targetId"]})
            b.call("Browser.setWindowBounds", {"windowId": w["windowId"], "bounds": {"windowState": "normal"}})
            b.call("Browser.setWindowBounds", {"windowId": w["windowId"], "bounds": {"left": 480, "top": 20, "width": 1000, "height": 800}})
        except Exception:
            pass
        json.dump({"targetId": r["targetId"], "created": time.strftime("%Y-%m-%d %H:%M:%S")}, open(STATE, "w"), indent=1)
        return r["targetId"]
    finally:
        b.close()


def wait_event(p: cdp_gpt.Page, method: str, timeout: float = 15):
    for i, ev in enumerate(p.events):
        if ev.get("method") == method:
            return p.events.pop(i)
    end = time.time() + timeout
    while time.time() < end:
        p.ws.settimeout(max(0.5, end - time.time()))
        try:
            m = json.loads(p.ws.recv())
        except websocket.WebSocketTimeoutException:
            break
        if m.get("method") == method:
            return m
        if "method" in m:
            p.events.append(m)
    return None


def btn_exact(p, label):
    return p.eval("(() => { const b=[...document.querySelectorAll('button')].find(e => (e.getAttribute('aria-label')||'') === %s && e.getBoundingClientRect().width > 0); if(!b) return null; const r=b.getBoundingClientRect(); return [r.left+r.width/2, r.top+r.height/2]; })()" % json.dumps(label))


def menu_item(p, text):
    return p.eval("(() => { const m=[...document.querySelectorAll('[role=menuitem],[role=menuitemradio],[role=menuitemcheckbox],[role=option]')].find(e => e.getBoundingClientRect().width > 0 && (e.innerText||'').includes(%s)); if(!m) return null; const r=m.getBoundingClientRect(); return [r.left+r.width/2, r.top+r.height/2]; })()" % json.dumps(text))


def clear_draft(p):
    for _ in range(4):
        c = btn_exact(p, "close attachment")
        if not c:
            break
        p.click_xy(*c); time.sleep(0.6)
    p.eval("(() => { const el=document.querySelector('div.ql-editor[contenteditable=true]'); if(!el) return; el.focus(); document.execCommand('selectAll', false, null); document.execCommand('delete', false, null); })()")
    time.sleep(0.4)


def capture_fullsize(p, out_dir, timeout=90):
    """Click the last 'Download full size image' button and capture the image response in this tab only (Fetch
    interception). The browser-side download is aborted so nothing lands in the user's Downloads folder."""
    p.call("Fetch.enable", {"patterns": [{"urlPattern": "*googleusercontent.com*", "requestStage": "Response"},
                                         {"urlPattern": "*usercontent.google.com*", "requestStage": "Response"}]})
    try:
        js = ("(() => { const bs=[...document.querySelectorAll('button')].filter(b => (b.getAttribute('aria-label')||'') === "
              "'Download full size image' && b.getBoundingClientRect().width > 0); const b = bs[bs.length-1]; if(!b) return null; "
              "b.scrollIntoView({block:'center'}); const r=b.getBoundingClientRect(); return [r.left+r.width/2, r.top+r.height/2]; })()")
        c = p.eval(js)
        if not c:
            return None
        time.sleep(0.6)
        c = p.eval(js)
        p.click_xy(*c)
        end = time.time() + timeout
        while time.time() < end:
            p.ws.settimeout(2)
            try:
                m = json.loads(p.ws.recv())
            except websocket.WebSocketTimeoutException:
                continue
            if m.get("method") != "Fetch.requestPaused":
                if "method" in m:
                    p.events.append(m)
                continue
            prm = m["params"]; rid = prm["requestId"]
            hdrs = {h["name"].lower(): h["value"] for h in prm.get("responseHeaders", [])}
            ct = hdrs.get("content-type", "")
            if prm.get("responseStatusCode") == 200 and ct.startswith("image/"):
                body = p.call("Fetch.getResponseBody", {"requestId": rid})
                data = base64.b64decode(body["body"]) if body.get("base64Encoded") else body["body"].encode()
                ext = ".png" if "png" in ct else (".webp" if "webp" in ct else ".jpg")
                fn = os.path.join(out_dir, "raw_0" + ext)
                open(fn, "wb").write(data)
                p.call("Fetch.failRequest", {"requestId": rid, "errorReason": "Aborted"})
                return fn
            p.call("Fetch.continueRequest", {"requestId": rid})
        return None
    finally:
        try:
            p.call("Fetch.disable")
        except Exception:
            pass


STATE_JS = r"""
(() => {
  const resp = [...document.querySelectorAll('model-response')];
  const last = resp[resp.length - 1];
  const imgs = last ? [...last.querySelectorAll('img')].map(i => ({src: i.currentSrc || i.src, alt: i.alt || '', nw: i.naturalWidth,
      nh: i.naturalHeight, done: i.complete})) : [];
  const busy = [...document.querySelectorAll('button')].some(b => /stop response|stop/i.test(b.getAttribute('aria-label') || '') && b.getBoundingClientRect().width > 0);
  return {n: resp.length, busy, imgs, text: last ? last.innerText.slice(0, 800) : '',
          signin: !![...document.querySelectorAll('a,button')].find(e => /^sign in$/i.test((e.innerText||'').trim()))};
})()
"""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("rel")
    ap.add_argument("--mode", default="")
    ap.add_argument("--tag", default="base")
    ap.add_argument("--note", default="")
    ap.add_argument("--timeout", type=float, default=600)
    ap.add_argument("--dry", action="store_true")
    a = ap.parse_args()

    src = os.path.join(SRC_DIR, a.rel.replace("/", os.sep) + ".jpg")
    wd = os.path.join(WORK, a.rel.replace("/", os.sep), a.tag)
    os.makedirs(wd, exist_ok=True)
    im = Image.open(src).convert("RGB")
    w, h = im.size
    s = 1024 / max(w, h)
    upl = os.path.join(wd, "upload.png")
    (im.resize((round(w * s), round(h * s)), Image.LANCZOS) if s > 1 else im).save(upl)
    prompt = BASE_PROMPT.format(ar=aspect_text(w, h))
    det = DETAILS.get(a.rel, "")
    if det:
        prompt += " Details that must stay exactly as in the input: " + det
    if a.rel in EXTRA:
        prompt += " " + EXTRA[a.rel]
    if a.note:
        prompt += " " + a.note
    meta = {"rel": a.rel, "src_size": [w, h], "tag": a.tag, "mode": a.mode, "prompt": prompt, "started": time.strftime("%Y-%m-%d %H:%M:%S")}
    print("PROMPT:", prompt)

    p = cdp_gpt.Page(ensure_tab())
    try:
        p.goto("https://gemini.google.com/app", wait=3)
        for _ in range(30):
            if p.eval("!!document.querySelector('div.ql-editor[contenteditable=true]')"):
                break
            time.sleep(1)
        clear_draft(p)
        st = p.eval(STATE_JS)
        if st["signin"]:
            print("NOT SIGNED IN - stop and ask the user to sign in by hand")
            return 3
        if a.mode:
            c = p.eval("(() => { const b=[...document.querySelectorAll('button')].find(e => (e.getAttribute('aria-label')||'').startsWith('Open mode picker')); if(!b) return null; const r=b.getBoundingClientRect(); return [r.left+r.width/2, r.top+r.height/2]; })()")
            p.click_xy(*c); time.sleep(1.2)
            mi = menu_item(p, a.mode)
            if mi:
                p.click_xy(*mi); time.sleep(1.0)
            else:
                p.key("Escape")
            meta["mode_set"] = bool(mi)
        # 'Create image' tool
        c = btn_exact(p, "Upload & tools")
        p.click_xy(*c); time.sleep(1.2)
        mi = menu_item(p, "Create image")
        if mi:
            p.click_xy(*mi); time.sleep(1.0)
        else:
            p.key("Escape")
        meta["create_image_tool"] = bool(mi)
        meta["tool_chip"] = p.eval("[...document.querySelectorAll('button')].filter(e => e.getBoundingClientRect().width > 0).map(e => (e.getAttribute('aria-label')||'') + '|' + (e.innerText||'').trim()).filter(t => /image/i.test(t)).slice(0,4)")
        # upload through an intercepted file chooser
        p.call("Page.setInterceptFileChooserDialog", {"enabled": True})
        c = btn_exact(p, "Upload & tools")
        p.click_xy(*c); time.sleep(1.2)
        mi = menu_item(p, "Upload files")
        if not mi:
            print("no 'Upload files' item"); p.key("Escape"); return 4
        p.click_xy(*mi)
        ev = wait_event(p, "Page.fileChooserOpened", 15)
        if not ev:
            print("file chooser did not open"); return 4
        p.call("DOM.setFileInputFiles", {"files": [os.path.abspath(upl)], "backendNodeId": ev["params"]["backendNodeId"]})
        p.call("Page.setInterceptFileChooserDialog", {"enabled": False})
        # wait for the upload preview to finish
        for _ in range(60):
            busy = p.eval("!![...document.querySelectorAll('mat-progress-spinner, .loading, [role=progressbar]')].find(e => e.getBoundingClientRect().width > 0)")
            thumb = p.eval("[...document.querySelectorAll('uploader-file-preview img, .file-preview img, img[alt*=\"preview\" i], img[src^=\"blob:\"]')].filter(i => i.getBoundingClientRect().width > 0).length")
            if thumb and not busy:
                break
            time.sleep(1)
        # prompt
        p.eval("(() => { const el=document.querySelector('div.ql-editor[contenteditable=true]'); el.focus(); })()")
        p.insert_text(prompt)
        time.sleep(0.8)
        p.shot(os.path.join(wd, "before_send.png"))
        if a.dry:
            print("dry run: not sent"); return 0
        c = btn_exact(p, "Send message")
        if not c:
            print("no send button"); return 5
        p.click_xy(*c)
        t0 = time.time()
        meta["sent"] = time.strftime("%Y-%m-%d %H:%M:%S")
        last, stable = None, 0
        st = None
        while time.time() - t0 < a.timeout:
            time.sleep(5)
            st = p.eval(STATE_JS)
            big = sorted([i for i in st["imgs"] if (i["nw"] or 0) >= 300], key=lambda i: -(i["nw"] * i["nh"]))
            cur = big[0]["src"] if big else None
            print("[%4ds] busy=%s imgs=%d cur=%s %s" % (time.time() - t0, st["busy"], len(big), (cur or "")[:70], (big[0]["nw"], big[0]["nh"]) if big else ""))
            if cur and cur == last and not st["busy"] and big[0]["done"]:
                stable += 1
            else:
                stable = 0
            last = cur
            if stable >= 2:
                break
            if not st["busy"] and not big and time.time() - t0 > 40 and st["text"]:
                print("finished without an image")
                break
        meta["elapsed_s"] = int(time.time() - t0)
        meta["response_text"] = st["text"] if st else ""
        p.shot(os.path.join(wd, "final.png"))
        saved = []
        if st and any((i["nw"] or 0) >= 300 for i in st["imgs"]):
            fn = capture_fullsize(p, wd)
            if fn:
                saved.append({"path": fn, "size": Image.open(fn).size, "how": "download full size (intercepted)"})
                print("saved", fn, Image.open(fn).size)
        meta["saved"] = saved
        print("RESPONSE:", (meta["response_text"] or "")[:500])
        return 0 if saved else 6
    finally:
        meta["ended"] = time.strftime("%Y-%m-%d %H:%M:%S")
        json.dump(meta, open(os.path.join(wd, "meta.json"), "w", encoding="utf-8"), indent=2, ensure_ascii=False)
        try:
            p.close()
        except Exception:
            pass


if __name__ == "__main__":
    sys.exit(main())
