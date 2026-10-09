# Step prompt rules

A step's `## Steps` section is a prompt. A Claude model reads it and acts. Write it so it works on the first try.

These rules apply to every step that a model reads.

First, find the surface that reads the step. Then apply that surface's rules. Infer the surface from context: the `run` mode, whether the target skill runs in Claude Code, and whether the step writes an artifact for GitHub Copilot.

## All Claude surfaces

- Be explicit. Claude follows instructions literally. Missing context gives narrow output, not a smart guess.
- State the output format and length.
- For output a human reads, add "Be terse."
- Give the reason when the reason changes what the reader does.
- Do not add "think step by step". Claude calibrates thinking depth by itself.
- Do not over-engineer. Add: "Make only the change asked for. Do not add features or refactor."
- For a factual step, ground it: "State only what you can verify. If unsure, say so. Do not invent facts or citations."

## Claude Code steps

Apply the rules above, plus:

- Anchor scope to a path. Name the files and directories the step may touch.
- Add stop conditions. Name the actions that must pause for a human.
- Add human-review triggers for destructive actions: delete a file, add a dependency, change a schema.
- Add a progress checkpoint: after each step, output the result.
- Name the tools to use when needed. Example: "Read all files in /src/auth/ before you start."

## GitHub Copilot steps

The step authors a prompt that Copilot reads. Apply File-Scope discipline:

- Give the exact file path and the function or component name.
- Describe input types, return type, and edge cases.
- State what the code must not do.
- Name the current behavior and the wanted behavior.
- State the done condition.

## Check

`lint` flags on any non-script step:

- Vague task verb.
- Two tasks in one step (split into sub-steps).
- No concrete `Out`.
- No format or length.
- A factual step with no grounding rule.
- A Claude Code step with no scope lock or no stop condition.
- A Copilot step with no file path or no "must not do" list.
