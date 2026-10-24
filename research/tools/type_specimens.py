"""Type specimens for the Q6 review: the same Kavalu copy, palette and wordmark set in each candidate.

Writes research/type/specimen_<role>.html (open from disk; Ranade is embedded, the rest come from
Google Fonts and Fontshare). One band per candidate, so roles can be compared one at a time with the
other roles held constant.
"""
import base64
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "research" / "type"
OUT.mkdir(parents=True, exist_ok=True)
FONTS = ROOT / "website" / "src" / "fonts"
WM = (ROOT / "website" / "src" / "components" / "brand" / "wordmark-paths.ts").read_text(encoding="utf-8")

# ---------- the wordmark, straight from the generated paths ----------
def word(name):
    block = re.search(rf"export const {name} = \{{ width: ([\d.]+), height: 100, glyphs: \[(.*?)\] \}};", WM, re.S)
    width = float(block.group(1))
    ds = re.findall(r'd: "([^"]+)"', block.group(2))
    return width, ds

def word_svg(name, h):
    width, ds = word(name)
    paths = "".join(f'<path d="{d}" fill-rule="evenodd"/>' for d in ds)
    return f'<svg viewBox="0 0 {width:.1f} 100" style="height:{h}px;width:auto;display:block" fill="currentColor">{paths}</svg>'

LOCKUP = f'<div class="wm">{word_svg("STUDIO", 15)}<div style="height:3px"></div><div style="padding-left:4px">{word_svg("KAVALU", 15)}</div></div>'

# ---------- fonts ----------
def ranade_faces():
    css = []
    for wt, style, f in [(300, "normal", "Light"), (400, "normal", "Regular"), (400, "italic", "Italic"), (500, "normal", "Medium")]:
        b64 = base64.b64encode((FONTS / f"Ranade-{f}.woff2").read_bytes()).decode()
        css.append(f"@font-face{{font-family:'Ranade';src:url(data:font/woff2;base64,{b64}) format('woff2');font-weight:{wt};font-style:{style}}}")
    return "\n".join(css)

GOOGLE = (
    "https://fonts.googleapis.com/css2?"
    "family=Fraunces:ital,opsz,wght,SOFT,WONK@0,9..144,300..700,0..100,0..1;1,9..144,300..700,0..100,0..1"
    "&family=Newsreader:ital,opsz,wght@0,6..72,300..600;1,6..72,300..600"
    "&family=IBM+Plex+Mono:wght@400;500&family=Courier+Prime:ital,wght@0,400;0,700;1,400"
    "&family=Cutive+Mono&family=Xanh+Mono:ital@0;1"
    "&family=Hanken+Grotesk:ital,wght@0,300..600;1,300..600"
    "&family=Homemade+Apple&family=Nothing+You+Could+Do&family=Reenie+Beanie&family=La+Belle+Aurore"
    "&family=Kalam:wght@300;400&family=Mrs+Saint+Delafield&family=Anek+Kannada:wdth,wght@75..125,300..700"
    "&display=swap"
)
# the Fontshare API serves one family per request, so each family gets its own stylesheet
FONTSHARE = [f"https://api.fontshare.com/v2/css?f[]={f}@300,301,400,401,500,501&display=swap"
             for f in ["gambetta", "erode", "sentient", "boska", "bespoke-serif", "switzer", "author"]]
FONTSHARE.append("https://api.fontshare.com/v2/css?f[]=zodiak@300,301,400,401,700&display=swap")

C = {"cream": "#F3F3E7", "ox": "#491C17", "plum": "#390D26", "deep": "#270617", "blue": "#ABCDD6", "faint": "rgb(57 13 38 / .55)"}

BASE_CSS = f"""
{ranade_faces()}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:#d9d6c8;font-family:Ranade,sans-serif;color:{C['plum']};-webkit-font-smoothing:antialiased}}
.band{{display:grid;grid-template-columns:1fr 430px;width:1440px;border-bottom:6px solid #d9d6c8}}
.paper{{background:{C['cream']};padding:34px 48px 38px;position:relative}}
.dark{{background:{C['deep']};color:{C['cream']};padding:34px 36px 38px;position:relative}}
.tag{{font:500 11px/1 'IBM Plex Mono',monospace;letter-spacing:.09em;text-transform:uppercase;color:{C['faint']};display:flex;justify-content:space-between;margin-bottom:22px}}
.dark .tag{{color:rgb(243 243 231 / .5)}}
.wm{{color:{C['plum']}}}
.dark .wm{{color:{C['blue']}}}
em{{font-style:italic}}
"""

