#!/usr/bin/env python3
"""Mechanical lint checks for a target skill.

Checks the deterministic rules: folder structure, section order,
What-it-does word/bullet limits, run-field validity, flow-graph
resolution and reachability, banned words, long sentences.

Judgment checks (sync of bullets vs steps, vague verbs, missing
grounding, scope locks) are done by the model, not here.

Usage: python checks.py <skill_dir>
Output: JSON report to stdout.
"""
import json
import re
import sys
from pathlib import Path

RUN_RE = re.compile(r"^(inline|subagent|subagent:[a-z0-9.\-]+)$")
BANNED = ["carefully", "simply", "just ", "please", "make sure to",
          "utilize", "leverage", "initiate", "commence", "terminate",
          "regarding", "concerning", "facilitate"]
REQUIRED_SECTIONS = ["## What it does", "**In:**", "**Out:**", "## Steps"]


def find_steps(skill_dir):
    """A step is a folder containing <name>/<name>.md."""
    steps = {}
    for p in skill_dir.rglob("*.md"):
        if p.name in ("SKILL.md", "GLOBAL.md"):
            continue
        if p.parent.name == p.stem:
            steps[p.stem] = p
    return steps


def check_frontmatter_run(text):
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.S)
    if not m:
        return None  # no frontmatter -> inline, valid
    for line in m.group(1).splitlines():
        line = line.strip()
        if line.startswith("run:"):
            val = line.split(":", 1)[1].strip()
            if not RUN_RE.match(val):
                return f"invalid run value: {val}"
    return None


def check_what_it_does(text):
    issues = []
    m = re.search(r"## What it does\s*\n(.*?)(\n##|\n\*\*In:\*\*)", text, re.S)
    if not m:
        return ["missing '## What it does' section"]
    block = m.group(1)
    words = len(block.split())
    if words > 130:
        issues.append(f"What it does is {words} words (max 130)")
    bullets = [l for l in block.splitlines() if l.strip().startswith("-")]
    if not (3 <= len(bullets) <= 6):
        issues.append(f"What it does has {len(bullets)} bullets (need 3-6)")
    return issues


def check_sections(text):
    positions = []
    for s in REQUIRED_SECTIONS:
        m = re.search(r"^" + re.escape(s), text, re.M)
        if not m:
            return [f"missing required section: {s}"]
        positions.append(m.start())
    if positions != sorted(positions):
        return ["required sections out of order"]
    return []


def check_banned(text):
    low = text.lower()
    return [f"banned word: {w.strip()}" for w in BANNED if w in low]


def check_long_sentences(text):
    # crude: sentences in Steps section
    m = re.search(r"## Steps\s*\n(.*)", text, re.S)
    if not m:
        return []
    out = []
    for line in m.group(1).splitlines():
        line = re.sub(r"^\s*\d+\.\s*", "", line).strip()
        if not line:
            continue
        for sent in re.split(r"[.!?]", line):
            n = len(sent.split())
            if n > 20:
                out.append(f"long sentence ({n} words): {sent.strip()[:50]}")
    return out


def parse_graph(skill_md):
    nodes, edges, entry = set(), [], None
    m = re.search(r"```(.*?)```", skill_md, re.S)
    if not m:
        return nodes, edges, entry, "no flow graph found"
    for line in m.group(1).splitlines():
        line = line.strip()
        if line.startswith("entry:"):
            entry = line.split(":", 1)[1].strip()
            nodes.add(entry)
        elif "->" in line:
            a, b = line.split("->", 1)
            a = a.strip()
            b = re.sub(r"\[if.*?\]", "", b).strip()
            nodes.add(a)
            nodes.add(b)
            edges.append((a, b))
    return nodes, edges, entry, None


def check_graph(skill_dir, steps):
    skill_md = (skill_dir / "SKILL.md")
    if not skill_md.exists():
        return ["no SKILL.md"]
    nodes, edges, entry, err = parse_graph(skill_md.read_text())
    if err:
        return [err]
    issues = []
    for n in nodes:
        if n in ("finish",):
            continue
        if n not in steps and n != entry:
            if n not in steps:
                issues.append(f"graph node has no step file: {n}")
    # reachability
    reach, frontier = set(), [entry] if entry else []
    adj = {}
    for a, b in edges:
        adj.setdefault(a, []).append(b)
    while frontier:
        cur = frontier.pop()
        if cur in reach:
            continue
        reach.add(cur)
        frontier.extend(adj.get(cur, []))
    for s in steps:
        if s not in reach:
            issues.append(f"step not reachable from entry: {s}")
    return issues


def check_skill_md(skill_dir):
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return ["no SKILL.md"]
    text = skill_md.read_text()
    issues = []
    if not re.search(r"^## Manager", text, re.M):
        issues.append("SKILL.md missing '## Manager' section")
    return issues


def main():
    skill_dir = Path(sys.argv[1])
    report = {"skill": str(skill_dir), "issues": {}}
    steps = find_steps(skill_dir)
    report["steps_found"] = sorted(steps)

    for name, path in steps.items():
        text = path.read_text()
        step_issues = []
        rv = check_frontmatter_run(text)
        if rv:
            step_issues.append(rv)
        step_issues += check_sections(text)
        step_issues += check_what_it_does(text)
        step_issues += check_banned(text)
        step_issues += check_long_sentences(text)
        if step_issues:
            report["issues"][name] = step_issues

    graph_issues = check_graph(skill_dir, steps)
    if graph_issues:
        report["issues"]["_graph"] = graph_issues

    skill_issues = check_skill_md(skill_dir)
    if skill_issues:
        report["issues"]["_skill_md"] = skill_issues

    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
