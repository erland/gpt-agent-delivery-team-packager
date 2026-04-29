# Knowledge Bundle — Script Templates

Use this bundle as reference material when generating helper scripts.



---

# codex-next-step.sh template

Source: `templates/scripts/codex-next-step.sh`

#!/usr/bin/env bash
set -euo pipefail

codex exec "Follow docs/agent-delivery-runbook.md. Implement exactly the next incomplete step. Update docs/agent-progress.md and stop after one step."




---

# codex-run-plan.sh template

Source: `templates/scripts/codex-run-plan.sh`

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




---

# zip-for-chatgpt.sh template

Source: `templates/scripts/zip-for-chatgpt.sh`

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




---

# apply-chatgpt-zip.sh template

Source: `templates/scripts/apply-chatgpt-zip.sh`

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




---

# validate-codex-agent-toml.py template

Source: `templates/scripts/validate-codex-agent-toml.py`

#!/usr/bin/env python3
"""Validate Codex custom agent TOML files for an agent delivery team package.

This script intentionally uses only Python standard library modules available in Python 3.11+.
It checks the common failure mode where Codex ignores agent role files because
`developer_instructions` is missing.

Usage:
  python3 scripts/validate-codex-agent-toml.py
  python3 scripts/validate-codex-agent-toml.py path/to/project
"""

from __future__ import annotations

import sys
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover
    print("ERROR: Python 3.11+ is required for tomllib.", file=sys.stderr)
    sys.exit(2)


ROLE_FILES = {
    "architect.toml",
    "implementer.toml",
    "test-engineer.toml",
    "reviewer.toml",
    "documentation-writer.toml",
}

READ_ONLY_ROLES = {"architect.toml", "reviewer.toml"}
WRITE_ROLES = {"implementer.toml", "test-engineer.toml", "documentation-writer.toml"}

FORBIDDEN_TOP_LEVEL_HINTS = {"role", "prompt", "objective", "instructions"}


def fail(message: str) -> None:
    print(f"ERROR: {message}")


def warn(message: str) -> None:
    print(f"WARN: {message}")


def validate_agent_file(path: Path) -> list[str]:
    errors: list[str] = []

    try:
        data = tomllib.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        return [f"{path}: invalid TOML: {exc}"]

    for field in ("name", "description", "developer_instructions"):
        value = data.get(field)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{path}: missing or empty required string field `{field}`")

    developer_instructions = data.get("developer_instructions")
    if isinstance(developer_instructions, str):
        required_terms = ["objective", "constraint"]
        lowered = developer_instructions.lower()
        for term in required_terms:
            if term not in lowered:
                errors.append(
                    f"{path}: developer_instructions should describe role {term}s"
                )
        if "edit" not in lowered and "read-only" not in lowered:
            errors.append(
                f"{path}: developer_instructions should state whether the agent may edit files"
            )

    sandbox_mode = data.get("sandbox_mode")
    if path.name in READ_ONLY_ROLES and sandbox_mode != "read-only":
        errors.append(f"{path}: expected sandbox_mode = "read-only"")
    if path.name in WRITE_ROLES and sandbox_mode != "workspace-write":
        errors.append(f"{path}: expected sandbox_mode = "workspace-write"")

    if path.name in ROLE_FILES:
        for forbidden in FORBIDDEN_TOP_LEVEL_HINTS:
            if forbidden in data and forbidden != "developer_instructions":
                errors.append(
                    f"{path}: avoid top-level `{forbidden}`; use `developer_instructions` instead"
                )

    return errors


