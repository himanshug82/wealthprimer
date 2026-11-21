---
layout: home
seo_title: "Wealth Primer: financial education for Indian investors"
description: "Learn to read a company, judge a mutual fund, size up risk and see how tax applies, with worked examples on real Indian data. Education, never stock tips."
# Homepage option A, problem-first (decided 21 Nov 2026; WEALTH_PRIMER_MASTER_PLAN.md §5).
# _layouts/home.html draws the page from these lists, so cards change here, not in the layout.
#
# goals: the "What are you trying to do?" cards. Point each at its flagship guide once it
# exists (/guides/<id>/), and at the journey page until then.
goals:
  - section: "Learn"
    title: "Understand a term I keep seeing"
    examples: "P/E, NAV, XIRR, ROCE, open interest"
    cta: "Browse the glossary"
    url: /glossary/
  - section: "Analyse"
    title: "Judge a mutual fund by its numbers"
    examples: "Returns measured properly, costs, drawdowns, factsheets"
    cta: "Guide to mutual funds"
    url: /guides/mutual-funds/
  - section: "Analyse"
    title: "Read a company's financial statements"
    examples: "Balance sheet, P&L, cash flow, ratios, valuation"
    cta: "Start with the statements"
    url: /analyse/
  - section: "Portfolio"
    title: "Build and look after a portfolio"
    examples: "Diversification, overlap, real returns, rebalancing"
    cta: "Portfolio basics"
    url: /portfolio/
  - section: "Risk & Tax"
    title: "Know the risk, and the tax, before I act"
    examples: "Losses, leverage, F&O data, capital gains"
    cta: "Risk and tax"
    url: /risk-and-tax/
# featured_tools: ids from _data/tools.yml, with a one-line blurb for the card.
featured_tools:
  - id: rolling-returns
    blurb: "Every 1, 3 or 5-year return a fund gave, not one flattering window"
  - id: sip-xirr
    blurb: "What a monthly SIP became, and its true annual return"
  - id: cost-drag
    blurb: "What the direct vs regular expense gap costs over the years"
  - id: loss-recovery
    blurb: "Why a 50% fall needs a 100% gain, with and without leverage"
---
