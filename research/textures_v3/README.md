# Studio Kavalu paper textures (v3)

Procedural, seamless paper for every background on the site: light papers, dark cardstock and the
project spreads. This replaces `website/public/textures/paper-grain.png`, `grain-alpha.png`,
`worn-light.png` and `torn-top.svg`, which were too faint (the old grain was about 0.5 L* of
variation on cream) and left the dark sections flat.

Nothing in `website/` has been changed by this work. To use these, copy the `.webp` files you need
(and the masks) into `website/public/textures/v3/` and apply the CSS below.

- `preview.jpg`: every texture as a 1440 x 900 page with the site's own type (Gambetta, Switzer,
  Courier Prime), a 2x loupe on the 16 px body text, retina and phone crops, the torn edge, and
  3 x 3 tiling checks (true contrast and contrast raised x2.5 to x8). The single panels are in
  `previews/`. All of them are rendered from the decoded `.webp` files, so they show what a
  browser shows.
- `metrics.json`: per-file mean-colour accuracy, strength, seam checks, how much detail the WebP
  encoder kept, the compensation colours for the neutral tiles, and the cardstock on every
  project colour.
- `contrast.json`: text contrast on every paper, against its mean and its worst 0.1 % patch.
- `tools/`: the generators (see "Regenerate").

---

## 1. Files

| Texture | Use | 1024 WebP | 1024 PNG | 512 WebP | 512 PNG |
|---|---|---:|---:|---:|---:|
| `paper-cream` | baked `#F3F3E7`: the page | 77.3 KB | 575.9 KB | 22.9 KB | 136.9 KB |
| `paper-writing-paper` | baked `#F8F5E8`: notes, letter, ruled sheets | 55.2 KB | 505.8 KB | 15.9 KB | 113.3 KB |
| `paper-powder-blue` | baked `#ABCDD6`: blue panels | 62.9 KB | 542.9 KB | 18.9 KB | 135.4 KB |
| `paper-deep-plum` | baked `#270617`: footer, the desk, dark sheets | 72.2 KB | 453.4 KB | 20.9 KB | 110.4 KB |
| `paper-plum` | baked `#390D26`: plum sheets | 63.8 KB | 429.9 KB | 18.1 KB | 110.4 KB |
| `paper-oxblood` | baked `#491C17`: oxblood sheets, overview card | 55.3 KB | 419.7 KB | 15.4 KB | 105.9 KB |
| `paper-neutral-light` | greyscale, `multiply` on any light colour | 47.8 KB | 321.7 KB | 14.9 KB | 85.2 KB |
| `paper-neutral-strong` | the same sheet, about 1.45x stronger | 79.6 KB | 372.5 KB | 22.8 KB | 97.3 KB |
| `cardstock-overlay` | mid-grey, `soft-light` (or `overlay`) on any mid or dark colour | 78.6 KB | 439.9 KB | 22.3 KB | 114.3 KB |
| `torn-edge-top` | alpha mask, 2048 x 96 (shown at 1024 x 48) | 18.0 KB | 25.3 KB | | |
| `torn-edge-bottom` | the same edge, flipped | 17.9 KB | 25.4 KB | | |
| `torn-rim-top` | the torn zone, for an optional lighter layer | 20.7 KB | 28.5 KB | | |

Every WebP is under 80 KB. The 512 PNGs are all under 150 KB. The 1024 PNGs are not (320 to
580 KB): real paper grain is close to incompressible losslessly. They are the lossless masters and
an optional fallback only (see 3.8); no current browser needs them.

**WebP quality is 95 (light papers, neutral tiles), 98 (dark papers) and 90 (cardstock), not 80.**
At q80 the encoder erases the fibre mat of these low-contrast sheets: on plum only 0.45 of the
fibre-scale structure survives (correlation of the 1.5 to 6 px band, source against decoded file;
deep plum 0.59, cream 0.78), and the fibres turn into 4 x 4 blocks (checked side by side, true
contrast and enhanced). At the qualities used, 0.90 to 0.98 of it survives (`metrics.json`,
`webp_detail`), and the files are still 2 to 3 times under budget.

---

## 2. Which paper goes where

