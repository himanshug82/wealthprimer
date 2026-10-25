# Audit checklist

Run on the **rendered meaning**, not the Liquid. The Sept 2026 review (`_review/REVIEW-2026-09-24.md`) found arithmetic almost always right and **interpretation** often wrong. CLAUDE.md has the full rules; this list is what a script can't do and what a model skims.

## A. Compliance — any failure blocks the post

- [ ] No buy/sell/hold, target, "avoid", implied call, "good time to…", and no hype ("guaranteed", "sure-shot", "multibagger", "can't lose").
- [ ] No verdict — even soft — on a real company's valuation, quality or management. `lint_post.py` holds the word lists; **a grep is a prompt, not a test.** Negated verdicts ("not cheap", "not an irrational multiple") and peer comparisons ("valued below peers") are verdicts too. Read every sentence about a real company and ask: measurement or judgement? Include tables, captions, headings and the "explain it like I'm 10" block.
- [ ] No DCF, WACC, discount rate, fair value or justified multiple for a real listed company.
- [ ] Real-company figures are one-year, backward-looking facts; no praise accumulating across the module.
- [ ] Comparisons state properties (cost, liquidity, tax treatment); never map products to reader types, ages or goals; never rank.
- [ ] No personalised advice; sizing/diversification are "conventions from the literature".
- [ ] No claimed credentials, team, track record or personal results; disclaimer not pasted or reworded.
- [ ] TA/trading posts state limits honestly; no hindsight-fitted setups.

## B. Accuracy — for each interpretive sentence, locate its table/number

- [ ] **Lag**: every date in every worked-example table/chart ≤ publish date − 3 months (12 November post → 12 August data), last row included. House rule — not "SEBI's rule" (SEBI: 30 days from 1 July 2026). Research statistics are exempt; say so.
- [ ] **Like with like**: pre- vs post-tax; same equity base; same period and plan; price vs total-return index.
- [ ] **Directions and signs**: rose/fell, above/below, same/opposite, who wins.
- [ ] **Base rate**: "90% of X lost again" means nothing if 88% of everyone lost.
- [ ] **No hindsight endpoints**: fixed forward horizons; incomplete windows dropped and counted.
- [ ] **The whole table**: "every" means every, including any unrecovered at the data's end.
- [ ] **Exact terms**: pre-/post-issue EPS (not "diluted"); tracking error vs tracking difference; Macaulay vs modified duration; volatility clustering.
- [ ] **Mechanisms**: write each (option buyer vs seller payoff, FIFO of SWP withdrawals, what capitalising an expense does to operating cash flow, loss set-off vs carry-forward) as a sequence and re-derive it on a three-line example.
- [ ] **Denominators**: name the denominator in the sentence and check it matches the label (₹145 lakh vs the ₹120 lakh demand).
- [ ] **Right cell**: after rendering, check each prose number against the table cell it points to. Half-year vs full-year periods.
- [ ] **Sums**: any real-company statement used must balance; data-script invariants asserted.
- [ ] **Rounding reproduces** from the displayed inputs.
- [ ] **Numbers from `_data/`**, none typed in prose; no series-structure copy ("the next nine posts", "final post").
- [ ] **Unsourced claims about the world** have a citation you have actually opened, or are labelled "in our view". Never invent a citation, author, paper, circular number or date.

## C. Rules and tax

- [ ] Each rule/rate/threshold has an as-of date and a primary source (circular/notification number + date; Finance Act; Income-tax Act, 2025 "Tax Year" terminology).
- [ ] If you could not open the primary document this session: no circular number, date, rate, threshold or section number. "Check the current rule", VERIFY row, delivered as a draft.
- [ ] Tax post: "Tax Year 2026-27" **and** "FY 2026-27" in the opening and one H2; old/new section numbers only from the Act itself; 4% cess consistent (or stated excluded); surcharge mentioned where it can change the answer; example fund and data source named; annual-refresh row in `TODO.md`.

## D. Style and rendering

- [ ] Every acronym defined on first use in this post (including P/E, SIP, NAV, NSE); jargon link at first use, earlier-dated posts only.
- [ ] Sentence-case headings and running text; ₹ with Indian grouping; "−" for negatives; no ".0"; dates written out in prose.
- [ ] No line starting with a number or Liquid value + ". ".
- [ ] Takeaway: starts `**Takeaway:**`; 2–3 sentences; first sentence ≤ 280 chars and standalone (count it with ₹ amounts and decimals rendered); few figures; no verdict on a real company.
- [ ] Common mistakes: 2–4, concrete (glossary posts may collapse it into the definition).
- [ ] Voice: short sentences, contractions, plain, a little informal.
- [ ] Desi Bites facts from `_data/`; never "SME".

## E. Mechanical

`lint_post.py` → `check_posts.py` (0 errors) → `make_og_cards.py` → Docker `jekyll build --future` → read the rendered page.

## F. Module level (batches only)

- [ ] `grep -l` the same real company across the new files: are verdicts or praise accumulating? Frame as one-year facts.
- [ ] No two new posts own the same term/intent; every internal link points to an earlier-dated post; owed links logged.
- [ ] `planned:` in `_data/series.yml` bumped; one post per series per day; Tax posts (if any) all marked pending professional read.
