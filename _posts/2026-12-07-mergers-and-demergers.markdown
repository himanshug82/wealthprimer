---
layout: post
title: "Mergers and demergers: what happens to your shares"
description: "In a merger you receive shares at a set ratio; in a demerger you keep yours and get new ones. The swap ratio worked through, with invented companies."
image: /assets/og/mergers-and-demergers.png
date: 2026-12-07 09:00:00 +0530
series: market-basics
needs_review: regulation
rules_as_of: "November 2026"
---

{% assign sc = site.data.market_basics.scheme %}
{% assign m = sc.merge %}
{% assign d = sc.demerge %}

## What a merger and a demerger do to your holding

A **merger** (also called an amalgamation) combines two companies into one. If you hold shares in the company that disappears, you receive shares of the surviving company, in a fixed **share exchange ratio**: so many new shares for every so many old ones. A **demerger** goes the other way. A company moves one of its businesses into a separate company, and its shareholders receive shares in that business, again at a fixed ratio, while they keep their original shares.

In both cases the exchange happens under the company's scheme: you are not asked to pay or sell, and the new shares are credited to your demat account. This post explains the mechanics and the approval steps. It uses invented companies and made-up prices, it says nothing about any real merger or demerger, and it is not a view on whether one is good for shareholders. It is part of [Your first year in the market]({{ '/series/market-basics/' | relative_url }}).

## The ratio, step by step

```
New shares = old shares held x (new shares per ratio / old shares per ratio)
Whole shares go to your demat account; any fraction is handled as the scheme says
```

### Merger: invented example

{{ m.b_name }} merges into {{ m.a_name }}. The scheme's ratio is **{{ m.ratio_new }} shares of {{ m.a_name }} for every {{ m.ratio_old }} shares of {{ m.b_name }}**. You hold {{ m.holding }} shares of {{ m.b_name }}.

| Step | Working | Result |
|---|---|---|
| Entitlement | {{ m.holding }} × {{ m.ratio_new }} ÷ {{ m.ratio_old }} | {{ m.entitled }} shares of {{ m.a_name }} |
| Whole shares credited | Whole part of {{ m.entitled }} | {{ m.whole }} |
| Left over | The fraction | {{ m.fraction_num }}/{{ m.ratio_old }} of a share ({{ m.fraction }}) |

You cannot hold 0.857 of a share, so the fraction needs a rule. SEBI's master circular on schemes of arrangement ({{ sc.master_circular }}; [source]({{ sc.master_url }}); as at {{ sc.as_of }}) says fractional entitlements are aggregated and held by a trust, which sells them in the market within {{ sc.fraction_trust_days }} days from the date of allotment, as the draft scheme says. The scheme document tells you how the proceeds reach you, so read it for that. **Check the current rule**: the circular was issued in June 2023 and can be amended.

Read the direction of the ratio carefully. "{{ m.ratio_new }} for {{ m.ratio_old }}" means {{ m.ratio_new }} shares of the surviving company for {{ m.ratio_old }} of the one being absorbed, so you end up with fewer shares than you started with. What each share is worth is a separate matter.

### Demerger: invented example

{{ d.parent }} demerges its beverages business into {{ d.child }}. Shareholders get **1 share of {{ d.child }} for every {{ d.per_old }} shares of {{ d.parent }} held**, and keep all their {{ d.parent }} shares. You hold {{ d.holding }}.

| Item | Before | After |
|---|---|---|
| {{ d.parent }} shares | {{ d.holding }} at ₹{{ d.pre_px }} | {{ d.holding }} at ₹{{ d.post_parent_px }} |
| {{ d.child }} shares | none | {{ d.child_shares }} at ₹{{ d.post_child_px }} |
| **Value of your holding** | **₹{% include inr.html n=d.value_before %}** | **₹{% include inr.html n=d.value_after %}** |

The {{ d.parent }} price fell ₹{{ d.parent_drop }} a share, and the holding is worth the same. That is because ₹{{ d.parent_drop }} is the value of the {{ d.child }} shares attached to each {{ d.parent }} share (¼ of a ₹{{ d.post_child_px }} share). The prices are made up to isolate the mechanics; real prices keep moving with the market, so a real price after a demerger will not line up this neatly.

For the date that decides who gets the new shares, see [record date and ex-date]({% post_url 2026-10-17-record-date-and-ex-date %}). Share splits and bonuses change your share count without changing what you own; those are in [face value, splits and bonuses]({% post_url 2026-10-12-face-value-splits-and-bonuses %}).

## The process before it reaches your account

The same master circular sets out the steps for a listed company. As written in the text we opened:

1. **Documents to the exchanges.** The company files the draft scheme with the stock exchanges, along with a valuation report from a registered valuer that shows the "fair share exchange ratio", a report from its audit committee, and a fairness opinion from a SEBI-registered merchant banker.
2. **Exchanges and SEBI review it.** SEBI (the Securities and Exchange Board of India) forwards comments from the public to the designated stock exchange for resolution.
3. **Shareholder vote.** The scheme sent to the NCLT (National Company Law Tribunal) for sanction must provide for e-voting by public shareholders. In some cases, for example where additional shares go to the promoter group, the scheme proceeds only if the public shareholders' votes in favour are more than those against.
4. **Sanction and allotment.** After sanction, shares are allotted and credited under the scheme.

One exception is worth knowing. The circular says a valuation report is not required where the shareholding pattern does not change. Its example: a company demerges a unit into a separate company that has exactly the same shareholders, each in the same proportion as before.

How the new shares are taxed, and how the cost of your old shares is split, are tax questions that this post does not cover. Check the current rule.

## Common mistakes

- **Reading a demerger-day price fall as a loss.** In the example the parent's price dropped ₹{{ d.parent_drop }} a share, but the holding's value did not change. Compare your total holding, not one price.
- **Reading the ratio backwards.** "{{ m.ratio_new }} for {{ m.ratio_old }}" and "{{ m.ratio_old }} for {{ m.ratio_new }}" give very different share counts.
- **Forgetting the fraction.** A holding that does not divide evenly leaves a fraction, and the scheme sets how it is paid out. {{ m.fraction_num }}/{{ m.ratio_old }} of a share is small, but it is not zero.
- **Treating an announced scheme as done.** A scheme needs the exchange review, the public-shareholder vote and sanction before shares move. The ratio you read in the announcement is the draft's.

**Takeaway:** In a merger or demerger the scheme's ratio decides how many new shares you get, whole shares are credited and fractions follow the scheme's rule. A price fall on a demerger date is not by itself a loss. Read the ratio's direction and the scheme document, and check the current SEBI rules.
