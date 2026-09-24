---
layout: post
title: "Free float and promoter holding: the part of a company that actually trades"
description: "Free float is the share of a company available to ordinary investors, outside promoters' hands. Why index weights use it, worked on Britannia and Desi Bites."
image: /assets/og/free-float-and-promoter-holding.png
date: 2026-10-18 09:00:00 +0530
series: jargon
term: "Free float"
---

{% assign ff = site.data.jargon_m7.free_float %}
{% assign d = ff.desi %}
{% assign b = ff.britannia %}
{% assign d_ff_cr = d.ff_mcap_lakh | divided_by: 100.0 %}
{% assign d_full_cr = d.full_mcap_lakh | divided_by: 100.0 %}
{% assign b_full = b.full_mcap_cr | round: 0 %}
{% assign b_ff = b.ff_mcap_cr | round: 0 %}

## What free float means

A listed company's shares aren't all equally "on the market". A big block
usually sits with the **promoters** — the founders or parent group who
control the company and are named as such in its filings. Other blocks may
be held by the government in a strategic role, a foreign parent, or an
employee trust. None of those holders is likely to sell on an ordinary day.

**Free float** is what's left: the shares realistically available to
ordinary investors. **Free-float market cap** is the
[market cap]({% post_url 2026-09-27-market-cap %}) of just that part.

Every listed company files its **shareholding pattern** with the exchanges
each quarter, splitting holders into "promoter and promoter group" and
"public". That filing is where both numbers start (the
[promoter holding post]({% post_url 2026-10-06-contingent-liabilities-pledges-and-promoter-holding %})
covers what else to read in it, pledges included).

Why it matters: index providers weight stocks by free-float market cap. NSE
Indices determines each company's **investible weight factor (IWF)** from
the shareholding in that quarterly pattern, excluding a long list of
holdings unlikely to trade — promoter-group holdings,
strategic stakes by corporate bodies, government holdings, foreign direct
investment, employee-benefit trusts, locked-in shares and more
([NSE Indices, Methodology Document for Equity Indices, September 2026](https://www.niftyindices.com/Methodology/Method_NIFTY_Equity_Indices.pdf)).
The Nifty 50 has been weighted this way since 26 June 2009 (same document).

## The formula

```
Free float (%)          = Shares not held by promoters or other locked-up holders
                          ÷ Total shares × 100
Free-float market cap   = Full market cap × Free float (%)
                        = Full market cap × IWF          (index providers' version)

Index weight of a stock = Its free-float market cap ÷ Sum of all constituents' free-float market caps
```

The simple version here uses "not promoter" as free float. NSE's IWF
excludes more, so an index's free float for a company is usually a little
lower than 100% minus promoter holding.

## Worked example: Britannia

At 31 March 2025, Britannia's promoter and promoter group — the Wadia group
entities — held {% include inr.html n=b.promoter_shares %} of its {% include inr.html n=b.total_shares %}
shares ([Annual Report 2024-25](https://media.britannia.co.in/B_Il_Annual_Report_for_FY_2024_25_b6d95d1717.pdf),
standalone financial statements, note on shareholding of promoters). Price is
the {{ b.price_date }} NSE close; for illustration only.

| | |
|---|---:|
| Promoter and promoter group | {{ b.promoter_pct }}% |
| Everyone else (simple free float) | {{ b.non_promoter_pct }}% |
| Full market cap at ₹{% include inr.html n=b.price %} | ₹{% include inr.html n=b_full %} crore |
| **Free-float market cap (simple)** | **₹{% include inr.html n=b_ff %} crore** |

Roughly half of Britannia's market value never really trades. In an index
weighted by full market cap it would count at twice the weight its tradable
shares justify.

## Worked example: Desi Bites

Desi Bites' [fictional](/case-study/) shareholding pattern, as of
{{ d.as_of | split: " (" | first }}, at the ₹{{ d.price }} listing price:

| | Shares (lakh) | % |
|---|---:|---:|
| Promoters | {{ d.promoter_lakh }} | {{ d.promoter_pct }}% |
| Public | {{ d.public_lakh }} | {{ d.public_pct }}% |
| **Total** | **{{ d.shares_lakh }}** | **100%** |
| Full market cap | ₹{% include inr.html n=d_full_cr %} crore | |
| **Free-float market cap** | **₹{% include inr.html n=d_ff_cr %} crore** | |

Only a fifth of Desi Bites is in public hands. That's thin: a small float is
one reason a small company's price can swing on little volume.

It is also, in the real world, too thin. Indian rules require every listed
company to keep **public shareholding of at least 25%**, and to restore it
within 12 months if it falls below
(Securities Contracts (Regulation) Rules, 1957, Rule 19A, [as amended to
13 March 2026](https://www.sebi.gov.in/legal/rules/mar-2026/securities-contracts-regulation-rules-1957-last-amended-on-march-13-2026-_100665.html)).
A company of Desi Bites' size would also have had to offer at least 25% in
its IPO (Rule 19(2)(b)). Our case study simplifies this: a real Desi Bites
would need to find another {% include inr.html n=d.mps_shortfall_shares %} shares for the public, typically by
promoters selling some — one of the routes the OFS post later in this module
describes. Very large companies get longer to reach 25%; the 13 March 2026
amendment set new, staggered timelines by size.

## Why weights use free float

Two made-up companies, identical full market caps:

| | Full market cap | Free float | Free-float market cap | Weight (full) | **Weight (free float)** |
|---|---:|---:|---:|---:|---:|{% for t in ff.twins %}
| {{ t.company }} | {% include inr.html n=t.full_mcap %} | {{ t.free_float_pct }}% | {{ t.ff_mcap }} | {{ t.weight_full_pct }}% | **{{ t.weight_ff_pct }}%** |{% endfor %}

An index fund tracking a full-cap index would have to buy equal amounts of
both — but Q only has 30% of its shares available, so the fund's buying
would push Q's price around far more. Weighting by free float makes an
index something funds can actually replicate, and it's why the Nifty 50
also requires constituents to be liquid: an average impact cost of 0.50% or
less on a ₹10 crore basket for 90% of observations (NSE Indices
methodology; impact cost is explained in the
[bid-ask spread post]({% post_url 2026-10-14-bid-ask-spread-and-liquidity %})).

## Common mistakes

- **Treating a high promoter holding as automatically good or bad.** High
  promoter holding can mean skin in the game; it also means a small float
  and less say for minority shareholders. The *trend* (and any pledges) says
  more than the level.
- **Using full market cap to judge how big a stock is in an index.** A
  company with a large full market cap and a small float can carry a modest
  index weight. Index weights, and so index-fund buying, follow free float.
- **Mixing the two in size labels.** SEBI's large/mid/small-cap buckets rank
  companies by *full* market cap; index weights use *free-float* market cap.
  A stock can be "large cap" and still a small index weight.
- **Assuming "public" means "retail".** The public category includes mutual
  funds, insurers and foreign portfolio investors, who may hold large,
  rarely traded blocks. Free float is an estimate of what *could* trade, not
  what does.

**Takeaway:** free float is the part of a company's shares outside promoters'
and other locked-up hands — the part that actually trades. Index weights are
built on it, which is why a company with half its shares held by promoters
counts for about half its market cap in the Nifty.
