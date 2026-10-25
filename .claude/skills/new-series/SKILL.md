---
name: new-series
description: Decide where a new topic belongs on Wealth Primer - an existing series, a brand-new series, or the standalone "explainers" bucket - and scaffold a new series when warranted. Use for "where does this topic go", "start a series on X", "this doesn't fit anywhere". Proposes first; scaffolds only after the owner approves.
---

# new-series

## Where does a topic go? (decision order)

1. **Existing series** if it extends that series' promise (see `_data/series.yml` `about`). Prefer this: more depth under an established hub beats a thin new one.
2. **New series** only if all hold: ≥ 5 posts you can name that read well in order; a distinct reader question ("how do I read a mutual fund factsheet?"); a hub-worthy title that someone would search; the compliance position is clear . Fewer than 5 → don't start a series; put the posts in 3.
3. **Standalone** — a single-topic explainer that fits no cluster. Use the catch-all series `explainers` ("Investing explainers", `numbered: false`, so no "Part N of M"). Create it when the first standalone post is approved; if the same theme collects 5+ posts, promote them into a real series later (the URLs stay; only the `series:` field and the hub change).
4. **Not a post** — if it needs a verdict, a tip or personalised advice to be interesting, it doesn't fit the blog (see `write-post/references/seo.md` §1).

## Scaffold (after the owner approves the series)

```
python3 scripts/new_series.py <slug> "<Title>" --description "<100-170 chars>" --about "<longer, different text>" [--planned N] [--unnumbered]
python3 scripts/check_posts.py
```
Creates the `_data/series.yml` entry and `series/<slug>.markdown`. The homepage card, `/series/` index, footer, breadcrumbs, prev/next, "Part N of M" and GA4 `content_series` all follow automatically; the hub stays noindexed until its first post is live. **The slug is permanent** (URL and GA4 key). Then: add the series to the `TODO.md` roadmap, run `plan-module` for its first module, and add a line to `README.md` if the series needs explaining. If the series needs its own rules (e.g. company analysis), the owner adds them to `CLAUDE.md`; don't edit CLAUDE.md yourself.

## Parked: company analysis

Company analysis (any series about analysing specific listed companies) is **parked by the owner (26 Oct 2026)**. Do not propose, plan or scaffold it, and do not list it as a candidate. It conflicts with the educational-only line in `CLAUDE.md` (no verdicts or views on real companies). Revisit only if the owner raises it again; an earlier design sketch is in this file's git history.
