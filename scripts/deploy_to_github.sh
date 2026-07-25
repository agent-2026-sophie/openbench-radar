#!/usr/bin/env bash
#
# One-command deploy helper for OpenBench Radar.
#
# Usage:
#   ./scripts/deploy_to_github.sh <github-username> [repo-name] [public|private]
#
# Examples:
#   ./scripts/deploy_to_github.sh wuwenya-sophie
#   ./scripts/deploy_to_github.sh wuwenya-sophie openbench-radar public
#
# It will:
#   1. create the GitHub repo (via `gh` CLI if available, otherwise print manual steps)
#   2. add the remote and push `main`
#   3. remind you to enable GitHub Pages (Settings -> Pages -> Source: GitHub Actions)
#
set -euo pipefail

USER="${1:?usage: deploy_to_github.sh <github-username> [repo-name] [public|private]}"
REPO="${2:-openbench-radar}"
VISIBILITY="${3:-public}"

# Ensure we run from the repo root (this script lives in ./scripts/).
cd "$(dirname "$0")/.."

if [ ! -d .git ]; then
  echo "==> git repo not initialized; initializing"
  git init -q
  git add -A
  git commit -q -m "feat: OpenBench Radar"
  git branch -M main
fi

if command -v gh >/dev/null 2>&1; then
  echo "==> creating repo via gh CLI: $USER/$REPO ($VISIBILITY)"
  gh repo create "$USER/$REPO" "--$VISIBILITY" --source=. --remote=origin --push
  echo "==> enabling GitHub Pages (source = GitHub Actions)"
  gh api -X POST "repos/$USER/$REPO/pages" -f "build_type=workflow" 2>/dev/null \
    || echo "   (enable Pages manually: Settings -> Pages -> Source: GitHub Actions)"
else
  echo "==> gh CLI not found. Create the repo on github.com first, then this script pushes it."
  echo "    1) Create an EMPTY repo named '$REPO' at https://github.com/new"
  REMOTE="https://github.com/$USER/$REPO.git"
  if git remote | grep -q '^origin$'; then
    git remote set-url origin "$REMOTE"
  else
    git remote add origin "$REMOTE"
  fi
  echo "==> pushing to $REMOTE"
  git push -u origin main
fi

echo ""
echo "✅ Done. Next steps:"
echo "   - Settings -> Pages -> Build and deployment -> Source: GitHub Actions"
echo "   - (optional) Settings -> Secrets -> add OPENAI_API_KEY / TAVILY_API_KEY for smarter reports"
echo "   - Actions tab -> run 'Benchmark Research' manually, or wait for the daily schedule"
echo "   - Your digest will be served at: https://$USER.github.io/$REPO/"
