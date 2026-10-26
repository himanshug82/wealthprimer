#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advisory lint for a Wealth Primer post: the CLAUDE.md rules a script can see.

    python3 .claude/skills/write-post/scripts/lint_post.py _posts/<file> [...]

FAIL (exit 1): hype word in title/description, forward {% post_url %}, a prose line that
kramdown will turn into a list item, an H1 in the body, no Takeaway paragraph, a post time
after 09:00 +0530, or worked-example data inside the 3-month lag.
WARN / INFO: places to look. Trade-call and verdict words are WARN because teaching text
legitimately quotes and negates them ("no guarantee"). This file's VERDICT/CALLS lists are the
canonical word lists; references/audit.md points here instead of keeping a second copy.

A clean run is NOT proof the post is compliant or accurate. check_posts.py (structure, data
refs, charts) is separate and still required.

Site-specific assumptions (edit here if the site changes): Desi Bites is main-board (flags "SME");
series slug "jargon" may collapse Common mistakes; "risk" posts needn't carry an as-of date.
"""
import calendar
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
VERDICT = (r"\b(overvalued|undervalued|cheap(ly)?|expensive|fairly (valued|priced)|(is|are|looks?) fair|fair price|mispric\w*|bargain|"
           r"attractive(ly)? valued|rich valuation|moat|compounder|impressive|excellent|healthy|robust|strong balance sheet|honest of|"
           r"solid|sound|stable|reasonable(ly)? priced|prudent|disciplined|conservative(ly)?|well-run|best-in-class|durable|"
           r"valued (below|above|at a premium|at a discount)|premium to peers|discount to peers|not (cheap|irrational|a mispricing)|"
           r"inexpensive|cheaper|safe (bet|stock|choice)|outperform\w*|underperform\w*)\b")
VALUATION = r"\b(DCF|WACC|discount rate|intrinsic value|fair value|justified (P/B|P/E|multiple))\b"
SERIES_COPY = r"\b(the next (two|three|four|five|six|seven|eight|nine|ten|\d+) posts|final post|last post in this series|closes? the series|fifty-nine posts)\b"
DO_NOT_TARGET = r"\b(best|top \d+|top (stocks|funds)|multibagger|intraday|strategy that works|tips?|should you (buy|invest)|which is better|target)\b"
PROPER = {"Desi", "Bites", "Foods", "Britannia", "Industries", "Nifty", "Sensex", "Infosys", "HDFC", "Bank", "India", "Indian", "Act", "Tax", "Year", "Income", "Securities", "Exchange", "Board"}
STOP_ACR = {"I", "A", "II", "III", "IV", "AM", "PM", "OK", "CSV", "SVG", "PNG", "ISO", "DB"}
LIQUID = r"\{%.*?%\}|\{\{.*?\}\}"
LAG_CUE = r"(?:as of|as at|up to|until|through|ends?|closing (?:price )?(?:on|of)|close on|prices? (?:on|of)|data (?:to|till|from))"


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


def lines_outside_code(body):
    out, fenced = [], False
    for n, line in enumerate(body.splitlines(), 1):
        if line.strip().startswith("```"):
            fenced = not fenced
            continue
        if not fenced:
            out.append((n, line))
    return out


def prose_lines(body):
    """Prose only: no code, tables, Liquid-only lines, HTML, headings or images."""
    return [(n, l) for n, l in lines_outside_code(body)
            if l.strip() and not l.strip().startswith(("|", "{%", "<", "#", "![", "---"))]


def scan_lines(body):
    """Every non-code line incl. table rows and <details>/<summary> text, markup stripped."""
    return [(n, re.sub(LIQUID + r"|<[^>]+>", " ", l)) for n, l in lines_outside_code(body) if l.strip()]


def minus_3_months(d):
    y, m = d.year, d.month - 3
    if m < 1:
        y, m = y - 1, m + 12
    return date(y, m, min(d.day, calendar.monthrange(y, m)[1]))


def lint(path):
    name = os.path.basename(path)
    text = open(path, encoding="utf-8").read()
    fm, body = split(text)
    off = len(text.splitlines()) - len(body.splitlines())
    res = []
    add = lambda lvl, msg: res.append(f"{lvl:4} {name}: {msg}")

    dm = re.match(r"(\d{4})-(\d{2})-(\d{2})", name)
    pub = date(*map(int, dm.groups())) if dm else None
    cutoff = minus_3_months(pub) if pub else None

    title, desc = fm.get("title", ""), fm.get("description", "")
    both = title + " " + desc
    serp = fm.get("seo_title") or title   # head.html renders seo_title if set; brand suffix only when it fits in 60
    if len(serp) > 60:
        add("WARN", f"search title is {len(serp)} chars (> 60, Google truncates); shorten it or add a seo_title ≤ 60")
    elif len(serp) > 44 and not fm.get("seo_title"):
        add("INFO", f"title is {len(serp)} chars, so ' | Wealth Primer' won't be appended (fine; ≤ 44 keeps the brand)")
    tw = re.findall(r"[A-Za-z][A-Za-z'’]+", title)[1:]
    if sum(w[0].isupper() and not w.isupper() and w not in PROPER for w in tw) >= 3:
        add("WARN", "title looks Title Case (house style is sentence case; proper nouns are fine)")
    if not 140 <= len(desc) <= 155:
        add("WARN", f"description is {len(desc)} chars (aim 140–155)")
    if re.search(HYPE, both, re.I):
        add("FAIL", "hype word in title/description")
    for rx, lbl in ((CALLS, "trade-call phrasing"), (VERDICT, "verdict word")):
        m = re.search(rx, both, re.I if rx != CALLS else 0)
        if m:
            add("WARN", f"{lbl} in title/description: “{m.group(0)}”")
    m = re.search(DO_NOT_TARGET, both, re.I)
    if m:
        add("WARN", f"possible do-not-target head term in title/description: “{m.group(0)}” (references/seo.md §1)")
    if not fm.get("image"):
        add("WARN", "no image: front matter (the site logo would ship as the social card; run scripts/make_og_cards.py)")
    tm = re.search(r"(\d{2}:\d{2}:\d{2})\s+\+0530$", fm.get("date", ""))
    if not tm:
        add("WARN", "date should read 'YYYY-MM-DD HH:MM:SS +0530'")
    elif tm.group(1) > "09:00:00":
        add("FAIL", "post time is after 09:00 +0530 and will miss that day's build")
    for tgt in re.findall(r"post_url\s+(\d{4}-\d{2}-\d{2})-", body):
        if pub and tgt > pub.isoformat():
            add("FAIL", f"post_url to a post dated {tgt}, after this post ({pub}); the build breaks on publish")
    if fm.get("series") == "tax" and not re.search(r"Tax Year|FY", both):
        add("INFO", "tax post: Tax Year / FY label not in title or description (must be in the opening and one H2)")

    if not fm.get("needs_review") and fm.get("series") != "tax":
        tm = re.search(r"\b(LTCG|STCG|STT|TDS|capital gains? tax|taxed at|slab rate|indexation|taxed (?:as|at|in|differently|when|only)|taxable in|Income-tax Act|section 1[0-9]{2}[A-Z]*)\b", body, re.I)
        if tm:
            add("WARN", f"states a tax rule (“{tm.group(0)}”) but has no needs_review: front matter; either soften to what is certain plus “check the current rule”, or add needs_review: tax and rules_as_of (CLAUDE.md, Professional review)")
    if fm.get("needs_review"):
        if not fm.get("rules_as_of"):
            add("FAIL", "needs_review set but rules_as_of is missing")
        if bool(fm.get("reviewed_by")) != bool(fm.get("reviewed_on")):
            add("FAIL", "reviewed_by and reviewed_on must be set together, and only when a professional really reviewed the post")

    plines = prose_lines(body)
    ptext = "\n".join(t for _, t in plines)
    hard_rs = []
    lines = body.splitlines()

    for n, t in scan_lines(body):
        for rx, lvl, label in ((HYPE, "WARN", "hype word (OK only if quoted/negated, e.g. “no guarantee”)"),
                               (CALLS, "WARN", "possible trade call (OK only if quoted or negated)"),
                               (VERDICT, "WARN", "verdict-style word (fine only for a fictional/generic company or a mechanical statement)")):
            m = re.search(rx, t, re.I if rx != CALLS else 0)
            if m:
                add(lvl, f"line {n + off}: {label}: “{m.group(0)}”")
        if re.search(VALUATION, t, re.I):
            add("WARN", f"line {n + off}: valuation-model term; allowed only for Desi Bites or a generic company, never a real listed one")
        if re.search(SERIES_COPY, t, re.I):
            add("WARN", f"line {n + off}: series-structure copy that goes stale (“{t.strip()[:50]}…”)")
        if re.search(r"\bSME\b|NSE Emerge", t) and "desi" in body.lower():
            add("WARN", f"line {n + off}: Desi Bites is a main-board company, not SME/Emerge")

    for n, t in plines:
        raw = lines[n - 1]  # un-stripped: Liquid still visible
        if re.match(r"^\s*(\d+|\{\{[^}]*\}\})\.\s", raw):
            i = n - 2
            while i >= 0 and lines[i].strip():
                i -= 1
            first = lines[i + 1].strip() if i + 1 < n - 1 else ""
            if first and not re.match(r"^(\d+\.|[-*+])\s|^\{\{[^}]*\}\}\.\s", first):
                liquid = raw.lstrip().startswith("{{")
                if not (liquid and "date:" in raw.split("}}")[0]):
                    add("WARN" if liquid else "FAIL",
                        f"line {n + off}: starts with a {'Liquid value (check it does not render as a bare number)' if liquid else 'number'} + '. ' inside a prose paragraph; kramdown may make it a list item. Reflow the line")
        clean = re.sub(r"`[^`]*`|" + LIQUID, "", t)
        if re.search(r"(?<=[\s(])-[₹\d]", clean):
            add("WARN", f"line {n + off}: hyphen-minus before a number; use '−' (U+2212)")
        if re.search(r"\b20\d\d-\d\d-\d\d\b", clean):
            add("WARN", f"line {n + off}: ISO date in a sentence; write '3 October 2024'")
        if re.search(r"(?<![\d,])\d{1,3}(,\d{3}){2,}(?![\d,])", clean):
            add("WARN", f"line {n + off}: Western digit grouping; Indian style is 12,34,567 (or use inr.html)")
        if re.search(r"₹\s?\d", t):
            hard_rs.append(n)
    if hard_rs:
        add("INFO", f"{len(hard_rs)} line(s) with a typed ₹ amount in prose (first: line {hard_rs[0] + off}); real data should come from _data/ via Liquid, scenario numbers are fine")

    for n, line in lines_outside_code(body):
        h = re.match(r"^(#{1,4})\s+(.*)", line)
        if not h:
            continue
        if len(h.group(1)) == 1:
            add("FAIL", f"line {n + off}: H1 in body; the layout already renders the title as H1")
            continue
        for rx, lvl in ((HYPE, "FAIL"), (CALLS, "WARN"), (VERDICT, "WARN")):
            if re.search(rx, h.group(2), re.I if rx != CALLS else 0):
                add(lvl, f"line {n + off}: compliance word in heading: “{h.group(2)}”")
        ws = re.findall(r"[A-Za-z][A-Za-z'’]+", h.group(2))[1:]
        if sum(w[0].isupper() and not w.isupper() and w not in PROPER for w in ws) >= 3:
            add("WARN", f"line {n + off}: heading looks Title Case: “{h.group(2)}”")

    # structure
    tk = re.search(r"^\*\*Takeaway:\*\*\s*(.*?)(?=\n\s*\n|\Z)", body, re.M | re.S)
    if not tk:
        add("FAIL", "no paragraph starting exactly '**Takeaway:**'")
    else:
        tt = re.sub(LIQUID, "0000000000", " ".join(tk.group(1).split()))
        first = re.split(r"(?<![0-9A-Za-z]\.[A-Za-z])(?<!e\.g)(?<!i\.e)(?<!No)(?<=[.!?])\s+(?=[A-Z*_\"“])", tt)[0]
        if len(first) > 280:
            add("WARN", f"first Takeaway sentence is {len(first)} chars (> 280; Liquid values counted as 10 chars)")
        if len(re.findall(r"[.!?](?:\s|$)", tt)) > 4:
            add("INFO", "Takeaway runs past ~3 sentences")
        if body[tk.end():].strip():
            add("INFO", "Takeaway is not the last paragraph of the post body")
    if "Common mistakes" not in body:
        add("INFO" if fm.get("series") == "jargon" else "WARN",
            "no 'Common mistakes' section" + (" (allowed to collapse for short glossary posts)" if fm.get("series") == "jargon" else ""))
    cm = re.search(r"^## Common mistakes\s*$(.*?)(?=^## |\Z)", body, re.M | re.S)
    if cm:
        items = len(re.findall(r"^(?:\d+\.|[-*]|###)\s", cm.group(1), re.M)) or len(re.findall(r"^\*\*[^*]+\*\*", cm.group(1), re.M))
        if items and not 2 <= items <= 4:
            add("INFO", f"Common mistakes has ~{items} items (house style 2–4)")
    if "<details" in body and "Explain it like I" not in body:
        add("INFO", "<details> block without the standard “Explain it like I'm 10” summary")
    h2 = re.findall(r"^## (.*)", body, re.M)
    if len(h2) < 3:
        add("INFO", "fewer than 3 H2 sections")
    if not any(re.search(r"\?$|^(What|How|Why|When|Which)\b", h) for h in h2):
        add("INFO", "no question-style H2 (consider phrasing one as the reader's search question)")
    if len(re.findall(r"post_url", body)) < 3:
        add("INFO", "fewer than 3 post_url internal links")
    if fm.get("series") and f"/series/{fm['series']}/" not in body:
        add("INFO", f"no link to the series hub (/series/{fm['series']}/) in the body")
    for alt in re.findall(r"!\[([^\]]*)\]\(", body):
        if len(alt.split()) < 4:
            add("WARN", f"image alt text too thin: “{alt}”")
    if "post-disclaimer" in body or "not investment advice" in body.lower():
        add("WARN", "disclaimer text in body; the layout renders it, don't paste or reword")
    if "term" in fm:
        t = re.sub(r"\(.*?\)", "", fm["term"]).strip().lower()
        if t and t not in " ".join(ptext.split()[:100]).lower():
            add("INFO", f"term “{t}” not in the first 100 words")

    # acronyms (heuristic: a visible expansion pattern somewhere in the post)
    seen, undefined = set(), []
    for a in re.findall(r"\b[A-Z]{2,6}\b|\b[A-Z]{1,6}/[A-Z]{1,6}\b", ptext):
        if a in seen or a in STOP_ACR:
            continue
        seen.add(a)
        ea = re.escape(a)
        if not re.search(rf"\({ea}\)|\b{ea}\s*\(|\*\*{ea}\b|\b{ea}\s+[—–-]|—\s*{ea}\b", ptext):
            undefined.append(a)
    if undefined:
        add("INFO", "acronyms with no visible definition (the expansion must precede first use; this check only confirms one exists): " + ", ".join(undefined))

    # lag: exact dates are FAIL, month-only dates that could straddle the cutoff are WARN
    if pub:
        for line_no, t in scan_lines(body):
            for dd, mo, yr in re.findall(rf"{LAG_CUE}\s+(?:(\d{{1,2}})\s+)?([A-Z][a-z]+)\s+(20\d\d)", t):
                mm = MONTHS.get(mo.lower())
                if not mm:
                    continue
                if dd:
                    d = date(int(yr), mm, min(int(dd), calendar.monthrange(int(yr), mm)[1]))
                    if d > pub:
                        add("INFO", f"line {line_no + off}: “{dd} {mo} {yr}” is after the post date; fine for a deadline, wrong for data")
                    elif d > cutoff:
                        add("FAIL", f"line {line_no + off}: as-of {dd} {mo} {yr} is inside the 3-month lag (data must be on or before {cutoff})")
                else:
                    end = date(int(yr), mm, calendar.monthrange(int(yr), mm)[1])
                    if end > pub:
                        add("INFO", f"line {line_no + off}: “{mo} {yr}” is after the post date; fine for a deadline, wrong for data")
                    elif end > cutoff:
                        add("WARN", f"line {line_no + off}: as-of {mo} {yr} may be inside the 3-month lag (cutoff {cutoff}); use an exact day on or before it")
            for iso in re.findall(r"\b(20\d\d-\d\d-\d\d)\b", re.sub("`", "", t)):
                try:
                    d = date.fromisoformat(iso)
                except ValueError:
                    continue
                if cutoff < d <= pub and "post_url" not in t:
                    add("WARN", f"line {line_no + off}: date {iso} is inside the 3-month lag (cutoff {cutoff}); if it is a market/price date it must be older")
    if not re.search(r"as of|as at|FY\d\d|Tax Year", ptext, re.I) and fm.get("series") != "risk":
        add("INFO", "no visible as-of date or period; worked examples need one")
    return res


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0 if argv else 2
    fails = 0
    for p in argv:
        out = lint(p)
        fails += sum(l.startswith("FAIL") for l in out)
        print("\n".join(out) if out else f"ok   {os.path.basename(p)}: no lint hits")
    print("\nExit 0 means no FAIL lines, NOT that the post is compliant or accurate. Read every WARN/INFO, then do the audit.")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
