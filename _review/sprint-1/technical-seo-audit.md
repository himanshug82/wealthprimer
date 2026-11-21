# Technical SEO audit — Sprint 1

21 November 2026. Sources: local build of `main` + this branch (no changes to site files), `.claude/skills/site-audit/scripts/audit_site.py`, local Lighthouse via headless Chrome, and Search Console read in the owner's browser (domain property, data to 19 Nov 2026). **[V]** verified, **[H]** hypothesis.

## Verdict

On-page technical SEO is **already good** and is not the bottleneck. The bottleneck is **indexing**: Google has crawled most of the site and chosen not to index it. Fix the four broken links and the build mismatch, then put the effort into content signals and internal architecture, not template work.

## 1. On-page implementation [V]

Checked across all 181 built pages (157 posts + 24 other pages):

| Item | Status |
|---|---|
| `<title>` | Present on all; custom logic appends the brand only when ≤ 60 chars; **8 titles > 60 chars**; no duplicates |
| Meta description | Present on all; posts' `description` checked to 140–155 chars by `check_posts.py` |
| Canonical | Present on all (jekyll-seo-tag) |
| H1 | Exactly one on every page |
| Images | 0 without `alt`; 0 chart images without width/height; `loading="lazy"` added by the post layout |
| Structured data | JSON-LD from jekyll-seo-tag on every page (`BlogPosting` with `Person` author and `Organization` publisher on posts, `WebSite` on home), plus `BreadcrumbList` on posts (Home › Series › series › post) |
| Open Graph / Twitter | Per-post OG cards in `assets/og/`, `summary_large_image` |
| Sitemap | Custom `sitemap.xml`: posts with `lastmod`, pages, tools; excludes `noindex` pages and empty series hubs. 179 URLs in the current build |
| robots.txt | `Allow: /` + sitemap line |
| noindex | `/series/market-basics/` and `/series/money-before-markets/` are noindexed because neither series has a published post yet (Money Before Markets starts 20 Dec 2026, Market basics 1 Jan 2027); they flip automatically. Intended |
| RSS | `/feed.xml` (jekyll-feed) |
| Language | `lang: en-IN` |

## 2. Errors found [V]

`audit_site.py` on the live-equivalent build: **4 errors, 0 warnings.** All four are published posts linking with a plain relative link to a post that is not yet published, so the link is a **404 on the live site today** (confirmed with `curl`: `/2026/11/26/fo-is-business-income/` returns 404).

| Source (live) | Broken target (publishes) |
|---|---|
| `/2026/11/18/option-writing-and-margin/` | `/2026/11/26/fo-is-business-income/` (26 Nov) |
| `/2026/11/18/option-writing-and-margin/` | `/2026/11/24/option-expiry-and-settlement/` (24 Nov) |
| `/2026/11/06/call-and-put-options/` | `/2026/11/26/fo-is-business-income/` (26 Nov) |
| `/2026/11/14/option-time-value/` | `/2026/11/30/implied-volatility/` (30 Nov) |

They heal on their own by 30 Nov, but the pattern will recur: `check_posts.py` guards `{% post_url %}` to future posts (a build failure) but not plain links to future posts (a silent 404). Fix: add that check to `check_posts.py` (see risk R2).

## 3. Performance and mobile [V]

Local Lighthouse (production analytics script is not in the local build, so live numbers will be slightly lower):

| Page | Mobile perf / a11y / best practices / SEO | Desktop | Mobile LCP | CLS |
|---|---|---|---|---|
| `/` | 100 / 100 / 100 / 100 | 100 ×4 | 1.1 s | 0 |
| `/2026/10/11/nim-and-the-spread/` | 100 / 100 / 100 / 100 | 100 ×4 | 1.1 s | 0 |
| `/tools/sip-xirr/` | 100 / 100 / 100 / 100 | 100 ×4 | 0.9 s | 0 |

The first homepage run showed a 1.95 s unattributed long task (score 72); a re-run gave 100 with 0 ms blocking time, so it was a cold-start artifact. Median post HTML is 23 KB; the largest page is `/glossary/` at 56 KB. There is no client-side framework; the only JavaScript is the 11 KB calculator file on tool pages and GA4 in production.

## 4. Search Console baseline [V]

Full numbers in `analytics-baseline-2026-11-21.md`.

### Indexing

| Status (21 Nov 2026) | Pages |
|---|---|
| Indexed | 53 (49 posts + home, privacy, two series hubs) |
| Crawled – currently not indexed | 101 |
| Discovered – currently not indexed | 20 |
| Page with redirect | 5 (not inspected; likely `http`/`www` variants [H]) |
| Excluded by noindex | 1 |

