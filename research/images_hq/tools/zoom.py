"""Side-by-side zoom of one region (given in SOURCE pixel coords) of the source and a candidate.

    python zoom.py <rel> <candidate.png> x0,y0,x1,y1 <out.jpg> [height]
"""
from __future__ import annotations

import os
import sys

from PIL import Image, ImageDraw

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
SRC_DIR = os.path.join(ROOT, "website", "public", "work")


def main() -> int:
    rel, cand, box, out = sys.argv[1:5]
    H = int(sys.argv[5]) if len(sys.argv) > 5 else 700
    src = Image.open(os.path.join(SRC_DIR, rel.replace("/", os.sep) + ".jpg")).convert("RGB")
    c = Image.open(cand).convert("RGB")
    x0, y0, x1, y1 = [float(v) for v in box.split(",")]
    sx, sy = c.width / src.width, c.height / src.height
    a = src.crop((int(x0), int(y0), int(x1), int(y1)))
    b = c.crop((int(x0 * sx), int(y0 * sy), int(x1 * sx), int(y1 * sy)))
    w = round(H * a.width / a.height)
    a = a.resize((w, H), Image.LANCZOS)
    b = b.resize((w, H), Image.LANCZOS)
    img = Image.new("RGB", (2 * w + 30, H + 30), (250, 248, 242))
    img.paste(a, (10, 25))
    img.paste(b, (w + 20, 25))
    d = ImageDraw.Draw(img)
    d.text((10, 6), "source " + box, fill=(0, 0, 0))
    d.text((w + 20, 6), "candidate", fill=(0, 0, 0))
    img.save(out, quality=92)
    print(out, img.size)
    return 0


if __name__ == "__main__":
    sys.exit(main())
