<div align="center">

[![Typing SVG](https://readme-typing-svg.demolab.com?font=IBM+Plex+Mono&size=18&duration=3000&pause=1200&color=0F6E56&center=true&vCenter=true&width=660&lines=Context+for+knowledge%2C+not+for+language.;Own+the+context%2C+rent+the+model.;97+domains+%C2%B7+269+tokens+%C2%B7+SHA-256+anchored.;Model+for+language%2C+context+for+knowledge.)](https://graphifymd.com)

### Daniel Yarmoluk
**Knowledge Graph Architect · Founder, [Graphify.md](https://graphifymd.com)**  
Minneapolis, MN · patent pending

[![PyPI downloads](https://img.shields.io/badge/PyPI-5%2C349%2Fmo-22c55e?style=flat-square&logo=pypi&logoColor=white)](https://pypi.org/user/danyarm/)
[![MCP Registry](https://img.shields.io/badge/MCP_Registry-5_live-0f6e56?style=flat-square)](https://registry.modelcontextprotocol.io)
[![CKG domains](https://img.shields.io/badge/CKG_domains-97-1d4ed8?style=flat-square)](https://graphifymd.com)
[![Benchmark F1](https://img.shields.io/badge/F1-0.471_+283%25_RAG-8b5cf6?style=flat-square)](https://graphifymd.com/paper.html)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-danyarm-f59e0b?style=flat-square&logo=huggingface&logoColor=white)](https://huggingface.co/danyarm)

</div>

---

<!-- TELEMETRY_START -->
```
CONTEXT KING                              graphifymd.com · ckg-benchmark v0.6.2
─────────────────────────────────────────────────────────────────────────────────
 BENCHMARK F1    ████████████████░░░░░░░░  0.471  +283% vs RAG  +292% vs GraphRAG
 TOKENS/QUERY    ██████░░░░░░░░░░░░░░░░░░  269    vs 2,982 RAG        11× savings
 CKG DOMAINS     ████████████████████████  97     deployed · MCP-native · SHA-256
 PYPI / MONTH    ████████████░░░░░░░░░░░░  5,349  installs · 5 packages
 MCP INSTALLS    ████░░░░░░░░░░░░░░░░░░░░  19     7-day · startup pings
 MCP REQUESTS    ████████░░░░░░░░░░░░░░░░  79     7-day · live via PostHog
─────────────────────────────────────────────────────────────────────────────────
 Own the context, rent the model.           Model for language, context for knowledge.
```
<!-- TELEMETRY_END -->

---

## Deployed Packages

| Package | What it serves | Downloads |
|---------|----------------|-----------|
| [**ckg-mcp**](https://github.com/Yarmoluk/ckg-mcp) | 97-domain MCP server · drop-in knowledge layer for any agent stack · SHA-256 provenance per node | [![dm](https://img.shields.io/pypi/dm/ckg-mcp?style=flat-square&color=22c55e&label=)](https://pypi.org/project/ckg-mcp/) |
| [**ckg-nvidia-ai**](https://github.com/Yarmoluk/ckg-nvidia-ai) | NVIDIA AI stack · 20 domains · 1,055 nodes · per-URL SHA-256 | [![dm](https://img.shields.io/pypi/dm/ckg-nvidia-ai?style=flat-square&color=22c55e&label=)](https://pypi.org/project/ckg-nvidia-ai/) |
| [**ckg-nvidia-nemoclaw**](https://github.com/Yarmoluk/ckg-nvidia-nemoclaw) | NemoClaw · **F1 0.576** benchmarked · 55 nodes / 74 edges | [![dm](https://img.shields.io/pypi/dm/ckg-nvidia-nemoclaw?style=flat-square&color=22c55e&label=)](https://pypi.org/project/ckg-nvidia-nemoclaw/) |
| [**ckg-agentforce**](https://github.com/Yarmoluk/ckg-agentforce) | Salesforce AgentForce · billing + permissions chains · rate-gated | [![dm](https://img.shields.io/pypi/dm/ckg-agentforce?style=flat-square&color=22c55e&label=)](https://pypi.org/project/ckg-agentforce/) |
| [**ckg-nemotron-perplexity**](https://github.com/Yarmoluk/ckg-nemotron-perplexity) | NVIDIA Nemotron + Perplexity Sonar · 2 domains · 83 nodes | [![dm](https://img.shields.io/pypi/dm/ckg-nemotron-perplexity?style=flat-square&color=22c55e&label=)](https://pypi.org/project/ckg-nemotron-perplexity/) |

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

## Active Threads

```
[ LIVE   ] Polar paywall · $10/year · license keys · rate-gated on 3 Render services
[ JUL 28 ] MCP v2 migration — stateless core · 5 packages · same install, new transport
[ NEXT   ] ElevenLabs CKG — voice AI platform · ~50 nodes
[ OPEN   ] AutoGen #7353 — cryptographic action receipts · PARTIAL conformance
```

---

<div align="center">

[![GitHub Stats](https://github-readme-stats.vercel.app/api?username=Yarmoluk&show_icons=true&hide_title=true&theme=dark&bg_color=0d1117&icon_color=0f6e56&text_color=8b949e&border_color=21262d&hide=issues&count_private=false)](https://github.com/Yarmoluk)
&nbsp;&nbsp;
[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=Yarmoluk&layout=compact&theme=dark&bg_color=0d1117&text_color=8b949e&border_color=21262d&hide_title=true&langs_count=6)](https://github.com/Yarmoluk)

---

[graphifymd.com](https://graphifymd.com) · [LinkedIn](https://www.linkedin.com/in/danyarmoluk/) · [PyPI](https://pypi.org/user/danyarm/) · [HuggingFace](https://huggingface.co/danyarm) · [MCP Registry](https://registry.modelcontextprotocol.io)

</div>