| Surface (token) | Texture | How |
|---|---|---|
| The page, cream sections, the manifesto sheet, the intro (`--cream`) | `paper-cream` | baked, no blend mode |
| Sheets laid on the cream, album pages (`--cream-2`) | `paper-neutral-light` | `multiply` on `#F1EFDF` |
| Index cards, folder tabs (`--cream-3`) | `paper-neutral-light`, or `-strong` for a heavier card | `multiply` on `#E8E5D1` (light) / `#EAE7D3` (strong) |
| Prints, stamps, polaroids, strips (`--paper`) | `paper-neutral-light` | `multiply` on `#FFFFF7` |
| Notes, ruled sheets, the letter, service cards (`--paper-note`) | `paper-writing-paper` | baked; draw the rules on top |
| Powder-blue panels: founder poster, nav tab (`--blue`) | `paper-powder-blue` | baked |
| Footer, the desk, the deepest folder (`--deep`) | `paper-deep-plum` | baked |
| Plum sheets and panels (`--plum`) | `paper-plum` | baked |
| Oxblood sheets, the overview card (`--oxblood`) | `paper-oxblood` | baked |
| Project spreads and case-study heads (`--p-bg`) | `cardstock-overlay` | `soft-light` over the project colour |
| Top of the manifesto sheet (any sheet with a torn top) | `torn-edge-top` (+ `torn-rim-top`) | CSS mask |

No texture on the wordmark or logo (BRAND_DESIGN logo misuse rule 5), on buttons, pills, chips,
inputs or other small controls, or on photographs.

---

## 3. CSS

### 3.1 Tokens: one texture pixel per device pixel

The tiles are drawn for one texture pixel per device pixel, which keeps them crisp and never
resampled: the 1024 tile at 1024 CSS px on 1x screens and at 512 CSS px on retina screens; on
phones the 512 tile at 256 CSS px (2x). Do not scale them to other sizes. Showing the 1024 tile at
512 px on a 1x screen downsamples it and erases the fibres; showing it at 1024 px on a retina screen
upscales it and goes soft. Both were checked (`previews/retina-*.jpg`, `previews/phone-512-tiles.jpg`).

```css
/* tokens.css: paper v3 (research/textures_v3/README.md) */
:root {
  --tex-cream: url("/textures/v3/paper-cream-1024.webp");
  --tex-writing: url("/textures/v3/paper-writing-paper-1024.webp");
  --tex-blue: url("/textures/v3/paper-powder-blue-1024.webp");
  --tex-deep: url("/textures/v3/paper-deep-plum-1024.webp");
  --tex-plum: url("/textures/v3/paper-plum-1024.webp");
  --tex-oxblood: url("/textures/v3/paper-oxblood-1024.webp");
  --tex-neutral: url("/textures/v3/paper-neutral-light-1024.webp");
  --tex-neutral-strong: url("/textures/v3/paper-neutral-strong-1024.webp");
  --tex-cardstock: url("/textures/v3/cardstock-overlay-1024.webp");
  --tex-size: 1024px;

  /* light colours lifted by 1 / tile mean, so a multiplied neutral tile keeps the brand colour */
  --cream-2-lift: #f1efdf; /* light tile; #f3f1e2 with the strong tile */
  --cream-3-lift: #e8e5d1; /* light tile; #eae7d3 with the strong tile */
  --paper-lift: #fffff7; /* light tile only */
}

@media (-webkit-min-device-pixel-ratio: 1.5), (min-resolution: 1.5dppx) {
  :root {
    --tex-size: 512px;
  }
}

/* phones: the 512 tiles (a quarter of the bytes), with calmer large clouds so the shorter repeat
   does not show at normal contrast */
@media (max-width: 639px) {
  :root {
    --tex-cream: url("/textures/v3/paper-cream-512.webp");
    --tex-writing: url("/textures/v3/paper-writing-paper-512.webp");
    --tex-blue: url("/textures/v3/paper-powder-blue-512.webp");
    --tex-deep: url("/textures/v3/paper-deep-plum-512.webp");
    --tex-plum: url("/textures/v3/paper-plum-512.webp");
    --tex-oxblood: url("/textures/v3/paper-oxblood-512.webp");
    --tex-neutral: url("/textures/v3/paper-neutral-light-512.webp");
    --tex-neutral-strong: url("/textures/v3/paper-neutral-strong-512.webp");
    --tex-cardstock: url("/textures/v3/cardstock-overlay-512.webp");
    --tex-size: 512px;
  }
}

@media (max-width: 639px) and (-webkit-min-device-pixel-ratio: 1.5),
  (max-width: 639px) and (min-resolution: 1.5dppx) {
  :root {
    --tex-size: 256px;
  }
}
```

### 3.2 Light sections: baked cream

