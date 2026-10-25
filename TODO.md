# TODO

Current state (25 Oct 2026): **168 posts written and scheduled** across six
series (Jargon 53 · FA 29 · TA 22 · MF 30 · Tax 18 · Risk 16). The cadence is
**one post per series per day** (MF Module 4 runs every other day, by request). Scheduled through: Jargon 21 Oct · FA 23 Oct
· TA 23 Oct · Risk 23 Oct · MF 7 Nov · **Tax held** 17 Nov → 4 Dec (18 posts,
moved back three weeks on 25 Oct) pending its professional read. **MF Module 4 (7 posts, 26 Oct → 7 Nov, every other
day) was added on 25 Oct 2026, so MF is scheduled through 7 Nov (30 posts).**
**The other written backlogs ran out on 25 Oct** (Tax runs to 4 Dec) — each series needs its next module planned and approved (`plan-module`). All posts were reviewed and every P0/P1/P2 finding
fixed — see `_review/REVIEW-2026-09-24.md`. House style and the rules every
post must follow are in `CLAUDE.md`; this file is for what's still open and
for how the repo works.

---

## Open — needs you

- **GA4 content tagging — one-time setup in Google Analytics (needed for the topic chart):** every
  page now sends `content_type` (home / post / series_hub / page) and, for posts and series
  hubs, `content_series` (e.g. `mutual-funds`) and `content_category` (the series title). In GA4:
  Admin → Data display → Custom definitions → Create custom dimension → scope **Event**, once
  for each of `content_series`, `content_category` (and optionally `content_type`), parameter
  name exactly as written. Data shows 24–48 h after registering; it is not retroactive.
