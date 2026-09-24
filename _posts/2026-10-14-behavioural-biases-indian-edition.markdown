---
layout: post
title: "Behavioural biases, Indian edition: five ways you'll fight your own portfolio"
description: "Loss aversion, recency, anchoring, the disposition effect and herding — each tied to a number already on this blog, so you can spot the bias before it bites."
image: /assets/og/behavioural-biases-indian-edition.png
date: 2026-10-14 09:00:00 +0530
series: risk
---

{% assign rk = site.data.risk %}
{% assign b = rk.behaviour %}
{% assign mf = site.data.mf %}
{% assign dd = mf.drawdowns %}
{% assign uw = mf.sip.underwater %}
{% assign rr = mf.rolling_returns %}
{% assign f = site.data.fno %}
{% assign u = f.fy26_unverified %}

## The variable no formula includes

So far in this series, every risk has been about the market or
the instrument — leverage, correlation, sequence, the arithmetic of losses.
This one is about the other party to every transaction you'll ever make:
you.

**Behavioural finance** is the study of the systematic ways people depart
from the cool calculation the formulas assume. "Systematic" is the important
word. These aren't random errors that average out. They're predictable
biases that push most people in the same wrong direction at the same moment
— which is exactly why they're expensive.

Five of them, each attached to a number from earlier in this blog. The point
of the numbers is recognition: it's much easier to catch a bias when you can
name the situation it lives in.

## 1. Loss aversion

**What it is.** Losses hurt roughly twice as much as equivalent gains feel
good — the finding behind Kahneman and Tversky's prospect theory (1979);
their 1992 follow-up put the ratio at about 2.25. A ₹10,000 loss and a
₹10,000 gain are not emotional opposites; the loss is heavier.

**Where it lives.** In the underwater chart. Over twenty years and
{% include inr.html n=b.days %} trading days, {{ rk.dataset.fund_name }} spent only **{% include inr.html n=b.pct_days_at_high %}% of trading days**
at or near an all-time high. It sat more than 10% below a previous peak on
**{{ b.pct_days_below_10 }}%** of days, and more than 20% below on
{{ b.pct_days_below_20 }}%. The median day was {{ b.median_drawdown_pct | abs }}%
below the high.

Read that again: a good, boring, diversified index fund spends most of its
life *below* a number it once reached. Owning it means looking at a shortfall
against the peak far more often than not. If each of those glances weighs
twice what the gains do, holding through twenty years is emotionally
punishing even when it's financially fine — and the
[drawdown post]({% post_url 2026-09-29-drawdown %}) showed that "financially
fine" included a six-year wait after 2008.

**The tell.** Checking the portfolio more often when it's falling. Loss
aversion makes each check hurt; frequent checking makes the hurt frequent.

## 2. Recency

**What it is.** Weighting what just happened far more than what usually
happens. The last year feels like the truth about the asset; the last twenty
feel like history.

**Where it lives.** In the
[rolling returns]({% post_url 2026-09-27-rolling-returns %}). Three-year
returns on the same fund ranged from {{ rr.years_3.min | replace: "-", "−" }}% to
{{ rr.years_3.max }}% a year depending on start date; the median barely moved
around {{ rr.years_3.median }}%. Someone who started in March 2020 saw three
years near the top of that range and quite reasonably concluded equities
return 30% a year. Someone who started in 2017 saw the bottom of it and
concluded the opposite. Both were extrapolating three years into a forecast.
Both were wrong in the same way.

The most expensive version is the money that arrives *after* a great run and
leaves after a bad one — retail flows into equity funds have tended to be
strongest after strong markets and weakest after falls. Recency converts the market's past into the investor's future at
exactly the wrong moments.

**The tell.** "This time it's different" and "it's been going up for years"
are both recency. So is judging a fund on its one-year return.

## 3. Anchoring to your buy price

**What it is.** Treating the price you paid as the reference point for every
future decision, when the market has no idea what you paid.

