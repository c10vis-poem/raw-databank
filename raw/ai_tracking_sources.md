# AI Tracking Sources — Master Reference

*Last updated: May 1, 2026*
*Scope: Aggregator sites, news feeds, code repositories, and developer hubs for tracking AI/ML releases, agentic frameworks, local model development, and Google ecosystem updates.*

---

## Primary Aggregators

### MarkTechPost — `marktechpost.com`
**Daily AI dashboard.** Broad coverage of model releases, coding tutorials, and research breakdowns. Strong for "here's what shipped this week" overviews. Articles often pair with GitHub repos and runnable code.

### AI Daily Brief — `aidailybrief.ai`
Companion site to the YouTube channel below. Daily digest format, less code-dense than MarkTechPost.

### Papers with Code — `paperswithcode.com`
**Most important site for open-source AI development.** When a new paper drops, this site instantly pairs the academic paper with the top trending GitHub repositories that implement it. Less of a magazine, more of a leaderboard.

### AlphaSignal — `alphasignal.ai`
Weekly newsletter built by algorithms — AI tracks GitHub, ArXiv, and Twitter, analyzes what top engineers are talking about, condenses into a heavily linked email. Dense with code and model links.

---

## Agentic Framework Hubs

### LangChain Blog — `blog.langchain.dev`
### LlamaIndex Blog — `llamaindex.ai/blog`

The two biggest frameworks for building AI agents. Step-by-step tutorials, YouTube videos, and GitHub gists showing how to wire up local models to use tools, search the web, and execute reasoning loops. Architecture-level detail you won't get from news aggregators.

---

## Twitter/X Feeds

### @_akhaliq (AK Feed)
24/7 feed of every major AI paper the second it's published. Short summary, video of the model working, GitHub link. AK runs `huggingface.co/papers` — this is upstream of MarkTechPost.

---

## Google Ecosystem (Official)

### Google Research Blog — `research.google/blog`
Deep, technical science and AI papers.

### The Keyword — `blog.google`
Mainstream consumer news and product drops.

### Gemini API Cookbook — `github.com/google-gemini/cookbook`
**The AI Studio bible.** Massive repository of quick-start guides and complex architectures. Whenever Google ships a new Gemini capability, engineers immediately upload a Python notebook showing how the code works. Clone into Termux or run in Colab.

### Google Cloud Generative AI Repository — `github.com/GoogleCloudPlatform/generative-ai`
Enterprise-level big brother to the Gemini Cookbook. Vertex AI and Model Garden focus. Hundreds of step-by-step implementation guides for taking open-weight models from the Vertex Model Garden, fine-tuning them, and deploying at scale.

### Google Cloud Tech YouTube — `youtube.com/@googlecloudtech`
Skip the marketing videos, go to "Generative AI" playlists. High-density whiteboard breakdowns of agent architectures and RAG systems on Google Cloud.

### Google AI Developers Discord — `discord.gg/google-dev-community`
Real-time news. Where Google DevRel team hangs out. Silent updates and Vertex Garden drops get discussed here before GitHub.

---

## Open Source & Model Tracking

### Hugging Face Papers — `huggingface.co/papers`
Daily trending AI research, paired with model/code links.

### Hugging Face Models — `huggingface.co/models`
Where actual open-weight models drop.

### GitHub Trending — `github.com/trending`
Most starred code repositories today. **Filter aggressively** (see Filter Guide below).

### LocalLLaMA Subreddit — `reddit.com/r/LocalLLaMA`
Community building local AI workflows. Real benchmarks, real failure modes, real hardware notes.

### Hacker News — `news.ycombinator.com`
Ruthless, highly technical front page of tech news.

---

## YouTube Channels (Daily Watch)

| Channel | Handle | Format | Why |
|---------|--------|--------|-----|
| Nate B Jones | `@NateBJones` | Daily breakdowns, frameworks | Already mentor — 7-skill framework, OB1 repo, OS thinking |
| AI Daily Brief | `@AIDailyBrief` | Daily news digest | Broad industry pulse |
| Tim Carambat | `@TimCarambat` | Builder-focused, AnythingLLM creator | Local AI deployment angle, builder POV |

