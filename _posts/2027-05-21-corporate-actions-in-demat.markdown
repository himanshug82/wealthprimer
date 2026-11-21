---
layout: post
title: "Corporate actions in your demat: what arrives, and when"
seo_title: "When are bonus shares credited? Corporate actions in demat"
description: "Bonuses, splits and dividends change what's in your demat account and bank. What each one does to your holding, and SEBI's T+2 timeline for bonus shares."
image: /assets/og/corporate-actions-in-demat.png
date: 2027-05-21 09:00:00 +0530
series: market-basics
term: "Corporate action credit"
needs_review: regulation
rules_as_of: "November 2026"
---

{% assign c = site.data.market_basics_m2.corp %}

## What a corporate action is

A **corporate action** is something a company does that changes what its
shareholders hold: a bonus issue, a stock split, a dividend, a rights issue,
a merger. Each one is tied to a **record date**: the date on which the
company checks who its shareholders are. Whoever is on the register that day
gets the benefit. Because trades settle the next working day, the
**ex-date** (the first day a buyer no longer gets it) is now the record date
itself, and the last day to buy and still get it is the working day before,
as the [record date and ex-date post]({% post_url 2026-10-17-record-date-and-ex-date %})
explains.

This post follows three common ones into your demat account and bank
account. It's part of
[Your first year in the market]({{ '/series/market-basics/' | relative_url }}),
and builds on [face value, splits and bonuses]({% post_url 2026-10-12-face-value-splits-and-bonuses %}).

## The rules for bonus shares

For bonus issues announced on or after {{ c.bonus_from }}, circular
[CIR/CFD/PoD/2024/122 of 16 September 2024]({{ c.bonus_url }}) from SEBI (the
Securities and Exchange Board of India) sets this timeline, where T is the
record date.

| Day | What happens |
|---|---|
| T (record date) | The company's shareholders on this date are entitled to the bonus |
| T+1 | Deemed date of allotment. The company submits the documents to the depositories by 12 noon for the shares to be credited |
| T+2 | The bonus shares are available for trading |

The bonus shares can now be credited straight into the stock's existing ISIN
(International Securities Identification Number, the code that identifies a
security), rather than a temporary one, as was required before.

## Worked example: one holding, three actions

A hypothetical holding of {{ c.shares }} shares at ₹{{ c.price }}, worth
₹{% include inr.html n=c.value %}. Each action below is separate, and each
ignores market moves.

| Action | Shares after | Price after (ignoring market moves) | Value | Where it arrives |
|---|---:|---:|---:|---|
| Bonus, {{ c.bonus_ratio }} | {{ c.bonus_shares_after }} | ₹{{ c.bonus_price }} | ₹{% include inr.html n=c.value %} | New shares in your demat account; tradable on T+2 |
| Split, face value ₹{{ c.split_from }} to ₹{{ c.split_to }} | {{ c.split_shares_after }} | ₹{{ c.split_price }} | ₹{% include inr.html n=c.value %} | Your demat holding is replaced by the new count |
| Dividend of ₹{{ c.dividend_per_share }} a share | {{ c.shares }} | Falls by about the dividend on the ex-date | Unchanged in total, now part cash | ₹{% include inr.html n=c.dividend_total %} to the bank account linked to your demat account, before any tax deducted |

Neither a bonus nor a split changes the total value of the holding: more
shares, each worth proportionately less. A dividend moves value out of the
share price into your bank account.

## Common mistakes

1. **Thinking you can buy on the record date and get the benefit.** With T+1
   settlement, a buyer on the record date isn't on the register in time; the
   last day to buy is the working day before.
2. **Panicking at a lower price after a bonus or split.** The price falls
   because there are more shares. Check the share count before reading the
   price as a loss.
3. **Missing a dividend because of an old bank account.** It goes to the bank
   account linked to your demat account; keep it current.
4. **Forgetting rights entitlements.** A rights issue credits rights
   entitlements to your demat account, which lapse if not used or sold, as
   the [rights issue post]({% post_url 2026-10-19-rights-issues %}) explains.

How dividends are taxed is covered in the
[dividends and interest post]({% post_url 2026-11-30-dividends-and-interest %}).

**Takeaway:** A bonus or a split gives you more shares at a proportionately
lower price, and a dividend moves money from the share price to your bank
account. Bonus shares are now credited for trading two working days after the
record date.

## Sources

- SEBI circular CIR/CFD/PoD/2024/122, [16 September 2024]({{ c.bonus_url }}), "Enabling T+2 trading of Bonus shares where T is the record date" (NSE's copy of the circular), read on 21 November 2026.
