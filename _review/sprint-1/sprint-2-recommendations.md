# Sprint 2 recommendations

21 November 2026. Based on the Sprint 1 documents in this folder. Each recommendation names its evidence; decisions marked **Owner** need your approval before any work starts.

## What Sprint 1 changed about the plan

1. **The problem is indexing and trust, not templates.** 49 of 157 published posts are indexed; posts that earned impressions have dropped out; on-page SEO and performance already score at the top. Sprint 2 should not include a technical SEO rebuild.
2. **There is no 12-month baseline and won't be for a while.** Seven weeks of Search Console data, under four months of GA4, mostly bots. Success measures for the next quarter should be leading indicators (indexed posts, impressions, organic sessions from India, newsletter sign-ups), not revenue.
3. **More posts is the wrong lever right now.** 59 posts are scheduled. Publishing them on the current schedule adds to the unindexed pile [H, but cheap to test by slowing down].

## Decisions needed from the owner before Sprint 2

| # | Decision | Recommendation |
|---|---|---|
| D1 | Publishing pace for the 59 scheduled posts | Keep posts that are time-sensitive (option expiry, advance tax, pre-Budget tax) and anything already linked from live posts; move the rest to one or two a week. A 4-week slowdown is a reversible experiment |
| D2 | Navigation labels | Learn · Analyse · Portfolio · Risk & Tax · Tools · About (6 items). Drop "Insights" (implies market commentary, at odds with the lag and no-calls rules). Methodology moves into About and the footer |
| D3 | Scope rule for "decision support" | Tools take generic inputs and show mechanics; nothing ranks, screens or scores real securities or reviews a reader's holdings. Add to `CLAUDE.md` |
| D4 | AdSense timing | Defer until organic traffic is meaningful; then `ads.txt`, consent tool, privacy update, category blocking |
| D5 | Inventory actions | Approve or amend the proposed KEEP / IMPROVE / CONSOLIDATE labels in `content-inventory.csv`. No REDIRECT or RETIRE is proposed; CONSOLIDATE means "connect under a hub and choose which post owns the head term", not merging |

## Sprint 2 backlog (weeks 3–4), in order

### A. Hygiene (small, ship first)

| # | Item | Evidence | Size |
|---|---|---|---|
| A1 | Build production with the Gemfile in `pages.yml`; diff the two builds once before switching | R1 | S |
| A2 | `check_posts.py`: error on plain links to dated-later posts | 4 live 404s, R2 | S |
| A3 | Add `jekyll-redirect-from` (no redirects configured) | R4 | S |
| A4 | **Owner:** resubmit the sitemap; set a GA4 internal-traffic filter; list current key events | Sitemap last read 25 Oct; GA4 bots | S |

### B. Information architecture (the main Sprint 2 work)

| # | Item | Notes |
|---|---|---|
| B1 | Journey map: assign every post a primary journey (draft in `content-inventory.csv`, column `proposed_journey`) | Draft counts incl. scheduled: Analyse 86, Learn 72, Risk 22, Portfolio 18, Risk & Tax 18. Portfolio is thin; that is a content gap to plan, not to fill with new posts this sprint |
| B2 | Hub/guide page template (layout + data file listing ordered posts, tools, case-study chapter) | One template serves all five flagship guides |
| B3 | Two homepage wireframes (problem-first vs. tools-first), plus the hub and post template changes | See `ux-assessment.md` "Direction for Sprint 2" |
| B4 | Design tokens: extract colours, type scale and spacing from `assets/main.scss` into variables; no visual change | Foundation for B3 |
| B5 | Fix the beginner FA path: the hub for "How to analyse stocks" starts with the three statement posts now in Jargon | U1 |

### C. Content (improve, don't add)

| # | Item | Notes |
|---|---|---|
| C1 | **Rolling returns cluster first.** Decide between an on-page rolling-returns calculator and a stronger tool page; connect `rolling-returns`, `point-to-point-returns`, `price-vs-total-return-index` and the tool | 14 query variants, the only calculator demand seen |
| C2 | Refresh the IMPROVE posts with page-2/3 impressions (`refresh-post` skill), one cluster at a time | 62 posts proposed IMPROVE; start with those with impressions |
| C3 | Link the 3 posts with zero inbound links from live posts (`insurance-as-risk-transfer`, `telecom-arpu-and-the-limits-of-sector-lenses`, `sips-and-fifo`) | Inventory |
| C4 | Editorial standards and corrections page, linked from every post and About | Trust signal for a finance site; content mostly exists in `CLAUDE.md` and Methodology |
| C5 | First flagship guide draft: *The Indian Investor's Guide to Mutual Funds* (27 published MF posts, 4 indexed; rolling-returns demand) | New connective writing only; no bulk rewrites |

### D. Measurement

| # | Item |
|---|---|
| D-1 | GA4 events: `calculator_use` (on-page tools), `sheet_open` (Google Sheet tools), `newsletter_signup`, outbound clicks to sources |
| D-2 | Monthly baseline refresh: indexed count, impressions, organic sessions (India), sign-ups; append to `analytics-baseline-*.md` |

## Proposed success measures for the quarter (owner to confirm)

| Measure | Now (21 Nov 2026) | Direction |
|---|---|---|
| Published posts indexed | 49 / 157 | Up, as a share |
| Search impressions per 28 days | read in Search Console at Sprint 2 start | Up |
| Organic sessions from India | 21 organic sessions in total since 1 Aug (all countries) | Up |
| Returning users | 0 recorded | Above 0, then up |
| Newsletter subscribers | unknown (owner) | Up |

No targets are set: the baseline is too small and too young to set honest ones.

## Not recommended for Sprint 2

- Migrating off Jekyll/GitHub Pages, adding a CMS, React or a database.
- Changing permalinks, deleting or merging posts.
- Bulk AI rewriting of existing posts.
- Building portfolio-evaluation tools before D3 is decided.

## Files in this folder

| File | What it is |
|---|---|
| `analytics-baseline-2026-11-21.md` | Search Console and GA4 numbers as read on 21 Nov 2026 |
| `repository-assessment.md` | Repo, stack, build, deploy, strengths and weaknesses |
| `content-inventory.csv` | 216 posts with front matter, words, links, Search Console data and a proposed action |
| `build_inventory.py` | Regenerates the inventory (inputs listed in its docstring) |
| `technical-seo-audit.md` | On-page SEO, errors, Lighthouse, indexing, queries |
| `ux-assessment.md` | Homepage, navigation, post and tool pages, behaviour data |
| `technical-risk-register.md` | 14 risks with mitigation and owner |