---

## GitHub Trending Filter Guide

GitHub Trending defaults to "Any Language" — which means you see JavaScript/CSS/frontend noise. Filter by language to cut through:

| Filter | What You Get |
|--------|-------------|
| **Python** | Agentic workflows, super-agent frameworks, LLM routing logic. King of AI. |
| **C++** | Hardware performance. `llama.cpp`-style local inference engines, robotics control systems. |
| **Jupyter Notebook** | Raw experimental code attached to brand-new academic papers. Math, data viz, and runnable cells together. |
| **Rust** | Newer entrant — high-performance inference, systems-level AI tooling. Worth checking weekly. |

Adjust **Date range** to "This week" if checking once weekly instead of daily.

---

## Additions From Claude Pass (May 2026)

### Newsletters / Aggregators worth adding:

- **Smol Newsletter** (Hugging Face) — open-source model and dataset releases, less polished but earlier than MarkTechPost
- **Ben's Bites** (`bensbites.com`) — daily, more business-angle but catches funding/deal news that affects ecosystem
- **The Batch** (DeepLearning.AI / Andrew Ng) — weekly, more curated, strong on industry-academic bridge

### YouTube channels to evaluate:

- **Yannic Kilcher** — paper deep-dives, less frequent but extremely technical
- **AI Explained** — weekly recap, good for "what mattered this week" not "what dropped today"
- **Two Minute Papers** — daily-ish, high signal-to-noise on novel research
- **Matt Wolfe** — daily news, more accessible/broader audience but useful for catching mainstream drops you missed

### Specifically for your stack:

- **Qualcomm AI Hub** (`aihub.qualcomm.com`) — direct source for Snapdragon/Hexagon-optimized models. Critical for NO.VA NPU work since Razr Ultra 25 runs Hexagon.
- **NVIDIA Developer Blog** (`developer.nvidia.com/blog`) — direct source for Jetson Nano Super updates, CUDA stack changes. Essential when Jetson lands this summer.
- **Thundercomm Forum** — already in build thread context, but worth listing here as the ground-truth source for Rubik Pi 3 OS releases and firmware fixes.
- **r/LocalLLaMA** + **r/EdgeAI** + **r/embedded** subreddits — for hardware-side local inference discussion.

---

## Discovery Workflow (Suggested)

| Frequency | Source | What to Look For |
|-----------|--------|-----------------|
| Daily | MarkTechPost, AK feed, AI Daily Brief | New model releases, coding tutorials |
| Daily (filtered) | GitHub Trending (Python) | New agentic frameworks, novel architectures |
| Weekly | Papers with Code, Hugging Face Papers | Implementation-paired research |
| Weekly | LangChain/LlamaIndex blogs | Agent architecture patterns |
| Weekly | AlphaSignal newsletter | Algorithmic curation of the week |
| Bi-weekly | Qualcomm AI Hub, NVIDIA Developer Blog | Hardware-specific drops for your stack |
| Continuous | LocalLLaMA subreddit | Real-world local inference reports |

---

## Integration With Tracker Thread

Once the systems-update tracker thread is operational, this document becomes its **input source list**. The tracker:

1. Polls these sources weekly (or as cadence allows)
2. Filters output through the BUILD-prompt **U (Understand)** lens — what's relevant to your active stacks (RazrPi, NO.VA, Vascu14R, Brain Trust LLC infrastructure)
3. Produces `systems_update.md` weekly
4. That `systems_update.md` gets linked into all new BUILD prompts so every fresh thread starts with current capability reality, not stale assumptions

This document is the **map**. The tracker is the **vehicle**. The output `.md` is the **briefing**.

---

*Original Gemini research: solid this pass — kept intact. Claude additions: hardware-specific sources for your stack, additional YouTube/newsletter coverage, integration spec for tracker thread workflow.*
