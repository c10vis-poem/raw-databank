---
source: CCConvo/Good catch,.txt
cleaned: 2026-08-26
converter: none - plain text
---
Good catch, because the term is genuinely a trap here — it means two different things depending on which system you're in.

**In general industry usage** (and how I used it a moment ago): **harness = the runtime, the actual engine.** Claude Code is a harness. Prime Agent is a harness. That's your second option — the tool that executes, calls the model, runs the loop, invokes tools. When I said "harness/agent stack," I meant the engines: Claude Code (with ECC/GateGuard layered on top of it) and Prime Agent, as a category.

**The rules/protocols/scripts that define direction** — AESOP XI, `CLAUDE.md`, `SKILL.md` files, GateGuard's fact-forcing rules — that's not usually called "the harness" in general usage. That's closer to *config*, *protocol*, or *system prompt* layer. That's your first option.

**Here's the trap: Prime Agent's own docs reuse the word for the opposite thing.** Their README names their durable-memory/prompt-refinement component **"Continual Harness"** — and by their own definition, that's specifically the *rules/state layer*: "supplemental prompts, memories, skill descriptions, and reusable subagent specifications... that Prime Agent can refine." In their branding, the engine itself is called "a persistent Python control environment" (the RLM/REPL), and "harness" is reserved for the rules/memory sitting inside it. So Prime Agent's proper-noun "Continual Harness" is your *first* category, wearing the name usually used for the second.

So, concretely, mapped onto your actual stack:

- **Engines** (general-sense "harness"): Claude Code, Prime Agent
- **Rules/protocol layer**: AESOP XI, `CLAUDE.md`/`SKILL.md`, GateGuard's rules, and — confusingly — Prime Agent's own "Continual Harness" subsystem also belongs here, not in the engine category despite the name

When I said "harness" earlier I meant the engines. If you want, I'll default to saying "engine" for the runtime and "harness" only for Prime Agent's specific rules-layer component going forward, so it stops being ambiguous between the two of us.