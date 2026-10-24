"""Run gen_gemini.py + fidelity.py (gemini mode) for a list of sources, strictly one after another.

    python batch_gemini.py rel1 rel2 ... [--mode "3.1 Pro"] [--tag pro]

Outputs are scored into research/images_hq/gemini/_work/<rel>/<tag>.png first (not the final path) so a human look
decides what is promoted. Stops on a sign-in prompt (exit 3) or a usage-limit reply.
"""
import glob
import json
import os
import re
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
PY = sys.executable
WORK = os.path.join(HERE, "..", "gemini", "_work")


def main():
    args = sys.argv[1:]
    mode, tag = "", "pro"
    if "--mode" in args:
        i = args.index("--mode"); mode = args[i + 1]; del args[i:i + 2]
    if "--tag" in args:
        i = args.index("--tag"); tag = args[i + 1]; del args[i:i + 2]
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    for rel in args:
        name = os.path.basename(rel)
        log = os.path.join(WORK, f"{name}.{tag}.log")
        os.makedirs(WORK, exist_ok=True)
        t0 = time.time()
        cmd = [PY, "-u", os.path.join(HERE, "gen_gemini.py"), rel, "--tag", tag] + (["--mode", mode] if mode else [])
        with open(log, "w", encoding="utf-8") as f:
            r = subprocess.run(cmd, stdout=f, stderr=subprocess.STDOUT, env=env, cwd=HERE)
        txt = open(log, encoding="utf-8").read()
        print(f"{rel}: gen exit {r.returncode} in {int(time.time() - t0)}s", flush=True)
        if r.returncode == 3:
            print("SIGN-IN REQUIRED - stopping", flush=True); break
        if re.search(r"limit|try again later|come back|quota", txt.split("RESPONSE:")[-1], re.I) and r.returncode != 0:
            print("LIMIT? - stopping", flush=True); break
        raws = sorted(glob.glob(os.path.join(WORK, rel.replace("/", os.sep), tag, "raw_0.*")))
        if r.returncode != 0 or not raws:
            continue
        clean = os.path.join(os.path.dirname(raws[0]), "clean.png")
        dw = subprocess.run([PY, os.path.join(HERE, "dewatermark.py"), raws[0], clean], capture_output=True, text=True, env=env, cwd=HERE)
        print("   watermark:", dw.stdout.strip()[:120], flush=True)
        flog = os.path.join(WORK, f"{name}.{tag}.fid.log")
        with open(flog, "w", encoding="utf-8") as f:
            subprocess.run([PY, os.path.join(HERE, "fidelity.py"), "gemini", rel, clean, "--tag", tag, "--out-name", tag],
                           stdout=f, stderr=subprocess.STDOUT, env=env, cwd=HERE)
        try:
            d = json.load(open(os.path.join(HERE, "..", "compare", f"{name}.{tag}.json")))
            print(f"   ssim {d['ssim']} half {d['ssim_half']} ncc {d['ncc']} dE {d['dE_mean']} size {d['size']}", flush=True)
        except Exception as e:
            print("   fidelity read failed", e, flush=True)
        time.sleep(3)


if __name__ == "__main__":
    main()
