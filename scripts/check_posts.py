#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pre-publish checks for every post in _posts/ (and, with --drafts, _drafts/).

WHY: the site publishes on a daily cron with `future: false`, so a post is
built for the first time on its own date, with no human watching. Two classes
of mistake only surface then:

  1. A {% post_url %} that points at a post whose date is LATER than the
     linking post's. That isn't a 404 — it fails the ENTIRE Jekyll build
     ("Could not find post ... in tag 'post_url'"), because unpublished posts
     are not in site.posts. See the build rule in TODO.md.
  2. Front matter that the layouts/SEO depend on: a `description` of the
     length Google shows, an `image` that exists in assets/og/, a `series`
     slug that exists in _data/series.yml, a valid date.

Also warns (not fails) on: missing `term:` (glossary), two posts on one date,
a `{{ site.data.X }}` reference to a data file that doesn't exist, and any
Liquid variable of the form `{{ foo.bar }}` whose root `foo` was never
assigned in the post (catches typos in {% assign %} names).

    python3 scripts/check_posts.py            # exit 1 on any error
    python3 scripts/check_posts.py --drafts   # include _drafts/ too

Pure standard library so it runs on the system python3 and in CI.
"""
import argparse
import glob
import os
import re
import sys
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POST_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})-(.+)\.(markdown|md)$")
POST_URL_RE = re.compile(r"{%-?\s*post_url\s+([^\s%]+)\s*-?%}")
ASSIGN_RE = re.compile(r"{%-?\s*assign\s+([A-Za-z_][A-Za-z0-9_]*)\s*=")
FOR_RE = re.compile(r"{%-?\s*for\s+([A-Za-z_][A-Za-z0-9_]*)\s+in\s+")
CAPTURE_RE = re.compile(r"{%-?\s*capture\s+([A-Za-z_][A-Za-z0-9_]*)")
VAR_RE = re.compile(r"{{-?\s*([A-Za-z_][A-Za-z0-9_]*)[\.\[\s|}]")
DATA_RE = re.compile(r"site\.data\.([A-Za-z_][A-Za-z0-9_]*)")
BUILTIN = {"site", "page", "content", "include", "forloop", "layout", "paginator", "jekyll"}


def front_matter(text):
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end < 0:
        return {}, text
    fm = {}
    for line in text[3:end].splitlines():
        m = re.match(r"^([A-Za-z_]+):\s*(.*)$", line)
        if m:
            v = m.group(2).strip()
            if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
                v = v[1:-1]
            fm[m.group(1)] = v
    return fm, text[end + 4:]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--drafts", action="store_true")
    args = ap.parse_args()

    files = sorted(glob.glob(os.path.join(ROOT, "_posts", "*.markdown")) + glob.glob(os.path.join(ROOT, "_posts", "*.md")))
    if args.drafts:
        files += sorted(glob.glob(os.path.join(ROOT, "_drafts", "*.markdown")))

    series_slugs = set(re.findall(r"^- slug:\s*(\S+)", open(os.path.join(ROOT, "_data", "series.yml"), encoding="utf-8").read(), re.M))
    data_files = {os.path.splitext(os.path.basename(p))[0] for p in glob.glob(os.path.join(ROOT, "_data", "*.yml"))}

    posts = {}
    for path in files:
        name = os.path.basename(path)
        m = POST_RE.match(name)
        if not m:
            if "_posts" in path:
                print(f"ERROR {name}: filename is not YYYY-MM-DD-slug.markdown")
            continue
        posts[m.group(1) + "-" + m.group(2)] = (path, date.fromisoformat(m.group(1)))

    errors = warnings = 0
    by_date = {}
    for key, (path, d) in posts.items():
        name = os.path.basename(path)
        text = open(path, encoding="utf-8").read()
        fm, body = front_matter(text)
        by_date.setdefault(d, []).append(name)

        # --- post_url direction -------------------------------------------
        for target in POST_URL_RE.findall(body):
            if target not in posts:
                print(f"ERROR {name}: post_url target '{target}' does not exist")
                errors += 1
            elif posts[target][1] > d:
                print(f"ERROR {name}: post_url '{target}' is dated {posts[target][1]} — AFTER this post ({d}); the build breaks on {d}")
                errors += 1

        # --- front matter -------------------------------------------------
        for k in ("title", "description", "date", "layout"):
            if k not in fm:
                print(f"ERROR {name}: front matter missing '{k}'")
                errors += 1
        desc = fm.get("description", "")
        if desc and not (110 <= len(desc) <= 170):
            print(f"WARN  {name}: description is {len(desc)} chars (aim 140–160)")
            warnings += 1
        if fm.get("date", "")[:10] != d.isoformat():
            print(f"ERROR {name}: front matter date '{fm.get('date')}' disagrees with filename date {d}")
            errors += 1
        if "_posts" in path:
            if fm.get("series") not in series_slugs:
                print(f"ERROR {name}: series '{fm.get('series')}' is not in _data/series.yml")
                errors += 1
            if "term" not in fm:
                print(f"WARN  {name}: no term: (won't appear in /glossary/)")
                warnings += 1
        img = fm.get("image", "")
        if img and not os.path.exists(os.path.join(ROOT, img.lstrip("/"))):
            print(f"WARN  {name}: image '{img}' does not exist yet (run scripts/make_og_cards.py)")
            warnings += 1

        # --- data references and undefined Liquid roots -------------------
        for dref in set(DATA_RE.findall(body)):
            if dref not in data_files:
                print(f"ERROR {name}: site.data.{dref} — no _data/{dref}.yml")
                errors += 1
        defined = set(ASSIGN_RE.findall(body)) | set(FOR_RE.findall(body)) | set(CAPTURE_RE.findall(body)) | BUILTIN
        for root_var in set(VAR_RE.findall(body)):
            if root_var not in defined:
                print(f"ERROR {name}: Liquid variable '{root_var}' is used but never assigned")
                errors += 1

        # --- chart references ---------------------------------------------
        for chart in re.findall(r"/assets/charts/([A-Za-z0-9_\-\.]+)", body):
            if not os.path.exists(os.path.join(ROOT, "assets", "charts", chart)):
                print(f"ERROR {name}: chart assets/charts/{chart} does not exist")
                errors += 1

    for d, names in sorted(by_date.items()):
        if len(names) > 1:
            print(f"WARN  {d}: {len(names)} posts share this date: {', '.join(names)}")
            warnings += 1

    print(f"\n{len(posts)} posts checked: {errors} error(s), {warnings} warning(s)")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
