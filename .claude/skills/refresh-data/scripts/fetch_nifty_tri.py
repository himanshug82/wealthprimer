#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Download Nifty total-return-index history from NSE Indices (niftyindices.com) into a CSV.

    python3 fetch_nifty_tri.py --start 2006-01-01 --end 2026-03-31 --out assets/data/nifty50-tri.csv
    python3 fetch_nifty_tri.py --extend assets/data/nifty50-tri.csv --end 2026-07-31   # append only new days

The endpoint returns at most about a year per request, so this walks in 300-day chunks.
Output columns: date, nifty50_tri_close (the TotalReturnsIndex value; price-return TRI, not NTR).
Never request dates inside the 3-month lag for a worked example (see data_status.py).
"""
import argparse
import csv
import datetime as dt
import json
import time

import requests

URL = "https://niftyindices.com/BackPage/getTotalReturnIndexString"
HDR = {"Content-Type": "application/json; charset=UTF-8", "User-Agent": "Mozilla/5.0",
       "X-Requested-With": "XMLHttpRequest", "Referer": "https://niftyindices.com/reports/historical-data"}


def chunk(name, a, b):
    f = lambda d: d.strftime("%d-%b-%Y")
    cinfo = json.dumps({"name": name, "startDate": f(a), "endDate": f(b), "indexName": name}).replace('"', "'")
    for attempt in range(4):
        try:
            r = requests.post(URL, headers=HDR, data=json.dumps({"cinfo": cinfo}), timeout=60)
            r.raise_for_status()
            return r.json()
        except Exception:  # noqa: BLE001
            time.sleep(2 ** (attempt + 1))
    raise SystemExit(f"failed: {a}..{b}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--index", default="NIFTY 50")
    ap.add_argument("--start"); ap.add_argument("--end", required=True)
    ap.add_argument("--out"); ap.add_argument("--extend")
    a = ap.parse_args()
    end = dt.date.fromisoformat(a.end)
    rows = {}
    path = a.extend or a.out
    if a.extend:
        for r in csv.DictReader(open(a.extend)): rows[r["date"]] = r["nifty50_tri_close"]
        start = dt.date.fromisoformat(max(rows)) + dt.timedelta(days=1)
    else:
        start = dt.date.fromisoformat(a.start)
    cur = start
    while cur <= end:
        nxt = min(cur + dt.timedelta(days=299), end)
        for rec in chunk(a.index, cur, nxt):
            d = dt.datetime.strptime(rec["Date"], "%d %b %Y").date().isoformat()
            rows[d] = rec["TotalReturnsIndex"]
        print(f"{cur}..{nxt}: {len(rows)} rows", flush=True)
        cur = nxt + dt.timedelta(days=1); time.sleep(0.5)
    with open(path, "w", newline="") as fh:
        w = csv.writer(fh); w.writerow(["date", "nifty50_tri_close"])
        for d in sorted(rows): w.writerow([d, rows[d]])
    print("wrote", path, len(rows), "rows, last", max(rows))


if __name__ == "__main__":
    main()