def page(title, bands, extra_css=""):
    return f"""<!doctype html><html><head><meta charset="utf-8"><title>{title}</title>
<link rel="stylesheet" href="{GOOGLE}">{"".join(f'<link rel="stylesheet" href="{u}">' for u in FONTSHARE)}
<style>{BASE_CSS}{extra_css}</style></head><body>{''.join(bands)}</body></html>"""

# ---------- 1. display serif ----------
DISPLAY = [
    ("Fraunces", "Google · current", "font-family:Fraunces;font-variation-settings:'SOFT' 0,'WONK' 0", "font-variation-settings:'SOFT' 100,'WONK' 1"),
    ("Gambetta", "Fontshare / ITF", "font-family:Gambetta", ""),
    ("Erode", "Fontshare / ITF", "font-family:Erode", ""),
    ("Sentient", "Fontshare / ITF", "font-family:Sentient", ""),
    ("Zodiak", "Fontshare / ITF", "font-family:Zodiak", ""),
    ("Boska", "Fontshare / ITF", "font-family:Boska", ""),
    ("Bespoke Serif", "Fontshare / ITF", "font-family:'Bespoke Serif'", ""),
    ("Newsreader", "Google · Production Type", "font-family:Newsreader", ""),
]

def display_band(i, name, src, fam, ital):
    return f"""<section class="band"><div class="paper">
  <p class="tag"><span>{i:02d} — {name}</span><span>{src}</span></p>
  <h1 style="{fam};font-weight:320;font-size:78px;line-height:.98;letter-spacing:-.02em">Every brand hits a <em style="{ital}">crossroads.</em></h1>
  <h2 style="{fam};font-weight:320;font-size:42px;line-height:1.05;letter-spacing:-.015em;margin-top:22px">What we pin above <em style="{ital}">the desk.</em></h2>
  <p style="{fam};font-weight:400;font-size:27px;margin-top:20px;letter-spacing:-.01em">Studio Anokhi &nbsp;·&nbsp; Nivritti &nbsp;·&nbsp; Not so Onam &nbsp;·&nbsp; <em style="{ital}">Fillers, not yet</em></p>
  <p style="font:400 17px/1.55 Ranade;max-width:640px;margin-top:18px">A brand is a set of choices; what it says, how it looks, where it shows up, who it speaks to.</p>
</div><div class="dark">
  {LOCKUP}
  <p style="{fam};font-weight:340;font-size:38px;line-height:1;letter-spacing:-.015em;margin-top:44px;color:{C['blue']}">Standing at a <em style="{ital}">crossroads?</em></p>
  <p style="{fam};font-weight:400;font-size:21px;margin-top:22px">connect@studiokavalu.com</p>
  <p style="font:400 15px/1.5 Ranade;margin-top:14px;opacity:.8">Five short steps, about three minutes, read by Ananya.</p>
</div></section>"""

# ---------- 2. text face (display held on the current Fraunces) ----------
TEXT = [("Ranade", "Fontshare / ITF · current"), ("Switzer", "Fontshare / ITF"), ("Author", "Fontshare / ITF"), ("Hanken Grotesk", "Google")]

def text_band(i, name, src):
    f = f"font-family:'{name}'"
    return f"""<section class="band"><div class="paper">
  <p class="tag"><span>{i:02d} — {name}</span><span>{src}</span></p>
  <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:26px">
    {LOCKUP}<nav style="{f};font-size:15px;display:flex;gap:34px"><span>Work</span><span>Studio</span></nav>
    <span style="{f};font-size:14px;background:{C['plum']};color:{C['cream']};padding:12px 20px;border-radius:99px">● Start a project</span></div>
  <h2 style="font-family:Fraunces;font-weight:320;font-size:46px;letter-spacing:-.02em;line-height:1">The studio, <em style="font-variation-settings:'SOFT' 100,'WONK' 1">and the roads.</em></h2>
  <p style="{f};font-weight:400;font-size:18px;line-height:1.6;max-width:720px;margin-top:18px">Studio Kavalu is a branding and content house that makes these choices with you. We shape brands, feeds and persona through a design lens backed with strategy. The aim: work with a point of view clear enough that people recognise it, and others follow it.</p>
  <p style="{f};font-weight:500;font-size:14px;margin-top:16px;color:{C['ox']}">Logo design · Visual identity · Packaging · Social media strategy</p>
</div><div class="dark">
  <p style="{f};font-weight:300;font-size:30px;line-height:1.15">Brand identity for a pottery studio in Bengaluru.</p>
  <p style="{f};font-size:15px;line-height:1.55;margin-top:18px;opacity:.85">A soft, rounded sans-serif forms the primary logo, its letters stacked closely together like interlocking puzzle pieces.</p>
  <p style="{f};font-style:italic;font-size:15px;margin-top:14px;color:{C['blue']}">Read the case study →</p>
</div></section>"""

