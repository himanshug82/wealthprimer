# TODO

Current state (25 Oct 2026): **168 posts written** across six series (Jargon 53 · FA 29 · TA 22 · MF 30 · Tax 18 · Risk 16), one post per series per day (MF Module 4 every other day). Scheduled through: Jargon 21 Oct · FA, TA, Risk 23 Oct · MF 7 Nov · Tax 4 Dec (starts 17 Nov). **Every series except MF and Tax has run out of written posts.** House style and the rules every post must follow are in `CLAUDE.md`; this file is for what's still open and for how the repo works.

---

## Open — needs you

- **Next content.** Every series needs its next module planned and approved with `plan-module`. Two inputs are waiting:
  - **Money Before Markets — Module 1: 7 of 8 posts drafted (25 Oct 2026); EPF pending.** Series `money-before-markets`, one post a day from 8 Nov, `planned: 7` until EPF lands (then 8). Written: 8 Nov `emergency-fund-sizing`; 9 Nov `fixed-deposit-vs-debt-fund`; 10 Nov `g-secs-and-t-bills`; 11 Nov `ppf-how-it-works`; 13 Nov `nps-exit-rules` (retitled from "NPS explained": it covers exit and withdrawal rules only); 14 Nov `ulip-charges`; 15 Nov `reit-structure` (retitled: REITs only; InvITs are not covered). **The 12 Nov slot is empty: EPF (`epf-how-it-works`) is not written** because every EPFO page and PDF returned 404 (epfindia.gov.in and epfo.gov.in). What is confirmed for it: PIB press release of 2 Mar 2026 — the 239th Central Board of Trustees meeting recommended 8.25% for FY 2025-26, to be officially notified by the Government before EPFO credits it. Not confirmed from a primary source (so not stated): contribution rates, the employer/pension split, withdrawal and transfer rules, how interest accrues and is credited, the notified rate. Needed from the owner or a reachable copy: the EPF Scheme, 1952 (paras on contributions, interest at para 60, withdrawals), the EPFO circular notifying the FY 2025-26 rate, and EPFO's table of declared rates. The `post-auditor` reviewed the seven written posts on 25 Oct 2026 (1 P0, 10 P1, 12 P2); all fixed except the open verifications below. All posts avoid stating tax rules, so none carries `needs_review: tax`; the tax treatment of PPF, EPF, NPS and ULIP payouts belongs in the Tax series. Data in `scripts/derive_mbm.py` → `_data/mbm.yml`. "Real return" stays with the Risk series; bond and REIT *tax* stay with Tax. Owed links from these posts to the Tax series (*dividends and interest* 21 Nov, *REITs and InvITs* 30 Nov, *bonds, debentures and SGBs* 1 Dec): add plain relative links once those are live; the Tax REIT post can `post_url` to `reit-structure`. Optional 9th post (corporate bonds and credit ratings) not planned.
  - **Your first year in the market (`market-basics`) — Module 1 approved 25 Oct 2026; series scaffolded, posts not yet written.** Housing rules approved: extend an existing series where a topic fits; a new series only with at least 5 named posts and a distinct reader question; everything else to a catch-all `explainers` series, created when its first post is approved. 7 posts, one a day, **1 → 7 Dec 2026**: (1) 1 Dec `demat-trading-bank-accounts`; (2) 2 Dec `nomination-demat-folios`; (3) 3 Dec `order-types-explained`; (4) 4 Dec `contract-note-charges` (carries `needs_review: tax` + `rules_as_of`; no professional read, by owner decision); (5) 5 Dec `ipo-application-asba-upi` (Desi Bites IPO as the example; add any missing IPO facts to `_data/case_study.yml` or its script first); (6) 6 Dec `scores-and-smart-odr`; (7) 7 Dec `mergers-and-demergers` (illustrative companies, no real demerger). Overlaps handled: post 1 links to *broker and counterparty risk* rather than re-explaining custody; post 3 owns "Order types" but not the "Stop-loss" term (TA post); tax treatment stays in Tax. **Primary sources to open before drafting:** SEBI nomination circular of 29 May 2026 on sebi.gov.in (only an NSDL copy was read); NSE order-type rules; NSE circular NSE/FATAX/73524 plus SEBI turnover fee, exchange transaction charges, GST on charges and stamp duty on securities; SEBI ICDR master circular chapters on UPI/ASBA and T+3 (the ₹5 lakh UPI limit and unblocking days are UNVERIFIED); NSE ODR page and SEBI's SCORES and SMART ODR circulars (timelines disputed); BSDA limits (NSDL blocked — state only what is confirmed). Not planned: option basics (Risk, next module), SIF (MF, blocked on SEBI text), reading a consolidated account statement (optional). A Search Console export was skipped for now. Data in `scripts/derive_mb.py` → `_data/market_basics.yml`.
- **SEO content follow-ups.** (1) Add primary-source links (SEBI circulars, AMFI data, company filings) to the 41 posts with no external links. (2) Monthly: export Search Console queries at position 8–20, refresh those posts (`refresh-post`), and set `last_modified_at` only for substantive changes. (3) Watch Pages (published posts indexed), Sitemaps (status Success), Enhancements → Breadcrumbs (valid items ≈ number of posts) and Core Web Vitals (no CLS issues). Leave dated URLs alone — no redirect plugin, so renaming breaks links.

