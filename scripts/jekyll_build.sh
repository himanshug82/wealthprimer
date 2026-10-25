#!/usr/bin/env bash
# Build the site without Docker or `bundle exec`.
#
#   scripts/jekyll_build.sh OUTDIR              # as the live site sees it (future posts left out)
#   scripts/jekyll_build.sh OUTDIR --future     # include scheduled posts
#   JEKYLL_ENV=production scripts/jekyll_build.sh OUTDIR   # include the analytics snippet
#
# Why: in the Claude cloud sandbox the gems are installed globally but neither `jekyll` nor
# `bundle exec jekyll` is on PATH, and Docker isn't available. This finds the gem's own entry
# point. On a normal machine, `bundle exec jekyll build` does the same thing.
set -euo pipefail
out="${1:?usage: scripts/jekyll_build.sh OUTDIR [--future]}"; shift || true
cd "$(dirname "$0")/.."
if command -v jekyll >/dev/null 2>&1; then
  exec jekyll build -d "$out" "$@"
fi
entry="$(ls "$(gem env gemdir)"/gems/jekyll-*/exe/jekyll 2>/dev/null | sort -V | tail -1)"
[ -n "$entry" ] || { echo "jekyll gem not found (try: bundle install)" >&2; exit 1; }
exec ruby "$entry" build -d "$out" "$@"
