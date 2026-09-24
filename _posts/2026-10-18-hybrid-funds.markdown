---
layout: post
title: "Hybrid funds: why \"balanced\" is a mix, not a promise"
description: "Aggressive hybrid, balanced advantage, equity savings: what SEBI's rules require of each, and how far real hybrid funds fell in 2008, 2020 and early 2026."
image: /assets/og/hybrid-funds.png
date: 2026-10-18 09:00:00 +0530
series: mutual-funds
term: "Hybrid funds"
---

{% assign m = site.data.mf3 %}
{% assign h = m.hybrid %}
{% assign r = m.reg %}
{% assign src = m.sources %}
{% assign w08 = h.windows[0] %}
{% assign w20 = h.windows[1] %}
{% assign w26 = h.windows[2] %}
{% assign c06 = h.common_windows[0] %}
{% assign c18 = h.common_windows[1] %}
{% assign c23 = h.common_windows[2] %}

## One fund, two asset classes

A **hybrid fund** holds more than one asset class — usually equity and debt,
sometimes gold or other assets too — inside a single scheme. The pitch is
convenience: one fund does the mixing and the rebalancing for you, so you don't
have to own an equity fund and a debt fund and keep the split right yourself.

That's a genuine service. The trouble starts with the names. "Balanced",
"conservative", "equity savings", "balanced advantage" all sound like
promises about how the fund will *feel* in a bad year. They aren't. Each one
is a category that SEBI (the Securities and Exchange Board of India, the
markets regulator) defines by an asset-allocation rule, and the rule is the
only promise. This post reads the rules, then checks how real hybrid funds
moved when markets fell.

The [SEBI categories post]({% post_url 2026-10-14-sebi-fund-categories-decoded %})
covered equity and debt categories and left hybrids for later. Here they are.

## The rules

SEBI's hybrid categories come from its October 2017 categorisation circular
({{ r.categorisation_2017 }}), revised by the circular of 26 February 2026 and
now set out in paragraph {{ r.hybrid_para }} of SEBI's
[Master Circular for Mutual Funds]({{ r.mc26.url }}) dated
{{ r.mc26.date | date: "%-d %B %Y" }}. "Equity" below means equity and
equity-related instruments, as a share of total assets.

| Category | The hard rule |
|---|---|{% for k in r.hybrid_rules %}
| **{{ k.category }}** | {{ k.rule }} |{% endfor %}

Three things in that table are worth slowing down for.

**Aggressive hybrid is mostly an equity fund.** Between 65% and 80% sits in
shares. The debt slice cushions a fall; it doesn't prevent one.

