---
layout: post
title: "Step-up SIPs: the arithmetic of raising your SIP every year"
description: "What raising a SIP by 5% or 10% a year did over 10, 15 and 20 years of real index-fund NAVs: a bigger corpus from bigger contributions, not a better return."
image: /assets/og/step-up-sips.png
date: 2026-10-25 09:00:00 +0530
series: mutual-funds
term: "Step-up SIP"
---

{% assign m = site.data.mf3 %}
{% assign s = m.stepup %}
{% assign src = m.sources %}
{% assign t10 = s.rows[0] %}
{% assign t15 = s.rows[1] %}
{% assign t20 = s.rows[2] %}
{% assign c = s.constant %}
{% assign st = s.same_total_10y %}
{% assign rl = s.rolling_10y %}

## A SIP that grows with you

A regular **SIP — systematic investment plan** — invests the same amount
every month. The [SIP post]({% post_url 2026-10-01-sips-xirr-and-timing-myths %})
ran ₹10,000 a month through twenty years of a Nifty 50 index fund.

But salaries rarely stay flat for twenty years. A **step-up SIP** (fund houses
also call it a top-up SIP) raises the instalment automatically at a fixed
interval — usually once a year — by a fixed percentage or a fixed rupee
amount. Many fund houses and platforms offer it as an option when you set up
the SIP.

It's often sold with a striking chart of how much bigger the final corpus
gets. That chart is true. It's also mostly showing you that you invested
more money. This post separates the two.

## The formula

```
Instalment in year k  =  A × (1 + g)^(k − 1)

  A = starting monthly instalment
  g = annual step-up (e.g. 0.10 for 10%)
  k = 1, 2, 3, … (the same amount every month within a year)

Total invested over Y years  =  12 × A × [(1 + g)^Y − 1] / g       (flat SIP: 12 × A × Y)
```

The final value is each instalment compounded for however long it was
invested, added up — which is why [XIRR]({% post_url 2026-10-01-sips-xirr-and-timing-myths %})
(extended internal rate of return, the single annual rate that fits all
those cash flows) is the right way to measure it.

One consequence of that formula matters more than any other: **a step-up
SIP puts more of its money in late**. In a ten-year, 10% step-up, the last
year's instalments are ₹{% include inr.html n=t10.step_10.last_instalment %} a month against
₹{% include inr.html n=s.base %} in the first year. Late money has less time to compound, so
its share of the final value depends heavily on the last few years' returns.

## First, with a steady return

If every month earned exactly the same return, how would the two compare?
Take a constant {{ c.rate_pct }}% a year, ₹{% include inr.html n=s.base %} a month to start, {{ c.years }} years:

| | Invested | Final value | Return (XIRR) |
|---|---:|---:|---:|
| Flat SIP | ₹{% include inr.html n=c.flat.invested %} | ₹{% include inr.html n=c.flat.value %} | {{ c.rate_pct }}% |
| 10% step-up | ₹{% include inr.html n=c.step_10.invested %} | ₹{% include inr.html n=c.step_10.value %} | {{ c.rate_pct }}% |

The step-up ends with a bigger corpus because it invested more rupees. Its
*return* is identical — with a constant rate, every rupee earns the same
{{ c.rate_pct }}% however long it's invested. So any difference in XIRR between the two on
real data comes from *when* the market did well, not from stepping up.

## Worked example: real NAVs

UTI Nifty 50 Index Fund, regular plan, growth option — the fund used
throughout this series (scheme code {{ src.index_fund.regular_code }} with AMFI, the Association of Mutual Funds in
India; source {{ src.label }}). ₹{% include inr.html n=s.base %} a month on the first of every month, raised
each April by 0%, 5% or 10% (rounded to the rupee), all ending
{{ src.end | date: "%-d %B %Y" }}. Historical data, for illustration only.

| Period | Step-up | Invested | Final value | XIRR | Last monthly instalment |
|---|---|---:|---:|---:|---:|{% for x in s.rows %}
| {{ x.label }} | None | ₹{% include inr.html n=x.step_0.invested %} | ₹{% include inr.html n=x.step_0.value %} | {{ x.step_0.xirr_pct }}% | ₹{% include inr.html n=x.step_0.last_instalment %} |
| | 5% a year | ₹{% include inr.html n=x.step_5.invested %} | ₹{% include inr.html n=x.step_5.value %} | {{ x.step_5.xirr_pct }}% | ₹{% include inr.html n=x.step_5.last_instalment %} |
| | 10% a year | ₹{% include inr.html n=x.step_10.invested %} | ₹{% include inr.html n=x.step_10.value %} | {{ x.step_10.xirr_pct }}% | ₹{% include inr.html n=x.step_10.last_instalment %} |{% endfor %}