**Index rate by publication date** (published posts only; from `content-inventory.csv`):

| Published | Indexed |
|---|---|
| 18–31 Aug | 4 / 7 |
| 1–15 Sep | 5 / 12 |
| 16–30 Sep | 13 / 26 |
| 1–15 Oct | 23 / 58 |
| 16–31 Oct | 4 / 43 |
| 1–20 Nov | 0 / 11 |

Reading: newer posts are less indexed, so part of the gap is plain lag. But even the oldest cohorts plateau at 40–57%, and **52 posts that earned impressions are not in the index now** (89 posts have impressions; 37 of them are indexed). A page that showed in results and then left the index points to a site-level quality or trust judgement rather than discovery [H — the "Crawled – currently not indexed" drilldown with dates would confirm it]. This is the single most important SEO finding.

By series, published posts indexed: Jargon 24/54, Fundamental analysis 13/29, Technical analysis 6/22, Mutual funds 4/27, Risk 2/20, Tax 0/5.

### Sitemap

`sitemap.xml` submitted 25 Oct 2026, **last read 25 Oct 2026**, status Success, 156 URLs discovered. Google has not re-read it in nearly four weeks; the 30+ posts published since are reached only by links. Owner action: resubmit, then watch whether it is read regularly.

### Performance (30 Sep – 19 Nov 2026)

2 clicks, 692 impressions, CTR 0.3%, average position 24.1. 91 queries, 99 pages with impressions. India 451 impressions, United States 98. Desktop 449, mobile 239.

### Query classification (all 91 queries)

| Class | Queries | Examples |
|---|---|---|
| Branded | 4 | wealthprimer.in (33 impressions, position 19.5), meet the bites, desi bites reading |
| Educational | 65 | capex intensity (pos 4.5), gnpa vs nnpa (10.3), what is ytm (95.2), trend lines, payout ratio, red herring prospectus |
| Investment problem | 8 | exit load on sip, exit load after 1 year, nav should be high or low (×2), entry load in mutual funds in india, ipo listing circuit rules, ex dividend vs record date, mutual fund exit load charges |
| Calculator | 6 | rolling returns calculator (pos 81.2), rolling return calculator (79.5), how to check rolling returns of mutual funds (86) |
| Taxation | 0 | — the first tax posts published from 4 Nov |
| Unclear / noise | 6 | yes, escorts, this quarter, 38.2/50 |
| Prompt-like | 2 | "our cash conversion cycle is 72 days and our cfo wants to get it under 50." — reads like text pasted from an AI assistant or a quiz [H] |

Classification is mine, by reading each query. Educational queries dominate, but almost all rank on page 3+; good positions (< 10) are long-tail terms with little competition (capex intensity, GNPA vs NNPA, NIM vs spread, cement EBITDA per tonne).

## 5. Intent gaps [V for the data, H for the remedy]

1. **Rolling returns** is the largest cluster (14 query variants, 46 impressions on the post at position 72.6, 6 of them explicitly calculator searches). The ranking page is the explainer; the calculator is a Google Sheet behind `/tools/rolling-returns/`, which has no impressions. An on-page rolling-returns tool or a stronger tool page is the clearest search opportunity on the site.
2. **Exit load / expense ratio / NAV / fund size**: 11 variants, mostly "what is" or practical questions; `exit-load` is indexed but at position 35.5.
3. **YTM**: 7 variants at positions 69–110 despite being indexed: the post competes with bank and broker glossaries; probably not winnable soon [H].
4. **Ex-date vs record date**: the only post with a click (position 32.4). A natural "investment problem" page.

## 6. Recommended technical changes (for Sprint 2; none made)

| # | Change | Why | Effort |
|---|---|---|---|
| 1 | Build production with the Gemfile (`bundle exec jekyll build` in `pages.yml`) | Same software in CI, local and live | S |
| 2 | Check plain links to future posts in `check_posts.py` | Stops recurring live 404s | S |
| 3 | Add `jekyll-redirect-from` (no redirects yet) | Makes consolidation possible later | S |
| 4 | Resubmit sitemap; request indexing for hub pages once built | Discovery of new hubs | Owner, S |
| 5 | Hub/guide pages with `CollectionPage`/`ItemList` JSON-LD | Strong internal link targets | M |
| 6 | Author and trust signals: an editorial standards and corrections page linked from every post, and an author page with `sameAs` links (JSON-LD already names the author) | E-E-A-T for a finance (YMYL) site | S–M |
| 7 | Shorten the 8 titles over 60 chars via `seo_title` | Minor | S |

Not recommended: changing permalinks, a site generator migration, AMP, or a CMS.
