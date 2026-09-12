# Unresolved (global)

Durable, cross-service backlog — not scoped to any one repo. Numbered, chronological
oldest→newest, no priority ranking (each repo's `RESUME.md` decides what's pertinent
for its own session). Items get added, resolved-and-removed, or explicitly kept here
across many sessions and many repos — this file is never rewritten wholesale the way
a `RESUME.md` is.

This is its real, permanent home: this repo (novae-xorpus) **is** #dumbass
(Database & Universal Memory Bank Across Split Services) — the universal memory/
housekeeping system, not a stand-in for it. Briefly lived at bare `~/unresolved.md`
before this repo was confirmed as the actual pre-dumbass foundation (2026-08-31);
that location is now dead, don't write there.

Each item is tagged with the repo/service it originated from, since this file now
spans more than one.

1. **[aesop-xi]** Tailscale install — status unknown as of the 2026-07-17 session
   (not installed then). Never re-checked since.
2. **[aesop-xi]** T3 infrastructure (Jetson Orin Nano, Rubik Pi) — on hold, needs
   hardware not yet procured. Deploy scripts already written and committed
   (`deploy/jetson/`, `deploy/rubik-pi/`), ready to run once hardware exists.
3. **[aesop-xi]** Clone `obsidian-skills` into `~/vault` — never done.
   `git clone https://github.com/c10vis-poem/obsidian-skills ~/vault/.claude/skills/obsidian-skills`
4. **[aesop-xi]** `notebooklm` proot+VNC login — the VNC approach here predates the
   no-VNC DroidDesk direction decided 2026-08-29. `~/.notebooklm/` exists but has
   never actually authenticated (empty `profiles/` dir, confirmed 2026-08-28). Needs
   a login path that doesn't depend on VNC, or explicit sign-off that VNC-based
   login is fine for this one-time setup step even though DroidDesk itself won't
   use VNC.
5. **[aesop-xi]** OpenWiki fork: upstream checkpointer PR — unclear if still wanted.
   The fork (`c10vis-poem/openwiki`, branch `claude/wiki-quinn-npu-local-m1crql`)
   has since diverged with its own real NPU/voice work (local llama-server
   provider, TTS markdown-strip fix, proot voice-sid fix) — the original "just
   submit a PR upstream" framing may no longer fit what this fork has become.
6. **[aesop-xi]** Open architectural decisions, never finalized:
   - Auditor: in-stack-isolated vs. strictly out-of-band (leaning cloud GLM-5.2)
   - Recall + Strategic memory: share one vector backend (namespaces) or stay separate
   - Home executive binds to Jetson vs. phone Qwen (per profile)
7. **[aesop-xi]** HTTP/WebSocket server for the voice engine — explicitly deferred
   past the 2026-08-31 session. See `aesop-voice-pipeline` skill's "Extension
   points still open." No server exists yet; `ARCHITECTURE.md` already spec'd it
   (Flask/FastAPI wrapping `VoiceEngine`).
8. **[aesop-xi]** OmniRoute / OB1 / ReasoningBank routing — see `ARCHITECTURE.md`
   §10 in aesop-xi. Genuinely unresolved, not just undocumented: how OB1 relates to
   OmniRoute's real SQLite hybrid vector store, whether "episodic" is a distinct
   5th memory type, and whether Postgres+vector's actual role is continuous recall
   or a post-training evaluation store. Needs a real design decision before
   anything gets built against it.
9. **[global / Claude Code]** Universal skill placement pattern — `obsidian-skills`
   proves the working model (plugin installed from a `directory` marketplace
   source pointing at its own repo, not copied into `~/.claude/skills/`). Worth
   applying the same pattern to graphify / notebooklm-py / honey-for-devs if the
   goal is tool-agnostic skills usable by more than just Claude Code.
10. **[aesop-xi]** Real remote work merged in at end of session, never reviewed:
    a bridge daemon (`deploy/phone/bridge/aesopd.py`), a supervised `llamad`
    daemon with actual NPU/Hexagon accelerator offload (`deploy/phone/daemons/`),
    `protocol/bridge-protocol.md`, and a `termux-helper` skill — 6 commits that
    existed on the remote (`origin/claude/wiki-quinn-npu-local-m1crql`) with zero
    local visibility until the end-of-session push was rejected and force a pull.
    Directly relevant to Task 5 (salvaging an APK as terminal daemon / NPU-manager
    microagent) — read this before starting that task, it may already be most of
    the way there.
11. **[global]** MASTER-SKILLS.md — same aggregation pattern as MASTER-RESUME.md/
    MASTER-CLAUDE.md, but for every attached project's `skills/*/SKILL.md`.
    Explicitly "eventually," not urgent, per the operator (2026-08-31). Needs a
    design call before building: full-content concatenation (matches the other
    two masters) vs. an index table (name/description/project/path) — skills are
    typically much longer than a RESUME.md, so concatenation may be the wrong
    shape here even though it's the established pattern. Also needs a
    `projects/<name>/skills` directory-symlink added alongside the existing
    RESUME.md/CLAUDE.md file symlinks before the hook can walk it.
12. **[global]** ECC's `unified-memory` skill (ECC Memory Vault: markdown-first,
    project/team/user scopes, cross-harness) vs. the hand-built #dumbass approach —
    ECC itself is now installed and configured (2026-08-31: plugin at user scope,
    hooks at standard profile, `common`/`python`/`kotlin` rule packs copied to
    `~/.claude/rules/ecc/`), so this is no longer "should we install it," it's
    "should novae-xorpus adopt or fold into the vault instead of continuing to
    hand-build the same thing." Real design decision, not yet made.
13. **[aesop-xi]** ECC dashboard-on-tablet via SSH tunnel — steps given
    (2026-08-31: `sshd` started on phone, port 8022, password still needs setting
    via `passwd`; tunnel command given: `ssh -L 3456:127.0.0.1:3456 -p 8022
    u0_a538@<phone-LAN-IP> `, then browse `http://127.0.0.1:3456` on the tablet
    while `npm run dashboard:web` runs on the phone) — never confirmed working.
    Phone's LAN IP (`172.20.20.20` as of this session) can change on reconnect.
