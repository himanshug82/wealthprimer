---
layout: post
title: "Nomination for demat accounts and mutual fund folios"
description: "Without a nominee, your family may face extra paperwork. What SEBI's May 2026 nomination rules say: up to three nominees, opt-out and how shares split."
image: /assets/og/nomination-demat-folios.png
date: 2026-12-02 09:00:00 +0530
series: market-basics
needs_review: regulation
rules_as_of: "November 2026"
---

{% assign n = site.data.market_basics.nomination %}

## What a nomination is

A nominee is the person you name for your DP or fund house to deal with first if you die. It makes the transfer on death simpler for the family, because the depository participant (DP) or fund house has a named person to deal with.

This post explains the rules as written in SEBI (Securities and Exchange Board of India) circular {{ n.circular }} ([source]({{ n.url }})), as at {{ n.as_of }}. The circular came into effect on {{ n.effective }} and supersedes SEBI's earlier circulars on nomination for demat accounts and mutual fund folios. A folio is a mutual fund investor's account with a fund house.

## What the circular says

| Question | Rule as printed |
|---|---|
| Single account or folio, opened on or after the effective date | Investor must provide a nomination, unless they submit the "opt-out" declaration |
| Joint account or folio | Nomination is optional; consent of all joint holders is needed to give or change it |
| How many nominees | Up to {{ n.max_nominees }} |
| Several nominees | After the investor's death they may continue in the same account or folio, or open separate ones for their holdings |
| Share not specified | Divided equally; any odd lot after division goes to the first nominee named |
| Changing nominees | Allowed any number of times |
| Existing accounts and folios | The circular says its clauses apply "mutatis mutandis" to existing accounts and folios; it names the forms and the reminders explicitly |
| How to give it | Online (with a digital signature, Aadhaar-based e-sign or another recognised e-sign, or two-factor authentication including a one-time password, OTP) or offline with a signature |

If you opt out, the declaration you agree to says, in substance, that without a nomination your legal heirs may need extra legal or court documents, which can delay transmission of securities, and that if no claim is made for a prolonged period the holdings may be treated as unclaimed assets and transferred to the Investor Education and Protection Fund Authority.

DPs and fund registrars must also send reminders to holders without a nomination, by email and SMS (the circular says "bi-annual") and by a pop-up on first log-in of the day, and statements must show nominee names or a Yes/No. **Check the current circular** before acting: it is the source of truth, not this summary.

## Worked example: splitting among nominees

Two illustrations with hypothetical holdings.

**Equal split** (our reading, using whole units; fund units can be fractional). An investor holds {{ n.example_units }} units and names {{ n.max_nominees }} nominees without giving shares. Divided equally, the shares are {{ n.example_split[0] }}, {{ n.example_split[1] }} and {{ n.example_split[2] }}: the odd unit after division goes to the first nominee named.

**Percentage split.** The same style of holding, {{ n.pct_example.units }} units, with shares specified as {{ n.pct_example.pcts[0] }}%, {{ n.pct_example.pcts[1] }}% and {{ n.pct_example.pcts[2] }}%, divides into {{ n.pct_example.shares[0] }}, {{ n.pct_example.shares[1] }} and {{ n.pct_example.shares[2] }} units.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Say you keep your toys in a locked box and nobody else knows who should get the key if you move away. The grown-ups would have to ask lots of questions before opening it.

Writing a name on the box means they know who to hand it to. You can change the name whenever you like, and you can name up to three friends.

</details>

## Common mistakes

- **Treating nomination as a will.** The circular says nomination helps transmission to legal heirs; this post doesn't say how that interacts with a will or succession law. For that, see a legal professional.
- **Setting it once and forgetting it.** Investors can change nominees any number of times. A nominee named years ago may no longer be who you want.
- **Forgetting that joint holders must agree.** Nomination is optional for joint holdings, but giving or changing one needs every joint holder's consent.
- **Leaving percentages unstated and assuming a split that isn't equal.** The circular's default is an equal split.

**Takeaway:** A nominee is the person your DP or fund house deals with first when you die, which can make transmission to your legal heirs faster and smoother. As of November 2026 SEBI's rules allow up to three nominees per account or folio and an opt-out; check the current circular.
