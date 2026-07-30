<!-- TELEMETRY_START -->
![Model for Language, Context for Knowledge](hud.svg)
<!-- TELEMETRY_END -->

<div align="center">

[![PyPI downloads](https://img.shields.io/badge/PyPI-1%2C186%2Fmo-22c55e?style=flat-square&logo=pypi&logoColor=white)](https://pypi.org/user/danyarm/)
[![MCP Registry](https://img.shields.io/badge/MCP_Registry-5_live-0f6e56?style=flat-square)](https://registry.modelcontextprotocol.io)
[![CKG domains](https://img.shields.io/badge/CKG_domains-97-1d4ed8?style=flat-square)](https://graphifymd.com)
[![Benchmark F1](https://img.shields.io/badge/F1-0.471_+283%25_vs_RAG-8b5cf6?style=flat-square)](https://graphifymd.com/paper.html)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-danyarm-f59e0b?style=flat-square&logo=huggingface&logoColor=white)](https://huggingface.co/danyarm)
[![Patent](https://img.shields.io/badge/patent-pending-7c3aed?style=flat-square)](https://graphifymd.com)

[![LangChain](https://img.shields.io/badge/LangChain-compatible-1c7c2c?style=flat-square&logo=chainlink&logoColor=white)](https://github.com/Yarmoluk/langchain-ckg)
[![LlamaIndex](https://img.shields.io/badge/LlamaIndex-compatible-6366f1?style=flat-square)](https://github.com/Yarmoluk/llamaindex-ckg)
[![CrewAI](https://img.shields.io/badge/CrewAI-compatible-ef4444?style=flat-square)](https://github.com/Yarmoluk/crewai-ckg)
[![Zep](https://img.shields.io/badge/Zep-compatible-0ea5e9?style=flat-square)](https://github.com/Yarmoluk/zep-ckg)
[![ElevenLabs](https://img.shields.io/badge/ElevenLabs-compatible-111827?style=flat-square)](https://elevenlabs.io)
[![NVIDIA](https://img.shields.io/badge/NVIDIA-compatible-76b900?style=flat-square&logo=nvidia&logoColor=white)](https://github.com/Yarmoluk/ckg-nvidia-ai)
[![Meta Llama](https://img.shields.io/badge/Meta_Llama-compatible-0668E1?style=flat-square)](https://github.com/Yarmoluk/ckg-mcp)
[![Smithery](https://img.shields.io/badge/Smithery-listed-ff6b35?style=flat-square)](https://smithery.ai/server/@Yarmoluk/ckg-mcp)
[![Anthropic](https://img.shields.io/badge/Anthropic_MCP-registry-0f6e56?style=flat-square&logo=anthropic&logoColor=white)](https://registry.modelcontextprotocol.io)

</div>

---

Agents need certainty. LLMs give probability. **Compact Knowledge Graphs (CKGs)** are the missing layer — structured, auditable domain knowledge served over MCP. 269 tokens per query vs 2,982 for RAG. F1 0.471, +283% vs RAG baseline. SHA-256 provenance on every node. Drop-in MCP servers, no infra required.

**New: CKG Router** — deterministic context + model routing from graph depth. `route_query()` returns the right subgraph AND the right model tier (haiku/sonnet/opus) derived from hop count. No heuristic — the graph decides. 4× more accurate, 90% cheaper, routed automatically.

---

## Packages

| Package | Domain | F1 | Downloads |
|---------|--------|----|-----------|
| [**ckg-mcp**](https://github.com/Yarmoluk/ckg-mcp) | 97 domains · full stack · CKG Router | — | ![](https://static.pepy.tech/badge/ckg-mcp/month) |
| [**ckg-nvidia-ai**](https://github.com/Yarmoluk/ckg-nvidia-ai) | NVIDIA AI · NIM · NeMo · 20 domains · 1,055 nodes · CKG Router | — | ![](https://static.pepy.tech/badge/ckg-nvidia-ai/month) |
| [**ckg-nvidia-nemoclaw**](https://github.com/Yarmoluk/ckg-nvidia-nemoclaw) | NemoClaw · 55 nodes / 74 edges · CKG Router | **0.576** | ![](https://static.pepy.tech/badge/ckg-nvidia-nemoclaw/month) |
| [**ckg-agentforce**](https://github.com/Yarmoluk/ckg-agentforce) | Salesforce AgentForce · billing + permissions · CKG Router | — | ![](https://static.pepy.tech/badge/ckg-agentforce/month) |
| [**ckg-nemotron-perplexity**](https://github.com/Yarmoluk/ckg-nemotron-perplexity) | Nemotron + Perplexity Sonar · 83 nodes | — | ![](https://static.pepy.tech/badge/ckg-nemotron-perplexity/month) |
| [**langchain-ckg**](https://github.com/Yarmoluk/langchain-ckg) | LangChain retriever · CKGRetriever + CKGHostedRetriever | — | ![](https://static.pepy.tech/badge/langchain-ckg/month) |

```bash
uvx ckg-mcp              # 97 domains — any agent stack
uvx ckg-nvidia-ai        # NVIDIA AI · NIM · NeMo · NemoClaw
uvx ckg-agentforce       # Salesforce AgentForce

# CKG Router — deterministic context + model routing
route_query("TensorRT-LLM", "nvidia-tensorrt-triton")
# → model_tier: opus · reasoning: sparql_cot · why: 4-hop chain
# → context subgraph: 847 tokens (not 10,000)
```

---

## Benchmark

| System | Macro F1 | Tokens/query | Cost @ $10/1M |
|--------|:--------:|:------------:|:-------------:|
| **▸ CKG** | **0.471** | **269** | **$0.003** |
| RAG | 0.123 | 2,982 | $0.030 |
| GraphRAG | 0.120 | 3,450 | $0.035 |

`ckg-benchmark v0.6.2` · 97 domains · [dataset](https://huggingface.co/datasets/danyarm/ckg-benchmark) · [paper](https://graphifymd.com/paper.html) · patent pending

F1 scales with hop depth: `0.374 → 0.772` at hop=5. RAG plateaus at hop=2.

---

## Pricing

| Tier | Calls | Price | Best for |
|------|-------|-------|----------|
| Free | 50/day | — | Evaluation |
| **Dev** | Unlimited | **$10/yr** | Solo devs, small teams |
| Pro | Unlimited + priority | $99/yr | Production |
| Sealed | On-prem Docker appliance | $299 | Enterprise / air-gap |

[**Upgrade → graphifymd.com/pricing**](https://graphifymd.com/pricing) · [Dev $10/yr](https://buy.stripe.com/00wbJ1gsYcm01tC52A1kA08)

---

<div align="center">

[![GitHub Streak](https://streak-stats.demolab.com?user=Yarmoluk&theme=transparent&background=0d1117&border=21262d&ring=0f6e56&fire=0f6e56&currStreakLabel=0f6e56&sideLabels=8b949e&dates=8b949e&currStreakNum=c9d1d9&sideNums=c9d1d9)](https://github.com/Yarmoluk)

![Python](https://img.shields.io/badge/Python-0d1117?style=flat-square&logo=python&logoColor=3776ab)
![TypeScript](https://img.shields.io/badge/TypeScript-0d1117?style=flat-square&logo=typescript&logoColor=3178c6)
![MCP](https://img.shields.io/badge/MCP-0d1117?style=flat-square&logo=anthropic&logoColor=0f6e56)
![Neo4j](https://img.shields.io/badge/Neo4j-0d1117?style=flat-square&logo=neo4j&logoColor=4581c3)
![FastAPI](https://img.shields.io/badge/FastAPI-0d1117?style=flat-square&logo=fastapi&logoColor=009688)
![Docker](https://img.shields.io/badge/Docker-0d1117?style=flat-square&logo=docker&logoColor=2496ed)
![Render](https://img.shields.io/badge/Render-0d1117?style=flat-square&logo=render&logoColor=46e3b7)
![PyPI](https://img.shields.io/badge/PyPI-0d1117?style=flat-square&logo=pypi&logoColor=3775a9)

---

[graphifymd.com](https://graphifymd.com) · [LinkedIn](https://www.linkedin.com/in/danyarmoluk/) · [PyPI](https://pypi.org/user/danyarm/) · [HuggingFace](https://huggingface.co/danyarm) · [MCP Registry](https://registry.modelcontextprotocol.io)

</div>
