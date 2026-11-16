#!/usr/bin/env python3
"""Troca "Chromium" por "Sora" nos textos da interface, numa árvore do Chromium já com os patches.

O grit não tem variável para o nome do produto: chromium_strings.grd e as traduções (.xtb)
escrevem "Chromium" por extenso em cada mensagem. Este script substitui o nome no texto das
mensagens dos .grd de GRDS (e dos .grdp que eles incluem com <part>) e nas traduções listadas
em <translations> de cada um.

O id de uma tradução no .xtb é a impressão digital do texto em inglês da mensagem. Mudou o
inglês, mudou o id; sem remapear, o grit não acha as traduções e a interface cai para o inglês.
Por isso o script lê o .grd com o grit da própria árvore (tools/grit) antes e depois da troca,
pareia as mensagens na ordem e reescreve os ids nos .xtb.

Regras de troca (só "Chromium" com C maiúsculo, só no texto das mensagens):
- não toca atributos (desc, meaning), comentários fora de <message>, nem o conteúdo de <ph>;
- não troca colado a letra/dígito/_ ASCII (ChromiumOS, ChromiumUpdater, fooChromium), nem
  depois de "." "/" "\\" (org.chromium.Chromium, caminhos), nem antes de ".x" (Chromium.exe);
- não troca "Chromium Authors" (direitos autorais) nem "Chromium OS" (o sistema, que algumas
  traduções escrevem separado);
- minúsculo nunca muda (chromium.org, esquemas, flags).
Letra não ASCII colada conta como separador, para pegar "Chromium을" ou "でChromiumを".

Idempotente: numa segunda passada não sobra "Chromium" trocável e o mapa de ids sai vazio.
Os .xtb são gravados antes dos .grd/.grdp, e o .grd por último.

    python3 sora/tools/rebrand_strings.py CAMINHO_DO_CHROMIUM [--name Sora]

O build.py chama depois dos patches e antes da substituição de domínios.
"""
import argparse
import re
import sys
import tempfile
from pathlib import Path

GRDS = [
    "chrome/app/chromium_strings.grd",
    "components/components_chromium_strings.grd",
]

PRODUCT = re.compile(r"(?<![A-Za-z0-9_./\\])Chromium(?![A-Za-z0-9_]|\.[A-Za-z0-9]|\s+(?:Authors|OS)\b)")
MESSAGE = re.compile(r"(<message\b[^>]*>)(.*?)(</message>)", re.S)
TRANSLATION = re.compile(r'<translation id="(\d+)">(.*?)</translation>', re.S)
TAG = re.compile(r"(<[^>]*>)")


def replace_text(body, name):
    """Troca o nome só nos trechos de texto, fora de tags e de <ph>...</ph>."""
    out, in_ph = [], False
    for part in TAG.split(body):
        if part.startswith("<"):
            if part.startswith("<ph") and not part.endswith("/>"):
                in_ph = True
            elif part.startswith("</ph"):
                in_ph = False
        elif not in_ph:
            part = PRODUCT.sub(name, part)
        out.append(part)
    return "".join(out)


def rebrand_grd(text, name):
    return MESSAGE.sub(lambda m: m.group(1) + replace_text(m.group(2), name) + m.group(3), text)


def grd_sources(grd):
    """O .grd e os .grdp que ele inclui, em caminhos relativos à pasta do .grd (como o grit)."""
    sources, pending = {}, [grd.name]
    while pending:
        rel = pending.pop()
        if rel not in sources:
            sources[rel] = (grd.parent / rel).read_text(encoding="utf-8")
            pending += re.findall(r'<part\s+file="([^"]+)"', sources[rel])
    return sources


def message_ids(grd):
    from grit import grd_reader
    from grit.node.message import MessageNode
    root = grd_reader.Parse(str(grd), dir=str(grd.parent), skip_validation_checks=True)
    return [node.GetCliques()[0].GetId() for node in root.Preorder() if isinstance(node, MessageNode)]


def new_message_ids(grd, new_sources):
    """Ids das mensagens com o texto já trocado, lendo uma cópia numa pasta temporária."""
    with tempfile.TemporaryDirectory() as tmp:
        for rel, text in new_sources.items():
            (Path(tmp) / rel).parent.mkdir(parents=True, exist_ok=True)
            (Path(tmp) / rel).write_text(text, encoding="utf-8")
        return message_ids(Path(tmp) / grd.name)


def rebrand_xtb(text, name, id_map):
    def sub(m):
        old_id = m.group(1)
        return '<translation id="%s">%s</translation>' % (id_map.get(old_id, old_id),
                                                          replace_text(m.group(2), name))
    return TRANSLATION.sub(sub, text)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("src", type=Path, help="raiz do Chromium (onde está chrome/)")
    parser.add_argument("--name", default="Sora")
    args = parser.parse_args()

    sys.path.insert(0, str(args.src / "tools" / "grit"))
    for rel in GRDS:
        grd = args.src / rel
        if not grd.is_file():
            sys.exit(f"{grd}: não encontrado")
        old = grd_sources(grd)
        new = {rel: rebrand_grd(text, args.name) for rel, text in old.items()}
        old_ids, new_ids = message_ids(grd), new_message_ids(grd, new)
        if len(old_ids) != len(new_ids):
            sys.exit(f"{rel}: número de mensagens mudou com a troca ({len(old_ids)} -> {len(new_ids)})")
        id_map = {o: n for o, n in zip(old_ids, new_ids) if o != n}

        xtbs = re.findall(r'<file path="([^"]+\.xtb)"', old[grd.name])
        changed = 0
        for path in xtbs:
            xtb = grd.parent / path
            if not xtb.is_file():
                continue  # árvore parcial (testes); no build todas existem
            text = xtb.read_text(encoding="utf-8")
            result = rebrand_xtb(text, args.name, id_map)
            if result != text:
                xtb.write_text(result, encoding="utf-8", newline="\n")
                changed += 1
        # O .grd por último: se a passada parar no meio, a próxima ainda acha os ids antigos.
        for part in sorted(new, key=lambda r: r == grd.name):
            if new[part] != old[part]:
                (grd.parent / part).write_text(new[part], encoding="utf-8", newline="\n")
        print(f"{rel}: {len(id_map)} ids remapeados, {changed}/{len(xtbs)} traduções alteradas")


if __name__ == "__main__":
    main()
