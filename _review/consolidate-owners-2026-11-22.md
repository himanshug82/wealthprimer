# CONSOLIDATE: one owner per head term (approved 22 Nov 2026)

**Approved by the owner on 22 Nov 2026, including the SEO-title change in conflict 3.** Status is tracked in `TODO.md`. Scope: the 37 published posts labelled CONSOLIDATE in `_review/sprint-1/content-inventory.csv` (D5), in 12 overlap clusters, plus the scheduled posts in those clusters and a 13th cluster (REITs) that holds only scheduled posts. CONSOLIDATE means choosing which post should rank for a head term and pointing the others at it. Nothing is merged, redirected or deleted.

## Evidence and its limits

- Search Console (export of 19 Nov 2026, about seven weeks of data): none of the 37 posts has a click; 32 have under 10 impressions. Query-level data is in `_review/sprint-1/technical-seo-audit.md` §4–5.
- That is too little to see two posts competing for one query. Owners below are chosen by **search intent**: the post's title, its `term`, what it actually teaches. Query data is used where it exists (rolling returns, index ETF, exit load, promoter holding).
- **Finding:** in 10 of 13 clusters, every post already targets a distinct term. ROE, ROCE and ROA are three searches, not one, and the overlap label grouped them by topic. Those clusters need no consolidation. Four real conflicts sit in the other three clusters (two of them in returns measurement), listed first.

## Real conflicts: proposed actions

| # | Head term (searcher's intent) | Posts in play | Proposed owner | Action | When |
|---|---|---|---|---|---|
| 1 | "rolling returns calculator" (6 of the 14 rolling-returns queries) | `rolling-returns` (post, 46 impressions, position 72.6), `/tools/rolling-returns/` (no impressions) | **Tool page** for calculator intent; **post** for "what are rolling returns" | Move the calculator link in the post from the bottom (line ~150) to a one-line pointer under the opening paragraph, so calculator searchers landing on the post reach the tool at once. Titles already split the intents; leave them | Now |
| 2 | "price index vs total return index", "TRI vs PRI" | `benchmarks-and-comparing-like-with-like` (live; has a "PRI versus TRI" section; `term: Benchmark (TRI vs PRI)`), `price-vs-total-return-index` (publishes 8 Jan 2027; `term: Total-return index (TRI)`) | **`price-vs-total-return-index`** for TRI/PRI; benchmarks post keeps "mutual fund benchmark" | After 8 Jan 2027: link the benchmarks post's PRI/TRI section to the TRI post as the full explanation, and change its `term` to "Benchmark (mutual fund)" so the glossary doesn't list TRI twice. The TRI post already links back | 8 Jan 2027 (owed link) |
| 3 | "promoter holding" | `free-float-and-promoter-holding` (8 impressions, position 6.0), `contingent-liabilities-pledges-and-promoter-holding` (0 impressions; its title and SEO title both say "promoter holding"; `term: Promoter pledge`) | **`free-float-and-promoter-holding`** for promoter holding; the other owns "pledged promoter shares" | Add a link from the contingent-liabilities post to the free-float post at first mention of promoter holding (today it links one way only). Optionally shorten its SEO title to "Contingent liabilities and pledged promoter shares" so the two don't share the phrase. It has no impressions, so there's nothing to lose, but per the retitle rule this is your call | Now (link); title on your OK |
| 4 | "margin", "margin call", "peak margin" | `leverage-and-margin` (live), `option-writing-and-margin` (live), `margin-calls-and-peak-margin` (publishes 10 Feb 2027) | **`leverage-and-margin`** for margin/leverage; **`margin-calls-and-peak-margin`** for margin call and peak margin | After 10 Feb 2027: link "margin call" in the leverage post and the option-writing post to the new post. The new post already links both | 10 Feb 2027 (owed links) |

## Clusters with no real conflict: proposed owners (no consolidation needed)

Each post owns its own term. Small linking fixes are listed where a natural link is missing; they are optional.

| Cluster | Head term → owner | Optional linking fix |
|---|---|---|
| debt-funds | debt funds → `debt-funds-explained`; YTM → `yield-to-maturity`; duration → `modified-duration`; FD vs debt fund → `fixed-deposit-vs-debt-fund`; liquid funds → `liquid-and-overnight-funds` | YTM post links to no other debt post: add one link to `debt-funds-explained` |
| enterprise-value | EV → `enterprise-value`; EV/EBITDA → `ev-ebitda`; net debt/EBITDA → `net-debt-ebitda` | None |
| free-cash-flow | FCF → `free-cash-flow`; FCFF for a DCF → `forecasting-free-cash-flow`; FCF yield → `earnings-yield-and-fcf-yield`; OCF/PAT → `ocf-pat` | None |
| fund-costs | expense ratio → `expense-ratios-direct-vs-regular`; exit load → `exit-load`; turnover → `portfolio-turnover-ratio` | None (exit-load queries like "exit load on SIP" are an IMPROVE job for that post) |
| index-tracking | index fund vs ETF ("index etf", 10 impressions) → `index-funds-vs-etfs`; tracking error → `tracking-error-and-tracking-difference` | None |
| price-to-book | P/B → `price-to-book`; book value per share → `book-value-per-share`; bank valuation → `valuing-a-bank-price-to-book` | None |
| reits | REIT → `reit-structure`; REIT/InvIT tax → `reits-and-invits` | None |
| return-ratios | ROE, ROCE, ROA, equity multiplier, DuPont: one owner each, the post of that name | None |
| risk-adjusted-return | Sharpe → `volatility-and-sharpe`; beta, alpha, capture ratios, Sortino/information ratio: the post of that name | Beta (2 Oct) doesn't link to alpha (later): add one plain link |
| sip | SIP returns / XIRR → `sips-xirr-and-timing-myths`; step-up SIP → `step-up-sips` | None |

## Inventory labels

If you approve this, the 37 CONSOLIDATE labels change as follows (the labels are what D5 approved, so this needs your OK):

- Posts in the four real conflicts keep **CONSOLIDATE** until their action is done: `rolling-returns`, `benchmarks-and-comparing-like-with-like`, `free-float-and-promoter-holding`, `contingent-liabilities-pledges-and-promoter-holding`, `leverage-and-margin`, `option-writing-and-margin`.
- The other 31 become **KEEP** (no conflict). The not-indexed ones among them (ROE, ROCE, P/B, EV/EBITDA, EV, FCF, OCF/PAT, expense ratio, point-to-point, Sharpe variants and others) are an indexing problem, not an overlap problem; they join the IMPROVE queue's indexing batches rather than this work.

## What I'd do on approval

1. One small PR now: conflict 1 (calculator pointer), conflict 3 (the link; the SEO title only if you say so), and the two optional links (YTM → debt funds, beta → alpha).
2. Two owed-link rows in `TODO.md` for conflicts 2 and 4, dated 8 Jan and 10 Feb 2027.
3. Update the inventory labels as above.
