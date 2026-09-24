---
layout: post
title: "Manager changes and style drift: when the fund you bought quietly changes"
description: "A fund can change manager or drift in style without changing its name or category. How to spot it in factsheets, worked on a hypothetical flexi-cap fund."
image: /assets/og/manager-changes-and-style-drift.png
date: 2026-10-23 09:00:00 +0530
series: mutual-funds
term: "Style drift"
---

{% assign m = site.data.mf3 %}
{% assign d = m.drift %}
{% assign f = m.reg.fundamental %}
{% assign r = m.reg %}
{% assign s0 = d.snapshots[0] %}
{% assign s1 = d.snapshots[1] %}
{% assign s2 = d.snapshots[2] %}
{% assign s3 = d.snapshots[3] %}
{% assign sh1 = d.shifts[1] %}

## Same name, different fund

You chose a fund for what it was: a mostly large-cap portfolio, say, with a
steady hand and low turnover. Two years later it has the same name, the same
category and the same benchmark. It may not be the same fund.

**Style drift** is a gradual change in *how* a fund invests — which part of
the market it fishes in, how concentrated it is, how often it trades — without
any change to its label. It often follows a **fund manager change**, though it
doesn't have to. Neither shows up in the returns table until after it has
already changed what you own.

The rules don't stop either. The list kept by SEBI (the Securities and
Exchange Board of India) of of a scheme's **fundamental
attributes** — the things a fund house can't change without writing to every
unitholder and offering a {{ f.exit_days }}-day exit at NAV (net asset value) with no exit load — covers
the type of scheme, the investment objective and asset-allocation ranges,
and the terms of issue: liquidity, fees and any safety net (paragraph
{{ f.mc_para }} of SEBI's [Master Circular for Mutual Funds]({{ r.mc26.url }}),
under {{ f.reg }} of the 2026 Regulations, which replaced
{{ f.old_reg }} of the 1996 ones). **The fund manager isn't on that list**, and
neither is anything a manager does *within* the category's rules. So a manager
change is typically announced by an addendum to the scheme documents, and
drift isn't announced at all. You find both by reading the factsheet.

## The formula: measuring drift

The simplest drift measure uses the market-cap split every equity factsheet
prints — large, mid, small, cash — and asks how much of the portfolio has
moved between bands:

```
Band shift = ½ × ( |Δ large| + |Δ mid| + |Δ small| + |Δ cash| )

  where Δ = weight now − weight then, in percentage points
```

Halving is because every point that leaves one band lands in another; without
it you'd count each move twice. A band shift of 0 means the same mix; 100
would mean a completely different one. It's the band-level cousin of the
[portfolio overlap]({% post_url 2026-10-15-portfolio-overlap %}) calculation,
and it's coarse on purpose — you can do it from four numbers on a factsheet.

Alongside it, three other factsheet lines move when style drifts: the **top-10
weight** (concentration), the **number of stocks**, and **portfolio turnover**
(how much of the portfolio was traded over the past year).

## Worked example: a hypothetical flexi-cap fund

The factsheets below are **invented** for a hypothetical "Example Flexi Cap
Fund". No real fund's data is used, and no real manager is being assessed —
drift is something you check for, not a verdict on anyone.

| Factsheet | Manager | Large cap | Mid cap | Small cap | Cash | Top-10 weight | Stocks | Turnover |
|---|---|---:|---:|---:|---:|---:|---:|---:|{% for x in d.snapshots %}
| {{ x.as_of }} | {{ x.manager }} | {{ x.large }}% | {{ x.mid }}% | {{ x.small }}% | {{ x.cash }}% | {{ x.top10 }}% | {{ x.stocks }} | {{ x.turnover }}% |{% endfor %}

Band shift between consecutive factsheets (pp = percentage points):

| From | To | Band shift | Change in small cap | Change in large cap |
|---|---|---:|---:|---:|{% for x in d.shifts %}
| {{ x.from }} | {{ x.to }} | {{ x.band_shift_pp }} pp | {% include inr.html n=x.small_change_pp %} pp | {% include inr.html n=x.large_change_pp %} pp |{% endfor %}

