---
layout: post
title: "Currency risk: what the rupee does to your foreign investments"
description: "A US fund's rupee return is two returns multiplied: the asset's and the exchange rate's. Twenty years of RBI and FBIL rates show how much the second moves."
image: /assets/og/currency-risk.png
date: 2026-10-19 09:00:00 +0530
series: risk
term: "Currency risk"
---

{% assign r2 = site.data.risk2 %}
{% assign d = r2.dataset %}
{% assign cu = r2.currency %}
{% assign flat08 = cu.decomp[1] %}
{% assign w0 = cu.worst_index_fys[0] %}
{% assign w1 = cu.worst_index_fys[1] %}

## Two returns, not one

Buy a US index fund, a Nasdaq ETF (exchange-traded fund) or a few US shares
from India, and the number that lands in your rupee account is the product of
two separate returns: what the asset did in dollars, and what the dollar did
against the rupee. You chose the first. The second came free with it.

**Currency risk** is the uncertainty in your return that comes from exchange
rates moving. For an Indian investor it shows up whenever an asset or a
liability is priced in another currency: international mutual funds, US
stocks bought directly, but also a child's future fees at a foreign
university or an EMI (equated monthly instalment) on a loan in dollars.

## The formula

```
Rupee return  =  (1 + return in dollars) × (1 + change in rupees per dollar)  −  1

    ≈  return in dollars  +  change in USD/INR          (for small numbers)

Change in USD/INR  =  (rupees per dollar at the end / at the start)  −  1
    positive  →  the rupee weakened  →  good for a rupee holder of dollar assets
    negative  →  the rupee strengthened  →  bad for a rupee holder of dollar assets
```

A weaker rupee *helps* you if you own dollar assets and *hurts* you if you owe
dollars. Same rate, opposite sign, depending on which side you're on.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Your cousin in America keeps your $10 in her piggy bank. When you visit, you
swap it back into rupees.

If one dollar buys ₹80 when you visit, your $10 is ₹800. If it buys ₹90, the
same $10 is ₹900 — you're richer without the piggy bank doing anything. If it
buys ₹70, you're poorer.

So money kept in another country's currency goes up and down for two
reasons: what happens inside the piggy bank, and how many rupees one dollar is
worth on the day you swap.

</details>

## Worked example: twenty financial years of USD/INR

Rupees per US dollar at each financial-year end, from the RBI (Reserve Bank of India) reference rate
([archive]({{ d.fx_rbi_url }})) up to 9 July 2018 and the FBIL (Financial
Benchmarks India Ltd) reference rate from {{ d.fx_fbil_start | date: "%-d %B %Y" }},
when FBIL took over the benchmark ([fbil.org.in]({{ d.fx_fbil_url }});
[our CSV]({{ d.fx_csv | relative_url }})). The last column is the
{{ site.data.risk.dataset.fund_name }}'s return in the same year (regular plan,
AMFI, the Association of Mutual Funds in India, via
[mfapi.in]({{ d.fund_source_url }})). Data to
{{ cu.end_date | date: "%-d %B %Y" }}; historical, for illustration only.

![USD/INR reference rate, 2006 to 2026]({{ '/assets/charts/risk2-usdinr.svg' | relative_url }})

| Year | Date | ₹ per $ | Change in ₹ per $ | Index fund return |
|---|---|---:|---:|---:|{% for row in cu.rows %}
| {{ row.fy }} | {{ row.date }} | {{ row.usd_inr }} | {{ row.change_pct }}% | {{ row.index_fund_pct }}% |{% endfor %}

From ₹{{ cu.start_rate }} on {{ cu.start_date | date: "%-d %B %Y" }} to
₹{{ cu.end_rate }} on {{ cu.end_date | date: "%-d %B %Y" }}, the dollar rose
{{ cu.total_change_pct | round }}% against the rupee — {{ cu.cagr_pct }}% a year
compounded over {{ cu.years }} years. But not smoothly, and not every year:

- The rupee **weakened** in {{ cu.depreciation_years }} of the {{ cu.years }}
  years and **strengthened** in {{ cu.appreciation_years }}.
- Its worst year was {{ cu.biggest_fall_fy }}, when the dollar rose
  {{ cu.biggest_fall_pct }}%. Its best was {{ cu.biggest_rise_fy }}, when the
  dollar fell {{ cu.biggest_rise_pct | abs }}%.
- In {{ cu.rows.last.fy }} alone the dollar rose {{ cu.fy26_pct }}%.
- Day to day, USD/INR was far calmer than equities: annualised volatility of
  {{ cu.fx_vol_pct }}% against {{ cu.nifty_vol_pct }}% for the Nifty 50 price
  index, over the dates both are available since
  {{ cu.vol_window_start | date: "%B %Y" }}.

