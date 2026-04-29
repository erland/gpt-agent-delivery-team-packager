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
