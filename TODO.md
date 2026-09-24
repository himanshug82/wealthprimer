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

The Tax Side of Investing — roadmap (fifth series, beyond CLAUDE.md's four)

- Scope decision (user-approved): a fifth series on how investment income is
  actually taxed in India. Written MECHANICS-FIRST, deliberately light on
  section numbers — see the accuracy note below for why that matters.
- ACCURACY / STALENESS — read before editing any post in this series:
  - Rates were VERIFIED against public sources in August 2026, not written
    from memory. Budget 2026 left capital gains rates unchanged from the
    Budget 2024 position: equity STCG 20%, equity LTCG 12.5% above a
    Rs 1,25,000 annual exemption, debt funds bought on/after 1 Apr 2023 at
    slab rate, 12-month holding period for listed securities and 24 for the
    rest, plus 4% health & education cess on the tax itself.
  - The Income-tax Act, 2025 REPLACED the Income-tax Act, 1961 from
    1 April 2026 — i.e. exactly the period these posts describe. Rates and
    slabs carried over unchanged, but nearly every section was renumbered
    (old 80C became 123), "Previous Year"/"Assessment Year" collapsed into a
    single "Tax Year", and Income Tax Rules 2026 replaced the 1962 Rules.
  - That is why the series teaches mechanics and avoids citing section
    numbers: holding periods, rates, set-off rules, FIFO and grandfathering
    are stable, while the numbering is not. Every post states the financial
    year its rules apply to.
  - incometaxindia.gov.in blocks automated fetches (HTTP 403), so nothing
    here is sourced from the primary text. Before publishing, these posts
    are worth a pass by someone who files professionally.
  - Every post carries a line saying it is educational and not tax advice,
    on top of the standard site disclaimer.
- Data: no new sourcing. Worked examples are computed from the fund NAV
  history already committed for the Mutual Funds series
  (assets/data/uti-nifty50-index-fund-nav.csv), so the tax arithmetic sits
  on real prices. Derived figures in _data/tax.yml.
- Roadmap, 9 posts, usual 2-day cadence:
  - TAX-1 How investment income is taxed: the map (2026-12-16)
  - TAX-2 Short-term vs long-term: the holding period decides (2026-12-18)
  - TAX-3 Equity and equity funds (2026-12-20)
  - TAX-4 Debt funds, gold and the rest (2026-12-22)
  - TAX-5 Dividends and interest (2026-12-24)
  - TAX-6 Losses: set-off, carry-forward and harvesting (2026-12-26)
  - TAX-7 SIPs and FIFO: one redemption, many tax lots (2026-12-28)
  - TAX-8 ELSS and the deduction that moved (2026-12-30)
  - TAX-9 Before you file (2027-01-01)
- Worked examples, all computed from real NAV data:
  - Lump sum Rs 5,00,000 (Apr 2020 to Mar 2026): gain Rs 9,19,901, tax
    Rs 99,363 before cess, Rs 1,03,337 with it.
  - Five-year SIP (Rs 10,000/month, Apr 2021 to Mar 2026): ONE redemption
    produces 48 long-term lots and 12 short-term ones. Real gain of
    Rs 88,376 and ZERO tax — the long-term gain sits under the exemption
    and the short-term lots are at a loss. Used for the FIFO post.
  - Two-year SIP (Apr 2024 to Mar 2026): an actual LOSS of Rs 18,292, split
    into a long-term and a short-term component by the Q1 2026 decline.
    Used for the set-off post, since that split is the whole subject.
  - Grandfathering: units bought Jan 2017 take their 31 Jan 2018 value as
    cost, excluding Rs 71,728 of gain from tax.
- TAX-1 to TAX-9 reviewed and scheduled (moved to _posts/):
  how-investment-income-is-taxed (2026-12-16), short-term-vs-long-term
  (2026-12-18), equity-and-equity-funds (2026-12-20),
  debt-funds-gold-and-the-rest (2026-12-22), dividends-and-interest
  (2026-12-24), losses-set-off-and-harvesting (2026-12-26), sips-and-fifo
  (2026-12-28), elss-and-the-deduction-that-moved (2026-12-30),
  before-you-file (2027-01-01). None link forward. Verified the site builds
  on all 69 publish dates.
- STILL OPEN for this series: have someone who files professionally read
  these before they go out. Nothing here is sourced from the primary text of
  the Act, because incometaxindia.gov.in blocks automated fetches.
- Also added: `tax` entry in _data/series.yml and series/tax.markdown, so the
  series appears at /series/ and /series/tax/ automatically.

DONE — Indian number formatting in posts (site-wide)

- CLAUDE.md asks for Indian digit grouping on currency (Rs 12,34,567), but
  figures pulled from _data rendered bare ("Rs 919901"). Fixed across the
  whole site: 166 currency outputs in 36 files now run through a new
  _includes/inr.html.
- IMPORTANT, do not "simplify" this into a plugin: the deploy workflow uses
  actions/jekyll-build-pages, which runs Jekyll in SAFE MODE. A custom Liquid
  filter in _plugins/ would work locally and be SILENTLY IGNORED in
  production. The include is pure Liquid for that reason.
- Two gotchas worth knowing if you extend it:
  - Jekyll's include tag rejects array subscripts as parameters
    (n=dcf.forecast[0].fcff fails to build). Pre-assign to a variable first.
    The forecasting-free-cash-flow post does this.
  - Do NOT apply the include to every numeric output. Values under 1,000 pass
    through untouched, but a DATE string like "2026-03-31" would be mangled,
    and a bare year would become "2,026". It is deliberately applied only to
    Rs-prefixed currency outputs.
- Verified by diffing the rendered text of all 69 posts before and after:
  30 posts changed, and in every case the ONLY difference was inserted
  comma separators.
- Not done, and fine to leave: figures inside tables whose column header
  says "Rs Lakh"/"Rs Crore" but which have no Rs prefix on the value itself
  (e.g. Britannia revenue rendering as 17942.67). Formatting those means
  targeting bare numeric outputs, which is where the date-mangling risk
  lives, so it needs a more careful pass than a regex.

DONE — SEO metadata and dead links (site-wide)

- PROBLEM FOUND: every post shipped the SAME <meta name="description">. Cause:
  68 of 69 posts open with a `{% assign %}` block, so Jekyll's auto-excerpt was
  that block, which renders to an empty string; jekyll-seo-tag then fell back to
  site.description on all 69 pages. Verified in the built HTML, not assumed.
- FIX: an explicit `description:` in every post's front matter, written from
  that post's own content (140-160 chars, the length Google shows). All 69 are
  distinct — verified by building with --future and diffing the rendered meta
  tags: 69 posts, 69 unique descriptions.
- Note this does NOT fix the homepage excerpts. `show_excerpts: true` is still
  silently rendering nothing for the same underlying reason, so /index.html is
  a bare list of titles. Fixing that needs `excerpt_separator` plus a marker in
  each post, or an explicit `excerpt:` — separate job, not done here.
- FIXED: twitter:creator was shipping as `@Himanshu Gupta` — a handle with a
  space in it. jekyll-seo-tag's AuthorDrop falls back to the author's NAME as
  the handle when none is set. `author:` in _config.yml cannot simply become a
  hash, because minima's footer prints `{{ site.author | escape }}` and would
  render the raw hash. Fix: keep `author:` a string and add _data/authors.yml,
  which seo-tag merges by name (AuthorDrop#site_data_hash). The top-level key
  in that file must stay identical to `author:` in _config.yml.
- FIXED: THREE dead LinkedIn links, all pointing somewhere useless.
  about.markdown and the `social.links` sameAs both used
  linkedin.com/feed/ — which sends a visitor to their OWN feed — and minima's
  social.html was separately rendering linkedin.com/in/wealthprimer_in out of
  `linkedin_username`, a profile that doesn't exist. All three removed
  (user's call) rather than pointed at a guess. If a real profile or company
  page is ever created, all three come back together — see the comment at
  `linkedin_username` in _config.yml. About now lists the contact email instead.
- FIXED: privacy.markdown was shipping three literal "TODO —" bullets to a
  public page, on the one page whose whole job is establishing credibility.
  Replaced with what is actually true today: no analytics, no cookies, no
  third-party resources, no ads, no comments, plus an honest note that GitHub
  Pages logs requests as any host does. Each of those is verifiable by a
  reader opening devtools, so there is a MAINTENANCE comment in the file: add
  any of them and the list must be updated in the same commit.

DONE — analytics, email capture, homepage, diagrams, social cards

- ANALYTICS: GoatCounter, in _includes/analytics.html, wired into head.html
  (replacing the never-configured google_analytics block). Renders ONLY when
  `goatcounter:` is set in _config.yml AND the build is production, so local
  serve stays clean. Set it to the site CODE from https://CODE.goatcounter.com,
  not the full URL. Chosen over GA4 so /privacy/ can keep saying no cookies.
- EMAIL: _includes/newsletter.html, on every post (above the disclaimer, since
  a signup under a wall of legal text is a signup nobody sees) and on the
  homepage. Renders nothing until `newsletter.action` is set, so a
  half-configured list ships nothing. Deliberately a PLAIN HTML form posting
  straight to the provider — no provider JS, no tracking pixel — which is what
  keeps the "loads no external resources" property true on page render.
  Configured for Mailchimp; switching to Buttondown is three config keys and no
  template change. Setup steps are in the include's own comment.
  - Mailchimp's free tier is 500 contacts / 1,000 sends a month with their
    branding in the footer. Buttondown's is 100 subscribers with neither. Worth
    revisiting once the list is real; the switch is one config edit.
- PRIVACY PAGE IS NOW SELF-MAINTAINING: the analytics, cookie, third-party and
  email bullets are rendered CONDITIONALLY on the same two config keys that
  switch those features on. Turning a feature on turns its disclosure on in the
  same act — they cannot silently disagree, which was the exact failure mode
  flagged last round. Claims not driven by a key (no ads, no comments) are still
  asserted as plain fact and still need a manual edit if that changes.
- HOMEPAGE: _layouts/home.html now overrides minima's. Was a bare reverse-chron
  list of every title, so a first-time reader landed on whatever ratio published
  last with no signal it was post 21 of 33. Now: a hero, a "Start here" grid of
  the five series (rendered from _data/series.yml, so a sixth series needs no
  edit here), then the 8 latest posts WITH one-line summaries, then the signup.
  - This is also the excerpt fix. Rather than fight Jekyll's auto-excerpt — which
    returns an empty string because 68 of 69 posts open with a {% assign %} block
    — the layout uses each post's `description:` front matter. That same field
    already feeds the meta description AND (checked in jekyll-feed's template)
    the RSS <summary>, which the descriptions silently fixed too. One sentence
    per post, written once, used in three places.
  - `show_excerpts: true` REMOVED from _config.yml. It was a no-op. Re-adding it
    will not bring excerpts back; the layout no longer reads post.excerpt.
  - Series with nothing published yet now read "Publishing soon" instead of
    "0 posts published so far" — four of five said the latter for months.
- DIAGRAMS: six schematics for the Jargon/FA posts, which had NO images at all
  across 41 posts (charts existed only in TA and MF). Balance sheet identity,
  income waterfall, cash flow bridge, cash conversion cycle, DuPont tree, and
  the composition of a DCF — inserted into the six posts they belong to.
  - GENERATED, NOT HAND-DRAWN: scripts/make_diagrams.py READS _data/case_study.yml
    and emits the SVG. Every number in these diagrams also appears in a post,
    rendered from that same YAML; hand-drawing would have created two sources of
    truth that drift apart silently. If the case study model changes, re-run it.
  - Authored as SVG rather than through matplotlib (unlike the TA/MF charts)
    because these are schematics, not plots of a dataset. Palette comes from
    assets/logo.svg so the whole site stays one visual system.
- SOCIAL CARDS: scripts/make_og_cards.py generates a per-post 1200x630 card into
  assets/og/, and every post now carries `image:` front matter pointing at its
  own. All 69 posts previously fell back to the site default, so every link to
  this blog on Twitter/LinkedIn/WhatsApp/Slack looked identical — the biggest
  click-through lever a text blog has, thrown away.
  - RE-RUN THIS WHEN A POST TITLE CHANGES or the card shows the old title. Each
    PNG stores the title+series it was built from in its own metadata, and
    `--check` compares them, so this is catchable rather than a silent rot.
  - .github/workflows/pages.yml runs that check as an ADVISORY job. It is
    deliberately NOT a dependency of build/deploy: publishing runs on a daily
    cron, and a forgotten regeneration must never be able to stop scheduled
    posts from going live. Red check, successful deploy.
  - The script also covers _drafts, so a draft's card exists before promotion.

DONE (code) / PENDING (your accounts) — Google Analytics 4 + giscus comments

- Decided 24 Sep 2026: GA4 for analytics (GoatCounter kept as an optional
  cookie-free cross-check), giscus for comments (Disqus rejected: ad-supported
  and tracker-heavy, contradicts /privacy/).
- Both are wired and self-hiding: _includes/analytics.html renders GA4 only
  when `google_analytics:` is set, _includes/comments.html renders giscus only
  when `giscus.repo_id` AND `giscus.category_id` are set, both only in
  production. /privacy/ reads the same keys, so each feature's disclosure
  (including the switch from "no cookies" to a _ga cookie disclosure) turns
  on in the same commit as the feature. The privacy page's old hardcoded
  "Comments: none" is now conditional too.
- GA4 is configured with Google Signals and ads personalisation OFF, and the
  privacy page asserts that as fact — keep them in sync.
- Comment box carries a moderation note (no tips, no price targets, no
  "should I buy X") — compliance, not just etiquette. Enforce it.
- YOUR TWO STEPS to switch on:
  1. GA4: create a property + web data stream at analytics.google.com, paste
     the Measurement ID (G-XXXXXXXXXX) into `google_analytics:` in _config.yml.
  2. giscus: repo Settings > enable Discussions; create an "Announcement"-type
     category named "Comments"; install https://github.com/apps/giscus on the
     repo; open https://giscus.app, pick repo + mapping "pathname" + category
     "Comments", copy data-repo-id and data-category-id into `giscus:` in
     _config.yml. Full notes in _includes/comments.html.
- Removed minima's disqus hook from _layouts/post.html (never configured).

DONE — structural fixes from the 24 Sep 2026 review (navigation, glossary, methodology)

- GA4 is LIVE: `google_analytics: "G-LYRDRDQSE8"` set by the user. /privacy/
  now discloses GA4 + `_ga` cookies automatically. giscus still needs
  repo_id/category_id (see the section above).
- SERIES NAVIGATION on every post (_includes/series-nav.html, used twice by
  _layouts/post.html: once with header=true to compute, once to render):
  - Header line "Jargon, Decoded · Part 13 of 33" linking to the series page.
    M comes from a new `planned:` field in _data/series.yml (33/8/10/9/9),
    because site.posts only sees PUBLISHED posts and would say "Part 3 of 3"
    on day three. Falls back to the published count if `planned` is missing
    or lower. BUMP `planned` when a module is added to a series.
  - Prev/next links after the body. Built from site.posts, never post_url,
    so a not-yet-published next post cannot break the build (see the build
    rule above). When there is no next post yet: "You're up to date — part
    N+1 of M publishes soon"; on the last planned post: "Pick the next
    series". Verified on first, middle and latest post.
- TABLE OF CONTENTS (_includes/toc.html): pure Liquid (safe mode — no
  plugin), parses the rendered <h2 id=…> tags. Auto-shows at >= 6 H2s, which
  is the 36 longer FA/TA/MF/tax posts and NOT the 29 five-section Jargon
  posts. Override per post with `toc: true|false`.
- "Updated <date>" in the post header when `last_modified_at:` is set in
  front matter (none set yet). jekyll-seo-tag and jekyll-sitemap read the
  same key, so setting it also updates dateModified / <lastmod>. Use it when
  a tax post's rates are re-verified.
- GLOSSARY at /glossary/ (glossary.markdown, in the top nav). Built from
  every published post with a `term:` front-matter key, across ALL series,
  A–Z with letter jump links; each entry shows the post's `description:` and
  series tag. 60 posts now carry `term:` (added by script; the 9 without one
  are openers/closers like "Meet Desi Bites", "What TA cannot do", "Before
  you file", plus the capstone and the FCF-forecasting post). Grows on each
  publish date with no edits. This is the page CLAUDE.md's "link at first
  use" rule points at — give every new concept post a `term:`.
- DATA & METHODOLOGY page at /methodology/ (methodology.markdown, in the top
  nav, linked from About): the rules (educational only, >= 3-month lag,
  one cited source per dataset, derived-not-typed), fictional-vs-real
  explained, a table of every dataset with source URL, range and the CSV
  link, known limits, and a corrections route (email + issues on the site
  repo). UPDATE THE TABLE when a dataset is added (e.g. the bank filing for
  R3, a debt-fund NAV series for R5).
- 404.html rewritten: explains that a link to an unpublished post lands
  here until its date, and points to /series/, /glossary/, /case-study/.
  `sitemap: false` so it stays out of sitemap.xml.
- Top nav is now Series · Glossary · Case study · Data & methodology · About
  · Privacy (header_pages in _config.yml).
- NOT done, needs your account: the newsletter is still unconfigured
  (`newsletter.action` empty), so the signup box on every post renders
  nothing. Mailchimp or Buttondown — three config keys, notes in
  _includes/newsletter.html.
- Local build note: this machine has no usable Ruby (system 2.6, no
  bundler). Builds were verified in a ruby:3.3 container via OrbStack:
    docker run --rm -v "$PWD":/srv -w /srv -e JEKYLL_ENV=production ruby:3.3 \
      sh -c 'bundle config set --local path vendor/bundle && bundle install && \
             bundle exec jekyll build'
  vendor/bundle is gitignored.

DRAFT WRITTEN — "What the F&O numbers actually say" (_drafts/)

- The gap flagged in review: the blog teaches RSI and MACD but never mentions
  that SEBI has counted, five years running, and the large majority of
  individual derivatives traders lose money. Highest-traffic, highest-
  credibility topic available, and it fits the "honest about limitations"
  brand the TA series already closes on.
- Figures live in _data/fno.yml, NOT inline. READ THE "VERIFY BEFORE PUBLISHING"
  BLOCK AT THE TOP OF THAT FILE before scheduling this.
  - Corroborated and safe: 89% (FY22), 93% and >Rs 1.8 lakh crore (FY22-FY24,
    confirmed on SEBI's own press release page), 87.7% and Rs 91,685 crore and
    the 92% options share (FY26, two independent sources agreeing).
  - Single-source and flagged `corroborated: false`: average loss per trader,
    transaction costs, repeat-loser rate, the portfolio-size split. SEBI serves
    its study PDFs behind a landing page that automated fetches could not get
    through — same situation as incometaxindia.gov.in and the tax series.
  - KNOWN CONFLICT: sources disagree on the FY26 participant count (~87.5 lakh
    vs ~78.6 lakh "active"), probably two different definitions. The post
    therefore never quotes a participant count. Settle it from the PDF.
- THREE DECISIONS FOR YOU, spelled out in a comment at the top of the draft:
  which series (it has no `series:` key on purpose — it is not technical
  analysis and not mutual funds; either standalone, or the opener of a sixth
  risk series), whether the flagged numbers check out, and the publish date
  (set to 2027-01-05 just to follow the tax series and hold the 2-day cadence).
- Compliance: names no security, recommends no transaction, and has a section
  saying plainly that a base rate is not an instruction. It DOES take a strong
  view on the segment, which CLAUDE.md explicitly permits. Also notes that F&O
  is taxed as business income, so the tax series' capital-gains rules do not
  apply to it — that is arguably its own post later.

ROADMAP — what comes after the first 69 posts (decided 24 Sep 2026)

- Context: the five series in CLAUDE.md (+ tax) are fully written and
  scheduled through 2027-01-01. Everything below is NEW scope, chosen from a
  content review of the 69 posts. Order = priority. Same rules as before: every
  figure in _data/, script-derived, lag-checked; Desi Bites for the fictional
  walkthrough, a real anchor company for the real one; nothing that reads as a
  call.
- Gaps the review found, which the modules below are built to close:
  1. Banks/NBFCs are absent — the most-held stocks in India, and none of the
     33 Jargon ratios apply to them (no inventory, no EBITDA, D/E meaningless).
  2. FA jumps from ratios straight to DCF — nothing on annual reports, notes to
     accounts, red flags or quarterly results (what people actually do every
     quarter).
  3. MF has no debt-fund mechanics and no index-fund-vs-ETF post, even though
     the tax series taxes debt funds and the flagship dataset is an index fund.
  4. No risk/behaviour content; the F&O draft is unscheduled because it has no
     home.
  5. No personal-finance layer (EPF/PPF/NPS, insurance vs investment, real
     returns) — largest new-audience opportunity.

- R1. NEW SERIES: "Risk, Leverage and Your Own Brain" (slug: risk), 8 posts.
  Resolves the F&O draft's open decision (b): it becomes the opener. Needs a
  `risk` entry in _data/series.yml + series/risk.markdown + `series: risk` on
  the draft. Reuses the UTI Nifty 50 NAV series and Britannia OHLCV — no new
  data sourcing except verifying fno.yml against the SEBI PDFs.
  - RISK-1 What the F&O numbers actually say (existing draft; verify fno.yml)
  - RISK-2 The arithmetic of losses (-50% needs +100%; volatility drag on real
    NAV data)
  - RISK-3 Position sizing and the 1-2% rule (ATR on Britannia OHLCV; pure
    method, no trade)
  - RISK-4 Leverage and margin: how a 10% move wipes out 100% (MTF, futures
    margin mechanics)
  - RISK-5 Diversification is a correlation problem (why ten large-cap funds
    is not diversification)
  - RISK-6 Sequence-of-returns risk (same SIP, crash in year 1 vs year 19)
  - RISK-7 Behavioural biases, Indian edition (loss aversion, recency,
    anchoring to buy price)
  - RISK-8 How finfluencers make money (incentive structures; a credibility
    post for a credibility-first blog)

- R2. FUNDAMENTAL ANALYSIS, Module 2: "Reading between the lines", 7 posts.
  Continues the Desi Bites story past its IPO. Needs new narrative beats in
  _data/case_study.yml (first quarterly results, an acquisition, a
  related-party sale, a contingent liability). Britannia remains the real
  anchor; its Q3 festive quarter is the seasonality example.
  - FA2-1 Reading an annual report (MD&A, auditor's report, notes; what to skip)
  - FA2-2 Desi Bites cooks the books (FICTIONAL forensic case: channel
    stuffing, capitalised expenses, related-party sales — teaches red flags
    without accusing a real company)
  - FA2-3 Reading quarterly results (YoY vs QoQ, seasonality)
  - FA2-4 Contingent liabilities, pledged shares and promoter holding (the
    shareholding-pattern page)
  - FA2-5 Goodwill, exceptional items and "other income" (Desi Bites acquires
    a competitor)
  - FA2-6 Capital allocation: dividends vs buybacks vs capex vs debt paydown
  - FA2-7 Reading a DRHP (the Desi Bites IPO retold from the prospectus side)

- R3. FUNDAMENTAL ANALYSIS, Module 3: "When the ratios don't work: banks and
  NBFCs", 6 posts. HIGHEST-VALUE GAP. Needs a SECOND real anchor company,
  sourced the same way as Britannia: an audited FY25 bank filing from
  NSE/BSE, into _data/real_bank.yml with the source URL, plus a lag check on
  any market data. Pick the bank before drafting. No fictional bank — the
  Desi Bites model has no banking analogue, so these posts are real-anchor
  only.
  - BANK-1 Why P/E and D/E break on a bank (the balance sheet is the business)
  - BANK-2 NIM and the spread (cost of funds, yield on advances)
  - BANK-3 CASA and the deposit franchise
  - BANK-4 GNPA, NNPA, provision coverage and credit cost
  - BANK-5 Capital adequacy: CAR and Tier-1
  - BANK-6 Valuing a bank: P/B, ROA, ROE and why P/B is the one that matters

- R4. JARGON, DECODED, Module 6: terms the other series already lean on but
  never define, 12 short glossary posts (definition -> formula -> one small
  example -> takeaway; Desi Bites / Britannia / the index fund as fits).
  Beta - Alpha - Tracking error vs tracking difference - YTM - Modified
  duration - Exit load - AUM - Operating leverage - Earnings yield and FCF
  yield - Payout ratio - Face value, splits and bonuses - Enterprise value on
  its own (currently defined only inside EV/EBITDA).

- R5. MUTUAL FUNDS, Module 2, 6 posts. Same compliance rule as MF-1..9: no
  ranking, no manager comparison, index fund does the arithmetic. Debt-fund
  posts need a debt-fund NAV series (a liquid or gilt index fund, AMFI via
  mfapi.in, lag-checked) added to assets/data/.
  - MF2-1 Debt funds explained (YTM, duration, credit risk)
  - MF2-2 Index funds vs ETFs (iNAV, liquidity, tracking difference)
  - MF2-3 SEBI fund categories decoded (large/mid/small/flexi/multi)
  - MF2-4 Portfolio overlap (why two funds can be one fund)
  - MF2-5 Why star ratings mislead
  - MF2-6 STP and SWP mechanics

- R6. TAX add-ons, 4 posts. Same staleness rules as TAX-1..9 (rates verified
  against public sources, mechanics-first, professional review before
  publishing).
  - TAX-10 ESOPs and RSUs (perquisite at exercise, capital gain at sale; the
    IT-worker audience)
  - TAX-11 Buybacks after 1 Oct 2024 (deemed dividend in the shareholder's
    hands; cost becomes a capital loss)
  - TAX-12 F&O as business income (audit thresholds, presumptive scheme;
    links to RISK-1)
  - TAX-13 Foreign stocks and Schedule FA

- R7. TECHNICAL ANALYSIS, Module 2, 4 posts. Same Britannia OHLCV; extend
  _data/ta.yml by script.
  - TA2-1 Bollinger Bands and ATR (volatility, not direction)
  - TA2-2 Relative strength vs the index (NOT RSI — the naming clash is the
    opening paragraph)
  - TA2-3 Multiple-timeframe analysis
  - TA2-4 How to backtest an indicator honestly (look-ahead bias,
    overfitting, transaction costs) — the sequel to "what TA cannot do" and
    the home for the pandas notebook CLAUDE.md promises

- R8. LATER / UNDECIDED: a personal-finance track ("Money Before Markets":
  emergency fund, EPF/PPF/NPS, term insurance vs ULIP/endowment, FDs vs debt
  funds, real return after inflation and tax). Out of CLAUDE.md's stated
  scope; decide whether the blog widens to it before drafting. Also: bonds
  and G-secs (RBI Retail Direct), REITs/InvITs, SGBs as a "beyond stocks and
  funds" mini-module.

- Still owed regardless of the above: the three Google Sheet calculators
  (DCF, rolling returns, SIP/XIRR — search posts for GOOGLE-SHEET-TODO) and a
  professional read of the tax series before 2026-12-16.

DONE — R1..R7 WRITTEN AND SCHEDULED (47 posts, 2026-11-05 → 2026-12-21)

- Written 24 Sep 2026, seven modules in parallel, then integrated: every post
  passes scripts/check_posts.py (new — see below), the whole site builds with
  --future (116 posts), OG cards regenerated. Daily cadence continues without a
  gap from the last original post (2026-11-04). R8 (personal finance) remains
  undecided and unwritten. `planned` in _data/series.yml bumped to
  45/21/14/15/13 and the new `risk` series (8) added with series/risk.markdown.
- NEW TOOL: scripts/check_posts.py — run before every commit that touches
  _posts/. Fails on: a forward-dated post_url (the build-breaker), missing
  front matter, filename/date mismatch, unknown series slug, site.data.X with
  no _data/X.yml, a Liquid `{{ var }}` whose root was never assigned, a chart
  path that doesn't exist. Warns on description length, missing term:, two
  posts on one date, missing OG card. Stdlib only.
- Local Python for derivation scripts: this machine has no pandas; a venv was
  used (see the build note above for docker). To re-run any scripts/derive_*.py
  create a venv with pandas numpy pyyaml matplotlib pillow.

- R1 Risk series (8): 11-05 what-the-fo-numbers-actually-say (promoted from
  _drafts; series: risk), 11-06 the-arithmetic-of-losses, 11-07
  position-sizing-and-the-one-percent-rule, 11-08 leverage-and-margin, 11-09
  diversification-is-a-correlation-problem, 11-10 sequence-of-returns-risk,
  11-11 behavioural-biases-indian-edition, 11-12 how-finfluencers-make-money.
  Data: scripts/derive_risk.py → _data/risk.yml + assets/charts/risk-*.svg,
  from the index-fund NAV, Britannia OHLCV and Nifty PRI (all end Mar 2026).
  _data/fno.yml: corroboration upgraded to "two independent secondary sources
  agree; primary PDF still unread" (corplawupdates.in summary of SEBI press
  release 50/2026 matched every fy26_unverified figure); participant count
  still not quoted (98.1→78.6 lakh vs "8.75 million" definitional conflict).
  Findings: FY07–FY26 arithmetic mean 13.03% vs CAGR 10.20% (2.83pp drag);
  Britannia–Nifty daily correlation 0.28 (β 0.42); same 20 yearly returns
  reordered turn a ₹10k SIP into ₹26.9 lakh (best-first) or ₹2.61 crore
  (worst-first) vs ₹80.4 lakh actual, while the lump sum is identical.
  VERIFY: fno.yml against SEBI's primary PDFs; RISK-8's summary of SEBI's
  finfluencer rules (2024 association ban, 2025 education carve-out, ASCI) is
  stated at confidence level only; RISK-8 says the site runs GA and has no
  ads/referrals — keep true; RISK-4 MTF 12% / futures margin ~12% are
  illustrative.
- R2 FA module 2 "Reading between the lines" (7): 11-13
  reading-an-annual-report, 11-14 desi-bites-cooks-the-books, 11-15
  reading-quarterly-results, 11-16
  contingent-liabilities-pledges-and-promoter-holding, 11-17
  goodwill-exceptional-items-and-other-income, 11-18 capital-allocation, 11-19
  reading-a-drhp. Data: scripts/build_case_study_2.py → _data/case_study_2.yml
  (FY26 honest accounts tracking the DCF forecast; a FICTIONAL "dressed" FY26;
  FY25 quarters + Q1/Q2 FY26; acquisition of "Chatpata Foods" for ₹600 lakh
  with ₹245 lakh goodwill; shareholding + 15% pledge at 62% LTV; GST demand
  as contingent liability; capital-allocation table; DRHP data). Script
  asserts both balance sheets balance and cash ties. case_study.yml itself is
  untouched. Diagrams: assets/charts/fa2-*.svg. Findings: dressed PAT +43% vs
  honest but OCF only +4% (OCF/PAT 1.50→1.10, debtor days 30→45); interest on
  idle IPO cash is 21% of honest PBT and drags closing-equity ROE 30.8%→12.1%.
  VERIFY: regulatory statements made from memory — ICDR 25% cap on general
  corporate purposes, SME promoter lock-in (3y minimum contribution / 1y
  rest), 45/60-day results deadlines, 21-day shareholding-pattern filing, KAMs
  since 2018. Note: FY26 inventory days show 56 vs 48 because acquired
  inventory arrives with six months of COGS.
- R3 FA module 3 "Banks and NBFCs" (6): 11-20 why-ratios-break-on-a-bank,
  11-21 nim-and-the-spread, 11-22 casa-and-the-deposit-franchise, 11-23
  gnpa-nnpa-and-provisions, 11-24 capital-adequacy, 11-25
  valuing-a-bank-price-to-book. Real anchor: HDFC Bank standalone audited
  FY25 (FY24 comparatives), results release 21 Apr 2025, primary source = the
  bank's release filed as a Form 6-K exhibit with the US SEC (URL in
  _data/real_bank.yml). scripts/derive_bank.py → real_bank.yml (reported
  lines typed once, every ratio computed); scripts/make_bank_diagrams.py →
  assets/charts/bank-*.svg. Two of the parent's extracted figures were wrong
  and corrected from the filing: shareholders' equity is capital + reserves
  ₹4,97,619 cr (₹4,88,900 cr is the RBI "net worth" line, kept separately);
  CASA ₹9,44,600 cr. Price for P/B: NSE close 30 Jun 2025 = ₹2,001.50
  pre-bonus (Yahoo's adjusted 1,000.75 × 2; 1:1 bonus record date 27 Aug 2025),
  paired with pre-bonus FY25 EPS/BVPS — explained in BANK-6. Findings: NIM on
  avg total assets 3.26% vs the bank's Q4 3.54% (methodology gap is the
  lesson); FY25 PAT +10.7% while pre-provision profit +6.1% because the FY24
  ₹10,900 cr floating provision wasn't repeated; P/B 3.08x with justified-P/B
  ranging 1.08x–3.40x across input pairs — no verdict drawn. VERIFY: FY24
  CASA ratio ~38.2% is not in the FY25 release (widely reported, flagged);
  D-SIB surcharge (filing implies 0.2%, RBI reviews annually).
- R4 Jargon module 6 (12): 11-26 beta, 11-27 alpha, 11-28
  tracking-error-and-tracking-difference, 11-29 yield-to-maturity, 11-30
  modified-duration, 12-01 exit-load, 12-02 aum, 12-03 operating-leverage,
  12-04 earnings-yield-and-fcf-yield, 12-05 payout-ratio, 12-06
  face-value-splits-and-bonuses, 12-07 enterprise-value.
  scripts/derive_jargon_m6.py → _data/jargon_m6.yml. Findings: Britannia beta
  0.42 over 2y but 0.29 (FY25) vs 0.55 (FY26), R² 0.18; index fund beats
  Nifty PRI by ~1pp every year 2016–2025 (dividends, not skill), tracking
  error 0.27%; Britannia payout 81.3% → sustainable growth ≈9.8%; Desi Bites
  40.2% → ≈20.3% (consistent with the DCF's 18%); Britannia EV < market cap
  (net cash). VERIFY: SEBI TER slab table in the AUM post is from memory.
- R5 MF module 2 (6): 12-08 debt-funds-explained, 12-09
  index-funds-vs-etfs, 12-10 sebi-fund-categories-decoded, 12-11
  portfolio-overlap, 12-12 why-star-ratings-mislead, 12-13 stp-and-swp.
  New data in assets/data/: uti-gilt-fund-nav.csv (102510/120792),
  uti-overnight-fund-nav.csv (100814), uti-money-market-fund-nav.csv (112077),
  uti-nifty50-etf-nav.csv (135320) — AMFI via mfapi.in, truncated 31 Mar
  2026. scripts/derive_mf2.py → _data/mf2.yml; scripts/make_mf2_charts.py →
  assets/charts/mf2-*.svg. Discontinuities found BY SCRIPT and taught: ETF
  1:10 unit split 26 Sep 2023; ETF ~₹40.89 payout 25 Feb 2021 (not a growth
  plan — comparisons use payout-reinvested NAV); overnight fund face value
  ₹10→₹1,000 on 3 May 2018 AND its pre-2018 history is not an overnight
  portfolio, so the debt comparison starts May 2018; money market fund face
  value change 22 Aug 2009. Findings: overnight fund 0% down days 2018–26 vs
  gilt 40%; gilt 20y max drawdown −16.05% (2009), 1,125 days to recover;
  trailing-3y return of the index fund ranged −4.8% to +32.0%, past-3y vs
  next-3y correlation 0.05 (the star-ratings post); SWP ₹1cr/₹50k from Jan
  2008 never regained ₹1cr, from Jan 2010 → ₹2.19cr. VERIFY: SEBI category
  thresholds in mf2.yml `categories:` typed from memory of the 2017 circular;
  overnight mandate start date inferred from the face-value change.
- R6 Tax add-ons (4): 12-14 esops-and-rsus, 12-15 buyback-taxation, 12-16
  fo-is-business-income, 12-17 foreign-stocks-and-schedule-fa.
  scripts/derive_tax2.py → _data/tax2.yml (a `verification` block per topic
  with source URLs, verification date Sept 2026, and recorded disagreements).
  Rules: ESOP perquisite at exercise (FMV − price, salary/TDS; section 192 →
  392 under the 2025 Act), CG on sale from that FMV, 24-month/12.5%/no
  exemption for foreign or unlisted, startup deferral only DPIIT+IMB (80-IAC).
  Buyback regimes: to 30 Sep 2024 company-paid 23.296%; 1 Oct 2024–31 Mar
  2026 deemed dividend at slab + cost as capital loss; from 1 Apr 2026 capital
  gains (Finance Act 2026) with promoter additional tax to 22%/30%. F&O:
  non-speculative business income, turnover = Σ|trade P&L| (ICAI), audit
  > ₹10 cr digital, presumptive 6% to ₹3 cr (no loss under presumptive),
  losses vs any head except salary, 8-year carry-forward only with a timely
  ITR-3. Foreign: 24-month LTCG 12.5% no exemption, US 25% withholding via
  Form 67 + FSI/TR, Schedule FA by CALENDAR year with no minimum, BMA ₹10 lakh
  penalty waived under ₹20 lakh aggregate but disclosure still due, LRS TCS
  20% above ₹10 lakh. PROFESSIONAL REVIEW NEEDED (also listed in tax2.yml):
  whether the ₹1.25 lakh exemption applies to post-Apr-2026 buyback gains;
  promoter definition for unlisted companies; ESOP deferral "48 months from
  end of AY"; the 1 Apr 2026 STT hike (single source); the two exchange-rate
  date conventions. Primary statute text still unfetchable.
- R7 TA module 2 (4): 12-18 bollinger-bands-and-atr, 12-19
  relative-strength-vs-the-index, 12-20 multiple-timeframe-analysis, 12-21
  how-to-backtest-honestly (the series' closing capstone, ~2,000 words).
  scripts/derive_ta2.py → _data/ta2.yml; scripts/make_ta2_charts.py →
  assets/charts/ta2-*.svg. Findings (kept honest): closes above the upper
  Bollinger band were followed by +0.92% avg over 10 sessions — the reversal
  reading points the wrong way in this sample; only 6 daily-oversold events,
  the one inside a weekly "uptrend" fell −12.6%; backtest (next-day fills,
  0.1%/side, Jan 2025–Mar 2026): buy-and-hold +8.9% CAGR, SMA 50/200 −2.8%,
  SMA 20/50 −25.2%, RSI 30/70 +14.5% on 3 trades / 12% time invested;
  parameter grid 32.5pp spread, 0 of 15 SMA pairs beat buy-and-hold. VERIFY:
  eyeball the four SVGs in a browser (not rasterised locally).
- Cross-module links: R5 post_urls three R4 posts (tracking error, modified
  duration, face value), R6 post_urls RISK-1; everything else forward is prose.
  All checked backward-dated by scripts/check_posts.py.

Lower-priority, not done (say the word if you want these next)

- DONE: Series index pages. /series/ lists every track in _data/series.yml
  with a live published-post count (the count of series is rendered from the
  data too, so adding a sixth series cannot leave stale copy behind); /series/<slug>/ lists that series' posts in reading
  order (oldest first, since these are learning series). Built from
  _data/series.yml plus each post's `series:` front matter, so adding a post
  needs no page edits. New: _layouts/series.html, series.markdown, and
  series/<slug>.markdown x4, plus styles in assets/main.scss.
  - Note: minima's header auto-lists EVERY titled page, so `header_pages` is
    now set explicitly in _config.yml (Series, Case study, About, Privacy).
    The four individual series pages are deliberately NOT in the top nav —
    they're reached from /series/. If you add a page and it doesn't appear in
    the nav, that's why.
- Formula rendering (MathJax/KaTeX) if you want real math notation rather than code-block formulas.
- Minor: minima's bundled SCSS throws harmless Dart-Sass deprecation warnings during build (lighten() is deprecated) — cosmetic build noise, not a bug, will resolve itself on minima's next release.
