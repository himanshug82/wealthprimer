---
layout: post
title: "Leverage and margin: how a 10% move becomes 100%"
description: "Margin trading and futures margin do one thing to your returns: multiply them, both ways. Worked with round numbers, including the interest bill nobody counts."
image: /assets/og/leverage-and-margin.png
date: 2026-11-08 09:00:00 +0530
series: risk
term: "Leverage"
---

{% assign rk = site.data.risk %}
{% assign lv = rk.leverage %}
{% assign m = lv.mtf %}

## Borrowed money, multiplied outcomes

**Leverage** is using borrowed money to hold a larger position than your own
capital would allow. In Indian retail investing it arrives in two common
forms: a broker's **MTF — Margin Trading Facility**, where you pay part of a
stock purchase and the broker lends the rest against the shares; and
**futures**, where a small margin deposit controls a much larger notional
contract — the mechanism the
[F&O post]({% post_url 2026-11-05-what-the-fo-numbers-actually-say %}) touched
on.

Both do exactly one thing to your returns: multiply them. In both directions.
That symmetry is the whole subject, and the reason this post is mostly
tables.

Every number here is a round illustration, not a real quote. Actual margin
requirements, interest rates and contract sizes change; the arithmetic
doesn't.

## The formula

```
Leverage (x)  =  Position value  /  Your own capital

Return on your capital  =  Leverage × Price move  −  Cost of borrowing

Move that wipes out your capital  =  −(1 / Leverage)     (before costs)
```

The last line is the one to memorise. At 2× leverage, a 50% fall takes
everything. At 5×, 20%. At 10×, a 10% fall — one bad week for a single
stock — leaves you with nothing. Losses beyond that point are still owed.

## Table one: the multiplier

Return on your own capital for a given price move, before any interest or
fees:

| Price move | Unlevered (1×) | 2× | 5× | 10× |
|---:|---:|---:|---:|---:|{% for row in lv.table %}
| {{ row.move_pct }}% | {{ row.x1 }}% | {{ row.x2 }}% | {{ row.x5 }}% | **{{ row.x10 }}%** |{% endfor %}

Read down the 10× column. Nothing exotic happens to the price — a 10% move
is well inside the normal range for a stock over a few weeks, and the
[position sizing post]({% post_url 2026-11-07-position-sizing-and-the-one-percent-rule %})
showed Britannia alone moving 2–3% on an ordinary day. What's exotic is what
the multiplier does to it.

The −100% entries are capped in the table. In practice a broker doesn't wait
for that: when the position's value falls toward the borrowed amount, you get
a **margin call** — top up cash, or the broker sells the position to protect
the loan. That sale happens at the worst possible moment by construction:
after a fall, at the low, with no say in the timing.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

You have ₹100 and want to buy a toy that costs ₹1,000, so a friend lends you
₹900. Tomorrow you sell the toy.

If it sells for ₹1,100, you pay back ₹900 and keep ₹200 — you doubled your
money on a 10% price rise. Brilliant.

If it sells for ₹900, you pay back ₹900 and keep nothing. Your ₹100 is gone on
a 10% price fall. And if it sells for ₹850, you *still owe* ₹50.

The toy moved 10% either way. Your money moved 100%. That's leverage.

</details>

## Table two: the interest bill

Borrowed money isn't free, and the cost is the part that turns a symmetric
multiplier into a tilted one. Take an MTF position: ₹{% include inr.html n=m.own %}
of your own money, ₹{% include inr.html n=m.borrowed %} borrowed at an
illustrative {{ m.rate_pct }}% a year, held for {{ m.months }} months.

| | |
|---|---:|
| Position | ₹{% include inr.html n=m.position %} |
| Leverage | 2× |
| Interest for {{ m.months }} months | ₹{% include inr.html n=m.interest %} |
| Price rise needed just to break even | **{{ m.breakeven_move_pct }}%** |

Now run the scenarios:

| Price move over {{ m.months }} months | Unlevered return | P&L on the MTF position | Return on your ₹{% include inr.html n=m.own %} |
|---:|---:|---:|---:|{% for s in m.scenarios %}
| {{ s.move_pct }}% | {{ s.unlevered_return_pct }}% | {% if s.pnl < 0 %}{% assign pnl_abs = s.pnl | abs %}−₹{% include inr.html n=pnl_abs %}{% else %}₹{% include inr.html n=s.pnl %}{% endif %} | **{{ s.return_on_own_pct }}%** |{% endfor %}

