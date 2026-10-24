"""Q6: what kinds of type the researched sites set, by role, from the census (screens/results.jsonl).

Classifies each loaded family by name into serif / grotesk-sans / mono / script-hand / other, then
counts sites per bucket that load at least one of each. Name-based, so the numbers are approximate;
icon fonts and placeholders are ignored.
"""
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
recs = [json.loads(l) for l in open(ROOT / "screens" / "results.jsonl", encoding="utf-8")]
recs = [r for r in recs if r.get("ok") and r.get("info")]

SERIF = re.compile(r"serif(?!.*sans)|garamond|caslon|times|tiempos|editorial|saol|sectra|canela|domaine|plantin|plantijn|baskerville|bodoni|didot|"
                   r"recoleta|fraunces|playfair|cormorant|lora|merriweather|newsreader|sabon|cheltenham|clarendon|century|schoolbook|copernicus|"
                   r"arizona|season ?mix|quadrant ?text(?!.*mono)|jannon|sentinel|freight-?(text|display)|gt.?super|alpina|kinfolk-serif|portrait text|"
                   r"epicene|bell mt|perpetua|georgia|dejanire|self modern|mackinac|untitled-serif|ps ?times|newparis|fancy-serif|acute|"
                   r"iskry|tomo slab|grand|lacrimamg|zapf-humanist|items mt|vevey|syllabus|canopee", re.I)
MONO = re.compile(r"mono|typewriter|courier|cutive|code|pressura mono|fono", re.I)
HAND = re.compile(r"hand|script|vibes|amatic|felt-tip|gooddog|comic|caveat|beanie|lacquer|swanky|marker", re.I)
IGNORE = re.compile(r"icon|awesome|judgeme|swiper|revicons|elegant|ionicons|material|placeholder|^wf_|^\w{1,2}$|fallback|stamped", re.I)

def kind(f):
    if IGNORE.search(f):
        return None
    if MONO.search(f):
        return "mono"
    if HAND.search(f):
        return "hand"
    if SERIF.search(f):
        return "serif"
    return "sans"

NAMES = {"A": "Boutique & founder-led", "B": "Indian studios", "C": "Established agencies", "D": "Motion-led / awarded",
         "E": "Tactile, collage, editorial", "F": "Lifestyle, food & craft", "G": "Designer portfolios"}
per = defaultdict(Counter)
serifs = Counter()
for r in recs:
    kinds = set()
    for f in r["info"].get("fonts") or []:
        k = kind(f)
        if k:
            kinds.add(k)
            if k == "serif":
                serifs[re.sub(r"[-_ ](regular|italic|light|medium|bold|book|text|display|deck).*$", "", f, flags=re.I)] += 1
    b = r["bucket"]
    per[b]["sites"] += 1
    per["all"]["sites"] += 1
    for k in kinds:
        per[b][k] += 1
        per["all"][k] += 1
    if kinds >= {"serif", "sans"}:
        per[b]["serif+sans"] += 1
        per["all"]["serif+sans"] += 1

out = ["| Bucket | Sites | Any grotesk / sans | Any serif | Serif + sans pairing | Any mono | Any script / hand |", "|---|---|---|---|---|---|---|"]
for b in ["A", "B", "C", "D", "E", "F", "G", "all"]:
    c = per[b]
    n = c["sites"] or 1
    pct = lambda k: f"{c[k]} ({round(100 * c[k] / n)}%)"
    out.append(f"| {NAMES.get(b, '**All**')} | {c['sites']} | {pct('sans')} | {pct('serif')} | {pct('serif+sans')} | {pct('mono')} | {pct('hand')} |")
print("\n".join(out))
print()
print("Serifs seen:", ", ".join(f"{k} ({v})" for k, v in serifs.most_common(40)))
