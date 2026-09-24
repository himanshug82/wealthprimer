---
layout: post
title: "Record date and ex-date: why a share 'falls' on the day its dividend is stripped off"
description: "The record date decides who gets a dividend; the ex-date is when the share starts trading without it. Worked on Britannia's ₹75 final dividend of August 2025."
image: /assets/og/record-date-and-ex-date.png
date: 2026-10-17 09:00:00 +0530
series: jargon
term: "Record date and ex-date"
---

{% assign st = site.data.jargon_m7.settlement %}
{% assign e1 = site.data.jargon_m7.exdiv[0] %}
{% assign e0 = site.data.jargon_m7.exdiv[1] %}
{% assign noise = site.data.jargon_m7.exdiv_noise %}
{% assign t2 = st.t2_example %}

## What the two dates mean

When a company declares a dividend (or a bonus, split or rights issue), it
has to decide *who* gets it. Shares change hands all day, so it picks a
date and says: whoever is on our register of shareholders at the end of
that day is entitled. That's the **record date**.

The **ex-date** ("ex" as in *without*) is the first trading day on which a
buyer does *not* get the dividend. Buy before the ex-date and the dividend
is yours; buy on or after it and it goes to the seller.

The two dates are linked by [settlement]({% post_url 2026-10-16-t-plus-1-settlement %}).
To be on the register at the end of the record date, your purchase must have
*settled* by then. With India's T+1 cycle, a trade settles one working day
later, so the last day to buy is the working day *before* the record date —
and the record date itself becomes the ex-date. NSE's corporate-actions
listing for Britannia shows exactly that: the ex-date and record date fall on
the same day for each of its recent dividends
([NSE corporate actions](https://www.nseindia.com/companies-listing/corporate-filings-actions)).
Under the old T+2 cycle they were a day apart: Britannia's ₹{{ t2.dps }} interim
dividend in 2020 went ex on {{ t2.ex_date | date: "%-d %B %Y" }}, with a record date of
{{ t2.record_date | date: "%-d %B %Y" }}.

## The rule

```
Last day to buy and receive the dividend  =  record date − 1 working day   (T+1)
Ex-date                                   =  record date                   (T+1)

Price adjustment on the ex-date (in theory):
Ex-dividend price  ≈  Previous close − Dividend per share
```

Why should the price drop? Because the cash is leaving the company. The
evening before the ex-date, a share is a claim on the business *plus* the
dividend about to be paid. The next morning it's a claim on the business
alone. Nothing about the business changed; the dividend just moved from the
company's bank account to yours. Your wealth is the same, split between the
share and the cash (before tax — the dividend is taxable in your hands).

## Worked example: Britannia's final dividend for FY 2024-25

Britannia's board recommended a final dividend of ₹{{ e1.dps }} a share on
{{ e1.board_date | date: "%-d %B %Y" }} and fixed **{{ e1.record_date | date: "%A %-d %B %Y" }}** as the record date, ahead of
the AGM (annual general meeting) on {{ e1.agm_date | date: "%-d %B %Y" }}
([Britannia's intimation to the exchanges](https://media.britannia.co.in/Intimation_of_Final_Dividend_pdf_43b8412ff2.pdf)).
Prices are NSE closes and opens from Yahoo Finance; for illustration only.

| | |
|---|---:|
| Last day to buy with the dividend ("cum-dividend") | {{ e1.last_cum_date | date: "%a %-d %b %Y" }} |
| Close that day | ₹{% include inr.html n=e1.cum_close %} |
| Ex-date (= record date) | {{ e1.ex_date | date: "%a %-d %b %Y" }} |
| Dividend per share | ₹{{ e1.dps }} ({{ e1.dividend_pct_of_cum_close }}% of the price) |
| "Expected" ex-dividend price (close − dividend) | ₹{% include inr.html n=e1.expected_ex_price %} |
| Actual open on the ex-date | ₹{% include inr.html n=e1.ex_open %} ({% include inr.html n=e1.open_gap_pct %}%) |
| Actual close on the ex-date | ₹{% include inr.html n=e1.ex_close %} ({% include inr.html n=e1.close_change_pct %}%) |
| Close + dividend, vs previous close | **+{{ e1.total_return_pct }}%** |
| Nifty 50 (price index) that day | +{{ e1.nifty_change_pct }}% |

Step by step:

1. Anyone holding at the close on {{ e1.last_cum_date | date: "%-d %B" }} — including a buyer that
   day, whose trade settled on the record date — got ₹{{ e1.dps }} a share, paid by
   {{ e1.paid_by | date: "%-d %B %Y" }}.
2. The share opened ₹{{ e1.open_gap | abs }} lower on the ex-date and closed ₹{{ e1.close_change | abs }}
   lower. Both are smaller than the ₹{{ e1.dps }} dividend.
3. Add the dividend back and a holder was {{ e1.total_return_pct }}% better off by the close
   — on a day the Nifty rose {{ e1.nifty_change_pct }}%.

The year before, the market was falling instead. Britannia's
₹{{ e0.dps_display }} final dividend for FY 2023-24 went ex on {{ e0.ex_date | date: "%-d %B %Y" }}
([105th AGM notice](https://media.britannia.co.in/Notice_of_105th_Annual_General_Meeting_pdf_8f7245e7e5.pdf)),
a day the Nifty fell {{ e0.nifty_change_pct | abs }}%. Britannia closed {{ e0.close_change_pct | abs }}% lower, and with
the dividend added back a holder was up {{ e0.total_return_pct }}%.

So did the price "not drop enough"? Two days can't tell you. The dividend was
about {{ e1.dividend_pct_of_cum_close }}% of the price; Britannia's ordinary daily move in FY26 had a
standard deviation of {{ noise.daily_sd_pct_fy26 }}%. The ex-dividend adjustment is the same size
as one day's noise, so on any single ex-date you see the adjustment *plus*
whatever else the market did. The mechanics are certain; reading them off
one day's chart isn't.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

A piggy bank with ₹100 inside is worth ₹100 plus the piggy. If the bank's
owner shakes out ₹5 for himself on Sunday, then on Monday the piggy bank is
worth ₹5 less. Nobody lost anything: the ₹5 is in his pocket now.

The record date is the day the teacher writes down who owns the piggy bank.
The ex-date is the first day someone who buys it doesn't get the ₹5.

</details>

## Common mistakes

- **Buying just before the ex-date to "capture" the dividend.** The price
  adjusts for it, so you're swapping share value for cash, and the dividend
  is taxed as income. There is no free lunch in the mechanics, whatever a
  single day's chart seems to show.
- **Buying on the record date.** Under T+1 your trade settles the next
  day, after the register is struck. The last day to buy is the working day
  before.
- **Reading the ex-date drop as bad news.** A long-term chart that isn't
  adjusted for dividends shows a small step down every year. It's cash
  leaving the company, not the market losing faith in it. The same goes,
  on a bigger scale, for bonuses and splits (see the
  [face-value post]({% post_url 2026-10-12-face-value-splits-and-bonuses %})).
- **Confusing the record date with the payment date.** Entitlement is fixed
  on the record date; the cash arrives weeks later (for Britannia's FY25
  final, by {{ e1.paid_by | date: "%-d %B %Y" }}). The [dividend yield post]({% post_url 2026-09-28-dividend-yield %})
  counts dividends by when they go ex.

**Takeaway:** the record date decides who gets a dividend, and under T+1 it
is also the ex-date: buy by the working day before, or the dividend goes to
the seller. The share price adjusts down by roughly the dividend that
morning, because the cash has left the company — nobody gets it for free.
