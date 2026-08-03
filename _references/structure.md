# Structure

Every target skill follows this structure. No exceptions.

## Folder tree

Every step is a folder. The folder holds the step file `<name>/<name>.md`. A step is never a bare file.

```
skill-name/
  SKILL.md
  GLOBAL.md
  _meta/              # skill-writer's own rules, stamped in — see "## Meta" below
    _references/
    _scripts/
  _scripts/           # shared across foo and bar only (optional)
  _references/        # shared across foo and bar only (optional)
  foo/
    foo.md            # the step
    _references/      # foo's own supporting docs (optional)
    _scripts/         # foo's own scripts (optional)
    sub-step-1/       # sub-steps are also folders (optional)
      sub-step-1.md
      _references/
      _scripts/
  bar/
    bar.md
```

Rules:

- Each step is a folder named for the step. Its entry file is `<foldername>.md`.
- A `references/` or `scripts/` folder is always named with a leading underscore: `_references/`, `_scripts/`. This marks it as skill machinery, not a step, and keeps it visually apart from step folders when listing the tree.
- A step's `_references/` and `_scripts/` live inside its own folder by default. A step does not reach into another step's folder.
- A file or script used by only one step lives in that step's own folder. Never duplicate it into a shared folder.
- A file or script used by two or more steps is shared. Put one copy in a `_references/` or `_scripts/` folder at the lowest level that contains every step that uses it. Do not place it higher than that, and do not duplicate it into each step's folder.
- Sub-steps are steps. Same folder rule, same file template. They nest to any depth.
- A parent step's `## Steps` section calls its sub-steps by path.
- `_meta/` is not a step. It never appears in the step table or the flow graph.

## Meta

Every target skill carries its own copy of the rules used to check and patch it, so it needs no dependency on skill-writer being installed. This lives in `_meta/` at the skill root.

```
_meta/
  _references/
    structure.md
    style.md
    principles.md
    step-prompt-rules.md
    lint-checks.md
  _scripts/
    lint_checks.py
```

Rules:

- `build` stamps `_meta/` into every new skill. `refactor` stamps it into every skill missing it.
- Stamp `_meta/` with the script `_scripts/stamp_meta.py` (skill-writer's own root `_scripts/`, shared by `build` and `refactor`). Never hand-copy or retype these files.
- `_meta/` holds a copy, not a symlink. The target skill must work standalone, moved to another machine with no skill-writer installed.
- Re-running the stamp script overwrites `_meta/` with the current rules. It does not touch the rest of the target skill.
- The `## Feedback` patch subagent (see below) reads `_meta/_references/` and runs `_meta/_scripts/lint_checks.py` on itself. It never reaches for skill-writer's own copy.

## SKILL.md template

SKILL.md is thin. It holds only these six things:

1. Frontmatter: `name` and `description`.
2. One line pointing to `GLOBAL.md`.
3. A step table: `order | step | purpose | file`.
4. A flow graph (see below).
5. A `## Manager` section (see below), stamped verbatim.
6. A `## Feedback` section (see below), stamped verbatim.

No instructions. No examples. No how-to. That content lives in step files.

## Flow graph

The flow graph is a plain edge list. Nodes are steps. Grammar:

```
entry: <step>
<a> -> <b>
<a> -> <b> [if <condition>]
<step> -> finish
```

Vocabulary: `entry:`, `finish`, `a -> b`, `a -> b [if <cond>]`. Nothing else.

Every node must resolve to a step file. Every step must be reachable.

## GLOBAL.md template

The target skill's `GLOBAL.md` is thin. Two sections:

```
## Shared knowledge
- <fact every step assumes>

## Running steps
<the dispatch rule — stamped verbatim, see below>
```

`## Shared knowledge` is the only part that varies per skill. Put shared facts here so step files do not repeat them.

`## Running steps` is stamped verbatim into every target skill:

```
To run a step, read its frontmatter `run` field.

- No `run` field, or `run: inline` → follow its steps in this context, same model.
- `run: subagent` → spawn a subagent, same model. Pass its `In`. Capture its `Out`.
- `run: subagent:<model>` → same as subagent, but use `<model>`.

Provide each step's `In`. Expect its `Out` back. For an artifact, `Out` is a file path, not the file body.
```

## Manager

Every skill has a manager. The manager is the human-facing layer. Its context must stay small, because the human may interact with it for days.

The manager is `SKILL.md` itself. Every `SKILL.md` has a `## Manager` section.

Stamp this section verbatim:

```
## Manager

You are the manager. You talk to the human. You do not execute steps.

Hold only:
- the current position in the flow graph
- the human's open decisions
- paths to what steps produced — never the content

On each human message:
1. Map it to the next step in the flow.
2. Dispatch that step. Pass its `In`. (See GLOBAL.md "Running steps".)
3. Take back its `Out` — a path, a status, or a question.
4. Tell the human the result, or ask the next decision.

Never read a produced file into your own context. Keep pointers, not bodies.
Never run a step inline. Always dispatch.
```

Rule: every step must return a small `Out` — a path or a status, not inline content. A step that returns a full document body pollutes the manager's context. That is a violation.

## Feedback

Every skill takes feedback about itself while the human runs it. This is separate from the flow graph. It is how a human reports a bug or a wanted change in the skill, without leaving the run.

Every `SKILL.md` has a `## Feedback` section, placed right after `## Manager`.

Stamp this section verbatim:

```
## Feedback

The human flags a problem with this skill by writing `/manager <text>` at any point in a run.

On `/manager <text>`:
1. Do not interpret `<text>` yourself. Do not edit anything inline.
2. Dispatch one subagent, `run: subagent`. Pass it:
   - the feedback text
   - the path to this skill
   - the current run's state: which step was active, and its `In`/`Out` so far
3. The subagent has two jobs, both in the same dispatch:
   - Fix the current run: redo the affected step's output so this run is correct.
   - Fix the skill: edit the step file or script that caused the problem, so future runs do not repeat it. Read `_meta/_references/` for the rules. Follow them. Run `_meta/_scripts/lint_checks.py` on this skill before returning. Fix what it flags.
4. Take back the subagent's `Out` — a short status, not the edited content.
5. Tell the human the status. Resume the flow graph at the position held before the interruption.

Never read the subagent's edits into your own context. Keep the status, not the body.
```

Rule: the patch subagent must change only the skill's own files, or the current run's in-progress output. It must not change unrelated steps. It must preserve the skill's existing behavior except for what the feedback describes.

## Step file template

```
---
run: inline
---

## What it does
- verb phrase
- verb phrase
- verb phrase
Gotchas: <optional — one or two lines. How it works. Traps.>

**In:** <what it needs, or "none">
**Out:** <a path, a value, or "none">

## Steps
1. <imperative instruction>
2. <imperative instruction>

## <optional named section>
<content the Steps section references by heading>
```

Rules for the step file:

- `run` is the only frontmatter field. Omit it for inline. Values: `inline`, `subagent`, `subagent:<model>`.
- `## What it does` is for the human, not the runtime. It is maintainer notes: what the step does, how it works, traps. Treat it as a comment. Never follow it as an instruction.
- `## What it does` is 75 words or less. 3 to 6 bullets. Bullets stay tight. `Gotchas` is optional.
- `## What it does` must stay in sync with `## Steps`. `## Steps` is the source of truth. If they drift, fix the bullets to match the steps.
- `**In:**` and `**Out:**` are the calling contract. For an artifact, `Out` is a path.
- `## Steps` holds the real instructions. Keep them minimal. Follow `style.md` and `step-prompt-rules.md`.
- Extra named sections are allowed. Each must be referenced by `## Steps`. No orphan sections.
