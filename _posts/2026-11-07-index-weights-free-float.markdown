---
layout: post
title: "How an index weights its stocks"
seo_title: "How a stock index is weighted: free-float method"
description: "An index isn't an average of prices: each stock counts by weight. Equal, full market cap and free-float weighting, worked on a five-stock index."
image: /assets/og/index-weights-free-float.png
date: 2026-11-07 09:00:00 +0530
series: jargon
term: "Index weighting (free-float market cap)"
---

{% assign iw = site.data.jargon_m8.index_weights %}

## What index weighting means

A stock index, such as the Nifty 50, is a single number built from many stocks. It is not a simple average of their prices. Each stock is given a **weight**, a share of the index, and a bigger weight means that stock's price moves push the index more.

There are three common ways to set the weights:

- **Equal weight.** Every stock counts the same, whatever its size.
- **Full market-cap weight.** A stock counts in proportion to its [market cap]({% post_url 2026-09-27-market-cap %}): shares outstanding times price.
- **Free-float market-cap weight.** A stock counts in proportion to the market cap of only the shares that are realistically available to trade. The [free float post]({% post_url 2026-10-18-free-float-and-promoter-holding %}) explains what is left out and why.

NSE Indices (the index arm of the National Stock Exchange of India) builds many of its indices on the free-float method. This post shows the arithmetic on a made-up five-stock index. The idea ties to [index funds]({% post_url 2026-10-13-index-funds-vs-etfs %}) in the Mutual Funds series, which buy stocks in the index's proportions. It is part of [Jargon, Decoded]({{ '/series/jargon/' | relative_url }}).

## The formula

NSE Indices states the price-return index formula for market-cap-based indices in its [Methodology Document for Equity Indices](https://www.niftyindices.com/Methodology/Method_NIFTY_Equity_Indices.pdf) (September 2026 edition):

```
Index value  =  Index market cap  ÷  Base free-float market cap  ×  Base index value

Index market cap  =  Σ  shares outstanding × IWF × capping factor × price

  IWF (investible weight factor) = the free-float fraction of the shares
  IWF = 1 for an index built on full market cap
  Capping factor = 1 for an uncapped index
```

Some indices also cap a stock's weight at a maximum; the capping factor does that. The example below is uncapped. How often the IWF and weights are reset is set by each index's own methodology, so check the index you care about.

## Worked example: a five-stock index, invented

All five companies are made up, and so are the prices. "Shares" are in crore and market caps in ₹ crore. The base index value is set to {% include inr.html n=iw.base_value %}.

| Company | Shares (cr) | Price | IWF | Full market cap | Free-float market cap | Weight: full | Weight: free float | Weight: equal |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
{% for r in iw.rows -%}
| {{ r.name }} | {{ r.shares_cr }} | {{ r.price }} | {{ r.iwf }} | {{ r.full_mcap }} | {{ r.ff_mcap }} | {{ r.w_full }}% | {{ r.w_ff }}% | {{ r.w_equal }}% |
{% endfor %}
The five companies together have a full market cap of ₹{% include inr.html n=iw.tot_full %} crore, but only ₹{% include inr.html n=iw.tot_ff %} crore of it is free float: {{ iw.ff_share_of_full_pct }}% of the total. Charlie and Echo have the same full market cap (₹{% include inr.html n=iw.rows[2].full_mcap %} crore each), yet Charlie's free-float weight ({{ iw.rows[2].w_ff }}%) is well above Echo's ({{ iw.rows[4].w_ff }}%), because {{ iw.rows[2].iwf }} of Charlie's shares float against {{ iw.rows[4].iwf }} of Echo's.

### One day later

Now suppose prices move the next day, as below. The index is recomputed with the same IWFs.

| Company | Price before | Price after | Move | Free-float weight after |
|---|---:|---:|---:|---:|
{% for r in iw.rows -%}
| {{ r.name }} | {{ r.price }} | {{ r.price1 }} | {% if r.ret_pct < 0 %}−{% assign m = r.ret_pct | times: -1 %}{{ m }}{% else %}+{{ r.ret_pct }}{% endif %}% | {{ r.w_ff_after }}% |
{% endfor %}
The same price moves give three different "index returns", depending on how the index is weighted:

| Weighting | Index return for the day |
|---|---:|
| Free-float market cap | +{{ iw.ret_ff_pct }}% (index {{ iw.index_after_ff }}) |
| Full market cap | +{{ iw.ret_full_pct }}% (index {{ iw.index_after_full }}) |
| Equal weight | +{{ iw.ret_equal_pct }}% |

Nothing is wrong with any of these. They answer different questions: what a basket in proportion to *tradable* value earned, what a basket in proportion to *total* value earned, and what an equal-sized bet on each stock earned. Notice, too, that weights drift as prices move: Alpha's free-float weight went from {{ iw.rows[0].w_ff }}% to {{ iw.rows[0].w_ff_after }}% in one day without any change to the index rules.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Imagine a class fruit basket made of five kinds of fruit. If you decide each fruit gets the *same* number of pieces, that's equal weight. If you decide a fruit gets pieces in proportion to how much of it the class grew, that's market-cap weight. And if you only count the fruit that is actually *ripe and ready to eat* (some is still green or locked in the cupboard), that's free-float weight. The basket's overall "sweetness" changes depending on which rule you picked, even though the fruit are the same.

</details>

## Common mistakes

- **Assuming an index is an average of share prices.** A ₹5,000 share does not count more than a ₹50 share by price. Weights come from market value (or equal shares of the index), not from the price tag.
- **Mixing full and free-float market cap.** A stock can be large by full market cap and have a modest index weight because a lot of its shares are held by promoters and others. The two columns in the table above rank the same companies differently.
- **Reading a weight as a quality score.** A big weight means a big tradable market value. It says nothing about whether the company is good, cheap or safe.
- **Expecting the weights to stay put.** Between resets, weights move with prices, and the reset rules and dates differ between indices. Check the methodology document of the index you actually follow.

**Takeaway:** An index weights each stock by a rule: equal, full market cap or free-float market cap. The same price moves can give different index returns under each rule, and a bigger weight is only a bigger tradable value, not a better company.
