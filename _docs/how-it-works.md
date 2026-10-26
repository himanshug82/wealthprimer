# How this repo works

Moved out of `TODO.md` on 25 Oct 2026. `CLAUDE.md` is the writing rulebook; this file is the repo mechanics: build, scheduling, data scripts, site features.

## Build and publish
- Pages deploys via GitHub Actions (`.github/workflows/pages.yml`) on every
  push to main and on four daily schedules (09:01, 09:37, 10:13 and 11:49 IST),
  with `future: false` — a post goes live on its date with no manual step.
  GitHub delays scheduled runs (the single 09:00 run fired 4.5–7.5 hours late
  in October 2026), so the extra times are there to get the post up close to
  09:00 IST. Keep post times at or before `09:00:00 +0530`, and never add a
  schedule earlier than 03:30 UTC: that build would run before the post's time
  and skip it.
- **Cadence: one post per series per day.** Several posts share a date (one
  per series); `check_posts.py` only warns when two posts from the SAME
  series share one. A series skips a day when its next post links to a post
  that hasn't published yet — never reorder posts within a series, and never
  add a forward `post_url` to make a date work.
- **Rescheduling:** rename the file (`YYYY-MM-DD-slug.markdown`), change
  `date:` to match, and rewrite every `{% post_url old-name %}` that points at
  it (`grep -rn "post_url OLD" _posts`). Then run `check_posts.py`. URLs of
  already-live posts must never change. Two posts compute their data lag from
  `page.date` (TA 1, Bollinger), so moving posts doesn't break them. `actions/jekyll-build-pages` runs Jekyll in **safe mode**: no custom
  plugins, which is why number formatting, the TOC and series nav are pure
  Liquid includes. Don't "simplify" them into `_plugins/`.
- **`{% post_url %}` may only point at an earlier-dated post** — a link to a
  future post fails the whole build on the linking post's publish date.
- **A line starting with a number or a Liquid value + ". "** mid-paragraph
  becomes a list item. Reflow it.
