---
source: CCConvo/Good — enough.txt
cleaned: 2026-08-26
converter: none - plain text
---
Good — enough to give you the real answer now. Only one MCP server is actually registered right now: `code-review-graph`. Everything else is dormant until wired.

**Direct answer on Honey vs. reverse-skill: no contradiction.** Honey compresses code and prose; `reverse-skill` is a security-tooling router (Burp MCP, Kali tooling, CTF sandbox) — different layers entirely, one's about how much you say, the other's about what tools get invoked. The one place they'd touch is if Honey's terseness ever tried to compress a pentest report or exploit writeup — Honey's own carve-out list exempts "anything you explicitly asked for," so a deliberately detailed security finding stays detailed. No fight there.

**Real findings, the concrete kind:**

**1. `reverse-skill` ships its own `burp-mcp-full/` — a real MCP server.** If you eventually run this alongside `code-review-graph` (also MCP) and anything else that registers a server, the actual collision risk isn't philosophical, it's **naming**: two servers claiming the same key in `~/.claude.json`'s `mcpServers`, or two local daemons trying to bind the same port. Right now only `code-review-graph` is registered, so there's no live collision yet — but check server names before wiring a second one in.

**2. OmniRoute binds `localhost:20128`** and exposes its own 37-tool MCP server. That's a second MCP surface. No conflict with the one currently registered, different name — but it's the same category of thing, worth tracking as you add more.

**3. `claude-video` is not an MCP server or a hook at all** — it's a `/watch` command that downloads, extracts frames, and transcribes. No collision surface with anything on your list. Fine as-is.

**4. `reasoning-bank`'s real upstream is `google-research/reasoning-bank`** — that's Google's own research repo, reference code for a paper, not a running service or plugin. Zero collision risk; nothing to wire.

**5. Prime Agent isn't in Honey's supported-agent list.** Honey's installer explicitly targets Claude Code, Codex, Cursor, Copilot, Gemini CLI, Windsurf, Cline, OpenClaw, Kiro, Kilo, Hermes — Prime Agent isn't one of them. Prime Agent is also its own separate harness process, not a layer inside Claude Code, so this isn't really a collision — Honey just won't follow you in there. If you want Prime Agent terse too, that's a separate, manual setup, not something this installer does for you.

**6. GateGuard and Honey actively cooperate, not compete.** GateGuard forces me to write out 4 facts before a destructive/write action. Honey's own carve-out list explicitly exempts "deletes" and "migrations" from compression. So Honey shouldn't touch the fact-presentation at all — that's exactly the kind of output its own rules protect.

**One thing I don't have full visibility into:** whether `mem0`, OB1, `reasoning-bank`(if you fork it live), and `code-review-graph` would all try to claim overlapping MCP server names if wired simultaneously — I haven't inspected mem0's or OB1's actual server config yet. That's worth a real check at the point you actually wire two memory backends together, not now while they're all still dormant.