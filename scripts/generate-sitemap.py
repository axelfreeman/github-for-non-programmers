#!/usr/bin/env python3
"""Генерирует sitemap.xml из списка страниц (для статического сайта).

Страницы задаются списком относительных путей. Формат вывода — валидный XML sitemap.
Полезно держать отдельно от CMS: любая новая страница — просто строка в списке.
"""
import datetime

BASE = "https://example.com"  # ← свой домен

# относительные пути ('' = главная). Для сабдиректорий — с хвостовым слэшем.
PAGES = [
    ("", "1.0"),
    ("about/", "0.8"),
    ("pricing/", "0.9"),
    ("blog/first-post/", "0.7"),
]

today = datetime.date.today().isoformat()
urls = "".join(
    f"  <url><loc>{BASE}/{p}</loc><lastmod>{today}</lastmod>"
    f"<changefreq>weekly</changefreq><priority>{pr}</priority></url>\n"
    for p, pr in PAGES
)
sitemap = (
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + urls
    + "</urlset>\n"
)

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(sitemap)

print(f"sitemap.xml: {len(PAGES)} URLs")