# ---------- 3. label face ----------
LABELS = [("IBM Plex Mono", "Google · current", ""), ("Courier Prime", "Google · typewriter", ""), ("Cutive Mono", "Google · typewriter", ""), ("Xanh Mono", "Google", "")]

def label_band(i, name, src, _):
    f = f"font-family:'{name}'"
    strip = f"display:inline-block;background:#fbfaf2;padding:6px 10px 5px;box-shadow:0 1px 2px rgb(0 0 0 / .18);{f};font-size:12.5px;letter-spacing:.02em;color:{C['plum']}"
    return f"""<section class="band"><div class="paper">
  <p class="tag"><span>{i:02d} — {name}</span><span>{src}</span></p>
  <div style="display:grid;grid-template-columns:repeat(3,auto);justify-content:start;gap:8px 46px;{f};text-transform:uppercase;letter-spacing:.09em;font-size:11px;color:{C['faint']}">
    <span>Client</span><span>Year</span><span>Services</span></div>
  <div style="display:grid;grid-template-columns:repeat(3,auto);justify-content:start;gap:8px 46px;margin-top:6px;font:400 17px Ranade">
    <span>Studio Anokhi</span><span>2025</span><span>Brand identity, social media</span></div>
  <p style="margin-top:26px;transform:rotate(-1.2deg)"><span style="{strip}">Studio Anokhi · the अ mark, cut from a pot's silhouette</span></p>
  <p style="margin-top:14px;transform:rotate(.8deg)"><span style="{strip}">Nivritti · linocut Himalaya, burnt orange and navy</span></p>
  <p style="margin-top:22px;{f};font-size:11px;letter-spacing:.1em;text-transform:uppercase">01 &nbsp; Home &nbsp;&nbsp; 02 &nbsp; Work &nbsp;&nbsp; 03 &nbsp; Studio &nbsp;&nbsp; Bengaluru 02:00 IST</p>
</div><div class="dark">
  <div style="background:{C['blue']};color:{C['deep']};padding:22px 24px">
    <p style="{f};font-size:11px;letter-spacing:.1em;text-transform:uppercase;opacity:.8">Admit one · ಕವಲು</p>
    <p style="font-family:Fraunces;font-weight:340;font-size:32px;line-height:1;margin-top:12px">Standing at a <em style="font-variation-settings:'SOFT' 100,'WONK' 1">crossroads?</em></p>
    <p style="{f};font-size:11px;letter-spacing:.04em;margin-top:14px;opacity:.75">Five short steps · about three minutes · read by Ananya</p>
  </div>
  <p style="{f};font-size:11px;letter-spacing:.1em;text-transform:uppercase;margin-top:22px;opacity:.7">© 2026 Studio Kavalu · A branding & content house, Bengaluru</p>
</div></section>"""

# ---------- 4. handwriting ----------
HANDS = [("Homemade Apple", "Google · current", 22), ("Nothing You Could Do", "Google", 24), ("La Belle Aurore", "Google", 26), ("Reenie Beanie", "Google", 34), ("Kalam", "Google / ITF", 24)]

def hand_band(i, name, src, size):
    f = f"font-family:'{name}'"
    return f"""<section class="band"><div class="paper" style="display:flex;gap:40px;align-items:flex-start">
  <div style="flex:1"><p class="tag"><span>{i:02d} — {name}</span><span>{src}</span></p>
  <div style="background:#fbfaf2;padding:22px 24px;width:330px;transform:rotate(-2deg);box-shadow:0 2px 3px rgb(0 0 0 / .18)">
    <p style="{f};font-size:{size}px;line-height:1.45;color:{C['plum']}">a point where paths meet, split, and become something new.</p></div></div>
  <div style="background:{C['blue']};padding:22px 24px;width:330px;transform:rotate(2.5deg);margin-top:30px;box-shadow:0 2px 3px rgb(0 0 0 / .18)">
    <p style="{f};font-size:{size}px;line-height:1.45;color:{C['deep']}">I don't design things. I design the story that holds them together.</p>
    <p style="font:500 11px 'IBM Plex Mono';letter-spacing:.09em;text-transform:uppercase;margin-top:10px">— Ananya</p></div>
  <p style="{f};font-size:{size - 2}px;color:{C['ox']};transform:rotate(-4deg);margin-top:60px">go on, move things around</p>
</div><div class="dark">
  <p style="{f};font-size:{size}px;color:{C['blue']};transform:rotate(-3deg);margin-top:30px">swipe along the desk →</p>
  <p style="font-family:'Mrs Saint Delafield';font-size:64px;margin-top:30px;color:{C['cream']}">Ananya</p>
</div></section>"""

