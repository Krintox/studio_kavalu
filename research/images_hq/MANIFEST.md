# High-quality versions of the work images

One row per source in `website/public/work/`. Outputs live in `research/images_hq/gpt/` (ChatGPT image generation, aligned to the source framing and colour-matched to it) and `research/images_hq/html/` (HTML/SVG recreations rendered at 3x, with their `.html` source beside them). Nothing in `website/` was changed.

**For integration:** use the `<name>.png` listed below. Files named `<name>.<layer>.png` beside the HTML outputs are intermediate layers (already embedded in the `.html`); `*.params.json` hold the measurements. The `.html` sources load Arimo / Figtree / Oswald from Google Fonts, so re-rendering them needs a connection; the PNGs are final. `gpt/_rejected/` and `gpt/_work/` (raw ChatGPT files, uploads, prompts) are for reference only.

**Fidelity:** each output is downscaled to the source size and compared with the source: SSIM on greyscale (at source size, and at half size, which is less sensitive to the source's own blur), normalised cross-correlation (NCC) and mean CIE76 colour difference (dE). Side-by-side sheets are in `compare/`. **Faithful** is a judgement made by looking at each sheet and close-up crops (layout, text, logos, faces), not a threshold on the numbers.

| # | Source | Method | Output | Size | SSIM | SSIM ½ | NCC | dE | Faithful |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `website/public/work/content/fillers-not-yet.jpg` (322x182) | none | still needed |  |  |  |  |  | - |
| 2 | `website/public/work/content/not-so-onam.jpg` (164x202) | none | still needed |  |  |  |  |  | - |
| 3 | `website/public/work/content/red-room-portrait.jpg` (184x244) | none | still needed |  |  |  |  |  | - |
| 4 | `website/public/work/content/red-saree-portrait.jpg` (124x222) | none | still needed |  |  |  |  |  | - |
| 5 | `website/public/work/nivritti/business-cards.jpg` (770x398) | none | still needed |  |  |  |  |  | - |
| 6 | `website/public/work/nivritti/cleanser-bottle.jpg` (288x348) | gpt | `research/images_hq/gpt/_rejected/nivritti/cleanser-bottle.png` | 1142x1380 | 0.774 | 0.866 | 0.974 | 5.56 | **no** |
| 7 | `website/public/work/nivritti/logo-navy.jpg` (288x346) | html | `research/images_hq/html/nivritti/logo-navy.png` | 1998x2400 | 0.920 | 0.958 | 0.964 | 2.78 | yes |
| 8 | `website/public/work/nivritti/logo-orange.jpg` (290x346) | html | `research/images_hq/html/nivritti/logo-orange.png` | 2013x2400 | 0.924 | 0.965 | 0.957 | 3.20 | yes |
| 9 | `website/public/work/nivritti/packaging-box.jpg` (290x348) | none | still needed |  |  |  |  |  | - |
| 10 | `website/public/work/nivritti/sign-street.jpg` (770x400) | gpt | `research/images_hq/gpt/nivritti/sign-street.png` | 1740x904 | 0.740 | 0.850 | 0.945 | 6.12 | yes |
| 11 | `website/public/work/studio-anokhi/collage-wheel.jpg` (266x332) | gpt | `research/images_hq/gpt/studio-anokhi/collage-wheel.png` | 1119x1397 | 0.891 | 0.941 | 0.969 | 3.92 | yes |
| 12 | `website/public/work/studio-anokhi/hero-wheel.jpg` (580x300) | gpt | `research/images_hq/gpt/studio-anokhi/hero-wheel.png` | 1739x899 | 0.873 | 0.930 | 0.978 | 3.83 | yes |
| 13 | `website/public/work/studio-anokhi/mark-evolution.jpg` (580x294) | html | `research/images_hq/html/studio-anokhi/mark-evolution.png` | 2400x1218 | 0.933 | 0.971 | 0.956 | 1.63 | yes |
| 14 | `website/public/work/studio-anokhi/mark-orange.jpg` (216x262) | html | `research/images_hq/html/studio-anokhi/mark-orange.png` | 1980x2400 | 0.887 | 0.940 | 0.974 | 3.95 | yes |
| 15 | `website/public/work/studio-anokhi/slow-making.jpg` (216x260) | gpt | `research/images_hq/gpt/studio-anokhi/slow-making.png` | 1137x1369 | 0.824 | 0.903 | 0.967 | 5.39 | yes |
| 16 | `website/public/work/studio-anokhi/stationery-ochre.jpg` (216x262) | html | `research/images_hq/html/studio-anokhi/stationery-ochre.png` | 1980x2400 | 0.971 | 0.986 | 0.991 | 0.92 | yes |
| 17 | `website/public/work/studio-anokhi/stationery-olive.jpg` (220x260) | html | `research/images_hq/html/studio-anokhi/stationery-olive.png` | 2031x2400 | 0.963 | 0.981 | 0.993 | 1.03 | yes |
| 18 | `website/public/work/studio-anokhi/vases-wordmark.jpg` (220x262) | html | `research/images_hq/html/studio-anokhi/vases-wordmark.png` | 2016x2400 | 0.976 | 0.986 | 0.991 | 1.12 | yes |
| 19 | `website/public/work/studio-anokhi/word-search.jpg` (220x262) | none | still needed |  |  |  |  |  | - |
| 20 | `website/public/work/studio-anokhi/wordmark-pattern.jpg` (580x320) | html | `research/images_hq/html/studio-anokhi/wordmark-pattern.png` | 2400x1323 | 0.946 | 0.964 | 0.948 | 2.27 | yes |
| 21 | `website/public/work/studio/ananya-portrait.jpg` (174x230) | none | still needed |  |  |  |  |  | - |

## Notes per image

- **content/fillers-not-yet.jpg** (none): Still needed. Photo of people; the ChatGPT Free image quota (5 per rolling day) ran out before this image's turn (resets 2026-10-25 13:14 IST). A photo cannot be recreated in HTML without inventing it.
- **content/not-so-onam.jpg** (none): Still needed. Photo of a person; ChatGPT image quota exhausted before its turn. Not recreatable in HTML.
- **content/red-room-portrait.jpg** (none): Still needed. ChatGPT refused three times ('may violate our guardrails around nudity, sexuality, or erotic content', a false positive on the bare-shoulder pose), with three different prompts. Not recreatable in HTML.
- **content/red-saree-portrait.jpg** (none): Still needed. Photo of a person; ChatGPT image quota exhausted before its turn. Not recreatable in HTML.
- **nivritti/business-cards.jpg** (none): Still needed. Product photograph: the black woven fabric is photographic texture (a code version could only enlarge it soft or invent weave detail), the navy card carries a distinctive serif ('MEERA SETHI', 'FOUNDER & CEO') that no available font matches and two contact lines that are illegible. Skipped rather than guessed; retry with ChatGPT after the quota resets (2026-10-25 13:14 IST) or use the original file.
- **nivritti/cleanser-bottle.jpg** (gpt): REJECTED. ChatGPT changed the label: the second line reads 'NATURAL HANDWASH' (source: a different, cut-off line, likely 'HEMP CLEANSER'), the mountain mark was redrawn with three peaks (source: the two-peak NIVRITTI mark) and the side plant illustration was replaced. Kept in gpt/_rejected for reference only; needs a retry with a stricter prompt once the quota resets.
- **nivritti/logo-navy.jpg** (html): Ground, guides and artwork measured from the source; artwork (mountain + NIVRITTI letters) is the averaged alpha of the navy and orange cards enlarged 8x (no substitute font: no candidate matched the wordmark closely enough). Edges are smooth but not vector-sharp.
- **nivritti/logo-orange.jpg** (html): Same artwork layer as logo-navy, placed with the measured registration (x offset 2.9 px); orange ground and guide opacity measured on this card.
- **nivritti/packaging-box.jpg** (none): Still needed. Product photograph with printed text, a line drawing and paper/foil textures; ChatGPT image quota exhausted before its turn. Not recreatable in HTML without inventing detail.
- **nivritti/sign-street.jpg** (gpt): Faithful: sign, mountain mark and NIVRITTI lettering match in shape and position. Global colour matched back to the source's faded film look (GPT had brightened it ~+30/255). Minor: a background house-number plaque that is illegible in the source was rendered by GPT as '13'.
- **studio-anokhi/collage-wheel.jpg** (gpt): Faithful: framing, hands, wordmark, the striped star corner and the bordered photo edge all match. Global colour matched to the source.
- **studio-anokhi/hero-wheel.jpg** (gpt): Faithful: hands, pot and the 'studio anokhi' wordmark match letter for letter in position and size. GPT had lifted the tones (+16/255); global colour matched back to the source.
- **studio-anokhi/mark-evolution.jpg** (html): Shapes traced from the source, arrows measured, sage pot from the source pixels. Small paragraph re-set in Figtree (best match; the source is ~3 px x-height). Wording checked by scoring rendered alternatives against the source: 'It is more than a studio; Anokhi is where time passes without notice, / where memories are shaped and you mould something as Anokhi as you.' ('It is' scored 0.85 vs 0.64 for 'It's'; 'mould' and bold 'Anokhi' in line 2). Label 'logo mark' in Figtree 450 (stem width matched).
- **studio-anokhi/mark-orange.jpg** (html): Every element measured from the source: the glyph traced, dotted guides fitted (pitch 5.97 / 4.95 px: the crop is stretched 1.21x vertically and that geometry is kept), corner circles fitted jointly and clipped to their cells as in the source.
- **studio-anokhi/slow-making.jpg** (gpt): Faithful: hands, tool, pot and the caption 'A glimpse of slow making' match; skin/clay texture is new fine detail. Global colour matched to the source.
- **studio-anokhi/stationery-ochre.jpg** (html): Vellum stationery mock-up rebuilt from its own pixels: gradient + soft shadows enlarged smoothly; both 70x140 px sheets as crisp rectangles (edges from gradient peaks); back-sheet paper flattened (removes the source's oversharpening halos); dark pottery icons and the अ on the vellum as smooth-edged silhouettes in their own colours; the faded see-through icons stay part of the vellum's observed colours. The tiny stacked 'studio anokhi' lockup is re-set in Arimo on the measured lines, with its faint side dashes kept from the source. Icons are only 10-15 px in the source, so their shapes stay approximate/soft.
- **studio-anokhi/stationery-olive.jpg** (html): Vellum stationery mock-up rebuilt from its own pixels: gradient + soft shadows enlarged smoothly; both 70x140 px sheets as crisp rectangles (edges from gradient peaks); back-sheet paper flattened (removes the source's oversharpening halos); dark pottery icons and the अ on the vellum as smooth-edged silhouettes in their own colours; the faded see-through icons stay part of the vellum's observed colours. The tiny stacked 'studio anokhi' lockup is re-set in Arimo on the measured lines, with its faint side dashes kept from the source. Icons are only 10-15 px in the source, so their shapes stay approximate/soft.
- **studio-anokhi/vases-wordmark.jpg** (html): Built from the source's own pixels: flat cream ground, the source's shadow darkening enlarged smoothly (shadows are soft), jug silhouettes with crisp edges and their interior colours enlarged smoothly (light mouths/handle holes kept), 'anokhi' re-set in Arimo 460 on its measured box (shape correlation favoured 400-450; consistent with the wordmark weight in wordmark-pattern). Matte surface texture is smooth, not invented.
- **studio-anokhi/word-search.jpg** (none): Still needed. A grid of ~5 px random letters over a dark photo; apart from the circled 'something', many letters are ambiguous (i/l, n/h/u), so a code version would have to guess letters. Retry with ChatGPT (with the letters checked against the source) or use the original file.
- **studio-anokhi/wordmark-pattern.jpg** (html): Panel texture is the source panel with the cream elements inpainted and enlarged (it is low-frequency). Wordmarks re-set in Arimo (Arial design, weight ~480 from ink matching; best of ~60 fonts, NCC 0.85) on each measured line box: the original is a Helvetica-class grotesque that cannot be identified exactly at this size. अ marks traced. 'MOLDING MUD, / CREATING LOVE' set in Oswald 500 (weak font evidence at 8 px caps). The two tiny taglines (~4 px) are illegible and are kept from the source pixels, not re-set.
- **studio/ananya-portrait.jpg** (none): Still needed. Was to be done last with ChatGPT and discarded if her identity drifted; the image quota ran out first. A portrait cannot be recreated in HTML.

## Summary

- Faithful high-quality outputs: 12 of 21 (4 ChatGPT, 8 HTML).
- Rejected: 1; still needed: 8.

## Method

- `tools/gen_gpt.py`: one new ChatGPT chat per image in our own window of the persistent Chrome (CDP 9333): 'Create image' tool, upload, a 'keep everything identical' prompt, wait, download the full-size file in-page.
- `tools/fidelity.py`: registers the GPT output to the source (scale + offset per axis), crops it to the source framing, fits a robust 2nd-order RGB colour transform back to the source's colours, scores, writes the sheet.
- HTML builders `tools/build_*.py`: every shape, colour and position is measured from the source (potrace traces, fitted guide lines, font matching by rendering candidates and scoring against the source, ink-box placement); rendered by `tools/render.py` at device scale 3.
