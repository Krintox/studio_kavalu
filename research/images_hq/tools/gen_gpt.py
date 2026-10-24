"""Generate a high-resolution, same-content version of one source image with ChatGPT (web).

    python gen_gpt.py <rel> [--strict] [--note "extra detail"] [--timeout 900] [--dry]

<rel> is the source path relative to website/public/work without extension, e.g. content/red-room-portrait.

Flow (all in our own ChatGPT tab, see cdp_gpt.py): new chat -> "Create image" tool -> upload the source
(Lanczos-enlarged copy, same pixels/aspect) -> precise "recreate exactly" prompt -> wait for the finished
image -> fetch the full-size file inside the page -> save to research/images_hq/gpt/_work/<rel>/.
Nothing in website/ is touched.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time

from PIL import Image

import cdp_gpt

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))  # studio_kavalu
SRC_DIR = os.path.join(ROOT, "website", "public", "work")
WORK = os.path.join(ROOT, "research", "images_hq", "gpt", "_work")
DETAILS = json.load(open(os.path.join(os.path.dirname(__file__), "details.json"), encoding="utf-8"))

BASE_PROMPT = (
    "Improve the quality of my photo and make it clearer and high resolution. "
    "It must stay exactly the same picture: same framing and crop, same aspect ratio ({ar}), same colours and light, "
    "the same people with the same faces and expressions, every object in the same place, and all text and logos "
    "letter for letter. Do not add, remove, restyle or reinterpret anything; only make it sharp and detailed."
)
STRICT_PROMPT = (
    "Improve the quality of my photo and make it clearer and high resolution, as a faithful restoration of this exact "
    "picture. When your result is scaled down to {w}x{h} it should line up with my photo almost pixel for pixel: same "
    "aspect ratio ({ar}) and exactly the same framing (no zoom, re-crop, recentring, extension or mirroring). Keep the "
    "same people exactly as they are (face, identity, hair, expression, clothing), every object, edge and corner piece, "
    "the colours and the lighting, and all text and logos letter for letter in the same font, size and position. "
    "Do not beautify or stylise; only remove blur and compression and add natural fine detail."
)

STATE_JS = r"""
(() => {
  const unitKey = el => { const u = el.closest('[data-chatgpt-search-unit-key]'); return u ? u.getAttribute('data-chatgpt-search-unit-key') : ''; };
  const units = [...document.querySelectorAll('[data-chatgpt-search-unit-key]')];
  const asst = units.filter(u => /:assistant$/.test(u.getAttribute('data-chatgpt-search-unit-key')));
  const last = asst[asst.length - 1];
  const states = [...document.querySelectorAll('[data-talvt-turn-state]')].map(e => e.getAttribute('data-talvt-turn-state'));
  const area = document.querySelector('main') || document.body;
  const imgs = [...area.querySelectorAll('img')].map(i => ({src: i.currentSrc || i.src, alt: i.alt || '',
      nw: i.naturalWidth, nh: i.naturalHeight, done: i.complete, unit: unitKey(i)}));
  const stop = [...document.querySelectorAll('button')].some(b => /stop/i.test(b.getAttribute('aria-label') || '') || b.getAttribute('data-testid') === 'stop-button');
  const txt = (area.innerText || '');
  return {url: location.href, stop, imgs, states, lastState: states[states.length - 1] || '',
          assistantText: last ? last.innerText.slice(0, 1500) : '', tail: txt.slice(-1500), nUnits: units.length};
})()
"""
REFUSAL = re.compile(r"violate our content polic|can.?t help with|cannot help with|unable to (create|generate)|"
                     r"not able to (create|generate)|reached .{0,40}limit|hit .{0,40}limit|limit .{0,30}(image|generat)|"
                     r"try again (later|after|tomorrow)|upgrade", re.I)


LIMIT = re.compile(r"reached .{0,60}limit|hit .{0,60}limit|limit .{0,40}(image|generat|reset)|"
                   r"try again (later|after|tomorrow|in)|upgrade to|more images|resets? (at|in|tomorrow)", re.I)


def is_generated(i: dict, before: set) -> bool:
    return (i["alt"] != "User attachment" and not i["unit"].endswith(":user") and i["src"] not in before
            and (i["nw"] or 0) >= 400 and not i["src"].startswith("data:"))


def aspect_text(w: int, h: int) -> str:
    from math import gcd
    g = gcd(w, h)
    orient = "portrait" if h > w else ("landscape" if w > h else "square")
    return f"{orient}, width:height = {w // g}:{h // g}, about {w / h:.3f}:1"


def prep_upload(src: str, dst: str, long_edge: int = 1024) -> tuple[int, int]:
    im = Image.open(src).convert("RGB")
    w, h = im.size
    s = long_edge / max(w, h)
    if s > 1:
        im = im.resize((round(w * s), round(h * s)), Image.LANCZOS)
    im.save(dst)
    return w, h


def wait_ready(p: cdp_gpt.Page, timeout: float = 40):
    end = time.time() + timeout
    while time.time() < end:
        ok = p.eval("!!document.querySelector('.ProseMirror') && document.querySelectorAll('input[type=file]').length > 0")
        if ok:
            return True
        time.sleep(1)
    return False


def select_create_image(p: cdp_gpt.Page) -> bool:
    p.click_sel('button[aria-label="Add files and more"]')
    time.sleep(1.2)
    c = p.eval("""(() => { const b=[...document.querySelectorAll('button,[role=menuitem],[role=menuitemradio]')]
        .find(e=>(e.innerText||'').trim().startsWith('Create image')); if(!b) return null;
        const r=b.getBoundingClientRect(); return [r.left+r.width/2, r.top+r.height/2]; })()""")
    if not c:
        p.key("Escape")
        return False
    p.click_xy(*c)
    time.sleep(1.0)
    return bool(p.eval("!!document.querySelector('.ProseMirror [data-system-hint-type=\"picture_v2\"]')"))


def clear_draft(p: cdp_gpt.Page):
    """Remove leftover attachments / text from a previous unsent draft."""
    for _ in range(5):
        c = p.eval("""(() => { const f=document.querySelector('form'); if(!f) return null;
            const b=[...f.querySelectorAll('button')].find(x=>/remove|delete/i.test(x.getAttribute('aria-label')||''));
            if(!b) return null; const r=b.getBoundingClientRect(); return [r.left+r.width/2, r.top+r.height/2]; })()""")
        if not c:
            break
        p.click_xy(*c)
        time.sleep(0.8)
    p.eval("(() => { const el=document.querySelector('.ProseMirror'); if(!el) return; el.focus(); "
           "document.execCommand('selectAll', false, null); document.execCommand('delete', false, null); })()")
    time.sleep(0.4)


def upload(p: cdp_gpt.Page, path: str, timeout: float = 60) -> bool:
    # the general "Add photos & files" input accepts everything; fall back to the image-only one
    sel = 'input[type=file]:not([accept])'
    try:
        has_generic = p.eval("[...document.querySelectorAll('input[type=file]')].some(i => !i.accept)")
        sel = 'input[type=file]:not([accept]), input[type=file][accept=""]' if has_generic else 'input[type=file][accept^="image"][multiple]'
        p.set_files(sel, [path])
    except Exception as e:  # noqa: BLE001
        print("upload error:", e)
        return False
    end = time.time() + timeout
    while time.time() < end:
        st = p.eval("""(() => { const imgs=[...document.querySelectorAll('form img, [class*=composer] img')];
            const busy=[...document.querySelectorAll('form [role=progressbar], form svg circle[stroke-dasharray], form .animate-spin')].length;
            const send=document.querySelector('button[aria-label="Send"], button[data-testid="send-button"]');
            return {thumbs: imgs.length, busy, sendDisabled: send ? send.disabled : null}; })()""")
        if st["thumbs"] > 0 and st["busy"] == 0:
            return True
        time.sleep(1)
    return False


def type_prompt(p: cdp_gpt.Page, text: str):
    p.eval("(() => { const el=document.querySelector('.ProseMirror'); el.focus(); "
           "const s=window.getSelection(); s.selectAllChildren(el); s.collapseToEnd(); })()")
    p.insert_text(text)
    time.sleep(0.6)


def send(p: cdp_gpt.Page) -> bool:
    for _ in range(30):
        c = p.eval("""(() => { const b=document.querySelector('button[data-testid="send-button"], button[aria-label="Send"], button[aria-label="Send prompt"]');
            if(!b || b.disabled) return null; const r=b.getBoundingClientRect(); return [r.left+r.width/2, r.top+r.height/2]; })()""")
        if c:
            p.click_xy(*c)
            return True
        time.sleep(1)
    return False


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("rel")
    ap.add_argument("--strict", action="store_true")
    ap.add_argument("--note", default="")
    ap.add_argument("--timeout", type=float, default=900)
    ap.add_argument("--dry", action="store_true", help="prepare and type, but do not send")
    ap.add_argument("--tag", default="")
    ap.add_argument("--prompt", default="", help="use this exact prompt instead of the built-in ones")
    ap.add_argument("--no-details", action="store_true")
    a = ap.parse_args()

    src = os.path.join(SRC_DIR, a.rel.replace("/", os.sep) + ".jpg")
    tag = a.tag or ("strict" if a.strict else "base")
    wd = os.path.join(WORK, a.rel.replace("/", os.sep), tag)
    os.makedirs(wd, exist_ok=True)
    upl = os.path.join(wd, "upload.png")
    w, h = prep_upload(src, upl)
    ar = aspect_text(w, h)
    prompt = a.prompt or (STRICT_PROMPT if a.strict else BASE_PROMPT).format(ar=ar, w=w, h=h)
    det = "" if (a.no_details or a.prompt) else DETAILS.get(a.rel, "")
    if det:
        prompt += " Details that must stay exactly as in the input: " + det
    if a.note:
        prompt += " " + a.note
    meta = {"rel": a.rel, "src": src, "src_size": [w, h], "tag": tag, "prompt": prompt,
            "started": time.strftime("%Y-%m-%d %H:%M:%S")}
    print("PROMPT:", prompt)

    p = cdp_gpt.Page()
    try:
        p.goto("https://chatgpt.com/", wait=2.5)
        if not wait_ready(p):
            p.shot(os.path.join(wd, "not_ready.png"))
            print("composer not ready (logged out? wall?) - see not_ready.png")
            return 2
        status = p.eval("({t: document.body.innerText.slice(0,400), login: [...document.querySelectorAll('button,a')].some(b=>/^log in$/i.test((b.innerText||'').trim()))})")
        if status["login"]:
            print("LOGGED OUT - stop and ask the user to log in by hand")
            return 3
        clear_draft(p)
        meta["create_image_mode"] = select_create_image(p)
        if not meta["create_image_mode"]:
            time.sleep(2)
            meta["create_image_mode"] = select_create_image(p)
        print("create-image mode:", meta["create_image_mode"])
        if not upload(p, upl):
            p.shot(os.path.join(wd, "upload_failed.png"))
            print("upload failed")
            return 4
        type_prompt(p, prompt)
        p.shot(os.path.join(wd, "before_send.png"))
        if a.dry:
            print("dry run: typed, not sent")
            return 0
        before = {i["src"] for i in p.eval(STATE_JS)["imgs"]}
        if not send(p):
            p.shot(os.path.join(wd, "send_failed.png"))
            print("send failed")
            return 5
        t0 = time.time()
        meta["sent"] = time.strftime("%Y-%m-%d %H:%M:%S")
        last_src, stable, shot_i = None, 0, 0
        result = None
        seen_srcs = []
        while time.time() - t0 < a.timeout:
            time.sleep(5)
            try:
                st = p.eval(STATE_JS)
            except Exception as e:  # noqa: BLE001
                print("poll error", e)
                continue
            el = int(time.time() - t0)
            gen = [i for i in st["imgs"] if is_generated(i, before)]
            for i in gen:
                if i["src"] not in seen_srcs:
                    seen_srcs.append(i["src"])
                    print("   new img:", json.dumps({k: (v[:120] if isinstance(v, str) else v) for k, v in i.items()}))
            if el // 60 >= shot_i:
                p.shot(os.path.join(wd, f"progress_{shot_i:02d}.png"))
                shot_i += 1
            big = sorted(gen, key=lambda i: -(i["nw"] * i["nh"]))
            cur = big[0]["src"] if big else None
            done_turn = st["lastState"] == "complete" and not st["stop"]
            print(f"[{el:4d}s] state={st['lastState']} stop={st['stop']} gen={len(gen)} "
                  f"cur={(cur or '')[:80]} {big[0]['nw'] if big else ''}x{big[0]['nh'] if big else ''}")
            if cur and cur == last_src and done_turn and big[0]["done"]:
                stable += 1
            else:
                stable = 0
            last_src = cur
            if stable >= 2:
                result = st
                break
            if done_turn and not gen and el > 15:
                at = st["assistantText"]
                if at and (REFUSAL.search(at) or el > 120):
                    print("assistant finished without an image")
                    result = st
                    break
        meta["elapsed_s"] = int(time.time() - t0)
        st = result or p.eval(STATE_JS)
        meta["assistant_text"] = st["assistantText"]
        meta["conversation_url"] = st["url"]
        p.shot(os.path.join(wd, "final.png"))
        gen = [i for i in st["imgs"] if is_generated(i, before)]
        seen, saved = set(), []
        for k, im in enumerate(sorted(gen, key=lambda i: -(i["nw"] * i["nh"]))):
            if im["src"] in seen:
                continue
            seen.add(im["src"])
            try:
                data, ct = p.fetch_b64(im["src"])
            except Exception as e:  # noqa: BLE001
                print("fetch failed", e)
                continue
            ext = ".png" if "png" in ct else (".webp" if "webp" in ct else (".jpg" if "jp" in ct else ".bin"))
            out = os.path.join(wd, f"raw_{k}{ext}")
            with open(out, "wb") as f:
                f.write(data)
            try:
                sz = Image.open(out).size
            except Exception:  # noqa: BLE001
                sz = None
            saved.append({"path": out, "ct": ct, "size": sz, "alt": im["alt"], "src": im["src"][:200]})
        meta["saved"] = saved
        print(json.dumps(saved, indent=1))
        print("ASSISTANT:", st["assistantText"][:800])
        if saved:
            return 0
        if LIMIT.search(st["assistantText"] or ""):
            print("LIMIT REACHED")
            return 7
        return 6
    finally:
        meta["ended"] = time.strftime("%Y-%m-%d %H:%M:%S")
        with open(os.path.join(wd, "meta.json"), "w", encoding="utf-8") as f:
            json.dump(meta, f, indent=2, ensure_ascii=False)
        p.close()


if __name__ == "__main__":
    sys.exit(main())
