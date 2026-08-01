---
run: inline
---

## What it does
- Run mechanical checks by script
- Do judgment checks by reading
- Report every violation
- Never edit the skill
Gotchas: Read-only. The script does deterministic checks: structure, section order, word limits, run field, graph, banned words. The model does judgment checks: bullet-step sync, vague verbs, grounding, scope locks. Two layers, one report.

**In:** path to a skill to check
**Out:** a report of violations, grouped by file

## Steps
1. Read `references/lint-checks.md`, `references/style.md`, `references/step-prompt-rules.md`.
2. Run `scripts/checks.py` on the skill path. Capture the JSON report.
3. Read each step file. Do the judgment checks from `lint-checks.md`. These cover: bullet-step sync, vague verbs, and two tasks in one step. They also cover missing grounding, missing scope locks, and Copilot file paths.
4. Merge the script report and the judgment checks.
5. Report every violation, grouped by file. Do not edit anything.
