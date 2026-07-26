<div align="center">

# Daniel Yarmoluk

**Knowledge Graph Architect · MCP Server Builder**  
Founder, [Graphify.md](https://graphifymd.com) · Minneapolis, MN

[![PyPI downloads](https://img.shields.io/badge/PyPI-5%2C349%2Fmo-22c55e?style=flat-square&logo=pypi&logoColor=white)](https://pypi.org/user/danyarm/)
[![MCP Registry](https://img.shields.io/badge/MCP_Registry-5_packages-0f6e56?style=flat-square)](https://registry.modelcontextprotocol.io)
[![97 domains](https://img.shields.io/badge/CKG_domains-97-1d4ed8?style=flat-square)](https://graphifymd.com)
[![Paper](https://img.shields.io/badge/paper-v0.6.2-8b5cf6?style=flat-square)](https://graphifymd.com/paper.html)

</div>

```
╔═══════════════════════════════════════════════════════════════╗
║  OPERATOR    Daniel Yarmoluk                                  ║
║  CLASS       Knowledge Graph Architect                        ║
║  ORG         Graphify.md (Founder) · Minneapolis, MN          ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  Benchmark F1    ██████████████░░░░░░  0.471   +283% RAG     ║
║  Token cost      ████████████████████  11×     fewer tokens   ║
║  CKG domains     ████████████████████  97      deployed       ║
║  PyPI / mo       ██████████░░░░░░░░░░  5,349   installs       ║
║  MCP Registry    ████████████████████  5/5     live packages  ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## ▸ Deployed Systems

| Package | Description | Version | Downloads |
|---------|-------------|---------|-----------|
| [ckg-mcp](https://github.com/Yarmoluk/ckg-mcp) | 97-domain MCP server — drop-in knowledge layer for any agent stack | [![PyPI](https://img.shields.io/pypi/v/ckg-mcp?style=flat-square)](https://pypi.org/project/ckg-mcp/) | [![Downloads](https://img.shields.io/pypi/dm/ckg-mcp?style=flat-square&color=22c55e)](https://pypi.org/project/ckg-mcp/) |
| [ckg-nvidia-ai](https://github.com/Yarmoluk/ckg-nvidia-ai) | NVIDIA AI stack · 20 domains · 1,055 nodes · SHA-256 provenance | [![PyPI](https://img.shields.io/pypi/v/ckg-nvidia-ai?style=flat-square)](https://pypi.org/project/ckg-nvidia-ai/) | [![Downloads](https://img.shields.io/pypi/dm/ckg-nvidia-ai?style=flat-square&color=22c55e)](https://pypi.org/project/ckg-nvidia-ai/) |
| [ckg-nvidia-nemoclaw](https://github.com/Yarmoluk/ckg-nvidia-nemoclaw) | NVIDIA NemoClaw · F1 0.576 benchmarked · 55 nodes | [![PyPI](https://img.shields.io/pypi/v/ckg-nvidia-nemoclaw?style=flat-square)](https://pypi.org/project/ckg-nvidia-nemoclaw/) | [![Downloads](https://img.shields.io/pypi/dm/ckg-nvidia-nemoclaw?style=flat-square&color=22c55e)](https://pypi.org/project/ckg-nvidia-nemoclaw/) |
| [ckg-agentforce](https://github.com/Yarmoluk/ckg-agentforce) | Salesforce AgentForce · 4 domains · billing chains | [![PyPI](https://img.shields.io/pypi/v/ckg-agentforce?style=flat-square)](https://pypi.org/project/ckg-agentforce/) | [![Downloads](https://img.shields.io/pypi/dm/ckg-agentforce?style=flat-square&color=22c55e)](https://pypi.org/project/ckg-agentforce/) |
| [ckg-nemotron-perplexity](https://github.com/Yarmoluk/ckg-nemotron-perplexity) | NVIDIA Nemotron + Perplexity Sonar · 2 domains · 83 nodes | [![PyPI](https://img.shields.io/pypi/v/ckg-nemotron-perplexity?style=flat-square)](https://pypi.org/project/ckg-nemotron-perplexity/) | [![Downloads](https://img.shields.io/pypi/dm/ckg-nemotron-perplexity?style=flat-square&color=22c55e)](https://pypi.org/project/ckg-nemotron-perplexity/) |

```bash
uvx ckg-mcp                 # 97-domain server, any agent stack
uvx ckg-nvidia-ai           # NVIDIA AI + NIM + NeMo stack
uvx ckg-nvidia-nemoclaw     # NemoClaw — benchmarked F1 0.576
```

---

## ▸ Benchmark Signal

| System | Macro F1 | Tokens/query | RDS |
|--------|:--------:|:-----------:|:---:|
| **▸ CKG** | **0.471** | **269** | **0.00175** |
| RAG | 0.123 | 2,982 | 0.0000413 |
| GraphRAG | 0.120 | 3,450 | 0.0000452 |

`ckg-benchmark v0.6.2` · 97 domains · [HuggingFace dataset](https://huggingface.co/datasets/danyarm/ckg-benchmark) · [paper](https://graphifymd.com/paper.html) · patent pending

F1 improves with hop depth (`0.374 → 0.772` at hop=5). RAG plateaus at hop=2.

---

## ▸ Open Threads

```
[ ACTIVE ] AutoGen #7353 — cryptographic action receipts
           CKG knowledge-receipt adapter · conformance suite partial

[ JUL 28 ] MCP v2 migration — stateless core · FastMCP → MCPServer

[ LIVE   ] Polar paywall · $10/year · license keys on 3 Render services

[ NEXT   ] ElevenLabs CKG — voice AI platform · ~50 nodes
```

---

<div align="center">

[graphifymd.com](https://graphifymd.com) · [LinkedIn](https://www.linkedin.com/in/danyarmoluk/) · [PyPI](https://pypi.org/user/danyarm/) · [HuggingFace](https://huggingface.co/danyarm)

</div>