Reading it:

1. **Under the old manager, nothing moved.** A band shift of
   {{ d.shifts[0].band_shift_pp }} percentage points in six months is ordinary
   drift from prices moving, not from decisions.
2. **After the change, the fund moved in steps.** The band shift was
   {{ sh1.band_shift_pp }} points in the first six months and
   {{ d.shifts[2].band_shift_pp }} in the next. Between the {{ s0.as_of }} and {{ s3.as_of }} factsheets,
   a net {{ d.total_band_shift_pp }}% of the portfolio changed bands.
3. **The small-cap share went from {{ s0.small }}% to {{ s3.small }}%** — about
   {{ d.small_multiple }} times — while large caps fell from {{ s0.large }}% to {{ s3.large }}%.
4. **Everything else agrees.** Turnover rose from {{ s0.turnover }}% to {{ s3.turnover }}%, the number
   of stocks from {{ s0.stocks }} to {{ s3.stocks }}, and the top-10 weight fell from {{ s0.top10 }}% to {{ s3.top10 }}%.
5. **All of it was within the rules.** Flexi cap requires at least 65% in
   equity and sets no minimum in any market-cap band (see the
   [categories post]({% post_url 2026-10-14-sebi-fund-categories-decoded %})).
   Every one of these factsheets is compliant. The label never changed.

What changed is the fund's *risk*. A portfolio with a quarter in small caps
tends to fall further in a sell-off than one with {{ s0.small }}% there — the
[drawdown]({% post_url 2026-09-29-drawdown %}) you signed up for is no longer
the drawdown you have. Whether the new approach is better or worse is a
separate question this post doesn't answer; the point is that it's
*different*, and the investor who chose the {{ s0.as_of }} fund now owns the
{{ s3.as_of }} one.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

You join a cricket academy because the coach teaches patient batting —
leave the bad balls, build an innings.

The coach leaves. The academy keeps its name, its ground and its uniforms.
The new coach teaches everyone to hit sixes from ball one.

Nothing on the gate has changed. But if you'd wanted to learn patient
batting, you're now at a different academy. The only way to know is to go
and watch a practice session — for a fund, that's reading the factsheet.

</details>

## How to check a real fund

1. **Pull two factsheets a year apart** — or either side of a manager change.
   Fund houses usually keep an archive on their websites.
2. **Compute the band shift** from the market-cap split. A few points is
   noise; double digits within a year deserves a closer look.
3. **Compare top-10 weight, number of stocks and turnover.** Drift usually
   moves all three.
4. **Check the manager field and its "managing since" date.** If the track
   record you liked is older than the current manager's tenure, it isn't
   theirs — the [factsheet post]({% post_url 2026-10-11-reading-a-factsheet %})
   made the same point.
5. **Look at sector weights too.** A fund can hold its market-cap mix steady
   while swinging between sectors, which the band shift won't catch.

## Common mistakes

- **Waiting for the returns to tell you.** Returns reveal a change in style
  only after it has either worked or hurt you. The factsheet reveals it
  within months.
- **Assuming the category protects you.** It limits drift only where the rule
  bites. A mid-cap fund can't go below 65% in mid caps; a flexi-cap fund can
  go almost anywhere. Know how much room your fund's category leaves.
- **Treating every manager change as a reason to sell.** Some fund houses run
  a process meant to outlast any one manager. A manager change is a reason
  to *check* — two factsheets, four numbers — not a signal in itself.
- **Judging drift by a single month.** Market moves shift band weights
  without any trading. Look for a sustained move alongside higher turnover.

**Takeaway:** A fund can change manager and drift in style without changing
its name, category or benchmark, and neither needs your consent. Compare two
factsheets a year apart — the market-cap split, top-10 weight, number of
stocks and turnover — and you'll see a changed fund months before its returns
would tell you.
