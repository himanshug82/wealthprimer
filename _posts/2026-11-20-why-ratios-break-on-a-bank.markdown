---
layout: post
title: "Why P/E and D/E break on a bank: the balance sheet is the business"
description: "Debt-to-equity, EBITDA and the current ratio mean nothing for a bank. What a bank sells, how its P&L is built, and which ratios replace the ones you know."
image: /assets/og/why-ratios-break-on-a-bank.png
date: 2026-11-20 09:00:00 +0530
series: fundamental-analysis
term: "Net interest income (NII)"
---

{% assign b = site.data.real_bank %}
{% assign f25 = b.reported.FY25 %}
{% assign f24 = b.reported.FY24 %}
{% assign seg = b.segments_fy25 %}
{% assign fixed_and_other = f25.fixed_assets | plus: f25.other_assets %}
{% assign de_like = f25.deposits | plus: f25.borrowings | divided_by: f25.shareholders_equity | round: 1 %}
{% assign pat_share_pct = f25.pat | times: 100 | divided_by: f25.interest_earned | round: 0 %}

## The toolkit you've built doesn't fit

Thirty-three ratio posts, a DuPont tree, a DCF — and if you open the results
of a bank and try to use any of it, almost everything either returns a
meaningless number or can't be computed at all.

Try [debt-to-equity]({% post_url 2026-09-15-debt-to-equity %}) on HDFC Bank.
Deposits plus borrowings come to about ₹{% include inr.html n=f25.deposits %}
crore plus ₹{% include inr.html n=f25.borrowings %} crore, against
shareholders' equity of ₹{% include inr.html n=f25.shareholders_equity %}
crore. That is a "D/E" of roughly {{ de_like }}.
For a snacks manufacturer that number would mean insolvency by lunchtime. For
a bank it is simply a description of what a bank is.

Try [EBITDA margin]({% post_url 2026-08-28-ebitda-margin %}). A bank has no
"revenue" in the sense a manufacturer does, and interest — the thing EBITDA
strips out as a financing cost — *is* the bank's raw-material cost. Strip it
out and there is nothing left to analyse.

[Current ratio]({% post_url 2026-09-13-current-ratio %})? Almost all of a
bank's liabilities are deposits repayable on demand, and most of its assets
are loans due over years. Every bank on earth has a "current ratio" that
would fail the test, by design.
[Inventory days]({% post_url 2026-09-07-inventory-days %})? There is no
inventory.

This module — six posts — is about the toolkit that replaces those. It uses
HDFC Bank's FY25 standalone results the way the earlier posts used Britannia's:
a real filing to compute from, not a company to form a view on.

## What a bank actually sells

A manufacturer buys inputs, transforms them, sells the output, and keeps the
difference. A bank does the same thing with money.

- Its **raw material** is other people's money: deposits (the vast majority)
  and borrowings. It pays for that money — interest expended.
- Its **product** is credit: loans and advances, plus a book of investments
  (largely government bonds). It is paid for that — interest earned.
- The **gross profit** is the gap between the two: **Net Interest Income
  (NII)**.

```
Net interest income (NII)  =  Interest earned  −  Interest expended
```

Then, like any business, it has operating costs (branches, staff,
technology), and a cost that is unique to lending: some loans don't come
back. Money set aside for those is **provisions**.

```
Pre-provision operating profit  =  NII + Other income − Operating expenses
Profit before tax               =  Pre-provision operating profit − Provisions
```

"Other income" is everything the bank earns that isn't interest — fees,
commissions, treasury gains, forex. For a large bank it is a big number in
its own right.

## HDFC Bank, FY25: the P&L built from the top

From HDFC Bank's [results for the year ended 31 March 2025]({{ b.company.source_url }})
(standalone, audited; released 21 April 2025). ₹ crore. Historical figures,
for illustration only.

