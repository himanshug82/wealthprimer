---
layout: page
title: "The Desi Bites Foods case study"
permalink: /case-study/
---

{% assign c = site.data.case_study %}

Every post in the [Jargon, Decoded]({{ '/' | relative_url }}) series that needs a
worked example uses the same fictional company, so the numbers stay familiar as you
move from one concept to the next. This page is the reference — individual posts
link back here instead of re-explaining the business or re-pasting the statements.

**{{ c.company.name }}** is not a real company — it's a fictional packaged
namkeen & snacks manufacturer, built as a fully reconciled three-statement model
(the balance sheet balances every year; the cash flow statement ties exactly to the
balance sheet's cash figure) so the arithmetic behind every ratio actually works out
the way it would for a real business. Nothing on this page is investment advice —
see the [privacy & disclaimer policy]({{ '/privacy/' | relative_url }}).

## The business

Desi Bites makes packaged namkeen and snacks, sold under its own brand to
distributors across a few states. One manufacturing unit, one product line, nothing
exotic — no subsidiaries, no foreign currency, no complex segments. It sells to
distributors on roughly 30 days' credit and buys raw material (edible oil, flour,
spices, packaging) on roughly 40 days' credit. A term loan funded a plant expansion,
drawn further in FY24 and being paid down since. All figures below are in
**₹ Lakh**, for the year ended {{ c.company.fiscal_year_end }}.

## Income Statement

| | FY23 | FY24 | FY25 |
|---|---:|---:|---:|
| Revenue | {{ c.income_statement.FY23.revenue }} | {{ c.income_statement.FY24.revenue }} | {{ c.income_statement.FY25.revenue }} |
| COGS | {{ c.income_statement.FY23.cogs }} | {{ c.income_statement.FY24.cogs }} | {{ c.income_statement.FY25.cogs }} |
| **Gross Profit** | {{ c.income_statement.FY23.gross_profit }} | {{ c.income_statement.FY24.gross_profit }} | {{ c.income_statement.FY25.gross_profit }} |
| Operating expenses | {{ c.income_statement.FY23.opex }} | {{ c.income_statement.FY24.opex }} | {{ c.income_statement.FY25.opex }} |
| **EBITDA** | {{ c.income_statement.FY23.ebitda }} | {{ c.income_statement.FY24.ebitda }} | {{ c.income_statement.FY25.ebitda }} |
| Depreciation | {{ c.income_statement.FY23.depreciation }} | {{ c.income_statement.FY24.depreciation }} | {{ c.income_statement.FY25.depreciation }} |
| **EBIT** | {{ c.income_statement.FY23.ebit }} | {{ c.income_statement.FY24.ebit }} | {{ c.income_statement.FY25.ebit }} |
| Interest | {{ c.income_statement.FY23.interest }} | {{ c.income_statement.FY24.interest }} | {{ c.income_statement.FY25.interest }} |
| **PBT** | {{ c.income_statement.FY23.pbt }} | {{ c.income_statement.FY24.pbt }} | {{ c.income_statement.FY25.pbt }} |
| Tax | {{ c.income_statement.FY23.tax }} | {{ c.income_statement.FY24.tax }} | {{ c.income_statement.FY25.tax }} |
| **PAT (Net Profit)** | {{ c.income_statement.FY23.pat }} | {{ c.income_statement.FY24.pat }} | {{ c.income_statement.FY25.pat }} |
| Dividend paid | {{ c.income_statement.FY23.dividend }} | {{ c.income_statement.FY24.dividend }} | {{ c.income_statement.FY25.dividend }} |

## Balance Sheet

