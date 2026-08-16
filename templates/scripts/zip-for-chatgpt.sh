#!/usr/bin/env bash
set -euo pipefail

PROJECT_NAME="$(basename "$(pwd)")"
STAMP="$(date +%Y%m%d-%H%M%S)"
OUT_DIR=".chatgpt-zips/outgoing"
OUT_FILE="$OUT_DIR/${PROJECT_NAME}-${STAMP}.zip"

mkdir -p "$OUT_DIR"

if command -v git >/dev/null 2>&1 && git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  if [ -n "$(git status --porcelain)" ]; then
    echo "Warning: Git working tree is not clean. Consider committing or stashing before zipping." >&2
  fi
fi

zip -r "$OUT_FILE" .   -x ".git/*"   -x ".chatgpt-zips/*"   -x "node_modules/*"   -x "target/*"   -x "build/*"   -x "dist/*"   -x "coverage/*"   -x ".next/*"   -x ".vite/*"   -x ".gradle/*"   -x "out/*"   -x "*.zip"   -x "*.tsbuildinfo"   -x ".DS_Store"

echo "$OUT_FILE"
