#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Which datasets are stale or too fresh, and which scripts/posts depend on them.

    python3 data_status.py [--for-date 2026-11-20]     # default: today

For each CSV in assets/data/: first/last date, and the derive/make scripts that read it.
Cutoff = for-date minus 3 calendar months (house rule: worked-example data must be at least 3
months old at publication). A dataset ending AFTER the cutoff is TOO FRESH for a post published
on for-date (fine to hold, but don't let a post use the tail). Then lists the next scheduled posts
(front matter `series`), so you can see what refresh could matter. Run from the repo root.
"""
import calendar
import csv
import datetime as dt
import glob
import os
import re
import sys


def minus_months(d, n):
    y, m = d.year, d.month - n
    while m < 1: m += 12; y -= 1
    return d.replace(year=y, month=m, day=min(d.day, calendar.monthrange(y, m)[1]))


def main():
    when = dt.date.today()
    if "--for-date" in sys.argv: when = dt.date.fromisoformat(sys.argv[sys.argv.index("--for-date") + 1])
    cutoff = minus_months(when, 3)
    scripts = {p: open(p, encoding="utf-8").read() for p in glob.glob("scripts/*.py")}
    print(f"post date {when}  ->  data must end on or before {cutoff}\n")
    print(f"{'file':46} {'first':10} {'last':10}  status      used by")
    for p in sorted(glob.glob("assets/data/*.csv")):
        rows = list(csv.reader(open(p)))
        ds = [r[0] for r in rows[1:] if r and re.match(r"\d{4}-\d{2}-\d{2}$", r[0])]
        if not ds: print(f"{os.path.basename(p):46} (no ISO dates)"); continue
        first, last = min(ds), max(ds)
        st = "TOO FRESH" if dt.date.fromisoformat(last) > cutoff else "ok"
        used = ", ".join(sorted(os.path.basename(s) for s, t in scripts.items() if os.path.basename(p) in t)) or "-"
        print(f"{os.path.basename(p):46} {first} {last}  {st:10}  {used}")
    print("\nUpcoming posts:")
    for f in sorted(glob.glob("_posts/*.markdown")):
        d = os.path.basename(f)[:10]
        if d >= str(dt.date.today()) and d <= str(when + dt.timedelta(days=14)):
            m = re.search(r"^series:\s*(\S+)", open(f, encoding="utf-8").read(), re.M)
            print(" ", os.path.basename(f), f"[{m.group(1) if m else '?'}]")
    print("\nTo refresh: fetch_nifty_tri.py / fetch_nav.py, then re-run the derive script listed above "
          "(never hand-edit _data/*.yml), then check_posts.py and re-read the numbers in the post.")


if __name__ == "__main__":
    main()
