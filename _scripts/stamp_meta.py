#!/usr/bin/env python3
"""Stamp _meta/ into a target skill.

Copies the rules a target skill needs to check and patch itself,
with no dependency on skill-writer being installed:
- _references/: structure.md, style.md, principles.md,
  step-prompt-rules.md, lint-checks.md
- _scripts/lint_checks.py: the mechanical lint checker

Used by both `build` and `refactor`. Safe to run again: it overwrites
_meta/ with the current rules, it does not touch the rest of the
target skill.

Usage: python stamp_meta.py <target_skill_dir>
Output: JSON status to stdout.
"""
import json
import shutil
import sys
from pathlib import Path

SKILL_WRITER_ROOT = Path(__file__).resolve().parent.parent
REFERENCE_FILES = [
    "structure.md",
    "style.md",
    "principles.md",
    "step-prompt-rules.md",
    "lint-checks.md",
]


def main():
    target_dir = Path(sys.argv[1]).resolve()
    if not target_dir.is_dir():
        print(json.dumps({"status": "error", "reason": f"not a directory: {target_dir}"}))
        sys.exit(1)

    meta_dir = target_dir / "_meta"
    ref_dir = meta_dir / "_references"
    scripts_dir = meta_dir / "_scripts"
    ref_dir.mkdir(parents=True, exist_ok=True)
    scripts_dir.mkdir(parents=True, exist_ok=True)

    copied = []
    for name in REFERENCE_FILES:
        src = SKILL_WRITER_ROOT / "_references" / name
        dst = ref_dir / name
        shutil.copyfile(src, dst)
        copied.append(str(dst.relative_to(target_dir)))

    src_script = SKILL_WRITER_ROOT / "lint" / "_scripts" / "checks.py"
    dst_script = scripts_dir / "lint_checks.py"
    shutil.copyfile(src_script, dst_script)
    copied.append(str(dst_script.relative_to(target_dir)))

    print(json.dumps({"status": "ok", "meta_dir": str(meta_dir.relative_to(target_dir)), "copied": copied}, indent=2))


if __name__ == "__main__":
    main()
