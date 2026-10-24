"""Q24 groundwork: move the site's colours onto semantic surface tokens (styles/surfaces.css).

1. Text and rules on a section's ground become semantic:
   color var(--ink) -> var(--on), --ink-soft -> --on-soft, --ink-faint -> --on-faint,
   color var(--plum) -> var(--on-strong), --rule -> --line, --rule-strong -> --line-strong,
   and plum borders, outlines, strokes and fills -> var(--on-strong).
2. Every rule block that paints a fixed object background (paper, cream, blue, plum, deep, oxblood)
   resets those tokens to that paper's own inks, so objects keep their colours on any ground.
Pill buttons are handled by hand (their fills become --btn-*).
Usage: surface_pass.py [--write]   (dry run by default)
"""
import re
import sys
from pathlib import Path

SRC = Path(__file__).resolve().parents[2] / "website" / "src"
WRITE = "--write" in sys.argv

PAPER = ("var(--paper)", "var(--paper-note)", "var(--cream)", "var(--cream-2)", "var(--cream-3)", "#fbfaf2", "#f8f5e8", "#efe7d2", "#f6efdc", "#ebe1c9")
BLUE = ("var(--blue)", "var(--blue-2)")
DARK = ("var(--plum)", "var(--deep)", "var(--oxblood)", "var(--rust)")
RESET = {
    "paper": "--on: var(--ink); --on-strong: var(--plum); --on-soft: var(--ink-soft); --on-faint: var(--ink-faint); --line: var(--rule); --line-strong: var(--rule-strong);",
    "blue": "--on: var(--deep); --on-strong: var(--plum); --on-soft: var(--blue-ink-soft); --on-faint: var(--blue-ink-faint); --line: rgb(39 6 23 / 0.18); --line-strong: rgb(39 6 23 / 0.36);",
    "dark": "--on: var(--cream); --on-strong: var(--cream); --on-soft: rgb(243 243 231 / 0.78); --on-faint: rgb(243 243 231 / 0.62); --line: rgb(243 243 231 / 0.16); --line-strong: rgb(243 243 231 / 0.34);",
}
TEXT = [(r"color:\s*var\(--ink\)", "color: var(--on)"), (r"color:\s*var\(--ink-soft\)", "color: var(--on-soft)"),
        (r"color:\s*var\(--ink-faint\)", "color: var(--on-faint)"), (r"(?<![-\w])color:\s*var\(--plum\)", "color: var(--on-strong)")]
LINES = [(r"var\(--rule-strong\)", "var(--line-strong)"), (r"var\(--rule\)", "var(--line)"),
         (r"((?<![-\w])(?:border(?:-[a-z]+)?|outline|stroke|fill):[^;]*?)var\(--plum\)", r"\g<1>var(--on-strong)")]
# the page itself and the text selection are not objects
NOT_OBJECTS = ("html", "body", "::selection")


def kind_of(body):
    m = re.search(r"(?<![-\w])background(?:-color)?:\s*([^;]+);", body)
    if not m:
        return None
    # the colour is the last layer (gradients and rulings sit on top of it); var(--np, var(--paper-note))
    # names its fallback last too
    val = m.group(1).strip().lower().rsplit(",", 1)[-1].strip()
    if any(val.startswith(p) for p in PAPER):
        return "paper"
    if any(val.startswith(p) for p in BLUE):
        return "blue"
    if any(val.startswith(p) for p in DARK):
        return "dark"
    return None


def fix_block(sel, body, log):
    pill = "999px" in body
    new = body
    for pat, rep in TEXT + LINES:
        new = re.sub(pat, rep, new)
    k = kind_of(body)
    name = re.sub(r"/\*.*?\*/", "", sel, flags=re.S).strip()
    if k and not pill and "--on:" not in new and name not in NOT_OBJECTS:
        new = new.rstrip() + "\n  /* an object: its own inks, on any ground */\n  " + RESET[k].replace("; ", ";\n  ") + "\n"
        log.append(f"  {name[:48]}: object ({k}) resets surface inks")
    elif new != body:
        log.append(f"  {name[:48]}: semantic text/lines")
    return new


for f in sorted(SRC.rglob("*.css")):
    if f.name in ("tokens.css", "surfaces.css"):
        continue
    css = f.read_text(encoding="utf-8")
    log = []
    out = re.sub(r"([^{}]+)\{([^{}]*)\}", lambda m: m.group(1) + "{" + fix_block(m.group(1), m.group(2), log) + "}", css)
    if out != css:
        print(f.relative_to(SRC), f"({len(log)} blocks)")
        for line in log[:80]:
            print(line)
        if WRITE:
            f.write_text(out, encoding="utf-8")
print("written" if WRITE else "dry run (pass --write to apply)")
