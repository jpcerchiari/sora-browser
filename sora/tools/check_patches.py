#!/usr/bin/env python3
"""Confere se os patches do Sora aplicam sobre a versão do ungoogled-chromium, como no build.

Monta uma árvore parcial (minitree.py) com todos os arquivos que os patches em patches/sora/
tocam, já com os patches anteriores da série, e aplica cada patch do Sora com
`patch -p1 --ignore-whitespace --forward`, o mesmo comando do build.py.

    python3 sora/tools/check_patches.py
"""
import re
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
TOOLS = Path(__file__).resolve().parent


def sora_patches():
    lines = (REPO / "patches" / "series").read_text(encoding="utf-8").splitlines()
    return [l.strip() for l in lines if l.strip().startswith("sora/")]


def touched_files(patch):
    text = (REPO / "patches" / patch).read_text(encoding="utf-8")
    return {m for m in re.findall(r"^--- a/(\S+)", text, re.M)}


def created_files(patch):
    text = (REPO / "patches" / patch).read_text(encoding="utf-8")
    return set(re.findall(r"^--- /dev/null\n\+\+\+ b/(\S+)", text, re.M))


def main():
    patches = sora_patches()
    if not patches:
        sys.exit("nenhum patch sora/ em patches/series")
    # Arquivos criados por um patch do Sora (e alterados por outro depois) não existem no
    # Chromium: quem os cria é o próprio patch, aplicado na ordem da série.
    created = set().union(*(created_files(p) for p in patches))
    files = sorted(set().union(*(touched_files(p) for p in patches)) - created)
    with tempfile.TemporaryDirectory() as tmp:
        tree = Path(tmp) / "tree"
        subprocess.run([sys.executable, str(TOOLS / "minitree.py"), str(tree), "--upto", patches[0], *files],
                       check=True, stdout=subprocess.DEVNULL)
        failed = []
        for patch in patches:
            result = subprocess.run(
                ["patch", "-p1", "--ignore-whitespace", "--forward", "--no-backup-if-mismatch",
                 "-d", str(tree), "-i", str(REPO / "patches" / patch)],
                capture_output=True, text=True)
            status = "ok" if result.returncode == 0 else "FALHOU"
            print(f"{status:7} {patch}")
            if result.returncode:
                print(result.stdout + result.stderr)
                failed.append(patch)
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
