"""Swap checked high-quality pictures into the site: swap_hq_image.py nivritti/cleanser-bottle ...
For each key: back up the current file to research/images_hq/originals/ (keeping its size and time, which
purge_image_cache.py relies on), write research/images_hq/gemini/<key>.png over it as a progressive JPEG
(quality 88, longest side at most 2400 px), and record its size, average colour and `hq` in
content/image-meta.json. Then run purge_image_cache.py, or the old resizes stay up to 4 hours."""
import json
import shutil
import sys
from pathlib import Path

from PIL import Image

ROOT = Path("C:/shashank/shashank/fnf/ananya_residency/studio_kavalu")
HQ = ROOT / "research/images_hq"
PUB = ROOT / "website/public/work"
META = ROOT / "website/src/content/image-meta.json"

keys = sys.argv[1:]
meta = json.loads(META.read_text(encoding="utf-8"))
for key in keys:
    src = HQ / "gemini" / f"{key}.png"
    cur = PUB / f"{key}.jpg"
    assert src.exists(), src
    assert cur.exists(), cur
    assert key in meta and not meta[key].get("hq"), (key, meta.get(key))
    backup = HQ / "originals" / f"{key}.jpg"
    backup.parent.mkdir(parents=True, exist_ok=True)
    if not backup.exists():
        shutil.copy2(cur, backup)
    im = Image.open(src).convert("RGB")
    if max(im.size) > 2400:
        k = 2400 / max(im.size)
        im = im.resize((round(im.width * k), round(im.height * k)), Image.LANCZOS)
    im.save(cur, "JPEG", quality=88, progressive=True, optimize=True)
    r, g, b = im.resize((1, 1), Image.BOX).getpixel((0, 0))
    meta[key] = {"w": im.width, "h": im.height, "avg": f"#{r:02X}{g:02X}{b:02X}", "hq": True}
    print(key, im.size, meta[key]["avg"], f"{cur.stat().st_size // 1024} KB", "backup:", backup.relative_to(ROOT))
META.write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