| | FY22 (opening) | FY23 | FY24 | FY25 |
|---|---:|---:|---:|---:|
| Net fixed assets | {{ c.balance_sheet.FY22.net_fixed_assets }} | {{ c.balance_sheet.FY23.net_fixed_assets }} | {{ c.balance_sheet.FY24.net_fixed_assets }} | {{ c.balance_sheet.FY25.net_fixed_assets }} |
| Inventory | {{ c.balance_sheet.FY22.inventory }} | {{ c.balance_sheet.FY23.inventory }} | {{ c.balance_sheet.FY24.inventory }} | {{ c.balance_sheet.FY25.inventory }} |
| Trade receivables | {{ c.balance_sheet.FY22.receivables }} | {{ c.balance_sheet.FY23.receivables }} | {{ c.balance_sheet.FY24.receivables }} | {{ c.balance_sheet.FY25.receivables }} |
| Cash & bank | {{ c.balance_sheet.FY22.cash }} | {{ c.balance_sheet.FY23.cash }} | {{ c.balance_sheet.FY24.cash }} | {{ c.balance_sheet.FY25.cash }} |
| **Total Assets** | {{ c.balance_sheet.FY22.total_assets }} | {{ c.balance_sheet.FY23.total_assets }} | {{ c.balance_sheet.FY24.total_assets }} | {{ c.balance_sheet.FY25.total_assets }} |
| Equity (capital + reserves) | {{ c.balance_sheet.FY22.equity }} | {{ c.balance_sheet.FY23.equity }} | {{ c.balance_sheet.FY24.equity }} | {{ c.balance_sheet.FY25.equity }} |
| Term loan | {{ c.balance_sheet.FY22.term_loan }} | {{ c.balance_sheet.FY23.term_loan }} | {{ c.balance_sheet.FY24.term_loan }} | {{ c.balance_sheet.FY25.term_loan }} |
| Trade payables | {{ c.balance_sheet.FY22.payables }} | {{ c.balance_sheet.FY23.payables }} | {{ c.balance_sheet.FY24.payables }} | {{ c.balance_sheet.FY25.payables }} |
| Other current liabilities* | {{ c.balance_sheet.FY22.other_current_liabilities }} | {{ c.balance_sheet.FY23.other_current_liabilities }} | {{ c.balance_sheet.FY24.other_current_liabilities }} | {{ c.balance_sheet.FY25.other_current_liabilities }} |
| **Total Liabilities + Equity** | {{ c.balance_sheet.FY22.total_liab_eq }} | {{ c.balance_sheet.FY23.total_liab_eq }} | {{ c.balance_sheet.FY24.total_liab_eq }} | {{ c.balance_sheet.FY25.total_liab_eq }} |

\* tax payable and accrued expenses, bundled into one line for simplicity — a real
filing splits these out further, and splits the term loan into its current and
non-current portions. Equity Share Capital is a constant ₹100L the whole way
through (10 lakh shares of ₹10 face value), set up now so per-share numbers have
clean figures to work with once the valuation posts introduce a hypothetical
listing.

## Cash Flow Statement

| | FY23 | FY24 | FY25 |
|---|---:|---:|---:|
| Cash from Operations | {{ c.cash_flow.FY23.cfo }} | {{ c.cash_flow.FY24.cfo }} | {{ c.cash_flow.FY25.cfo }} |
| Cash from Investing | {{ c.cash_flow.FY23.cfi }} | {{ c.cash_flow.FY24.cfi }} | {{ c.cash_flow.FY25.cfi }} |
| Cash from Financing | {{ c.cash_flow.FY23.cff }} | {{ c.cash_flow.FY24.cff }} | {{ c.cash_flow.FY25.cff }} |
| **Net change in cash** | {{ c.cash_flow.FY23.net_change }} | {{ c.cash_flow.FY24.net_change }} | {{ c.cash_flow.FY25.net_change }} |
| Closing cash | {{ c.cash_flow.FY23.closing_cash }} | {{ c.cash_flow.FY24.closing_cash }} | {{ c.cash_flow.FY25.closing_cash }} |

Built with a simplified indirect method — starting from PAT and adjusting for
depreciation and working-capital movements — rather than a full Ind-AS
presentation. Good enough to show how the three statements connect, which is the
point of a case study like this.

## A note on the numbers

These statements were built as a single reconciled model, not typed in separately —
the balance sheet balances to zero in every year (including the FY22 opening
position) and cash flow ties exactly to the balance sheet's cash figure. If a post
ever shows a ratio that doesn't match what you calculate from these tables, that's a
bug — [let us know]({{ '/privacy/' | relative_url }}).
