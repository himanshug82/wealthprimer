---
layout: post
title: "Liquid and overnight funds: where idle cash waits"
description: "Overnight and liquid funds hold debt that matures in a day or within 91 days. What SEBI's rules require, and what four funds' NAVs did over five years."
image: /assets/og/liquid-and-overnight-funds.png
date: 2026-11-03 09:00:00 +0530
series: mutual-funds
term: "Liquid and overnight funds"
---

{% assign m = site.data.mf4 %}
{% assign lo = m.liquid_overnight %}
{% assign o = lo.funds.overnight %}
{% assign l = lo.funds.liquid %}
{% assign mm = lo.funds.money_market %}
{% assign g = lo.funds.gilt %}
{% assign reg = m.regulation %}
{% assign mc = reg.master_circular %}
{% assign src = m.sources.funds %}

## What these funds are

Overnight and liquid funds are debt funds that hold very short-dated paper, so that their NAV (net asset value, the price per unit) barely moves. Both are commonly described as places to hold cash for a short time.

The category table of SEBI (the Securities and Exchange Board of India) sets the limits. As of its [Master Circular for Mutual Funds]({{ mc.url }}) dated {{ mc.date | date: "%-d %B %Y" }} (number {{ mc.number }}), paragraph 3.8.2 says:

- An **overnight fund** invests in overnight securities having a maturity of 1 day. It may hold up to 5% of net assets in government securities (**G-secs**) or treasury bills (**T-bills**) with up to 30 calendar days left, as margin and collateral for certain transactions.
- A **liquid fund** invests only in debt and money market securities with a maturity of up to 91 calendar days.
- A **money market fund**, a step along, invests in money market instruments with a maturity of up to 1 year.
- A **gilt fund** invests at least 80% of its assets in G-secs across maturities.

The [debt funds post]({% post_url 2026-10-12-debt-funds-explained %}) explained why maturity matters: the longer the paper, the more its price moves when interest rates change, which is what [modified duration]({% post_url 2026-10-06-modified-duration %}) measures. This post is part of [Mutual Funds, Minus the Marketing]({{ '/series/mutual-funds/' | relative_url }}).

## The extra rules

Paragraphs 5.6.1 to 5.6.5 of the same circular add a risk framework for the two categories:

- A liquid fund must hold at least {{ reg.liquid_framework.liquid_assets_min_pct }}% of its net assets in **liquid assets**: cash, G-secs, T-bills and repo on G-secs (a short-term loan secured against government securities).
- Liquid and overnight funds may not park money pending deployment in short-term deposits of scheduled commercial banks, and may not invest in debt with structured obligations or credit enhancements (government-guaranteed debt is excluded from that bar).
- A liquid fund must charge an **exit load** on investors who leave within 7 calendar days. The circular leaves the graded minimum scale to AMFI (the Association of Mutual Funds in India), set in consultation with SEBI. The [exit load post]({% post_url 2026-10-07-exit-load %}) covers how an exit load works.

These are rules as of 20 March 2026. Later circulars can change them, so check the current text before relying on a detail.

## What the NAVs did

