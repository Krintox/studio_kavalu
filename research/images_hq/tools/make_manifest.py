"""Write research/images_hq/MANIFEST.md and manifest.json: one row per source image.

Merges tools/status.json (method, faithful verdict from looking at the compare sheets, notes) with the fidelity numbers
in compare/<name>.json (written by fidelity.py).
"""
from __future__ import annotations

import glob
import json
import os

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
HQ = os.path.abspath(os.path.join(HERE, ".."))
ROOT = os.path.abspath(os.path.join(HQ, "..", ".."))
SRC_DIR = os.path.join(ROOT, "website", "public", "work")

status = json.load(open(os.path.join(HERE, "status.json"), encoding="utf-8"))
rows = []
for src in sorted(glob.glob(os.path.join(SRC_DIR, "*", "*.jpg"))):
    rel = os.path.relpath(src, SRC_DIR).replace("\\", "/")[:-4]
    st = status.get(rel, {"method": "none", "faithful": None, "notes": ""})
    name = os.path.basename(rel)
    cmp_json = os.path.join(HQ, "compare", name + ".json")
    met = json.load(open(cmp_json)) if (st["method"] != "none" and os.path.exists(cmp_json)) else {}
    out = st.get("output") or met.get("output")
    size = None
    if out and os.path.exists(os.path.join(ROOT, out)):
        size = list(Image.open(os.path.join(ROOT, out)).size)
    html_src = None
    if st["method"] == "html":
        h = os.path.join(HQ, "html", rel.replace("/", os.sep) + ".html")
        html_src = os.path.relpath(h, ROOT).replace("\\", "/") if os.path.exists(h) else None
    src_size = list(Image.open(src).size)
    row = {
        "source": "website/public/work/%s.jpg" % rel,
        "source_size": src_size,
        "method": st["method"],
        "output": out,
        "html_source": html_src,
        "size": size,
        "faithful": st["faithful"],
        "fidelity": {k: met.get(k) for k in ("ssim", "ssim_half", "ncc", "dE_mean", "dE_p95", "rgb_bias")} if met else None,
        "compare_sheet": ("research/images_hq/compare/%s.jpg" % name) if met else None,
        "notes": st.get("notes", ""),
    }
    if met.get("before_colour_match"):
        b = met["before_colour_match"]
        row["fidelity_before_colour_match"] = {k: b.get(k) for k in ("ssim", "ssim_half", "ncc", "dE_mean")}
    rows.append(row)

json.dump({"generated_by": "research/images_hq/tools/make_manifest.py", "images": rows},
          open(os.path.join(HQ, "manifest.json"), "w", encoding="utf-8"), indent=2, ensure_ascii=False)

fmt = lambda v, d=3: "" if v is None else (f"{v:.{d}f}" if isinstance(v, float) else str(v))
lines = ["# High-quality versions of the work images",
         "",
         "One row per source in `website/public/work/`. Outputs live in `research/images_hq/gpt/` (ChatGPT image generation), "
         "`research/images_hq/gemini/` (Gemini image generation; both aligned to the source framing and colour-matched to it) "
         "and `research/images_hq/html/` (HTML/SVG recreations rendered at 3x, with their `.html` source beside them). "
         "Nothing in `website/` was changed.",
         "",
         "**For integration:** use the `<name>.png` listed below. Files named `<name>.<layer>.png` beside the HTML outputs are "
         "intermediate layers (already embedded in the `.html`); `*.params.json` hold the measurements. The `.html` sources "
         "load Arimo / Figtree / Oswald from Google Fonts, so re-rendering them needs a connection; the PNGs are final. "
         "`gpt/_rejected/` and `gpt/_work/` (raw ChatGPT files, uploads, prompts) are for reference only.",
         "",
         "**Fidelity:** each output is downscaled to the source size and compared with the source: SSIM on greyscale "
         "(at source size, and at half size, which is less sensitive to the source's own blur), normalised "
         "cross-correlation (NCC) and mean CIE76 colour difference (dE). Side-by-side sheets are in `compare/`. "
         "**Faithful** is a judgement made by looking at each sheet and close-up crops (layout, text, logos, faces), not "
         "a threshold on the numbers.",
         "",
         "| # | Source | Method | Output | Size | SSIM | SSIM ½ | NCC | dE | Faithful |",
         "|---|---|---|---|---|---|---|---|---|---|"]
for i, r in enumerate(rows, 1):
    f = r["fidelity"] or {}
    faithful = {True: "yes", False: "**no**", None: "-"}[r["faithful"]]
    out = f"`{r['output']}`" if r["output"] else "still needed"
    size = "x".join(map(str, r["size"])) if r["size"] else ""
    lines.append(f"| {i} | `{r['source']}` ({r['source_size'][0]}x{r['source_size'][1]}) | {r['method']} | {out} | {size} | "
                 f"{fmt(f.get('ssim'))} | {fmt(f.get('ssim_half'))} | {fmt(f.get('ncc'))} | {fmt(f.get('dE_mean'), 2)} | {faithful} |")
lines += ["", "## Notes per image", ""]
for r in rows:
    lines.append(f"- **{r['source'].split('/work/')[1]}** ({r['method']}): {r['notes']}")
done = [r for r in rows if r["faithful"] is True]
lines += ["", "## Summary", "",
          f"- Faithful high-quality outputs: {len(done)} of {len(rows)} "
          f"({sum(1 for r in done if r['method'] == 'gpt')} ChatGPT, {sum(1 for r in done if r['method'] == 'html')} HTML).",
          f"- Rejected: {sum(1 for r in rows if r['faithful'] is False)}; still needed: {sum(1 for r in rows if r['faithful'] is None)}.",
          "", "## Method", "",
          "- `tools/gen_gpt.py`: one new ChatGPT chat per image in our own window of the persistent Chrome (CDP 9333): "
          "'Create image' tool, upload, a 'keep everything identical' prompt, wait, download the full-size file in-page.",
          "- `tools/gen_gemini.py`: one new Gemini chat per image in our own window (signed-in Gemini Pro, '3.1 Pro' mode, "
          "'Images' tool): upload via an intercepted file chooser, the same 'keep everything identical' prompt, then the "
          "'Download full size image' file captured in-tab (the browser download is aborted). `tools/dewatermark.py` removes "
          "Gemini's visible sparkle watermark by copying neighbouring texture over it (the sparkle is not in the sources).",
          "- `gpt/_chats/`: every image in the project's ChatGPT chats, downloaded at full resolution through ChatGPT's file "
          "API; `gpt/_chats/chats.json` lists chat id, title, source and file id. Each generated image there is byte-identical "
          "to the one already used (one per chat; the three red-room chats were refusals with no image).",
          "- `tools/fidelity.py`: registers the GPT output to the source (scale + offset per axis), crops it to the source "
          "framing, fits a robust 2nd-order RGB colour transform back to the source's colours, scores, writes the sheet.",
          "- HTML builders `tools/build_*.py`: every shape, colour and position is measured from the source (potrace traces, "
          "fitted guide lines, font matching by rendering candidates and scoring against the source, ink-box placement); "
          "rendered by `tools/render.py` at device scale 3.",
          ]
open(os.path.join(HQ, "MANIFEST.md"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
print("wrote", len(rows), "rows;", len(done), "faithful")
