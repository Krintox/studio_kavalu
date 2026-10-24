"""Drop Next's cached resizes of the pictures that were replaced, and nothing else.

Each cache entry is <cache>/<key>/<maxAge>.<expireAt>.<etag>.<upstreamEtag>.<ext>, where upstreamEtag is
the base64url of the source file's ETag, W/"<size hex>-<mtime ms hex>". The old sources are backed up in
research/images_hq/originals with their size and mtime kept (shutil.copy2), so an entry made from an old
source can be recognised exactly. A missing entry is a cache miss to Next (it rebuilds it), so this is
safe while the dev server runs."""
import base64
import shutil
import sys
from pathlib import Path

ROOT = Path("C:/shashank/shashank/fnf/ananya_residency/studio_kavalu")
ORIG = ROOT / "research/images_hq/originals"
dry = "--dry" in sys.argv

old = {}
for f in ORIG.rglob("*.jpg"):
    st = f.stat()
    old[f'W/"{st.st_size:x}-{st.st_mtime_ns // 1_000_000:x}"'] = f.relative_to(ORIG).as_posix()
print(f"{len(old)} replaced pictures")

for cache in (ROOT / "website/.next/dev/cache/images", ROOT / "website/.next/cache/images"):
    if not cache.exists():
        continue
    hits, total = {}, 0
    for entry in cache.iterdir():
        files = list(entry.iterdir()) if entry.is_dir() else []
        if not files:
            continue
        total += 1
        parts = files[0].name.split(".", 4)
        if len(parts) < 5:
            continue
        try:
            up = base64.urlsafe_b64decode(parts[3] + "=" * (-len(parts[3]) % 4)).decode("utf-8", "replace")
        except Exception:
            continue
        if up in old:
            hits.setdefault(old[up], []).append(entry)
    n = sum(len(v) for v in hits.values())
    print(f"{cache.relative_to(ROOT)}: {total} entries, {n} made from replaced pictures")
    for name, entries in sorted(hits.items()):
        print(f"  {len(entries):3d}  {name}")
        if not dry:
            for e in entries:
                shutil.rmtree(e, ignore_errors=True)
