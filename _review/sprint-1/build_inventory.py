#!/usr/bin/env python3
"""Build _review/sprint-1/content-inventory.csv (Sprint 1, assessment only).

Inputs
  _posts/*.markdown           front matter
  SITE_FUTURE                 a `jekyll build --future` output dir (word counts, outbound links)
  SITE_LIVE                   a plain `jekyll build` output dir (inbound links as Google sees them today)
  GSC_PAGES                   Search Console Pages tab, all data to 19 Nov 2026: path|clicks|impressions|position;...
  GSC_INDEXED                 Search Console "indexed pages" list, 21 Nov 2026: space-separated paths, '/2026/' stripped

    scripts/jekyll_build.sh /tmp/site && scripts/jekyll_build.sh /tmp/sitef --future
    python3 _review/sprint-1/build_inventory.py /tmp/sitef /tmp/site \
        _review/sprint-1/data/gsc-pages-2026-11-19.txt _review/sprint-1/data/gsc-indexed-2026-11-21.txt

Proposed actions are proposals for the owner, not decisions. Nothing here changes a URL or a post.
"""
import csv, os, re, sys, collections
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TODAY = date(2026, 11, 21)
site_future, site_live, gsc_pages_f, gsc_indexed_f = sys.argv[1:5]

# Overlapping topics: candidates for one hub / clearer canonical owner. CONSOLIDATE here means
# "connect under a hub and decide which post owns the head term" — not merge or redirect.
CLUSTERS = {
    "returns-measurement": ["point-to-point-returns", "rolling-returns", "price-vs-total-return-index", "benchmarks-and-comparing-like-with-like"],
    "sip": ["sips-xirr-and-timing-myths", "step-up-sips"],
    "return-ratios": ["roe", "roa", "roce", "dupont-roe-decomposition", "equity-multiplier"],
    "free-cash-flow": ["free-cash-flow", "forecasting-free-cash-flow", "earnings-yield-and-fcf-yield", "ocf-pat"],
    "enterprise-value": ["enterprise-value", "ev-ebitda", "net-debt-ebitda"],
    "price-to-book": ["price-to-book", "valuing-a-bank-price-to-book", "book-value-per-share"],
    "promoter-and-float": ["free-float-and-promoter-holding", "contingent-liabilities-pledges-and-promoter-holding", "index-weights-free-float"],
    "risk-adjusted-return": ["volatility-and-sharpe", "sortino-and-information-ratio", "up-and-down-capture-ratios", "alpha", "beta"],
    "index-tracking": ["index-funds-vs-etfs", "tracking-error-and-tracking-difference"],
    "margin-and-leverage": ["leverage-and-margin", "margin-calls-and-peak-margin", "option-writing-and-margin"],
    "debt-funds": ["debt-funds-explained", "fixed-deposit-vs-debt-fund", "liquid-and-overnight-funds", "yield-to-maturity", "modified-duration"],
    "reits": ["reit-structure", "reits-and-invits"],
    "fund-costs": ["expense-ratios-direct-vs-regular", "exit-load", "portfolio-turnover-ratio"],
}
CLUSTER_OF = {s: c for c, ss in CLUSTERS.items() for s in ss}

SERIES_JOURNEY = {
    "jargon": "Learn", "market-basics": "Learn", "money-before-markets": "Portfolio",
    "fundamental-analysis": "Analyse", "technical-analysis": "Analyse", "mutual-funds": "Analyse",
    "risk": "Risk", "tax": "Risk & Tax",
}
PORTFOLIO = {"rebalancing-arithmetic", "diversification-is-a-correlation-problem", "concentration-risk",
             "portfolio-overlap", "sequence-of-returns-risk", "emergency-fund-sizing", "inflation-and-real-returns",
             "sips-xirr-and-timing-myths", "step-up-sips", "stp-and-swp", "hybrid-funds", "currency-risk"}


def front_matter(text):
    m = re.match(r"---\n(.*?)\n---\n(.*)", text, re.S)
    fm, body = (m.group(1), m.group(2)) if m else ("", text)
    out = {}
    for line in fm.splitlines():
        mm = re.match(r"^([a-z_]+):\s*(.*)$", line)
        if mm:
            out[mm.group(1)] = mm.group(2).strip().strip('"').strip("'")
    return out, body


def page_html(site, url):
    p = os.path.join(site, url.strip("/"), "index.html")
    return open(p, encoding="utf-8").read() if os.path.exists(p) else None


def article(html):
    m = re.search(r'<div class="post-content e-content"[^>]*>(.*?)</div>\s*(?:<nav|<aside|<section|<div class="series)', html, re.S)
    return m.group(1) if m else html


