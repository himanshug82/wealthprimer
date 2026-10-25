#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Add width/height to every chart image in _posts/ so the browser reserves the space before the
SVG loads (no layout shift, a Core Web Vitals signal). Idempotent: images that already carry a
kramdown attribute list `{: ...}` are left alone.

    python3 scripts/add_img_dims.py            # rewrite posts in place
    python3 scripts/add_img_dims.py --check    # exit 1 if any chart image still lacks dimensions

Dimensions come from each SVG's viewBox (CSS keeps `height: auto`, so images still scale down).
Run it after adding a post with a new chart. Pure standard library.
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = re.compile(r"(!\[[^\]]*\]\(\{\{\s*'/assets/charts/([A-Za-z0-9_\-\.]+)'\s*\|\s*relative_url\s*\}\}\))(?!\{:)")


def dims(name):
    path = os.path.join(ROOT, "assets", "charts", name)
    head = open(path, encoding="utf-8").read(4000)
    m = re.search(r'viewBox="\s*[-\d.]+\s+[-\d.]+\s+([\d.]+)\s+([\d.]+)\s*"', head)
    if not m:
        return None
    return round(float(m.group(1))), round(float(m.group(2)))


def main(check):
    missing = changed = 0
    for path in sorted(glob.glob(os.path.join(ROOT, "_posts", "*.markdown"))):
        text = open(path, encoding="utf-8").read()

        def repl(m):
            nonlocal changed
            d = dims(m.group(2))
            if not d:
                return m.group(0)
            changed += 1
            return f'{m.group(1)}{{: width="{d[0]}" height="{d[1]}"}}'

        new = IMG.sub(repl, text)
        if check:
            missing += len(IMG.findall(text))
        elif new != text:
            open(path, "w", encoding="utf-8").write(new)
    if check:
        print(f"{missing} chart image(s) without width/height")
        return 1 if missing else 0
    print(f"added dimensions to {changed} chart image(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main("--check" in sys.argv))