The four funds are {{ src.overnight.name }}, {{ src.liquid.name }}, {{ src.money_market.name }} and {{ src.gilt.name }}, all regular growth plans. NAVs come from [AMFI via mfapi.in](https://api.mfapi.in/mf/{{ src.liquid.code }}) and end on 31 March 2026, more than three months before this post. They are historical and shown only to illustrate how maturity changes behaviour. Nothing here ranks the funds, and each column is one fund from one fund house, not its category.

The window is the last five years. The overnight fund's face value changed in May 2018 and its NAV history before that doesn't behave like an overnight portfolio, which is why the post on [systematic transfer and withdrawal plans]({% post_url 2026-10-17-stp-and-swp %}) doesn't compare earlier years either.

**Return by financial year** (FY — the year to 31 March; NAV on the last day of each year):

| | Overnight | Liquid | Money market | Gilt |
|---|---:|---:|---:|---:|
{% for lab in lo.fy_labels -%}
| {{ lab }} | {{ o.fy_returns_pct[forloop.index0] }}% | {{ l.fy_returns_pct[forloop.index0] }}% | {{ mm.fy_returns_pct[forloop.index0] }}% | {{ g.fy_returns_pct[forloop.index0] }}% |
{% endfor -%}
| Five years, per year | {{ o.cagr_5y_pct }}% | {{ l.cagr_5y_pct }}% | {{ mm.cagr_5y_pct }}% | {{ g.cagr_5y_pct }}% |

**How bumpy the ride was**, same five years:

| | Overnight | Liquid | Money market | Gilt |
|---|---:|---:|---:|---:|
| Days the NAV fell | {{ o.down_days }} of {{ o.days }} | {{ l.down_days }} of {{ l.days }} | {{ mm.down_days }} of {{ mm.days }} | {{ g.down_days }} of {{ g.days }} |
| Share of days down | {{ o.down_days_share_pct }}% | {{ l.down_days_share_pct }}% | {{ mm.down_days_share_pct }}% | {{ g.down_days_share_pct }}% |
| Worst single day | +{{ o.worst_day_pct }}% | {{ l.worst_day_pct }}% | {{ mm.worst_day_pct }}% | {{ g.worst_day_pct }}% |
| Worst three months | +{{ o.worst_3m_pct }}% | +{{ l.worst_3m_pct }}% | +{{ mm.worst_3m_pct }}% | {{ g.worst_3m_pct }}% |
| Deepest fall from a peak | {{ o.max_drawdown.pct }}% | {{ l.max_drawdown.pct }}% | {{ mm.max_drawdown.pct }}% | {{ g.max_drawdown.pct }}% |

Two notes on reading the tables. The overnight and liquid funds' NAV series include weekend dates, while the other two are almost entirely business days, so the day counts differ; the share of days is the fair comparison. The FY returns mostly rise and fall together, which in our view reflects the same interest-rate cycle, so they are not a ranking of the funds.

What the second table shows is the effect of maturity. The overnight fund's NAV never fell in {{ o.days }} days; its worst day was a gain of {{ o.worst_day_pct }}%. The liquid fund fell on {{ l.down_days }} days, by at most {{ l.worst_day_pct | abs }}% in a day. The money market fund fell on {{ mm.down_days }} days, with a worst day of {{ mm.worst_day_pct | abs }}%, and took until {{ mm.max_drawdown.recovered_date | date: "%-d %B %Y" }} to recover from its {{ mm.max_drawdown.pct | abs }}% dip. The gilt fund fell on {{ g.down_days_share_pct }}% of days, and its worst three months, to {{ g.worst_3m_end | date: "%-d %B %Y" }}, lost {{ g.worst_3m_pct | abs }}%. That fund also took until {{ g.max_drawdown.recovered_date | date: "%-d %B %Y" }} to climb back from its {{ g.max_drawdown.pct | abs }}% fall.

Small is not zero. The rules limit what these funds can hold, but they don't fix the NAV.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Lending a friend ₹100 until tomorrow is very safe. You know exactly when you'll get it back and who owes you.

Lending ₹100 for a year is different. Lots can change. And if you needed the money back sooner, you might have to sell the loan at a discount.

An overnight fund is the "until tomorrow" loan. A liquid fund is the "up to three months" loan. A gilt fund is a loan of many different lengths. The longer the loan, the more its value wobbles.

</details>

## Common mistakes

- **Thinking a liquid fund is a bank balance.** It's a debt fund. The rules above limit its holdings, and the NAV above fell on {{ l.down_days }} days. It can fall, by a little.
- **Ignoring the exit load.** The circular requires one for exits within 7 calendar days of investing in a liquid fund. Check the scheme's own documents for the scale.
- **Comparing returns across the rungs without the rate cycle.** The FY returns above mostly move together, so a gap in one year isn't a lasting difference.
- **Assuming overnight, liquid and money market funds are interchangeable.** The first holds 1-day paper only, the second up to 91 days, the third up to a year. Longer paper moves more, as the money market row shows.

**Takeaway:** Overnight and liquid funds hold debt that matures in a day or within 91 days, so their NAV barely moves, and the rules limit what they can hold. Barely isn't never, and the longer the maturity, the larger the moves.
