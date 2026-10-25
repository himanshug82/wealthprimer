# Audit checklist (run on the rendered meaning, not the Liquid)

The Sept 2026 review found arithmetic almost always right and **interpretation** often wrong. Audit sentences against the numbers beside them.

## A. Compliance (any failure blocks the post)

- [ ] No buy/sell/hold, target, "avoid", "accumulate", implied call, or "good time to…".
- [ ] No verdict — even soft — on a real company's valuation, quality or management. Grep the draft for: `rich|cheap|expensive|undervalued|overvalued|attractive|fairly valued|justified|mispric|honest of|impressive|excellent|healthy|robust|strong|quality|moat|compounder|bargain|safe`. Each hit must be a mechanical description or about a fictional/generic company.
- [ ] No hype: guaranteed, sure-shot, multibagger, can't lose, risk-free, easy money.
- [ ] No DCF, WACC, discount rate, fair value or justified multiple for a real listed company. Real companies get observables only.
- [ ] Real-company figures are one-year, backward-looking, framed as facts; no cumulative praise across the module.
- [ ] Every price/chart/figure used as a worked example is ≥ 3 months before the post's date, with the as-of date and source stated. (House rule — don't call it "SEBI's rule".)
- [ ] No personalised advice ("if you are 30 you should…"). Sizing/diversification rules are "conventions from the literature".
- [ ] Disclaimer not pasted or reworded.
- [ ] TA/trading posts: limits stated honestly; no indicator "wins"; no hindsight-fitted setups.

## B. Accuracy

For each interpretive sentence, locate the table/number it rests on and check:

- [ ] **Like with like**: pre-tax vs post-tax; same equity base (post-IPO book is mostly IPO cash); same period and plan; price vs total-return index.
- [ ] **Directions and signs**: rose/fell, above/below, same/opposite, who wins — match the data.
- [ ] **Base rate**: a stat like "90% of X lost again" means nothing if 88% of everyone lost.
- [ ] **No hindsight endpoints**: fixed forward horizons (e.g. 63 sessions); incomplete windows dropped and the count stated.
- [ ] **The whole table**: if the heading says "every", the table has every one, including any unrecovered at the data's end.
- [ ] **Exact terms**: pre-/post-issue EPS (not "diluted"); tracking error (std dev) vs tracking difference; Macaulay vs modified duration; volatility clustering.
- [ ] **Rounding reproduces**: a reader recomputing from the displayed inputs gets the displayed answer.
- [ ] **Numbers from `_data/`**: none typed in prose; a script derived them; invariants asserted.
- [ ] **No series-structure copy**: no counts, "final post", "closes the series".
- [ ] **Unsourced claims about the world** have a citation you have actually seen, or are labelled "in our view". Never invent a citation, author, paper, circular number or date. If you cannot open it, say "not verified" and log VERIFY.

## C. Rules and tax

- [ ] Each rule/rate/threshold: as-of date + primary source (circular/notification number and date; Finance Act; Income-tax Act, 2025 "Tax Year" terminology).
- [ ] Nothing stated from memory; if unconfirmed, soften to what is certain and say "check the current rule".
- [ ] Tax post: "Tax Year 2026-27 (FY 2026-27)" label; 4% cess consistent (or stated excluded); surcharge mentioned where it can change the answer; example fund and data source named.
- [ ] Logged in `TODO.md`: VERIFY rows for anything secondary; professional read for tax posts.

## D. Style and rendering

- [ ] Every acronym defined on first use, in this post; jargon link (earlier-dated posts only) at first use.
- [ ] Sentence-case headings and running text; ₹ with Indian grouping; "−" for negatives; no ".0"; dates written out in prose.
- [ ] No line starting with a number or Liquid value followed by ". ".
- [ ] Takeaway: starts `**Takeaway:**`; first sentence ≤ 280 chars.
- [ ] Common mistakes: 2–4, concrete.
- [ ] Voice: short sentences, contractions, plain, a little informal; humour doesn't undercut clarity.

## E. Mechanical

`lint_post.py` (advisory) → `check_posts.py` (0 errors) → `make_og_cards.py` → Docker `jekyll build --future` → read the rendered page, including tables and the Takeaway card.
