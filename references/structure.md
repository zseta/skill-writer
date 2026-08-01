# Structure

Every target skill follows this structure. No exceptions.

## Folder tree

Every step is a folder. The folder holds the step file `<name>/<name>.md`. A step is never a bare file.

```
skill-name/
  SKILL.md
  GLOBAL.md
  foo/
    foo.md            # the step
    references/       # foo's supporting docs (optional)
    scripts/          # foo's scripts (optional)
    sub-step-1/       # sub-steps are also folders (optional)
      sub-step-1.md
      references/
      scripts/
  bar/
    bar.md
```

Rules:

- Each step is a folder named for the step. Its entry file is `<foldername>.md`.
- A step's `references/` and `scripts/` live inside its own folder. There is no skill-wide `references/` or `scripts/`.
- Sub-steps are steps. Same folder rule, same file template. They nest to any depth.
- A parent step's `## Steps` section calls its sub-steps by path.

## SKILL.md template

SKILL.md is thin. It holds only these four things:

1. Frontmatter: `name` and `description`.
2. One line pointing to `GLOBAL.md`.
3. A step table: `order | step | purpose | file`.
4. A flow graph (see below).

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
- `run: script` → run its script. No model. Capture its `Out`.

Provide each step's `In`. Expect its `Out` back. For an artifact, `Out` is a file path, not the file body.
```

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

- `run` is the only frontmatter field. Omit it for inline. Values: `inline`, `subagent`, `subagent:<model>`, `script`.
- `## What it does` is for the human, not the runtime. It is maintainer notes: what the step does, how it works, traps. Treat it as a comment. Never follow it as an instruction.
- `## What it does` is 130 words or less. 3 to 6 bullets. Bullets stay tight. `Gotchas` is optional.
- `## What it does` must stay in sync with `## Steps`. `## Steps` is the source of truth. If they drift, fix the bullets to match the steps.
- `**In:**` and `**Out:**` are the calling contract. For an artifact, `Out` is a path.
- `## Steps` holds the real instructions. Keep them minimal. Follow `style.md` and `step-prompt-rules.md`.
- Extra named sections are allowed. Each must be referenced by `## Steps`. No orphan sections.