- **Search Console and DNS (from the SEO audit, `_review/SEO-AUDIT-2026-10-25.md`):**
  verify a *Domain* property for wealthprimer.in (DNS TXT), submit `/sitemap.xml`,
  request indexing for `/`, `/series/` and `/series/risk/` (it was `noindex` until
  25 Oct); www is fine — it resolves to GitHub Pages and 301-redirects to the apex
  over http and https (re-checked 25 Oct; the audit's "doesn't resolve" was a test
  timeout). "Page with redirect" (8 URLs: the http:// and www variants) is expected;
  no validation needed. If applying for AdSense, add `ads.txt` and disclose ad cookies on `/privacy/`.
  **Canonical issue (25 Oct):** Search Console reported 1 page as "Duplicate,
  Google chose different canonical than user". The likely cause was `/series/`,
  which repeated the homepage's series cards (54% shared text, 199 words); it
  now has its own per-series text (`about:` in `_data/series.yml`) plus
  start-with/latest links (under 15% overlap, 534 words). `/404.html` is now
  `noindex`. Confirm in Search Console which URL was flagged (Pages → that issue →
  example URL → URL Inspection shows the Google-selected canonical); if it isn't
  `/series/`, tell Claude the URL.
- **Tax series professional read** — all 18 tax posts, now held at 17 Nov →
  4 Dec (daily; moved back three weeks on 25 Oct to make room for the read —
  the Tax hub stays noindexed until 17 Nov automatically). The rules were re-checked against primary sources where
  reachable, but someone who files professionally should read them before
  they publish. `_data/tax2.yml` lists the recorded disagreements. Once
  reviewed, the tax posts can move earlier (rename the files; keep one per day
  and check `scripts/check_posts.py`) — and restore the RELINK links below (14 markers).
- **Next content:** every series except Tax has run out of written posts (MF
  runs to 7 Nov). Plan and approve the next module per series with
  `plan-module`. **R8 "Money Before Markets" is approved (25 Oct) as a new
  series and is next to plan** — emergency fund, EPF/PPF/NPS, term insurance vs
  ULIP, FDs vs debt funds, real returns, plus bonds/G-secs and REITs/InvITs. It
  needs a new slug in `_data/series.yml`, primary sources for every rule and
  rate, and a professional read for the tax-touching posts.

## Decided — 25 Oct 2026

- **Desi Bites' public float stays at 20%** — the free-float and OFS/delisting
  posts already use the gap below the 25% minimum as the teaching example; no
  data change.
- **Formulas stay in code blocks** — no MathJax/KaTeX.
- **No real peer table** in the comparables post — it stays on Desi Bites
  (a listed-peer table drifts toward relative-valuation verdicts).
- **About page avatar: done** — `assets/avatar.svg` (HG monogram, brand blue),
  floated beside the opening paragraph.
- **Tax series moved back three weeks** (see "Tax series professional read").

## Parked — revisit later

- **PageSpeed** (25 Oct, `_review/PAGESPEED-2026-10-25.md`): accessibility/best-practices/SEO are
  100 on all pages and desktop performance is 100. Google Analytics (`gtag.js`) was the one big
  mobile cost (the homepage swung 76–95 with the test machine's CPU), so since 25 Oct it loads at
  the visitor's first tap, click, scroll or key press, or after 10 s (see the comment in
  `_includes/analytics.html`). Trade-off: visitors who leave within 10 s without interacting are
  not counted. Re-run your PageSpeed link after deploy and send the numbers if mobile is below ~90.

- **Newsletter** (decided "later", 25 Oct): `newsletter.action` in `_config.yml`
  is empty, so the signup box renders nothing. Mailchimp or Buttondown — three
  config keys; setup notes in `_includes/newsletter.html`.
- **Comments / giscus** (decided "not now", 25 Oct — moderating "should I buy
  X" questions is a compliance load): `giscus.repo_id` and `giscus.category_id`
  are empty, so nothing renders. To enable: Discussions on, an
  "Announcement"-type category "Comments", install https://github.com/apps/giscus,
  copy both ids from https://giscus.app (mapping: pathname). Notes in
  `_includes/comments.html`.

## Open — verify before the affected post publishes

Each of these is in a post today, worded cautiously, but rests on a secondary
source or on memory. **Several now publish within days** (the schedule moved
earlier on 24 Sep) — work top-down by date. Confirm from the primary source, then tighten the
wording (or correct it).

| Claim | Post(s) | Publishes | Current basis |
|---|---|---|---|
| Britannia left the Nifty 50 effective 28 Mar 2025 | volume | 7 Oct | news coverage, not NSE's circular |
| ICDR caps: GCP ≤ 25%, GCP + unidentified acquisitions ≤ 35%; lock-ins 18 m / 6 m | contingent liabilities, reading a DRHP | 6, 9 Oct | law-firm write-ups |
| HDFC Bank FY24 one-off gain (HDFC Credila stake sale, ₹7,340 cr) | why ratios break on a bank | 10 Oct | Business Standard |
| RBI external-benchmark rule for floating-rate loans (Oct 2019) | NIM and the spread | 11 Oct | memory |
| HDFC Bank FY24 CASA ratio 38.2% | CASA and the deposit franchise | 12 Oct | Business Standard (the Q4 FY24 presentation timed out) |
| HDFC Bank D-SIB surcharge 0.40% from 1 Apr 2025 | capital adequacy | 14 Oct | news report of the RBI release |
| SPIVA India Year-End 2025: 76.3% of large-cap funds lagged over 10 years | alpha | 3 Oct | search results (PDF returned 403) |
| SEBI MF Regulations 2026 expense-ratio slabs (post keeps the 2018/19 slabs, labelled) | AUM, expense ratios | 8 Oct, 28 Sep | new slab table not found |
| Britannia FY25 declared dividend ₹75 | payout ratio | 11 Oct | stockanalysis.com |
| Overnight fund's mandate change "around May 2018" | debt funds explained | 12 Oct | inferred from the NAV series |
| SEBI Feb 2026 categorisation revision (value/contra/dividend yield/sectoral to 80%) | SEBI fund categories | 14 Oct | press summaries |
| ~~Liquid-fund graded exit load in the first week~~ — now confirmed: SEBI Master Circular (20 Mar 2026) para 5.6.5 requires an exit load for exits within 7 calendar days, graded as AMFI prescribes with SEBI; the scale itself is AMFI's and is not in the circular. Tighten the STP and SWP wording if it states more. | STP and SWP | 17 Oct | Master Circular text read 25 Oct |
| Index-futures margins "low-to-mid teens" | leverage and margin | 11 Oct | hedged ("check NSE's margin files") |
| 29 Aug 2024 intermediaries amendment "left room" for education | how finfluencers make money | 15 Oct | secondary sources |
| Tax, from memory: property's 12.5%/20% option; business filers' one-time switch back to the new regime; CBDT condoning late filing; GAAR on round-trips; old 80C → section 123 | several tax posts | 17 Nov → 4 Dec | memory / secondary (incometaxindia.gov.in returns 403) |
| Buyback Regime C: ₹1.25 lakh exemption, promoter definition, timing; foreign shares' exchange-rate convention | buyback taxation, foreign stocks | 27, 29 Nov | recorded as disagreements in `tax2.yml` |
| Ex-date = record date under T+1 (inferred from NSE corporate-actions data); rights-issue rules "from April 2025" (7 or 8 April); OFS framework's current master circular; T+0 rollout status | T+1, record/ex-date, rights issues, OFS | 16–20 Oct | NSE data / secondary |
| GSM stage mechanics ("buyer pays in full plus deposit" is inferred); "not an adverse action" confirmed only for ASM/ESM; GSM criteria after May 2026 | ASM and GSM surveillance | 21 Oct | NSE FAQs + inference |
| Attributions: Lane (stochastic), Granville (OBV); papers cited without fetching (Bouman & Jacobsen 2002; Moskowitz, Ooi & Pedersen 2012; Jegadeesh & Titman 1993); NSE closing auction live from 3 Aug 2026 | TA honest-tests posts | 16–23 Oct | memory / citation not fetched |
| USFDA NAI/VAI/OAI meanings, Form 483 → warning letter chain (fda.gov blocked); embedded value definition; Airtel net debt incl. leases (inferred); Bajaj Finance ALM gap limits (from its presentation, not RBI) | sector-lens posts | 20–23 Oct | secondary / inference |
| Overseas-investment halts of Jan 2022 and 1 Apr 2024 (press reports); whether a domestic FoF uses your LRS limit; Franklin Templeton SAT stay and ₹250 cr escrow (FT disclosure only) | international funds, segregated portfolios | 20, 24 Oct | press / company disclosure |
| SEBI → AMFI stress-test direction dated 27 Feb 2024 (an AMC policy document); "at least one SAT appeal succeeded" (SCC Online); SBI FD rates FY16–FY22 (messy SBI workbook, 4 cross-checked); deposit insurance (DICGC) and IRDAI rules left out | liquidity risk, broker risk, inflation, insurance | 17–23 Oct | secondary |
| SGB early redemption after year five losing the exemption (no official clarification); clubbing "income on income" and loans to a spouse (case law); TRC form number under the new Rules | bonds and SGBs, gifts and clubbing, NRI basics | 1–4 Dec | case law / unconfirmed |

Also: eyeball the four TA module 2 charts (`assets/charts/ta2-*.svg`) in a
browser — never rasterised locally.

## Open — content and tooling

- **Tooling PR follow-ups (Oct 2026):** the new skills, `post-auditor` agent,
  `pr-checks.yml` workflow and three scheduled tasks are inventoried in
  `.claude/README.md`. After the PR merges: (1) check the first **PR checks**
  run is green (workflow files can be refused by token scope — if so, add the
  file by hand in GitHub); (2) attach the repo to the three scheduled tasks in
  the Claude routines UI if a fired session shows no checkout; (3) run
  `verify-claims` on the VERIFY table below, starting with the superseded MF
  citations; (4) the Google Sheet calculators below can now start from the
  `build-calculator` specs.

- **Google Sheet calculators (3):** DCF (terminal value post, 30 Sep — its
  placeholder comment was removed, but the sheet is still owed), rolling
  returns (27 Sep) and SIP/XIRR (1 Oct) — search `_posts/` for
  `GOOGLE-SHEET-TODO`. View-only, "make a copy to use"; link from each post.
- **Superseded MF citations in existing posts:** SEBI's Master Circular for
  Mutual Funds (27 Jun 2024) and the 1996 MF Regulations were replaced from
  1 Apr 2026 (new Master Circular 20 Mar 2026; SEBI (Mutual Funds)
  Regulations, 2026). The new module-3 posts cite the new ones; older MF posts
  (notably SEBI fund categories, 14 Oct, and its clause numbers) still cite the
  old — update before they publish.
- **Two USD/INR series:** `usd-inr-reference-rate.csv` (RBI/FBIL; currency
  risk, 19 Oct) and `usd-inr-fred-dexinus.csv` (Fed H.10; international funds,
  20 Oct) differ slightly. Consider standardising on the RBI/FBIL series.
- **Links into the held Tax series (14 `RELINK` markers)** were turned into plain text so the
  other series aren't blocked (F&O numbers; YTM; modified duration; exit load;
  debt funds explained; index funds vs ETFs; STP and SWP). Each carries a
  hidden `<!-- RELINK <target> -->` marker right after the text — once Tax is
  live (or rescheduled earlier than the linking post), turn each back into
  `[text]({% post_url <target> %})`: `grep -rn "RELINK" _posts`.
- **Links owed once targets publish — swept 25 Oct for every live target.** 42
  links added in 35 posts: each "later in this series" promise whose target was
  live now links to it, plus links into the posts Search Console listed as
  "Crawled – currently not indexed" (record date, bid-ask spread, T+1, Kelly,
  backtesting, Fibonacci, liquidity risk, STP/SWP, bank P/B) and the jargon terms
  first explained inline (beta, operating leverage, earnings yield, payout ratio,
  enterprise value, portfolio overlap, exit load). **Rule used:** a post links an
  *earlier* post with `{% post_url %}`; it links a *later* post only once that
  post is live, with a plain relative link (`{{ '/YYYY/MM/DD/slug/' | relative_url }}`)
  — `post_url` to a later post breaks the build, and live URLs never change.
  Still owed (targets not live yet): the Tax series (RELINK markers, after
  4 Dec), Module 4 MF posts (after 7 Nov), and the F&O post's tax-series
  pointer. Re-run the sweep with
  `grep -rn "later in this series\|covered later\|coming up" _posts`.
- **TA module 1 charts have no generator in the repo** (`assets/charts/ta-*.svg`;
  the script was left in a session scratchpad). Recreate it as
  `scripts/make_ta_charts.py` from the Britannia CSV — and redraw `ta-rsi.svg`,
  which predates the switch to Wilder-seeded RSI (differs only in the first
  month shown).
- **Terminal value post, "aggressive" case (₹753):** can't be reproduced from
  `_data/case_study.yml`. Derive it in a script with stated margin/capex
  assumptions, or drop it.
- **Prose numbers still typed by hand** (should come from `_data/risk.yml` /
  `mf.yml`): arithmetic of losses ("about 66% more", "nearly three percentage
  points"), diversification ("1.6 / 0.4 percentage points", "15% less"),
  sequence of returns ("₹24/₹27 lakh", "₹2.6 crore", incl. its description),
  position sizing ("26% decline").
- **Module 4 data and sources (added 25 Oct 2026):** `assets/data/nifty50-tri.csv`
  is the Nifty 50 **total return index** (NSE Indices' historical-data service,
  fetched 25 Oct 2026, 2006-01-02 to 2026-03-30; checked against the price
  index: daily-return correlation 0.99993, TRI beats PRI by ~1.3 points a year).
  The benchmarks, alpha and tracking-error posts still use the price index —
  they can now be redone against the TRI. `assets/data/uti-liquid-fund-nav.csv`
  is UTI Liquid Fund regular growth (AMFI via mfapi.in, code 102012). The
  **SEBI Master Circular for Mutual Funds of 20 March 2026** (HO/24/13/11(1)2026-IMD-POD-1/I/7602/2026)
  was downloaded from sebi.gov.in and read in full for the new posts: it
  supersedes older MF citations (see "Superseded MF citations" above).
- **Correction made to a live post:** *Reading a factsheet* (11 Oct) said
  trading costs "sit outside the expense ratio"; Master Circular para 11.2.4(a)
  puts brokerage and transaction costs inside the TER (only market impact is
  outside). Fixed on 25 Oct with `last_modified_at`. Other older posts that
  discuss TER composition may carry the same pre-2026 wording: `grep -rn "outside the expense ratio\|not in the TER" _posts`.
- **Owed links from Module 4 (targets are later-dated, so earlier posts can't
  link yet — sweep after 7 Nov):** factsheet (11 Oct) → *portfolio turnover
  ratio* (its text says "a later post covers it"); *volatility and Sharpe*
  (30 Sep) → *Sortino and information ratio*; benchmarks (2 Oct) and star
  ratings (16 Oct) → *survivorship bias*; tracking error (4 Oct) →
  *Sortino and information ratio*; STP and SWP (17 Oct) → *liquid and
  overnight funds*; *growth vs IDCW* → the Tax series' *dividends and
  interest* (now 21 Nov, held) once the Tax read is done.
- **Module 4 VERIFY / judgement calls:** (1) the ETF payout of 25 Feb 2021
  (₹40.89/unit) is an *estimate* from the NAV gap, as in `mf2.yml`; the post
  says so. (2) Capture ratios use the Nifty 50 TRI for a hybrid fund that does
  not track it — the post says so; a hybrid-category TRI benchmark would be
  the like-with-like choice. (3) The survivorship simulation's closing rule
  (worst 10% by trailing 3-year return, years 3–9) is an assumption; no real
  closure rate is quoted. (4) Market-impact assumptions (0.05/0.10/0.20% a
  side) are illustrative. No tax rate or tax rule is stated in any Module 4
  post, so no professional read is needed.
- **Index data source:** Britannia prices and the Nifty 50 price index come
  from Yahoo Finance. The Nifty 50 TRI is now in the repo (see the Module 4
  bullet above), so the benchmarks, alpha and tracking-error posts can be
  redone against the right index.
- **Glossary coverage:** 11 opener/closer posts have no `term:` (by design —
  `check_posts.py` warns). Add one if you want a post in `/glossary/`.

---

## Reference — how this repo works

### Build and publish
- Pages deploys via GitHub Actions (`.github/workflows/pages.yml`), daily at
  09:00 IST, with `future: false` — a post goes live on its date with no manual
  step. Keep post times at or before `09:00:00 +0530` or they miss that day's
  build.
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
  `docker run --rm -v "$PWD":/site -w /site -v wp-bundle:/usr/local/bundle ruby:3.3 bash -c "bundle install -q && bundle exec jekyll build --future"`
  In the Claude cloud session Ruby 3.3 and the gems are already installed (but `bundle exec`
  and `jekyll` aren't on PATH): `ruby $(gem env gemdir)/gems/jekyll-4.4.1/exe/jekyll build --future -d /tmp/site`
  builds in ~5 seconds (`--future` includes the scheduled posts).
- Python scripts need a venv with pandas, numpy, pyyaml, matplotlib, pillow.
  Re-running a chart script rewrites every SVG it owns with new random ids —
  revert the ones whose only diff is ids.
- minima's SCSS prints Dart-Sass deprecation warnings (`lighten()`); harmless.

### Data discipline
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

### The Desi Bites case study
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

### Site features
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

---

## History

- Aug–Sep 2026: 69 posts across Jargon (M0–M5), FA (8), TA (10), MF (9) and
  Tax (9); then R1–R7 added 47 more (Risk series, FA "Reading between the
  lines" and "Banks and NBFCs", Jargon module 6, MF module 2, tax add-ons,
  TA module 2). Posts were rescheduled into a daily cadence from 18 Aug.
- 24 Sep 2026: site redesign; Indian comma grouping in tables; full review of
  all 116 posts with every P0/P1/P2 fixed (`_review/REVIEW-2026-09-24.md`);
  `CLAUDE.md` updated with the lessons. Rescheduled the 88 unpublished posts
  to one per series per day (Tax held to 27 Oct).
- 25 Sep 2026: six new modules, 45 posts — Jargon 7 market mechanics, FA 4
  sector lenses, TA 3 honest tests, MF 3, Risk 2, Tax 3 add-ons — continuing
  each series daily to 21–25 Oct (Tax 9–13 Nov).
- Details of any change: `git log`.
