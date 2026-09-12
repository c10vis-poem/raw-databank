---
source: CCConvo/You're right,.txt
cleaned: 2026-08-26
converter: none - plain text
---
You're right, and I undersold it — I answered off the fork metadata (`parent: google-research/reasoning-bank`, empty description) without reading what's actually in it. Real answer, from the README:

**It's the reference implementation of exactly the recursive-memory idea you're describing** — "a memory mechanism for agents that learns from both successful and failed trajectories, with reasoning stored as memory content," plus what they call "memory-aware test-time scaling" — using accumulated reasoning memory as a second axis of scaling alongside more inference-time compute. That's squarely in the same territory as the Continual Harness paper Prime Agent is built on, and adjacent to RLVR — it learns from trajectory outcomes, though it's worth being precise: this is **inference-time memory accumulation, not weight updates via verified reward** — so it's RLVR-adjacent in spirit, not literally an RLVR training pipeline.

**What it actually is, practically:** Python research code — `SWE-Bench/` and `WebArena/` directories, evaluation harnesses, needs API keys (OpenAI/Gemini/Claude-on-Vertex) and Docker for WebArena. You'd run it to reproduce their benchmark results or study the approach, not "install" it as a live component in your stack the way OB1 or mem0 would be.

So two things are both true: my "zero collision risk" stands in the narrow sense — no hooks, no MCP server, nothing that touches ECC/Honey/GateGuard — but "nothing to wire, just reference code" undersold what it actually *is*. It's the methodology reference for how a recursive reasoning-memory layer should work, which is a real input into how you'd want mem0/OB1/reasoning-bank-as-a-concept to actually behave, not a component that plugs into the live stack directly.