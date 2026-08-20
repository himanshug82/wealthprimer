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
- M5 (Valuation / Market) needs a "Desi Bites goes public" narrative beat
  designed before any posts can be drafted — a listing price, share count,
  and market cap for the fictional company — plus real Britannia share
  price/valuation data (P/E, P/B, EV/EBITDA etc. need a market price,
  which is different from the financial-statement data used so far and
  will need its own lagged, cited, as-of date). Don't start M5 without
  first deciding the listing narrative with the user.

Lower-priority, not done (say the word if you want these next)

- Series index pages — _data/series.yml has the four series, titles, slugs as a source of truth, but there's no /series/fundamental-analysis/ listing page yet.
- Analytics (GA4/Plausible/GoatCounter) — not added, your call which one.
- Formula rendering (MathJax/KaTeX) if you want real math notation rather than code-block formulas.
- Minor: minima's bundled SCSS throws harmless Dart-Sass deprecation warnings during build (lighten() is deprecated) — cosmetic build noise, not a bug, will resolve itself on minima's next release.
