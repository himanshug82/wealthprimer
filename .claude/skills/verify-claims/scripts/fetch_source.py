#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fetch a primary source (PDF or web page) as searchable text, and search it with paragraph and page
numbers, so a claim can be checked against the actual document instead of memory.

    python3 fetch_source.py get  <URL> [--name NAME]      download + convert; prints the cache name
    python3 fetch_source.py find <NAME> <REGEX> [-C 4]    matches with page and nearest clause number
    python3 fetch_source.py show <NAME> <LINE> [-C 25]    print a stretch of text around a line
    python3 fetch_source.py list                          what is cached

Cache: $WP_SOURCES (default ~/.cache/wealthprimer-sources). Nothing here is committed to the repo.
PDFs go through `pdftotext -layout` (poppler); pages are counted from form feeds. HTML is stripped
to text. Uses the environment's proxy settings; retries on the TLS/connection resets sebi.gov.in
sometimes gives. Standard library + requests.
"""
import argparse
import html
import os
import re
import subprocess
import sys
import time

CACHE = os.environ.get("WP_SOURCES", os.path.expanduser("~/.cache/wealthprimer-sources"))
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36"
CLAUSE = re.compile(r"^\s{0,12}((?:\d{1,2}\.){1,4}\d{0,2}|\d{1,2}\.\s|\([a-z]\)|\([ivx]+\))")


def slugify(url):
    s = re.sub(r"^https?://(www\.)?", "", url).split("?")[0]
    return re.sub(r"[^A-Za-z0-9]+", "-", s).strip("-").lower()[-60:]


def fetch(url):
    import requests
    last = None
    for attempt in range(4):
        try:
            r = requests.get(url, headers={"User-Agent": UA}, timeout=120)
            r.raise_for_status()
            return r
        except Exception as e:  # noqa: BLE001
            last = e
            time.sleep(2 ** attempt)
    raise SystemExit(f"could not fetch {url}: {last}\n(If this host is blocked or returns 403, record that in TODO.md and do NOT state the rule from memory.)")


def cmd_get(a):
    os.makedirs(CACHE, exist_ok=True)
    name = a.name or slugify(a.url)
    r = fetch(a.url)
    raw = os.path.join(CACHE, name + (".pdf" if "pdf" in r.headers.get("content-type", "").lower() or a.url.lower().endswith(".pdf") else ".html"))
    open(raw, "wb").write(r.content)
    txt = os.path.join(CACHE, name + ".txt")
    if raw.endswith(".pdf"):
        subprocess.run(["pdftotext", "-layout", raw, txt], check=True)
    else:
        t = r.text
        t = re.sub(r"(?is)<(script|style|nav|header|footer)[^>]*>.*?</\1>", " ", t)
        t = re.sub(r"(?i)<br\s*/?>|</(p|div|li|tr|h\d)>", "\n", t)
        t = html.unescape(re.sub(r"<[^>]+>", " ", t))
        t = re.sub(r"[ \t]+", " ", t)
        t = re.sub(r"\n\s*\n+", "\n\n", t)
        open(txt, "w", encoding="utf-8").write(t)
    n = sum(1 for _ in open(txt, encoding="utf-8", errors="replace"))
    open(os.path.join(CACHE, name + ".url"), "w").write(a.url + "\n")
    print(f"cached as '{name}': {n} lines, {os.path.getsize(raw)//1024} KB  ({a.url})")


def load(name):
    p = os.path.join(CACHE, name + ".txt")
    if not os.path.exists(p):
        raise SystemExit(f"'{name}' is not cached; run `get` first (see `list`).")
    return open(p, encoding="utf-8", errors="replace").read().split("\n")


def page_of(lines, i):
    return sum(l.count("\f") for l in lines[: i + 1]) + 1


def cmd_find(a):
    lines = load(a.name)
    rx = re.compile(a.regex, re.I)
    hits = 0
    for i, l in enumerate(lines):
        if rx.search(l):
            hits += 1
            clause = next((lines[j].strip()[:60] for j in range(i, max(i - 80, -1), -1) if CLAUSE.match(lines[j]) and lines[j].strip()), "")
            print(f"--- line {i+1} | page {page_of(lines, i)} | nearest clause: {clause}")
            for j in range(max(0, i - a.C), min(len(lines), i + a.C + 1)):
                print(("> " if j == i else "  ") + lines[j].rstrip().replace("\f", "")[:170])
            if hits >= a.max:
                print(f"... stopped after {a.max} matches (use --max)")
                break
    if not hits:
        print("no match: try a shorter or alternative wording before concluding the document doesn't say it")


def cmd_show(a):
    lines = load(a.name)
    i = a.line - 1
    for j in range(max(0, i - a.C), min(len(lines), i + a.C + 1)):
        print(f"{j+1:6} {lines[j].rstrip().replace(chr(12), '')[:170]}")


def cmd_list(_):
    if not os.path.isdir(CACHE):
        print("(empty)")
        return
    for f in sorted(os.listdir(CACHE)):
        if f.endswith(".txt"):
            u = os.path.join(CACHE, f[:-4] + ".url")
            print(f[:-4].ljust(62), open(u).read().strip() if os.path.exists(u) else "")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    g = sub.add_parser("get"); g.add_argument("url"); g.add_argument("--name"); g.set_defaults(f=cmd_get)
    f = sub.add_parser("find"); f.add_argument("name"); f.add_argument("regex"); f.add_argument("-C", type=int, default=4); f.add_argument("--max", type=int, default=12); f.set_defaults(f=cmd_find)
    s = sub.add_parser("show"); s.add_argument("name"); s.add_argument("line", type=int); s.add_argument("-C", type=int, default=25); s.set_defaults(f=cmd_show)
    l = sub.add_parser("list"); l.set_defaults(f=cmd_list)
    a = ap.parse_args()
    a.f(a)


if __name__ == "__main__":
    sys.exit(main())
