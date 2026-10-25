#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Crawl a built copy of the site (the way Googlebot reads the HTML) and report SEO/structure problems.

    scripts/jekyll_build.sh /tmp/site            # as live: scheduled posts left out
    python3 audit_site.py /tmp/site [--json out.json]

Checks: <title> missing/duplicate/over 60; meta description missing/duplicate/outside 140-160
(posts) ; canonical missing/off-site/not self; h1 count; skipped heading levels; images without
alt or width/height; internal links to files that don't exist; posts with no inbound internal link
(orphans); noindex pages; near-duplicate bodies (Jaccard on word 5-grams); JSON-LD that doesn't parse.
Exit 1 if any ERROR. WARN/INFO are for a human. Standard library only.
"""
import json
import os
import re
import sys
from collections import defaultdict
from html.parser import HTMLParser
from urllib.parse import urldefrag, urljoin, urlparse


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = ""; self._in = None; self.meta = {}; self.canonical = None
        self.h = []; self.imgs = []; self.links = []; self.ldjson = []; self.text = []
        self._buf = ""; self._skip = 0; self._ld = False; self._ldbuf = ""

    def handle_starttag(self, tag, a):
        a = dict(a)
        if tag == "title": self._in = "title"
        elif tag == "meta" and a.get("name"): self.meta[a["name"].lower()] = a.get("content", "")
        elif tag == "meta" and a.get("property"): self.meta[a["property"].lower()] = a.get("content", "")
        elif tag == "link" and a.get("rel") == "canonical": self.canonical = a.get("href")
        elif re.fullmatch(r"h[1-6]", tag): self._in = tag; self._buf = ""
        elif tag == "img": self.imgs.append(a)
        elif tag == "a" and a.get("href"): self.links.append(a["href"])
        elif tag == "script":
            if a.get("type") == "application/ld+json": self._ld = True; self._ldbuf = ""
            else: self._skip += 1
        elif tag == "style": self._skip += 1

    def handle_endtag(self, tag):
        if tag == "title": self._in = None
        elif re.fullmatch(r"h[1-6]", tag) and self._in == tag:
            self.h.append((int(tag[1]), self._buf.strip())); self._in = None
        elif tag == "script":
            if self._ld: self.ldjson.append(self._ldbuf); self._ld = False
            elif self._skip: self._skip -= 1
        elif tag == "style" and self._skip: self._skip -= 1

    def handle_data(self, d):
        if self._in == "title": self.title += d
        elif self._in: self._buf += d
        if self._ld: self._ldbuf += d
        elif not self._skip: self.text.append(d)


def load(root):
    pages = {}
    for dp, _, fs in os.walk(root):
        for f in fs:
            if f.endswith(".html"):
                p = os.path.join(dp, f)
                url = "/" + os.path.relpath(p, root).replace(os.sep, "/")
                url = re.sub(r"index\.html$", "", url)
                pg = Page(); pg.feed(open(p, encoding="utf-8").read()); pages[url] = pg
    return pages


def is_post(url): return bool(re.match(r"/\d{4}/\d{2}/\d{2}/", url))


def main():
    root = sys.argv[1]; res = defaultdict(list); pages = load(root)
    exists = set(pages) | {"/" + os.path.relpath(os.path.join(dp, f), root).replace(os.sep, "/")
                           for dp, _, fs in os.walk(root) for f in fs}
    titles = defaultdict(list); descs = defaultdict(list); inbound = defaultdict(set); grams = {}
    site = None
    for url, pg in pages.items():
        if url == "/404.html": continue
        noindex = "noindex" in pg.meta.get("robots", "")
        if noindex: res["INFO"].append(f"noindex: {url}")
        t = pg.title.strip()
        if not t: res["ERROR"].append(f"no <title>: {url}")
        elif len(t) > 60: res["WARN"].append(f"title {len(t)} chars: {url}")
        titles[t].append(url)
        d = pg.meta.get("description", "")
        if not d: res["ERROR"].append(f"no meta description: {url}")
        elif is_post(url) and not 140 <= len(d) <= 160: res["WARN"].append(f"description {len(d)} chars: {url}")
        descs[d].append(url)
        if not pg.canonical: res["ERROR"].append(f"no canonical: {url}")
        else:
            c = urlparse(pg.canonical); site = site or f"{c.scheme}://{c.netloc}"
            if c.path != url and not noindex: res["WARN"].append(f"canonical {c.path} != {url}")
        n1 = sum(1 for l, _ in pg.h if l == 1)
        if n1 != 1: res["ERROR"].append(f"{n1} h1 tags: {url}")
        prev = 0
        for l, _ in pg.h:
            if prev and l > prev + 1: res["WARN"].append(f"heading skip h{prev}->h{l}: {url}"); break
            prev = l
        for im in pg.imgs:
            if "alt" not in im: res["ERROR"].append(f"img without alt: {url} {im.get('src')}")
            if not (im.get("width") and im.get("height")) and (im.get("src") or "").startswith(("/", "assets")) \
               and "data:" not in (im.get("src") or ""):
                res["WARN"].append(f"img without width/height: {url} {im.get('src')}")
        for ld in pg.ldjson:
            try: json.loads(ld)
            except Exception: res["ERROR"].append(f"JSON-LD does not parse: {url}")
        for h in pg.links:
            if h.startswith(("mailto:", "tel:", "javascript:")): continue
            u = urlparse(h)
            if u.netloc and (not site or u.netloc != urlparse(site).netloc): continue
            tgt = urldefrag(urljoin(url, u.path or url))[0]
            cand = {tgt, tgt.rstrip("/") + "/", tgt + "index.html"} if not os.path.splitext(tgt)[1] else {tgt}
            if not (cand & exists): res["ERROR"].append(f"broken internal link {h} on {url}")
            else:
                hit = (cand & set(pages)) or (cand & exists)
                if url not in hit: inbound[next(iter(hit))].add(url)
        words = re.findall(r"\w+", " ".join(pg.text).lower())
        if is_post(url) and len(words) > 80:
            grams[url] = {" ".join(words[i:i + 5]) for i in range(0, len(words) - 4, 3)}
    for t, us in titles.items():
        if t and len(us) > 1: res["ERROR"].append(f"duplicate title {t!r}: {', '.join(us)}")
    for d, us in descs.items():
        if d and len(us) > 1: res["ERROR"].append(f"duplicate description on {', '.join(us)}")
    for url in pages:
        if is_post(url) and not inbound.get(url): res["WARN"].append(f"orphan (no inbound internal link): {url}")
    keys = sorted(grams)
    for i, a in enumerate(keys):
        for b in keys[i + 1:]:
            j = len(grams[a] & grams[b]) / max(1, len(grams[a] | grams[b]))
            if j > 0.5: res["WARN"].append(f"near-duplicate body ({j:.0%}): {a} ~ {b}")
    posts = sum(1 for u in pages if is_post(u))
    print(f"{len(pages)} pages ({posts} posts)")
    for lvl in ("ERROR", "WARN", "INFO"):
        print(f"\n{lvl}: {len(res[lvl])}")
        for m in res[lvl][:60]: print("  ", m)
        if len(res[lvl]) > 60: print(f"   ... {len(res[lvl]) - 60} more")
    if "--json" in sys.argv:
        json.dump(res, open(sys.argv[sys.argv.index("--json") + 1], "w"), indent=1)
    sys.exit(1 if res["ERROR"] else 0)


if __name__ == "__main__":
    main()
