---
layout: post
title: "Capital allocation: what a company does with a rupee it doesn't need"
description: "Six things a company can do with spare cash, and one test that ranks them: does the return clear the cost of capital? Desi Bites' IPO money, a year on."
image: /assets/og/capital-allocation.png
date: 2026-11-18 09:00:00 +0530
series: fundamental-analysis
term: "Capital allocation"
---

{% assign c2 = site.data.case_study_2 %}
{% assign ca = c2.capital_allocation %}
{% assign a = c2.acquisition %}
{% assign f = c2.fy26 %}
{% assign r = f.ratios %}
{% assign cs = site.data.case_study %}

## The decision that compounds

Everything in the first module was about *measuring* a business. This post
is about the one decision management makes that changes what the
measurements will say in five years: what to do with the cash the business
throws off.

A company that generates [free cash flow]({% post_url 2026-09-19-free-cash-flow %})
has six options. It can reinvest in the existing business, buy another one,
pay down debt, pay a dividend, buy back its own shares, or sit on the cash.
Every rupee goes to one of the six. Over a decade, the *pattern* of those
choices — not the margin, not the growth rate — decides whether a good
business made its shareholders rich or merely made its managers busy.

There is one test that ranks the six, and this blog already built it.

## The test

```
Is the expected return on this use of cash  >  the cost of that cash (WACC)?
```

The [WACC post]({% post_url 2026-10-03-wacc-cost-of-capital %}) worked out that
Desi Bites' capital costs about {{ ca.hurdle_wacc }}% a year. Any use of cash that earns
less than that destroys value — even if it makes profit go up, even if it
makes the company bigger. The [ROCE post]({% post_url 2026-09-03-roce %}) made the
same point from the other side: ROCE above WACC is value creation, ROCE
below it isn't. Capital allocation is that comparison, applied one decision
at a time.

## Desi Bites' ₹1,600 lakh

In June 2025 Desi Bites raised ₹{% include inr.html n=ca.ipo_proceeds %} lakh in its IPO. Twelve months
later, here is where it went and what each use is earning:

| Use of cash | ₹ lakh | Expected return | Clears {{ ca.hurdle_wacc }}%? |
|---|---:|---:|---|{% for o in ca.options %}
| **{{ o.option }}** | {% if o.amount %}{{ o.amount }}{% else %}—{% endif %} | {% if o.expected_return_pct %}{{ o.expected_return_pct }}%{% else %}n/a{% endif %} — {{ o.basis }} | {% if o.expected_return_pct == nil %}—{% elsif o.expected_return_pct > ca.hurdle_wacc %}**Yes**{% else %}No{% endif %} |{% endfor %}

Actually deployed in FY26: ₹{% include inr.html n=ca.deployed_fy26.acquisition %} lakh on the acquisition and ₹{% include inr.html n=ca.deployed_fy26.capex_from_proceeds %} lakh on
capex; ₹{% include inr.html n=ca.deployed_fy26.still_in_cash %} lakh more sits in the bank than a year ago. Each row is worth
a paragraph.

**Cash.** The safest choice and, judged by the test, the worst. Fixed
deposits earn about 6.5% before tax, roughly {{ ca.options[0].expected_return_pct }}% after — some {{ ca.idle_cash_drag_pct_points }}
percentage points below the hurdle, every year the money sits there.
Desi Bites ended FY26 with ₹{% include inr.html n=ca.cash_pile_fy26 %} lakh of cash, {{ ca.cash_pct_of_total_assets }}% of total assets.
The visible cost is in the ROE: FY25's {{ r.roe_fy25_closing }}% became {{ r.roe_on_closing_equity }}% on closing
equity, not because the business got worse but because the denominator
filled up with idle money. Cash has a real option value — the ability to
act when a competitor stumbles — but "we're keeping our powder dry" is
also the most common excuse for not having a plan.

**Repaying debt.** Earns exactly the after-tax interest saved, {{ ca.options[1].expected_return_pct }}% here.
Below the hurdle, so on the test it's a poor use — *for this company*. For
a company whose debt is expensive or whose lenders are nervous, retiring
it is the best available return, and the peace of mind doesn't show in the
arithmetic.

**Organic capex.** The strongest case on paper: if a new production line
earns what the existing business earns — a [ROCE]({% post_url 2026-09-03-roce %}) of
{{ cs.ratios.FY25.roce }}% — it clears the hurdle by a mile. The catch is the *if*. The first
line was built into demand the founders knew personally. The second line
needs demand that doesn't yet exist, in states the brand hasn't reached.
Incremental returns are usually lower than average returns, and the
prospectus promised ₹700 lakh of this; ₹{{ ca.deployed_fy26.capex_from_proceeds }} lakh was spent.

