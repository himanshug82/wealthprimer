---
layout: post
title: "Why star ratings mislead — and why the same fund can swing from five stars to two"
description: "Star ratings rank trailing risk-adjusted returns within a category. On one index fund that figure swung from −1% to 27% a year; past winners earned no more."
image: /assets/og/why-star-ratings-mislead.png
date: 2026-12-12 09:00:00 +0530
series: mutual-funds
term: "Star ratings (mutual funds)"
---

{% assign r = site.data.mf2.ratings %}
{% assign mr = r.mean_reversion %}
{% assign mf = site.data.mf %}

## What a star rating actually is

Every fund platform shows stars. Few people know what they measure, so here
is the general recipe most rating agencies follow (each has its own
variations — this is the common shape, not any one firm's method):

1. Take every fund in a **category** (large cap, gilt, and so on).
2. For each fund, compute a **trailing** return — usually over 3 and 5 years —
   adjusted for some measure of risk (volatility, downside deviation, or a
   utility function that penalises losses).
3. **Rank** the funds. Top 10% get five stars, next 22.5% four, middle 35%
   three, and so on down a fixed distribution.
4. Repeat monthly.

Notice three things built into that. It is *relative* — a five-star fund in a
category that lost 30% is the fund that lost least. It is *trailing* — it
summarises what already happened. And it is *categorical* — the
[category definition]({% post_url 2026-12-10-sebi-fund-categories-decoded %}) decides who
is compared with whom.

None of that is dishonest. A rating is a compact, consistent way of saying
"over the last three to five years, this fund's risk-adjusted return ranked
here among its peers". The trouble is what people *hear*: a prediction.

## The input swings wildly — on the same fund

The single biggest driver of a rating is the trailing return. Here is that
number for one fund — the Nifty 50 index fund this series has used throughout
— read off on 31 March each year. A passive fund: no manager, no strategy
change, the same fifty stocks the whole time. Source: AMFI via mfapi.in,
regular plan, {{ mf.index_fund.regular_start }} to {{ mf.index_fund.regular_end }}. Historical data, for illustration only.

![Trailing three-year CAGR of the index fund at every date, with the 31 March readings marked]({{ '/assets/charts/mf2-trailing-3y.svg' | relative_url }})

| Read on | Trailing 3-year return (a year) | Percentile within the fund's own history |
|---|---:|---:|{% for s in r.trailing_3y_snapshots %}
| {{ s.as_of }} | {{ s.trailing_3y_cagr_pct }}% | {{ s.percentile_within_own_history | round }} |{% endfor %}

The same fund's "three-year return" — the headline input to a rating — ranged
from **{{ r.trailing_3y_min_pct }}%** to **{{ r.trailing_3y_max_pct }}%** a year across all the dates it could have been
read. On 31 March 2020 it was negative. Three years later it was 27%.

Nothing about the fund changed. The *window* changed. That's the first
lesson: most of a trailing return is simply what the market did over those
three years, not anything the fund did.

The ranking point is separate. A rating compares a fund against peers, not
against its own history — and in March 2020 every Nifty fund fell together,
so this fund's *rank* among them would barely have moved. Peers swing with the
same market, which makes the stars steadier than these raw figures. But it
also means the ranking is decided by the small *differences* between funds'
trailing returns, and those differences are mostly which fund happened to be
tilted the right way for the window that just closed. When the window rolls
on and a different tilt wins, a small gap in return can be enough to move a
fund from the top tenth of its category to the bottom third — five stars to
two, with the fund itself unchanged.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Imagine rating a cricket batter with stars based only on their last three
matches. After three good pitches, five stars. After three rainy games, two
stars. Same batter.

Now imagine picking your team for next season from those stars. You'd mostly
be picking whoever got the friendliest pitches recently — which tells you
very little about next season's pitches.

</details>

## Does a good past three years predict a good next three?

This is the question the stars are silently answering "yes" to, so it's worth
checking on data. Take the index fund's trailing three-year return at every
month-end, and pair it with the return over the *following* three years.
{{ mr.pairs }} such pairs exist in the data.

| | Past 3-year return (average) | Next 3-year return (average) |
|---|---:|---:|
| Top quarter of past readings | {{ mr.top_quartile_past_avg_pct }}% a year | {{ mr.top_quartile_next_avg_pct }}% a year |
| Bottom quarter of past readings | {{ mr.bottom_quartile_past_avg_pct }}% a year | {{ mr.bottom_quartile_next_avg_pct }}% a year |
| Correlation, past vs next | | {{ mr.corr_past3y_next3y }} |

The dates when the fund had just delivered its *best* three-year stretches
(averaging {{ mr.top_quartile_past_avg_pct }}% a year) were followed by three years averaging
{{ mr.top_quartile_next_avg_pct }}%. The dates when it had just delivered its *worst* (averaging
{{ mr.bottom_quartile_past_avg_pct }}%) were followed by three years averaging {{ mr.bottom_quartile_next_avg_pct }}%.
Essentially the same. The correlation between past and next is
{{ mr.corr_past3y_next3y }} — no detectable relationship in this sample. Hold that number
loosely, though: neighbouring month-ends share almost all of their three-year
windows, so those {{ mr.pairs }} pairs contain only about five or six genuinely
independent three-year periods. That's enough to rule out strong persistence
here, not enough to prove there's none.

This is one fund, and a passive one, so it isolates the *market's* contribution
to a trailing return: none of it persisted. The academic evidence on active
funds points the same way — outperformance over one window is a weak
predictor of the next, and the strongest persistent signal is *cost*, which
the [expense ratio post]({% post_url 2026-10-21-expense-ratios-direct-vs-regular %})
covered. Morningstar's own study (Russel Kinnel, "How Expense Ratios and Star
Ratings Predict Success", August 2010) found that low expense ratios predicted
a fund's future success more reliably than its star rating did.

## Two more things ratings can't see

**Survivorship.** Funds that do badly get merged into siblings or wound up.
Their records vanish from the category. The peer group a five-star fund is
ranked against is therefore missing its worst members — every survivor's
rank is flattered a little by the ghosts.

**The category itself.** A rating tells you a fund ranked well *within* its
category. It says nothing about whether that category — small cap, credit
risk, sectoral — belongs in your portfolio at all. Five stars on a
credit-risk fund is still 65% in bonds rated AA and below.

## What ratings are good for

Not nothing. Used as intended:

- **Screening out the persistently bad.** A fund with one or two stars for
  several consecutive years has usually earned it — persistent *under*
  performance is more predictable than persistent outperformance, and it is
  usually costs.
- **A quick risk-adjustment.** Most ratings penalise volatility or downside,
  so a five-star fund at least didn't get its return by taking wild risks *in
  the window measured*.
- **A prompt to read the factsheet**, not a substitute for it. The
  [factsheet post]({% post_url 2026-10-26-reading-a-factsheet %}) covers what
  to look at instead: mandate, cost, portfolio, and
  [rolling returns]({% post_url 2026-10-20-rolling-returns %}) across many
  windows rather than the one that just closed.

## Common mistakes

- **Reading stars as a forecast.** They summarise the window that just
  closed. On this data, that window had no predictive power for the next.
- **Switching funds when a rating drops.** The drop usually means the trailing
  window rolled off a good stretch. Selling then is buying high and selling
  low with extra steps — and a taxable event.
- **Comparing stars across categories.** A five-star gilt fund and a
  five-star small-cap fund are not comparable in any way.
- **Ignoring how many funds are in the category.** In a category of twelve,
  "top 10%" is one fund.
- **Forgetting who the rating is for.** Ratings drive flows; fund houses know
  which windows flatter them and market accordingly. Treat the stars on an
  advertisement as marketing.

**Takeaway:** A star rating ranks a fund's trailing risk-adjusted return
within its category — a summary of the window that just closed. On a passive
Nifty index fund that trailing figure swung from −1% to 27% a year depending
on the day you read it, and the best past three-year stretches were followed
by the same returns as the worst. Stars describe the weather that was. They
don't forecast.
