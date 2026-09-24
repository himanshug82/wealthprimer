---
layout: post
title: "Insurance as risk transfer: why term cover isn't an investment"
description: "Some risks you can't afford to carry. How term life cover transfers them, a needs-based sum, and how to find the savings return inside a bundled plan."
image: /assets/og/insurance-as-risk-transfer.png
date: 2026-10-23 09:00:00 +0530
series: risk
term: "Risk transfer (insurance)"
---

{% assign r2 = site.data.risk2 %}
{% assign nd = r2.insurance.need %}
{% assign bd = r2.insurance.bundle %}

## The risks you can't diversify away

Everything else in this series has been about risks you can shape: size a
position, spread it across things that don't move together, avoid leverage,
keep your broker honest. Some risks don't bend to any of that. If a
household's main earner dies, the income stops — all of it, at once — and no
asset allocation fixes that.

There are four things you can do with a risk: **avoid** it, **reduce** it,
**retain** it (carry it yourself), or **transfer** it to someone else for a
price. Insurance is the last one. You pay a small, certain amount — the
premium — so that a large, uncertain loss lands on an insurer instead of on
you. The insurer can carry it because it pools thousands of similar risks,
most of which never claim.

**Term life insurance** is the plainest form: you pay premiums for a fixed
term; if you die during it, the insurer pays the sum assured; if you don't,
it pays nothing. No maturity value, no return. That's not a flaw. It's what
makes it pure risk transfer.

This post is about mechanics. It doesn't recommend any product, insurer or
amount of cover, and every number in it is a clearly labelled illustration.

## The formula

```
Expected claim cost for one year  =  probability of death × sum assured
Premium  ≈  expected claim cost  +  the insurer's expenses, capital cost and margin

Needs-based cover (one common way to size it):
    Cover  =  PV (present value) of the household's future expenses
            +  outstanding loans
            +  future goals (education, a wedding)
            −  existing investments that could meet them

PV of a fixed yearly amount E for n years at rate r:
    PV  =  E × [1 − (1 + r)^(−n)] / r

The savings return inside a bundled (insurance + savings) plan:
    the IRR (internal rate of return) that makes the premiums you pay grow into the maturity value
```

The needs-based formula is [discounting]({% post_url 2026-09-27-discounting-time-value-of-money %})
turned around: instead of asking what future cash flows are worth today, it
asks what lump sum today would replace them. Using a *real* rate (after
inflation) keeps the expenses in today's rupees; the
[real returns post]({% post_url 2026-10-20-inflation-and-real-returns %})
shows why the difference matters.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

A thousand kids each put ₹20 in a jar at the start of the year. If any kid's
bicycle gets stolen, the jar buys them a new one.

Most years, only a few bikes get stolen, so most kids "lose" their ₹20 — but
nobody has to face buying a whole new bicycle alone. You're not paying ₹20 to
make money. You're paying ₹20 so that one bad day doesn't wreck your year.

Now imagine a jar that promised to give everyone *back* more than their ₹20
at the end, *and* buy stolen bikes. It would have to charge a lot more than
₹20. That's the difference between plain insurance and a plan that bundles
savings in.

</details>

## Worked example: a hypothetical household

Everything here is invented to show the method. Real needs depend on the
household, and a real premium depends on age, health, term and the insurer.

**Step 1: how much cover?**

| Component | Assumption (hypothetical) | Amount (₹) |
|---|---|---:|
| Household expenses to replace | ₹{% include inr.html n=nd.annual_expenses %} a year for {{ nd.years }} years, at a {{ nd.real_rate_pct }}% real rate | {% include inr.html n=nd.pv_expenses %} |
| Outstanding loans | Home loan balance | {% include inr.html n=nd.loans %} |
| Future goals | Children's education, in today's rupees | {% include inr.html n=nd.goals %} |
| Less: existing investments | Savings that could be used | −{% include inr.html n=nd.existing_assets %} |
| **Cover needed** | | **{% include inr.html n=nd.cover %}** |