**The acquisition.** Judged on year one, {{ ca.acquisition_case.year1_roic }}%. Judged on management's
case — Chatpata's revenue growing 15% with margins converging toward Desi
Bites' own — about {{ ca.acquisition_case.management_case_roic }}%. Still below the hurdle. The
[goodwill post]({% post_url 2026-11-17-goodwill-exceptional-items-and-other-income %})
explained why acquisitions look like this: the seller knows the business
better than the buyer and sets the price accordingly, and the buyer
justifies the premium with synergies that are real about half the time.
The empirical record of acquisitions destroying acquirer value is one of
the most robust findings in corporate finance. It doesn't mean never; it
means the burden of proof sits with the deal.

**Dividends.** A dividend earns the shareholder whatever *they* do with
it, so it can't be scored on the company's hurdle. Its logic is the
reverse of the test: **if the company can't find uses that clear the
hurdle, it should hand the money back.** Desi Bites paying ₹{{ f.dividend }} lakh while
holding ₹{% include inr.html n=ca.cash_pile_fy26 %} lakh idle is a small gesture in that direction. The
[dividend yield post]({% post_url 2026-09-28-dividend-yield %}) covered what the
shareholder sees; this is what the board sees.

**Buybacks.** Also a return of capital, with a twist: the company buys
shares, so the return depends entirely on the price paid. Buying back
stock at a [P/E]({% post_url 2026-09-24-price-to-earnings %}) of 38 is accepting an
earnings yield of {{ ca.earnings_yield_at_ipo_price }}% — below the hurdle again. Buying back at a P/E
of 10 is a 10% yield on money the company knows better than any other
investment. Buybacks are excellent or terrible depending on one number,
and companies tend to do them when the stock is expensive and cash is
plentiful, which is the wrong end. (How a buyback is taxed in the
shareholder's hands has changed twice since 2024; the tax series covers
it.)

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

You've saved ₹1,000 from your lemonade stand. What do you do with it?

You could buy a second table and jug (more lemonade, if there are more
customers). You could buy your friend's stand (but he wants ₹600 for
something that only earns ₹10 a summer). You could pay back the ₹200 you
borrowed from your sister. You could give some to the people who lent you
money at the start. Or leave it in a jar.

The jar is easy and earns nothing. Each of the others is a bet. The
question for every rupee is the same: *will this earn more than I'd get
just by not doing anything silly with it?* A company's version of "not
doing anything silly" is called the cost of capital, and it's about 14% a
year for Desi Bites.

</details>

## How to read a company's allocation record

You can't see the decision being made, but you can see the pattern over
five to ten years, in three places:

**The cash flow statement.** Investing activities show capex and
acquisitions; financing shows debt repaid, dividends and buybacks. Add up
ten years and you have the company's revealed preferences.

**Incremental ROCE.** Take the change in operating profit over five years
and divide by the change in capital employed. That's roughly what the
*new* money earned. A company with a 30% ROCE and a 9% incremental ROCE
is living off an old plant and wasting new cash.

**Goodwill and impairments.** A balance sheet where goodwill grows every
year is a serial acquirer. Impairments in the notes are the acquisitions
that didn't work, admitted late.

The best allocators are rare and look boring: they reinvest when returns
are high, buy back when the stock is cheap, hand cash back when neither is
true, and say so in plain language in the annual report. The worst look
exciting — a deal a year, a rising cash pile that's "strategic," and a
chairman's letter about transformation.

## Common mistakes

- **Judging a decision by whether profit went up.** Buying a fixed deposit
  raises profit. So does buying a 5% business with 14% money. The test is
  return versus cost of capital, not more versus less.
- **Applauding cash on the balance sheet.** Safety, yes. But a cash pile
  earning 5% inside a 14% company is a drag the ROE line will show, and
  the ROE post is where beginners misread it as the business weakening.
- **Treating dividends as generosity.** A dividend is an admission that
  the company has nothing better to do with the money. Often that's the
  right admission. It isn't a gift.
- **Cheering buybacks without checking the price.** A buyback at a high
  multiple transfers value from remaining shareholders to selling ones.
- **Taking acquisition synergies at face value.** The seller priced them
  in. Judge the deal on the target's margins two years later.
- **Confusing average ROCE with incremental ROCE.** The average is
  history. The incremental figure is what your money, invested today,
  is actually earning.

**Takeaway:** Every rupee a company keeps goes to one of six uses —
reinvest, acquire, repay, pay out, buy back, or hold — and one test ranks
them: does the expected return beat the cost of capital? On that test Desi
Bites' idle ₹{% include inr.html n=ca.cash_pile_fy26 %} lakh earns {{ ca.options[0].expected_return_pct }}% inside a {{ ca.hurdle_wacc }}% company, its acquisition
earned {{ ca.acquisition_case.year1_roic }}% in year one, and its ROE fell from {{ r.roe_fy25_closing }}% to {{ r.roe_on_closing_equity }}% without the
business getting worse. Capital allocation is the decision the ratios can't see
happening, and the one they'll be reporting on for the next decade.
