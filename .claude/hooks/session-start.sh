#!/bin/bash
# SessionStart hook for Claude Code cloud sessions (synchronous, idempotent, cloud-only).
# Installs the Python packages the repo's scripts import, so `python3 scripts/derive_*.py`,
# `make_og_cards.py`, the charts scripts and the skills' audit scripts work from the first turn.
# Chromium is in the cloud image. Jekyll is NOT always there (1 Nov 2026 session had no gems), so
# install the Gemfile's gems if the jekyll gem is missing; see scripts/jekyll_build.sh for the build.
set -euo pipefail
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then exit 0; fi
cd "${CLAUDE_PROJECT_DIR:-$(dirname "$0")/../..}"
need=""
for mod in pandas numpy yaml matplotlib PIL requests; do
  python3 -c "import $mod" 2>/dev/null || need="$need $mod"
done
if [ -n "$need" ]; then
  pip install --quiet --disable-pip-version-check pandas numpy pyyaml matplotlib pillow requests
fi
if ! ls "$(gem env gemdir 2>/dev/null)"/gems/jekyll-*/exe/jekyll >/dev/null 2>&1 && ! command -v jekyll >/dev/null 2>&1; then
  bundle install --quiet >/dev/null 2>&1 || echo "wealthprimer session setup: bundle install failed; jekyll build will not run" >&2
fi
# Skills call these by name; keep them executable.
chmod +x scripts/*.sh .claude/skills/*/scripts/* 2>/dev/null || true
echo "wealthprimer session setup: python deps and jekyll ready"