Three things in that table are worth sitting with.

**A flat market loses you {{ m.scenarios[2].return_on_own_pct | abs }}%.** The stock does
nothing, and you're down the interest.

**A 5% rise earns you *less* than owning the stock outright.** {{ m.scenarios[1].return_on_own_pct }}%
levered against {{ m.scenarios[1].unlevered_return_pct }}% unlevered — the multiplier
doubled the gain and the interest ate more than the doubling added. Leverage
only helps if the move is bigger than the borrowing cost, in the time you
have.

**The losses aren't doubled — they're doubled *and then* the interest is
added.** A 10% fall costs {{ m.scenarios[4].return_on_own_pct }}% of your capital,
not 20%. At this rate and holding period, a fall of about
{{ m.wipeout_move_pct | abs }}% would take the entire ₹{% include inr.html n=m.own %}.

## Futures: the same thing with a smaller deposit

A futures contract on an index or a stock typically asks for a margin of
somewhere around {{ lv.futures_margin_pct }}% of the contract's value — the
figure varies by contract and by day, set by the exchange from the underlying's
volatility. That's roughly {{ 100 | divided_by: lv.futures_margin_pct | round: 1 }}× leverage
on the margin you put down.

Which means the wipeout line from the formula sits at about
−{{ lv.futures_wipeout_move_pct }}%. The F&O post's worked example showed the
upside version — a 1% index move returning 8.3% on margin. This is its
mirror: the same contract, the index falls {{ lv.futures_wipeout_move_pct }}% over
a few weeks, and the margin is gone. Not "down a lot." Gone, with a demand
for more (a **mark-to-market** call, settled daily) along the way.

There's no interest bill on a future in the MTF sense, but there is an
equivalent: the futures price normally sits above the spot price by roughly
the cost of carry, and that premium decays toward zero at expiry. You pay for
the leverage either way; it's just less visible.

## What leverage is actually for

Being fair: leverage isn't a scam. Companies use it (the entire
[debt-to-equity]({% post_url 2026-09-15-debt-to-equity %}) discussion is about
leverage at the corporate level), home buyers use it, and hedgers use futures
to *reduce* risk by offsetting a position they already hold. The problem
isn't the tool. It's that the tool's cost is quiet and its downside is loud,
and most people who reach for it are looking at the left half of table one.

The [arithmetic of losses]({% post_url 2026-11-06-the-arithmetic-of-losses %})
is what makes it so unforgiving. A leveraged account that drops 50% needs
100% to recover — on an account that now has less margin capacity, paying the
same interest. Leverage makes every drawdown deeper *and* every recovery
steeper, at the same time.

## Common mistakes

- **Thinking of leverage as "a bigger position."** It's a bigger position
  *and* a loan. The loan has a cost and a lender who can call it.
- **Ignoring the interest because it's quoted per year.** {{ m.rate_pct }}% a year
  on a position held six months is {{ m.breakeven_move_pct }}% of the position
  you have to earn before you've made anything.
- **Comparing the levered return to zero instead of to the unlevered one.**
  The honest question is whether borrowing beat simply owning. In the 5%
  scenario above it didn't.
- **Assuming you'll get out before the margin call.** The call is triggered
  by the price, not by your plan, and it forces a sale at the low.
- **Sizing the position by the margin instead of by the notional.** A
  ₹2 lakh margin controlling a ₹18 lakh contract is an ₹18 lakh risk. The
  1% rule from the last post applies to the notional exposure, which usually
  means the position you can "afford" on margin is far larger than the one
  you can afford to lose on.
- **Adding leverage to recover a loss.** This is the recovery table's worst
  case: the hole is deeper, the multiplier is larger, and the wipeout line is
  closer.

**Takeaway:** Leverage multiplies both directions by the same number and then
charges you for the privilege — at 2× a flat market costs you the interest, a
5% rise can earn less than owning outright, and at 10× an ordinary 10% fall
is the whole account. The wipeout move is just 1 ÷ leverage. Work that number
out before the position, not after the margin call.
