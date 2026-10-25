#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
After a merge: wait for the GitHub Pages deploy, then check the live site.

    python3 verify_live.py URL [URL ...] [--marker TEXT] [--wait 600] [--base https://wealthprimer.in]

URLs may be paths (/2026/10/26/slug/) or full URLs. For each: HTTP 200, one <title>,
one <h1>, a canonical on the site, not noindex (unless --allow-noindex), and optionally
--marker text present. Polls every 20 s until all pass or --wait seconds elapse.
Note: from the cloud sandbox the egress proxy can slow or fail requests; a failure here is
a lead to re-check, not proof the site is broken.
"""
import argparse
import re
import sys
import time

import requests


def check(url, marker, allow_noindex):
    problems = []
    try:
        r = requests.get(url, timeout=30, headers={"Cache-Control": "no-cache"})
    except Exception as e:  # noqa: BLE001
        return [f"request failed: {e}"]
    if r.status_code != 200:
        return [f"HTTP {r.status_code}"]
    h = r.text
    if len(re.findall(r"<title>", h)) != 1:
        problems.append("title count != 1")
    if len(re.findall(r"<h1[ >]", h)) != 1:
        problems.append("h1 count != 1")
    m = re.search(r'<link rel="canonical" href="([^"]+)"', h)
    if not m:
        problems.append("no canonical")
    if not allow_noindex and re.search(r'name="robots"[^>]*noindex', h):
        problems.append("noindex")
    if marker and marker not in h:
        problems.append(f"marker not found: {marker!r}")
    return problems


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("urls", nargs="+")
    ap.add_argument("--marker")
    ap.add_argument("--wait", type=int, default=600)
    ap.add_argument("--base", default="https://wealthprimer.in")
    ap.add_argument("--allow-noindex", action="store_true")
    a = ap.parse_args()
    urls = [u if u.startswith("http") else a.base.rstrip("/") + "/" + u.lstrip("/") for u in a.urls]
    deadline = time.time() + a.wait
    while True:
        res = {u: check(u, a.marker, a.allow_noindex) for u in urls}
        bad = {u: p for u, p in res.items() if p}
        if not bad:
            print("LIVE OK:", *urls, sep="\n  ")
            return 0
        if time.time() > deadline:
            for u, p in bad.items():
                print("NOT OK", u, "->", "; ".join(p))
            return 1
        print(f"waiting ({len(bad)} of {len(urls)} not ready)...", flush=True)
        time.sleep(20)


if __name__ == "__main__":
    sys.exit(main())
