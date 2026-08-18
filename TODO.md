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
- Real-world anchor company for the "real example" half of each post: Britannia
  Industries (proposed, not yet confirmed by name — swap if you'd rather use a
  different company). Needs actual filings/price data at least 3 months old at
  publish time, per the SEBI-lag rule in CLAUDE.md.
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
- Not yet started: drafting the actual M0 posts.

Lower-priority, not done (say the word if you want these next)

- Series index pages — _data/series.yml has the four series, titles, slugs as a source of truth, but there's no /series/fundamental-analysis/ listing page yet.
- Analytics (GA4/Plausible/GoatCounter) — not added, your call which one.
- Formula rendering (MathJax/KaTeX) if you want real math notation rather than code-block formulas.
- Minor: minima's bundled SCSS throws harmless Dart-Sass deprecation warnings during build (lighten() is deprecated) — cosmetic build noise, not a bug, will resolve itself on minima's next release.
