---
layout: post
title: "Specialised investment funds: what the SIF label means"
description: "A specialised investment fund is a mutual fund product with flexible strategies and a ₹10 lakh minimum. What SEBI's rules say, and how a breach is handled."
image: /assets/og/specialised-investment-funds.png
date: 2027-02-07 09:00:00 +0530
series: mutual-funds
term: "Specialised investment fund (SIF)"
needs_review: regulation
rules_as_of: "November 2026"
---

{% assign f = site.data.mf5.sif %}
{% assign m = site.data.mf5.merger %}

## What a SIF is

A **specialised investment fund** (SIF) is a product run by a mutual fund
house under the SEBI (Mutual Funds) Regulations, 2026, with more room to
manoeuvre than an ordinary scheme. SEBI is the Securities and Exchange Board
of India. In SEBI's own FAQ, it offers "advanced
investment strategies with greater portfolio flexibility, including limited
unhedged short exposure through derivatives", and sits between regular
mutual funds and PMS (portfolio management services).

The labels differ too: a SIF's products are called **investment strategies**,
not schemes, and must be kept visibly separate from the fund house's ordinary
schemes. This post sets out the rules as read in November 2026. It's part of
[Mutual Funds, Minus the Marketing]({{ '/series/mutual-funds/' | relative_url }}),
and assumes the [fund categories post]({% post_url 2026-10-14-sebi-fund-categories-decoded %}).

## The rules

From [the Regulations]({{ m.regs_url }}) (chapter IX, regulations 47 to 55)
and [SEBI's SIF FAQ for investors]({{ f.faq_url }}) of {{ f.faq_date }}:

| Feature | Ordinary mutual fund scheme | SIF investment strategy |
|---|---|---|
| Minimum investment | Set by each scheme | ₹{{ f.min_lakh }} lakh in aggregate across the SIF's strategies, per PAN (permanent account number); accredited investors (a category defined under SEBI's alternative investment fund regulations) exempt (regulation {{ f.regulation }}) |
| Strategies | Within the scheme's category rules | More flexible, including limited unhedged short positions through derivatives |
| Redemption | Mostly daily | Open-ended, close-ended or interval, with the frequency set in the offer document (regulation 50) |
| Identity | Under the mutual fund's name | Distinct identification and a separate website from the mutual fund's (regulation 53) |
| What you hold | Units of a pooled scheme | Units of a pooled strategy; not an individually managed portfolio, unlike PMS |

For joint holdings, the threshold is checked against the first holder's PAN.
Investments in the same fund house's ordinary schemes don't count towards it.

## Worked example: what a breach does

The ₹{{ f.min_lakh }} lakh minimum must be maintained (FAQ A6), and the FAQ
separates two ways of falling below it. A hypothetical investor holds
₹11 lakh across two strategies of one SIF.

| What happens | Type | Consequence (per the FAQ) |
|---|---|---|
| A market fall takes the value to ₹9.5 lakh | Passive breach | No forced redemption. The investor can keep holding, but can only redeem the whole investment in that SIF, not part of it, while below the minimum |
| The investor redeems ₹2 lakh, leaving ₹9 lakh | Active breach | All units in that SIF are frozen for debit; {{ f.restore_days }} calendar days to restore the minimum; if not restored, the units are redeemed automatically at the NAV (net asset value) of the next business day after the {{ f.restore_days }}th day |

For units held as a statement of account, a redemption that would cause an
active breach may simply be rejected.

## Common mistakes

1. **Reading "mutual fund" as "same as any mutual fund".** A SIF runs inside
   the mutual fund framework but can use strategies ordinary schemes can't,
   including short positions. SEBI's FAQ says it "carries relatively higher
   risk".
2. **Assuming daily liquidity.** A strategy may be interval or close-ended,
   and the FAQ (A15) says debt strategies "cannot offer daily redemptions"
   (the minimum frequency is once a week) and hybrid strategies neither
   (twice a week). A strategy may also require a notice period of up to 15
   working days (A17). The strategy's information
   document sets the terms.
3. **Treating the minimum as a one-time entry fee.** It is an ongoing
   threshold. A partial redemption that takes you below it triggers the
   freeze and the {{ f.restore_days }}-day clock.
4. **Comparing a SIF with PMS on labels alone.** In PMS the portfolio is
   managed for you individually; in a SIF you hold units of a pool, as the
   FAQ puts it. Costs, tax and reporting differ too; read each product's
   documents.

**Takeaway:** A specialised investment fund is a mutual fund product with room
for more complex strategies, a ₹{{ f.min_lakh }} lakh minimum per PAN that must
be maintained, and redemption terms that may not be daily. The label
promises flexibility, not safety.

## Sources

- [SEBI (Mutual Funds) Regulations, 2026, as amended to 10 October 2026]({{ m.regs_url }}), chapter IX (regulations 47 to 55), read on 21 November 2026.
- [SEBI, FAQs for Specialized Investment Funds, Part A – for investors]({{ f.faq_url }}), issued {{ f.faq_date }}.
