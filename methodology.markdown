---
layout: page
title: "Data & methodology"
nav_title: "Methodology"   # short label for the header nav; `title` stays the page H1
permalink: /methodology/
description: "Where every number on Wealth Primer comes from: the audited filings, AMFI NAV history and exchange data behind each series, the 3-month lag rule, and how figures are derived rather than typed."
---

Every worked example on this blog is built on numbers you can check. This page
says where they come from, what rules they follow, and how to tell a real
figure from an illustrative one.

## The rules every post follows

1. **Educational only.** Posts explain how a ratio, chart or rule works. No post
   recommends buying, selling or holding anything, and no post publishes a
   target price or an intrinsic value for a real listed company. The full
   position is on the [privacy & disclaimer page]({{ '/privacy/' | relative_url }}).
2. **Real data is at least three months old.** Any price, NAV or financial figure
   from a real company or fund is lagged by at least three months at the time
   the post publishes — SEBI's expectation for educational content. Every post
   states the as-of date of the figures it uses.
3. **One source per dataset, cited.** Each dataset below has a single primary
   source, named in the post and in the data file. Where two independent
   sources overlap (for example, the same closing price appearing in two feeds),
   they have been cross-checked against each other.
4. **Derived, not typed.** Ratios, indicator values, rolling returns, drawdowns,
   XIRRs and tax computations are calculated by script from the committed data
   files and rendered into posts from a single data store — so a correction
   happens in one place, and a figure in a chart always matches the same figure
   in the text.

## Two companies, one fictional

Most Jargon and Fundamental Analysis posts walk through each concept twice:

- **Desi Bites Foods** is a **fictional** snacks manufacturer with a fully
  reconciled three-statement model (the balance sheet balances every year; the
  cash flow ties to the balance sheet cash). It exists so a concept can be shown
  on clean, complete numbers — including a hypothetical IPO and a full DCF,
  which would read as a price call on a real company. The whole model is at
  [/case-study/]({{ '/case-study/' | relative_url }}).
- **Britannia Industries** (NSE: BRITANNIA, BSE: 500825) is the **real** anchor,
  chosen because it is in the same broad sector. Its figures are taken from its
  own audited filing, not from a screener or aggregator.

If a number is about Desi Bites, it is made up by design. If it is about
Britannia or a named fund, it is real and sourced below.

## The datasets

