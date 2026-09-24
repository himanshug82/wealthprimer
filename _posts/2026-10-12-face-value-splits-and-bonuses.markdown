---
layout: post
title: "Face value, splits and bonuses: why a ₹320 share isn't cheaper than a ₹640 one"
description: "Face value is the nominal amount on a share; splits and bonuses change the share count, not the company. A 1:1 bonus halves Desi Bites' price and EPS, not P/E."
image: /assets/og/face-value-splits-and-bonuses.png
date: 2026-10-12 09:00:00 +0530
series: jargon
term: "Face value, splits and bonuses"
---

{% assign bo = site.data.jargon_m6.bonus %}
{% assign b = bo.before %}
{% assign a1 = bo.after_1_1_bonus %}
{% assign a2 = bo.after_1_2_split %}

## What face value is

Every share has a **face value** (also called par or nominal value): the
amount printed on it, set when the shares are issued (a split changes it
later) — ₹10 is common in
India, ₹1 and ₹2 also. It is an accounting quantity: share capital on the
balance sheet is face value × number of shares, and dividends are often
declared as a percentage of it ("150% dividend" on a ₹10 face value means
₹15 a share).

It has *nothing* to do with what a share is worth. Desi Bites' shares have a
₹{{ bo.face_value }} face value and listed at ₹{% include inr.html n=b.price %}. Britannia's have a face value of
₹{{ bo.britannia_face_value }} and traded at ₹{% include inr.html n=bo.britannia_price %} on {{ site.data.real_company.market.price_date }}. The
gap between face value and price is the entire history of the business.

Face value matters here because two corporate actions change it, or change
the share count around it, and both reliably confuse people.

## Splits and bonuses

A **stock split** divides each share into several: a 1:2 split turns one ₹10
face-value share into two ₹5 face-value shares. Share count doubles, face
value halves, share capital is unchanged.

A **bonus issue** gives shareholders extra shares free: a 1:1 bonus gives one
new share for each held. Share count doubles, face value stays at ₹10, and
the company moves an amount equal to the new shares' face value from its
reserves into share capital. Total equity is unchanged; it's a reshuffle
between two lines of the same section.

Either way, *the company is exactly the same company*. Same factories, same
profit, same debt, same cash. There are just more pieces of paper representing
it, so each piece is worth proportionally less.

## The formula

```
After a split or bonus with ratio k (k = 2 for 1:1 bonus or 1:2 split):

Shares outstanding   × k
Price per share      ÷ k          (mechanically, on the ex-date)
EPS, BVPS, DPS       ÷ k
Market cap, P/E, P/B, total equity, PAT    — unchanged
```

## Worked example: Desi Bites does a 1:1 bonus

Hypothetical, using the [case study](/case-study/)'s listing figures as the
starting point:

| | Before | After 1:1 bonus | After 1:2 split |
|---|---:|---:|---:|
| Shares (lakh) | {% include inr.html n=b.shares_lakh %} | {% include inr.html n=a1.shares_lakh %} | {% include inr.html n=a2.shares_lakh %} |
| Face value | ₹{{ bo.face_value }} | ₹{{ a1.face_value }} | ₹{% include inr.html n=a2.face_value %} |
| Share capital (₹ lakh) | {% include inr.html n=b.share_capital_lakh %} | {% include inr.html n=a1.share_capital_lakh %} | {% include inr.html n=a2.share_capital_lakh %} |
| Price per share | ₹{% include inr.html n=b.price %} | ₹{% include inr.html n=a1.price %} | ₹{% include inr.html n=a2.price %} |
| **Market cap (₹ lakh)** | **{% include inr.html n=b.market_cap_lakh %}** | **{% include inr.html n=a1.market_cap_lakh %}** | **{% include inr.html n=a2.market_cap_lakh %}** |
| EPS (post-issue) | ₹{{ b.eps_diluted }} | ₹{{ a1.eps_diluted }} | ₹{{ a2.eps_diluted }} |
| Book value per share | ₹{{ b.bvps }} | ₹{{ a1.bvps }} | ₹{{ a2.bvps }} |
| **P/E** | **{{ bo.pe_before }}x** | **{{ bo.pe_after }}x** | **{{ bo.pe_after }}x** |

Read the two bold rows. Market cap is unchanged; P/E is unchanged. Everything
per share halved because there are twice as many shares. The only difference
between the bonus and the split columns is the accounting: the bonus
capitalised ₹{% include inr.html n=a1.reserves_capitalised_lakh %} lakh of reserves into share capital (face value held at
₹{{ bo.face_value }}); the split left share capital alone and halved the face value.

For a real-world instance: HDFC Bank issued 1:1 bonus shares in August 2025.
Its share price roughly halved on the ex-date, its EPS and book value per
share halved with it, and anyone comparing its post-bonus EPS with its FY25
EPS without adjusting would conclude profit had collapsed. It hadn't. This is
why any per-share history — EPS, DPS, price charts — has to be *adjusted* for
splits and bonuses, and why data providers publish "adjusted" series.

## Why companies do it

Officially: to improve liquidity. A ₹5,000 share is awkward for a small
retail buyer; ₹500 is not. Bonus issues also signal that reserves are healthy
enough to capitalise. Unofficially: a lower price can *feel* "cheaper" to many
retail investors, and companies know it. The
[market cap post]({% post_url 2026-09-27-market-cap %}) made the point that
price per share on its own tells you nothing; a split is the cleanest possible
demonstration.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

You have one pizza cut into 8 slices. Someone cuts every slice in half — now
you have 16 slices. Do you have more pizza? No. Each slice is half the size.

A "₹320 share" after a split is a half-slice. It's not cheaper pizza; it's a
smaller piece of the same pizza.

</details>

## Common mistakes

- **Thinking a post-split share is cheap.** Same company, smaller slice.
  Compare P/E, P/B or EV (enterprise value) multiples, never price.
- **Comparing unadjusted per-share figures across a bonus or split.** EPS
  "falling" 50% on the ex-date is arithmetic, not performance.
- **Treating a bonus as free money.** You own the same fraction of the same
  company. The "gift" is a re-labelling of reserves you already owned.
- **Confusing face value with book value or price.** Face value is a nominal
  amount that only a split (or consolidation) changes. Book value per share is
  [equity divided by shares]({% post_url 2026-09-22-book-value-per-share %}).
  Price is what the market pays. Three different numbers.
- **Missing that dividends declared "per cent" are on face value.** A "300%
  dividend" on a ₹1 face value is ₹3 a share, not 300% of anything you paid.

**Takeaway:** face value is the nominal amount on a share, unrelated to price;
splits and bonuses multiply the share count and divide everything per share
by the same factor. Desi Bites at ₹320 after a 1:1 bonus is exactly as
expensive as it was at ₹640 — same market cap, same P/E, twice the slices.