def words(html):
    return len(re.sub(r"<[^>]+>", " ", re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", html, flags=re.S)).split())


def post_links(html):
    return {h.split("#")[0] for h in re.findall(r'href="(/20\d\d/\d\d/\d\d/[^"]+/)', html)}


# Search Console
gsc = {}
for row in open(gsc_pages_f).read().replace("\n", ";").split(";"):
    if "|" in row:
        p, c, i, pos = row.split("|")
        gsc[p] = (int(c), int(i), float(pos))
indexed = set()
for tok in open(gsc_indexed_f).read().split():
    indexed.add(tok if tok.startswith("/") and not re.match(r"/\d\d/", tok) else "/2026/" + tok)

posts = []
for fn in sorted(os.listdir(os.path.join(ROOT, "_posts"))):
    m = re.match(r"(\d{4})-(\d\d)-(\d\d)-(.+)\.(markdown|md)$", fn)
    if not m:
        continue
    y, mo, d, slug = m.group(1), m.group(2), m.group(3), m.group(4)
    fm, body = front_matter(open(os.path.join(ROOT, "_posts", fn), encoding="utf-8").read())
    url = f"/{y}/{mo}/{d}/{slug}/"
    posts.append(dict(file=fn, slug=slug, date=f"{y}-{mo}-{d}", url=url, fm=fm, body=body,
                      published=date(int(y), int(mo), int(d)) <= TODAY))

# Inbound links: among live pages (what Google can crawl today), and among all posts once scheduled ones publish
inbound_live, inbound_all = collections.Counter(), collections.Counter()
outbound = {}
for p in posts:
    h = page_html(site_future, p["url"])
    p["html"] = h
    out = post_links(article(h)) - {p["url"]} if h else set()
    outbound[p["url"]] = out
    for t in out:
        inbound_all[t] += 1
        if p["published"]:
            inbound_live[t] += 1

rows = []
for p in posts:
    fm, h = p["fm"], p["html"]
    art = article(h) if h else ""
    c, i, pos = gsc.get(p["url"], (0, 0, None))
    is_idx = p["url"] in indexed
    wc = words(art)
    tools = re.findall(r'include tool\.html id="([^"]+)"', p["body"])
    journey = "Portfolio" if p["slug"] in PORTFOLIO else SERIES_JOURNEY.get(fm.get("series", ""), "")
    cluster = CLUSTER_OF.get(p["slug"], "")
    reasons = []
    if not p["published"]:
        action, idx = "KEEP (scheduled)", "not yet published"
        reasons.append("scheduled; review publishing pace before it goes live")
    else:
        idx = "indexed" if is_idx else "not indexed"
        if cluster:
            action = "CONSOLIDATE"
            reasons.append(f"overlaps cluster '{cluster}': pick the post that owns the head term and connect the rest under a hub; no merge or redirect proposed")
        elif pos is not None and 8 <= pos <= 40 and i >= 3:
            action = "IMPROVE"
            reasons.append(f"page-2/3 impressions (pos {pos}): refresh title intent and body against queries")
        elif not is_idx and inbound_live[p["url"]] < 3:
            action = "IMPROVE"
            reasons.append(f"not indexed and only {inbound_live[p['url']]} inbound link(s) from live posts: link it from its hub and related posts")
        else:
            action = "KEEP"
            if not is_idx:
                reasons.append("not indexed yet despite inbound links; recheck after hub pages exist")
    rows.append({
        "date": p["date"], "url": "https://wealthprimer.in" + p["url"], "slug": p["slug"],
        "status": "published" if p["published"] else "scheduled",
        "series": fm.get("series", ""), "proposed_journey": journey,
        "title": fm.get("title", ""), "title_chars": len(fm.get("title", "")),
        "seo_title": fm.get("seo_title", ""),
        "description_chars": len(fm.get("description", "")),
        "term": fm.get("term", ""), "needs_review": fm.get("needs_review", ""), "rules_as_of": fm.get("rules_as_of", ""),
        "last_modified_at": fm.get("last_modified_at", ""),
        "words": wc, "tables": art.count("<table"), "images": art.count("<img"),
        "tools_linked": " ".join(tools), "has_kid_section": "yes" if "Explain it like" in p["body"] else "",
        "inbound_links_live": inbound_live[p["url"]], "inbound_links_all": inbound_all[p["url"]],
        "outbound_post_links": len(outbound[p["url"]]),
        "gsc_index_status": idx, "gsc_clicks": c, "gsc_impressions": i, "gsc_avg_position": pos if pos is not None else "",
        "overlap_cluster": cluster, "proposed_action": action, "rationale": "; ".join(reasons),
    })

out = os.path.join(ROOT, "_review", "sprint-1", "content-inventory.csv")
with open(out, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader()
    w.writerows(rows)

pub = [r for r in rows if r["status"] == "published"]
print(len(rows), "rows;", len(pub), "published;", sum(r["gsc_index_status"] == "indexed" for r in pub), "published posts indexed")
print(collections.Counter(r["proposed_action"] for r in rows))
print("words median", sorted(r["words"] for r in pub)[len(pub) // 2], "min", min(r["words"] for r in pub))
print("inbound_live zero:", sum(r["inbound_links_live"] == 0 for r in pub))
assert all(r["words"] > 0 for r in rows), [r["slug"] for r in rows if r["words"] == 0]