def validate_config(config_path: Path) -> list[str]:
    errors: list[str] = []
    if not config_path.exists():
        return errors

    try:
        data = tomllib.loads(config_path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        return [f"{config_path}: invalid TOML: {exc}"]

    if "mcp_servers" in data:
        errors.append(
            f"{config_path}: must not configure MCP servers by default"
        )
    if "plugins" in data:
        errors.append(
            f"{config_path}: must not enable plugins by default"
        )

    agents = data.get("agents")
    if agents is not None:
        if not isinstance(agents, dict):
            errors.append(f"{config_path}: [agents] must be a table")
        else:
            max_depth = agents.get("max_depth")
            if max_depth is not None and max_depth != 1:
                errors.append(f"{config_path}: expected agents.max_depth = 1 by default")
    return errors


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    agents_dir = root / ".codex" / "agents"

    all_errors: list[str] = []

    if not agents_dir.exists():
        fail(f"Missing directory: {agents_dir}")
        return 1

    forbidden_config = agents_dir / "config.toml"
    if forbidden_config.exists():
        fail(f"Invalid config location: {forbidden_config}. Use .codex/config.toml instead.")
        return 1

    for name in sorted(ROLE_FILES):
        path = agents_dir / name
        if not path.exists():
            all_errors.append(f"Missing required agent file: {path}")
            continue
        all_errors.extend(validate_agent_file(path))

    all_errors.extend(validate_config(root / ".codex" / "config.toml"))

    if all_errors:
        for error in all_errors:
            fail(error)
        return 1

    print("Codex agent TOML validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())




---

# validate-zip-workflow-scripts.py template

Source: `templates/scripts/validate-zip-workflow-scripts.py`

#!/usr/bin/env python3
"""Validate ChatGPT zip workflow scripts in an agent delivery team package.

This validator checks that the generated package contains the expected zip workflow scripts
and that their contents include important safety behaviors.

Usage:
  python3 scripts/validate-zip-workflow-scripts.py
  python3 scripts/validate-zip-workflow-scripts.py path/to/project
"""

from __future__ import annotations

import os
import stat
import sys
from pathlib import Path


REQUIRED_FILES = [
    "scripts/zip-for-chatgpt.sh",
    "scripts/apply-chatgpt-zip.sh",
    "docs/chatgpt-zip-workflow.md",
]


ZIP_SCRIPT_REQUIRED_SNIPPETS = [
    ".chatgpt-zips/outgoing",
    "zip -r",
    ".git/*",
    ".chatgpt-zips/*",
    "node_modules/*",
    "target/*",
    "build/*",
    "dist/*",
    "coverage/*",
    "*.zip",
    "*.tsbuildinfo",
]


APPLY_SCRIPT_REQUIRED_SNIPPETS = [
    "git status --porcelain",
    "Refusing to apply zip because the Git working tree is not clean",
    "mktemp -d",
    "unzip",
    "rsync",
    "--exclude \".git/\"",
    "--exclude \".chatgpt-zips/\"",
    "--exclude \".env\"",
    "--exclude \".env.*\"",
    "--delete-missing",
]


DOC_REQUIRED_SNIPPETS = [
    ".chatgpt-zips/",
    "outgoing",
    "incoming",
    "applied",
    "zip-for-chatgpt.sh",
    "apply-chatgpt-zip.sh",
    "git status",
    "git diff",
    "verify",
    "commit",
]


def is_executable(path: Path) -> bool:
    mode = path.stat().st_mode
    return bool(mode & stat.S_IXUSR)


def require_file(root: Path, rel: str, errors: list[str]) -> Path | None:
    path = root / rel
    if not path.exists():
        errors.append(f"Missing required file: {rel}")
        return None
    if not path.is_file():
        errors.append(f"Expected file but found non-file path: {rel}")
        return None
    return path


def require_snippets(path: Path, snippets: list[str], errors: list[str]) -> None:
    text = path.read_text(encoding="utf-8", errors="replace")
    for snippet in snippets:
        if snippet not in text:
            errors.append(f"{path.relative_to(path.parents[1])}: missing expected snippet: {snippet}")


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    errors: list[str] = []
    warnings: list[str] = []

    paths = {rel: require_file(root, rel, errors) for rel in REQUIRED_FILES}

    zip_script = paths.get("scripts/zip-for-chatgpt.sh")
    if zip_script:
        require_snippets(zip_script, ZIP_SCRIPT_REQUIRED_SNIPPETS, errors)
        if not is_executable(zip_script):
            warnings.append("scripts/zip-for-chatgpt.sh is not executable. Run: chmod +x scripts/zip-for-chatgpt.sh")

    apply_script = paths.get("scripts/apply-chatgpt-zip.sh")
    if apply_script:
        require_snippets(apply_script, APPLY_SCRIPT_REQUIRED_SNIPPETS, errors)
        if not is_executable(apply_script):
            warnings.append("scripts/apply-chatgpt-zip.sh is not executable. Run: chmod +x scripts/apply-chatgpt-zip.sh")

    doc = paths.get("docs/chatgpt-zip-workflow.md")
    if doc:
        require_snippets(doc, DOC_REQUIRED_SNIPPETS, errors)

    # Check the local exchange directories are ignored if .gitignore exists.
    gitignore = root / ".gitignore"
    if gitignore.exists():
        text = gitignore.read_text(encoding="utf-8", errors="replace")
        if ".chatgpt-zips/" not in text:
            errors.append(".gitignore exists but does not include .chatgpt-zips/")
        if "*.zip" not in text:
            errors.append(".gitignore exists but does not include *.zip")
    else:
        warnings.append(".gitignore not found. Generated packages should create or update it with zip workflow exclusions.")

    for warning in warnings:
        print(f"WARN: {warning}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print("ChatGPT zip workflow script validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())




---

# validate-gitignore-convention.py template

Source: `templates/scripts/validate-gitignore-convention.py`

#!/usr/bin/env python3
"""Validate .gitignore conventions for an agent delivery team package.

Usage:
  python3 scripts/validate-gitignore-convention.py
  python3 scripts/validate-gitignore-convention.py path/to/project
"""

from __future__ import annotations

import sys
from pathlib import Path


REQUIRED_PATTERNS = [
    ".chatgpt-zips/",
    "*.zip",
]

RECOMMENDED_PATTERNS = [
    "node_modules/",
    "target/",
    "build/",
    "dist/",
    "coverage/",
    ".next/",
    ".vite/",
    ".gradle/",
    "out/",
    "*.tsbuildinfo",
    ".DS_Store",
]

DANGEROUS_OR_UNWANTED_PATTERNS = [
    "!.chatgpt-zips/",
    "!*.zip",
]


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    gitignore = root / ".gitignore"

    errors: list[str] = []
    warnings: list[str] = []

    if not gitignore.exists():
        errors.append("Missing .gitignore")
    else:
        text = gitignore.read_text(encoding="utf-8", errors="replace")

        for pattern in REQUIRED_PATTERNS:
            if pattern not in text:
                errors.append(f".gitignore missing required pattern: {pattern}")

        for pattern in RECOMMENDED_PATTERNS:
            if pattern not in text:
                warnings.append(f".gitignore missing recommended pattern: {pattern}")

        for pattern in DANGEROUS_OR_UNWANTED_PATTERNS:
            if pattern in text:
                warnings.append(f".gitignore contains pattern that may re-include zip artifacts: {pattern}")

        if "Agent delivery" not in text and "ChatGPT zip" not in text:
            warnings.append(".gitignore does not contain a clearly marked agent-delivery/ChatGPT zip section")

    for warning in warnings:
        print(f"WARN: {warning}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(".gitignore convention validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())




---

# validate-active-work-profiles.py template

Source: `templates/scripts/validate-active-work-profiles.py`

#!/usr/bin/env python3
"""Validate active-work and team-profile files in an agent delivery team package."""

from __future__ import annotations
import sys
from pathlib import Path

REQUIRED_FILES = [
    "docs/active-work.md",
    "docs/feature-plan.md",
    "docs/refactoring-plan.md",
    "docs/bugfix-plan.md",
    "docs/migration-plan.md",
    "docs/team-profiles/general-feature-delivery.md",
    "docs/team-profiles/refactoring.md",
    "docs/team-profiles/bugfix.md",
    "docs/team-profiles/architecture-review.md",
    "docs/team-profiles/migration.md",
]

def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    errors = []
    for rel in REQUIRED_FILES:
        p = root / rel
        if not p.exists():
            errors.append(f"Missing required file: {rel}")
        elif p.stat().st_size == 0:
            errors.append(f"Required file is empty: {rel}")
    active = root / "docs/active-work.md"
    if active.exists():
        text = active.read_text(encoding="utf-8", errors="replace")
        for field in ["Type:", "Team profile:", "Active plan:", "Status:"]:
            if field not in text:
                errors.append(f"docs/active-work.md missing expected field: {field}")
    profiles = root / "docs/team-profiles"
    if profiles.exists():
        for profile in profiles.glob("*.md"):
            text = profile.read_text(encoding="utf-8", errors="replace")
            if "## Rules" not in text:
                errors.append(f"{profile}: missing '## Rules' section")
            if "## Source of truth" not in text and profile.name != "architecture-review.md":
                errors.append(f"{profile}: missing '## Source of truth' section")
    if errors:
        for e in errors:
            print(f"ERROR: {e}", file=sys.stderr)
        return 1
    print("Active work and team profile validation passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())


