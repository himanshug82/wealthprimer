---
layout: post
title: "Diluted EPS: what stock options do to earnings per share"
seo_title: "Diluted EPS explained: Ind AS 33 and the treasury method"
description: "Diluted EPS adds the shares that options could create. Ind AS 33's weighted average and treasury-stock method, worked on Desi Bites' FY26 profit and ESOPs."
image: /assets/og/diluted-eps-and-dilution.png
date: 2027-04-05 09:00:00 +0530
series: fundamental-analysis
term: "Diluted EPS"
---

{% assign e = site.data.fa5.eps %}
{% assign ga = e.grants[0] %}
{% assign gb = e.grants[1] %}

## What diluted EPS means

**Basic EPS** (earnings per share) divides a year's profit by the average
number of shares that were actually outstanding. **Diluted EPS** asks what
EPS would have been if everything that could turn into shares had done so:
employee stock options, warrants, convertible bonds. Both are defined by
Ind AS 33 (the Indian Accounting Standard on earnings per share), and
companies within its scope present both on the face of the income statement.

The [EPS post]({% post_url 2026-09-23-eps %}) introduced the pair, and used
"pre-issue" and "post-issue" for a different comparison: the same profit
over the share count before and after an IPO (initial public offering).
This post is about the Ind AS 33 sense of "diluted". It's part of
[Fundamental Analysis]({{ '/series/fundamental-analysis/' | relative_url }}).

## The formulas

```
Basic EPS     =  profit attributable to the parent's shareholders
                 ÷  weighted average shares outstanding           (paras 10, 19–20)

Weighted average  =  shares at the start
                     +  new shares × days outstanding / days in the year

Diluted EPS   =  the same profit (adjusted for convertibles, if any)
                 ÷  (weighted average shares + dilutive potential shares)

Options (treasury-stock method, paras 45–47):
  Shares the option proceeds could buy at the average market price
      =  options × exercise price ÷ average market price
  Dilutive potential shares  =  options − shares those proceeds could buy
  An option counts only if exercise price < average market price;
  otherwise it is antidilutive and left out                       (paras 41–44)
```

The logic: if holders exercise, the company receives the exercise price.
Ind AS 33 assumes that cash buys back shares at the average market price,
so only the shortfall, the shares issued "for nothing", dilutes.

## Worked example: Desi Bites, FY26

[Desi Bites Foods]({{ '/case-study/' | relative_url }}) is fictional. Its
FY26 profit after tax was ₹{{ e.pat }} lakh, and as a
[consolidated]({% post_url 2027-03-29-consolidated-vs-standalone %}) group
with a wholly owned subsidiary, all of it belongs to its own shareholders.
This post adds three fictional facts: the IPO shares were allotted on
{{ e.allotment_date }}, before the {{ e.listing_date }} listing; FY26's
average share price was ₹{{ e.avg_price }}; and the company has two employee
stock option (ESOP) grants, made before the IPO and vested by FY26, for
illustration.

**Step 1: the weighted average share count.** Desi Bites started FY26 with
{{ e.pre_shares_lakh }} lakh shares and issued {{ e.fresh_shares_lakh }}
lakh in the IPO, outstanding for {{ e.days_outstanding }} of the year's
{{ e.days_fy }} days.

```
Weighted average  =  {{ e.pre_shares_lakh }}  +  {{ e.fresh_shares_lakh }} × {{ e.days_outstanding }} / {{ e.days_fy }}  =  {{ e.wavg_shares_lakh }} lakh shares
Basic EPS         =  ₹{{ e.pat }} lakh ÷ {{ e.wavg_shares_lakh }} lakh  =  ₹{{ e.basic }}
```

Earlier posts in this series quoted Desi Bites' FY26 EPS as
₹{{ e.year_end_eps }}, dividing by the {{ e.year_end_shares_lakh }} lakh
shares at the year-end. That's a simpler figure; the Ind AS 33 basic EPS
uses the weighted average, which is higher in a year when new shares arrived
part-way through.

**Step 2: test each grant.**

| Grant | Options (lakh) | Exercise price | vs average price ₹{{ e.avg_price }} | Shares the proceeds buy (lakh) | Shares "for nothing" (lakh) | Counted? |
|---|---:|---:|---|---:|---:|---|
| {{ ga.name }} | {{ ga.options_lakh }} | ₹{{ ga.exercise }} | below: in the money | {{ ga.shares_at_market_lakh }} | {{ ga.free_shares_lakh }} | Yes, dilutive |
| {{ gb.name }} | {{ gb.options_lakh }} | ₹{{ gb.exercise }} | above: out of the money | {{ gb.shares_at_market_lakh }} | — | No, antidilutive |

Grant B's holders would pay more than the average market price, so assuming
they exercise would *raise* EPS. Ind AS 33 leaves such options out.

**Step 3: diluted EPS.**

```
Diluted shares  =  {{ e.wavg_shares_lakh }}  +  {{ e.incremental_lakh }}  =  {{ e.diluted_shares_lakh }} lakh
Diluted EPS     =  ₹{{ e.pat }} lakh ÷ {{ e.diluted_shares_lakh }} lakh  =  ₹{{ e.diluted }}
```

Diluted EPS is {{ e.dilution_pct }}% below basic. Had we simply added every
option to the share count, the result would have been ₹{{ e.naive_all_options }},
overstating the dilution for two reasons: it ignores the cash the options
bring in, and it counts an out-of-the-money grant.

One more detail from the standard: for employee options, the "exercise
price" in this test also includes the value of any service employees still
have to give before the options vest (paragraph 47A). Both grants here have
vested, so the exercise price alone applies.

## Common mistakes

1. **Using "diluted" for "after the IPO".** In Ind AS 33, dilution comes from
   potential shares such as options and convertibles, not from new shares
   already issued; those are in basic EPS through the weighted average.
2. **Adding all options to the share count.** The treasury-stock method
   counts only the shares issued for no consideration, and only for options
   in the money at the average price.
3. **Assuming the gap between basic and diluted stays put.** It moves with
   the share price: a higher average price makes more grants dilutive and
   each one more so. A company with a large ESOP pool can show a growing gap
   in a rising market. The [ESOPs and RSUs (restricted stock units) post]({% post_url 2026-12-02-esops-and-rsus %})
   covers how those grants are taxed for the employee.
4. **Mixing EPS bases in a P/E.** A [P/E]({% post_url 2026-09-24-price-to-earnings %})
   (price-to-earnings ratio) built on year-end shares, basic EPS or diluted EPS
   can differ noticeably in an IPO year. State which one you used.

**Takeaway:** Diluted EPS asks what earnings per share would be if every
option and convertible that could become a share did. Ind AS 33 counts only
the in-the-money part, net of the cash exercise would bring in, so the gap
from basic EPS is usually smaller than the raw option count suggests.

## Sources

- Ind AS 33, *Earnings per Share*, paragraphs 10, 19–21, 41–47A and 66, read on
  21 November 2026 in [a copy of the standard](https://ca2013.com/wp-content/uploads/2017/03/INDAS33.pdf)
  on the Companies Act Integrated Ready Reckoner, a third-party site (a 2017
  upload), because the Ministry of Corporate Affairs' (MCA's) [Ind AS page](https://www.mca.gov.in/content/mca/global/en/acts-rules/ebooks/accounting-standards.html)
  refuses automated requests. Check against MCA's current text.
