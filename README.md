<!-- TELEMETRY_START -->
```ansi
[92mModel for Language, Context for Knowledge ▸ ckg-benchmark v0.6.2
══════════════════════════════════════════════════════════════════════════
 BENCHMARK F1     [▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░]  0.471   +283% vs RAG
 TOKEN EFFICIENCY [▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░]  91%     tokens saved vs RAG
 CKG DOMAINS      [▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░]  97      SHA-256 · MCP-native
 PYPI / MONTH     [▓▓▓░░░░░░░░░░░░░░░]  1,381   downloads / month
 TOKENS SAVED     [▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░]  727k    this month vs RAG
 SAVINGS AT SCALE [▓░░░░░░░░░░░░░░░░░]  $478    est · enterprise
══════════════════════════════════════════════════════════════════════════
 Own the context, rent the model.[0m
```
<!-- TELEMETRY_END -->

<div align="center">

[![PyPI downloads](https://img.shields.io/badge/PyPI-5%2C349%2Fmo-22c55e?style=flat-square&logo=pypi&logoColor=white)](https://pypi.org/user/danyarm/)
[![MCP Registry](https://img.shields.io/badge/MCP_Registry-5_live-0f6e56?style=flat-square)](https://registry.modelcontextprotocol.io)
[![CKG domains](https://img.shields.io/badge/CKG_domains-97-1d4ed8?style=flat-square)](https://graphifymd.com)
[![Benchmark F1](https://img.shields.io/badge/F1-0.471_+283%25_RAG-8b5cf6?style=flat-square)](https://graphifymd.com/paper.html)
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

## Deployed Packages

| Package | What it serves | Downloads |
|---------|----------------|-----------|
| [**ckg-mcp**](https://github.com/Yarmoluk/ckg-mcp) | 97-domain MCP server · drop-in knowledge layer for any agent stack · SHA-256 provenance per node | ![downloads](https://static.pepy.tech/badge/ckg-mcp/month) |
| [**ckg-nvidia-ai**](https://github.com/Yarmoluk/ckg-nvidia-ai) | NVIDIA AI stack · 20 domains · 1,055 nodes · per-URL SHA-256 | ![downloads](https://static.pepy.tech/badge/ckg-nvidia-ai/month) |
| [**ckg-nvidia-nemoclaw**](https://github.com/Yarmoluk/ckg-nvidia-nemoclaw) | NemoClaw · **F1 0.576** benchmarked · 55 nodes / 74 edges | ![downloads](https://static.pepy.tech/badge/ckg-nvidia-nemoclaw/month) |
| [**ckg-agentforce**](https://github.com/Yarmoluk/ckg-agentforce) | Salesforce AgentForce · billing + permissions chains · rate-gated | ![downloads](https://static.pepy.tech/badge/ckg-agentforce/month) |
| [**ckg-nemotron-perplexity**](https://github.com/Yarmoluk/ckg-nemotron-perplexity) | NVIDIA Nemotron + Perplexity Sonar · 2 domains · 83 nodes | ![downloads](https://static.pepy.tech/badge/ckg-nemotron-perplexity/month) |

```bash
uvx ckg-mcp                 # any agent stack — 97 domains, MCP-native
uvx ckg-nvidia-ai           # NVIDIA AI · NIM · NeMo · NemoClaw
uvx ckg-nvidia-nemoclaw     # NemoClaw — F1 0.576 benchmarked
```

---

## Benchmark

| System | Macro F1 | Tokens/query | Ratio/Dollar Score |
|--------|:--------:|:------------:|:------------------:|
| **▸ CKG** | **0.471** | **269** | **0.00175** |
| RAG | 0.123 | 2,982 | 0.0000413 |
| GraphRAG | 0.120 | 3,450 | 0.0000452 |

`ckg-benchmark v0.6.2` · 97 domains · [HuggingFace dataset](https://huggingface.co/datasets/danyarm/ckg-benchmark) · [paper](https://graphifymd.com/paper.html) · patent pending

F1 scales with hop depth: `0.374 → 0.772` at hop=5. RAG plateaus at hop=2.

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
