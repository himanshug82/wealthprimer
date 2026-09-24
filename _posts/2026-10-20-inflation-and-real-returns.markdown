---
layout: post
title: "Inflation and real returns: what your money actually bought"
description: "Thirteen years of MoSPI's CPI against an index fund, a gilt fund and a rolled SBI fixed deposit — nominal returns, real returns, and the years each lost ground."
image: /assets/og/inflation-and-real-returns.png
date: 2026-10-20 09:00:00 +0530
series: risk
term: "Real return"
---

{% assign r2 = site.data.risk2 %}
{% assign d = r2.dataset %}
{% assign inf = r2.inflation %}
{% assign si = inf.summary.idx %}
{% assign sg = inf.summary.gilt %}
{% assign sf = inf.summary.fd %}
{% assign fy21 = inf.rows[7] %}

## The risk that doesn't show up on a statement

A fixed deposit statement never shows a loss. A savings account never has a
bad year. And yet money in both can lose ground every year, because the thing
it's measured against — what a rupee buys — keeps moving. That's **inflation
risk**: the chance that your money grows more slowly than prices, so that
you end up with more rupees and less to spend them on.

The number that captures it is the **real return**: the return after
inflation. It's the only return that tells you whether you're actually better
off. This post computes it for three things this blog has data on, over the
longest stretch the current inflation series allows.

## The formula

```
Inflation over a year  =  CPI at the end / CPI at the start  −  1

Real return  =  (1 + nominal return) / (1 + inflation)  −  1
             ≈  nominal return − inflation               (only for small numbers)

Rupees needed today to match ₹1 then  =  CPI today / CPI then
```

CPI is the **Consumer Price Index**: the price of a fixed basket of goods and
services an average household buys, published monthly by MoSPI (the Ministry
of Statistics and Programme Implementation). The exact formula matters when
numbers are large: in {{ fy21.fy }} the index fund's {{ fy21.idx_nominal_pct }}% nominal
return, with {{ fy21.cpi_pct }}% inflation, was a {{ fy21.idx_real_pct }}% real return, not
{{ fy21.idx_nominal_pct | minus: fy21.cpi_pct | round: 1 }}%.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Last summer ₹100 bought you 5 ice creams at ₹20 each. You saved the ₹100 in
a box and it grew to ₹104 by this summer. Nice!

But ice cream now costs ₹22. Your ₹104 buys 4 ice creams, with ₹16 left over.
You have more money and fewer ice creams. The "real" question isn't how many
rupees you have — it's how many ice creams they buy.

</details>

## The data, and one wrinkle

**Inflation:** the All-India CPI (General index, Combined), from
[MoSPI]({{ d.cpi_source_url }}) ([our CSV]({{ d.cpi_csv | relative_url }})).
The series used here starts in January 2013, so the comparison runs over
{{ inf.years }} financial years, {{ inf.first_fy }} to {{ inf.last_fy }}
(March 2013 to March 2026). The wrinkle: MoSPI moved CPI to a new base year
(2024 = 100) with its release of
[12 February 2026]({{ d.cpi_base_change_url }}), and publishes a linking
factor ({{ d.cpi_linking_factor_combined }} for the Combined index) to join
the old series to the new one. We chain year-on-year changes instead:
{{ inf.first_fy }} to FY25 within the old base-2012 series, and
{{ inf.last_fy }} within the new one. Each year's rate is then exactly MoSPI's
published March inflation.

**Returns**, all pre-tax, each year from 31 March to 31 March:

- **Index fund** — {{ site.data.risk.dataset.fund_name }}, regular plan growth
  NAV (net asset value; AMFI, the Association of Mutual Funds in India, via [mfapi.in]({{ d.fund_source_url }})).
- **Gilt fund** — UTI Gilt Fund, regular plan growth NAV (AMFI via
  [mfapi.in]({{ d.gilt_source_url }})); a fund of government bonds, see the
  [debt funds post]({% post_url 2026-10-12-debt-funds-explained %}).
- **Fixed deposit (FD)** — a one-year deposit with SBI (State Bank of India), opened each 1 April at the
  rate SBI was paying the general public that day, compounded quarterly, and
  rolled into a new one-year deposit each year. Rates from SBI's
  [historical rate sheet]({{ d.sbi_rates_url }}) and its
  [deposit rate page]({{ d.sbi_page_url }}).

Historical data to {{ d.as_of }}, for illustration only.

## Worked example: {{ inf.years }} years, year by year

| Year | CPI inflation | SBI 1-yr rate | Index fund | Gilt fund | FD | Index fund, real | Gilt fund, real | FD, real |
|---|---:|---:|---:|---:|---:|---:|---:|---:|{% for row in inf.rows %}
| {{ row.fy }} | {{ row.cpi_pct }}% | {{ row.fd_rate_pct }}% | {{ row.idx_nominal_pct }}% | {{ row.gilt_nominal_pct }}% | {{ row.fd_nominal_pct }}% | **{{ row.idx_real_pct }}%** | **{{ row.gilt_real_pct }}%** | **{{ row.fd_real_pct }}%** |{% endfor %}