**Where it lives.** In the phrase "I'll sell when it gets back to my price."
The [arithmetic of losses]({% post_url 2026-10-09-the-arithmetic-of-losses %})
showed why the anchor is so sticky: a stock down 40% needs +67% to reach it.
Waiting for that isn't a strategy, it's a hope with a number attached — and
while you wait, the question you *should* be asking ("would I buy this today
at this price?") goes unasked.

The anchor also works in reverse. A stock that has doubled feels "expensive"
relative to your cost, so it gets sold, even if nothing about the business
says so. Your purchase price is a fact about your history. It is not
information about the asset.

**The tell.** Any sentence that includes "my price," "back to even," or
"I'm up X% so I'll book it."

## 4. The disposition effect

**What it is.** Selling winners too early and holding losers too long. It's
loss aversion and anchoring combined: booking a gain feels good and makes the
gain "real," while selling a loser makes the loss "real," so people do the
first and avoid the second.

**Where it lives.** In the F&O data. The
[F&O post]({% post_url 2026-10-08-what-the-fo-numbers-actually-say %}) noted
that among individual traders who lost money two years running, about
{{ u.repeat_loser_pct }}% lost again the following year. On its own that
can't separate skill from luck, and much of it is structural — costs,
counterparties, leverage. But SEBI's
[behaviour study]({{ f.sources.fy25_fy26_behaviour_study.url }}) (August 2026)
adds a telling detail: among traders who had both profitable and losing
quarters, about {{ u.traders_avg_loss_exceeds_avg_gain_pct }}% lost more in an
average losing quarter than they made in an average winning one. That
pattern — small wins, large losses — is consistent with the disposition
effect: wins taken quickly, losses held in the hope of recovery. You can be
right more often than wrong and still lose.

For long-term investors the cost is quieter but real: a portfolio pruned of
its winners and stocked with its losers, by design.

**The tell.** Your realised gains are many and small; your unrealised losses
are few and large.

## 5. Herding

**What it is.** Doing what everyone else is doing because everyone else is
doing it. Evolutionarily sensible — the herd is usually right about where the
water is. Financially expensive — the herd is, by construction, the crowd
that has already bought.

**Where it lives.** In participation numbers. The F&O studies describe the
number of individual traders in the derivatives segment rising sharply
through a bull market and falling sharply after — new entrants arriving when
the activity was most visible, most discussed and most recently profitable,
and leaving after the losses. (The FY26 fall also followed SEBI's
derivatives curbs, phased in from November 2024 — larger minimum contract
sizes, weekly expiries limited to one index per exchange — so not all of it
is the herd changing its mind; SEBI's own study says it can't establish
cause.) The same pattern shows up in every IPO boom,
every small-cap rally, every "everyone's buying" moment.

Herding is also what makes correlations rise in a crash — the
[last post but one]({% post_url 2026-10-12-diversification-is-a-correlation-problem %})
noted that risky assets fall together precisely when you need them not to.
That's not a property of the assets. It's everyone selling at once.

**The tell.** You can't remember your own reason for the position, but you
can remember who else has it.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Imagine you and your friends trading cricket cards.

- You *hate* losing a card twice as much as you like getting one, so you
  hold onto bad cards forever. That's loss aversion.
- Whichever player scored a century last week, everyone wants his card this
  week. That's recency.
- You won't trade a card for less than you paid, even though nobody else
  cares what you paid. That's anchoring.
- You trade away your best cards quickly for a small gain and keep the duds
  hoping they'll come good. That's the disposition effect.
- When the whole class suddenly wants one player's card, you want it too —
  and pay the most for it. That's herding.

None of these makes you a bad trader. They make you a normal person. The
trick is knowing which one you're doing.

</details>

## The other side: what the data says about staying put

Being fair to human nature, the same dataset has a counterweight. The
[SIP post]({% post_url 2026-10-01-sips-xirr-and-timing-myths %}) found that a
₹10,000 monthly SIP over twenty years — straight through 2008 — was worth
less than the amount invested in only **{{ uw.months_below_invested }} of
{{ uw.months_total }} months**, and never for longer than
{{ uw.longest_stretch_months }} months at a stretch. And of the fund's
{{ b.up_fys | plus: b.down_fys }} financial years, {{ b.up_fys }} were up and
{{ b.down_fys }} were down; the worst ({{ b.worst_fy }}, {{ b.worst_fy_pct | replace: "-", "−" }}%)
was followed immediately by +{{ b.next_fy_pct }}%.

So the biases above don't need to be *defeated*. They need to be made
irrelevant to the decision — which is what a fixed monthly amount, a written
asset allocation, and a rule for when you'll look do. Not because rules are
smarter than you, but because they were written by the version of you that
wasn't looking at a red number.

## Common mistakes

- **Believing you're the exception.** Everybody does. That belief is itself
  a documented bias (overconfidence), and it's what keeps the other five in
  business.
- **Trying to out-think the biases in the moment.** They work *because* they
  feel like clear thinking at the time. The defence is a rule made in
  advance, not willpower made on the day.
- **Confusing activity with control.** Checking, trading and rebalancing more
  often *feels* like managing risk. Mostly it gives loss aversion and
  recency more opportunities.
- **Learning the wrong lesson from a good outcome.** A trade that worked
  through luck teaches the same bias as one that worked through skill, and
  the market doesn't label which was which.
- **Reading this post and changing nothing.** Research on "debiasing" (the
  classic review is Fischhoff, 1982) found that simply warning people about
  a bias does little to reduce it. Changing the process — the
  automation, the rules, the checking frequency — is what moves the outcome.

**Takeaway:** Loss aversion, recency, anchoring, the disposition effect and
herding each have a number on this blog, and each number marks a moment
you'll recognise. A diversified index fund spent {{ b.pct_days_below_10 }}% of
twenty years more than 10% below its previous high, which is when the biases
bite. You don't beat them in the moment; you write the rule before it.