```css
body {
  background-color: var(--cream); /* shows while the image loads; it is the image's mean colour */
  background-image: var(--tex-cream);
  background-size: var(--tex-size);
  /* baked: delete the old `background-blend-mode: multiply`. Multiplying a baked tile with its own
     colour squares it and darkens the page by about 4 L* (dE00 4.7) */
}
```

The same three lines replace the grain on `.manifesto` (Manifesto.module.css) and `.intro`
(Intro.module.css).

**One ground, one sheet.** Every element starts its own copy of the tile at its own top-left corner.
Two neighbouring sections on the same ground that each carry the texture therefore meet in a
straight cut through the clouds and fibres. It is faintly visible on cream at true contrast and
plain at 4x (checked). Do one of these:

- Leave cream sections transparent, so the body's single sheet runs under all of them
  (`[data-surface="cream"] { background: none; }` when the body already carries the cream paper).
- Wrap consecutive sections on the same ground in one element that carries the texture.
- Or pin every section's texture to the page, so they line up as one sheet. Set `--page-y` from JS
  on load and resize (`el.style.setProperty("--page-y", el.offsetTop + "px")`), then:

```css
[data-surface] {
  background-position: 0 calc(-1 * var(--page-y, 0px));
}
```

A cut is right only where the paper really changes: a different ground, or a separate piece of
paper such as a sheet, a card, or the manifesto sheet that slides over the spreads.

### 3.3 Dark sections: baked deep plum, plum, oxblood

```css
/* Footer.module.css .body */
.body {
  background-color: var(--deep);
  background-image: var(--tex-deep);
  background-size: var(--tex-size);
}

/* plum and oxblood sheets: the same, with --plum / --tex-plum and --oxblood / --tex-oxblood */
```

### 3.4 Any other light colour: the neutral tile with `multiply`

`multiply` can only darken, so the tile is near white (light: mean 0.980, range 237 to 255;
strong: mean 0.971). Set the background colour to the brand colour divided by that mean and the
average lands back on the brand colour:

```css
.sheet {
  /* cream-2 sheet */
  background-color: var(--cream-2-lift); /* #ECEADB / 0.980 */
  background-image: var(--tex-neutral);
  background-size: var(--tex-size);
  background-blend-mode: multiply;
}
```

For any other light colour, where supported (relative colour syntax):
`background-color: rgb(from #ECEADB calc(r / 0.98) calc(g / 0.98) calc(b / 0.98));`
(use `0.971` with the strong tile).

| Colour | Lifted base, light tile | Lifted base, strong tile | Mean dE00 if you skip the lift (light / strong) |
|---|---|---|---|
| cream `#F3F3E7` (use the baked one) | `#F8F8EC` | `#FAFAEE` | 1.02 / 1.48 |
| cream-2 `#ECEADB` | `#F1EFDF` | `#F3F1E2` | 1.02 / 1.48 |
| cream-3 `#E3E0CD` | `#E8E5D1` | `#EAE7D3` | 1.02 / 1.47 |
| writing paper `#F8F5E8` | `#FDFAED` | `#FFFCEF` (dE00 0.18) | 1.02 / 1.48 |
| bright paper `#FBFAF2` | `#FFFFF7` (dE00 0.48: the lift clips at white) | not reachable (dE00 1.19): use the light tile | 1.02 / 1.48 |
| powder blue `#ABCDD6` (use the baked one) | `#AED1DA` | `#B0D3DC` | 1.01 / 1.47 |

All lifted results are dE00 0.00 against the hex unless noted. On dark colours `multiply` barely
shows (L* std 0.09 to 0.29): use the baked dark papers or the cardstock.

### 3.5 Project spreads: the cardstock tile with `soft-light`

```css
/* Spreads.module.css .spread and .inner; CaseStudy.module.css heads that use --p-bg */
.spread {
  background-color: var(--p-bg);
  background-image: var(--tex-cardstock);
  background-size: var(--tex-size);
  background-blend-mode: soft-light;
}
```

`soft-light` is the recommended mode: it gives an even surface across all five project colours
(L* std 0.85 to 1.13) and lifts the fibres on the dark ones, which is how dyed-through cardstock
looks. `overlay` is linear in the tile, so with this tile (mean exactly 127.5) it leaves the mean
colour exactly where it was. Its strength, though, varies 3.5x between colours (0.48 on deep plum,
1.66 on rust):