### Putting the two returns together

Take a hypothetical US asset that returned +10%, 0% or −10% in dollars, and
apply two real years — {{ cu.decomp[0].fy }}, when the rupee strengthened,
and {{ cu.decomp[3].fy }}, when it weakened:

| Year | Return in dollars (hypothetical) | Change in ₹ per $ (actual) | Return in rupees |
|---|---:|---:|---:|{% for row in cu.decomp %}
| {{ row.fy }} | {{ row.usd_return_pct }}% | {{ row.fx_pct }}% | **{{ row.inr_return_pct }}%** |{% endfor %}

The same +10% dollar return became {{ cu.decomp[0].inr_return_pct }}% in one
year and {{ cu.decomp[3].inr_return_pct }}% in another. A flat asset returned
{% include inr.html n=flat08.inr_return_pct %}% and {{ cu.decomp[4].inr_return_pct }}% purely from the exchange rate. For a single year, the
currency can matter as much as the investment.

### Does the rupee fall when Indian stocks fall?

The index fund fell in {{ cu.index_down_fys }} of the {{ cu.years }} years
({{ cu.index_down_fy_list }}). The rupee weakened in
**{{ cu.index_down_fys_rupee_weaker }} of those {{ cu.index_down_fys }}** —
including {{ cu.worst_index_fys[0].fy }} ({% include inr.html n=w0.index_fund_pct %}%
for the fund, dollar up {{ cu.worst_index_fys[0].fx_pct }}%) and
{{ cu.worst_index_fys[1].fy }} ({% include inr.html n=w1.index_fund_pct %}%,
dollar up {{ cu.worst_index_fys[1].fx_pct }}%). In those years a dollar asset
held by a rupee investor got a cushion exactly when the Indian one hurt.

Check the base rate before making much of it. The rupee weakened in
{{ cu.base_rate_weaker_pct | round }}% of *all* years, including
{{ cu.index_up_fys_rupee_weaker }} of the {{ cu.index_up_fys }} years the
fund rose. If each year were a coin weighted to that rate, all
{{ cu.index_down_fys }} down years would line up this way about
{{ cu.chance_all_down_by_base_rate_pct | round }}% of the time by chance.
Just {{ cu.index_down_fys }} observations suggest a pattern that has a plausible story behind it
(money leaves emerging markets in a panic); they don't prove it will hold.

## What this means for a rupee investor

Currency risk isn't only about returns. If a goal is priced in dollars — a
foreign degree, travel, a relative abroad — then holding rupee assets for it
*is* the currency bet, and holding dollar assets reduces it. Whether foreign
assets add or remove risk depends on what you'll spend the money on.

It can also be hedged: a fund can use currency forwards to lock in an
exchange rate. In textbook theory (covered interest parity) the cost of that
hedge is roughly the gap between Indian and US interest rates, so a hedged
dollar asset gives back much of the rupee's average drift. Whether a
particular international fund hedges is stated in its scheme documents;
check rather than assume.

## Common mistakes

- **Treating rupee depreciation as extra return.** Economic theory
  (purchasing power parity) links long-run currency moves to differences in
  inflation. In that view — and it's a rough guide, not a law — a weakening
  rupee is largely compensation for higher Indian inflation, not a bonus. The
  {{ cu.cagr_pct }}% a year here doesn't make dollar assets "better" — it
  makes their rupee returns look different.
- **Assuming the rupee only goes one way.** It strengthened in
  {{ cu.appreciation_years }} of {{ cu.years }} years, by as much as
  {{ cu.biggest_rise_pct | abs }}% in one. Extrapolating a
  {{ cu.years }}-year
  [CAGR]({% post_url 2026-09-26-point-to-point-returns %}) (compound annual growth rate) into next year is
  the same mistake as extrapolating any other trend.
- **Comparing a foreign fund's dollar return with an Indian fund's rupee
  return.** An international fund's rupee NAV (net asset value) already includes the currency
  move. Compare rupee with rupee.
- **Forgetting liabilities.** A dollar goal funded with rupee savings carries
  currency risk even if you never buy a foreign asset.

**Takeaway:** A foreign investment's rupee return is its own return
multiplied by the exchange rate's, and the exchange rate alone moved as much
as {{ cu.biggest_fall_pct }}% in a single year. Over two decades the rupee
mostly weakened, but not every year. Know which currency your goals are in
before deciding whether foreign assets add risk or remove it.