## Open — verify claims

Each of these is in a post today, worded cautiously, but rests on a secondary source or on memory. Most of the October posts are already live; Tax and Module 4 are still ahead. Confirm from the primary source, then tighten the wording (or correct it); `verify-claims` does this. Separately: the STP and SWP post's liquid-fund exit-load wording is now confirmed against the SEBI Master Circular (20 Mar 2026) para 5.6.5 — tighten it if it states more than "an exit load applies for exits within 7 calendar days; the scale is AMFI's".

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
| Index-futures margins "low-to-mid teens" | leverage and margin | 11 Oct | hedged ("check NSE's margin files") |
| 29 Aug 2024 intermediaries amendment "left room" for education | how finfluencers make money | 15 Oct | secondary sources |
| DICGC's ₹5 lakh limit: the guide page states it but gives no effective date; the 4 Feb 2020 date and the payout timing are not read from a primary page | FD vs debt fund | 9 Nov | DICGC guide (primary), dates unconfirmed |
| Retail Direct minimum bid ₹10,000 is printed "as on 12 Nov 2021"; current minimum, bid caps and the T-bill/G-sec tenors are RBI pages dated 2020–21 | G-secs and T-bills | 10 Nov | RBI FAQs (primary, old) |
| PPF: the rules read are the notification of 12 Dec 2019 (G.S.R. 915(E)); later amendments to the Scheme were not read. NSI's rate table is a selection in the post | PPF | 11 Nov | India Post PDF (primary, original text) |
| NPS exit rules read from the Gazette of 12 Dec 2025 and PFRDA's March 2026 FAQ; the 13 Jul 2026 amendment read (specific-purpose schemes only). Tier-I/Tier-II, asset classes and annuity terms not covered | NPS exit rules | 13 Nov | primary |
| ULIP: IRDAI's life-products master circular of 12 Jun 2024 (reviewed yearly: a later version may exist); the charge caps in Schedule I of the Insurance Products Regulations, 2024 were NOT read | ULIP charges | 14 Nov | primary circular; Schedule I unread |
| REIT: SEBI's published regulations text carries amendments only to 30 Nov 2016; the master circular and later amendments (including the 2024–25 changes to holdco distribution) were NOT read; 25% public holding and listing thresholds not stated | REIT structure | 15 Nov | primary, dated |
| Tax, from memory: property's 12.5%/20% option; business filers' one-time switch back to the new regime; CBDT condoning late filing; GAAR on round-trips; old 80C → section 123 | several tax posts | 17 Nov → 4 Dec | memory / secondary (incometaxindia.gov.in returns 403) |
| Buyback Regime C: ₹1.25 lakh exemption, promoter definition, timing; foreign shares' exchange-rate convention | buyback taxation, foreign stocks | 27, 29 Nov | recorded as disagreements in `tax2.yml` |
| Ex-date = record date under T+1 (inferred from NSE corporate-actions data); rights-issue rules "from April 2025" (7 or 8 April); OFS framework's current master circular; T+0 rollout status | T+1, record/ex-date, rights issues, OFS | 16–20 Oct | NSE data / secondary |
| GSM stage mechanics ("buyer pays in full plus deposit" is inferred); "not an adverse action" confirmed only for ASM/ESM; GSM criteria after May 2026 | ASM and GSM surveillance | 21 Oct | NSE FAQs + inference |
| Attributions: Lane (stochastic), Granville (OBV); papers cited without fetching (Bouman & Jacobsen 2002; Moskowitz, Ooi & Pedersen 2012; Jegadeesh & Titman 1993); NSE closing auction live from 3 Aug 2026 | TA honest-tests posts | 16–23 Oct | memory / citation not fetched |
| USFDA NAI/VAI/OAI meanings, Form 483 → warning letter chain (fda.gov blocked); embedded value definition; Airtel net debt incl. leases (inferred); Bajaj Finance ALM gap limits (from its presentation, not RBI) | sector-lens posts | 20–23 Oct | secondary / inference |
| Overseas-investment halts of Jan 2022 and 1 Apr 2024 (press reports); whether a domestic FoF uses your LRS limit; Franklin Templeton SAT stay and ₹250 cr escrow (FT disclosure only) | international funds, segregated portfolios | 20, 24 Oct | press / company disclosure |
| SEBI → AMFI stress-test direction dated 27 Feb 2024 (an AMC policy document); "at least one SAT appeal succeeded" (SCC Online); SBI FD rates FY16–FY22 (messy SBI workbook, 4 cross-checked); deposit insurance (DICGC) and IRDAI rules left out | liquidity risk, broker risk, inflation, insurance | 17–23 Oct | secondary |
| SGB early redemption after year five losing the exemption (no official clarification); clubbing "income on income" and loans to a spouse (case law); TRC form number under the new Rules | bonds and SGBs, gifts and clubbing, NRI basics | 1–4 Dec | case law / unconfirmed |

