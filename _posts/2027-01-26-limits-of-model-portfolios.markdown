---
layout: post
title: "What a model portfolio can't tell you"
description: "Backtested asset mixes look precise, but the period decides the ranking. Two halves of 18 years of Indian data, and what no allocation table can settle."
image: /assets/og/limits-of-model-portfolios.png
date: 2027-01-26 09:00:00 +0530
series: money-before-markets
---

{% assign m = site.data.mbm2 %}
{% assign ds = m.dataset %}
{% assign l1 = m.limits.first %}
{% assign l2 = m.limits.second %}
{% assign ac = m.asset_classes %}

## The problem with a neat table

The last few posts in [Money Before Markets]({{ '/series/money-before-markets/' | relative_url }})
built tables: what each [asset class]({% post_url 2027-01-21-asset-classes %})
did, how often it lost money over each
[horizon]({% post_url 2027-01-22-investment-horizon %}), how seven
[asset allocations]({% post_url 2027-01-23-asset-allocation %}) fared and how
a [glide path]({% post_url 2027-01-25-glide-path %}) compared with a fixed
mix. A **model portfolio** is a table like that turned into a
recommendation: "this mix returned X% with a worst fall of Y%".

The numbers in those posts are arithmetic on real data, and they reproduce.
What they can't do is say what the next {{ ds.fy_count }} years will look
like. This post shows how much the answer depends on the dates chosen, and
lists what no backtest settles.

## Worked example: the same data, split in two

Split the {{ ds.fy_count }} financial years into two halves of
{{ l1.years }} years each and compute each asset's CAGR (compound annual
growth rate) separately. Same four series as before: the Nifty 50 TRI (Total
Returns Index, dividends reinvested) and three UTI funds' NAVs (net asset
values) from AMFI, the Association of Mutual Funds in India. Past data to
{{ ds.end_month }}, pre-tax, for illustration only.

| CAGR | {{ l1.label }} | {{ l2.label }} |
|---|---:|---:|
| Equity (Nifty 50 TRI) | {{ l1.equity }}% | {{ l2.equity }}% |
| Government bonds (UTI Gilt Fund) | {{ l1.gilt }}% | {{ l2.gilt }}% |
| Cash-like (UTI Liquid Fund) | {{ l1.liquid }}% | {{ l2.liquid }}% |
| Gold (UTI Gold ETF) | {{ l1.gold }}% | {{ l2.gold }}% |
| 60/40 equity and bonds, reset yearly | {{ l1.mix60 }}% | {{ l2.mix60 }}% |
| Ranking, highest first | {{ l1.rank | join: ", " }} | {{ l2.rank | join: ", " }} |
| Correlation of yearly returns, equity and bonds | {{ l1.corr_equity_gilt }} | {{ l2.corr_equity_gilt }} |
| Correlation of yearly returns, equity and gold | {{ l1.corr_equity_gold }} | {{ l2.corr_equity_gold }} |

What it shows:

1. **The ranking changed.** In {{ l1.label }}, {{ l1.rank[0] | downcase }}
   came first; in {{ l2.label }}, {{ l2.rank[0] | downcase }} did. Someone
   who built a model portfolio at the end of the first half, from that
   half's numbers, would have been looking at a different order of winners
   from the one that followed.
2. **The mix was steadier than its parts.** The 60/40 mix's CAGR was
   {{ l1.mix60 }}% in the first half and {{ l2.mix60 }}% in the second,
   while equity and bonds each moved by more. That's one period's result,
   not a rule, but it's the kind of thing a mix is for.
3. **Correlations shifted too.** Equity and gold's yearly correlation was
   {{ l1.corr_equity_gold }} in one half and {{ l2.corr_equity_gold }} in the
   other. With {{ l1.years }} yearly points each, these are rough
   descriptions, not stable constants; the
   [correlation post]({% post_url 2026-10-12-diversification-is-a-correlation-problem %})
   explains why a correlation estimate needs plenty of data.

## What no allocation table can settle

1. **The future period.** Every table here is one stretch of Indian history.
   The next stretch will have its own order of returns, its own interest-rate
   path and its own crises.
2. **Your behaviour in the bad year.** A table says a mix fell
   {{ m.allocation.rows.m60_40.max_dd_pct }}% and recovered. It can't say
   whether the person holding it stayed put. A mix abandoned at the bottom
   doesn't deliver the table's return; the
   [behavioural biases post]({% post_url 2026-10-14-behavioural-biases-indian-edition %})
   covers why that's common.
3. **Tax and costs.** These backtests ignore tax and, for the index, fund
   costs. Rebalancing in real life can trigger tax, so its benefit is
   smaller than shown.
4. **Which funds survive.** The three funds used here are still running,
   which is why their histories are long. Funds that closed don't appear in
   anyone's backtest; the
   [survivorship bias post]({% post_url 2026-11-01-survivorship-bias-in-fund-tables %})
   shows how that flatters tables.
5. **Your own situation.** Income stability, other assets, dependants,
   when each goal falls due: none of this is in the data, and it shapes what
   any household can actually hold.

## Common mistakes

1. **Treating a backtest's precision as accuracy.** A CAGR to one decimal
   place is exact arithmetic on the past, not a measure of how sure anyone is
   about the future.
2. **Picking the mix that won the last period.** The first table here shows
   how fast the winners changed between halves. Choosing by the most recent
   leader is a bet that the order repeats.
3. **Testing only the period that's easy to download.** A longer or
   different window can change the answer. If a claim only holds for one
   start date, the [rolling returns post]({% post_url 2026-09-27-rolling-returns %})
   shows how to test it across many.

**Takeaway:** A model portfolio is the past arranged neatly, and the
neatness hides how much the dates decide. Use backtests to understand how a
mix behaves in falls and recoveries, not to predict its return, and expect
the next period to rank things differently.
