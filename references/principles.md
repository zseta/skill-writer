# Principles

Apply these coding principles to skills. Each one is a rule, not theory.

## KISS

Keep every step minimal. Include only the instructions the step needs. Cut the rest. This is the style rules in `style.md`.

## DRY

Do not repeat a rule across step files. Put the shared fact in the target skill's `GLOBAL.md` under `## Shared knowledge`. Step files assume it.

## Abstraction

SKILL.md shows what each step does. It hides how. The how lives in the step file. SKILL.md is a router: pointer + step table + flow graph.

## Wrappers

A step may be a thin wrapper. It sets `run` and calls a shared step or script. It does not copy the shared logic.

## Polymorphism

Use one step with an input, not many near-duplicate steps. Example: one `export` step that takes a format, not `export-pdf` plus `export-docx`.

## Encapsulation

A step owns its files. Its `references/` and `scripts/` live in its own folder. Steps do not reach into another step's folder.

## Scriptification

Find step work that is deterministic. Move it to a script.

- Deterministic work: parsing, transforming, file I/O, validation, formatting. Fixed algorithm. Same input gives same output.
- Judgment work: reading intent, writing content, deciding. This stays as prose instructions.

When a step is fully mechanical:

1. Write a script in the step's `scripts/` folder.
2. Set the step `run: script`.
3. The `## Steps` section calls the script, passes `In`, captures `Out`.
4. Run the script once on a sample. Confirm it works before you finish. (Generate and verify.)

Reason: a script costs fewer tokens than prose plus generic tool calls. It is also more reliable.
