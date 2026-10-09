---
name: skill-writer
description: "Build, refactor, and lint agent skills: create a new skill, edit its steps, restructure it cleaner, check it for problems, or convert a workflow into one. Trigger on any mention of a skill, SKILL.md, or skill steps."
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

## Manager

You are the manager. You talk to the human. You do not execute steps. Be terse.

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

## Feedback

The human flags a problem with this skill by writing `/meta <text>` at any point in a run.

On `/meta <text>`:
1. Do not interpret `<text>` yourself. Do not edit anything inline.
2. Dispatch one subagent, `run: subagent`. Pass it:
   - the feedback text
   - the path to this skill
   - the current run's state: which step was active, and its `In`/`Out` so far
3. The subagent has three jobs, all in the same dispatch:
   - Fix the current run: redo the affected step's output so this run is correct.
   - Fix the skill: edit the step file or script that caused the problem, so future runs do not repeat it. Read `_meta/_references/` for the rules. Follow them. Run `_meta/_scripts/lint_checks.py` on this skill before returning. Fix what it flags.
   - Push the fix: if this skill is in a git repo with a remote, commit only the files it changed. Push to the current branch. If there is no remote, skip this job. Never force-push. If the push fails, report the error.
4. Take back the subagent's `Out` — a short status and the push result, not the edited content.
5. Tell the human the status. Resume the flow graph at the position held before the interruption.

Never read the subagent's edits into your own context. Keep the status, not the body.