| Dataset | Source | Range / as-of | Used in |
|---|---|---|---|
| Britannia Industries — audited consolidated financial results (FY25, with FY24 comparatives) | [Company filing with NSE/BSE, 8 May 2025 (PDF)]({{ site.data.real_company.source.source_url | default: "https://media.britannia.co.in/Audited_Consolidated_Financial_Results_31_03_2025_74a7c03628.pdf" }}) | Year ended 31 March 2025 | Jargon, Decoded; Fundamental Analysis |
| Britannia — share price and FY25 dividend | Yahoo Finance historical data (NSE close, 30 June 2025); stockanalysis.com (dividend) | 30 June 2025 | Jargon M5 (valuation ratios); Fundamental Analysis |
| Britannia — daily OHLCV | [Yahoo Finance, BRITANNIA.NS](https://finance.yahoo.com/quote/BRITANNIA.NS/history/) · [CSV]({{ '/assets/data/britannia-ohlcv-2024-04-to-2026-03.csv' | relative_url }}) | 1 April 2024 – 30 March 2026, 495 trading days | Technical Analysis |
| UTI Nifty 50 Index Fund — NAV history, regular (AMFI 100822) and direct (120716) plans | AMFI daily NAV via [mfapi.in](https://api.mfapi.in/mf/100822) · [CSV]({{ '/assets/data/uti-nifty50-index-fund-nav.csv' | relative_url }}) | 3 April 2006 – 31 March 2026 | Mutual Funds; Tax |
| Parag Parikh Flexi Cap — NAV history, regular (122640) and direct (122639) plans | AMFI daily NAV via [mfapi.in](https://api.mfapi.in/mf/122640) · [CSV]({{ '/assets/data/parag-parikh-flexicap-nav.csv' | relative_url }}) | To 31 March 2026 | One post only: expense ratios, comparing the fund against itself |
| Nifty 50 price index (^NSEI) — daily close | [Yahoo Finance](https://finance.yahoo.com/quote/%5ENSEI/history/) · [CSV]({{ '/assets/data/nifty50-price-index.csv' | relative_url }}) | To 31 March 2026 | Mutual Funds (benchmarks); Jargon (beta, alpha, tracking error); Technical Analysis (relative strength); Risk (correlation) |
| UTI Gilt Fund — NAV history, regular (AMFI 102510) and direct (120792) plans | AMFI daily NAV via [mfapi.in](https://api.mfapi.in/mf/102510) · [CSV]({{ '/assets/data/uti-gilt-fund-nav.csv' | relative_url }}) | 3 April 2006 – 31 March 2026 | Mutual Funds module 2 (debt funds: duration and rate cycles) |
| UTI Overnight Fund — NAV history, regular plan (AMFI 100814) | AMFI daily NAV via [mfapi.in](https://api.mfapi.in/mf/100814) · [CSV]({{ '/assets/data/uti-overnight-fund-nav.csv' | relative_url }}) | 3 April 2006 – 31 March 2026 | Mutual Funds module 2 (debt funds; STP parking) |
| UTI Money Market Fund — NAV history, regular plan (AMFI 112077) | AMFI daily NAV via [mfapi.in](https://api.mfapi.in/mf/112077) · [CSV]({{ '/assets/data/uti-money-market-fund-nav.csv' | relative_url }}) | 13 July 2009 – 31 March 2026 | Mutual Funds module 2 (debt funds) |
| UTI Nifty 50 ETF — NAV history (AMFI 135320) | AMFI daily NAV via [mfapi.in](https://api.mfapi.in/mf/135320) · [CSV]({{ '/assets/data/uti-nifty50-etf-nav.csv' | relative_url }}) | 2 September 2015 – 31 March 2026 (NAV only; no market-price series) | Mutual Funds module 2 (index fund vs ETF) |
| HDFC Bank Ltd — standalone audited results (FY25, with FY24 comparatives) | [Results release for the quarter and year ended 31 March 2025, filed as a Form 6-K exhibit with the US SEC, 21 April 2025](https://www.sec.gov/Archives/edgar/data/1144967/000119312525087787/d930582dex99.htm) | Year ended 31 March 2025 | Fundamental Analysis (banks and NBFCs module) |
| SEBI studies of individual traders in equity derivatives | [SEBI, Jan 2023 study](https://www.sebi.gov.in/reports-and-statistics/research/jan-2023/study-analysis-of-profit-and-loss-of-individual-traders-dealing-in-equity-fando-segment_67525.html); [SEBI press release 37/2024](https://www.sebi.gov.in/media-and-notifications/press-releases/sep-2024/updated-sebi-study-reveals-93-of-individual-traders-incurred-losses-in-equity-fando-between-fy22-and-fy24-aggregate-losses-exceed-1-8-lakh-crores-over-three-years_86906.html); [SEBI, Aug 2026 FY25–FY26 study](https://www.sebi.gov.in/reports-and-statistics/research/aug-2026/study-profitability-of-individual-traders-in-the-equity-derivatives-segment-fy25-fy26-_103835.html) (headline figures from SEBI's own pages; several detail figures from two independent secondary reports of the study, flagged as such in the data file) | FY22 – FY26 | Risk series (F&O reality check); Tax (F&O as business income) |
| Indian capital-gains, dividend and interest tax rules | Public sources, verified August 2026 (Budget 2026 position; Income-tax Act, 2025 in force from 1 April 2026) | Financial year 2026-27 | Tax |
| UTI hybrid and arbitrage funds — NAV history: Aggressive Hybrid (AMFI 100684/120674), Equity Savings (144484/144490), Balanced Advantage (151882), Arbitrage (104075/120795) | AMFI daily NAV via [mfapi.in](https://api.mfapi.in/mf/100684) · [CSV]({{ '/assets/data/uti-aggressive-hybrid-fund-nav.csv' | relative_url }}) · [CSV]({{ '/assets/data/uti-equity-savings-fund-nav.csv' | relative_url }}) · [CSV]({{ '/assets/data/uti-balanced-advantage-fund-nav.csv' | relative_url }}) · [CSV]({{ '/assets/data/uti-arbitrage-fund-nav.csv' | relative_url }}) | From each fund's first NAV to 31 March 2026 | Mutual Funds (module 3) |
| Navi Nifty 50 Index Fund — NAV history, regular (AMFI 149040) and direct (149039) | AMFI daily NAV via [mfapi.in](https://api.mfapi.in/mf/149040) · [CSV]({{ '/assets/data/navi-nifty50-index-fund-nav.csv' | relative_url }}) | 16 July 2021 to 31 March 2026 | Mutual Funds (NFOs) |
| USD/INR — RBI reference rate (to 9 July 2018), then FBIL reference rate | RBI and FBIL published reference rates · [CSV]({{ '/assets/data/usd-inr-reference-rate.csv' | relative_url }}) | 2 January 2006 to 30 March 2026 | Risk (currency risk) |
| USD/INR — Federal Reserve H.10 noon buying rate (DEXINUS) | [FRED](https://fred.stlouisfed.org/series/DEXINUS) · [CSV]({{ '/assets/data/usd-inr-fred-dexinus.csv' | relative_url }}) | 3 April 2006 to 31 March 2026 | Mutual Funds (international funds) |
| Consumer Price Index, all-India combined (base 2012 and 2024) | MoSPI API · [CSV]({{ '/assets/data/cpi-all-india-combined.csv' | relative_url }}) | January 2013 to March 2026 | Risk (inflation and real returns) |
| AMFI small- and mid-cap fund stress tests (category statistics only) | AMFI disclosures · [CSV]({{ '/assets/data/amfi-small-mid-cap-stress-test-2026-03.csv' | relative_url }}) | As of March 2026 | Risk (liquidity risk) |
| Sector anchor companies — FY26 results releases (Infosys, Marico, UltraTech Cement, Dr. Reddy's, HDFC Life, Bajaj Finance, Bharti Airtel) | Each company's own results release or investor presentation, April–May 2026 (SEC 6-K exhibits for Infosys and Dr. Reddy's); the URL for every figure is in `_data/sectors.yml` | FY26 (year ended 31 March 2026) | Fundamental Analysis (sector lenses) |
| Britannia — FY25 annual report, dividend and AGM notices | Company filings (URLs in `_data/jargon_m7.yml`) | FY25; dividend record date 4 August 2025 | Jargon, Decoded (market mechanics) |
| Desi Bites Foods — three-statement model, IPO terms, DCF | Fictional, constructed for teaching | FY23–FY25 (+ FY26–FY30 forecast) | Jargon, Decoded; Fundamental Analysis |

The mutual-fund posts use an **index fund** for every calculation on purpose:
it has twenty years of history spanning the 2008 and 2020 crashes, and being
passive, nothing about the arithmetic implies a view on any manager's skill. No
post on this site ranks funds or compares one fund manager to another.

## Charts and diagrams

Every chart in the Technical Analysis and Mutual Funds series is generated by
script from the CSVs above; every schematic in the Jargon and Fundamental
Analysis posts is generated from the same case-study data the post's text
reads. Nothing is drawn by hand, so a chart cannot quietly disagree with the
number beside it.

## Known limits

- Tax posts teach mechanics and deliberately avoid leaning on section numbers,
  which were renumbered by the Income-tax Act, 2025. Rates are verified against
  public sources, not the primary text of the Act. They are not a substitute
  for a tax professional.
- Britannia's figures are for one financial year. They illustrate a
  calculation; they say nothing about the company's prospects.
- Data files are frozen at the dates above and are **not** extended toward the
  present, so that the lag rule holds on every post's publish date.

## Corrections

Found a number that doesn't reconcile? Email
[{{ site.email }}](mailto:{{ site.email }}) or open an issue on the
[site repository](https://github.com/himanshug82/wealthprimer/issues). Fixes are
made in the data file so every post that uses the figure updates together.
