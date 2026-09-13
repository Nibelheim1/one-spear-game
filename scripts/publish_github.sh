#!/usr/bin/env bash
set -euo pipefail

REPO_NAME="${1:-one-spear-game}"
VISIBILITY="${VISIBILITY:-private}"

if ! command -v git >/dev/null 2>&1; then
  echo "git is required" >&2
  exit 1
fi
if ! command -v gh >/dev/null 2>&1; then
  echo "GitHub CLI (gh) is required" >&2
  exit 1
fi
if [[ "$VISIBILITY" != "private" && "$VISIBILITY" != "public" ]]; then
  echo "VISIBILITY must be private or public" >&2
  exit 1
fi

gh auth status >/dev/null
OWNER="$(gh api user --jq .login)"
if gh repo view "$OWNER/$REPO_NAME" >/dev/null 2>&1; then
  echo "Repository $OWNER/$REPO_NAME already exists; refusing to overwrite it." >&2
  exit 2
fi

if [[ ! -d .git ]]; then
  git init -b main
fi

git add .
if ! git diff --cached --quiet; then
  git commit -m "Initial game release v1.5.1"
fi

gh repo create "$REPO_NAME" "--$VISIBILITY" --source=. --remote=origin --push
echo "Published: https://github.com/$OWNER/$REPO_NAME"
