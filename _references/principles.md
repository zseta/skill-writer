# Principles

Apply these coding principles to skills. Each one is a rule, not theory.

## KISS

Keep every step minimal. Include only the instructions the step needs. Cut the rest. This is the style rules in `style.md`.

## DRY

Do not repeat a rule across step files. Put the shared fact in the target skill's `GLOBAL.md` under `## Shared knowledge`. Step files assume it.

Before adding a rule to any `_references/*.md` file read the other files in that same `_references/` folder first. If the rule already exists there, point to it instead of restating it.


## Abstraction

SKILL.md shows what each step does. It hides how. The how lives in the step file. SKILL.md is a router: pointer + step table + flow graph.

## Encapsulation

A step owns its files. Its `_references/` and `_scripts/` live in its own folder. Steps do not reach into another step's folder. The leading underscore marks these as skill machinery, not a step folder.

When two or more steps need the same file or script, do not duplicate it into each step's folder. Put one shared copy in a `_references/` or `_scripts/` folder at the lowest level that contains all steps that use it. Example: if `build` and `refactor` both call the same script, the shared `_scripts/` folder sits next to `build/` and `refactor/`, not inside either one. A shared folder is scoped to its level: only steps at or below that level may use it. It is still a violation to place a shared folder above the lowest common level, or to let a step reach into a sibling step's private folder.

## Scriptification

Find step work that is deterministic. Move it to a script.

- Deterministic work: parsing, transforming, file I/O, validation, formatting. Fixed algorithm. Same input gives same output.
- Judgment work: reading intent, writing content, deciding. This stays as prose instructions.

When a step is fully mechanical:

1. Write a script in the step's `_scripts/` folder.
2. The `## Steps` section calls the script, passes `In`, captures `Out`.
3. Run the script once on a sample. Confirm it works before you finish. (Generate and verify.)

Reason: a script costs fewer tokens than prose plus generic tool calls. It is also more reliable.
