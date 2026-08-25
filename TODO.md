Resolved

- Domain: confirmed dummynotes.com is correct.
- Twitter/X handle, author name, LinkedIn, contact email: filled in (see _config.yml, about.markdown, privacy.markdown).
- Favicon, header logo, social share image: done (see assets/, _includes/head.html, _includes/header.html).

Still open

- Avatar/photo for the About page — external AI-generated image, or an SVG monogram placeholder?

Jargon, Decoded — case study & roadmap

- Case study: Desi Bites Foods Pvt Ltd (fictional snacks/namkeen manufacturer),
  3-year reconciled financial model. Data: _data/case_study.yml. Reference page:
  /case-study/ (case-study.markdown). Every ratio post should link there for the
  numbers instead of re-pasting statements.
- Real-world anchor company for the "real example" half of each post:
  Britannia Industries (NSE: BRITANNIA, BSE: 500825) — confirmed. Numbers
  sourced from the official audited consolidated FY25 results filing (year
  ended 31 March 2025, filed with NSE/BSE 8 May 2025), not secondary
  aggregators: _data/real_company.yml, cited with the source URL. Well past
  the SEBI 3-month lag rule in CLAUDE.md.
- Per-post structure for this series: definition -> formula -> Desi Bites
  walkthrough (fictional, always current) -> real-company walkthrough (real,
  lagged data) -> common mistakes -> takeaway.
- Roadmap, 33 posts across 6 modules (M1-M4 are independent of each other once
  M0 exists; M5 depends on a hypothetical "Desi Bites goes public" narrative
  beat introduced in that module):
  - M0 Foundations (4): Meet Desi Bites (series-opener post, links to
    /case-study/) - Reading a Balance Sheet - Reading a P&L - Reading a Cash
    Flow Statement
  - M1 Profitability (6): Gross Margin - EBITDA Margin - Net Margin - ROE -
    ROCE - ROA
  - M2 Efficiency / Working Capital (5): Inventory Days - Debtor Days -
    Creditor Days - Cash Conversion Cycle - Asset Turnover
  - M3 Leverage / Solvency (7): Net Working Capital - Current Ratio - Quick
    Ratio - Debt-to-Equity - Equity Multiplier - Interest Coverage - Net
    Debt/EBITDA
  - M4 Cash Flow Quality (3): Free Cash Flow - OCF/PAT (earnings quality) -
    Capex Intensity
  - M5 Valuation / Market (8, needs the hypothetical listing beat): Book Value
    per Share - EPS - P/E - P/B - EV/EBITDA - Market Cap - Dividend Yield - PEG
- Moved to the Fundamental Analysis series instead of Jargon, Decoded (these
  combine multiple ratios rather than defining one, and DuPont specifically
  needs Net Margin + Asset Turnover + Equity Multiplier to already exist as
  Jargon posts to link to): DuPont ROE Decomposition, and eventually a capstone
  post applying the whole toolkit to a real stock end-to-end.
- M0 reviewed and scheduled (moved to _posts/): meet-desi-bites-foods
  (2026-08-18, live), reading-a-balance-sheet (2026-08-20),
  reading-an-income-statement (2026-08-22), reading-a-cash-flow-statement
  (2026-08-24) — staggered a few days apart, auto-publishing via the daily
  Pages rebuild. All Desi-Bites-only, no real-company data needed for these
  four.
- M1 reviewed and scheduled (moved to _posts/): gross-margin (2026-08-26),
  ebitda-margin (2026-08-28), net-margin (2026-08-30), roe (2026-09-01),
  roce (2026-09-03), roa (2026-09-05) — staggered a few days apart, same
  cadence as M0. Each pairs a Desi Bites walkthrough with a cited Britannia
  FY25 walkthrough from _data/real_company.yml.
- M2 reviewed and scheduled (moved to _posts/): inventory-days (2026-09-07),
  debtor-days (2026-09-09), creditor-days (2026-09-11),
  cash-conversion-cycle (2026-09-13), asset-turnover (2026-09-15) —
  staggered a few days apart, same cadence as M0/M1. Notable real finding:
  Britannia's cash conversion cycle is negative (-8.6 days) — it collects
  from customers and turns inventory faster than it pays its own suppliers.
  No new research needed — used the inventory/receivables/payables already
  in _data/real_company.yml.