# ---------- 5. the whole system: current against proposed ----------
SYSTEMS = [
    ("Current", "Fraunces · Ranade · IBM Plex Mono · Homemade Apple",
     "font-family:Fraunces", "font-variation-settings:'SOFT' 100,'WONK' 1", "Ranade", "IBM Plex Mono"),
    ("Proposed", "Gambetta · Switzer · Courier Prime · Homemade Apple",
     "font-family:Gambetta", "", "Switzer", "Courier Prime"),
]

def system_band(i, name, desc, disp, ital, text, mono):
    t, m = f"font-family:'{text}'", f"font-family:'{mono}'"
    lab = f"{m};font-size:11px;letter-spacing:.09em;text-transform:uppercase"
    strip = f"display:inline-block;background:#fbfaf2;padding:6px 10px 5px;box-shadow:0 1px 2px rgb(0 0 0 / .18);{m};font-size:12.5px;color:{C['plum']}"
    return f"""<section class="band" style="grid-template-columns:1fr 470px"><div class="paper" style="padding-bottom:46px">
  <p class="tag"><span>{i:02d} — {name}</span><span>{desc}</span></p>
  <div style="display:flex;align-items:center;justify-content:space-between">
    {LOCKUP}<nav style="{t};font-size:15px;display:flex;gap:34px"><span>Work</span><span>Studio</span></nav>
    <span style="{lab};opacity:.75">Bengaluru 02:00 IST</span></div>
  <p style="{lab};margin-top:44px;color:{C['ox']}">A branding &amp; content house · Bengaluru</p>
  <h1 style="{disp};font-weight:320;font-size:104px;line-height:.95;letter-spacing:-.025em;margin-top:14px">A brand is a set<br>of <em style="{ital}">choices.</em></h1>
  <p style="{t};font-size:18px;line-height:1.6;max-width:600px;margin-top:22px">What it says, how it looks, where it shows up, who it speaks to. Studio Kavalu makes these choices with you.</p>
  <p style="margin-top:22px;transform:rotate(-1.4deg)"><span style="{strip}">Studio Anokhi · the अ mark, cut from a pot's silhouette</span></p>
  <p style="font-family:'Homemade Apple';font-size:19px;color:{C['ox']};transform:rotate(-3deg);margin:18px 0 0 340px">every piece adds up to one story</p>
</div><div class="dark">
  <div style="background:{C['blue']};color:{C['deep']};padding:24px 26px;transform:rotate(-1.5deg)">
    <p style="{lab};opacity:.8">Admit one · ಕವಲು</p>
    <p style="{disp};font-weight:340;font-size:36px;line-height:1;margin-top:12px">Standing at a <em style="{ital}">crossroads?</em></p>
    <p style="{t};font-size:15px;margin-top:16px;display:inline-block;background:{C['deep']};color:{C['cream']};padding:11px 18px;border-radius:99px">Start a project →</p>
    <p style="{m};font-size:11px;margin-top:14px;opacity:.75">Five short steps · about three minutes · read by Ananya</p>
  </div>
  <div style="background:#fbfaf2;color:{C['plum']};padding:20px 24px;margin-top:30px;transform:rotate(1deg)">
    <p style="{lab};color:{C['faint']}">Write to the studio</p>
    <p style="{disp};font-size:24px;margin-top:10px;color:{C['plum']}">connect@studiokavalu.com</p>
    <p style="{t};font-size:14px;margin-top:10px">Bengaluru, India &nbsp;·&nbsp; Clients worldwide</p>
  </div>
</div></section>"""

specs = {
    "system": page("Kavalu type — current against proposed", [system_band(i + 1, *s) for i, s in enumerate(SYSTEMS)]),
    "display": page("Kavalu type — display serif", [display_band(i + 1, *d) for i, d in enumerate(DISPLAY)]),
    "text": page("Kavalu type — text face", [text_band(i + 1, *t) for i, t in enumerate(TEXT)]),
    "labels": page("Kavalu type — label face", [label_band(i + 1, *l) for i, l in enumerate(LABELS)]),
    "hand": page("Kavalu type — handwriting", [hand_band(i + 1, *h) for i, h in enumerate(HANDS)]),
}
for k, html in specs.items():
    (OUT / f"specimen_{k}.html").write_text(html, encoding="utf-8")
    print("wrote", OUT / f"specimen_{k}.html", f"{len(html) // 1024} KB")