Also: eyeball the four TA module 2 charts (`assets/charts/ta2-*.svg`) in a browser — never rasterised locally.

## Open — content and tooling

- **Tooling follow-ups.** Attach the repo to the three scheduled tasks in the Claude routines UI if a fired session shows no checkout (inventory in `.claude/README.md`); run `verify-claims` on the table above.
- **Google Sheet calculators (3):** DCF (terminal value post, 30 Sep — the sheet is still owed), rolling returns (27 Sep) and SIP/XIRR (1 Oct). Search `_posts/` for `GOOGLE-SHEET-TODO`. View-only, "make a copy to use"; link from each post. The `build-calculator` skill can write the specs.
- **Superseded MF citations.** SEBI's Master Circular for Mutual Funds (27 Jun 2024) and the 1996 MF Regulations were replaced from 1 Apr 2026 (Master Circular 20 Mar 2026; SEBI (Mutual Funds) Regulations, 2026). `_data/mf2.yml` line 310 still cites the 27 June 2024 circular (clause 2.6) for the *SEBI fund categories* post (14 Oct) — update it to the new Master Circular's clause (the new citation is already in `mf3.yml`).
- **Two USD/INR series:** `usd-inr-reference-rate.csv` (RBI/FBIL; currency risk, 19 Oct) and `usd-inr-fred-dexinus.csv` (Fed H.10; international funds, 20 Oct) differ slightly. Consider standardising on the RBI/FBIL series.
- **Benchmarks, alpha and tracking-error posts** still use the Nifty 50 *price* index (Yahoo Finance). The Nifty 50 total return index is now in the repo (`assets/data/nifty50-tri.csv`, NSE Indices, 2006-01-02 to 2026-03-30; TRI beats PRI by about 1.3 points a year), so they can be redone against the right index.
- **Links owed once targets publish.**
  - Tax series (14 `RELINK` markers, after 4 Dec): these links were turned into plain text so other series weren't blocked. Each carries a hidden `<!-- RELINK <target> -->` marker; turn each back into `[text]({% post_url <target> %})` (`grep -rn "RELINK" _posts`). Also the F&O post's tax-series pointer.
  - Module 4 MF posts (sweep after 7 Nov): factsheet (11 Oct) → *portfolio turnover ratio*; *volatility and Sharpe* (30 Sep) and tracking error (4 Oct) → *Sortino and information ratio*; benchmarks (2 Oct) and star ratings (16 Oct) → *survivorship bias*; STP and SWP (17 Oct) → *liquid and overnight funds*; *growth vs IDCW* → the Tax series' *dividends and interest*.
  - **Rule:** a post links an *earlier* post with `{% post_url %}`; it links a *later* post only once that post is live, with a plain relative link (`{{ '/YYYY/MM/DD/slug/' | relative_url }}`). Re-run the sweep with `grep -rn "later in this series\|covered later\|coming up" _posts`.
- **TA module 1 charts have no generator in the repo** (`assets/charts/ta-*.svg`; the script was left in a session scratchpad). Recreate it as `scripts/make_ta_charts.py` from the Britannia CSV, and redraw `ta-rsi.svg`, which predates the switch to Wilder-seeded RSI (differs only in the first month shown).
- **Terminal value post, "aggressive" case (₹753):** the value is typed by hand in `_data/case_study.yml` (`scenario_aggressive`) and can't be reproduced from the other data. Derive it in a script with stated margin/capex assumptions, or drop it.
- **Prose numbers still typed by hand** (should come from `_data/risk.yml` / `mf.yml`): arithmetic of losses ("about 66% more", "nearly three percentage points"), diversification ("1.6 / 0.4 percentage points", "15% less"), sequence of returns ("₹24/₹27 lakh", "₹2.6 crore", incl. its description), position sizing ("26% decline").
- **Module 4 judgement calls to revisit:** (1) the ETF payout of 25 Feb 2021 (₹40.89/unit) is an *estimate* from the NAV gap, as in `mf2.yml`; the post says so. (2) Capture ratios use the Nifty 50 TRI for a hybrid fund that does not track it — a hybrid-category TRI benchmark would be the like-with-like choice. (3) The survivorship simulation's closing rule (worst 10% by trailing 3-year return, years 3–9) is an assumption. (4) Market-impact assumptions (0.05/0.10/0.20% a side) are illustrative.

## Parked — revisit later

- **Company analysis series** (parked 26 Oct): conflicts with the no-verdicts rule; skills and the research agent won't propose it.
- **Newsletter:** `newsletter.action` in `_config.yml` is empty, so the signup box renders nothing. Mailchimp or Buttondown — three config keys; notes in `_includes/newsletter.html`.
- **Comments / giscus** (moderating "should I buy X" questions is a compliance load): `giscus.repo_id` and `giscus.category_id` are empty, so nothing renders. Notes in `_includes/comments.html`.

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
  `docker run --rm -v "$PWD":/site -w /site -v wp-bundle:/usr/local/bundle ruby:3.3 bash -c "bundle install --quiet && bundle exec jekyll build --future"`
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

- Details of any change: `git log`.
