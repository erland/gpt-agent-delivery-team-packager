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