- M3 reviewed and scheduled (moved to _posts/): net-working-capital
  (2026-09-17), current-ratio (2026-09-19), quick-ratio (2026-09-21),
  debt-to-equity (2026-09-23), equity-multiplier (2026-09-25),
  interest-coverage (2026-09-27), net-debt-ebitda (2026-09-29) —
  staggered a few days apart, same cadence as M0-M2. Notable real finding:
  Britannia is in a net CASH position (Net Debt/EBITDA of -0.06x) — more
  cash and liquid investments than borrowings. Added
  total_current_assets/total_current_liabilities/cash_and_bank/
  current_investments to real_company.yml, and
  net_working_capital/equity_multiplier/net_debt_ebitda to case_study.yml.
- M4 reviewed and scheduled (moved to _posts/): free-cash-flow
  (2026-10-01), ocf-pat (2026-10-03), capex-intensity (2026-10-05) —
  staggered a few days apart, same cadence as M0-M3. This closes out the
  Jargon, Decoded ratio roadmap (M0-M4); only M5 (Valuation/Market, 8
  posts) remains, and it needs the hypothetical "Desi Bites goes public"
  narrative beat first. Notable real finding: Britannia's FCF rose FY24 to
  FY25 mainly because capex fell (3.3% to 2.1% of revenue), not because
  operating cash generation improved — worth remembering before assuming a
  rising FCF is automatically an operating improvement. Added a
  cash_flow: block (cfo, capex) to real_company.yml, and
  ocf_pat/capex_intensity to case_study.yml's ratios.
- M5 reviewed and scheduled (moved to _posts/): book-value-per-share
  (2026-10-07), eps (2026-10-09), price-to-earnings (2026-10-11),
  price-to-book (2026-10-13), ev-ebitda (2026-10-15), market-cap
  (2026-10-17), dividend-yield (2026-10-19), peg-ratio (2026-10-21) —
  staggered a few days apart, same cadence as M0-M4. **This completes the
  entire 33-post Jargon, Decoded roadmap (M0-M5).**
  - "Desi Bites goes public" narrative (user-decided): fresh-issue IPO on
    NSE Emerge, listed 15 June 2025 off FY25 financials, priced off the
    fresh-issue dilution (undiluted vs diluted EPS deliberately kept
    distinct as a teaching point). Full terms in
    _data/case_study.yml's `listing:` block.
  - Britannia's real market data lives in _data/real_company.yml's
    `market:` block, separate from the financial-statement data — price
    is the NSE close on 30 June 2025 (source: Yahoo Finance historical
    data), dividend is the FY25 payout (source: stockanalysis.com),
    shares outstanding is derived (PAT/EPS) and cross-checked against
    reported share capital. This needed its own 3-month-lag check
    independent of the financial-statement lag already satisfied.
  - Notable real finding: Britannia's PEG ratio comes out to ~35.9 —
    absurd-looking, not because it's a bad business but because FY25 PAT
    growth was only ~1.8% (the margin-compression year from M1). Used
    deliberately in the PEG post as a live illustration of why PEG breaks
    down on single-year growth figures, rather than smoothed over.
Fundamental Analysis — Beginner to Expert — roadmap

- Scope decision: the statement-reading and ratio ground this series would
  normally cover is already done in Jargon, Decoded (M0-M5, 33 posts). So this
  series picks up where the ratios stop: synthesis (DuPont) and valuation
  (comparables, discounting, WACC, DCF, margin of safety), closing with a
  capstone that applies the whole toolkit end-to-end.
- Same two-company structure as Jargon, Decoded (Desi Bites for the fictional
  walkthrough, Britannia for the real one) with ONE deliberate exception: the
  DCF itself is built only on Desi Bites. A DCF that outputs an intrinsic
  value for a real listed stock reads as a price target, which CLAUDE.md's
  compliance guardrails rule out. Britannia still appears in these posts for
  observable inputs (its actual cost of debt, effective tax rate, FCF,
  multiples) — just never as the subject of a value-per-share output.
