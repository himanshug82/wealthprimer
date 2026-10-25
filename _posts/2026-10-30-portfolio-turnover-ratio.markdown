---
layout: post
title: "Portfolio turnover ratio: how busy is a fund?"
description: "Portfolio turnover shows how much of its size a fund trades in a year. SEBI's formula, what trading costs, and why a high ratio is a strategy, not a verdict."
image: /assets/og/portfolio-turnover-ratio.png
date: 2026-10-30 09:00:00 +0530
series: mutual-funds
term: "Portfolio turnover ratio"
---

{% assign m = site.data.mf4 %}
{% assign t = m.turnover %}
{% assign b = t.cases.base %}
{% assign a = b.fund_a %}
{% assign f = b.fund_b %}
{% assign lo = t.cases.low %}
{% assign hi = t.cases.high %}
{% assign reg = m.regulation %}
{% assign mc = reg.master_circular %}
{% assign a_cost = a.purchases_cr | plus: a.sales_cr | times: b.impact_per_side_pct | divided_by: t.avg_aum_cr | round: 3 %}
{% assign gap_a = t.value_ignoring_impact | minus: a.ten_year_value %}
{% assign gap_f = t.value_ignoring_impact | minus: f.ten_year_value %}
{% assign net_nocost = t.gross_return_pct | minus: t.ter_pct %}
{% assign f_cost = f.purchases_cr | plus: f.sales_cr | times: b.impact_per_side_pct | divided_by: t.avg_aum_cr | round: 3 %}

## What portfolio turnover means

The portfolio turnover ratio shows how much of its own size a fund bought or sold over a year. A fund that holds its stocks for years scores low. A fund that moves in and out all the time scores high.

You'll find it in a fund's key statistics (the financial highlights) and on its factsheet, and the [factsheet post]({% post_url 2026-10-11-reading-a-factsheet %}) shows where. It matters because trading isn't free. Every purchase and sale has a cost, and that cost comes out of the NAV (net asset value, the fund's price per unit) that you own a slice of. This post is part of [Mutual Funds, Minus the Marketing]({{ '/series/mutual-funds/' | relative_url }}).

## The formula

SEBI (the Securities and Exchange Board of India) defines it this way in its reporting format, where AUM is assets under management, the fund's total size ([Master Circular for Mutual Funds]({{ mc.url }}), {{ mc.date | date: "%-d %B %Y" }}, number {{ mc.number }}, Key Statistics table in the formats annex, footnote 3):

```
Portfolio turnover = lower of (total sales, total purchases)
                     ÷ average AUM for the year × 100
```

The [AUM post]({% post_url 2026-10-08-aum %}) covers how AUM is measured. The idea behind using the *lower* of purchases and sales is to strip out trading that was only a response to money coming in or going out. If investors add money, the fund buys more than it sells, and the sales side shows the churn that was a choice.

A ratio of 100% means the fund sold, and bought, roughly its whole size in a year. It can also exceed 100%.

## What a trade costs

Three costs sit behind each trade, and the rules put them in different places. The **TER** is the total expense ratio, the yearly running cost a fund discloses as a percentage of its assets.

| Cost | What it is | Where it shows |
|---|---|---|
| Brokerage | What the broker charges | Inside the TER |
| Transaction charges | Other costs of executing the trade | Inside the TER |
| Market impact | Buying pushes the price up and selling pushes it down, so you pay a little worse than the screen price | Not itemised as an expense; it's in the price the fund got |

The TER formula in the same Master Circular, paragraph 11.2.4(a), is "Base Expense Ratio (BER) + Brokerage Cost + Transaction Cost incurred for the purpose of execution of trade + Statutory levies (including GST)", where **GST** is the goods and services tax. So the explicit charges are already in the expense ratio covered in the [expense ratio post]({% post_url 2026-09-28-expense-ratios-direct-vs-regular %}). What's left out is the third row. The [bid-ask spread post]({% post_url 2026-10-14-bid-ask-spread-and-liquidity %}) explains impact cost: it's bigger for stocks that trade thinly and bigger for large orders.

## Worked example: two funds, same size

These two are made up. They are not real funds, and the numbers are illustrative inputs, not market data.

