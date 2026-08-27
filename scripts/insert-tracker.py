#!/usr/bin/env python3
"""Вставляет tracking-скрипт (Umami / GA) во все .html сайта — идемпотентно.

Использование:
    python3 insert-tracker.py /var/www/site '<script defer src="..." data-website-id="ID"></script>'

Повторный запуск пропускает файлы, где скрипт уже есть.
Работает на статике (голый HTML), для Next.js — вставлять в layout.tsx один раз.
"""
import glob
import sys

BASE = sys.argv[1] if len(sys.argv) > 1 else "/var/www/site"
TAG = sys.argv[2] if len(sys.argv) > 2 else (
    '<script defer src="https://stats.example.com/script.js" data-website-id="YOUR_ID"></script>'
)

MARKER = "stats.example.com"  # подстрока, по которой видно, что уже вставлено

inserted = skipped = 0
for path in glob.glob(BASE + "/**/*.html", recursive=True):
    with open(path, encoding="utf-8") as f:
        content = f.read()

    if MARKER in content:
        skipped += 1
        continue

    if "</head>" in content:
        content = content.replace("</head>", TAG + "\n</head>", 1)
    elif "<head>" in content:
        content = content.replace("<head>", "<head>\n" + TAG, 1)
    else:
        skipped += 1
        continue

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    inserted += 1

print(f"inserted: {inserted}, skipped: {skipped}")
