---
layout: post
title: "Authorised, issued and paid-up capital: three numbers, one company"
seo_title: "Authorised, issued and paid-up capital explained"
description: "Authorised capital is the ceiling, issued is what is offered, paid-up is what shareholders have paid. Desi Bites' IPO shows where the premium goes."
image: /assets/og/authorised-issued-paid-up-capital.png
date: 2027-03-06 09:00:00 +0530
series: jargon
term: "Share capital (authorised, issued, paid-up)"
---

{% assign cp = site.data.jargon_m9.capital %}

## What are the three kinds of share capital?

A company's share capital is usually described in three layers, and the numbers differ (company accounts also show subscribed capital, which this post leaves out; check the Companies Act, 2013 for the exact definitions):

- **Authorised capital** is the maximum amount of share capital the company is permitted to issue, as set out in its constitutional documents. It is a ceiling, and it can be raised by following the company's formal procedure.
- **Issued capital** is the part of that ceiling the company has actually offered to shareholders.
- **Paid-up capital** is the part shareholders have actually paid for. If shares are fully paid, issued and paid-up are the same. If a company has asked for only part of the face value, the paid-up figure is lower.

All three are counted at **face value** (also called par value), the nominal amount per share, as described in the [face value post]({% post_url 2026-10-12-face-value-splits-and-bonuses %}). The price investors pay above face value does not go into share capital; it goes into a separate reserve called **securities premium**. This post uses Desi Bites Foods, the blog's fictional company, and assumes an authorised capital for it. It doesn't describe any real company's capital structure, and rules for raising authorised capital are not covered here. It is part of the [Jargon, Decoded]({{ '/series/jargon/' | relative_url }}) series.

## The formula

```
Paid-up capital     =  number of shares issued × face value × (share of the face value called and paid)
Securities premium  =  (issue price − face value) × number of new shares
Money raised        =  new paid-up capital + securities premium
```

For fully paid shares, paid-up capital is simply shares × face value.

## Worked example: Desi Bites before and after its IPO (initial public offering)

Desi Bites' face value is ₹{{ cp.face }} a share. Assume its authorised capital is {{ cp.authorised_shares_lakh | round }} lakh shares, ₹{{ cp.authorised_capital_lakh | round }} lakh. Amounts in ₹ lakh:

| | Shares (lakh) | Paid-up capital (₹ lakh) | Room left under the authorised limit (lakh shares) |
|---|---:|---:|---:|
| Before the IPO | {{ cp.pre_ipo_shares_lakh }} | {{ cp.pre_ipo_paid_up_lakh }} | {{ cp.pre_ipo_headroom_lakh }} |
| New shares in the IPO | {{ cp.fresh_shares_lakh }} | {{ cp.capital_added_lakh }} | |
| After the IPO | {{ cp.post_ipo_shares_lakh }} | {{ cp.post_ipo_paid_up_lakh }} | {{ cp.post_headroom_shares_lakh }} |

The IPO priced the shares at ₹{{ cp.ipo_price }}, which is ₹{{ cp.premium_per_share }} above face value. So of the money raised, only the face value part joined share capital. The rest went into securities premium:

| Where the IPO money went | ₹ lakh |
|---|---:|
| Share capital: {{ cp.fresh_shares_lakh }} lakh shares × ₹{{ cp.face }} | {{ cp.capital_added_lakh }} |
| Securities premium: {{ cp.fresh_shares_lakh }} lakh shares × ₹{{ cp.premium_per_share }} | {{ cp.premium_lakh }} |
| **Total raised** | **{{ cp.proceeds_lakh }}** |

That total is before issue expenses. Both lines sit within equity on the balance sheet, so the equity jump you see after an IPO is mostly premium and not share capital. The share count of {{ cp.post_ipo_shares_lakh }} lakh shares fits under the {{ cp.authorised_shares_lakh | round }} lakh authorised, with {{ cp.post_headroom_shares_lakh }} lakh to spare. If it did not, the company would have to raise the ceiling first.

## A partly paid share

Occasionally a company calls the price in instalments. Suppose {{ cp.partly_paid_example.shares_lakh | round }} lakh shares of face value ₹{{ cp.face }} are issued, with ₹{{ cp.partly_paid_example.called_per_share }} per share called so far. The issued capital is ₹{{ cp.partly_paid_example.issued_lakh | round }} lakh, the paid-up capital is ₹{{ cp.partly_paid_example.paid_up_lakh | round }} lakh, and the remaining ₹{{ cp.partly_paid_example.uncalled_per_share }} per share is uncalled. Authorised ≥ issued ≥ paid-up, always.

## Common mistakes

- **Reading authorised capital as money in the bank.** It is a permission, not an amount raised.
- **Confusing share capital with equity.** Equity includes reserves and the securities premium. Share capital is only the face-value part.
- **Using share capital to compute shares outstanding without checking the face value.** ₹{{ cp.pre_ipo_paid_up_lakh | round }} lakh of capital is {{ cp.pre_ipo_shares_lakh | round }} lakh shares only because the face value is ₹{{ cp.face }}. After a split, the same capital is more shares.
- **Treating the IPO price as the amount per share added to capital.** Only face value is.

**Takeaway:** Authorised capital is the ceiling, issued capital is what has been offered, and paid-up capital is what shareholders have paid, all at face value. In an IPO priced well above face value, most of the money goes into securities premium, not share capital.
