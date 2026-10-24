"""Q9 consistency pass, the mechanical part: bring every CSS module onto the tokens in BRAND_DESIGN.md.

Usage: consistency_pass.py [--write]   (dry run by default; prints every change per file)
"""
import re
import sys
from pathlib import Path

SRC = Path(__file__).resolve().parents[2] / "website" / "src"
WRITE = "--write" in sys.argv

COLOURS = {
    "#fbfaf2": "var(--paper)", "#fbfaf3": "var(--paper)",
    "#f8f5e8": "var(--paper-note)", "#f8f6ea": "var(--paper-note)",
    "#d9d2c1": "var(--placeholder)", "#d8d1c1": "var(--placeholder)", "#d7d0c0": "var(--placeholder)", "#cfc8b8": "var(--placeholder)",
    "#24131a": "var(--corner)", "#1d1016": "var(--corner)",
    "#a4201f": "var(--error)", "#fbeee9": "var(--error-wash)",
}
CLAMPS = {
    "clamp(2.9rem, 0.9rem + 5.15vw, 6.9rem)": "var(--t-hero)",
    "clamp(3.4rem, 1rem + 7vw, 9.2rem)": "var(--t-spread)",
    "clamp(2.2rem, 1rem + 4.4vw, 5.9rem)": "var(--t-manifesto)",
    "clamp(2rem, 1.2rem + 2.6vw, 3.9rem)": "var(--t-quote)",
    "clamp(2.2rem, 1.5rem + 2.4vw, 4rem)": "var(--t-quote)",
    "clamp(2.1rem, 1.5rem + 2vw, 3.4rem)": "var(--t-sheet)",
    "clamp(1.9rem, 1.4rem + 1.8vw, 3rem)": "var(--t-sheet)",
    "clamp(2rem, 1.4rem + 1.8vw, 3.2rem)": "var(--t-sheet)",
    "clamp(1.7rem, 1.2rem + 1.8vw, 3rem)": "var(--t-3)",
    "clamp(1.7rem, 1.2rem + 1.1vw, 2.4rem)": "var(--t-4)",
    "clamp(1.5rem, 1.1rem + 1vw, 2.1rem)": "var(--t-4)",
    "clamp(1.7rem, 1.2rem + 1vw, 2.2rem)": "var(--t-4)",
}
SIZES = {"0.875rem": "var(--t-small)", "0.6875rem": "var(--t-label)", "0.625rem": "var(--t-tiny)", "0.5625rem": "var(--t-tiny)"}
BREAKS = {"(max-width: 900px)": "(max-width: 899px)", "(max-width: 640px)": "(max-width: 639px)", "(max-width: 1100px)": "(max-width: 1099px)"}
DESK = "0 2px 2px rgb(0 0 0 / 0.2), 0 22px 36px -18px rgb(0 0 0 / 0.55)"


def duration(ms: int) -> str:
    if ms <= 260:
        return "var(--d-quick)"
    if ms <= 440:
        return "var(--d-base)"
    if ms <= 640:
        return "var(--d-move)"
    return "var(--d-slow)"


def fix_block(selector: str, body: str, log: list) -> str:
    """Rules that need the whole declaration block: mono labels and transitions."""
    mono = "var(--f-mono)" in body
    upper = re.search(r"text-transform:\s*uppercase", body)
    if mono:
        new = re.sub(r"font-weight:\s*500\b", "font-weight: 400", body)
        if new != body:
            log.append(f"  {selector.strip()[:50]}: mono weight 500 -> 400")
            body = new
        if upper:
            new = re.sub(r"letter-spacing:\s*0\.(0[4-7]|1)em", "letter-spacing: 0.08em", body)
        else:
            new = re.sub(r"letter-spacing:\s*0\.0[4-6]em", "letter-spacing: 0.02em", body)
        if new != body:
            log.append(f"  {selector.strip()[:50]}: mono tracking unified")
            body = new

    def dur(m):
        decl = m.group(0)
        return re.sub(r"(?<![\w.-])(\d{3})ms", lambda d: duration(int(d.group(1))), decl)

    new = re.sub(r"transition(-duration)?:[^;]+;", dur, body)
    if new != body:
        log.append(f"  {selector.strip()[:50]}: transition durations -> tokens")
        body = new
    return body


def process(path: Path):
    css = path.read_text(encoding="utf-8")
    orig = css
    log = []
    # pure white stays pure white only where it is a mask (SVG luminance masks need #fff); the one
    # other #fff in the CSS is the plain print on the spreads, which is paper
    if path.name == "Spreads.module.css":
        css = re.sub(r"#fff(?![0-9a-fA-F])", "var(--paper)", css, flags=re.I)
    for k, v in COLOURS.items():
        pat = re.compile(re.escape(k) + r"(?![0-9a-fA-F])", re.I)
        n = len(pat.findall(css))
        if n:
            css = pat.sub(v, css)
            log.append(f"  colour {k} -> {v} x{n}")
    for k, v in CLAMPS.items():
        if k in css:
            log.append(f"  {k} -> {v} x{css.count(k)}")
            css = css.replace(k, v)
    for k, v in SIZES.items():
        pat = re.compile(r"font-size:\s*" + re.escape(k) + r";")
        n = len(pat.findall(css))
        if n:
            css = pat.sub(f"font-size: {v};", css)
            log.append(f"  font-size {k} -> {v} x{n}")
    for k, v in BREAKS.items():
        if k in css:
            log.append(f"  {k} -> {v} x{css.count(k)}")
            css = css.replace(k, v)
    if DESK in css:
        log.append(f"  desk shadow -> var(--shadow-desk) x{css.count(DESK)}")
        css = css.replace(DESK, "var(--shadow-desk)")
    css = re.sub(r"([^{}]+)\{([^{}]*)\}", lambda m: m.group(1) + "{" + fix_block(m.group(1), m.group(2), log) + "}", css)
    if css != orig:
        print(path.relative_to(SRC))
        print("\n".join(log))
        if WRITE:
            path.write_text(css, encoding="utf-8")


for f in sorted(SRC.rglob("*.css")):
    if f.name == "tokens.css":
        continue
    process(f)
print("written" if WRITE else "dry run (pass --write to apply)")
