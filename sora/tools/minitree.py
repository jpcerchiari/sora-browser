#!/usr/bin/env python3
"""Monta uma árvore parcial do Chromium para escrever patches sem baixar o código inteiro.

Baixa só os arquivos pedidos, na versão de ungoogled-chromium/chromium_version.txt, e aplica
neles, na ordem do build.py, os patches do ungoogled-chromium, os do Windows e os do Sora.
A árvore sai com um commit "base" (os arquivos como estarão antes do patch novo) e serve
para editar e gerar o patch com `git diff`.

    python3 sora/tools/minitree.py DESTINO caminho/no/chromium.cc [...]
    python3 sora/tools/minitree.py DESTINO --upto sora/foo.patch caminho.cc

--upto PATCH aplica a série só até antes de PATCH: serve para refazer um patch que já está
na série. A substituição de domínios do ungoogled roda depois dos patches no build, então
não entra aqui.
"""
import argparse
import base64
import os
import re
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
GITILES = "https://chromium.googlesource.com/chromium/src/+/refs/tags/{version}/{path}?format=TEXT"


def series(patches_dir):
    lines = (patches_dir / "series").read_text(encoding="utf-8").splitlines()
    return [patches_dir / l.strip() for l in lines if l.strip() and not l.lstrip().startswith("#")]


def created_by_series():
    """Files that some patch in the series creates (diff from /dev/null)."""
    created = set()
    for patch in series(REPO / "ungoogled-chromium" / "patches") + series(REPO / "patches"):
        text = patch.read_text(encoding="utf-8", errors="replace")
        created.update(re.findall(r"^--- /dev/null\n\+\+\+ b/(\S+)", text, re.M))
    return created


CACHE = Path(os.environ.get("SORA_CHROMIUM_CACHE", Path.home() / ".cache" / "sora-chromium"))


def fetch(version, path):
    """Baixa do gitiles, com cache local por versão (o gitiles limita requisições)."""
    cached = CACHE / version / path
    if cached.is_file():
        return cached.read_bytes()
    url = GITILES.format(version=version, path=path)
    for attempt in range(5):
        try:
            with urllib.request.urlopen(url, timeout=60) as resp:
                data = base64.b64decode(resp.read())
            break
        except urllib.error.HTTPError as err:
            if err.code != 429 or attempt == 4:
                sys.exit(f"{path}: {err.code} em {url}")
            time.sleep(10 * (attempt + 1))
    cached.parent.mkdir(parents=True, exist_ok=True)
    cached.write_bytes(data)
    return data


def git(dest, *args):
    subprocess.run(["git", "-C", str(dest), *args], check=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("dest", type=Path)
    parser.add_argument("files", nargs="+")
    parser.add_argument("--upto", help="caminho do patch, relativo a patches/, que não deve ser aplicado")
    args = parser.parse_args()

    if args.dest.exists() and any(args.dest.iterdir()):
        sys.exit(f"{args.dest} já existe e não está vazio")
    version = (REPO / "ungoogled-chromium" / "chromium_version.txt").read_text().strip()

    created = created_by_series()
    for path in args.files:
        if path in created:
            continue  # an earlier patch creates it; `git apply` below does that
        target = args.dest / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(fetch(version, path))

    git(args.dest, "init", "-q")
    upto = (REPO / "patches" / args.upto).resolve() if args.upto else None
    applied = []
    for patch in series(REPO / "ungoogled-chromium" / "patches") + series(REPO / "patches"):
        if patch.resolve() == upto:
            break
        text = patch.read_text(encoding="utf-8", errors="replace")
        if not any(f in text for f in args.files):
            continue
        includes = [f"--include={f}" for f in args.files]
        git(args.dest, "apply", "--whitespace=nowarn", *includes, str(patch))
        applied.append(patch.relative_to(REPO))

    git(args.dest, "add", "-A")
    git(args.dest, "-c", "user.name=minitree", "-c", "user.email=minitree@localhost",
        "commit", "-q", "-m", f"base {version}")
    print(f"Chromium {version} em {args.dest}")
    for p in applied:
        print(f"  aplicado: {p}")


if __name__ == "__main__":
    main()