| Colour | soft-light: mean dE00 / L* std | overlay: mean dE00 / L* std |
|---|---|---|
| rust `#9F4A30` | 0.13 / 1.11 | 0.03 / 1.66 |
| ink blue `#07253D` | 0.29 / 1.13 | 0.01 / 0.94 |
| magenta `#A11F5B` | 0.08 / 0.85 | 0.02 / 1.30 |
| cocoa `#3F1B0E` | 0.22 / 1.10 | 0.02 / 0.98 |
| vermilion `#A32D02` | 0.14 / 0.90 | 0.02 / 1.29 |
| deep plum `#270617` | 0.26 / 0.68 | 0.02 / 0.48 |
| plum `#390D26` | 0.16 / 0.94 | 0.01 / 0.84 |
| oxblood `#491C17` | 0.18 / 1.11 | 0.02 / 1.09 |

To set the amount per section, put the tile on a pseudo-element instead:

```css
.spread {
  position: relative;
  isolation: isolate;
  background-color: var(--p-bg);
}

.spread::before {
  content: "";
  position: absolute;
  inset: 0;
  z-index: -1; /* above the colour, below the content */
  pointer-events: none;
  background: var(--tex-cardstock) 0 0 / var(--tex-size) repeat;
  mix-blend-mode: soft-light;
  opacity: var(--paper-amount, 1); /* 0.6 to 1 */
}
```

The baked deep plum, plum and oxblood are calmer than the cardstock on the same colours (compare
`previews/paper-deep-plum.jpg` with `previews/cardstock-on-deep-plum.jpg`). Use the baked ones for
the brand's own dark surfaces and keep the cardstock for project colours.

### 3.6 Writing paper with rules

```css
.note {
  background-color: var(--paper-note);
  background-image:
    repeating-linear-gradient(
      to bottom,
      transparent 0 calc(1.9rem - 1px),
      rgb(171 205 214 / 0.6) calc(1.9rem - 1px) 1.9rem
    ),
    var(--tex-writing);
  background-size: auto, var(--tex-size);
}
```

### 3.7 The torn edge

This replaces `torn-top.svg`. The old file is a 4 px zigzag polygon stretched to the element's
width, so on a phone it is squeezed 3.7 times. The new mask repeats at a fixed size. Its tear line
has three scales of irregularity, a 3 to 6 px translucent torn zone, and short fibres that clump
along the edge, all periodic every 1024 px. The tear sits 9 to 24 px below the element's top, and
the mask is solid from 36 px down.

```css
/* Manifesto.module.css .manifesto: replaces the two mask lines */
.manifesto {
  -webkit-mask:
    url("/textures/v3/torn-edge-top.webp") 0 0 / 1024px 48px repeat-x,
    linear-gradient(#000 0 0) 0 46px / 100% 100% no-repeat;
  mask:
    url("/textures/v3/torn-edge-top.webp") 0 0 / 1024px 48px repeat-x,
    linear-gradient(#000 0 0) 0 46px / 100% 100% no-repeat;
}

/* optional: the torn fibres read a little lighter than the sheet (the mask above clips this too) */
.manifesto::before {
  content: "";
  position: absolute;
  inset: 0 0 auto;
  height: 48px;
  z-index: -1; /* .manifesto is a stacking context (z-index: 2): above its paper, below its content */
  pointer-events: none;
  background: var(--paper);
  opacity: 0.35;
  -webkit-mask: url("/textures/v3/torn-rim-top.webp") 0 0 / 1024px 48px repeat-x;
  mask: url("/textures/v3/torn-rim-top.webp") 0 0 / 1024px 48px repeat-x;
}
```

For a torn bottom, use `torn-edge-bottom` at `0 100% / 1024px 48px repeat-x`, with the gradient
layer covering `100% calc(100% - 46px)` from the top. The image is drawn at 2x, so it is crisp on
retina screens and downsamples cleanly on 1x.

### 3.8 PNG fallback (optional)

Every current browser decodes WebP (Safari since 14 on macOS 11). If a fallback is wanted anyway,
write it per property, not through a custom property (an invalid `var()` does not fall back to the
earlier declaration):

```css
body {
  background-image: url("/textures/v3/paper-cream-1024.png");
  background-image: image-set(
    url("/textures/v3/paper-cream-1024.webp") type("image/webp"),
    url("/textures/v3/paper-cream-1024.png") type("image/png")
  );
}
```

Browsers that understand `image-set()` with `type()` fetch only the WebP; older ones take the first
line. Use the PNG of the same size as the WebP, so `--tex-size` fits both. Its weight (576 KB here)
only ever reaches a browser with no WebP. On phones, pair the 512 WebP with the 512 PNG the same way.

