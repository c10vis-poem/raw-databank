# OB1 ("Open Brain") — Repository Reference

Source: `/home/user/OB1`. Category: **memory layer** (the actual working memory backend of the three repos surveyed) + **skills** taxonomy precedent.

## 1. What it is

Open Brain is pitched as "the infrastructure layer for your thinking" — one Supabase database + pgvector, one MCP protocol, any AI client, no SaaS middleware chains. Explicitly not a notes app: "a database with vector search and an open protocol" so every AI tool (Claude, ChatGPT, Cursor, Claude Code, whatever ships next) shares one persistent memory. Created by Nate B. Jones, with Matt Hallett as first community admin.

`CLAUDE.md` frames this repo as the *community layer* on top of a core Open Brain setup — extensions/recipes/schemas/dashboards/integrations/skills that plug into one canonical `thoughts` table. FSL-1.1-MIT licensed (source-available, no-commercial-derivative-works, converts to MIT after a time delay).

`CONTRIBUTING.md` is the actual constitution: defines what goes in each folder, required files (`README.md` + `metadata.json`), a metadata JSON-schema, an automated PR-review bot (`.github/workflows/ob1-review.yml`), and a non-technical contribution path (mentors turn plain-language ideas into PRs for non-coders, crediting them as `author`).

## 2. Repo structure

| Folder | Nature | Contents |
|---|---|---|
| `extensions/` | Curated, ordered (6 builds, "the learning path") | `household-knowledge` → `home-maintenance` → `family-calendar` → `meal-planning` → `professional-crm` → `job-hunt`. Each: README.md, metadata.json, schema.sql, index.ts (Deno/Supabase Edge Function MCP server), deno.json, .env.example. `extensions/_template/AGENT_SPEC.md` is a machine-readable generator spec for scaffolding new ones. |
| `primitives/` | Curated, README-only | Reusable concept guides referenced by 2+ extensions: `rls`, `shared-mcp`, `remote-mcp`, `deploy-edge-function`, `troubleshooting`. |
| `recipes/` | Open, ~30 folders | Data importers (chatgpt/perplexity/obsidian-vault/x-twitter/instagram/google-activity/grok-export/journals-blogger/email-history import) + workflow/tooling (auto-capture, panning-for-gold, claudeception, schema-aware-routing, daily-digest, life-engine, live-retrieval, content-fingerprint-dedup, local-ollama-embeddings, ob-graph, repo-learning-coach, research-to-decision-workflow, vercel-neon-telegram, work-operating-model-activation, source-filtering, infographic-generator). |
| `schemas/` | Open, sparse | Only `schemas/workflow-status/migration.sql` is real; README says "none yet — contributions welcome" for a listing table. |
| `dashboards/` | Open frontend templates | `open-brain-dashboard` (SvelteKit, MCP proxy + Supabase auth) and `open-brain-dashboard-next` (Next.js, 9 pages: Dashboard, Workflow/Kanban, Browse, Detail, Search, Add-to-Brain smart ingest, Audit, Duplicates, Login). |
| `integrations/` | Open | `slack-capture`, `discord-capture`, `kubernetes-deployment` (fully self-hosted K8s + Postgres/pgvector, no Supabase). |
| `skills/` | Open, plain-text | `SKILL.md`/`*.skill.md` packs: `auto-capture`, `claudeception`, `panning-for-gold`, `competitive-analysis`, `financial-model-review`, `deal-memo-drafting`, `research-synthesis`, `meeting-synthesis`, `heavy-file-ingestion`, `work-operating-model`, `autodream-brain-sync`, `n-agentic-harnesses`, `weekly-signal-diff`. |
| `docs/` | — | `01-getting-started.md` (45-min setup walkthrough), `02-companion-prompts.md`, `03-faq.md`, `04-ai-assisted-setup.md`, `05-tool-audit.md` (MCP context/tool-surface-area management). |
| `resources/` | — | Official packaged exports/companion skill bundles (`.skill`/`.zip`). |
| `server/index.ts` + `server/deno.json` | — | The canonical core MCP server, distributed from repo root. |

## 3. The core `thoughts` table

```sql
create table thoughts (
  id uuid default gen_random_uuid() primary key,
  content text not null,
  embedding vector(1536),
  metadata jsonb default '{}'::jsonb,
  created_at timestamptz default now(),
  updated_at timestamptz default now()
);
```
Indexes: HNSW on `embedding` (`vector_cosine_ops`) for ANN similarity, GIN on `metadata` for filtering, btree on `created_at desc`. RLS enabled, `service_role`-only policy. A later migration adds `content_fingerprint TEXT` (SHA-256, unique partial index) plus an `upsert_thought()` RPC for idempotent dedup-on-write. `metadata jsonb` carries all classification: `type` (`observation|task|idea|reference|person_note`), `topics[]`, `people[]`, `action_items[]`, `dates_mentioned[]`, `source`.

**Guard rail**: never alter/drop existing `thoughts` columns or modify the core MCP server — additive changes only (`schemas/workflow-status/migration.sql` shows the sanctioned extension pattern: adds `status` + `status_updated_at`, never touches existing columns).

## 4. MCP — remote-only, hard rule

MCP servers **must** be Supabase Edge Functions (Deno + Hono + `@modelcontextprotocol/sdk` + `StreamableHTTPTransport`) — never `StdioServerTransport`, never wired via `claude_desktop_config.json`. Connection happens through each client's custom-connector UI (URL + key).

