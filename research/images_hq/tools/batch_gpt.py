"""Run gen_gpt.py + fidelity.py for a list of sources, one after another, in our own ChatGPT tab.
Stops as soon as ChatGPT reports an image-generation limit (exit code 7).

    python batch_gpt.py rel1 rel2 ...  [--strict]
"""
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
PY = sys.executable
WORK = os.path.join(HERE, "..", "gpt", "_work")


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = [a for a in sys.argv[1:] if a.startswith("--")]
    tag = "strict" if "--strict" in flags else "base"
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    for rel in args:
        log = os.path.join(WORK, os.path.basename(rel) + f".{tag}.log")
        t0 = time.time()
        with open(log, "w", encoding="utf-8") as f:
            r = subprocess.run([PY, "-u", os.path.join(HERE, "gen_gpt.py"), rel] + flags, stdout=f,
                               stderr=subprocess.STDOUT, env=env, cwd=HERE)
        print(f"{rel}: gen exit {r.returncode} in {int(time.time() - t0)}s", flush=True)
        if r.returncode == 7:
            print("LIMIT REACHED - stopping batch", flush=True)
            break
        if r.returncode != 0:
            continue
        raw = os.path.join(WORK, rel.replace("/", os.sep), tag, "raw_0.png")
        flog = os.path.join(WORK, os.path.basename(rel) + f".{tag}.fid.log")
        with open(flog, "w", encoding="utf-8") as f:
            r2 = subprocess.run([PY, os.path.join(HERE, "fidelity.py"), "gpt", rel, raw, "--tag", tag] +
                                (["--out-name", "strict"] if tag == "strict" else []),
                                stdout=f, stderr=subprocess.STDOUT, env=env, cwd=HERE)
        print(f"{rel}: fidelity exit {r2.returncode}", flush=True)
        time.sleep(3)


if __name__ == "__main__":
    main()