### 3.9 Do not

- Combine a baked paper with any `background-blend-mode`.
- Keep the old `.paper-grain::after` overlay (`grain-alpha.png`, multiply, 0.55) on top of the new
  papers: that is a second grain, and it also lay over the content.
- Scale the tiles to sizes other than those in 3.1, or use `background-attachment: fixed` (repaints
  on scroll, and paper moves with its sheet).
- Put the cardstock on the light papers (it is tuned for mid and dark colours) or the neutral tile on
  dark ones (`multiply` does almost nothing there).

---

## 4. Checks

### Colour: mean on the hex

| Paper | hex | mean dE00, WebP 1024 / 512 | mean dE00, PNG 1024 / 512 | L* std 1024 / 512 |
|---|---|---|---|---|
| cream | `#F3F3E7` | 0.10 / 0.03 | 0.01 / 0.01 | 1.11 / 0.90 |
| writing paper | `#F8F5E8` | 0.04 / 0.10 | 0.00 / 0.01 | 0.83 / 0.68 |
| powder blue | `#ABCDD6` | 0.04 / 0.06 | 0.02 / 0.01 | 0.93 / 0.75 |
| deep plum | `#270617` | 0.10 / 0.08 | 0.01 / 0.00 | 0.89 / 0.71 |
| plum | `#390D26` | 0.21 / 0.27 | 0.01 / 0.01 | 0.85 / 0.68 |
| oxblood | `#491C17` | 0.09 / 0.08 | 0.02 / 0.02 | 0.77 / 0.62 |

The mean is the sRGB-encoded mean, which is what a downscale or an eyedropper on a blurred screenshot
reads. The linear-light mean and the median are in `metrics.json`; all stay under dE00 0.3. WebP's
4:2:0 chroma moves the mean a little, so each WebP was re-encoded against its decoded mean until it
landed. A side-by-side of every paper against a flat swatch of its hex reads as the same colour.

### Text at 16 px (WCAG contrast; "worst" = the paper's darkest or lightest 0.1 % patch, blurred 1 px)

| Text on paper | mean | worst |
|---|---:|---:|
| ink `#241319` on cream | 15.9 : 1 | 14.9 : 1 |
| plum `#390D26` on cream | 14.9 : 1 | 13.9 : 1 |
| cream `#F3F3E7` on deep plum | 16.7 : 1 | 15.9 : 1 |
| powder blue on deep plum | 11.1 : 1 | 10.5 : 1 |
| cream on plum / on oxblood | 14.9 / 12.8 : 1 | 14.0 / 12.0 : 1 |
| ink on writing paper | 16.3 : 1 | 15.4 : 1 |
| plum on powder blue | 9.9 : 1 | 9.3 : 1 |
| ink on cream-2 (neutral light) / cream-3 (neutral strong) | 14.7 / 13.5 : 1 | 14.1 / 12.5 : 1 |
| each project's ink on its cardstock spread (soft-light) | 5.1 to 12.8 : 1 | 4.5 to 11.4 : 1 |

The texture costs 5 to 12 % of the flat contrast. The one tight pair is rust (`#FAEBCA` on
`#9F4A30`): 5.1 : 1 flat, and 4.5 : 1 on its lightest 0.1 % patches. That still meets AA, and it
comes from the pair's colours, not the paper. If it needs more room, set `--paper-amount: 0.7` on
the rust spread. The 2x loupe in every panel shows the body text clean at the stroke level.

### Seams and repetition

- Everything is periodic by construction: spectral noise lives on the tile's own Fourier grid;
  blurs, gradients and warps wrap; fibres are drawn with wrapped indices.
- PNG: the step across the wrap falls among the ordinary interior steps for every tile (`seam_rank_png`
  in `metrics.json`: 3 to 95 % of interior neighbour pairs step more than the wrap does, the spread
  chance gives; a seam would be about 0 %).
- WebP: the step across the wrap is close to the source's own pixel step (0.3 to 0.5 L*), but the
  encoder smooths the interior to about half of that, and it cannot filter across the image edge. So
  the wrap ranks high (`seam_rank_webp` 0 to 18 %). There is no brightness offset across it, and it
  could not be seen at 2x zoom even with contrast raised 8x at the corner where four tiles meet. It
  is a 1 px line of the original grain's sharpness, not a seam you can see.
