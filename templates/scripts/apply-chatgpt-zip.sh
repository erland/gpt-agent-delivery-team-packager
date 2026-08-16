#!/usr/bin/env bash
set -euo pipefail

if [ $# -lt 1 ]; then
  echo "Usage: $0 <returned-zip> [--delete-missing]" >&2
  exit 1
fi

ZIP_FILE="$1"
DELETE_MISSING="${2:-}"

if [ ! -f "$ZIP_FILE" ]; then
  echo "Zip file not found: $ZIP_FILE" >&2
  exit 1
fi

if command -v git >/dev/null 2>&1 && git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  if [ -n "$(git status --porcelain)" ]; then
    echo "Refusing to apply zip because the Git working tree is not clean." >&2
    echo "Commit or stash local changes first." >&2
    exit 1
  fi
fi

TMP_DIR="$(mktemp -d)"
trap 'rm -rf "$TMP_DIR"' EXIT

unzip -q "$ZIP_FILE" -d "$TMP_DIR"

# If the zip contains a single top-level directory, use it as the source root.
ENTRY_COUNT="$(find "$TMP_DIR" -mindepth 1 -maxdepth 1 | wc -l | tr -d ' ')"
if [ "$ENTRY_COUNT" = "1" ] && [ -d "$(find "$TMP_DIR" -mindepth 1 -maxdepth 1 -type d | head -n 1)" ]; then
  SRC_ROOT="$(find "$TMP_DIR" -mindepth 1 -maxdepth 1 -type d | head -n 1)"
else
  SRC_ROOT="$TMP_DIR"
fi

rsync -a   --exclude ".git/"   --exclude ".chatgpt-zips/"   --exclude ".env"   --exclude ".env.*"   --exclude ".idea/"   --exclude ".vscode/"   "$SRC_ROOT"/ ./

if [ "$DELETE_MISSING" = "--delete-missing" ]; then
  rsync -a --delete     --exclude ".git/"     --exclude ".chatgpt-zips/"     --exclude ".env"     --exclude ".env.*"     --exclude ".idea/"     --exclude ".vscode/"     "$SRC_ROOT"/ ./
elif [ -n "$DELETE_MISSING" ]; then
  echo "Unknown option: $DELETE_MISSING" >&2
  exit 1
fi

git status --short 2>/dev/null || true
