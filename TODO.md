# TODO

Current state (25 Sep 2026): **161 posts written and scheduled** across six
series (Jargon 53 · FA 29 · TA 22 · MF 23 · Tax 18 · Risk 16). The cadence is
**one post per series per day**. Scheduled through: Jargon 21 Oct · FA 23 Oct
· TA 23 Oct · Risk 23 Oct · MF 25 Oct · **Tax held** 27 Oct → 13 Nov pending
its professional read. **The written backlog runs out after 25 Oct** (Tax
after 13 Nov) — the next module per series needs approving by about 10 Oct. All posts were reviewed and every P0/P1/P2 finding
fixed — see `_review/REVIEW-2026-09-24.md`. House style and the rules every
post must follow are in `CLAUDE.md`; this file is for what's still open and
for how the repo works.

---

## Open — needs you

- **Newsletter:** `newsletter.action` in `_config.yml` is empty, so the signup
  box renders nothing. Mailchimp or Buttondown — three config keys; setup notes
  in `_includes/newsletter.html`.
- **Comments (giscus):** `giscus.repo_id` and `giscus.category_id` are empty.
  Enable Discussions on the repo, create an "Announcement"-type category named
  "Comments", install https://github.com/apps/giscus, then copy both ids from
  https://giscus.app (mapping: pathname). Notes in `_includes/comments.html`.
  Enforce the moderation note (no tips, no targets, no "should I buy X").
- **Tax series professional read** — all 13 tax posts, held at 27 Oct →
  8 Nov (daily). The rules were re-checked against primary sources where
  reachable, but someone who files professionally should read them before
  they publish. `_data/tax2.yml` lists the recorded disagreements. Once
  reviewed, the tax posts can move earlier (rename the files; keep one per day
  and check `scripts/check_posts.py`) — and restore the nine RELINK links below.
- **Next content (approve a roadmap):** at one post per series per day the
  backlog runs dry after 25 Oct (Tax 13 Nov). Pick the next module for each
  series by ~10 Oct so it can be written and checked in time.
- **Desi Bites' public float:** the fictional IPO left 20% public, below the
  real 25% minimum public shareholding. The market-mechanics posts (free float,
  18 Oct; OFS and delisting, 20 Oct) say so and use it as the teaching example.
  Alternative: raise the IPO float in the case-study data (ripples through
  every Desi Bites per-share figure). Decide which.
- **About page avatar** — photo, illustration, or an SVG monogram?
- **Decisions, whenever:** R8 personal-finance track ("Money Before Markets":
  emergency fund, EPF/PPF/NPS, term insurance vs ULIP, FDs vs debt funds, real
  returns; plus bonds/G-secs, REITs/InvITs) — widen the blog's scope or not? ·
  A real peer table for the comparables post (Nestlé India, Tata Consumer…,
  each sourced from its own filing) · MathJax/KaTeX for formulas instead of
  code blocks.

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
| Liquid-fund graded exit load in the first week | STP and SWP | 17 Oct | memory, stated qualitatively |
| Index-futures margins "low-to-mid teens" | leverage and margin | 11 Oct | hedged ("check NSE's margin files") |
| 29 Aug 2024 intermediaries amendment "left room" for education | how finfluencers make money | 15 Oct | secondary sources |
| Tax, from memory: property's 12.5%/20% option; business filers' one-time switch back to the new regime; CBDT condoning late filing; GAAR on round-trips; old 80C → section 123 | several tax posts | 27 Oct → 8 Nov | memory / secondary (incometaxindia.gov.in returns 403) |
| Buyback Regime C: ₹1.25 lakh exemption, promoter definition, timing; foreign shares' exchange-rate convention | buyback taxation, foreign stocks | 6, 8 Nov | recorded as disagreements in `tax2.yml` |
| Ex-date = record date under T+1 (inferred from NSE corporate-actions data); rights-issue rules "from April 2025" (7 or 8 April); OFS framework's current master circular; T+0 rollout status | T+1, record/ex-date, rights issues, OFS | 16–20 Oct | NSE data / secondary |
| GSM stage mechanics ("buyer pays in full plus deposit" is inferred); "not an adverse action" confirmed only for ASM/ESM; GSM criteria after May 2026 | ASM and GSM surveillance | 21 Oct | NSE FAQs + inference |
| Attributions: Lane (stochastic), Granville (OBV); papers cited without fetching (Bouman & Jacobsen 2002; Moskowitz, Ooi & Pedersen 2012; Jegadeesh & Titman 1993); NSE closing auction live from 3 Aug 2026 | TA honest-tests posts | 16–23 Oct | memory / citation not fetched |
| USFDA NAI/VAI/OAI meanings, Form 483 → warning letter chain (fda.gov blocked); embedded value definition; Airtel net debt incl. leases (inferred); Bajaj Finance ALM gap limits (from its presentation, not RBI) | sector-lens posts | 20–23 Oct | secondary / inference |
| Overseas-investment halts of Jan 2022 and 1 Apr 2024 (press reports); whether a domestic FoF uses your LRS limit; Franklin Templeton SAT stay and ₹250 cr escrow (FT disclosure only) | international funds, segregated portfolios | 20, 24 Oct | press / company disclosure |
| SEBI → AMFI stress-test direction dated 27 Feb 2024 (an AMC policy document); "at least one SAT appeal succeeded" (SCC Online); SBI FD rates FY16–FY22 (messy SBI workbook, 4 cross-checked); deposit insurance (DICGC) and IRDAI rules left out | liquidity risk, broker risk, inflation, insurance | 17–23 Oct | secondary |
| SGB early redemption after year five losing the exemption (no official clarification); clubbing "income on income" and loans to a spouse (case law); TRC form number under the new Rules | bonds and SGBs, gifts and clubbing, NRI basics | 10–13 Nov | case law / unconfirmed |

Also: eyeball the four TA module 2 charts (`assets/charts/ta2-*.svg`) in a
browser — never rasterised locally.

## Open — content and tooling

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
- **Privacy page wording:** `privacy.markdown` line 15 says the 3-month lag is
  "per SEBI's guidance". Since the SEBI circular of 8 May 2026 (30 days from
  1 Jul 2026) it is our stricter house rule — reword to match `CLAUDE.md`.
- **Nine links into the held Tax series** were turned into plain text so the
  other series aren't blocked (F&O numbers; YTM; modified duration; exit load;
  debt funds explained; index funds vs ETFs; STP and SWP). Each carries a
  hidden `<!-- RELINK <target> -->` marker right after the text — once Tax is
  live (or rescheduled earlier than the linking post), turn each back into
  `[text]({% post_url <target> %})`: `grep -rn "RELINK" _posts`.
- **Links owed once targets publish.** Posts can only `post_url` earlier-dated
  posts, so several explain a term inline and name its post in plain text
  ("later in this series"). After the target's date the link becomes safe to
  add — e.g. jargon module 6 terms (beta, operating leverage, earnings
  yield, payout ratio, enterprise value) are explained inline in earlier FA
  posts; capex intensity in the free cash flow post; the portfolio-overlap,
  exit-load and STP/SWP posts from risk posts. Sweep once everything is live
  (after 8 Nov):
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
- **Index data source:** Britannia prices and the Nifty 50 price index come
  from Yahoo Finance. A Nifty 50 TRI series (niftyindices.com) would let the
  benchmarks, alpha and tracking-error posts show tracking difference against
  the right index.
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
- **Analytics:** GA4 is live (`G-LYRDRDQSE8`, Google Signals and ads
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
