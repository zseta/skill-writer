# skill-writer

An agent skill that builds, refactors, and lints other agent skills.

It enforces a standardized structure and style on every skill it produces: a thin `SKILL.md` router, a `GLOBAL.md` for shared knowledge, and steps as self-contained folders. It writes step instructions in Simplified Technical English, moves mechanical work into scripts, and checks its output against a fixed rule set.

## What it does

Three entry points:

- **build** — Inspect a target path. Scaffold a new skill, or add and edit steps in an existing one. Grills you first, one question at a time.
- **refactor** — Plan a restructure of an existing skill, get your approval, then rewrite it to comply. Shortens verbose prose.
- **lint** — Read-only. Report every violation. Never edits.

To use it after install, ask Claude to build, refactor, or lint a skill — for example: "Use skill-writer to build a skill that deploys my app" or "Lint this skill folder."

## Requirements

- A paid Claude plan (Pro, Max, Team, or Enterprise).
- Code execution turned on (the `lint` step runs a Python script).

## Install

### Claude.ai (web or desktop)

1. Download `skill-writer.zip` from this repository. The zip must contain the `skill-writer/` folder at its root, with `SKILL.md` inside that folder.
2. Open Claude and go to **Settings → Capabilities → Skills** (also shown as **Customize → Skills** in some versions).
3. Click **Upload skill** and select `skill-writer.zip`.
4. Claude reads `SKILL.md` and shows the skill name and description. The skill is now active.

Skills you upload here are available in both Claude Chat and Cowork — they share one personal skill library.

### Claude Code

Copy the skill folder into your skills directory, then restart.

Personal install (available in every project on your machine):

```bash
mkdir -p ~/.claude/skills
cp -r skill-writer ~/.claude/skills/
```

Project install (available only in the current project):

```bash
mkdir -p .claude/skills
cp -r skill-writer .claude/skills/
```

Restart Claude Code. Run `/skills` to confirm `skill-writer` loaded.

### GitHub Copilot

Copilot agent mode reads the same SKILL.md format. Copy the folder into a skills directory Copilot scans — `.github/skills/` (project, shared with your team through the repo), `.claude/skills/`, or `.agents/skills/`.

```bash
mkdir -p .github/skills
cp -r skill-writer .github/skills/
```

Start a new Copilot session. Copilot loads the skill based on its description, or you can name it in your prompt.

Note: the `lint` step runs a Python script. It works where Copilot can run code (agent mode, CLI). In review-only contexts with no code execution, the mechanical checks are skipped and only the judgment checks run.

### Claude API

Upload the skill through the Skills API. See the Skills API quickstart in the Claude Platform docs.

## One folder, every agent

The `skill-writer` folder is portable. The same folder works in Claude.ai, Claude Code, and GitHub Copilot with no changes — they all read the SKILL.md format. Copy it to whichever skills directory your agent scans.

This applies to the skills `skill-writer` produces too. It writes step instructions tuned to the surface that runs them — claude.ai, Claude Code, or GitHub Copilot — so a skill you build here can target any of the three.

## Structure

```
skill-writer/
  SKILL.md              # router: pointer, step table, flow graph
  GLOBAL.md             # shared knowledge + dispatch rule
  build/build.md        # entry point: build
  refactor/refactor.md  # entry point: refactor
  lint/
    lint.md             # entry point: lint
    scripts/checks.py   # mechanical lint checks
  references/           # the rules the skill applies
    structure.md        # folder tree and file templates
    style.md            # Simplified Technical English rules
    principles.md       # KISS, DRY, scriptification, etc.
    step-prompt-rules.md# prompt rules for Claude, Claude Code, Copilot
    lint-checks.md      # the full check list
```

## Troubleshooting

- **Skill does not appear after upload.** Confirm the zip has the `skill-writer/` folder at its root with `SKILL.md` inside — not `SKILL.md` alone at the zip root.
- **Skill never triggers.** The description controls triggering. It is written to trigger on any mention of making, editing, or checking a skill. If it still does not fire, ask for it by name: "Use skill-writer to …".
- **In Claude Code, the skill did not load.** Run `/skills` to check. Restart Claude Code after adding files.
- **The lint step fails.** Confirm code execution is on and Python is available in the environment.