(The twenty-year run has {{ t20.step_0.instalments }} instalments, not 240, because the fund's first
NAV (net asset value) in the data is 3 April 2006 — the same reason as in the SIP post. Its flat
row matches that post's ₹{% include inr.html n=t20.step_0.value %}.)

Reading the table:

1. **The corpus grows a lot.** Over twenty years a 10% step-up ended at
   ₹{% include inr.html n=t20.step_10.value %} against ₹{% include inr.html n=t20.step_0.value %} for the flat SIP.
2. **So did the money put in.** It invested ₹{% include inr.html n=t20.step_10.invested %} against
   ₹{% include inr.html n=t20.step_0.invested %}. The bigger corpus is the bigger contributions plus the
   growth on them.
3. **The return didn't improve.** In all three periods, the step-up's XIRR was
   equal to or slightly *below* the flat SIP's — {{ t10.step_10.xirr_pct }}% against {{ t10.step_0.xirr_pct }}% over
   ten years. These windows all end on {{ src.end | date: "%-d %B %Y" }}, just after
   a quarter in which the index fund fell, and a step-up SIP's largest
   instalments are its most recent ones, so it felt that fall more.

That last point is about the end date, not about step-ups in general, so it
needs a base rate. Across all {{ rl.windows }} ten-year windows starting on the first of each
month from {{ rl.first_start | date: "%B %Y" }} to {{ rl.last_start | date: "%B %Y" }} (overlapping, so
not independent), the 10% step-up's XIRR was higher than the flat SIP's in
{{ rl.step_xirr_higher }} and lower in {{ rl.step_xirr_lower }}. So it came out ahead more often than not — but by a
median of only {{ rl.median_gap_pp }} percentage points, and the range ran from
{% include inr.html n=rl.min_gap_pp %} to +{{ rl.max_gap_pp }} points. A step-up tilts the return towards whatever the
later years of the plan do; when those years were good it helped a little,
and when they were bad, as in the window ending March 2026, it hurt. It mainly changes
the amount invested and its timing, and the market decides the rest.

## The fair comparison: same money, different timing

If a step-up SIP's advantage is "more money", compare it with a flat SIP
that invests the **same total**. Over the ten years to March 2026, the 10%
step-up put in ₹{% include inr.html n=t10.step_10.invested %}; a flat SIP of
₹{% include inr.html n=st.monthly %} a month invests almost exactly the same
(₹{% include inr.html n=st.invested %}).

| Same total invested, ten years | Final value | XIRR |
|---|---:|---:|
| 10% step-up, from ₹{% include inr.html n=s.base %} | ₹{% include inr.html n=t10.step_10.value %} | {{ t10.step_10.xirr_pct }}% |
| Flat, ₹{% include inr.html n=st.monthly %} a month | ₹{% include inr.html n=st.value %} | {{ st.xirr_pct }}% |

The flat SIP ended with more — and across all {{ rl.windows }} ten-year windows above, the
same-total flat SIP finished ahead in {{ rl.same_total_flat_ahead }} of them. It's no mystery: the same rupees
invested *earlier* had longer to compound, in a market that rose over every
ten-year window in this fund's history (the
[rolling returns post]({% post_url 2026-09-27-rolling-returns %}) has the
distribution).

That isn't an argument against step-ups. Most people can't invest ₹{% include inr.html n=st.monthly %}
a month in year one if their income only allows ₹{% include inr.html n=s.base %}. A step-up is a
**contribution schedule** that tracks a rising income; it's the right tool
for that job. It just isn't a return strategy, and a chart showing its bigger
corpus without the bigger contributions beside it is telling you half the
story.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

You plant one mango sapling every month. Your friend plants one too — but
every year, she plants a few more a month than the year before.

After ten years she has a much bigger orchard. Is she a better farmer? No —
she planted more trees. Her newest trees are also still small, because they
were planted recently.

If you'd planted all her extra saplings in the first year instead, they'd
have had ten years to grow and your orchard would be bigger still. She
couldn't, because she only earned the money for them later. That's fine —
it just means her bigger orchard is about planting more, not growing faster.

</details>

## The thread through these posts

A step-up SIP is one more product whose name describes the feature and hides
the arithmetic — the same pattern as the other posts around this one. A
"balanced" fund is a mix, not a promise; an arbitrage fund's equity is
hedged; an international fund carries a currency and a limit; a ₹10 NFO (new fund offer) is a
unit size; the riskometer scores ingredients; a fund can drift without
changing its name; a side pocket decides who owns a loss. In every case the
label is the marketing, and the mechanism is what happens to your money.

## Common mistakes

- **Comparing a step-up SIP's corpus with a flat SIP's without showing the
  money invested.** The corpus gap is mostly a contribution gap. Put the
  "invested" column next to the "value" column, always.
- **Expecting a step-up to raise your return.** On a constant return it
  changes nothing; on real data it moved XIRR up in some windows and down in
  others.
- **Setting a step-up your income can't keep up with.** With a 10% step-up,
  the instalment in year ten is about {{ t10.step_10.last_instalment | times: 1.0 | divided_by: s.base | round: 1 }} times the first year's, and in
  year twenty about {{ t20.step_10.last_instalment | times: 1.0 | divided_by: s.base | round: 1 }} times. If you have to cancel it in year
  eight, the plan was the wrong size.
- **Forgetting that the late, large instalments carry the most timing risk.**
  A fall near the end of the plan hits the biggest sums invested for the
  shortest time — the same [sequence problem]({% post_url 2026-10-13-sequence-of-returns-risk %})
  withdrawals face, in reverse.

**Takeaway:** A step-up SIP builds a bigger corpus because it invests more
money, not because it earns a better return — on real index-fund data its
XIRR was sometimes higher and sometimes lower than a flat SIP's. It's the
right tool for matching savings to a rising income, as long as you judge it
by what you put in as well as what you got out.
