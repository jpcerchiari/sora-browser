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

    # Same sizes as Chromium's chromium.ico.
    sizes = (16, 32, 48, 256)
    ico = OUT / "chromium" / "win" / "chromium.ico"
    ico.parent.mkdir(parents=True, exist_ok=True)
    render(ICON, 256).save(ico, sizes=[(s, s) for s in sizes],
                           append_images=[render(ICON, s) for s in sizes[:-1]])

    save(tile(600, 220), "chromium/win/tiles/Logo.png")
    save(tile(176, 118), "chromium/win/tiles/SmallLogo.png")


if __name__ == "__main__":
    main()