Rounded up to the next ₹25 lakh: **₹{{ nd.cover_rounded_crore }} crore**. Note what drives it. The expenses line — {{ nd.years }} years of a
family's life — is most of the total: about {{ nd.pv_multiple_of_expenses }} times a year's
expenses on its own. That's why a round number that merely "sounds like a
lot" can fall far short.

**Step 2: what is the insurer actually charging for?** Suppose, purely for
illustration, a one-year chance of death of 1 in
{% include inr.html n=nd.q_one_in %} (not an estimate for any real person or
age). The expected claim cost on ₹{{ nd.cover_rounded_crore }}
crore of cover that year is ₹{% include inr.html n=nd.expected_claim_cost %}.
The premium is that plus the insurer's costs and margin — so on average the
policyholder pays more than they expect to get back. That's true of every
insurance policy and it's fine: you aren't buying an expected profit, you're
buying the removal of a loss that would be ruinous. The
[Kelly post]({% post_url 2026-10-16-kelly-criterion-and-risk-of-ruin %})
made the same point about betting: some outcomes are worth paying to avoid
because you can't recover from them.

**Step 3: the savings inside a bundled plan.** Many policies combine
insurance with savings: you pay more, and get a maturity value back. Take a
hypothetical plan: ₹{% include inr.html n=bd.premium %} a year for
{{ bd.years }} years (paid at the start of each year, ₹{% include inr.html n=bd.paid %}
in total) and a maturity value of ₹{% include inr.html n=bd.maturity %} at
the end.

| Hypothetical bundled plan | |
|---|---:|
| Total premiums paid (₹) | {% include inr.html n=bd.paid %} |
| Maturity value (₹) | {% include inr.html n=bd.maturity %} |
| **IRR of premiums into maturity value** | **{{ bd.irr_pct }}%** |
{% for a in bd.alt_rows %}| The same premiums compounded at {{ a.rate_pct }}% a year (₹) | {% include inr.html n=a.fv %} |
{% endfor %}

The {{ bd.irr_pct }}% is the return on the savings part *including* the cost
of the life cover it carries, so it isn't a like-for-like comparison with a
deposit or a fund; the compounding rows are arithmetic at round rates, not
forecasts. The
point is the method. Any bundled plan's guaranteed maturity value can be
turned into an IRR (the [XIRR post]({% post_url 2026-10-01-sips-xirr-and-timing-myths %})
shows how), and then you can see what you're earning on the savings and ask
whether you'd buy the cover and the savings separately. How premiums and
payouts are taxed changes the answer and is covered in the tax series.

## Why this closes the module

Read back through this series and one idea keeps returning: **stay in the
game**. The [arithmetic of losses]({% post_url 2026-10-09-the-arithmetic-of-losses %})
showed that deep losses need huge gains to repair. Position sizing, Kelly and
leverage were all about never taking a bet that can end you. Concentration,
liquidity, currency, inflation and counterparty risk, and outright
manipulation, were about losses that arrive from directions the price chart
doesn't show. Insurance is the same idea applied
to your life instead of your portfolio: identify the loss you couldn't
recover from, and don't carry it alone.

## Common mistakes

- **Judging insurance by whether you "got your money back".** A term policy
  that never pays out did its job: it carried the risk for the whole term.
  Wanting a return from insurance is how people end up paying for bundled
  savings they'd never choose on their own.
- **Picking cover by a round number.** Cover sized by what "sounds like a
  lot", rather than by what it must replace, is, in our view, one of the commonest
  ways to be under-insured. Do the needs arithmetic, even roughly.
- **Insuring the wrong person.** Life cover replaces *income*. Cover on a
  child, with no one depending on their earnings, transfers very little risk.
- **Letting the cover end before the need does.** Term cover transfers risk
  only for its term. If the loans run for 20 more years and the children
  depend on the income for 25, a shorter policy leaves the last years
  uncovered.

**Takeaway:** Insurance is for losses you can't afford to carry, not for
returns — you pay a small certain cost so that a large uncertain one lands on
someone else. Size life cover by what it must replace, and if a policy bundles
in savings, turn its maturity value into an IRR before you judge it.
