# Audit checklist (run on the rendered meaning, not the Liquid)

The Sept 2026 review found arithmetic almost always right and **interpretation** often wrong. Audit sentences against the numbers beside them.

## A. Compliance (any failure blocks the post)

- [ ] No buy/sell/hold, target, "avoid", "accumulate", implied call, or "good time to…".
- [ ] No verdict — even soft — on a real company's valuation, quality or management. Grep the draft for: `rich|cheap|expensive|undervalued|overvalued|attractive|fair(ly)?|justified|mispric|honest of|impressive|excellent|healthy|robust|strong|quality|moat|compounder|bargain|safe|solid|sound|stable|reasonable|sensible|prudent|disciplined|conservative|aggressive|well-run|durable|leader|premium|discount to|outperform|underperform|deserve|warrant|worth`. **The grep is a prompt, not a test.** Negated verdicts ("not cheap", "not an irrational multiple") and peer comparisons ("valued below peers") are verdicts too. Read every sentence about a real company and ask: measurement or judgement? Also check tables, captions and the "explain like I'm 10" block.
- [ ] No hype: guaranteed, sure-shot, multibagger, can't lose, risk-free, easy money.
- [ ] No DCF, WACC, discount rate, fair value or justified multiple for a real listed company. Real companies get observables only.
- [ ] Real-company figures are one-year, backward-looking, framed as facts; no cumulative praise across the module.
- [ ] Every price/chart/figure used as a worked example is ≥ 3 months before the post's **publish date** — check every row and chart point, last one included (a 12 November post may use 12 August data, not 13 August). Never pull newer data even if a tool returns it. As-of date and source stated. House rule — don't call it "SEBI's rule"; SEBI's own condition is 30 days from 1 July 2026. New research statistics are exempt from the lag (say so).
- [ ] Comparisons state properties (cost, liquidity, tax treatment); they never map products to reader types, ages or goals, and never rank.
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
- [ ] **Mechanisms**: write each mechanism (option buyer vs seller payoff, FIFO order of SWP withdrawals, what capitalising an expense does to operating cash flow, set-off vs carry-forward of losses) as a sequence and re-derive it on a three-line example.
- [ ] **Denominators**: for every % or ratio, name the denominator in the sentence and check it matches the label (₹145 lakh vs the ₹120 lakh demand).
- [ ] **Right cell**: after rendering, check each number in prose against the table cell it points to (ten-fund figure vs infinite-fund floor). Half-year vs full-year periods.
- [ ] **Real-company statements used must sum** (balance sheet: both sides equal); data-script invariants asserted.
- [ ] **Rounding reproduces**: a reader recomputing from the displayed inputs gets the displayed answer.
- [ ] **Numbers from `_data/`**: none typed in prose; a script derived them; invariants asserted.
- [ ] **No series-structure copy**: no counts, "final post", "closes the series".
- [ ] **Unsourced claims about the world** have a citation you have actually seen, or are labelled "in our view". Never invent a citation, author, paper, circular number or date. If you cannot open it, say "not verified" and log VERIFY.

## C. Rules and tax

- [ ] Tax post carries both "Tax Year 2026-27" and "FY 2026-27" in the opening and one H2; old/new section numbers only from the Act itself; annual-refresh row in `TODO.md`.
- [ ] Each rule/rate/threshold: as-of date + primary source (circular/notification number and date; Finance Act; Income-tax Act, 2025 "Tax Year" terminology).
- [ ] Nothing stated from memory. If you could not open the primary document this session: no circular number, date, rate, threshold or section number — write "check the current rule" and add a VERIFY row. Tax and rule posts are delivered as drafts pending review, never "ready".
- [ ] Tax post: "Tax Year 2026-27 (FY 2026-27)" label; 4% cess consistent (or stated excluded); surcharge mentioned where it can change the answer; example fund and data source named.
- [ ] Logged in `TODO.md`: VERIFY rows for anything secondary; professional read for tax posts.

## D. Style and rendering

- [ ] Every acronym defined on first use, in this post; jargon link (earlier-dated posts only) at first use.
- [ ] Sentence-case headings and running text; ₹ with Indian grouping; "−" for negatives; no ".0"; dates written out in prose.
- [ ] No line starting with a number or Liquid value followed by ". ".
- [ ] Takeaway: starts `**Takeaway:**`; 2–3 sentences; first sentence ≤ 280 chars and standalone (count it with ₹ amounts and decimals rendered); few figures; no verdict on a real company.
- [ ] No Desi Bites "SME" wording; Desi Bites facts from `_data/`.
- [ ] Common mistakes: 2–4, concrete.
- [ ] Voice: short sentences, contractions, plain, a little informal; humour doesn't undercut clarity.

## E. Mechanical

`lint_post.py` (advisory) → `check_posts.py` (0 errors) → `make_og_cards.py` → Docker `jekyll build --future` → read the rendered page, including tables and the Takeaway card.
