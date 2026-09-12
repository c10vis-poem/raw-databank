---
checker: tools/check.py
checked: 2026-08-27
sources_checked: 94
reports_written: 94
---

# 03-check — the RLVR pass

One report per source. `FINDINGS.jsonl` has every finding, machine-readable.

The checker shares no code and no method with `tools/clean.py`. Different
extractor per format (`pypdf`, stdlib `zipfile`+`xml.etree`, stdlib
`html.parser`) and a different comparison (containment of named atoms and
order-sensitive segments in a fold-and-squash character stream, plus an exact
`difflib` line audit where extraction is byte-faithful). No word frequencies.
No percentages. Hard rule 5 is satisfied.

## Result

| verdict | files |
|---|---|
| PASS | 44 |
| PASS + UPSTREAM DEFECT | 22 |
| PASS WITH WARNINGS | 22 |
| PASS WITH WARNINGS + UPSTREAM DEFECT | 4 |
| FAIL | 1 |
| NO-COUNTERPART | 1 |

| findings | count |
|---|---|
| FAIL — fused token | 7 |
| FAIL — no counterpart | 1 |
| UPSTREAM — source truncated | 26 |
| WARN — respaced value | 77 |
| WARN — stray byte-order mark | 21 |

## Everything that is not a clean pass

