---
source: universal-memory/1. Well I need to plan all this shit for later This....pdf
cleaned: 2026-08-26
converter: pymupdf get_text()
source_pages: 2
---
That STT slip ("Santa Claus tree") is fantastic! Before getting to the workflow, here are the "A" 
words that fit an encyclopedia/glossary/recall reference: 
●​ Almanac: A detailed, structured compendium of data, tables, and reference facts. 
●​ Archive: A permanent, indexed repository of raw records and data. 
●​ Atlas: A visual map or organized domain framework (like a "Knowledge Atlas"). 
●​ Ancillary (Index): A supporting, quick-lookup reference attached to a main vault. 
●​ Phonetic STT guess: If you spoke "a Santa Claus tree," your voice parser might have 
mangled "a syntax tree," "an archive tree," or "a directory tree." 
Regardless of the name, your 5-layer knowledge pipeline is a solid architecture for local LLM 
recall and contextual indexing. 
The 5-Layer Knowledge Architecture 
To keep your files organized, fast, and accessible across local scripts, Obsidian, and LLM 
repositories, structure your data into these distinct functional tiers: 
Tier 1: Raw Source Layer (/raw_pdf/) 
●​ Format: .pdf / Raw Docs 
●​ Role: The untouchable source of truth. Heavy, unedited reference manuals, research 
papers, and technical specs. 
●​ Storage: Stored in deep local storage or Google Drive. You rarely feed these raw files 
directly to an LLM due to context weight. 
Tier 2: Conceptual Wiki Layer (/wiki_md/) 
●​ Format: .md (Markdown) 
●​ Role: Consolidated, human-readable summaries and briefs. 
●​ Target: Obsidian Vault / LLM Wiki repo. 
●​ Structure: Uses strict internal linking ([[links]] or relative paths) so both you and an LLM 
can traverse concepts without reading 50-page PDFs. 
Tier 3: High-Speed Machine Caches (/recall_jsonl/) 
●​ Format: .jsonl (JSON Lines) 
●​ Role: Structured, line-delimited metadata optimized for instantaneous parsing by 
on-device agents and local scripts. 
●​ Structure: Each line is a self-contained record:​
JSON​
{"id": "doc_001", "topic": "QAIRT_conversion", "summary": "...", "source_pdf": "specs/qairt.pdf", 
"wiki_link": "wiki/qairt.md"}​
 
Tier 4: Execution & Runtimes (/repos/ & /scripts/) 
●​ Format: .sh, .py, codebases 
●​ Role: The actual working code, model conversion scripts, shell loops, and active 
toolchains. 

●​ Rule: Scripts should point to Tier 3 (.jsonl) or Tier 2 (.md) for their configuration and 
reference data rather than hardcoding paths. 
Tier 5: The Master "Almanac" / Index (INDEX.jsonl or MAP.md) 
●​ Format: Single root file or global database line-map 
●​ Role: The glue that bridges Tiers 1 through 4. It maps every raw PDF to its corresponding 
Markdown wiki summary, its JSONL cache offset, and the specific script repo that 
executes it. 
Why This Pipeline Works 
1.​ Speed: When your local agent needs to recall facts, it scans the Tier 3 JSONL file in 
milliseconds without needing to read heavy Markdown files or parse PDFs. 
2.​ Context Preservation: When you need deep reasoning in a chat interface or Obsidian, 
you point the agent to the Tier 2 Markdown brief. 
3.​ Traceability: If the summary feels incomplete, the Tier 5 Index gives you the exact line 
number and source PDF path to inspect. 
 
 
