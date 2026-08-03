---
run: inline
---

## What it does
- Check path for an existing skill
- Grill user on the workflow
- Scaffold folders and files
- Split work into steps
- Move mechanical steps to scripts
- Add the manager to SKILL.md
Gotchas: One entry point for new skills and for adding steps. It decides by reading the path. A skill exists if the path has a `SKILL.md`. Grill with no question limit, one at a time, with a recommendation each time. Every skill gets a manager in SKILL.md.

**In:** target path, and a rough idea of the skill
**Out:** path to the built or updated skill

## Steps
1. Read `_references/structure.md`, `_references/style.md`, `_references/principles.md`, and `_references/step-prompt-rules.md`.
2. Check the target path. If it has a `SKILL.md`, this is an update. If not, this is a new skill.
3. Grill the user. Ask one question at a time. Give a recommended answer each time. Ask as many as needed. See `## Grill topics`.
4. Plan the steps. Name each step. Write the flow graph. Get user approval.
5. For a new skill: scaffold the tree from `structure.md`. Write `SKILL.md` and `GLOBAL.md`. Stamp `## Running steps` verbatim.
6. Add the `## Manager` and `## Feedback` sections to `SKILL.md`, in that order. Stamp both verbatim from `structure.md`. Make sure every step returns a small `Out` — a path or a status, not inline content.
7. For an update: add or edit the step folders. Update the step table and flow graph in `SKILL.md`.
8. For each step, run the scriptification check in `principles.md`. Move mechanical work to a script. Run the script once on a sample to confirm it works.
9. Write each step file to the template. Apply `style.md` and `step-prompt-rules.md`.
10. Run `_scripts/stamp_meta.py <target skill path>`. This copies skill-writer's rules into the target skill's `_meta/`, so it needs no dependency on skill-writer at patch time.
11. Run `lint` on the result. Fix what it flags.
12. Return the skill path.

## Grill topics
- What the skill does, and when it should trigger.
- The steps, in order. Which are optional. Which branch.
- What each step needs (`In`) and returns (`Out`).
- Which steps are cheap or mechanical. These become `subagent:<model>`, or a script the step calls.
- The surface each step runs on: claude.ai, Claude Code, or GitHub Copilot.
- The shared facts for `GLOBAL.md`.
