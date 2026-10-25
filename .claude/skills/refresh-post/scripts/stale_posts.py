#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rank published posts by how likely they are to be out of date.

    python3 stale_posts.py [--days 120] [--top 30]

Signals: age since `last_modified_at` (or date); markers of changeable facts in the body
(SEBI/RBI circular, Master Circular, Tax Year / FY 2026-27, section numbers, rates "per cent",
"as of"); title carrying a year; series tax/mutual-funds weigh more. Scheduled (future) posts
are skipped. This ranks leads for `refresh-post`; it does not decide anything.
"""
import datetime as dt
import glob
import os
import re
import sys

MARK = {
    r"circular|master circular|notification": 3,
    r"tax year|FY ?20\d\d|assessment year": 2,
    r"\bsection \d+[A-Z]{0,3}\b": 2,
    r"\b(STT|TDS|cess|surcharge|LTCG|STCG)\b": 1,
    r"as of |as on ": 1,
    r"20(2[5-9])": 1,
}
W = {"tax": 2.0, "mutual-funds": 1.3}


def main():
    days = int(sys.argv[sys.argv.index("--days") + 1]) if "--days" in sys.argv else 120
    top = int(sys.argv[sys.argv.index("--top") + 1]) if "--top" in sys.argv else 30
    today = dt.date.today(); out = []
    for f in glob.glob("_posts/*.markdown"):
        name = os.path.basename(f); d = dt.date.fromisoformat(name[:10])
        if d > today: continue
        t = open(f, encoding="utf-8").read()
        fm = t.split("---")[1] if t.startswith("---") else ""
        lm = re.search(r"^last_modified_at:\s*(\d{4}-\d{2}-\d{2})", fm, re.M)
        last = dt.date.fromisoformat(lm.group(1)) if lm else d
        age = (today - last).days
        if age < days: continue
        score = sum(w * min(3, len(re.findall(p, t, re.I))) for p, w in MARK.items())
        ser = re.search(r"^series:\s*(\S+)", fm, re.M)
        score *= W.get(ser.group(1) if ser else "", 1.0)
        title = re.search(r'^title:\s*"?(.*?)"?\s*$', fm, re.M)
        if title and re.search(r"20\d\d", title.group(1)): score += 5
        if score > 0: out.append((score, age, name, ser.group(1) if ser else "?"))
    out.sort(reverse=True)
    print(f"{len(out)} posts older than {days} days with changeable-fact markers (top {top}):")
    print(f"{'score':>6} {'age':>5}  {'series':14} post")
    for s, a, n, se in out[:top]: print(f"{s:6.1f} {a:5d}  {se:14} {n}")


if __name__ == "__main__":
    main()
