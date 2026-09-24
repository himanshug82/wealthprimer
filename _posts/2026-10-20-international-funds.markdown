---
layout: post
title: "International funds and fund of funds: the limit and the currency"
description: "Why Indian funds that invest abroad sometimes stop taking money, how SEBI's industry-wide overseas limits work, and what the rupee added in rupee returns."
image: /assets/og/international-funds.png
date: 2026-10-20 09:00:00 +0530
series: mutual-funds
term: "International fund and FoF (fund of funds)"
---

{% assign m = site.data.mf3 %}
{% assign i = m.international %}
{% assign o = m.reg.overseas %}
{% assign r = m.reg %}
{% assign fx = m.sources.fx %}
{% assign wk = i.walk %}

## Two ways to own the world from India

An Indian mutual fund can give you overseas exposure in two ways:

- **An international fund** buys foreign shares (or bonds) directly — a US
  technology stock, a Japanese carmaker — and holds them in its own
  portfolio.
- **A fund of funds (FoF)** doesn't buy shares at all. It buys units of
  *another* fund — often an overseas mutual fund or an exchange-traded fund
  (ETF) listed abroad — and passes the result on to you. SEBI files FoFs under
  "other schemes" — SEBI being the Securities and Exchange Board of India, the
markets regulator (the [categories post]({% post_url 2026-10-14-sebi-fund-categories-decoded %})
  mentioned the group).

Either way you invest in rupees, see a rupee [NAV]({% post_url 2026-09-25-what-a-mutual-fund-is %})
(net asset value, the per-unit value of the fund), and redeem in rupees. Two
things make these funds behave differently from domestic ones, and neither
is about the stocks inside: a **limit** on how much the whole Indian fund
industry may invest abroad, and the **currency**.

## The limit that switches funds off