- Deviation from CLAUDE.md worth noting: CLAUDE.md says the DCF post should
  link out to a Jargon post on WACC. No such Jargon post exists and the
  Jargon roadmap is closed at M0-M5, so WACC is covered as FA-4 in this
  series instead, and the DCF posts link there.
- Data added for this module: `dupont:` and `dcf:` blocks in
  _data/case_study.yml (the DCF block holds assumptions, the FY26-FY30
  forecast, the result, a reverse-DCF, and a WACC x terminal-growth
  sensitivity grid); `dupont:` and `multiples:` blocks in
  _data/real_company.yml. No new external sourcing was needed — the DCF is
  built off figures already in the case study, and Britannia's multiples come
  from the already-cited FY25 filing plus the already-lag-checked 30 June 2025
  price.
- Roadmap, 8 posts, proposed dates on the same 2-day cadence as M0-M5:
  - FA-1 DuPont ROE decomposition (2026-10-23)
  - FA-2 Relative valuation: comparables and the peer set (2026-10-25)
  - FA-3 Discounting: what a future rupee is worth today (2026-10-27)
  - FA-4 Cost of capital: WACC (2026-10-29)
  - FA-5 Forecasting free cash flow (2026-10-31)
  - FA-6 Terminal value and the full DCF (2026-11-02)
  - FA-7 Margin of safety and sensitivity (2026-11-04)
  - FA-8 Capstone: Britannia end to end (2026-11-06)
- Notable finding baked into the module: the Desi Bites DCF values the share
  at Rs 398 against its Rs 640 IPO price — a 38% gap. Kept honestly rather
  than tuning assumptions to match the price (which is exactly the bad
  practice FA-7 warns about). It sets up the reverse-DCF beat: Rs 640 implies
  either a 9.6% perpetual growth rate, or roughly 25-30% revenue growth for
  five years with EBITDA margins expanding to ~20%.
- FA-1 to FA-8 reviewed and scheduled (moved to _posts/): dupont-roe-decomposition
  (2026-10-23), relative-valuation-comparables (2026-10-25),
  discounting-time-value-of-money (2026-10-27), wacc-cost-of-capital
  (2026-10-29), forecasting-free-cash-flow (2026-10-31),
  terminal-value-and-the-full-dcf (2026-11-02),
  margin-of-safety-and-sensitivity (2026-11-04),
  capstone-britannia-end-to-end (2026-11-06) — staggered a few days apart,
  same cadence as M0-M5. All intra-module links converted to {% post_url %}.
