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
