The sorting phase is always the messiest part of building a local AI architecture. When you are staring down a massive pile of unstructured files, the trick is to stop thinking about *what* the file is, and start thinking about *how* the agent is going to use it.

Here is your triage matrix. When you pick up a file, run it through these four rules to figure out exactly where it belongs in your new Termux/Snapdragon setup.

## The Triage Matrix

| The Bucket | File Format | Storage Location | The Sorting Rule |
| :-: | :-: | :-: | :-: |
| **1. The Cold Archive** | Raw .pdf, heavy manuals, untouched code | Google Drive / Deep Local Storage | **Is it heavy and unedited?** If an agent would have to waste context window space searching through it to find a single answer, it stays here. You only retrieve these when you need to re-summarize a missing concept. |
| **2. The Obsidian Vault** | Human-readable .md | Master Wiki Vault | **Does it explain why?** This is for project goals, architecture decisions, and conceptual summaries. If a human needs to read it to understand a system, or if the agent needs broad context on what you are trying to achieve, it goes here. |
| **3. The Almanac (Glossary)** | .jsonl lines | Local Device (Fast Cache) | **Is it a raw fact or parameter?** Hardware specs, QAIRT compilation flags, specific shell commands, and API endpoints. If the agent needs to instantly inject a specific fact into the terminal without reading a paragraph, it gets chopped into the JSONL. |
| **4. The Inference Skills** | SKILL.md (Agent instructions) | Local ~/.claude/skills/ or repo | **Is it a verb?** If the file describes an action the agent needs to execute (e.g., "how to run an Unsloth conversion" or "how to query the JSONL"), it must become a Skill. |

## Setting Up the SKILL.md Layer

Since you mentioned turning your model runtimes and inference scripts into a "skill MD," you need to know exactly how agents (like Claude Code or OpenClaw) actually read these files.

There is a standardized open specification for Agent Skills. If you format your files correctly now, your local agents will be able to load and execute them perfectly on your Termux setup.

Every skill must live in its own folder, and the file *must* be named SKILL.md. It requires two parts: YAML metadata at the top, and Markdown instructions below.

Here is exactly how you should format one of your inference skills:

```markdown
---
name: run-qairt-inference
description: Executes local model inference using the QAIRT toolchain on the Snapdragon 8 Elite. Use when the user asks to test a model or run local inference.
---

# QAIRT Inference Protocol

When the user asks you to run inference, follow these exact steps in the Termux environment:

1. **Verify Environment:** Check that the GenieX stack is active.
2. **Set Parameters:** Ensure batch size is 1 and precision is INT8.
3. **Execute:** Run `sh /data/data/com.termux/files/usr/bin/run_qairt.sh --model <model_path>`

Do not attempt to use standard Linux paths. Always use the Termux synthetic root.
```

The name must match the folder name exactly, and the description is the most critical part — that is the "trigger" the agent reads to decide if it should activate the skill.
</content>
