### Daniel Yarmoluk

**Forward-deployed / applied AI engineer and solutions architect, Minneapolis, MN.**
I build the knowledge layer for AI agents: Compressed Knowledge Graphs (CKGs) with typed, declared
edges and a source URL plus SHA-256 hash on every node. The model handles language; the graph
handles facts. The graph doesn't guess, it traverses. Patent pending.

[LinkedIn](https://www.linkedin.com/in/danyarmoluk) · [Book a call](https://cal.com/daniel-yarmoluk-sjmnub) · [daniel.yarmoluk@gmail.com](mailto:daniel.yarmoluk@gmail.com) · [graphifymd.com](https://graphifymd.com) · [Hugging Face](https://huggingface.co/danyarm)

---

## What I build

Everything below resolves today.

- **[langchain-ckg](https://github.com/Yarmoluk/langchain-ckg)** - a LangChain retriever (`pip install langchain-ckg`), listed in the [official LangChain integrations docs](https://docs.langchain.com/oss/python/integrations/retrievers). 11 agent-stack graphs ship in the wheel and run offline.
- **[ckg-nvidia-ai](https://pypi.org/project/ckg-nvidia-ai/)** - the NVIDIA AI developer stack as 20 graphs (1,006 nodes), served over MCP. Live demo: [Hugging Face Space](https://huggingface.co/spaces/danyarm/ckg-nvidia-nemoclaw).
- **[glp1-pa-copilot](https://yarmoluk.github.io/glp1-pa-copilot/)** ([source](https://github.com/Yarmoluk/glp1-pa-copilot)) - healthcare prior-authorization draft gate on synthetic data. The model cannot add a fact: it verbalizes what the policy graph returns, a named reviewer accepts or edits, and every action lands in an append-only audit log.
- **[ckg-strands-showcase](https://github.com/Yarmoluk/ckg-strands-showcase)** - CKG with Strands Agents: a one-model-call cap and a 55-test suite. The repo is an overview with reported results; the implementation is private.
- **Hosted MCP endpoint** at `https://www.graphifymd.com/api/mcp` (list_domains, query_ckg, get_prerequisites, search_concepts, query_intersect), plus a free library of graphs you can download as Markdown at [graphifymd.com](https://graphifymd.com/#/library). The served library is 317 domain graphs (284 free, 33 Pro), 57,705 nodes, counted from the served files on 2026-10-06.
- Six production MCP services (design, auth, license gating, metering, telemetry, operations) and 80+ Claude Code skills, some public in [skills-1](https://github.com/Yarmoluk/skills-1).

Try an agent card that states its own economics, including when not to call it:

```bash
curl -s https://ckg-nvidia-ai.onrender.com/.well-known/agent-card.json | jq .economics
```

---

## How I work

I treat evaluation as the product. Frozen corpora, SHA-256 manifests, paired runs, controls.
I publish null results and limits: a LongMemEval-V2 run reported as the tie it was, graph-relative
scores labeled as graph-relative, and a correction to my own earlier cost figures.

The one benchmark I quote, from one locked run (v0.6.2), 44 hand-curated domains, 7,758 queries:

| | CKG | RAG | GraphRAG |
|:--|--:|--:|--:|
| macro-F1 | 0.471 | 0.123 | 0.120 |
| tokens per query | 269 | 2,982 | - |

That is nearly 4x RAG on structural queries. The 11x token reduction comes from the same run, not an
independent result. At 5 hops, CKG F1 is 0.772 against 0.170 for RAG. Dataset:
[huggingface.co/datasets/danyarm/ckg-benchmark](https://huggingface.co/datasets/danyarm/ckg-benchmark).

---

## Background

- **Slalom** - Solution Owner / AI and Digital Transformation Architect: UnitedHealthcare, Best Buy, Cargill. Discovery, build-versus-buy, production-readiness and evaluation requirements.
- **West Monroe** - Lead Solution Architect.
- **ATEK Access Technologies** - built the IoT and data science practice from zero.
- **University of St. Thomas** - Adjunct Professor, Graduate AI Systems (2018-present).

Fifteen-plus years of enterprise delivery.

---

## Open to

Forward-deployed, applied AI, and solutions architecture roles where agents must be grounded,
auditable, and deployed into real enterprise environments. Remote US; open to relocation.

[LinkedIn](https://www.linkedin.com/in/danyarmoluk) · [cal.com/daniel-yarmoluk-sjmnub](https://cal.com/daniel-yarmoluk-sjmnub) · [daniel.yarmoluk@gmail.com](mailto:daniel.yarmoluk@gmail.com)