- Before committing post changes: `python3 scripts/check_posts.py` (must show
  0 errors; it catches forward `post_url`s, bad front matter, unknown series,
  missing data files, unassigned Liquid roots, missing charts), then build with
  future posts. This machine's Ruby is too old; build in Docker:
  `docker run --rm -v "$PWD":/site -w /site -v wp-bundle:/usr/local/bundle ruby:3.3 bash -c "bundle install --quiet && bundle exec jekyll build --future"`
  In the Claude cloud session Ruby 3.3 and the gems are already installed (but `bundle exec`
  and `jekyll` aren't on PATH): `ruby $(gem env gemdir)/gems/jekyll-4.4.1/exe/jekyll build --future -d /tmp/site`
  builds in ~5 seconds (`--future` includes the scheduled posts).
- Python scripts need a venv with pandas, numpy, pyyaml, matplotlib, pillow.
  Re-running a chart script rewrites every SVG it owns with new random ids —
  revert the ones whose only diff is ids.
- minima's SCSS prints Dart-Sass deprecation warnings (`lighten()`); harmless.

## Weekly content pipeline

Two cloud routines in the owner's Claude account (set up 26 Oct 2026), with
the owner as the gate between them. Neither merges or pushes to `main`.

1. **Friday 22:00 IST: research and roadmap** (`trig_01B2BK6zgJHbZG6DhFWFykPJ`).
   Runs `post-researcher`, then `plan-module` for the one or two series with
   the shortest written backlog. Writes `_review/research/<date>.md`, one
   roadmap per series in `_review/roadmaps/<date>-<series>.md`, and one
   `**[Proposed]**` bullet per roadmap in `TODO.md` → *Next content*. Opens a
   PR from `research/<date>`.
2. **Owner, over the weekend:** in that PR, edit the roadmap(s), change
   `[Proposed]` to `[Approved]` for what should be written, delete the rest,
   and merge. Not merging = nothing gets drafted.
3. **Sunday 10:00 IST: drafting** (`trig_01VQPiCaGpgUB8T99nbcfY5w`). Reads
   `[Approved]` bullets on `main`, drafts up to 8 posts (earliest dates first)
   with `write-post` batch mode, runs `post-auditor` and fixes P0/P1, then
   `check_posts.py` and `scripts/jekyll_build.sh /tmp/site --future`. Opens a
   PR from `drafts/<date>`. A post counts as done once its slug exists in
   `_posts/` on `main` or on any `drafts/*` branch, so an unmerged drafts PR
   is not redrafted the next week. The tag becomes `[Drafted]` when every
   post in the roadmap is in a PR.
4. **Owner:** read the rendered pages, merge the drafts PR. The daily
   scheduled build publishes each post on its date.

Dates follow the cadence rules above: the roadmap gives each post a date
(first free day after the series' latest post, one per series per day); if
that date is taken by the time drafting runs, the routine moves it and later
posts of that roadmap to the next free days, keeping their order. Keep two to
three weeks of written backlog so a skipped week leaves no gap.

## Data discipline
- Every figure in a post comes from `_data/` via Liquid, and every derived
  `_data/` file comes from a script — re-run the script, don't hand-edit:

| Script | Writes | Used by |
|---|---|---|
| `build_case_study_2.py` | `case_study_2.yml` (FY26 honest/dressed accounts, quarters, acquisition, DRHP, capital allocation) | FA module 2 |
| `derive_bank.py` | `real_bank.yml` (asserts the balance sheet sums) | FA banks module |
| `derive_ta2.py` | `ta2.yml` | TA module 2 |
| `derive_mf2.py` / `make_mf2_charts.py` | `mf2.yml` / `mf2-*.svg` | MF module 2 |
| `derive_jargon_m6.py` | `jargon_m6.yml` | Jargon module 6 |
| `derive_tax2.py` | `tax.yml`, `tax2.yml` (with per-topic `verification` blocks) | Tax |
| `derive_risk.py` | `risk.yml`, `risk-*.svg` | Risk |
| `derive_jargon_m7.py` | `jargon_m7.yml` | Jargon module 7 (market mechanics) |
| `derive_sectors.py` | `sectors.yml` (each figure with its filing URL) | FA module 4 (sector lenses) |
| `derive_ta3.py` / `make_ta3_charts.py` | `ta3.yml` / `ta3-*.svg` (fixed random seed) | TA module 3 (honest tests) |
| `derive_mf3.py` | `mf3.yml` | MF module 3 |
| `derive_mf4.py` | `mf4.yml` (capture, Sortino/IR, turnover, survivorship simulation, liquid/overnight, IDCW; also holds the Master Circular citations it typed from the primary text) | MF module 4 |
| `derive_risk2.py` | `risk2.yml`, `risk2-*.svg` | Risk module 2 |
| `derive_tax3.py` | `tax3.yml` (with `verification` blocks) | Tax module 3 |
| `derive_mbm.py` | `mbm.yml` (emergency fund, FD vs debt fund, G-secs, PPF, NPS exits, ULIP, REIT; sourced rules typed once with their URLs, asserts reproduce the regulators' own examples) | Money Before Markets |
| `derive_dcf_scenarios.py` | the reverse-DCF scenarios in `case_study.yml` (`dcf.reverse`, written in place; asserts the base case, implied growth, cash-flow multiple and sensitivity grid) | FA terminal value post |
| `make_ta_charts.py` | `ta-*.svg` (asserts `ta.yml`'s RSI, MACD, SMA, zone and double-top figures, and the trend-line post's figures, against the CSV) | TA module 1 |
| `make_diagrams.py`, `make_fa2_diagrams.py`, `make_bank_diagrams.py`, `make_ta2_charts.py` | schematic/chart SVGs | FA, TA |
| `make_og_cards.py` | `assets/og/*.png` (re-run when a title changes; CI's advisory `--check` flags stale cards) | every post |

- Hand-maintained (no script): `case_study.yml`, `real_company.yml`,
  `ta.yml`, `mf.yml`, `fno.yml`. Keep existing values stable — many posts read
  them.
- **Sources:** Britannia — audited consolidated FY25 results filed with NSE/BSE
  8 May 2025 (`real_company.yml`); market price = NSE close 30 Jun 2025.
  HDFC Bank — standalone audited FY25 results, 21 Apr 2025, via its SEC Form
  6-K exhibit (`real_bank.yml`); price ₹2,001.50 pre-bonus (Yahoo's adjusted
  price × 2; 1:1 bonus, record date 27 Aug 2025). Fund NAVs — AMFI via
  mfapi.in, truncated 31 Mar 2026. Britannia OHLCV and Nifty 50 price index —
  Yahoo Finance, to 30 Mar 2026. F&O — SEBI's own study PDFs, checked Sept 2026
  (`fno.yml`: 87.5 lakh = all active FY26 traders; 78.6 lakh = the top-15-broker
  sample every loss figure is computed on). Update the dataset table on
  `/methodology/` when adding a source.
- **Known data quirks** (all taught in posts, found by script): ETF 1:10 unit
  split 26 Sep 2023 and a ₹40.89 payout 25 Feb 2021; overnight fund face value
  ₹10 → ₹1,000 on 3 May 2018, and its pre-2018 history isn't an overnight
  portfolio (the STP/SWP post calls it the "parking fund"); money-market fund
  face-value change 22 Aug 2009; the index fund's first NAV is 3 Apr 2006, so
  the 20-year SIP has 239 instalments.

## The Desi Bites case study
- Fictional snacks company; one reconciled set of books across all series
  (`case_study.yml`, `case_study_2.yml`, reference page `/case-study/`).
- **Main-board NSE and BSE listing** (changed from NSE Emerge/SME on
  24 Sep 2026 so quarterly results, ICDR lock-ins and issue-object caps are
  consistent): DRHP December 2024, RHP June 2025 with FY25 accounts, listed
  15 June 2025 at ₹640. Pre-issue vs post-issue EPS (never "diluted/undiluted"
  — the data keys `eps_undiluted`/`eps_diluted` keep their old names).
- Its size is below real main-board thresholds; fine for teaching.
- Only Desi Bites (or a generic company/bank) gets a DCF, WACC, or justified
  multiple — never a real listed company.

## Site features
- **Series nav** ("Part N of M", prev/next): M is `planned:` in
  `_data/series.yml` — bump it when a series grows. Series with no published
  posts are hidden from the homepage, `/series/` and the footer.
- **Glossary** (`/glossary/`) is built from each post's `term:`.
- **Table of contents** shows automatically at ≥ 6 H2s (`toc: true|false`
  overrides). `last_modified_at:` adds an "Updated" date and updates the
  sitemap — use it when re-verifying a tax post.
- **Number formatting:** `_includes/inr.html` (Indian grouping, true minus,
  drops an all-zero decimal) for prose; `_includes/inr-tables.html` applies it
  to every purely numeric table cell (leaves dates, codes and first-column
  years alone). Jekyll's include tag rejects array subscripts — assign to a
  variable first.
- **Takeaway card:** a paragraph starting `**Takeaway:**` is styled by the post
  layout.
- **`description:`** (140–160 chars) feeds the homepage summary, the meta
  description and the RSS summary.
- **Analytics:** GA4 is live (`G-6KTY7W7VCR`, Google Signals and ads
  personalisation off — `/privacy/` asserts this, keep them in sync);
  GoatCounter optional. `/privacy/` turns each disclosure on from the same
  config keys that enable the feature.
- **Nav:** Series · Glossary · Case study · Methodology · About
  (`header_pages`); Privacy lives in the footer. Pages can set `nav_title:`.

Details of any change: `git log`.
