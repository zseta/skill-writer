---
name: skill-writer
description: "Build, refactor, and lint agent skills. Use this whenever the user wants to create a new skill, add or edit steps in an existing skill, restructure a skill to be thinner and cleaner, check a skill for problems, or convert a rough workflow into a proper skill. Trigger on any mention of making a skill, editing a skill, a SKILL.md file, skill steps, or 'turn this into a skill' — even if the user does not say the word 'skill-writer'."
---

# skill-writer

Builds skills that follow one structure and one style. Read `GLOBAL.md` first.

## Entry points

The user invokes one of these. Grill the user first (see each step). Ask one question at a time. Give a recommended answer each time. Ask as many questions as needed.

| Entry point | Purpose | File |
|---|---|---|
| build | Inspect the target path. Scaffold a new skill, or add/edit steps in an existing one. | build/build.md |
| refactor | Plan, get approval, then rewrite an existing skill to comply. Shortens prose. | refactor/refactor.md |
| lint | Read-only. Report violations. Never edits. | lint/lint.md |

## Flow

```
entry: pick
pick -> build [if new skill or adding steps]
pick -> refactor [if reshaping an existing skill]
pick -> lint [if only checking]
build -> finish
refactor -> finish
lint -> finish
```

If intent is unclear, ask the user which entry point they want.
