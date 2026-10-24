"""Q9: audit the rendered site against BRAND_DESIGN.md §14 using computed styles (what the reader sees)."""
import json
import sys

from preview import Preview

AUDIT = r"""
(() => {
  const out = { mono: [], pills: [], heads: [], pureText: [], focus: [], counts: {} };
  const px = v => parseFloat(v);
  const visible = e => { const r = e.getBoundingClientRect(); const cs = getComputedStyle(e); return r.width > 0 && r.height > 0 && cs.visibility !== 'hidden' && cs.display !== 'none'; };
  const name = e => (e.tagName.toLowerCase() + '.' + String(e.className).split(' ')[0].replace(/^[A-Za-z0-9]+_+/, '')).slice(0, 40) + ' "' + (e.textContent || '').trim().slice(0, 22) + '"';
  const textEls = [...document.querySelectorAll('body *')].filter(e => [...e.childNodes].some(n => n.nodeType === 3 && n.textContent.trim().length > 1) && visible(e));
  out.counts.text = textEls.length;
  for (const e of textEls) {
    const cs = getComputedStyle(e);
    const fam = cs.fontFamily.split(',')[0].replace(/["']/g, '').trim();
    const fs = px(cs.fontSize);
    if (fam === 'mono') {
      const upper = cs.textTransform === 'uppercase';
      const ls = cs.letterSpacing === 'normal' ? 0 : px(cs.letterSpacing) / fs;
      const okLs = upper ? Math.abs(ls - 0.08) < 0.011 : (Math.abs(ls - 0.02) < 0.011 || ls === 0);
      const okW = cs.fontWeight === '400';
      const okSize = [10, 11, 12, 13, 8].includes(Math.round(fs));
      if (!okLs || !okW || !okSize) out.mono.push(`${name(e)} size=${fs} ls=${ls.toFixed(3)} upper=${upper} w=${cs.fontWeight}`);
    }
    const c = cs.color;
    if (c === 'rgb(0, 0, 0)' || c === 'rgb(255, 255, 255)') out.pureText.push(name(e) + ' ' + c);
  }
  for (const h of document.querySelectorAll('h1, h2, h3')) {
    if (!visible(h)) continue;
    const cs = getComputedStyle(h);
    const fam = cs.fontFamily.split(',')[0].replace(/["']/g, '').trim();
    const w = +cs.fontWeight;
    if (!['display', 'Anek Kannada'].includes(fam) || w < 300 || w > 400) out.heads.push(`${name(h)} fam=${fam} w=${w}`);
  }
  for (const b of document.querySelectorAll('a, button')) {
    if (!visible(b)) continue;
    const cs = getComputedStyle(b);
    if (cs.borderRadius !== '999px' || (cs.backgroundColor === 'rgba(0, 0, 0, 0)' && cs.borderTopWidth === '0px')) continue;
    const h = Math.round(b.getBoundingClientRect().height * 10) / 10;
    if (![48, 41.6].includes(h)) out.pills.push(`${name(b)} h=${h}`);
  }
  for (const d of document.querySelectorAll('[data-tone="dark"]')) {
    const f = getComputedStyle(d).getPropertyValue('--focus').trim();
    if (f && f !== 'var(--blue)' && f !== '#abcdd6') out.focus.push(name(d) + ' --focus=' + f);
  }
  return JSON.stringify(out);
})()
"""

paths = ["/", "/work", "/studio", "/work/studio-anokhi", "/work/nivritti", "/work/not-so-onam"]
p = Preview()
p.viewport(1440, 900)
total = {}
for path in paths:
    p.open(path, wait=2.5)
    p.walk(steps=30, dy=1000)
    p.pump(2)
    r = json.loads(p.eval(AUDIT))
    total[path] = r
    print(f"\n{path}  ({r['counts']['text']} text elements)")
    for k in ("mono", "pills", "heads", "pureText", "focus"):
        items = sorted(set(r[k]))
        print(f"  {k:8s} {len(items):3d} {'OK' if not items else ''}")
        for it in items[:12]:
            print("      ", it)
p.close()
