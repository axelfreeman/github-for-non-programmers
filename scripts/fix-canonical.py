#!/usr/bin/env python3
"""Добавляет self-canonical на все страницы, где его нет.

Использование:
    python3 fix-canonical.py https://example.com /var/www/site

Маппинг файл -> URL строится из пути: /var/www/site/about/index.html -> https://example.com/about/
Главная (index.html в корне) -> https://example.com/
"""
import glob
import os
import sys

BASE = sys.argv[1].rstrip("/") if len(sys.argv) > 1 else "https://example.com"
SITE = sys.argv[2].rstrip("/") if len(sys.argv) > 2 else "/var/www/site"

fixed = skipped = 0
for path in glob.glob(SITE + "/**/index.html", recursive=True):
    rel = os.path.relpath(path, SITE)
    if rel == "index.html":
        url = BASE + "/"
    else:
        url = BASE + "/" + os.path.dirname(rel) + "/"

    with open(path, encoding="utf-8") as f:
        html = f.read()

    if 'rel="canonical"' in html:
        skipped += 1
        continue

    link = f'<link rel="canonical" href="{url}">'
    if "</head>" in html:
        html = html.replace("</head>", link + "\n</head>", 1)
    else:
        skipped += 1
        continue

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    fixed += 1
    print("canonical:", url)

print(f"\nfixed: {fixed}, skipped (already present / no head): {skipped}")