Canonical implementation `server/index.ts`: Hono app wrapping an `McpServer` with 4 tools — `search_thoughts`, `list_thoughts`, `thought_stats`, `capture_thought` — auth via `x-brain-key` header or `?key=` query param against `MCP_ACCESS_KEY`, CORS preflight, documented workaround for Claude Desktop connectors' `Accept` header quirk. Every extension replicates this exact skeleton per `extensions/_template/AGENT_SPEC.md`.

`primitives/remote-mcp/README.md` documents per-client connection recipes (Claude Desktop, ChatGPT Developer Mode, `claude mcp add --transport http`, Cursor native `url` field, `supergateway`/`mcp-remote` bridges for stdio-only clients) — warns `mcp-remote` triggers OAuth discovery that breaks against Supabase's simple key auth; use `supergateway --streamableHttp` instead.

`docs/05-tool-audit.md` discusses MCP context economics directly relevant to a websocket/frontend layer aggregating many tools: 150-400 tokens/tool definition, tool-search deferred-loading, routing misfires past ~10 tools.

## 5. Embeddings / pgvector / RAG flow

**Write path** (`capture_thought`): text → parallel OpenRouter calls for (a) `text-embedding-3-small` embedding (1536-dim) and (b) `gpt-4o-mini` JSON-mode metadata extraction → `upsert_thought()` RPC (SHA-256 fingerprint dedup, merges metadata into existing row on conflict) → embedding column updated in a second write.

**Read path** (`search_thoughts`): query text → OpenRouter embedding → `match_thoughts(query_embedding, match_threshold, match_count, filter jsonb)` RPC does `1 - (embedding <=> query_embedding)` cosine similarity ordered/limited, optional jsonb `@>` metadata filter, default threshold 0.7 (server default 0.5).

`list_thoughts`/`thought_stats` do plain Postgres filtering over `metadata` (no embedding) for recency/keyword browsing. Dedup pattern documented separately in `recipes/content-fingerprint-dedup/README.md` (normalize → SHA-256 → `ON CONFLICT` upsert; battle-tested to 75,000+ thoughts across 9 import sources). `recipes/local-ollama-embeddings` offers a local-model alternative to OpenRouter embeddings. `recipes/live-retrieval/README.md` closes the retrieval loop proactively — a Claude Code skill that fires `search_thoughts`/`list_thoughts` on topic-shift detection during active work sessions, logging hit/miss to `.claude/live-retrieval-log.jsonl` ("Every recipe writes in. This one reads back.").

## 6. Taxonomy: extensions vs primitives vs recipes vs skills

From `CONTRIBUTING.md`'s "What Goes Where":
- **Extensions** = curated, ordered, full progressive builds (schema + MCP server + guide) requiring maintainer sign-off.
- **Primitives** = curated concept documentation only, extracted once 2+ extensions need the same pattern.
- **Recipes** = open, standalone, no-ordering capability builds — full setup guides/schema changes/automation wiring/end-to-end implementations. Can declare `requires_skills`.
- **Skills** = open, smaller, plain-text portable prompt/behavior packs — the canonical reusable unit recipes should depend on rather than re-embedding.

Maps directly onto a "skill / memory / project reference" content model: `skills/` ≈ reusable behavior layer, `thoughts` table + `recipes/schemas` ≈ memory/data layer, `extensions/primitives` ≈ curated project-reference/pattern layer.

## 7. Dashboards / frontend precedent

`open-brain-dashboard-next` (Next.js 16/React 19/Tailwind 4) talks to a separate REST gateway (`open-brain-rest` Edge Function, not the MCP server directly) via `/search`, `/capture`, `/stats`, `/duplicates`; uses `iron-session` encrypted cookies; includes a drag-and-drop Kanban "Workflow" board (`@dnd-kit`) built on the `schemas/workflow-status` migration, semantic-duplicate resolution UI, and a "smart ingest" auto-router (short text → single capture, long text → extraction with dry-run preview) — a concrete precedent for a websocket/frontend layer over a memory backend.

## Key file paths
- `/home/user/OB1/CLAUDE.md`, `/home/user/OB1/README.md`, `/home/user/OB1/CONTRIBUTING.md`, `/home/user/OB1/LICENSE.md`
- `/home/user/OB1/docs/01-getting-started.md`, `/home/user/OB1/docs/05-tool-audit.md`
- `/home/user/OB1/server/index.ts`
- `/home/user/OB1/schemas/workflow-status/migration.sql`
- `/home/user/OB1/extensions/household-knowledge/schema.sql`, `/home/user/OB1/extensions/_template/AGENT_SPEC.md`
- `/home/user/OB1/primitives/remote-mcp/README.md`
- `/home/user/OB1/integrations/slack-capture/README.md`, `/home/user/OB1/integrations/discord-capture/README.md`
- `/home/user/OB1/recipes/content-fingerprint-dedup/README.md`, `/home/user/OB1/recipes/live-retrieval/README.md`
- `/home/user/OB1/skills/README.md`, `/home/user/OB1/skills/auto-capture/SKILL.md`
- `/home/user/OB1/dashboards/open-brain-dashboard-next/README.md`
- `/home/user/OB1/.github/metadata.schema.json`
