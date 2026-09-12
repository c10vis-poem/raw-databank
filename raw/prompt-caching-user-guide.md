# Prompt caching — practical user guide

Distilled from the official doc (`anthropic-prompt-caching-official-2026-08-11.md`, same folder) for actually using this in a Termux/Claude Code + custom-agent context. Full detail lives in that file; this is the "what do I actually type" version.

## The one rule that matters most

**Cache breakpoints only cache what's *behind* them, and only if that content is byte-identical to a previous request.** Put the breakpoint on the last block that stays the same across calls — never on something that changes every request (a timestamp, the live user message).

## Minimal working example (Python)

```python
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-5",
    max_tokens=1024,
    cache_control={"type": "ephemeral"},   # top-level = automatic caching
    system="You are a helpful assistant.",
    messages=[{"role": "user", "content": "Hello"}],
)

# Check it worked:
print(response.usage.cache_creation_input_tokens)  # tokens written (1st call)
print(response.usage.cache_read_input_tokens)       # tokens read (2nd+ call)
```

Run this twice in a row with the same `system` text: first call shows `cache_creation_input_tokens > 0` and `cache_read_input_tokens == 0`; second call flips that. If both stay 0 both times, your prompt is under the per-model minimum (see table below) — pad it or don't bother caching.

## Explicit breakpoint (fine-grained control)

```python
response = client.messages.create(
    model="claude-opus-5",
    max_tokens=1024,
    system=[
        {
            "type": "text",
            "text": LARGE_STABLE_SYSTEM_PROMPT,
            "cache_control": {"type": "ephemeral"},   # breakpoint HERE, not on messages
        }
    ],
    messages=[{"role": "user", "content": user_input}],  # this can change every call — fine
)
```

Use this over automatic caching whenever your prompt has a **static prefix + varying suffix** shape (system prompt/tool defs that rarely change, followed by a live user message that changes every time). Automatic caching would put the breakpoint on the last block — which in this shape is the varying one — and you'd pay full write cost every single call with zero reads, ever.

## 1-hour TTL (for gaps longer than 5 minutes)

```python
system=[{
    "type": "text",
    "text": LARGE_STABLE_SYSTEM_PROMPT,
    "cache_control": {"type": "ephemeral", "ttl": "1h"},
}]
```

Use when: your own usage pattern has gaps over 5 minutes but under an hour (e.g. you step away between terminal sessions). Costs 2x base input to write instead of 1.25x — only worth it if you're not hitting it constantly anyway.

## Pre-warming (kill the first-request latency penalty)

```python
def prewarm():
    client.messages.create(
        model="claude-opus-5",
        max_tokens=0,                      # <-- this is what makes it a pre-warm, not a real call
        system=[{
            "type": "text", "text": LARGE_STABLE_SYSTEM_PROMPT,
            "cache_control": {"type": "ephemeral"},
        }],
        messages=[{"role": "user", "content": "warmup"}],   # placeholder, never read/answered
    )
```

Fire this before you actually start typing (e.g. right when you open the terminal session), then your first real message hits a warm cache instead of paying the cold-write latency. Breakpoint goes on the system prompt, **not** on the placeholder message — put it on the placeholder and the warm-up caches the wrong thing.

## Cache minimums — will your prompt even cache?

| Model | Minimum tokens |
|---|---|
| Opus 5, Fable 5, Mythos 5 | 512 |
| Opus 4.8, Sonnet 5, Sonnet 4.6 | 1,024 |
| Opus 4.7 | 2,048 |
| Opus 4.6, Haiku 4.5 | 4,096 |

Below the minimum = silently not cached, no error. If `cache_creation_input_tokens` and `cache_read_input_tokens` are both 0 after two identical calls, this is almost always why.

## What breaks the cache (in order of how often people trip on it)

1. **Anything after the breakpoint changing** — obviously.
2. **Editing the top-level `system` field mid-conversation** — use a `{"role": "system", ...}` message appended to `messages[]` instead (works on Opus 5, Opus 4.8, Sonnet 5, Fable 5, Mythos 5 — not Sonnet 4.6).
3. **Adding/removing a tool, or editing a tool description** — nukes the *entire* cache (tools, system, messages).
4. **Toggling web search or citations on/off** — invalidates system + messages, tools survive.
5. **Adding/removing an image anywhere** — invalidates messages only.
6. **Changing `tool_choice`, `thinking` config, or `output_config.effort`** — invalidates messages, and model-specific whether tools/system survive.
7. **Non-deterministic JSON key ordering** (Go, Swift) in `tool_use` blocks — the hash sees different bytes even though the data is "the same."

## Command to actually check if caching is working right now

```bash
# via the ant CLI, if installed
ant messages create --transform usage --model claude-opus-5 \
  --message '{role: user, content: "test"}'
```

Look at the returned `usage` block: `cache_read_input_tokens` nonzero on the 2nd+ identical call = it's working. Zero every time = something above is breaking it, or you're under the token minimum.

## Pricing quick-reference (Opus 5, per MTok)

| | Price |
|---|---|
| Base input | $5 |
| 5-min cache write | $6.25 |
| 1-hour cache write | $10 |
| Cache read | $0.50 |
| Output | $25 |

Break-even: 5-min TTL needs **2 requests** to beat paying full price twice; 1-hour TTL needs **3 requests**. Fewer than that and caching isn't worth it — just send the plain request.
