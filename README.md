# skill-writer

An agent skill that builds, refactors, and lints other agent skills.

It enforces a standardized structure and style on every skill it produces: a thin `SKILL.md` router, a `GLOBAL.md` for shared knowledge, and steps as self-contained folders. It writes step instructions in Simplified Technical English, moves mechanical work into scripts and fixes itself if you find an issue later.

## Benefits of using skill-writer

### Built-in self-healing
When you are using a skill produced by skill-writer and you experience issues with the skill, just call `/meta <problem you're experiencing>` and it will spawn a sub agent to fix the problem real-time so you can continue whatever you are working on. If the skill lives in a git repo with a remote, the sub agent also commits and pushes the fix.

### Consistent structure across skills
Every skill it produces follows the same layout: a thin `SKILL.md` router, a `GLOBAL.md` for shared knowledge, and steps as self-contained folders. Once you understand skill-writer structure, you know how to navigate all of them.

### Prefer deterministic scripts
Deterministic work — parsing, transforming, file I/O, validation, formatting — is moved into scripts instead of left as prose instructions. Scripts run the same way every time and cost fewer tokens than prose plus generic tool calls.


## What it does

Three entry points:

- **build** — Inspect a target path. Scaffold a new skill, or add and edit steps in an existing one. Grills you first, one question at a time.
- **refactor** — Plan a restructure of an existing skill, get your approval, then rewrite it to comply. Shortens verbose prose.
- **lint** — Read-only. Report every violation. Never edits.

### Example usage:
```
Use skill-writer to build a skill that deploys my app
```
or 
```
Use skill-writer to refactor skills/my-skill
```

or 
```
Use skill-writer to lint skills/my-skill
```

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


## Structure

```
skill-writer/
  SKILL.md              # router: pointer, step table, flow graph, Manager, Feedback
  GLOBAL.md             # shared knowledge + dispatch rule
  build/build.md        # entry point: build
  refactor/refactor.md  # entry point: refactor
  lint/
    lint.md             # entry point: lint
    _scripts/checks.py  # mechanical lint checks
  _scripts/
    stamp_meta.py        # copies _references/ + the lint script into a target skill's _meta/
  _references/          # the rules the skill applies
    structure.md        # folder tree and file templates
    style.md            # Simplified Technical English rules
    principles.md       # KISS, DRY, scriptification, etc.
    step-prompt-rules.md# prompt rules for Claude, Claude Code, Copilot
    lint-checks.md      # the full check list
```

