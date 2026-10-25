---
name: new-series
description: Decide where a new topic belongs on Wealth Primer - an existing series, a brand-new series, or the standalone "explainers" bucket - and scaffold a new series when warranted. Use for "where does this topic go", "start a series on X", "company analysis", "this doesn't fit anywhere". Proposes first; scaffolds only after the owner approves.
---

# new-series

## Where does a topic go? (decision order)

1. **Existing series** if it extends that series' promise (see `_data/series.yml` `about`). Prefer this: more depth under an established hub beats a thin new one.
2. **New series** only if all hold: ≥ 5 posts you can name that read well in order; a distinct reader question ("how do I read a company's filings?"); a hub-worthy title that someone would search; the compliance position is clear (below). Fewer than 5 → don't start a series; put the posts in 3.
3. **Standalone** — a single-topic explainer that fits no cluster. Use the catch-all series `explainers` ("Investing explainers", `numbered: false`, so no "Part N of M"). Create it when the first standalone post is approved; if the same theme collects 5+ posts, promote them into a real series later (the URLs stay; only the `series:` field and the hub change).
4. **Not a post** — if it needs a verdict, a tip or personalised advice to be interesting, it doesn't fit the blog (see `write-post/references/seo.md` §1).

## Scaffold (after the owner approves the series)

```
python3 scripts/new_series.py <slug> "<Title>" --description "<100-170 chars>" --about "<longer, different text>" [--planned N] [--unnumbered]
python3 scripts/check_posts.py
```
Creates the `_data/series.yml` entry and `series/<slug>.markdown`. The homepage card, `/series/` index, footer, breadcrumbs, prev/next, "Part N of M" and GA4 `content_series` all follow automatically; the hub stays noindexed until its first post is live. **The slug is permanent** (URL and GA4 key). Then: add the series to the `TODO.md` roadmap, run `plan-module` for its first module, and add a line to `README.md` if the series needs explaining. If the series needs its own rules (e.g. company analysis), the owner adds them to `CLAUDE.md`; don't edit CLAUDE.md yourself.

## Company analysis: a guarded design, owner decision required

`CLAUDE.md` forbids verdicts, valuation views, discount rates/fair values and anything that reads as a call on a real listed company; that is why the blog needs no SEBI Research Analyst registration. A "company analysis" series stays on the safe side of that line only as **"How to read a company's filings"**, with these constraints (propose them; the owner and, ideally, a securities-law adviser decide — don't treat this as legal advice):

- **Method, not opinion.** Fixed rubric applied the same way every time (revenue and margin trend, working-capital days, ROCE, cash conversion, leverage, related-party and auditor notes), reported as observables and arithmetic, with each metric defined in a Jargon post.
- **No verdicts of any kind**, including soft ones ("healthy", "stretched", "rich", "comfortable"); no ranking; no "better than peers"; no price, target, discount rate or fair value; no "what to watch for upside/downside".
- **Selection by rule, not by view:** companies chosen by a published mechanical rule (e.g. index constituents in alphabetical order, or by teaching need such as "a company with a large receivables build") and said so; never "stocks to study".
- **Lag and as-of:** figures ≥ 3 months old with filing/period stated; company-reported figures from the filing, with link; prices only if a concept needs them and then lagged.
- **Fixed disclaimer plus a visible note** that the post is a worked example of reading filings, not research or a recommendation, and that the company has no connection to the blog; no company outreach, no commissions, no affiliate links.
- **Cumulative effect:** one company at most per post, no repeats within a module, and the planner checks that praise or criticism doesn't pile up across posts.
- **Pre-publication check:** `post-auditor` on every post, `verify-claims` on every cited filing statement.

Until the owner approves this design, `post-researcher` may list company-analysis topics only as "owner decision" items.