- Repetition: the large clouds are soft-clipped at 1.6 sigma, so no single cloud stands out, and no
  scale is larger than about 40 % of the tile. The 3 x 3 checks show no dominant repeating feature
  at true contrast. With contrast raised x6, the 512 tile's lattice can be found, so the 512 tiles
  also calm their largest clouds (they are the phone tiles).

---

## 5. How the paper is made

It is built in perceptual lightness (CIE L*), as the sum of periodic components:

| Component | What it is | At strength 1, light / dark recipe |
|---|---|---|
| formation, large | cloud-like mottling, blobs about 120 px, slightly longer along x (machine direction) | 0.44 / 0.30 L* |
| formation, mid | about 40 px, domain-warped so the clouds are not round | 0.32 / 0.22 L* |
| flocs | about 12 px, negatively skewed: small denser, darker flocs | 0.20 / 0.12 L* |
| fibre mat | 200,000 very short (6 px), faint, random fibres: the fibrous body of the sheet | 0.24 / 0.12 L* mean strength |
| fibres | 3,400 strands (15 px) and 300 long ones (32 px): curved, tapered, fading in and out along their length (they dip under the sheet); centres follow the flocs | light: 45 % lighter, 55 % darker; dark: about 90 % lighter |
| tooth | a gentle relief (6 px bumps + fibres) lit from the top left | 0.26 / 0.16 L* |
| grain | band-limited, sigma 0.62 px | 0.14 / 0.05 L* |

Strengths: cream 1.6, writing paper 1.6 (less cloud and tooth: a smoother sheet), powder blue 1.35,
deep plum 1.75, plum 1.6, oxblood 1.65, neutral 1.2 / 1.75, cardstock 1.4.

Colour: each pixel's L* comes from the field. Chroma follows lightness by a small factor: on light
papers the darker areas are a touch richer, which is how dyed paper behaves. On dark papers the
lighter fibres keep their chroma, so they read as lighter strands of the same plum, never grey lint
or dust. The colour is a function of that one value, so the PNG is an exact palette image sorted by
lightness, and the encoder sees no chroma noise. The base colour is then solved so the mean lands on
the hex.

The neutral tile is the light recipe, mapped so that multiplying it onto cream gives the same L*
field, with its light side softly compressed to keep the mean near 1. The cardstock tile is the dark
recipe as an offset around mid-grey, 10 levels per L*, with its mean forced to exactly 127.5.

Everything is seeded, so a rebuild is byte-for-byte the same.

---

## 6. Regenerate

Run from `research/textures_v3/tools`, in this order (the preview reads the files the first two write):

```
python make_textures.py   # all papers, both sizes, metrics.json (about 2.5 min)
python make_edge.py       # torn edge masks + previews/torn-edge.jpg
python make_preview.py    # previews/, preview.jpg, contrast.json
```

On this machine `python` is `C:/Users/YB-TSR/AppData/Local/Python/pythoncore-3.14-64/python.exe`.

`make_textures.py --only cream,deep-plum --sizes 1024` rebuilds a subset. The recipes, strengths and
WebP qualities are at the top of `make_textures.py`. `paperlib.py` holds the colour maths (sRGB, Lab,
CIEDE2000, WCAG), the periodic noise and fibre renderer, and the W3C blend modes used to simulate
the CSS. `preview_lib.py` holds the page renderer. Needs numpy, scipy and Pillow (with WebP).

---

## 7. Honest limits

- These are procedural. At 1:1 they read as good uncoated paper: soft cloud, a fibrous body, a few
  visible strands, a quiet tooth. But they have none of the idiosyncrasies of a specific mill sheet,
  such as felt marks, a watermark's ghost or the odd inclusion. A high-resolution scan of a real
  premium stock, cleaned and made seamless, would have more character. It would also be harder to
  keep on the exact brand colours, which these hit to within dE00 0.3.
- The relief is lit from the top left, as in a scan, and that direction holds everywhere.
- The 1024 PNGs are over the 150 KB budget (320 to 580 KB). The WebPs and 512 PNGs are within it.
- The WebP qualities depart from the q80 in the brief, deliberately (section 1).
- `soft-light` moves a project colour's mean by up to dE00 0.29 (ink blue). Use `overlay` where exact
  matters more than evenness.
- `paper-neutral-strong` cannot hold bright paper `#FBFAF2` exactly (white clips the lift), so use
  the light tile there.
- The previews are simulations: the CSS blends are computed with the W3C formulas in sRGB, as
  browsers do, and the text is rendered by FreeType rather than a browser. They have not been checked
  in a live browser on the site.
