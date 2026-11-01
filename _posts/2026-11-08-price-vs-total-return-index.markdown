---
layout: post
title: "Price index vs total-return index: why the same index has two returns"
seo_title: "Price vs total return index (Nifty 50 TRI) explained"
description: "The Nifty 50 price index ignores dividends; the total-return index reinvests them. The gap over 1, 5 and 10 years, and why funds compare to the TRI."
image: /assets/og/price-vs-total-return-index.png
date: 2026-11-08 09:00:00 +0530
series: jargon
term: "Total-return index (TRI)"
---

{% assign tr = site.data.jargon_m8.price_vs_tr %}
{% assign il = tr.illustration %}

## What a total-return index means

The headline level of the Nifty 50 that you see in the news is a **price index**. It moves only with the prices of the 50 stocks. It ignores the dividends those companies pay.

A **total-return index (TRI)** tracks the same 50 stocks with the same weights, but it also assumes the dividends are reinvested in the index. NSE Indices, the index arm of the National Stock Exchange of India (NSE), describes its total-return version as one that "assumes dividends are reinvested in the index after the close on the ex-date" ([Methodology Document for Equity Indices](https://www.niftyindices.com/Methodology/Method_NIFTY_Equity_Indices.pdf), September 2026 edition).

So the two series cover the same stocks and differ only by dividends. Over a short window the gap is small. Over many years it compounds. This is a [Jargon, Decoded]({{ '/series/jargon/' | relative_url }}) post; the related ideas are in the [dividend yield post]({% post_url 2026-09-28-dividend-yield %}) and the [tracking error vs tracking difference post]({% post_url 2026-10-04-tracking-error-and-tracking-difference %}).

## The formula

NSE Indices gives the daily calculation:

```
PR = price-return index;  TR = total-return index

TR index (today) = TR index (previous day) × [ 1 + ( (PR index today + indexed dividend)
                                                      ÷ PR index previous day  − 1 ) ]

Indexed dividend = dividend payout ÷ base market capitalisation of the index

Price return     = PR index today ÷ PR index previous day − 1
```

Dividends that are unusually large (the document treats a dividend of {{ tr.special_dividend_pct }}% or more of the share price at announcement as a "special dividend") are adjusted in the price index and left out of the total-return index, so the two series are not simply "price plus every rupee paid".

An invented one-day illustration: the price index goes from {% include inr.html n=il.prev_pr %} to {% include inr.html n=il.today_pr %} ({{ il.pr_ret_pct }}%), and that day's dividends amount to {{ il.div_pts }} index points. A TR index that stood at {% include inr.html n=il.prev_tr %} becomes {% include inr.html n=il.today_tr %} ({{ il.tr_ret_pct }}%).

## Worked example: Nifty 50, price index vs TRI

Both series run to {{ tr.data_end | date: "%-d %B %Y" }}. The price index is Yahoo Finance's daily close of the Nifty 50 (^NSEI); the TRI is from NSE Indices' [historical data](https://niftyindices.com/reports/historical-data). Data to March 2026, so this is historical and for illustration only. Each window starts on the last trading day on or before the same calendar date in the earlier year.

| Window | Start | Price index total | TRI total | Price index CAGR (compound annual rate) | TRI CAGR | Gap |
|---|---|---:|---:|---:|---:|---:|
{% for r in tr.rows -%}
| {{ r.label }} | {{ r.start | date: "%-d %b %Y" }} | {% if r.pr_total_pct < 0 %}−{% assign v = r.pr_total_pct | times: -1 %}{{ v }}{% else %}+{{ r.pr_total_pct }}{% endif %}% | {% if r.tr_total_pct < 0 %}−{% assign v = r.tr_total_pct | times: -1 %}{{ v }}{% else %}+{{ r.tr_total_pct }}{% endif %}% | {% if r.pr_cagr_pct < 0 %}−{% assign v = r.pr_cagr_pct | times: -1 %}{{ v }}{% else %}{{ r.pr_cagr_pct }}{% endif %}% | {% if r.tr_cagr_pct < 0 %}−{% assign v = r.tr_cagr_pct | times: -1 %}{{ v }}{% else %}{{ r.tr_cagr_pct }}{% endif %}% | {{ r.gap_pp }} pts |
{% endfor %}
CAGR is the compound annual growth rate: the steady yearly rate that would take the starting level to the ending level over the window. The table is historical, for illustration only.

Put in rupees, ₹1,00,000 invested at the start of the longest window ({{ tr.rows[2].label }}) would have grown to ₹{% include inr.html n=tr.rows[2].pr_100k %} on the price index and ₹{% include inr.html n=tr.rows[2].tr_100k %} on the TRI. The ₹{% assign diff = tr.rows[2].tr_100k | minus: tr.rows[2].pr_100k %}{% include inr.html n=diff %} difference is the reinvested dividends. In the one-year window both series fell, and the TRI fell a little less, because the dividends partly offset the price loss.

These are index figures. They are not what an investor would have received: nobody earns an index return, and the TRI assumes dividends are reinvested in full with no tax or cost.

## Why funds compare to the TRI

A mutual fund that holds the shares receives the dividends. Comparing it with the price index would credit the index with less than the fund could have earned from the same stocks. Fund benchmarks are the total-return version (the [tracking error vs tracking difference post]({% post_url 2026-10-04-tracking-error-and-tracking-difference %}) shows cites the SEBI requirement and shows what happens when an index fund is measured against the wrong one), and the [benchmarks post]({% post_url 2026-10-02-benchmarks-and-comparing-like-with-like %}) covers the like-with-like rule more widely.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Say you have an orchard. The **price index** only tracks how much each tree is *worth*. The **total-return index** also counts the fruit the trees drop each year, and imagines you planted the seeds from that fruit to grow more trees. After a few years, the second way of counting shows a bigger orchard. Same trees, same weather; the second way just remembers the fruit.

</details>

## Common mistakes

- **Comparing a fund's return with the price index.** The fund earns dividends and the price index leaves them out, so the comparison understates the benchmark. Compare with the TRI (and say which one you used).
- **Thinking the TRI is a different set of stocks.** It holds the same stocks in the same weights. The only difference is the dividends.
- **Ignoring that the gap compounds.** The yearly gap looks small, but over ten years in the table above it is a difference of ₹{% include inr.html n=diff %} on ₹1,00,000.
- **Treating the TRI as what you would have earned.** It assumes full reinvestment with no taxes or costs. NSE Indices also publishes a net total-return (NTR) version that deducts withholding tax on dividends (it states that NTR is computed for the Nifty 50, Nifty Midcap 50 and Nifty 500), so even "total return" has more than one flavour.

**Takeaway:** The price index and the total-return index cover the same stocks; the TRI adds reinvested dividends. Over ten years of Nifty 50 history in our data the TRI ended ahead of the price index by more than one percentage point a year, which is why funds are compared with the TRI.