SEBI caps how much Indian mutual funds may invest overseas — not per investor,
but **per fund house and for the whole industry together**. Paragraph
{{ o.mc_para }} of SEBI's [Master Circular for Mutual Funds]({{ r.mc26.url }})
({{ r.mc26.date | date: "%-d %B %Y" }}) sets the current limits, unchanged
since [SEBI's circular]({{ o.circular_url }}) {{ o.circular }}:

| | Per fund house | Whole industry |
|---|---:|---:|
| Overseas securities (shares, bonds, overseas funds) | US${{ o.per_mf_usd_bn }} billion | US${{ o.industry_usd_bn }} billion |
| Overseas ETFs | US${{ o.etf_per_mf_usd_mn }} million | US${{ o.etf_industry_usd_bn }} billion |

Each fund house also has a reserved quota of US${{ o.reserved_quota_usd_mn }} million
within the industry's US${{ o.industry_usd_bn }} billion.

Those are **dollar** ceilings shared by every Indian fund that invests abroad.
When a popular theme pulls in money, the industry can approach the ceiling,
and then funds have to stop accepting fresh money into their overseas
investments — no matter how many investors want in. That has already
happened:

- **January–February 2022.** SEBI wrote to the industry by email on
  {{ o.pause_2022_email | date: "%-d %B %Y" }} (the email is cited in SEBI's
  2024 Master Circular but not published), and fresh overseas investment was
  halted industry-wide. A press note from AMFI (the Association of Mutual Funds
  in India), [dated {{ o.resume_2022_note | date: "%-d %B %Y" }}]({{ o.resume_2022_url }}),
  let schemes resume, but only up to each fund house's utilisation "as of
  EOD [end of day] of {{ o.pause_2022_cap_date | date: "%B %-d, %Y" }}".
- **April 2024.** Funds investing in overseas ETFs were asked to stop
  accepting subscriptions from {{ o.etf_pause_2024 | date: "%-d %B %Y" }}. The
  SEBI emails behind this (19 and 20 March 2024) are cited in the 2024 Master
  Circular but not published; the date comes from press reports such as
  [Business Today's]({{ o.etf_pause_2024_secondary }}).

Press reports since then describe individual fund houses pausing and
reopening their own schemes as their share of the limit filled up. The practical consequence: **an
international fund may not take your SIP (systematic investment plan)
instalment next month**, for reasons that have
nothing to do with the fund's holdings. Check the scheme's current
subscription status before planning a regular investment into one.

One more rule worth knowing: since SEBI's circular
{{ o.indian_exposure_circular }}, Indian funds may also invest in overseas
funds that hold some *Indian* shares, as long as those holdings are no more
than {{ o.indian_exposure_pct }}% of the overseas fund's assets.

**This isn't your LRS limit.** The Reserve Bank of India's (RBI's) Liberalised Remittance Scheme lets
each resident individual send up to US${% include inr.html n=o.lrs_usd %} abroad per
financial year ([RBI FAQ]({{ o.lrs_url }})). When you buy a domestic
international fund or FoF, you pay the fund in rupees and the *fund* makes
the overseas investment under SEBI's industry limits. We couldn't find an RBI
or SEBI document that says in so many words that this leaves your own LRS
headroom untouched, so if it matters to you, confirm with your bank.

## The formula: what the currency does

A rupee investor in a dollar asset earns two returns multiplied together:

```
Rupee return = (1 + dollar return) × (1 + change in ₹ per $) − 1

  where  change in ₹ per $ = (₹/$ at the end ÷ ₹/$ at the start) − 1
```

If the rupee weakens (more rupees per dollar), your rupee return is *higher*
than the dollar return. If the rupee strengthens, it's lower. The fund
manager doesn't choose this; it comes with the asset.

## Worked example: ten financial years of the rupee

{{ fx.name }}, from the Federal Reserve Board's H.10 release (series DEXINUS,
[via FRED]({{ fx.url }})), on the last
trading day of each financial year (April to March), to 31 March 2026.
{{ fx.note }} Historical data, for illustration only.

| Financial year | ₹ per $ at start | ₹ per $ at end | Change |
|---|---:|---:|---:|{% for y in i.fy_rows %}
| {{ y.fy }} | {{ y.start }} | {{ y.end }} | {{ y.change_pct }}% |{% endfor %}

The rupee weakened in {{ i.years_rupee_weakened }} of the {{ i.years }} years and strengthened in the other
{{ i.years_rupee_strengthened }}; over the decade the price of a dollar in rupees rose by about
{{ i.cagr_10y_pct }}% a year. That's the long-run tailwind rupee investors in dollar
assets have had — and the table also shows it arrives in lumps, not smoothly.

Now a **hypothetical** overseas portfolio that earns exactly
{{ i.usd_return_pct }}% in dollars in a year:

| If the year was… | Dollar return | Rupee change | Your rupee return |
|---|---:|---:|---:|
| {{ i.fy26.fy }} | {{ i.usd_return_pct }}% | {{ i.fy26.change_pct }}% | **{{ i.fy26_rupee_return_pct }}%** |
| {{ i.fy21.fy }} | {{ i.usd_return_pct }}% | {{ i.fy21.change_pct }}% | **{{ i.fy21_rupee_return_pct }}%** |

Step by step for the first row, on ₹{% include inr.html n=wk.inr %}:

1. At ₹{{ i.fy26.start }} per dollar, ₹{% include inr.html n=wk.inr %} buys
   US${% include inr.html n=wk.usd %}.
2. The portfolio earns {{ i.usd_return_pct }}% in dollars: US${% include inr.html n=wk.usd_end %}.
3. At ₹{{ i.fy26.end }} per dollar that converts back to
   ₹{% include inr.html n=wk.inr_end %} — a {{ i.fy26_rupee_return_pct }}% rupee return.

Same portfolio, same dollar return, and the rupee investor's result was
{{ i.fy26_rupee_return_pct }}% in one year and {{ i.fy21_rupee_return_pct }}% in the other. A
fund's rupee performance mixes the manager's stock-picking (or the index's
return) with a currency move nobody in the fund controls. When you compare
an international fund with its benchmark, check whether the benchmark is
also measured in rupees — the
[benchmarks post]({% post_url 2026-10-02-benchmarks-and-comparing-like-with-like %})
made the same like-for-like point about dividends.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

You save up ₹850 and swap it for 10 dollars to buy a toy in an American shop.
A year later you sell the toy for 11 dollars — you made one dollar.

Now you swap the 11 dollars back into rupees. If the shopkeeper now gives you
₹94 for each dollar instead of ₹85, you get ₹1,034. Most of your gain came
from the swap, not the toy.

If the rupee had got *stronger* instead, the swap would have eaten some of
your toy profit. You don't get to choose which — it's part of owning
something that's priced in dollars.

</details>

## Costs and tax, briefly

A fund of funds has **two layers of cost**: the Indian FoF's own expense ratio
and the underlying overseas fund's, which comes out of that fund's NAV before
the FoF ever sees a return. Look up both — the
[expense ratio post]({% post_url 2026-09-28-expense-ratios-direct-vs-regular %})
showed how a percentage point compounds.

For tax, an international fund or FoF isn't an "equity-oriented fund" in the
Indian tax sense even if it holds only shares, because the tax test counts
*domestic* listed shares. How such funds are taxed is in the tax series<!-- RELINK 2026-10-30-debt-funds-gold-and-the-rest -->;
check the current rule before assuming equity treatment.

## Common mistakes

- **Assuming you can always add money.** The industry-wide dollar limit has
  shut these funds to new money before. A plan that depends on a monthly SIP
  into one needs a fallback.
- **Crediting the fund for the currency.** Part of a good rupee return in a
  year like {{ i.fy26.fy }} was the rupee falling, not the manager doing well.
  Strip it out before judging anything.
- **Treating the rupee's decline as guaranteed.** It weakened in most years
  of the table, and strengthened in {{ i.years_rupee_strengthened }}. Ten years of history is a
  record, not a forecast.
- **Ignoring the second expense layer** in a fund of funds.

**Takeaway:** An international fund gives you two returns multiplied
together — the overseas assets' and the currency's — and sits under a
dollar limit shared by the whole Indian fund industry. On the numbers above,
the same {{ i.usd_return_pct }}% dollar return became {{ i.fy26_rupee_return_pct }}% or {{ i.fy21_rupee_return_pct }}% in rupees depending
only on the year.
