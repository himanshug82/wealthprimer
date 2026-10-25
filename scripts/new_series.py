#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Scaffold a new series: appends its entry to _data/series.yml and creates series/<slug>.markdown.

    python3 scripts/new_series.py SLUG "Title" --description "…" --about "…" [--planned N] [--unnumbered]

SLUG: lowercase letters, digits, hyphens; becomes the URL /series/<slug>/ and the stable GA4 key, so it
can never be renamed later. Everything else (homepage card, /series/ index, footer, "Part N of M",
prev/next, breadcrumbs, analytics dimensions) reads series.yml. A hub is noindexed automatically until
its first post is live, so scaffolding early is safe. Run scripts/check_posts.py afterwards.
Description: 100-170 chars and different from `about` (so /series/ isn't a near-duplicate of the homepage).
"""
import argparse
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def q(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug"); ap.add_argument("title")
    ap.add_argument("--description", required=True); ap.add_argument("--about", required=True)
    ap.add_argument("--planned", type=int, default=0); ap.add_argument("--unnumbered", action="store_true")
    a = ap.parse_args()
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", a.slug): sys.exit("slug: lowercase letters, digits, hyphens")
    yml = os.path.join(ROOT, "_data", "series.yml"); hub = os.path.join(ROOT, "series", a.slug + ".markdown")
    txt = open(yml, encoding="utf-8").read()
    if re.search(rf"^- slug:\s*{re.escape(a.slug)}\s*$", txt, re.M) or os.path.exists(hub): sys.exit("series already exists")
    if not 100 <= len(a.description) <= 170: print(f"warning: description is {len(a.description)} chars (aim 100-170)")
    if a.description.strip() == a.about.strip(): sys.exit("description and about must differ")
    entry = f"- slug: {a.slug}\n  title: {q(a.title)}\n  description: {q(a.description)}\n  about: {q(a.about)}\n"
    if a.planned: entry += f"  planned: {a.planned}\n"
    if a.unnumbered: entry += "  numbered: false\n"
    open(yml, "w", encoding="utf-8").write(txt.rstrip("\n") + "\n" + entry)
    open(hub, "w", encoding="utf-8").write(
        f"---\nlayout: series\ntitle: {q(a.title)}\npermalink: /series/{a.slug}/\nseries_slug: {a.slug}\n"
        f"description: {q(a.description)}\n---\n")
    print("added", a.slug, "-> _data/series.yml and", os.path.relpath(hub, ROOT))
    print("next: add posts with series:", a.slug, "; update TODO.md roadmap; run scripts/check_posts.py")


if __name__ == "__main__":
    main()
