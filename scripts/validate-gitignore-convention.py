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
