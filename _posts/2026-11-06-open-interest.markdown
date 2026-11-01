---
layout: post
title: "Open interest: what it counts and what it can't say"
seo_title: "Open interest meaning: what it counts, what it can't"
description: "Open interest counts futures and options contracts still open; volume counts trades. A five-day worked example shows how they differ and what neither shows."
image: /assets/og/open-interest.png
date: 2026-11-06 09:00:00 +0530
series: jargon
term: "Open interest"
---

{% assign oi = site.data.jargon_m8.open_interest %}

## What open interest means

**Open interest** (OI) is the number of futures or options contracts that are still open: bought or sold, and not yet closed out or expired. It is a stock, like the number of cars currently parked in a lot. It is not a flow.

Every derivatives contract has two sides: someone who is long and someone who is short. When the two agree on a trade, that is *one* contract. Open interest counts it once, not twice.

That makes OI different from **[volume]({% post_url 2026-10-07-volume %})**, which counts how many contracts *changed hands* during the day, however many times. Volume is a flow, and it resets each day. Open interest carries over: it is whatever is left open at the close.

If you are new to the contracts themselves, the [call and put options post]({{ '/2026/11/04/call-and-put-options/' | relative_url }}) in the Risk series explains what is being counted. This post is part of [Jargon, Decoded]({{ '/series/jargon/' | relative_url }}). Exchanges publish open interest for each contract; the definition here is stated in our own words as a counting convention, not quoted from a rule.

## The rule of thumb

```
New trade, both sides opening   →  open interest rises by the trade size
New trade, one side closing     →  open interest does not change
New trade, both sides closing   →  open interest falls by the trade size
```

The trade between a buyer and a seller has two participants, and each is either *opening* a position (new) or *closing* one that already exists. Open interest depends on the combination.

## Worked example: five days in one hypothetical contract

This is an invented futures contract with made-up numbers, built only to show the counting. No real market is used.

| Day | What happened | Volume (contracts) | Change in OI | OI at the close |
|---|---|---:|---:|---:|
{% for r in oi.rows -%}
{% assign ch = r.change -%}
| {{ r.day }} | {{ r.desc }} | {{ r.volume }} | {% if ch > 0 %}+{{ ch }}{% elsif ch < 0 %}−{% assign pos = ch | times: -1 %}{{ pos }}{% else %}0{% endif %} | {{ r.oi }} |
{% endfor %}
Total volume across the five days is {{ oi.total_volume }} contracts. Open interest at the end is {{ oi.final_oi }}. They are different quantities and would almost never match.

Look at Day 2 and Day 5: volume was {{ oi.rows[1].volume }} and {{ oi.rows[4].volume }} contracts, yet open interest did not move at all. Nobody opened anything new; the same open contracts just changed hands. Look at Day 4: volume was {{ oi.rows[3].volume }}, and open interest *fell* by the same {{ oi.rows[3].volume }}, because the trade closed positions on both sides.

<details markdown="1">
<summary>🧒 Explain it like I'm 10 <em>(optional — skip if this is already clear)</em></summary>

Think of a playground with a see-saw and a bunch of "promise notes". Every time two kids shake hands and promise something to each other, that's one promise. Open interest is how many promises are *still waiting to be kept* right now. Volume is how many handshakes happened today, even if some were just kids passing an old promise to a new kid. If a kid hands their promise to a friend, there were two handshakes but still one promise waiting. If two kids tear up a promise together, there's one fewer.

</details>

## Common mistakes

- **Reading open interest as direction.** Every open contract has a long side and a short side of equal size. A rise in OI means more contracts were opened; it does not say whether the new money is bullish or bearish. Statements such as "OI rose, so buyers are in control" read a direction into a number that has none.
- **Mixing up open interest and volume.** Volume says how busy the day was. Open interest says how many positions are still open. A high-volume day can leave OI unchanged.
- **Treating a change in OI as a prediction.** OI is a backward-looking count. It tells you how many contracts exist now, and says nothing about what the price will do next. Ratios built from it, such as the put-call ratio, are bundles of the same count and carry the same limit; this post doesn't cover them or recommend reading them.
- **Forgetting expiry.** When a contract expires, its open interest runs to zero. A drop in OI near expiry is the contracts ending, not a change in opinion.

**Takeaway:** Open interest counts the contracts still open, each long-and-short pair once, while volume counts trades during the day. It can rise, fall or stay flat on a busy day, and it does not say which way anyone expects the price to go.
