#!/usr/bin/env bash
set -euo pipefail

MAX_STEPS="${1:-3}"

for i in $(seq 1 "$MAX_STEPS"); do
  echo "=== Codex plan iteration $i/$MAX_STEPS ==="

  codex exec "Follow docs/agent-delivery-runbook.md. Implement exactly the next incomplete step. Update docs/agent-progress.md and stop after one step."

  git status --short

  if grep -qi "Status: Blocked\|blocked" docs/agent-progress.md 2>/dev/null; then
    echo "Progress indicates blocked work. Stopping."
    exit 1
  fi

  if grep -qi "plan complete\|all steps complete" docs/agent-progress.md 2>/dev/null; then
    echo "Progress indicates the plan is complete. Stopping."
    exit 0
  fi

  if ! git diff --quiet || ! git diff --cached --quiet; then
    git add -A
    git commit -m "Codex: implement next delivery step" || true
  fi
done
