---
layout: post
title: "Growth vs IDCW: what a payout does to NAV"
description: "An IDCW payout lowers a fund's NAV by the amount paid, and can come from your own capital. SEBI's rules, a worked example, and a ten-year pre-tax test."
image: /assets/og/growth-vs-idcw.png
date: 2026-11-05 09:00:00 +0530
series: mutual-funds
term: "IDCW (growth vs payout)"
---

{% assign m = site.data.mf4 %}
{% assign d = m.idcw %}
{% assign e = d.example %}
{% assign t = d.ten_year %}
{% assign etf = d.etf_observed %}
{% assign reg = m.regulation %}
{% assign mc = reg.master_circular %}
{% assign etf_b = etf.nav_before | round: 2 %}
{% assign etf_a = etf.nav_after | round: 2 %}

## What IDCW means

IDCW stands for **income distribution cum capital withdrawal**. It's the name a mutual fund gives to the option that pays you money out of the scheme from time to time. The name used to be "dividend", and the new one is more honest: the payout can be income, and it can also be your own money coming back.

A fund usually offers two kinds of option. In the **growth option**, nothing is paid out and all gains stay in the NAV (net asset value, the fund's price per unit; the [mutual fund basics post]({% post_url 2026-09-25-what-a-mutual-fund-is %}) covers it). In an **IDCW option**, the trustees decide from time to time to pay out part of the fund's value, and the NAV falls by what was paid. This post is part of [Mutual Funds, Minus the Marketing]({{ '/series/mutual-funds/' | relative_url }}). How each option is taxed is a separate question for the tax series. This post is pre-tax on purpose.

## What the rules say

The [Master Circular for Mutual Funds]({{ mc.url }}) from SEBI (the Securities and Exchange Board of India), dated {{ mc.date | date: "%-d %B %Y" }} (number {{ mc.number }}), sets the main points in chapter 12.

- **Names (12.1).** The options are called "Payout of Income Distribution cum capital withdrawal option", "Reinvestment of Income Distribution cum capital withdrawal option" and "Transfer of Income Distribution cum capital withdrawal plan".
- **Capital (12.2, 12.3).** Offer documents must say that amounts can be distributed out of investors' capital (the *equalisation reserve*, which the circular describes as the part of the sale price that represents realised gains), and the account statement must separate income distribution (NAV appreciation) from capital distribution.
- **Not assured (12.5.1(a)).** The trustees decide the amount and the [record date]({% post_url 2026-10-17-record-date-and-ex-date %}), and the payout is made "subject to availability of distributable surplus".
- **NAV falls (12.5.1(b), (e), for unlisted schemes).** The NAV is adjusted at close of business on the record date, and the notice must state that the NAV will fall by the payout and statutory levy. Paragraph 12.5.2 relaxes the notice for schemes that pay up to monthly. Advertisements of payouts must say the same (14.1.3).
- **Timing (12.4).** Payment is due within {{ reg.idcw_payment.days }} working days of the record date.

These are the rules as of 20 March 2026. Check the current text before relying on any detail.

## Worked example: one payout

This example is made up for illustration. A fund's NAV is ₹{{ e.nav_before }}, and you hold {% include inr.html n=e.units %} units, so your holding is worth ₹{% include inr.html n=e.value_before %}. The trustees declare an IDCW of ₹{{ e.idcw }} per unit.

| | Before the record date | After the payout |
|---|---:|---:|
| NAV per unit | ₹{{ e.nav_before }} | ₹{{ e.nav_after }} |
| Units held | {{ e.units }} | {{ e.units }} |
| Value in the fund | ₹{{ e.value_before }} | ₹{{ e.value_after_nav }} |
| Cash received | | ₹{{ e.cash_received }} |
| **Total** | **₹{{ e.value_before }}** | **₹{{ e.value_after_nav | plus: e.cash_received }}** |

Nothing was created. The payout moved ₹{% include inr.html n=e.cash_received %} from the fund to you, and the NAV fell to match. If you chose the *reinvestment* option, that cash would buy {{ e.reinvest_new_units }} new units at ₹{{ e.nav_after }}, giving {% include inr.html n=e.reinvest_total_units %} units worth ₹{% include inr.html n=e.reinvest_value %}: the same value as before the payout.

Now suppose someone bought {% include inr.html n=e.units %} units at ₹{{ e.nav_before }} the day before the record date. They'd get the same ₹{% include inr.html n=e.cash_received %} and see the same ₹{{ e.nav_after }} NAV. They earned nothing, and part of their own money came back to them labelled as a distribution. That's the "capital withdrawal" in the name.

### A likely payout, in an ETF

An exchange-traded fund (**ETF**) isn't a growth plan, and appears to show the same mechanics. On {{ etf.ex_date | date: "%-d %B %Y" }}, the UTI (Unit Trust of India) Nifty 50 ETF's NAV fell from ₹{% include inr.html n=etf_b %} to ₹{% include inr.html n=etf_a %}, which was {{ etf.nav_gap_vs_index_pct | abs }} percentage points behind the Nifty 50's move that day. We estimate the payout at about ₹{{ etf.estimated_payout_per_unit }} per unit. That figure is our estimate from the gap, not an amount read from the fund's notice. It's the same series used in the [index funds vs ETFs post]({% post_url 2026-10-13-index-funds-vs-etfs %}).

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

You have an apple tree. Every year it grows more apples.

If you leave all the apples on the tree, the tree gets bigger. That's the growth option.

If you pick some apples each year and put them in a basket, the tree has fewer apples on it, but you have a basket. That's an IDCW payout. The total apples you own are the same. Plant the picked apples' seeds back, and you've reinvested. Keep them in the basket, and they stop growing.

</details>

## Ten years, pre-tax

This is a simple model, not market data. A fund starts at a NAV of ₹{{ e.nav_before }}, and you put in ₹{% include inr.html n=t.start_amount %}. Before any payout, the fund grows {{ t.gross_return_pct }}% a year. The IDCW option pays {{ t.idcw_pct_of_opening_nav }}% of the opening NAV at each year end. Taxes and costs are left out so that only the payout design shows.

| Year | Growth plan NAV | IDCW NAV | Payouts received so far (₹) | IDCW with reinvestment (₹) |
|---:|---:|---:|---:|---:|
{% for y in t.years -%}
| {{ y.year }} | {{ y.growth_nav }} | {{ y.payout_nav }} | {{ y.payout_cum }} | {{ y.reinvest_value }} |
{% endfor %}

After {{ t.years.size }} years:

| | Value (₹) |
|---|---:|
| Growth option | {{ t.growth_value }} |
| IDCW, payouts kept as cash: NAV value | {{ t.payout_nav_value }} |
| IDCW, payouts kept as cash: payouts received | {{ t.payout_cash_cumulative }} |
| **IDCW, payouts kept as cash: total** | **{{ t.payout_total }}** |
| IDCW, payouts reinvested | {{ t.reinvest_value }} |

Reinvesting every payout gives exactly the growth option's value, before tax. Keeping the payouts as cash gives less, because the cash stops compounding: ₹{% include inr.html n=t.growth_value %} against ₹{% include inr.html n=t.payout_total %}, before counting what you might earn on the cash elsewhere. The model says nothing about which is better for anyone. It only shows where the difference comes from. Taking cash out of a fund on a schedule you choose yourself is a different tool, covered in the post on [systematic transfer and withdrawal plans]({% post_url 2026-10-17-stp-and-swp %}).

### In Python

```python
units, nav0, growth, idcw_pct = 1000, 100.0, 0.10, 0.03

g_nav = p_nav = r_nav = nav0           # growth plan, IDCW payout, IDCW reinvest
r_units, cash = units, 0.0
for year in range(10):
    g_nav *= 1 + growth
    p_before = p_nav * (1 + growth)
    p_pay = idcw_pct * p_nav            # paid at year end: 3% of the opening NAV
    p_nav = p_before - p_pay
    cash += p_pay * units
    r_before = r_nav * (1 + growth)
    r_pay = idcw_pct * r_nav
    r_nav = r_before - r_pay
    r_units += r_units * r_pay / r_nav  # payout buys more units at the ex-payout NAV

print(f"growth    {units * g_nav:,.0f}")
print(f"payout    {units * p_nav:,.0f} in NAV + {cash:,.0f} received = {units * p_nav + cash:,.0f}")
print(f"reinvest  {r_units * r_nav:,.0f}")
```

## Common mistakes

- **Treating IDCW as a yield or a salary.** The payout depends on a trustee decision and on distributable surplus. It isn't promised, and part of it can be your own capital coming back, which is why the account statement has to separate income from capital distribution.
- **Reading the NAV drop as a loss.** After a payout the NAV falls by what was paid, and the cash is in your hands. Judge the total, as in the first table.
- **Comparing the NAV of the growth and IDCW options of one fund.** The IDCW option's NAV is lower because of past payouts. Compare total returns with payouts included, not NAVs.
- **Forgetting the tax, which this post leaves out.** How each option is taxed is a separate question, and it can change the comparison. Check the current rules or ask a tax professional.

**Takeaway:** An IDCW payout lowers a fund's NAV by the amount paid, and part of it can be your own capital coming back. Compare options by total value, with payouts included, never by NAV alone.
