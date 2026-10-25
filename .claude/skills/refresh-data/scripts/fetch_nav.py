#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Download a mutual-fund scheme's NAV history from mfapi.in into a CSV (oldest first).

    python3 fetch_nav.py --search "UTI Liquid"                       # find scheme codes
    python3 fetch_nav.py --code 102004 --out assets/data/x.csv [--until 2026-03-31] [--column nav_regular_growth]

mfapi.in is a community mirror of AMFI data, not a regulator: fine for data, never a source for rules.
Pick the exact plan/option (Regular vs Direct, Growth vs IDCW) and say which in the post.
Dates are as AMFI publishes them (business days; some history is forward-filled by AMFI).
"""
import argparse
import csv
import datetime as dt

import requests


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--search"); ap.add_argument("--code", type=int)
    ap.add_argument("--out"); ap.add_argument("--until")
    ap.add_argument("--column", default="nav_regular_growth")
    a = ap.parse_args()
    if a.search:
        for s in requests.get("https://api.mfapi.in/mf/search", params={"q": a.search}, timeout=60).json()[:40]:
            print(s["schemeCode"], s["schemeName"])
        return
    if not (a.code and a.out): ap.error("--code and --out required")
    j = requests.get(f"https://api.mfapi.in/mf/{a.code}", timeout=60).json()
    print("scheme:", j["meta"]["scheme_name"], "|", j["meta"].get("scheme_category"))
    until = dt.date.fromisoformat(a.until) if a.until else None
    rows = []
    for r in j["data"]:
        d = dt.datetime.strptime(r["date"], "%d-%m-%Y").date()
        if until and d > until: continue
        rows.append((d.isoformat(), r["nav"]))
    rows.sort()
    with open(a.out, "w", newline="") as fh:
        w = csv.writer(fh); w.writerow(["date", a.column]); w.writerows(rows)
    print("wrote", a.out, len(rows), "rows,", rows[0][0], "to", rows[-1][0])


if __name__ == "__main__":
    main()