- IMPORTANT build rule learned while scheduling this module: a
  {% post_url %} pointing at a post whose date is still in the FUTURE does
  not merely 404 — it fails the ENTIRE Jekyll build ("Could not find post
  ... in tag 'post_url'"), because `future: false` keeps unpublished posts
  out of site.posts. So a post may only post_url a post dated on or BEFORE
  its own date. Forward references must be plain prose with no link.
  - This turned up four pre-existing posts that would have taken the live
    site down on their own publish dates, now fixed by dropping the link and
    keeping the prose: roe -> roce (would have broken 2026-09-01),
    interest-coverage -> net-debt-ebitda (2026-09-27), book-value-per-share
    -> price-to-book (2026-10-07), eps -> price-to-earnings (2026-10-09).
  - Guard for future modules: check every post_url target exists and is
    backward-dated, then simulate the build on each publish date (build with
    posts dated after that day temporarily moved aside). Both checks were run
    across all 41 posts and pass.
- Open item for this module: FA-6 calls for the Google Sheet DCF calculator
  that CLAUDE.md asks for. The draft ships a working Python/pandas snippet
  (which stands on its own) plus a placeholder for the Sheet link — the Sheet
  itself still needs to be built and shared view-only. Search the draft for
  GOOGLE-SHEET-TODO.
- Possible enhancement, not done: FA-2 teaches peer-set selection using only
  Desi Bites and Britannia, because adding a real peer table (Nestle India,
  Tata Consumer, etc.) means sourcing each peer's multiples from their own
  filings. Deliberately not faked. Say the word if you want that sourced.

Technical Analysis — Zero to Hero — roadmap

- Series arc follows CLAUDE.md exactly: candlesticks -> support/resistance ->
  trend lines -> moving averages -> volume -> RSI -> MACD -> chart patterns,
  opening with an honest framing post and closing with the honest reckoning
  on what TA cannot do.
- Data: real daily OHLCV for Britannia (NSE: BRITANNIA), the same anchor
  company as the other two series, so readers can connect the charts to the
  financials already in _data/real_company.yml.
  - Full series committed at assets/data/britannia-ohlcv-2024-04-to-2026-03.csv
    (495 daily bars, 1 Apr 2024 to 30 Mar 2026, no gaps). Source: Yahoo
    Finance historical data for BRITANNIA.NS.
  - Verified figures + the specific events each post is built on live in
    _data/ta.yml, all DERIVED from the CSV by script, not typed by hand.
  - LAG CHECK: series ends 30 Mar 2026; earliest TA post publishes
    2026-11-08, over seven months later. Comfortably past the 3-month SEBI
    rule. Do not extend the dataset toward the present without re-checking.
  - SOURCE CROSS-CHECK: this feed's close for 30 June 2025 is Rs 5,851.00,
    exactly matching the price already committed in real_company.yml's
    `market:` block. The two are consistent.
- Charts: 10 SVGs in assets/charts/, all generated by script from the same
  CSV so prose and figures cannot drift apart. Generation script is in the
  session scratchpad; if charts need regenerating, re-derive from the CSV.
  Note matplotlib's DejaVu Sans has no rupee glyph, so chart text uses "Rs"
  rather than the symbol (post prose still uses the symbol).
- COMPLIANCE NOTE, specific to this series: TA is inherently about entry and
  exit signals, which makes it the closest any series here comes to the line
  CLAUDE.md draws. Every post frames indicators as things to UNDERSTAND, and
  none says when to buy or sell. Where a signal is shown, its failures are
  shown alongside its successes, from the same dataset.
- Roadmap, 10 posts, proposed dates on the usual 2-day cadence:
  - TA-1 What technical analysis is, and what it assumes (2026-11-08)
  - TA-2 Reading a candlestick chart (2026-11-10)
  - TA-3 Support and resistance (2026-11-12)
  - TA-4 Trend lines and trend structure (2026-11-14)
  - TA-5 Moving averages (2026-11-16)
  - TA-6 Volume (2026-11-18)
  - TA-7 RSI (2026-11-20)
  - TA-8 MACD (2026-11-22)
  - TA-9 Chart patterns (2026-11-24)
  - TA-10 What technical analysis cannot do (2026-11-26)
- Findings from the real data that shape several posts, all verified:
  - Only ONE 50/200 SMA crossover in two years (golden cross, 4 Jun 2025)
    and no death cross at all. TA-5 makes the scarcity the point: a signal
    this rare cannot be judged from one chart.
  - RSI gave three signals with three different outcomes in the same
    dataset: overbought Jul 2024 (price rose a further 12%), overbought
    Sep 2024 (price then fell 26%), oversold Nov 2024 (price fell a further
    9%). TA-7 uses all three rather than the flattering one.
  - MACD produced 31 crossovers in 460 bars, one every ~15 trading days.
    TA-8 uses that to show the whipsaw problem directly.
  - The largest volume day in the dataset (27 Mar 2025, 13.2x the 50-day
    average) moved the close by -0.2%. TA-6 uses it against the assumption
    that heavy volume means a big move.
  - The "double top" that ISN'T: what looks like a textbook double top
    (10 Nov 2025 and 7 Jan 2026 highs, 0.15% apart) is really six swing
    highs inside a 3% band, and the highest of the six came BEFORE both of
    the chosen peaks, with another printing after the supposed breakdown.
    TA-9 uses it to show how a pattern appears once you select two points
    and discard the rest; TA-10 refers back to it. The textbook measured
    target was never reached.
  - Trend lines: the Oct 2024 downtrend line broke 20 Jan 2025 (close 4,885
    against a line at 4,883); the Mar 2025 uptrend line held 384 days before
    breaking 23 Mar 2026.
- TA-1 to TA-10 reviewed and scheduled (moved to _posts/):
  what-technical-analysis-is (2026-11-08), reading-a-candlestick-chart
  (2026-11-10), support-and-resistance (2026-11-12), trend-lines
  (2026-11-14), moving-averages (2026-11-16), volume (2026-11-18), rsi
  (2026-11-20), macd (2026-11-22), chart-patterns (2026-11-24),
  what-technical-analysis-cannot-do (2026-11-26) — staggered a few days
  apart, same cadence as every module before it. Intra-module links
  converted to {% post_url %}; no post links forward (see the build rule
  above). Verified the site builds on all 51 publish dates.
- This completes THREE of the four series in CLAUDE.md: Jargon, Decoded
  (33 posts), Fundamental Analysis (8), Technical Analysis (10). Only
  Mutual Funds, Minus the Marketing remains.

Mutual Funds, Minus the Marketing — roadmap

- The fourth and final series in CLAUDE.md. Covers the topics listed there:
  NAV basics, point-to-point vs rolling returns, expense ratios, drawdown
  and volatility, Sharpe, SIP timing myths, benchmarks/category comparison,
  and reading a factsheet.
- Data: real AMFI NAV history, truncated at 31 March 2026 (FY26 close) to
  match the TA dataset's cutoff.
  - UTI Nifty 50 Index Fund, regular (AMFI code 100822) and direct (120716):
    assets/data/uti-nifty50-index-fund-nav.csv — 4,915 NAV points from
    3 Apr 2006, i.e. 20 years spanning BOTH the 2008 and 2020 crashes.
    This fund carries every calculation in the series.
  - Parag Parikh Flexi Cap, regular (122640) and direct (122639):
    assets/data/parag-parikh-flexicap-nav.csv — used in ONE post only
    (expense ratios), and only to compare the fund against ITSELF.
  - Source: AMFI's official NAV history via the free mfapi.in wrapper.
  - Verified figures in _data/mf.yml, all script-derived from the CSVs.
  - LAG CHECK: both end 31 Mar 2026; first post publishes 2026-11-28, nearly
    eight months later.
  - CROSS-CHECK: the index fund NAV falls ~14.6% between 1 Jan and 31 Mar
    2026, matching the Q1 2026 decline independently visible in the
    Britannia price data (-13.5%). Two unrelated sources agreeing.
- COMPLIANCE NOTE for this series: fund performance is the easiest thing on
  this blog to misread as a recommendation. So: no post ranks funds, no post
  compares one manager against another, and no post says any fund is worth
  owning. An INDEX fund does all the arithmetic (passive, no manager skill
  claim). The one active fund appears solely as a direct-vs-regular fee
  comparison of the fund against itself, with an explicit note that its own
  merits are not being assessed.
- Roadmap, 9 posts, usual 2-day cadence:
  - MF-1 What a mutual fund is, and what NAV does not mean (2026-11-28)
  - MF-2 Point-to-point returns and the start-date problem (2026-11-30)
  - MF-3 Rolling returns (2026-12-02)
  - MF-4 Expense ratios: direct vs regular (2026-12-04)
  - MF-5 Drawdown: the fall, and how long it lasted (2026-12-06)
  - MF-6 Volatility and the Sharpe ratio (2026-12-08)
  - MF-7 SIPs, XIRR, and the timing myths (2026-12-10)
  - MF-8 Benchmarks and comparing like with like (2026-12-12)
  - MF-9 Reading a factsheet (2026-12-14)
- Findings from the real data that shape the posts, all verified:
  - Five-year returns on the SAME index fund range from 2.56% a year
    (starting Jan 2007) to 23.92% (starting Apr 2020). MF-2 is built on it.
  - Rolling returns narrow sharply with holding period: 3-year windows run
    -4.8% to +32.0% and are negative 2.9% of the time; 10-year windows run
    +4.4% to +16.1% and are never negative. Median barely moves (~11.8%).
  - 2008 drawdown: -59.7%, and 2,162 days (5.9 years) back to break-even.
    2020: -38.4%, recovered in 300 days. Same asset, very different waits.
  - Expense drag, same fund both sides: the index fund's direct plan beat
    its regular plan by 0.125pp a year (Rs 6,135 on Rs 1 lakh over 13 years);
    the active fund's gap is 0.83pp a year (Rs 74,134, or 9.5%). The
    contrast is the post.
  - A Rs 10,000 monthly SIP from Jan 2007 to Jan 2012 — five years, 61
    instalments, right through the crash — returned an XIRR of -0.02%.
    MF-7 leads with it.
  - But across the full 20 years the same SIP was below its invested amount
    in only 12 of 239 months (longest stretch 8 months, Oct 2008 to May
    2009). Both facts are true and MF-7 states both.
  - Sharpe over the full period is 0.18 (10.20% return, 20.99% volatility,
    6.5% risk-free) — a deliberately unflattering number, used to show what
    the ratio actually measures.
  - Note the full-period annualised return (10.20%) sits BELOW the median
    5-year rolling return (12.25%), because that one window starts near a
    2006 high and ends at a Q1 2026 low. MF-3 uses the discrepancy directly.
- Charts: 6 SVGs in assets/charts/ (mf-*.svg), generated by script from the
  CSVs, same discipline as the TA series.
- MF-1 to MF-9 reviewed and scheduled (moved to _posts/): what-a-mutual-fund-is
  (2026-11-28), point-to-point-returns (2026-11-30), rolling-returns
  (2026-12-02), expense-ratios-direct-vs-regular (2026-12-04), drawdown
  (2026-12-06), volatility-and-sharpe (2026-12-08), sips-xirr-and-timing-myths
  (2026-12-10), benchmarks-and-comparing-like-with-like (2026-12-12),
  reading-a-factsheet (2026-12-14). Links converted to {% post_url %}, none
  forward. Verified the site builds on all 60 publish dates.
- ALL FOUR SERIES IN CLAUDE.md ARE NOW WRITTEN AND SCHEDULED: Jargon,
  Decoded (33 posts, to 2026-10-21), Fundamental Analysis (8, to 2026-11-06),
  Technical Analysis (10, to 2026-11-26), Mutual Funds (9, to 2026-12-14).
  60 posts total, publishing through 14 December 2026. There is no further
  roadmap — anything beyond this is new scope, not a continuation.
- Two data bugs found and fixed during this module, both by the derived-data
  checks rather than by reading the prose:
  - The SIP routine silently skipped the 1 Apr 2006 instalment (the fund's
    first NAV is 3 Apr 2006), so the 20-year scenario is 239 instalments and
    Rs 23,90,000 invested, not 240 / Rs 24,00,000.
  - The SIP chart had been annotated "below water for most of 2008-2013".
    The real figure is 12 of 239 months, longest stretch 8 months
    (Oct 2008 to May 2009). Corrected in both the chart and mf.yml.
- Calculators still owed for this series (same open item as the FA module's
  DCF sheet): CLAUDE.md asks for rolling-returns and SIP/XIRR Google Sheet
  calculators. Every post ships working Python instead; search the drafts
  for GOOGLE-SHEET-TODO.

Lower-priority, not done (say the word if you want these next)

- Series index pages — _data/series.yml has the four series, titles, slugs as a source of truth, but there's no /series/fundamental-analysis/ listing page yet.
- Analytics (GA4/Plausible/GoatCounter) — not added, your call which one.
- Formula rendering (MathJax/KaTeX) if you want real math notation rather than code-block formulas.
- Minor: minima's bundled SCSS throws harmless Dart-Sass deprecation warnings during build (lighten() is deprecated) — cosmetic build noise, not a bug, will resolve itself on minima's next release.
