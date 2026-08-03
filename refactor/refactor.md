---
run: inline
---

## What it does
- Read the existing skill
- Run lint to find violations
- Plan the restructure
- Get user approval
- Rewrite to the rules
- Shorten verbose prose
Gotchas: Plan first. Get approval before you rewrite. Never invent behavior — reshape and shorten what is there. If a step is unclear, flag it, do not guess. `## Steps` is the source of truth when bullets and steps disagree.

**In:** path to an existing skill
**Out:** path to the refactored skill

## Steps
1. Read `_references/structure.md`, `_references/style.md`, `_references/principles.md`, `_references/step-prompt-rules.md`, and `_references/lint-checks.md`.
2. Read the whole skill.
3. Run `lint`. List every violation.
4. Write a plan. Show how you will split content into steps, what moves to `GLOBAL.md`, what becomes a step or a script.
5. Show the plan to the user. Get approval. Do not edit before approval.
6. Copy the skill to a writable location if the source is read-only.
7. Rewrite to the structure in `structure.md`. Preserve behavior. Do not add behavior. Add `## Manager` and `## Feedback` to `SKILL.md` if either is missing, stamped verbatim, in that order.
8. Shorten verbose prose to meet `style.md`.
9. Run the scriptification check. Move mechanical steps to scripts. Verify each script on a sample.
10. Fix drift: where `## What it does` and `## Steps` disagree, rewrite the bullets to match the steps.
11. Run `_scripts/stamp_meta.py <target skill path>`. This copies skill-writer's current rules into the target skill's `_meta/`, replacing any stale copy.
12. Run `lint` again. Fix what it flags.
13. Return the skill path.
