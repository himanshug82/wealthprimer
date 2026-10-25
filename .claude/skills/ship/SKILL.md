---
name: ship
description: Run the pre-merge checks for Wealth Primer, open the PR, and (only when the owner asks) merge it and verify the live site. Use for "ship this", "create PR and merge", "check before merge". Never opens or merges a PR unprompted.
---

# ship

## Working agreement

- Develop on the session branch (`claude/happy-babbage-45qbnc`). **Open a PR only when asked; merge only when asked** ("create PR and merge" = both).
- After a merge, restart the branch from main: `git fetch -q origin main && git checkout -q -B <branch> origin/main`; later pushes use `--force-with-lease`.

## Steps

1. **Checks.** `scripts/ship_check.sh` — check_posts (0 errors), lint on changed posts (0 FAIL), OG cards current, image dimensions, full `jekyll build --future`. Fix anything red; don't skip. A WARN is for you to read, not to ignore.
2. **Read the diff** for: a post edited after it went live (needs `last_modified_at` only if substantive; no forward `post_url`), numbers typed into prose, a rule stated without a source (→ `verify-claims`), a renamed title with a stale OG card.
3. **`TODO.md`**: strike done items; add owed links and VERIFY rows created by this change.
4. **Commit** with a message that says what and why; end with the attribution lines from the session's system reminder.
5. **Push**: `git push -u origin <branch>` (retry network errors only, 2/4/8/16 s).
6. **PR** (only if asked): use `.github/pull_request_template.md` if it exists; otherwise sections: Summary · What changed · Checks run (paste the ship_check summary) · Owner follow-ups · Risks. End with the PR attribution line from the session reminder.
7. **Merge** (only if asked): confirm the PR is mergeable and no required check is red, then merge (squash unless the repo convention says otherwise). The `og-cards` job is advisory by design and must never block publishing.
8. **Verify live** after the Pages deploy (about 2–4 minutes):
   `python3 .claude/skills/ship/scripts/verify_live.py /path/ [/other/] --marker "text only the new version has"`
   Failures from the sandbox can be proxy noise — re-run once before reporting a problem, and say so.
9. **Report**: PR link (as `owner/repo#N` markdown link), merged or not, checks result, live verification result, owner follow-ups.

## Never

- Push to another branch, force-push to main, or create the PR/merge unasked.
- Merge with failing `check_posts.py` or a failing build.
- Add a workflow that makes the daily publish depend on advisory checks.
