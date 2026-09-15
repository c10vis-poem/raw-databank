---
source: CCConvo/Got it — Open.txt
cleaned: 2026-08-26
converter: none - plain text
---
Got it — Open Interpreter, not Open Route. That's a different job than the routing question, so let me answer both parts cleanly.

**Part 1 — which forks actually do swarm orchestration.** Five real hits, verified:

| your fork | upstream | what it actually is |
|---|---|---|
| `NovA-orca` | `stablyai/orca` | ADE for running a fleet of parallel agents — agent-agnostic, works with any coding agent |
| `Novus-ringer` | `NateBJones-Projects/ringer` | Parallel AI-agent swarm orchestrator, plus a mission-control HUD |
| `NovA-crewAI` | `crewAIInc/crewAI` | Role-playing collaborative agents — you define roles, they work together |
| `poem-langflow` | `langflow-ai/langflow` | Visual drag-and-drop builder for agent workflows |
| `Novus-openinterpreter` | `openinterpreter/openinterpreter` | Not swarm orchestration — lets one model execute code/actions on your local machine |

Four real orchestrators, one thing that's actually a different category (local code execution, not multi-agent coordination).

**Part 2 — the actual architecture question.** You're conflating two separate layers, and separating them answers both halves of what you asked:

**Layer A — which backend serves an inference call.** This is `LocalAI`'s job: it exposes your local weights over an OpenAI-compatible API, so anything that can point at a custom base URL (Prime Agent included — it has its own custom-provider support) can call your local GGUF files as if they were a cloud model. `OmniRoute` sits in front of *that* — it's a router deciding which backend handles a given call: your local weights via LocalAI, or Anthropic's API for Claude, or whatever else. So the real chain is **Prime Agent → OmniRoute → (LocalAI for local weights, or Claude's API for Claude)**. LocalAI is the thing that makes your local weights reachable at all; OmniRoute is what picks between it and everything else.

**Layer B — which agent handles which piece of a task.** This is Orca/Ringer/CrewAI territory, and it's also literally AESOP XI's job description from a minute ago — "decides which harness runs which task." So no, AESOP isn't competing with Orca/Ringer/CrewAI, and it doesn't need to reinvent what they already do. The honest answer: **AESOP is the protocol; one of these is the plumbing AESOP runs on.** AESOP defines *what* should happen and *who* decides; Orca or Ringer or CrewAI is the actual mechanism that moves control and state between agents when it does. Given how you described AESOP earlier — "uses Prime Agent to do X" — that's CrewAI's exact paradigm (define roles, they collaborate), which makes it the closest fit if you want AESOP built on top of something rather than from scratch.

**Does it benefit from LocalAI?** Yes, directly — it's the missing piece that turns "I have local weights" into "anything in my stack can actually call them." Without it, Prime Agent and OmniRoute have no clean way to reach your local models at all.

So the full stack, correctly separated: **AESOP XI (protocol) → running on CrewAI or Orca or Ringer (the swarm plumbing) → directing harnesses (Prime Agent, Claude Code+ECC) → which call out through OmniRoute (the router) → to either LocalAI (your weights) or Claude's API → with MCP servers as the tools any of them can reach for.** That's five distinct layers doing five distinct jobs, not five things competing for the same one.