Both have an average AUM of ₹{% include inr.html n=t.avg_aum_cr %} crore, earn the same {{ t.gross_return_pct }}% a year before costs, and have a TER of {{ t.ter_pct }}%. Only their trading differs. Market impact is assumed to be {{ b.impact_per_side_pct }}% of the traded value on each purchase and each sale. Real impact varies with the stock and the order size.

| | Fund A | Fund B |
|---|---:|---:|
| Purchases in the year (₹ crore) | {{ a.purchases_cr }} | {{ f.purchases_cr }} |
| Sales in the year (₹ crore) | {{ a.sales_cr }} | {{ f.sales_cr }} |
| Lower of the two | {{ a.sales_cr }} | {{ f.sales_cr }} |
| **Turnover** = lower ÷ ₹{% include inr.html n=t.avg_aum_cr %} crore | **{{ a.turnover_pct }}%** | **{{ f.turnover_pct }}%** |
| Market-impact drag = (purchases + sales) × {{ b.impact_per_side_pct }}% ÷ ₹{% include inr.html n=t.avg_aum_cr %} crore | {{ a_cost }}% | {{ f_cost }}% |
| Net return = {{ t.gross_return_pct }}% − {{ t.ter_pct }}% TER − drag | {{ a.net_return_pct }}% | {{ f.net_return_pct }}% |
| ₹1,00,000 after {{ t.years }} years at that rate | ₹{{ a.ten_year_value }} | ₹{{ f.ten_year_value }} |

With no impact drag at all, ₹1,00,000 would grow to ₹{% include inr.html n=t.value_ignoring_impact %} on a net {{ net_nocost }}%. Fund B gives up ₹{% include inr.html n=gap_f %} of that and Fund A gives up ₹{% include inr.html n=gap_a %}.

The gap rests on the impact assumption. At {{ lo.impact_per_side_pct }}% a side, Fund B's ₹1,00,000 reaches ₹{% include inr.html n=lo.fund_b.ten_year_value %}; at {{ hi.impact_per_side_pct }}% it reaches ₹{% include inr.html n=hi.fund_b.ten_year_value %}. Fund A moves from ₹{% include inr.html n=lo.fund_a.ten_year_value %} to ₹{% include inr.html n=hi.fund_a.ten_year_value %} over the same range. The direction never changes, but the size does.

Nothing here says Fund B is a worse fund. It might earn that extra return back by trading well, or it might not. Turnover tells you what is being spent. It doesn't tell you what the spending bought.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Two shopkeepers run the same size shop. One keeps the same stock for months. The other swaps half the shelves every week.

Every swap costs a little: a delivery fee, and a worse price because the wholesaler knows you need the goods. Swapping a lot isn't wrong if the new goods sell better. But the fees are paid either way, so the swapping has to earn them back.

Portfolio turnover is a count of how many swaps the shopkeeper made.

</details>

## What else SEBI asks the fund to say

The scheme's offer document also has to say something about the policy: for equity-oriented schemes, it must describe the portfolio turnover policy and, where significant, the probable effect of the strategy on turnover, including higher brokerage and transaction costs (Master Circular, scheme information document format). Look for that paragraph.

## Common mistakes

- **Treating high turnover as bad and low as good, or comparing it across categories.** It's a strategy. An index fund trades mostly when its index changes or when money flows in and out, so it scores low by design. A fund that opens and closes positions every month, like the mechanism in the [arbitrage fund post]({% post_url 2026-10-19-arbitrage-funds %}), can score high by design. Compare within a category.
- **Assuming a single year is typical.** A big inflow or a manager change can push a year's figure up. Look at several years, and read it with the [manager change post]({% post_url 2026-10-23-manager-changes-and-style-drift %}) in mind.
- **Using the same words for different things.** The Master Circular also uses "portfolio turnover ratio" in paragraph 6.7.3, for how much a *distributor's* client money is churned (AMCs must do extra due diligence on a distributor above twice the industry average). That isn't a fund's ratio.
- **Counting only what's itemised.** The brokerage is in the TER. The price impact isn't itemised, which is why it gets missed.

**Takeaway:** Portfolio turnover shows how much of its size a fund trades in a year, and trading has costs that only partly show up in the expense ratio. A high ratio is a strategy to understand, not a verdict, so compare it within a category.