| | FY25 | FY24 |
|---|---:|---:|
| Interest earned | {% include inr.html n=f25.interest_earned %} | {% include inr.html n=f24.interest_earned %} |
| − Interest expended | {% include inr.html n=f25.interest_expended %} | {% include inr.html n=f24.interest_expended %} |
| **= Net interest income** | **{% include inr.html n=f25.net_interest_income %}** | **{% include inr.html n=f24.net_interest_income %}** |
| + Other income | {% include inr.html n=f25.other_income %} | {% include inr.html n=f24.other_income %} |
| − Operating expenses | {% include inr.html n=f25.operating_expenses %} | {% include inr.html n=f24.operating_expenses %} |
| **= Pre-provision operating profit** | **{% include inr.html n=f25.pre_provision_operating_profit %}** | **{% include inr.html n=f24.pre_provision_operating_profit %}** |
| − Provisions and contingencies | {% include inr.html n=f25.provisions_and_contingencies %} | {% include inr.html n=f24.provisions_and_contingencies %} |
| − Tax | {% include inr.html n=f25.tax %} | {% include inr.html n=f24.tax %} |
| **= Profit after tax** | **{% include inr.html n=f25.pat %}** | **{% include inr.html n=f24.pat %}** |

![How a bank's profit is built]({{ '/assets/charts/bank-pnl-waterfall.svg' | relative_url }})

Two things to notice, because they recur through this module.

First, the scale of the funnel. Interest earned is
₹{% include inr.html n=f25.interest_earned %} crore; what survives to
shareholders is ₹{% include inr.html n=f25.pat %} crore — about {{ pat_share_pct }}%.
A bank is a thin-margin business operating on an enormous base, which is why
a shift of half a percentage point in any one line matters so much.

Second, look at the provisions row. It **halved** between FY24 and FY25
({{ b.derived_fy25.provisions_change_pct }}%), while pre-provision profit grew
only {{ b.derived_fy25.ppop_growth_pct }}%. Profit after tax grew
{{ b.derived_fy25.pat_growth_pct }}% — and a good part of that growth came
from the provisions line, not the lending line. FY24's figure included a
one-off ₹{% include inr.html n=f24.floating_provision %} crore "floating"
provision the bank chose to make; FY25's didn't. The fourth post in this
module is about exactly this: a bank's profit is partly a *decision*.

## The balance sheet is the business

For a manufacturer, the balance sheet is the machinery that makes the
product. For a bank, the balance sheet *is* the product. The loans are the
sales; the deposits are the cost of goods.

![A bank's balance sheet]({{ '/assets/charts/bank-balance-sheet.svg' | relative_url }})

| Funding (liabilities) | ₹ crore | Deployed as (assets) | ₹ crore |
|---|---:|---|---:|
| Deposits | {% include inr.html n=f25.deposits %} | Advances (loans) | {% include inr.html n=f25.advances %} |
| Borrowings | {% include inr.html n=f25.borrowings %} | Investments | {% include inr.html n=f25.investments %} |
| Other liabilities | {% include inr.html n=f25.other_liabilities %} | Cash and balances with RBI | {% include inr.html n=f25.cash_with_rbi %} |
| Employee stock options outstanding | {% include inr.html n=f25.esop_outstanding %} | Balances with banks and call money | {% include inr.html n=f25.balances_with_banks_call_money %} |
| Shareholders' equity | {% include inr.html n=f25.shareholders_equity %} | Fixed and other assets | {% include inr.html n=fixed_and_other %} |
| **Total** | **{% include inr.html n=f25.total_assets %}** | **Total** | **{% include inr.html n=f25.total_assets %}** |

Equity is {{ f25.equity_to_assets_pct }}% of the balance sheet. Put
differently, every ₹1 of shareholders' money supports about
₹{{ f25.leverage_assets_to_equity }} of assets. That leverage is not a
warning sign; it is the engine. The whole of banking regulation — the
subject of the fifth post — exists to decide how thin that slice of equity is
allowed to get.

And this is why the ordinary ratios fail. They were built for a company whose
liabilities are a *funding choice* and whose assets are *tools*. A bank's
liabilities are its inventory and its assets are its sales ledger. Same words
on the page, different objects underneath.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Imagine a friend who borrows ₹100 from ten classmates, promising each of them
₹5 at the end of the year, and lends the ₹1,000 to older kids who promise to
pay back ₹1,090.

At the end of the year your friend collects ₹1,090, pays the classmates
₹1,050, and keeps ₹40. That ₹40 is net interest income. If one older kid
doesn't pay back, the ₹40 disappears fast — that's what provisions are for.

Now: your friend "owes" ₹1,000 and owns maybe ₹50 of their own money. Is your
friend drowning in debt? No — owing lots of money to lots of people and
lending it on *is the entire business*. You judge them by whether the older
kids pay back, not by how much they owe the classmates.

</details>

## Where the revenue comes from

HDFC Bank reports its revenue by business line. FY25, ₹ crore:

| Segment | Revenue | Share |
|---|---:|---:|
| Retail banking | {% include inr.html n=seg.retail_banking %} | {{ seg.retail_banking | times: 100 | divided_by: seg.total | round: 0 }}% |
| Wholesale banking | {% include inr.html n=seg.wholesale_banking %} | {{ seg.wholesale_banking | times: 100 | divided_by: seg.total | round: 0 }}% |
| Treasury | {% include inr.html n=seg.treasury %} | {{ seg.treasury | times: 100 | divided_by: seg.total | round: 0 }}% |
| Other banking operations | {% include inr.html n=seg.other_banking_operations %} | {{ seg.other_banking_operations | times: 100 | divided_by: seg.total | round: 0 }}% |

(Segment revenue totals more than the P&L's interest earned plus other income
because it includes inter-segment transfers — treasury "sells" funding to the
lending businesses internally. Read it for proportions, not absolute size.)

## The replacement toolkit

Here is the map for the rest of this module: for each ratio that breaks, the
one that does the same job for a bank.

| Manufacturer ratio | What it asked | Bank equivalent | Post |
|---|---|---|---|
| [Gross margin]({% post_url 2026-08-26-gross-margin %}) | What survives the cost of inputs? | Net interest margin (NIM) | 2 |
| Cost of raw material | How cheap are the inputs? | Cost of funds; CASA ratio | 2, 3 |
| [Debtor days]({% post_url 2026-09-08-debtor-days %}) | Are customers paying? | Gross and net NPA, provision coverage, credit cost | 4 |
| [Debt-to-equity]({% post_url 2026-09-15-debt-to-equity %}), [interest coverage]({% post_url 2026-09-17-interest-coverage %}) | Can it survive a shock? | Capital adequacy ratio (CAR), CET1 | 5 |
| [P/E]({% post_url 2026-09-24-price-to-earnings %}), EV/EBITDA | What is the market paying? | Price-to-book, anchored on ROE | 6 |

Two old ratios survive nearly intact, because they were about the whole
balance sheet to begin with: [ROA]({% post_url 2026-09-05-roa %}) and
[ROE]({% post_url 2026-09-01-roe %}). For a bank, ROA is the honest measure
of how well it lends and ROE is what leverage does to that — the
[DuPont]({% post_url 2026-09-30-dupont-roe-decomposition %}) logic with the
asset-turnover term collapsed to almost nothing. The sixth post leans on both.

## Common mistakes

- **Screening banks on debt-to-equity or "high debt."** Every screener will
  show a bank as the most indebted company in its universe. It means nothing.
  Look at capital adequacy instead.
- **Reading a bank's "other income" as a side show.** At
  {{ f25.other_income_share_pct }}% of operating income for HDFC Bank, fees
  and treasury are a core line, and a volatile one. Its fall in FY25 is part
  of why pre-provision profit grew only {{ b.derived_fy25.ppop_growth_pct }}%.
- **Judging a bank's year by profit after tax.** Provisions sit between
  operating profit and PAT and are partly discretionary. Pre-provision
  operating profit is the cleaner read of the underlying business; PAT tells
  you what management decided to set aside.
- **Applying a DCF.** Free cash flow to a bank is close to meaningless —
  deposit growth shows up as "cash inflow" and lending as "outflow." Bank
  valuation runs through book value and return on equity, which is where this
  module ends.

**Takeaway:** A bank's liabilities are its raw material and its loans are its
sales, so debt-to-equity, EBITDA and the current ratio describe nothing when
applied to one. Start again from the bank's own P&L — interest earned, minus
interest paid, minus costs, minus the loans that won't come back — and its
balance sheet, where ₹1 of equity supports about ₹{{ f25.leverage_assets_to_equity }}
of assets by design.
