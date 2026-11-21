# Repository assessment — Sprint 1

Assessed 21 November 2026 on branch `claude/happy-babbage-45qbnc` (main at `9fb57bd`). Assessment only: no production file, post or URL was changed.

**[V]** = checked in the repo, the local build, the deploy log or Search Console/GA4. **[H]** = hypothesis, not yet tested.

## Summary

The repository is in much better shape than the brief assumes. It has a mature publishing pipeline, data-driven posts, strong technical SEO, tested calculators and documented house rules. What it lacks is not engineering but **audience and indexing**: as of 21 Nov 2026 Google indexes 49 of 157 published posts, and the site has had 2 search clicks since search data began on 30 Sep 2026 (see `analytics-baseline-2026-11-21.md`). Sprint 2 should spend most effort on information architecture and content quality signals, and very little on rebuilding the site.

## Inventory

| Area | Finding |
|---|---|
| Posts | 216 in `_posts/`: **157 published** (18 Aug – 20 Nov 2026), **59 scheduled** (to 18 Mar 2027) [V] |
| Pace | 7 posts in Aug, 38 in Sep, 101 in Oct, 16 in Nov so far; one every two days from Nov [V] |
| Series (written, incl. scheduled) | Jargon 65 · Fundamental analysis 33 · Mutual funds 30 · Technical analysis 28 · Risk 28 · Tax 18 · Money Before Markets 7 · Market basics 7 [V] |
| Pages | Home, Series hub + 8 series pages, Glossary, Tools hub + 8 tool pages, Case study, Methodology, About, Privacy, 404 [V] |
| Calculators | 8: **3 Google Sheets** (rolling returns, SIP/XIRR, DCF) and **5 on-page JavaScript calculators** (loss recovery, cost drag, real return, bond yield, position size) in `assets/js/calc.js` (11 KB, no libraries) [V] |
| Data pipeline | ~40 Python scripts in `scripts/` derive `_data/*.yml` (36 files), charts (`assets/charts/`, 3.3 MB SVG) and OG cards (`assets/og/`, 8.7 MB) [V] |
| Editorial process | `CLAUDE.md`, `_docs/how-it-works.md`, `TODO.md`, 11 project skills and 2 agents in `.claude/` (write, audit, verify claims, refresh, ship, site audit…) [V] |
| Review material | `_review/` (research briefs, module roadmaps, calculator specs, source PDFs) — excluded from the build because of the leading underscore [V] |

## Stack and configuration

- **Jekyll 4.4.1 locally** (Gemfile), theme **minima 2.5** heavily overridden: 5 layouts, 16 includes, `assets/main.scss` ~1,500 lines [V].
- Plugins: `jekyll-feed`, `jekyll-seo-tag`, `jekyll-sitemap` (the sitemap is replaced by a custom `sitemap.xml` that omits noindexed pages) [V].
- `future: false`, permalink `/:year/:month/:day/:title/`, timezone `Asia/Kolkata` [V].
- Integrations configured in `_config.yml`: GA4 (`G-6KTY7W7VCR`, production only), Buttondown newsletter, giscus comments, AdSense account meta tag (no ad code, no `ads.txt`) [V].
- Collections: `tools` → `/tools/:name/` [V].

## Deployment

- `.github/workflows/pages.yml`: on push to `main`, on `workflow_dispatch`, and four daily crons (03:31, 04:07, 04:43, 06:19 UTC) so future-dated posts publish without a manual step [V].
- **Production build uses `actions/jekyll-build-pages@v1` (image v1.0.13)**, which builds with GitHub's own `github-pages` gem set, not the Gemfile. The 20 Nov deploy log shows the theme loading from `/usr/local/bundle/gems/minima-2.5.1` while bundler had installed 2.5.2. The image ships Jekyll 3.10 [H, inferred from the image; the log line naming the Jekyll version was not printed]. PR checks and local builds use Jekyll 4.4.1. See risk R1.
- `.github/workflows/pr-checks.yml`: `check_posts.py`, lint of changed posts, OG-card and image-dimension checks, and a `--future` build. Advisory, not required [V].

## Local build and checks (21 Nov 2026)

| Check | Result |
|---|---|
| `bundle exec jekyll build` | Pass, 2.8 s, 181 HTML pages, 179 sitemap URLs [V] |
| `bundle exec jekyll build --future` | Pass, 3.3 s [V] |
| Warnings | Sass deprecation warnings from minima's `_base.scss` (`lighten()`); harmless now [V] |
| `scripts/check_posts.py` | 216 posts, **0 errors**, 19 warnings (no `term:` on non-glossary posts) [V] |
| `scripts/check_tools.mjs` | **103 calculator figures checked against the posts, 0 mismatches** [V] |
| `scripts/add_img_dims.py --check` | 0 chart images without dimensions [V] |
| `scripts/make_og_cards.py --check` | Not run: Pillow is not installed on this Mac (runs in CI) [V] |
| `site-audit/audit_site.py` | **4 errors: broken internal links to scheduled posts**, 0 warnings, 2 info (two noindexed series hubs) [V]; see `technical-seo-audit.md` |
| Lighthouse (local build, mobile and desktop) | 100 in all categories on home, a post and a tool page [V] |

## Strengths worth preserving

1. **Numbers are generated, not typed.** Posts read figures from `_data/` produced by scripts; calculators are tested against the posts. This is the site's real differentiator and is unusual for a finance blog.
2. **Compliance by construction.** Shared disclaimer, `needs_review` notices with `rules_as_of`, lag rule, "no verdicts on real companies" — all enforced in includes and checks.
3. **Template quality.** One H1, canonical, meta description, breadcrumbs JSON-LD, Indian number formatting, accessible tables, lazy images — on every page.
4. **Process documentation.** A new contributor (or agent) can learn the rules from `CLAUDE.md` and `_docs/how-it-works.md`.

## Weaknesses

1. **Indexing and authority** — 108 of 157 published posts are not indexed [V]. Cause not yet proven: age explains part of it (see technical SEO audit), site-level quality assessment may explain the rest [H].
2. **Information architecture follows the writing plan, not the reader.** The beginner path for company analysis (`reading-a-balance-sheet`, `reading-an-income-statement`, `reading-a-cash-flow-statement`) sits in *Jargon, Decoded*, so the *Fundamental Analysis — Beginner to Expert* card says "start with DuPont" [V].
3. **The highest-demand calculator lives off-site.** "rolling returns calculator" and five similar queries are the only calculator searches seen; the rolling-returns tool is a Google Sheet, and `/tools/rolling-returns/` has had no impressions [V].
4. **Production and CI build with different software** (R1).
5. **Plain links to scheduled posts break on live pages** until the target's date (R2).
6. **No redirect capability** (no `jekyll-redirect-from`), so any consolidation that moves a URL is currently impossible without a 404 [V].
7. **Analytics is mostly bot traffic and has no event design** for calculators, newsletter or outbound sheet clicks [V for traffic; event set not inspected].

## What was not assessed

- Production HTML byte-for-byte against the local build (would confirm R1's impact).
- GA4 key-event configuration and filters (internal traffic, bot filtering).
- Buttondown subscriber count and AdSense application status (owner only).
- Accuracy of individual posts (the September 2026 review and `post-auditor` cover this; not repeated).
