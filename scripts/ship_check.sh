#!/usr/bin/env bash
# Pre-merge checks, the same ones CI runs. Exit 1 if any hard check fails.
#
#   scripts/ship_check.sh            # compare with origin/main
#   scripts/ship_check.sh BASE_REF   # compare with another ref
#
# 1 check_posts.py (0 errors)   2 lint_post.py on changed posts (0 FAIL)
# 3 make_og_cards.py --check    4 add_img_dims.py --check
# 5 full Jekyll build with --future (catches Liquid errors and forward post_url links)
set -uo pipefail
cd "$(dirname "$0")/.."
base="${1:-origin/main}"
fail=0
step() { printf '\n== %s\n' "$1"; }
run()  { "$@" || { echo "FAILED: $*"; fail=1; }; }

step "check_posts.py"
python3 scripts/check_posts.py | tail -4
python3 scripts/check_posts.py >/dev/null || { echo "FAILED: check_posts.py"; fail=1; }

step "lint_post.py on changed posts (vs $base)"
changed="$( { git diff --name-only "$base"...HEAD 2>/dev/null; git diff --name-only; git ls-files -o --exclude-standard; } | grep -E '^_posts/.*\.(markdown|md)$' | sort -u )"
if [ -n "$changed" ]; then
  # shellcheck disable=SC2086
  run python3 .claude/skills/write-post/scripts/lint_post.py $changed
else
  echo "no changed posts"
fi

step "og cards";  run python3 scripts/make_og_cards.py --check
step "img dims";  run python3 scripts/add_img_dims.py --check

step "jekyll build --future"
out="$(mktemp -d)"
if scripts/jekyll_build.sh "$out" --future >"$out.log" 2>&1; then
  grep -E "warning|Warning" "$out.log" | head -5 || true
  echo "build ok ($(find "$out" -name '*.html' | wc -l) html files)"
else
  tail -20 "$out.log"; echo "FAILED: jekyll build"; fail=1
fi
rm -rf "$out" "$out.log"

echo
[ $fail -eq 0 ] && echo "ALL CHECKS PASSED" || echo "SOME CHECKS FAILED"
exit $fail
