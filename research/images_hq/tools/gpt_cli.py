"""Small CLI around cdp_gpt.Page for inspecting our own ChatGPT tab.

    python gpt_cli.py open                 # create/reuse our tab (new window) and print its state
    python gpt_cli.py status               # url, title, login/composer hints
    python gpt_cli.py shot out.png         # screenshot of our tab
    python gpt_cli.py eval "<js>"          # evaluate JS in our tab, print JSON result
    python gpt_cli.py dom                  # list buttons / inputs / test-ids useful for automation
    python gpt_cli.py goto <url>
"""
from __future__ import annotations

import json
import sys

import cdp_gpt

STATUS_JS = r"""
(() => {
  const vis = el => { const r = el.getBoundingClientRect(); return r.width > 0 && r.height > 0; };
  const txt = (document.body && document.body.innerText || '').slice(0, 1500);
  return {
    url: location.href, title: document.title,
    composer: !!document.querySelector('#prompt-textarea, div[contenteditable="true"]'),
    fileInputs: [...document.querySelectorAll('input[type=file]')].map(i => ({id: i.id, accept: i.accept, multiple: i.multiple})),
    loginButtons: [...document.querySelectorAll('button, a')].filter(vis).map(b => (b.innerText||'').trim()).filter(t => /^(log in|sign up|sign in)/i.test(t)).slice(0, 5),
    cloudflare: /verify you are human|checking your browser|cf-chl/i.test(document.documentElement.innerHTML.slice(0, 200000)),
    text: txt,
  };
})()
"""

DOM_JS = r"""
(() => {
  const vis = el => { const r = el.getBoundingClientRect(); return r.width > 0 && r.height > 0; };
  const out = [];
  for (const el of document.querySelectorAll('button, [role=button], input, textarea, [contenteditable=true], [data-testid]')) {
    const r = el.getBoundingClientRect();
    out.push({tag: el.tagName.toLowerCase(), tid: el.getAttribute('data-testid'), id: el.id, type: el.type || '',
      aria: el.getAttribute('aria-label'), text: (el.innerText || el.value || '').trim().slice(0, 50),
      vis: vis(el), x: Math.round(r.left), y: Math.round(r.top), w: Math.round(r.width), h: Math.round(r.height)});
  }
  return out;
})()
"""


def main() -> int:
    cmd = sys.argv[1] if len(sys.argv) > 1 else "status"
    if cmd == "open":
        tid = cdp_gpt.ensure_tab()
        print("tab", tid)
        cmd = "status"
    p = cdp_gpt.Page()
    try:
        if cmd == "status":
            print(json.dumps(p.eval(STATUS_JS), indent=1, ensure_ascii=False))
        elif cmd == "shot":
            print(p.shot(sys.argv[2], fmt="png"))
        elif cmd == "eval":
            print(json.dumps(p.eval(sys.argv[2], timeout=60), indent=1, ensure_ascii=False))
        elif cmd == "dom":
            for e in p.eval(DOM_JS):
                if e["vis"] or e["tag"] == "input":
                    print(json.dumps(e, ensure_ascii=False))
        elif cmd == "goto":
            p.goto(sys.argv[2])
            print(json.dumps(p.eval(STATUS_JS), indent=1, ensure_ascii=False))
        else:
            print(__doc__)
            return 1
    finally:
        p.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