And over the whole period:

| {{ inf.first_fy }}–{{ inf.last_fy }} | Index fund | Gilt fund | Fixed deposit |
|---|---:|---:|---:|
| Nominal return, a year ([CAGR]({% post_url 2026-09-26-point-to-point-returns %}), compound annual growth rate) | {{ si.nominal_cagr_pct }}% | {{ sg.nominal_cagr_pct }}% | {{ sf.nominal_cagr_pct }}% |
| Real return, a year | **{{ si.real_cagr_pct }}%** | **{{ sg.real_cagr_pct }}%** | **{{ sf.real_cagr_pct }}%** |
| ₹1 lakh became (rupees) | {% include inr.html n=si.lakh_nominal %} | {% include inr.html n=sg.lakh_nominal %} | {% include inr.html n=sf.lakh_nominal %} |
| …in March-2013 rupees | {% include inr.html n=si.lakh_real %} | {% include inr.html n=sg.lakh_real %} | {% include inr.html n=sf.lakh_real %} |
| Years with a negative real return | {{ si.negative_real_years }} of {{ inf.years }} | {{ sg.negative_real_years }} of {{ inf.years }} | {{ sf.negative_real_years }} of {{ inf.years }} |

![Real value of ₹1 lakh in each, deflated by CPI]({{ '/assets/charts/risk2-real-returns.svg' | relative_url }})

What the tables say:

1. **Prices rose {{ inf.cpi_cum_pct | round }}% in {{ inf.years }} years** —
   {{ inf.cpi_cagr_pct }}% a year. You needed
   ₹{% include inr.html n=inf.lakh_needed %} in March 2026 to buy what
   ₹1,00,000 bought in March 2013. At that pace prices double roughly every
   {{ inf.doubling_years_at_cagr }} years.
2. **Every one of the three beat inflation over the full period**, pre-tax.
   The FD's ₹1 lakh grew to ₹{% include inr.html n=sf.lakh_nominal %} on
   paper but ₹{% include inr.html n=sf.lakh_real %} in purchasing power: a
   real gain of about {{ sf.real_cagr_pct }}% a year, not
   {{ sf.nominal_cagr_pct }}%.
3. **The index fund had the highest real return and by far the deepest
   losing year**: a real return of {% include inr.html n=si.worst_real_pct %}% in {{ si.worst_real_fy }}. Its
   real return was negative in {{ si.negative_real_years }} years, the gilt fund's in
   {{ sg.negative_real_years }}, the FD's in {{ sf.negative_real_years }} ({{ sf.negative_real_fy_list }}, when the deposit rate
   sat below inflation). Real return and real *risk* came together.
4. **The gilt fund's real return was barely above the FD's**, with more
   losing years — the interest-rate risk the
   [modified duration post]({% post_url 2026-10-06-modified-duration %})
   describes, showing up as real losses in the years its nominal return was
   low.

## What "pre-tax" hides

Every figure above is before tax, and that flatters the FD most. FD interest
is generally taxed year by year as it accrues, while fund gains are taxed
when you sell, under different rules; the tax series covers how each is taxed. After
tax, a deposit whose pre-tax real return is about {{ sf.real_cagr_pct }}% a
year can end up close to zero or below it, depending on your slab. The
funds' figures are regular-plan NAVs, so they're already after the
[expense ratio]({% post_url 2026-09-28-expense-ratios-direct-vs-regular %});
direct plans would show a little more.

## Common mistakes

- **Subtracting instead of dividing.** For a big year the shortcut breaks:
  nominal minus inflation overstates the real return. Use the division.
- **Treating "no loss" as "safe".** The FD never showed a nominal loss, and
  still lost purchasing power in {{ sf.negative_real_years }} years.
  Inflation risk is invisible on a statement by design.
- **Assuming CPI is your inflation.** CPI is an all-India average basket. A
  household whose spending tilts to school fees, rent or healthcare can see a
  very different number. For a long goal, the relevant inflation is the one
  for *that* goal.
- **Comparing a real return with a nominal one.** "The index fund did
  {{ si.nominal_cagr_pct }}% a year" and "my FD's real return was {{ sf.real_cagr_pct }}%" are different
  kinds of number.
  Convert both, or neither.

**Takeaway:** A return only means something after inflation, and inflation
compounds quietly — prices rose {{ inf.cpi_cum_pct | round }}% in
{{ inf.years }} years here. Over that stretch, pre-tax, a rolled SBI FD
earned about {{ sf.real_cagr_pct }}% a year in real terms and an index fund
about {{ si.real_cagr_pct }}%, with much deeper bad years. Check what your money
buys, not how many rupees it shows.
