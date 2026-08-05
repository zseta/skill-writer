# Lint checks

The full check list. `lint` reports these. `build` and `refactor` fix them.

## Structure

- SKILL.md holds only: frontmatter, the `GLOBAL.md` pointer, the step table, the flow graph, `## Manager`, `## Feedback`. Anything else is a violation.
- Every step is a folder with `<name>/<name>.md`. A bare step file is a violation.
- A `references/` or `scripts/` folder without a leading underscore is a violation. Use `_references/` and `_scripts/`.
- A folder that is not a step folder, `_references/`, `_scripts/`, or (skill root only) `_meta/` is a violation, even if underscore-prefixed (`_cli/`, `_layouts/`, ...).
- A step's `_references/` and `_scripts/` live in its own folder, unless shared. A file used by only one step must live in that step's own folder, not a shared one.
- A shared `_references/` or `_scripts/` folder sits at the lowest level that contains every step using it. A shared folder placed higher than that, or duplicated across steps instead of shared, is a violation.
- `GLOBAL.md` holds only `## Shared knowledge` and `## Running steps`.
- `## Running steps` matches the stamped dispatch rule.
- Every `SKILL.md` has a `## Manager` section, stamped verbatim.
- Every `SKILL.md` has a `## Feedback` section, stamped verbatim, right after `## Manager`.
- Every target skill has `_meta/_references/` (all five files) and `_meta/_scripts/lint_checks.py`. Missing or incomplete `_meta/` is a violation.
- Every step's `Out` is a path or a status, not inline content.

## Flow graph

- Every graph node resolves to a step file.
- Every step is reachable from `entry`.
- The graph uses only the allowed grammar.

## Step file

- Required sections in order: `## What it does`, `**In:**`, `**Out:**`, `## Steps`.
- `## What it does` is 130 words or less, 3 to 6 bullets.
- `## What it does` is in sync with `## Steps`.
- `**Out:**` is a path when the step makes an artifact.
- Extra sections are referenced by `## Steps`. No orphan sections. No broken references.
- `run` field is valid: absent, `inline`, `subagent`, or `subagent:<model>`.

## Style (see style.md)

- Sentences over 20 words (soft flag).
- Banned hedge words.
- Fancy words with a simple swap.
- Paragraphs where a list fits.

## Principles (see principles.md)

- A rule repeated across step files (move to `GLOBAL.md`).
- A mechanical step that should be a script.

## Step prompts (see step-prompt-rules.md)

- Vague task verb.
- Two tasks in one step.
- No concrete `Out`.
- No format or length.
- Factual step with no grounding.
- Claude Code step with no scope lock or stop condition.
- Copilot step with no file path or "must not do" list.