| source | verdict | fails | warnings | upstream | report |
|---|---|---|---|---|---|
| `AESOP_XI_/Four Core Buckets.txt.txt` | PASS WITH WARNINGS | 0 | 1 | 0 | [report](03-check/AESOP_XI_/four-core-buckets-txt.check.md) |
| `AESOP_XI_/How Your Forked Repos (The MCP Tools) Move into the APK.txt` | PASS WITH WARNINGS | 0 | 1 | 0 | [report](03-check/AESOP_XI_/how-your-forked-repos-the-mcp-tools-move-into-the-apk.check.md) |
| `AESOP_XI_/Local-first code intelligence graph..txt` | PASS WITH WARNINGS | 0 | 1 | 0 | [report](03-check/AESOP_XI_/local-first-code-intelligence-graph.check.md) |
| `AESOP_XI_/Red Agent file systems layout..txt` | PASS WITH WARNINGS | 0 | 1 | 0 | [report](03-check/AESOP_XI_/red-agent-file-systems-layout.check.md) |
| `AESOP_XI_/Why You Need an MCP Host (The Bridge).txt` | PASS WITH WARNINGS | 0 | 1 | 0 | [report](03-check/AESOP_XI_/why-you-need-an-mcp-host-the-bridge.check.md) |
| `AESOP_XI_/deploy∕T3-BRINGUP.md.txt` | PASS WITH WARNINGS | 0 | 1 | 0 | [report](03-check/AESOP_XI_/deploy-t3-bringup-md.check.md) |
| `App_Builders_Guide_/Building inside of Google.txt` | PASS WITH WARNINGS | 0 | 1 | 0 | [report](03-check/App_Builders_Guide_/building-inside-of-google.check.md) |
| `CCConvo/And yeah I.txt` | PASS + UPSTREAM DEFECT | 0 | 0 | 1 | [report](03-check/CCConvo/and-yeah-i.check.md) |
| `CCConvo/Last task.txt` | PASS + UPSTREAM DEFECT | 0 | 0 | 1 | [report](03-check/CCConvo/last-task.check.md) |
| `CCConvo/NovÆgenti.txt` | PASS + UPSTREAM DEFECT | 0 | 0 | 1 | [report](03-check/CCConvo/novaegenti.check.md) |
| `CCConvo/Phase one.txt` | PASS + UPSTREAM DEFECT | 0 | 0 | 1 | [report](03-check/CCConvo/phase-one.check.md) |
| `CCConvo/Repo breakdown.txt` | PASS WITH WARNINGS + UPSTREAM DEFECT | 0 | 1 | 1 | [report](03-check/CCConvo/repo-breakdown.check.md) |
| `CCConvo/So these other.txt` | PASS + UPSTREAM DEFECT | 0 | 0 | 1 | [report](03-check/CCConvo/so-these-other.check.md) |
| `CCConvo/That reminds.txt` | PASS + UPSTREAM DEFECT | 0 | 0 | 1 | [report](03-check/CCConvo/that-reminds.check.md) |
| `CCConvo/That's one of.txt` | PASS + UPSTREAM DEFECT | 0 | 0 | 1 | [report](03-check/CCConvo/that-s-one-of.check.md) |
| `CCConvo/This is Horizons now .txt` | PASS + UPSTREAM DEFECT | 0 | 0 | 1 | [report](03-check/CCConvo/this-is-horizons-now.check.md) |
| `CCConvo/Well I would.txt` | PASS + UPSTREAM DEFECT | 0 | 0 | 1 | [report](03-check/CCConvo/well-i-would.check.md) |
| `CCConvo/Yeah that's.txt` | PASS + UPSTREAM DEFECT | 0 | 0 | 1 | [report](03-check/CCConvo/yeah-that-s.check.md) |
| `Llm wiki/## Part 1 Llm Wiki.txt.docx.txt` | PASS WITH WARNINGS | 0 | 1 | 0 | [report](03-check/Llm%20wiki/part-1-llm-wiki-txt-docx.check.md) |
| `Llm wiki/1..txt` | PASS + UPSTREAM DEFECT | 0 | 0 | 1 | [report](03-check/Llm%20wiki/1.check.md) |
| `Llm wiki/System Mapping.txt` | PASS + UPSTREAM DEFECT | 0 | 0 | 1 | [report](03-check/Llm%20wiki/system-mapping.check.md) |
| `Llm wiki/Unified ecosystem analysis..txt` | PASS WITH WARNINGS | 0 | 1 | 0 | [report](03-check/Llm%20wiki/unified-ecosystem-analysis.check.md) |
| `Llm wiki/Why do you.txt` | PASS + UPSTREAM DEFECT | 0 | 0 | 1 | [report](03-check/Llm%20wiki/why-do-you.check.md) |
| `Llm wiki/wiki marcor obsidian.txt` | PASS + UPSTREAM DEFECT | 0 | 0 | 1 | [report](03-check/Llm%20wiki/wiki-marcor-obsidian.check.md) |
| `Llm wiki/wiki on desktop.txt` | PASS + UPSTREAM DEFECT | 0 | 0 | 1 | [report](03-check/Llm%20wiki/wiki-on-desktop.check.md) |
| `Llm wiki/wiki on mobile.txt` | PASS + UPSTREAM DEFECT | 0 | 0 | 1 | [report](03-check/Llm%20wiki/wiki-on-mobile.check.md) |
| `NovA-Corpus Diagnostic.pdf` | PASS WITH WARNINGS | 0 | 1 | 0 | [report](03-check/nova-corpus-diagnostic.check.md) |
| `Nova Corpus — Device Stack.html` | FAIL | 7 | 0 | 0 | [report](03-check/nova-corpus-device-stack.check.md) |
| `ORIGINAL-DIRECTIONS-2026-08-18.md` | PASS + UPSTREAM DEFECT | 0 | 0 | 1 | [report](03-check/original-directions-2026-08-18.check.md) |
| `SKILLS.md/GitHub_Docs_SKILL.txt` | PASS WITH WARNINGS | 0 | 1 | 0 | [report](03-check/SKILLS.md/github-docs-skill.check.md) |
| `SKILLS.md/technical-builder-style.skill.zip` | NO-COUNTERPART | 1 | 0 | 0 | [report](03-check/SKILLS.md/technical-builder-style.skill.zip.check.md) |
| `TERMUX/Copy of  tmux.pdf` | PASS WITH WARNINGS | 0 | 8 | 0 | [report](03-check/TERMUX/copy-of-tmux.check.md) |
| `Three-APK Architecture (v1).pdf` | PASS + UPSTREAM DEFECT | 0 | 0 | 1 | [report](03-check/three-apk-architecture-v1.check.md) |
| `Three-APK Architecture (v2).pdf` | PASS WITH WARNINGS + UPSTREAM DEFECT | 0 | 1 | 1 | [report](03-check/three-apk-architecture-v2.check.md) |
| `architecture-edits/EDIT-Clarifying Clean Text to skills and tools plus outdated architecture (Drive text extract, RED FORMATTING LOST).txt` | PASS + UPSTREAM DEFECT | 0 | 0 | 1 | [report](03-check/architecture-edits/edit-clarifying-clean-text-to-skills-and-tools-plus-outdated-architecture-drive-text-extract-red-formatting-lost.check.md) |
| `continual-harness/Continual Harness (Google Doc export).txt` | PASS WITH WARNINGS | 0 | 1 | 0 | [report](03-check/continual-harness/continual-harness-google-doc-export.check.md) |
| `continual-harness/Continual Harness- Online Adaptation for Self-Improving Foundation Agents 2605.09998v1.pdf` | PASS WITH WARNINGS | 0 | 59 | 0 | [report](03-check/continual-harness/continual-harness-online-adaptation-for-self-improving-foundation-agents-2605-09998v1.check.md) |
| `continual-harness/XContinual_Harnessl.txt` | PASS WITH WARNINGS | 0 | 1 | 0 | [report](03-check/continual-harness/xcontinual-harnessl.check.md) |
| `novaexopia-vincet/NovÆcopia Vincet.txt` | PASS WITH WARNINGS | 0 | 1 | 0 | [report](03-check/novaexopia-vincet/novaecopia-vincet.check.md) |
| `part1-lex/## Part 1- Lex (1) (Drive text extract, truncated).txt` | PASS WITH WARNINGS + UPSTREAM DEFECT | 0 | 1 | 1 | [report](03-check/part1-lex/part-1-lex-1-drive-text-extract-truncated.check.md) |
| `recursive-training/Nova Corpus — Device Stack.pdf` | PASS WITH WARNINGS | 0 | 8 | 0 | [report](03-check/recursive-training/nova-corpus-device-stack.check.md) |
| `universal-memory/TRAINING/Page - Purpose - Key evidence sources (Google Doc export).txt` | PASS + UPSTREAM DEFECT | 0 | 0 | 1 | [report](03-check/universal-memory/TRAINING/page-purpose-key-evidence-sources-google-doc-export.check.md) |
| `whyyoucodevoicelikeass/Fixitnowpaigow.txt` | PASS WITH WARNINGS | 0 | 1 | 0 | [report](03-check/whyyoucodevoicelikeass/fixitnowpaigow.check.md) |
| `whyyoucodevoicelikeass/Untitled document.txt` | PASS WITH WARNINGS + UPSTREAM DEFECT | 0 | 1 | 1 | [report](03-check/whyyoucodevoicelikeass/untitled-document.check.md) |
| `whyyoucodevoicelikeass/in order to bypass the memory killer.txt` | PASS WITH WARNINGS | 0 | 1 | 0 | [report](03-check/whyyoucodevoicelikeass/in-order-to-bypass-the-memory-killer.check.md) |
| `whyyoucodevoicelikeass/local voice layer .txt` | PASS + UPSTREAM DEFECT | 0 | 0 | 1 | [report](03-check/whyyoucodevoicelikeass/local-voice-layer.check.md) |
| `whyyoucodevoicelikeass/no shit Sherlock..txt` | PASS WITH WARNINGS | 0 | 1 | 0 | [report](03-check/whyyoucodevoicelikeass/no-shit-sherlock.check.md) |
| `whyyoucodevoicelikeass/whyyoubreaknofix.pdf` | PASS + UPSTREAM DEFECT | 0 | 0 | 1 | [report](03-check/whyyoucodevoicelikeass/whyyoubreaknofix.check.md) |
| `whyyoucodevoicelikeass/whyyounocodegoodai.txt` | PASS WITH WARNINGS | 0 | 1 | 0 | [report](03-check/whyyoucodevoicelikeass/whyyounocodegoodai.check.md) |
| `whyyoucodevoicelikeass/youfixitnowgwilo.txt` | PASS WITH WARNINGS | 0 | 1 | 0 | [report](03-check/whyyoucodevoicelikeass/youfixitnowgwilo.check.md) |
