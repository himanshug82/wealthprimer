#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advisory lint for a Wealth Primer post: the CLAUDE.md rules a script can see.

    python3 .claude/skills/write-post/scripts/lint_post.py _posts/<file> [...]

Exit 1 only on FAIL lines (compliance words, missing Takeaway, bad lag).
WARN/INFO lines are prompts for a human read, not verdicts: a hit is a place to
look, a clean run is NOT proof the post is compliant or accurate.
check_posts.py (structure, post_url direction, data refs) is separate and still required.
"""
import os
import re
import sys
from datetime import date

MONTHS = {m: i for i, m in enumerate(
    ["january", "february", "march", "april", "may", "june", "july",
     "august", "september", "october", "november", "december"], 1)}
HYPE = r"guarantee[ds]?|sure[- ]?shot|multi-?baggers?|can'?t lose|easy money|get rich|double your money"
CALLS = (r"\b(buy|sell|accumulate|avoid|exit)\s+(it|this|the stock|the share|[A-Z][a-z]+\b)|target price|price target|\bmust[- ]buy|\bstrong buy|"
         r"\bbuy on dips?|add on dips?|worth (buying|owning)|you should (buy|sell|hold|invest)|investors? (may|could) consider|good entry|time to (enter|buy|sell)|"
         r"book profits|stay invested|\bhold (it|this|the stock)")
VERDICT = (r"\b(overvalued|undervalued|cheap(ly)?|expensive|fairly valued|mispric\w*|bargain|attractive(ly)? valued|"
           r"rich valuation|moat|compounder|impressive|excellent|healthy|robust|strong balance sheet|honest of|"
           r"solid|sound|stable|reasonable(ly)? priced|prudent|disciplined|conservative(ly)?|well-run|best-in-class|durable|"
           r"valued (below|above|at a premium|at a discount)|premium to peers|discount to peers|not (cheap|irrational|a mispricing)|"
           r"inexpensive|cheaper|safe (bet|stock|choice)|outperform\w*|underperform\w*)\b")
VALUATION = r"\b(DCF|WACC|discount rate|intrinsic value|fair value|justified (P/B|P/E|multiple))\b"
SERIES_COPY = r"\b(the next (two|three|four|five|six|seven|eight|nine|ten|\d+) posts|final post|last post in this series|closes? the series|fifty-nine posts)\b"
STOP_ACR = {"I", "A", "II", "III", "IV", "AM", "PM", "OK", "CSV", "SVG", "PNG", "ISO", "DB"}


def split(text):
    m = re.match(r"^---\n(.*?)\n---\n?", text, re.S)
    if not m:
        return {}, text
    fm = {}
    for line in m.group(1).splitlines():
        k = re.match(r"^([A-Za-z_]+):\s*(.*)$", line)
        if k:
            v = k.group(2).strip()
            fm[k.group(1)] = v[1:-1] if len(v) > 1 and v[0] == v[-1] and v[0] in "\"'" else v
    return fm, text[m.end():]


def prose_lines(body):
    """(lineno, text) for lines that are prose: not code, table, Liquid-only, HTML or heading."""
    out, fenced = [], False
    for n, line in enumerate(body.splitlines(), 1):
        if line.strip().startswith("```"):
            fenced = not fenced
            continue
        s = line.strip()
        if fenced or not s or s.startswith(("|", "{%", "<", "#", "![", "---")):
            continue
        out.append((n, line))
    return out


def scan_lines(body):
    """Every non-code line, including table rows and <details>/<summary> text, for compliance words."""
    out, fenced = [], False
    for n, line in enumerate(body.splitlines(), 1):
        if line.strip().startswith("```"):
            fenced = not fenced
            continue
        if not fenced and line.strip():
            out.append((n, re.sub(r"\{%.*?%\}|\{\{.*?\}\}|<[^>]+>", " ", line)))
    return out


def lint(path):
    name = os.path.basename(path)
    text = open(path, encoding="utf-8").read()
    fm, body = split(text)
    res = []
    add = lambda lvl, msg: res.append(f"{lvl:4} {name}: {msg}")

    dm = re.match(r"(\d{4})-(\d{2})-(\d{2})", name)
    pub = date(*map(int, dm.groups())) if dm else None

    title, desc = fm.get("title", ""), fm.get("description", "")
    if len(title) > 60:
        add("WARN", f"title is {len(title)} chars (aim ≤ 60 so search results don't truncate it)")
    words = re.findall(r"[A-Za-z][A-Za-z'’]+", title)[1:]
    if sum(w[0].isupper() and not w.isupper() for w in words) >= 3:
        add("WARN", "title looks Title Case (house style is sentence case; proper nouns are fine)")
    if not 140 <= len(desc) <= 160:
        add("WARN", f"description is {len(desc)} chars (aim 140–160)")
    if re.search(HYPE, title + " " + desc, re.I):
        add("FAIL", "hype word in title/description")
    for rx, lbl in ((CALLS, "trade-call phrasing"), (VERDICT, "verdict word")):
        m = re.search(rx, title + " " + desc, re.I if rx != CALLS else 0)
        if m:
            add("WARN", f"{lbl} in title/description: “{m.group(0)}”")
    if not fm.get("image"):
        add("WARN", "no image: front matter (run scripts/make_og_cards.py)")
    if pub and not re.search(r"\s(0\d|1[0-9]):\d\d:\d\d\s\+0530|\s09:00:00\s\+0530", fm.get("date", "")):
        add("WARN", "date has no '+0530' time; keep the time ≤ 09:00:00 +0530")
    elif pub and fm.get("date", "")[11:19] > "09:00:00":
        add("FAIL", "post time is after 09:00 +0530 and will miss that day's build")

    off = len(text.splitlines()) - len(body.splitlines())
    plines = prose_lines(body)
    hard_rs = []
    ptext = "\n".join(t for _, t in plines)

    for n, t in scan_lines(body):
        for rx, lvl, label in ((HYPE, "WARN", "hype word (OK only if quoted/negated, e.g. “no guarantee”)"), (CALLS, "WARN", "possible trade call (OK only if quoted or negated)"),
                               (VERDICT, "WARN", "verdict-style word (fine only for a fictional/generic company or a mechanical statement)")):
            m = re.search(rx, t, re.I if rx != CALLS else 0)
            if m:
                add(lvl, f"line {n + off}: {label}: “{m.group(0)}”")
        if re.match(r"^\s*(\d+|\{\{[^}]*\}\})\.\s", t):
            ls = body.splitlines()
            i = n - 2
            while i >= 0 and ls[i].strip():
                i -= 1
            block_first = ls[i + 1].strip() if i + 1 < n - 1 else ""
            if block_first and not re.match(r"^(\d+\.|[-*+])\s|^\{\{[^}]*\}\}\.\s", block_first):
                liquid = t.lstrip().startswith("{{")
                if liquid and "date:" in t.split("}}")[0]:
                    pass  # renders as a date ("20 March 2026."), not "number. "
                else:
                    add("WARN" if liquid else "FAIL", f"line {n + off}: starts with a {'Liquid value (check it does not render as a bare number)' if liquid else 'number'} + '. ' inside a prose paragraph; kramdown may make it a list item. Reflow the line")
        if re.search(r"(?<=[\s(])-[₹\d]", re.sub(r"`[^`]*`|\{%.*?%\}|\{\{.*?\}\}", "", t)):
            add("WARN", f"line {n + off}: hyphen-minus before a number; use '−' (U+2212)")
        if re.search(r"\b20\d\d-\d\d-\d\d\b", re.sub(r"`[^`]*`|\{%.*?%\}|\{\{.*?\}\}", "", t)):
            add("WARN", f"line {n + off}: ISO date in a sentence; write '3 October 2024'")
        if re.search(r"₹\s?\d", t):
            hard_rs.append(n)

    if hard_rs:
        add("INFO", f"{len(hard_rs)} line(s) with a typed ₹ amount in prose (first: line {hard_rs[0] + off}); real data should come from _data/ via Liquid, scenario numbers are fine")
    fenced = False
    for n, line in enumerate(body.splitlines(), 1):
        if line.strip().startswith("```"):
            fenced = not fenced
        if fenced:
            continue
        h = re.match(r"^(#{2,4})\s+(.*)", line)
        if h:
            for rx, lvl in ((HYPE, "FAIL"), (CALLS, "WARN"), (VERDICT, "WARN")):
                if re.search(rx, h.group(2), re.I if rx != CALLS else 0):
                    add(lvl, f"line {n + off}: compliance word in heading: “{h.group(2)}”")
            ws = re.findall(r"[A-Za-z][A-Za-z'’]+", h.group(2))[1:]
            if sum(w[0].isupper() and not w.isupper() for w in ws) >= 3:
                add("WARN", f"line {n + off}: heading looks Title Case: “{h.group(2)}”")
        if re.match(r"^# ", line):
            add("FAIL", f"line {n + off}: H1 in body; the layout already renders the title as H1")

    # structure
    tk = re.search(r"^\*\*Takeaway:\*\*\s*(.*)$", body, re.M)
    if not tk:
        add("FAIL", "no paragraph starting exactly '**Takeaway:**'")
    else:
        first = re.split(r"(?<![0-9A-Za-z]\.[A-Za-z])(?<!e\.g)(?<!i\.e)(?<!No)(?<=[.!?])\s+(?=[A-Z*_\"“])", tk.group(1))[0]
        if len(first) > 280:
            add("WARN", f"first Takeaway sentence is {len(first)} chars (> 280; raw text, Liquid not rendered)")
    if "Common mistakes" not in body and fm.get("series") != "jargon":
        add("WARN", "no 'Common mistakes' section")
    elif "Common mistakes" not in body:
        add("INFO", "no 'Common mistakes' section (allowed to collapse for short glossary posts)")
    h2 = re.findall(r"^## (.*)", body, re.M)
    if len(h2) < 3:
        add("INFO", "fewer than 3 H2 sections")
    if not any(re.search(r"\?$|^(What|How|Why|When|Which)\b", h) for h in h2):
        add("INFO", "no question-style H2 (consider phrasing one as the reader's search question)")
    if len(re.findall(r"post_url", body)) < 3:
        add("INFO", "fewer than 3 post_url internal links")
    for alt in re.findall(r"!\[([^\]]*)\]\(", body):
        if len(alt.split()) < 4:
            add("WARN", f"image alt text too thin: “{alt}”")
    intro = " ".join(ptext.split()[:100]).lower()
    if "term" in fm:
        t = re.sub(r"\(.*?\)", "", fm["term"]).strip().lower()
        if t and t not in intro:
            add("INFO", f"term “{t}” not in the first 100 words")

    for n, t in scan_lines(body):
        if re.search(VALUATION, t, re.I):
            add("WARN", f"line {n + off}: valuation-model term; allowed only for Desi Bites or a generic/illustrative company, never a real listed one")
        if re.search(SERIES_COPY, t, re.I):
            add("WARN", f"line {n + off}: series-structure copy that goes stale (“{t.strip()[:50]}…”)")
        if re.search(r"\bSME\b|NSE Emerge", t) and "desi" in body.lower():
            add("WARN", f"line {n + off}: Desi Bites is a main-board company, not SME/Emerge")
    if "post-disclaimer" in body or "not investment advice" in body.lower():
        add("WARN", "disclaimer text in body; the layout renders it, don't paste or reword")
    cm = re.search(r"^## Common mistakes\s*$(.*?)(?=^## |\Z)", body, re.M | re.S)
    if cm:
        items = len(re.findall(r"^(?:\d+\.|[-*]|###)\s", cm.group(1), re.M)) or len(re.findall(r"^\*\*[^*]+\*\*", cm.group(1), re.M))
        if items and not 2 <= items <= 4:
            add("INFO", f"Common mistakes has ~{items} items (house style 2–4)")
    if "details" in body and "Explain it like I" not in body:
        add("INFO", "<details> block without the standard “Explain it like I'm 10” summary")
    if tk and body.strip().splitlines()[-1].strip() != tk.group(0).strip() and "Takeaway" not in body.strip().splitlines()[-1]:
        add("INFO", "Takeaway is not the last paragraph of the post")

    # acronyms: heuristic — expansion nearby anywhere in post
    seen, undefined = set(), []
    for a in re.findall(r"\b[A-Z]{2,6}\b", ptext):
        if a in seen or a in STOP_ACR:
            continue
        seen.add(a)
        if not re.search(rf"\({a}\)|\b{a}\s*\(|\*\*{a}\b|\b{a}\s+[—–-]|—\s*{a}\b", ptext):
            undefined.append(a)
    if undefined:
        add("INFO", "acronyms with no visible definition (every post must define each on first use): " + ", ".join(undefined))

    # lag: "as of / to / until <Month YYYY>"
    if pub:
        for mo, yr in re.findall(r"\b(?:as of|as at|up to|until|through|ends)\s+(?:\d{1,2}\s+)?([A-Z][a-z]+)\s+(20\d\d)", ptext):
            mm = MONTHS.get(mo.lower())
            if mm:
                months_old = (pub.year - int(yr)) * 12 + pub.month - mm
                if months_old < 0:
                    add("INFO", f"“{mo} {yr}” is after the post date; fine for a deadline, wrong for data")
                elif months_old < 3:
                    add("FAIL", f"as-of {mo} {yr} is only {months_old} month(s) before the post date; house rule is ≥ 3")
    if not re.search(r"as of|as at|FY\d\d|Tax Year", ptext, re.I) and fm.get("series") != "risk":
        add("INFO", "no visible as-of date or period; worked examples need one")
    return res


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    fails = 0
    for p in argv:
        out = lint(p)
        fails += sum(l.startswith("FAIL") for l in out)
        print("\n".join(out) if out else f"ok   {os.path.basename(p)}: no lint hits")
    print("\nExit 0 means no FAIL lines, NOT that the post is compliant or accurate. Read every WARN/INFO, then do the audit.")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
