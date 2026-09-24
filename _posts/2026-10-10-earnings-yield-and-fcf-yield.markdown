---
layout: post
title: "Earnings yield and FCF yield: the P/E turned upside down"
description: "Earnings yield is the P/E flipped into a percentage you can hold beside a bond. Britannia's 64.7x P/E is a 1.55% yield against a 6.5% G-Sec; what the gap means."
image: /assets/og/earnings-yield-and-fcf-yield.png
date: 2026-10-10 09:00:00 +0530
series: jargon
term: "Earnings yield and FCF yield"
---

{% assign y = site.data.jargon_m6.yields %}
{% assign b = y.britannia %}
{% assign d = y.desi_bites %}

## What the two yields mean

The [P/E post]({% post_url 2026-09-24-price-to-earnings %}) asked "how many
years of earnings am I paying for?" **Earnings yield** asks the same question
the other way round: *what percentage of my purchase price does the company
earn each year?* It is simply EPS divided by price — the P/E inverted and
expressed as a percentage.

The reason to bother is comparison. A P/E of 40 is hard to weigh against
anything else. A 2.5% earnings yield sits naturally beside a 6.5% government
bond, a 7% fixed deposit, or a 1.3% dividend yield — all of them "what does
this pay me per rupee" numbers.

**FCF yield** does the same thing with
[free cash flow]({% post_url 2026-09-19-free-cash-flow %}) instead of
accounting profit: cash the business actually generated after capex (capital
expenditure), divided
by market capitalisation. It is the stricter of the two, for the reasons the
[OCF/PAT post]({% post_url 2026-09-20-ocf-pat %}) laid out — profit is an
opinion, cash is a fact. Strictly, free cash flow before interest belongs to
lenders as well as shareholders, so it pairs more consistently with
[enterprise value]({% post_url 2026-09-26-ev-ebitda %}) than with market cap; the market-cap version is the
common shortcut, and for companies with little net debt, like both here, the
two barely differ.

## The formula

```
Earnings yield  =  EPS / Price            =  1 / (P/E)

FCF yield       =  Free cash flow / Market cap
```

## Worked example: Desi Bites Foods Ltd, at listing

From the [case study](/case-study/): IPO price ₹{{ d.price }}, FY25 post-issue EPS
₹{{ d.eps_diluted }}, FY25 free cash flow ₹{{ d.fcf_lakh }} lakh, market cap
₹{% include inr.html n=d.market_cap_lakh %} lakh.

| | |
|---|---:|
| P/E (post-issue) | {{ d.pe }}x |
| **Earnings yield** = {{ d.eps_diluted }} / {{ d.price }} | **{{ d.earnings_yield_pct }}%** |
| **FCF yield** = {{ d.fcf_lakh }} / {% include inr.html n=d.market_cap_lakh %} | **{{ d.fcf_yield_pct }}%** |
| 10-year G-Sec (Government of India bond) yield (illustrative, from the WACC post) | {{ y.gsec_yield_pct }}% |

## Worked example: Britannia Industries

Price ₹{% include inr.html n=b.price %} (NSE close, {{ b.price_date }}; source: Yahoo Finance
historical data), against FY25 financials from the
[audited results](https://media.britannia.co.in/Audited_Consolidated_Financial_Results_31_03_2025_74a7c03628.pdf).
For illustration only.

| | |
|---|---:|
| P/E | {{ b.pe }}x |
| **Earnings yield** = {{ b.eps }} / {% include inr.html n=b.price %} | **{{ b.earnings_yield_pct }}%** |
| FCF (₹ crore) / market cap (₹ crore) | {% include inr.html n=b.fcf_cr %} / {% include inr.html n=b.market_cap_cr %} |
| **FCF yield** | **{{ b.fcf_yield_pct }}%** |
| Dividend yield (from the [dividend yield post]({% post_url 2026-09-28-dividend-yield %})) | {{ b.dividend_yield_pct }}% |
| 10-year G-Sec yield (illustrative) | {{ y.gsec_yield_pct }}% |

## What the gap to the bond means — and doesn't

A {{ b.earnings_yield_pct }}% earnings yield next to a {{ y.gsec_yield_pct }}% bond looks like a terrible deal, and
that reading is half right. It *is* the market saying it expects Britannia's
earnings to grow substantially — enough that the yield on today's price
catches up with and overtakes the bond's fixed coupon in the years ahead. A
bond's yield never grows. A company's earnings can.

Which is exactly why the comparison is useful and exactly why it isn't a
verdict. It converts a valuation into a *growth expectation* you can look at
directly: "this price only makes sense if earnings compound at roughly X% for
Y years." The [reverse DCF]({% post_url 2026-10-01-margin-of-safety-and-sensitivity %})
did that for Desi Bites. Whether the expectation is reasonable is the
analyst's job; the yield just states it plainly.

Notice also that Britannia's FCF yield ({{ b.fcf_yield_pct }}%) sits close to its earnings
yield ({{ b.earnings_yield_pct }}%) — the two agree because its cash conversion is close to
1x. When FCF yield is far *below* earnings yield, profit isn't turning into
cash and the earnings yield is flattering. When it's far *above*, capex is
unusually low (or working capital was released), and the FCF yield may be the
one that's flattering — the [capex intensity post]({% post_url 2026-09-21-capex-intensity %})
showed Britannia's FY25 FCF rose mainly because capex fell.

Desi Bites shows the other direction: its FCF yield ({{ d.fcf_yield_pct }}%) is above its earnings
yield ({{ d.earnings_yield_pct }}%) because FY25 free cash flow (₹{{ d.fcf_lakh }} lakh) was larger than PAT
(₹{{ site.data.case_study.income_statement.FY25.pat }} lakh) — operating cash flow came in at {{ site.data.case_study.ratios.FY25.ocf_pat }}x profit, more than
covering that year's capex.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Two piggy banks cost ₹100 each. The first one hands you ₹6.50 every year,
forever, the same amount. The second one hands you ₹1.55 this year — but
promises the amount will grow.

The second only makes sense if it really does grow, and keeps growing, for
years. Earnings yield just tells you how big the *first* year's coin is, so you
can see how much growing it has to do.

</details>

## Common mistakes

- **Treating earnings yield below the bond yield as "overvalued".** It means
  growth is priced in. Whether enough growth arrives is the question, not the
  answer.
- **Using pre-issue EPS after a fresh issue.** Same trap as the
  [EPS post]({% post_url 2026-09-23-eps %}) — Desi Bites' figure above uses
  the post-issue share count.
- **Reading a high FCF yield as cheap without checking why.** A capex holiday
  inflates one year's FCF. Look at capex intensity over several years.
- **Comparing yields across countries without adjusting for rates.** A 4%
  earnings yield means something different where bonds pay 1% than where they
  pay 7%.

**Takeaway:** earnings yield is the P/E flipped into a percentage you can hold
beside a bond, and FCF yield is the same idea on cash instead of profit. The
gap to the bond isn't a verdict; it's the growth the price is assuming, stated
in a unit you can actually think about.
