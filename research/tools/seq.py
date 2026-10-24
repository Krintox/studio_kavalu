"""seq.py URL OUT.jpg STEP COUNT [w h] [cols] -> scroll by STEP px COUNT times, one frame per stop, tiled with labels."""
import io, sys, time, base64
from PIL import Image, ImageDraw, ImageFont
from cdp import Tab
url, out, step, count = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
w = int(sys.argv[5]) if len(sys.argv) > 5 else 1440
h = int(sys.argv[6]) if len(sys.argv) > 6 else 900
cols = int(sys.argv[7]) if len(sys.argv) > 7 else 3
t = Tab(); t.front(); t.viewport(w, h, mobile=w < 600)
t.goto(url, wait=4, timeout=60)
t.eval("window.scrollTo(0,0)"); time.sleep(1.5)
frames = []
font = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 22)
for k in range(count):
    if k:
        t.wheel(step, x=w // 2, y=h // 2, steps=max(4, step // 100), pause=0.04)
        time.sleep(1.6)
    r = t.call("Page.captureScreenshot", {"format": "jpeg", "quality": 70})
    im = Image.open(io.BytesIO(base64.b64decode(r["data"]))).convert("RGB")
    y = t.eval("Math.round(scrollY)")
    d = ImageDraw.Draw(im); d.rectangle((0, 0, 190, 34), fill=(255, 230, 0)); d.text((8, 3), f"#{k}  y={y}", fill="black", font=font)
    frames.append(im)
tw = 600 if w > 600 else 300
th = round(tw * h / w)
rows = (len(frames) + cols - 1) // cols
sheet = Image.new("RGB", (cols * tw + (cols - 1) * 6, rows * th + (rows - 1) * 6), (20, 20, 20))
for k, im in enumerate(frames):
    sheet.paste(im.resize((tw, th), Image.LANCZOS), ((k % cols) * (tw + 6), (k // cols) * (th + 6)))
sheet.save(out, quality=84)
print("frames", len(frames))
t.close_ws()
