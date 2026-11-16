#!/usr/bin/env python3
"""Gera os ícones do Sora a partir de sora/branding/icon/*.svg.

Saída em sora/branding/theme/, com os mesmos caminhos de chrome/app/theme/ no Chromium;
o build.py copia essa pasta por cima da árvore. Rodar de novo sempre que o SVG mudar e
versionar o resultado (o build não depende de cairosvg).

    pip install cairosvg pillow
    python3 sora/tools/render_icons.py
"""
import io
from pathlib import Path

import cairosvg
from PIL import Image

BRANDING = Path(__file__).resolve().parents[1] / "branding"
ICON = BRANDING / "icon" / "sora.svg"
MONO = BRANDING / "icon" / "sora-mono.svg"
OUT = BRANDING / "theme"


def render(svg, size):
    png = cairosvg.svg2png(url=str(svg), output_width=size, output_height=size)
    return Image.open(io.BytesIO(png)).convert("RGBA")


def save(img, rel):
    path = OUT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path, optimize=True)


def document(size, pdf=False):
    """Page with the app icon, as in Chromium's chromium_doc.ico / chromium_pdf.ico."""
    img = render(BRANDING / "icon" / "doc-page.svg", size)
    logo = render(ICON, round(size * 0.47))
    img.alpha_composite(logo, (round(size * 0.265), round(size * 0.42)))
    if pdf:
        img.alpha_composite(render(BRANDING / "icon" / "pdf-label.svg", size))
    return img


def save_ico(make, rel):
    """ICO with the same sizes as Chromium's (16, 32, 48 and 256)."""
    sizes = (16, 32, 48, 256)
    path = OUT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    make(256).save(path, sizes=[(s, s) for s in sizes],
                   append_images=[make(s) for s in sizes[:-1]])


def tile(canvas, logo):
    """Logo centred on a transparent canvas, as in the Windows Start tiles."""
    img = Image.new("RGBA", (canvas, canvas))
    img.paste(render(ICON, logo), ((canvas - logo) // 2,) * 2)
    return img


def main():
    for size in (16, 24, 48, 64, 128, 256):
        save(render(ICON, size), f"chromium/product_logo_{size}.png")
    save(render(MONO, 22), "chromium/product_logo_22_mono.png")
    (OUT / "chromium" / "product_logo.svg").write_bytes(ICON.read_bytes())

    for scale, factor in (("100", 1), ("200", 2)):
        for size in (16, 32):
            save(render(ICON, size * factor), f"default_{scale}_percent/chromium/product_logo_{size}.png")

    save_ico(lambda s: render(ICON, s), "chromium/win/chromium.ico")
    save_ico(document, "chromium/win/chromium_doc.ico")
    save_ico(lambda s: document(s, pdf=True), "chromium/win/chromium_pdf.ico")

    save(tile(600, 220), "chromium/win/tiles/Logo.png")
    save(tile(176, 118), "chromium/win/tiles/SmallLogo.png")


if __name__ == "__main__":
    main()
