---
name: verify-claims
description: Check a Wealth Primer post's rules, rates, thresholds and citations against the primary source (SEBI, RBI, Income-tax Act, AMFI) instead of memory. Use for "verify this rule", "clear the VERIFY rows in TODO.md", "is this circular citation right", and before scheduling any rules or tax post. Reports confirmed / corrected / unreachable; never states a rule from memory.
---

# verify-claims

CLAUDE.md: *never state a rule from memory; cite the primary source with number and date; if you can't confirm, soften and say "check the current rule".* This skill is the procedure for doing that.

## Inputs

A post path, a quoted claim, or a `VERIFY` row from `TODO.md`. If none is given, list the `VERIFY` rows (`grep -n VERIFY TODO.md`) and ask which to clear.

## Procedure

1. **Extract the claims.** For each post, list every sentence that states a rule, rate, threshold, limit, date of effect, definition-by-regulation or a circular/section number. Skip pure arithmetic from `_data/`. One line each: *claim · where in the post · cited source*.
2. **Find the primary source.** Start from `references/sources.md` (known URLs and what is reachable from this sandbox). Otherwise WebSearch restricted to `sebi.gov.in`, `rbi.org.in`, `incometaxindia.gov.in`, `amfiindia.com`, `nseindia.com`. A news piece or broker blog is a lead, never the source.
3. **Fetch and search the text.**
   ```
   python3 .claude/skills/verify-claims/scripts/fetch_source.py get <URL> --name <short-name>
   python3 .claude/skills/verify-claims/scripts/fetch_source.py find <short-name> "<regex>" -C 4
   python3 .claude/skills/verify-claims/scripts/fetch_source.py show <short-name> <LINE> -C 25
   ```
   Read the clause itself, including provisos and the effective date. Check the **version in force**: has a later circular amended or replaced it?
4. **Decide, per claim:**
   - **Confirmed**: wording and number match. Record the citation in the form `SEBI Master Circular for Mutual Funds, <number>, <date>, para <x>`.
   - **Corrected**: the post says more, less or something different. Fix the post (smallest edit), add `last_modified_at` (a rule changed → substantive), and say what changed.
   - **Unreachable / ambiguous**: soften the sentence to what is certain plus "check the current rule", and leave a `VERIFY` row in `TODO.md` naming the source you could not open. Never fill the gap from memory.
5. **Update the record.** Strike or remove cleared `VERIFY` rows; add owed ones. Do not edit a live post's links to later-dated posts (`post_url` rule).
6. **Report** a table: claim · verdict · source (number, date, para/page) · edit made. Say plainly which claims you could not check.

## Rules of thumb

- No professional reads the tax posts (owner decision), so this skill is the main safeguard: for flagged posts, every rule needs a primary source or must be softened. Say in the report what could not be confirmed. It is not a professional's review.
- Quote at most a short phrase from a source; paraphrase the rest.
- Rates and limits that change with the Budget: check the Finance Act / Income-tax Act, 2025 text, and state Tax Year and FY.
- A circular number you cannot find in the document text is not a citation. Don't paraphrase one from a secondary page.
- If a source contradicts CLAUDE.md or a post, trust the source, fix the post, and flag the CLAUDE.md line for the owner (don't edit CLAUDE.md yourself).
- The cache lives outside the repo (`~/.cache/wealthprimer-sources`); never commit downloaded PDFs.
