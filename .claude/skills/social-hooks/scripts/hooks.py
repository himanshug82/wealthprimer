#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Draft the tweet hook for a post: the Takeaway's first sentence + link, with compliance flags.

    python3 hooks.py _posts/<file> [...]

Prints, per post: the Takeaway first sentence, its length (must be <= 280 on its own), the public
URL, total length counting the link as 23 characters, and flags from write-post's lint word lists
(trade calls, valuation verdicts, hype). Twitter here is distribution, not a second content
stream: one hook + link, never a thread repeating the post. Posts dated in the future are marked
NOT LIVE YET. Output is a draft for the owner to post; nothing is sent anywhere.
"""
import datetime as dt
import importlib.util
import os
import re
import sys

BASE = "https://wealthprimer.in"
lint_path = os.path.join(os.path.dirname(__file__), "..", "..", "write-post", "scripts", "lint_post.py")
spec = importlib.util.spec_from_file_location("lint_post", lint_path)
lint = importlib.util.module_from_spec(spec); spec.loader.exec_module(lint)


def first_sentence(par):
    par = re.sub(r"\*\*Takeaway:\*\*\s*", "", par).strip()
    par = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", par)
    m = re.match(r"(.+?[.!?])(\s|$)", par, re.S)
    return (m.group(1) if m else par).replace("\n", " ").strip()


def main():
    for f in sys.argv[1:]:
        name = os.path.basename(f); t = open(f, encoding="utf-8").read()
        m = re.search(r"^\*\*Takeaway:\*\*.*?(?=\n\s*\n|\Z)", t, re.M | re.S)
        if not m: print(f"{name}: no Takeaway paragraph"); continue
        s = first_sentence(m.group(0))
        d = dt.date.fromisoformat(name[:10]); slug = name[11:].rsplit(".", 1)[0]
        url = f"{BASE}/{d:%Y/%m/%d}/{slug}/"
        flags = []
        for label in ("CALLS", "VERDICT", "HYPE"):
            pat = getattr(lint, label, None)
            if pat and re.search(pat, s, re.I): flags.append(label)
        total = len(s) + 1 + 23
        print(f"\n{name}" + ("   [NOT LIVE YET]" if d > dt.date.today() else ""))
        print(f"  hook ({len(s)} chars{' - OVER 280' if len(s) > 280 else ''}): {s}")
        print(f"  tweet ({total} incl. link): {s} {url}")
        print(f"  flags: {', '.join(flags) or 'none'}")


if __name__ == "__main__":
    main()