**Balanced advantage has no range at all.** "Managed dynamically" is the whole
rule. A balanced advantage fund (SEBI's table lists the category as "balanced
advantage fund / dynamic asset allocation fund") can be mostly equity one year and mostly debt the next,
depending on the fund house's model or judgement. Two funds in this category
can behave nothing alike.

**Equity savings and arbitrage funds count hedged shares as equity.** A fund
can own a share and simultaneously sell a futures contract on it, which
cancels out most of the price risk. That hedged position still counts toward
the 65% equity minimum. So an equity savings fund can be "65% equity" on
paper while only 15% to 40% of its assets are *net long* — actually exposed to
the market going up or down. (The 15–40% band is in the current text; the
fund history below was run under the earlier rules, which asked only that the
minimum hedged and unhedged shares be stated in the scheme document.) The
arbitrage funds post<!-- RELINK 2026-10-19-arbitrage-funds --> later in this
series shows how the hedge works.

## The formula: what a mix actually does

The arithmetic of a two-asset fund is simple, and it's the arithmetic the name
glosses over:

```
Fund return  ≈  wₑ × equity return  +  w_d × debt return  −  costs

where wₑ = share in (unhedged) equity, w_d = share in debt, wₑ + w_d ≈ 1
```

Set wₑ = 0.75 and the equity market falls 50%. Even if debt earns 8% in the
same year, the fund loses roughly 0.75 × 50% − 0.25 × 8% = 35.5%. The debt
slice turned a 50% loss into a 35.5% one. That's real protection — and it's
still a loss of more than a third.

The formula is an approximation. The fund rebalances, the equity it holds
isn't the index, the debt isn't a single bond, and in a crash bonds don't
always rise. But it tells you what order of loss to expect, which is the thing
the word "balanced" hides.

## Worked example: four hybrid funds and an index fund, in three bad stretches

Four UTI hybrid funds, one from each of four categories — aggressive hybrid,
balanced advantage, equity savings and arbitrage — plus the Nifty 50 index
fund used throughout this series. Regular plans, growth option; source
{{ src.label }} (AMFI is the Association of Mutual Funds in India), data to {{ src.end | date: "%-d %B %Y" }}. They're all from
one fund house so that the only thing changing is the category. Historical
data, for illustration only. **This post takes no view on any of these funds**,
and nothing here compares their managers — the point is what each
*category's* rule allowed to happen.

Returns over fixed calendar windows, each measured from the last NAV (net
asset value, the per-unit value of the fund) of the previous period:

| Window | Aggressive hybrid | Balanced advantage | Equity savings | Arbitrage | Nifty 50 index fund |
|---|---:|---:|---:|---:|---:|{% for x in h.windows %}
| {{ x.label }} | {% if x.aggressive_hybrid %}{{ x.aggressive_hybrid }}%{% else %}—{% endif %} | {% if x.balanced_advantage %}{{ x.balanced_advantage }}%{% else %}—{% endif %} | {% if x.equity_savings %}{{ x.equity_savings }}%{% else %}—{% endif %} | {{ x.arbitrage }}% | {{ x.index_fund }}% |{% endfor %}

A dash means the fund has no NAV history for that window (the equity savings
fund's AMFI history starts in August 2018, the balanced advantage fund's in
August 2023).

Reading it row by row:

1. **2008.** The aggressive hybrid fund lost {{ w08.aggressive_hybrid | abs }}% in the
   calendar year, against {{ w08.index_fund | abs }}% for the index fund. Measured peak to
   trough, it fell {{ h.aggressive_2008_drawdown.pct | abs }}% between
   {{ h.aggressive_2008_drawdown.peak_date | date: "%B %Y" }} and
   {{ h.aggressive_2008_drawdown.trough_date | date: "%B %Y" }} — about
   {{ h.aggr_to_index_2008_ratio | times: 100 | round }}% of the index fund's
   {{ h.index_2008_drawdown.pct | abs }}% fall. The cushion was real and it
   was small: a hybrid fund investor lost close to half their money.
2. **Early 2020.** Same shape. The aggressive hybrid fund lost {{ w20.aggressive_hybrid | abs }}% in the
   quarter, the index fund {{ w20.index_fund | abs }}%. The equity savings fund, with far less
   net equity, lost {{ w20.equity_savings | abs }}% — much less, but a double-digit
   loss in three months from a fund whose name contains "savings".
3. **Early 2026.** The balanced advantage fund — the category marketed on
   its ability to shift out of equity — fell {{ w26.balanced_advantage | abs }}%, about as much as the
   aggressive hybrid fund's {{ w26.aggressive_hybrid | abs }}%. "Dynamic" describes what the
   fund *may* do. Whether it has cut equity before a particular fall is a
   different question, and the category rule doesn't answer it.
4. **The arbitrage fund rose in every window.** It isn't really a mixed fund
   at all, in the sense that matters: its equity is hedged. The arbitrage
   funds post<!-- RELINK 2026-10-19-arbitrage-funds --> takes it apart.

And the full common-window picture — each fund's worst peak-to-trough fall
([drawdown]({% post_url 2026-09-29-drawdown %})) and annualised
[volatility]({% post_url 2026-09-30-volatility-and-sharpe %}), measured only
over the stretch where every fund in the row has data:

| Window | Measure | Aggressive hybrid | Balanced advantage | Equity savings | Arbitrage | Index fund |
|---|---|---:|---:|---:|---:|---:|{% for c in h.common_windows %}
| {{ c.label }} | Worst fall | {{ c.aggressive_hybrid.max_drawdown_pct }}% | {% if c.balanced_advantage %}{{ c.balanced_advantage.max_drawdown_pct }}%{% else %}—{% endif %} | {% if c.equity_savings %}{{ c.equity_savings.max_drawdown_pct }}%{% else %}—{% endif %} | {% if c.arbitrage %}{{ c.arbitrage.max_drawdown_pct }}%{% else %}—{% endif %} | {{ c.index_fund.max_drawdown_pct }}% |
| | Volatility | {{ c.aggressive_hybrid.volatility_pct }}% | {% if c.balanced_advantage %}{{ c.balanced_advantage.volatility_pct }}%{% else %}—{% endif %} | {% if c.equity_savings %}{{ c.equity_savings.volatility_pct }}%{% else %}—{% endif %} | {% if c.arbitrage %}{{ c.arbitrage.volatility_pct }}%{% else %}—{% endif %} | {{ c.index_fund.volatility_pct }}% |{% endfor %}

The ordering is the one the rules predict: the more net equity a category
allows, the deeper its falls. The hybrid label moved each fund along that
line. It didn't take any of them off it — except the one whose equity was
fully hedged.

One caveat on the longest row. SEBI's categories were implemented during 2018, and the
aggressive hybrid scheme's 2006–2018 history was run under the older, looser
rules that applied before categorisation (the scheme has also changed its name
since). Its 2008 figures show what a mostly-equity balanced fund of that era
did, not a fund bound by today's 65–80% band.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Imagine a lunchbox with rice and ice cream in it. On a hot day the ice cream
melts — that's the stock market falling.

An "aggressive hybrid" lunchbox is three-quarters ice cream. The rice is still
fine, so you don't lose your whole lunch — but you lose most of it.

An "equity savings" lunchbox has lots of ice cream too, but most of it is
packed in a cold box (that's the hedge), so only a little melts.

A "balanced advantage" lunchbox has a helper who is *allowed* to swap ice
cream for rice when it looks hot. Some days the helper swaps in time. Some
days not. The name on the box tells you there's a helper. It doesn't tell you
whether the helper got it right today.

</details>

## Common mistakes

- **Reading "balanced" or "hybrid" as "low risk".** An aggressive hybrid fund
  is 65–80% equity by rule. In 2008 the one above fell
  {{ h.aggressive_2008_drawdown.pct | abs }}% peak to trough. Check the category's
  equity band, not the adjective.
- **Assuming a balanced advantage fund will de-risk before a fall.** The rule
  permits it; it doesn't require it, and in our view no model reliably spots
  falls in advance. In early 2026 the one above fell as much as the aggressive hybrid
  fund. Look at how its equity share has actually moved month to month in
  the factsheets.
- **Comparing hybrid funds across categories.** An equity savings fund
  "losing" to an aggressive hybrid fund over a bull run tells you about net
  equity, not about the managers. Compare within a category, over the same
  window — the [benchmarks post]({% post_url 2026-10-02-benchmarks-and-comparing-like-with-like %})
  applies here too.
- **Double-counting diversification.** If you already hold equity funds and
  debt funds, adding a hybrid fund doesn't add a new asset class — it adds
  more of the two you have, at a blended split you now have to track across
  several funds.

The tax treatment of a hybrid fund depends on how much of it is in domestic
listed shares, which is why two hybrid funds can be taxed completely
differently. The tax series covers that<!-- RELINK 2026-10-29-equity-and-equity-funds -->;
check the fund's classification before assuming.

**Takeaway:** A hybrid fund's name describes a mix, and the only promise is
the asset-allocation rule behind it — 65–80% equity for aggressive hybrid,
anything at all for balanced advantage. On real data the debt slice softened
falls without preventing them, so read a hybrid fund's equity band before
reading its name.
