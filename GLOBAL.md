# GLOBAL

## Shared knowledge

These facts apply to every entry point in this skill.

- This skill authors other skills. The skill you author is the "target skill".
- The target skill is built from steps. A step is one unit of a workflow. The target skill runs its own steps. The human does not run steps.
- Rules this skill applies live in `references/`. Read them when a step tells you to.
- `references/structure.md` — the folder tree and file templates every target skill must follow.
- `references/style.md` — how to write step prose (Simplified Technical English).
- `references/principles.md` — the coding principles applied to skills.
- `references/step-prompt-rules.md` — how to write step instructions as prompts for Claude models.
- `references/lint-checks.md` — the full check list.

## Running steps

To run a step, read its frontmatter `run` field.

- No `run` field, or `run: inline` → follow its steps in this context, same model.
- `run: subagent` → spawn a subagent, same model. Pass its `In`. Capture its `Out`.
- `run: subagent:<model>` → same as subagent, but use `<model>`.
- `run: script` → run its script. No model. Capture its `Out`.

Provide each step's `In`. Expect its `Out` back. For an artifact, `Out` is a file path, not the file body.
