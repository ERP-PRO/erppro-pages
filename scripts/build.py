#!/usr/bin/env python3
"""Monta o site de erppro.pages.dev a partir de site/ e paginas.json.

- Atualiza o bloco de guias da capa (entre <!-- GUIAS:INICIO --> e <!-- GUIAS:FIM -->)
- Gera site/sitemap.xml e site/robots.txt
- Gera dist/site.zip e dist/site.zip.b64 (para enviar pela tela de upload da Cloudflare)

Uso: python3 scripts/build.py
"""
import base64
import html
import json
import os
import re
import sys
import zipfile
from datetime import date

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(RAIZ, "site")
DIST = os.path.join(RAIZ, "dist")


def main():
    with open(os.path.join(RAIZ, "paginas.json"), encoding="utf-8") as f:
        dados = json.load(f)
    base = dados["site"].rstrip("/")
    guias = sorted(dados["guias"], key=lambda g: g["publicado_em"], reverse=True)

    # Confere se cada guia existe
    for g in guias:
        caminho = os.path.join(SITE, g["slug"], "index.html")
        if not os.path.isfile(caminho):
            sys.exit(f"ERRO: falta {caminho}")

    # Bloco de guias da capa
    cards = []
    for i, g in enumerate(guias):
        classe = "tile dark s3" if i == 0 else "tile s3"
        estilo = ' style="color:#a5f3fc"' if i == 0 else ""
        cards.append(
            f'    <div class="{classe}"><div class="ic">{g.get("icone", "📘")}</div>'
            f'<h3>{html.escape(g["titulo"])}</h3><p>{html.escape(g["resumo"])} '
            f'<a href="/{g["slug"]}/"{estilo}>Ler o guia</a></p></div>'
        )
    capa_path = os.path.join(SITE, "index.html")
    with open(capa_path, encoding="utf-8") as f:
        capa = f.read()
    novo, n = re.subn(
        r"<!-- GUIAS:INICIO -->.*?<!-- GUIAS:FIM -->",
        "<!-- GUIAS:INICIO -->\n" + "\n".join(cards) + "\n<!-- GUIAS:FIM -->",
        capa,
        flags=re.S,
    )
    if n != 1:
        sys.exit("ERRO: marcadores GUIAS não encontrados na capa")
    with open(capa_path, "w", encoding="utf-8") as f:
        f.write(novo)

    # sitemap e robots
    hoje = date.today().isoformat()
    urls = [f"  <url><loc>{base}/</loc><lastmod>{hoje}</lastmod></url>"]
    for g in guias:
        urls.append(f"  <url><loc>{base}/{g['slug']}/</loc><lastmod>{g['publicado_em']}</lastmod></url>")
    with open(os.path.join(SITE, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                + "\n".join(urls) + "\n</urlset>\n")
    with open(os.path.join(SITE, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(f"User-agent: *\nAllow: /\n\nSitemap: {base}/sitemap.xml\n")

    # zip para upload
    os.makedirs(DIST, exist_ok=True)
    zip_path = os.path.join(DIST, "site.zip")
    if os.path.exists(zip_path):
        os.remove(zip_path)
    import shutil
    import subprocess
    if shutil.which("zip"):
        # Formato que a Cloudflare comprovadamente lê (pastas incluídas)
        subprocess.run(["zip", "-q", "-r", "-9", zip_path, "."], cwd=SITE, check=True)
    else:
      with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for pasta, _, arquivos in os.walk(SITE):
            rel_pasta = os.path.relpath(pasta, SITE)
            if rel_pasta != ".":
                # A Cloudflare só lê subpastas que têm entrada de diretório no zip
                info = zipfile.ZipInfo(rel_pasta.replace(os.sep, "/") + "/")
                info.external_attr = (0o40755 << 16) | 0x10  # marca como pasta
                info.create_system = 3
                z.writestr(info, "")
            for nome in sorted(arquivos):
                cheio = os.path.join(pasta, nome)
                z.write(cheio, os.path.relpath(cheio, SITE))
    with open(zip_path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    with open(zip_path + ".b64", "w") as f:
        f.write(b64)
    print(f"OK: {len(guias)} guias, zip {os.path.getsize(zip_path)} bytes, base64 {len(b64)} chars")


if __name__ == "__main__":
    main()
