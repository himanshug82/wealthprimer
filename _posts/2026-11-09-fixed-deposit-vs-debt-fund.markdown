---
layout: post
title: "Fixed deposit vs debt fund: how each one earns"
description: "A fixed deposit promises a rate; a debt fund earns interest plus price changes. How each earns, with five years of FD and fund returns side by side."
image: /assets/og/fixed-deposit-vs-debt-fund.png
date: 2026-11-09 09:00:00 +0530
series: money-before-markets
term: "Fixed deposit (FD)"
---

{% assign m = site.data.mbm %}
{% assign d = m.fd_vs_debt %}
{% assign dq = d.dicgc %}
{% assign gl = d.gilt_drawdown %}
{% assign last = d.rows | last %}

## What a fixed deposit is, and what a debt fund is

A **fixed deposit (FD)** is money you lend to a bank for a set term at a rate fixed when you open it. The bank owes you the principal plus that interest at maturity. The rate is a promise, and it is made by the bank.

A **debt fund** is a mutual fund that holds bonds and other interest-bearing securities. It promises no rate. Its **[NAV]({% post_url 2026-09-25-what-a-mutual-fund-is %})** (net asset value, the price per unit) moves with two things: the interest its holdings pay, and the changing market price of those holdings. That is the whole difference, and the rest of this post follows from it. The mechanics are in [debt funds explained]({% post_url 2026-10-12-debt-funds-explained %}).

This is part of [Money Before Markets]({{ '/series/money-before-markets/' | relative_url }}). The [emergency fund post]({% post_url 2026-11-08-emergency-fund-sizing %}) was about holding a cash buffer. This one compares two of the places money can wait.

## How they differ, property by property

| | Fixed deposit | Debt fund |
|---|---|---|
| Who sets the return | The rate fixed at opening | Interest earned plus price changes; no promise |
| Can the rupee amount fall? | Not if held to maturity | Yes; NAV can fall |
| Deposit insurance | Covered up to a limit per depositor per bank | Not covered; the Deposit Insurance and Credit Guarantee Corporation (DICGC) lists mutual funds among exclusions |
| Early exit | The bank's terms apply; check the deposit's terms | Sell units at the applicable NAV; an exit load may apply |
| What drives surprises | The rate on offer when you renew | Interest-rate moves and the quality of what the fund holds |

The tax treatment of the two also differs, and it has changed in recent years, so check the current rule before comparing returns after tax.

## The formula

```
FD value after one year  =  principal × (1 + r/4)^4     (r fixed at opening; quarterly compounding)

Debt fund return      =  NAV at end / NAV at start  −  1     (r is known only afterwards)
```

Quarterly compounding makes the year's return a little higher than the quoted rate: a 5% rate earns about 5.1% over the year, which is why the FD return column below sits just above the rate column. Banks set their own compounding schedule, so read the terms of the deposit you are looking at.

## Worked example: ₹1,00,000 over five years

Start each year with the same ₹{% include inr.html n=d.start_value %}. The FD is a one-year SBI (State Bank of India) deposit, renewed on 1 April each year at that day's rate, interest reinvested. The funds are {{ gl.name }} and the {{ m.emergency.liquid.name }}, regular growth plans. Fund NAVs come from AMFI (the Association of Mutual Funds in India) via mfapi.in; the SBI rates are from its [published historical rate table]({{ d.fd_source.url }}). All figures are as of 31 March 2026 (the end of FY26), before tax, and shown for illustration only.

| Financial year (FY) | CPI (consumer price index) inflation, March to March (our calculation) | SBI 1-year rate on 1 April | FD return | Liquid fund return | Gilt fund return |
|---|---:|---:|---:|---:|---:|
{% for r in d.rows -%}
| {{ r.fy }} | {% assign a = r.cpi_pct %}{% include inr.html n=a %}% | {% assign a = r.sbi_1y_rate_pct %}{% include inr.html n=a %}% | {% assign a = r.fd_pct %}{% include inr.html n=a %}% | {% assign a = r.liquid_pct %}{% include inr.html n=a %}% | {% assign a = r.gilt_pct %}{% include inr.html n=a %}% |
{% endfor %}
Here is what ₹{% include inr.html n=d.start_value %} became after each year:

| FY | FD (₹) | Liquid fund (₹) | Gilt fund (₹) |
|---|---:|---:|---:|
{% for r in d.rows -%}
| {{ r.fy }} | {{ r.fd_value }} | {{ r.liquid_value }} | {{ r.gilt_value }} |
{% endfor %}
Three things show in the table, and none is a ranking:

1. The FD's return follows the rate on the day you renew. The one-year rate moved from {% assign a = d.rate_path[0].rate_pct %}{% include inr.html n=a %}% on 1 April 2020 to {% assign a = d.rate_path[1].rate_pct %}{% include inr.html n=a %}% a year later, and to {% assign a = d.rate_path[5].rate_pct %}{% include inr.html n=a %}% by 1 April 2025. A depositor who had to renew in a low-rate year earned that low rate.
2. The gilt fund's {{ last.fy }} return was {% assign a = last.gilt_pct %}{% include inr.html n=a %}%, below the FD's {% assign a = last.fd_pct %}{% include inr.html n=a %}% in the same year. It was above the FD in {{ d.gilt_above_fd | array_to_sentence_string }} and below it in {{ d.gilt_below_fd | array_to_sentence_string }}. It fell {{ gl.max_drawdown_pct | abs }}% peak to trough from {{ gl.peak_date | date: "%-d %B %Y" }} to {{ gl.trough_date | date: "%-d %B %Y" }} along the way.
3. The liquid fund's yearly return ranged from {% assign a = d.liquid_min_pct %}{% include inr.html n=a %}% to {% assign a = d.liquid_max_pct %}{% include inr.html n=a %}% and was never negative in these five years, consistent with the short-dated holdings its [rules]({% post_url 2026-11-03-liquid-and-overnight-funds %}) require, though that is not a guarantee.

Each is one instrument over five years, so these are examples of how the mechanics play out, not estimates of what an FD or a debt fund will do next.

## The insurance limit

Deposit insurance counts what you hold *per bank*. The DICGC's [guide to deposit insurance]({{ dq.source.url }}) says: "{{ dq.source.wording }}" It covers principal and interest together, and deposits across the branches of one bank are added up. Deposits in different banks are insured separately. (Read on {{ dq.source.read | date: "%-d %B %Y" }}.) The limit has applied since {{ dq.effective.date | date: "%-d %B %Y" }}, when it was raised from ₹{% include inr.html n=dq.effective.previous_limit %} ([{{ dq.effective.name }}]({{ dq.effective.url }})).

Take an illustrative total of ₹{% include inr.html n=dq.illustrative_balance %} at one bank across a savings account and FDs. The insured part is ₹{% include inr.html n=dq.insured %}; ₹{% include inr.html n=dq.uninsured %} is above the limit. The same total split evenly across two banks is ₹{% include inr.html n=dq.split_banks_each %} in each, and all of it falls under the limit. That is how the rule counts, not a suggestion about where to hold money. Mutual fund units sit outside this scheme altogether.

## Common mistakes

- **Reading an FD rate and a debt fund's past return as the same kind of number.** One is a rate fixed in advance. The other is a result known only afterwards. And an FD's rate is certain only for its term, not for the renewal after it.
- **Assuming "debt" means the price can't fall.** The gilt fund's {{ gl.max_drawdown_pct | abs }}% fall above is a debt fund doing what the mechanics say.
- **Overlooking the insurance limit.** The cover applies per depositor per bank, so a large balance in one bank isn't fully covered.
- **Comparing pre-tax with after-tax.** Put both on the same footing, using the current tax rule for each.

**Takeaway:** A fixed deposit is a bank's promise of a rate; a debt fund is a portfolio whose return is known only afterwards. They differ in what sets the return, whether the rupee amount can fall, and what insurance applies, so compare those properties before the numbers.
