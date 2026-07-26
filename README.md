# Daniel Yarmoluk

**Building pre-structured knowledge graphs that outperform RAG at 4× F1 and 11× lower token cost.**

Founder of [Graphify.md](https://graphifymd.com) — CKG architecture, benchmark design, and enterprise deployment.

---

## Compact Knowledge Graph Benchmark

97 domains · Fully reproducible · [HuggingFace dataset](https://huggingface.co/datasets/danyarm/ckg-benchmark)

| System | Macro F1 | Tokens/query |
|--------|----------|-------------|
| **CKG** | **0.471** | **269** |
| RAG | 0.123 | 2,982 |
| GraphRAG | 0.120 | 3,450 |

CKG F1 **improves** with hop depth (0.374 → 0.772 at hop=5). RAG plateaus at hop=2.

→ [**ckg-benchmark**](https://github.com/Yarmoluk/ckg-benchmark) — benchmark repo, paper, reproducible results

---

## What Is CKG?

Pre-structured knowledge as a plain `.md` or `.csv` file. Drop it in your LLM context. No graph database, no embeddings, no retrieval pipeline.

The structure is the signal — not the curation effort. A GLP-1/Obesity pharmacology CKG built entirely from the ClinicalTrials.gov API in one session achieved F1 = 0.530, exceeding the hand-curated educational average.

---

## Live Packages

| Package | What it is | PyPI |
|---------|-----------|------|
| [ckg-mcp](https://github.com/Yarmoluk/ckg-mcp) | 97-domain MCP server — CKG traversal for any agent stack | [![PyPI](https://img.shields.io/pypi/v/ckg-mcp)](https://pypi.org/project/ckg-mcp/) |
| [ckg-nvidia-ai](https://github.com/Yarmoluk/ckg-nvidia-ai) | NVIDIA AI stack — 20 domains, 1,055 nodes, SHA-256 provenance | [![PyPI](https://img.shields.io/pypi/v/ckg-nvidia-ai)](https://pypi.org/project/ckg-nvidia-ai/) |
| [ckg-nvidia-nemoclaw](https://github.com/Yarmoluk/ckg-nvidia-nemoclaw) | NVIDIA NemoClaw — F1 0.576, benchmarked, 55 nodes | [![PyPI](https://img.shields.io/pypi/v/ckg-nvidia-nemoclaw)](https://pypi.org/project/ckg-nvidia-nemoclaw/) |
| [ckg-agentforce](https://github.com/Yarmoluk/ckg-agentforce) | Salesforce AgentForce — 4 domains, 138 nodes, billing chains | [![PyPI](https://img.shields.io/pypi/v/ckg-agentforce)](https://pypi.org/project/ckg-agentforce/) |
| [ckg-nemotron-perplexity](https://github.com/Yarmoluk/ckg-nemotron-perplexity) | NVIDIA Nemotron + Perplexity Sonar — 2 domains, 83 nodes | [![PyPI](https://img.shields.io/pypi/v/ckg-nemotron-perplexity)](https://pypi.org/project/ckg-nemotron-perplexity/) |

---

## Paper

*Benchmarking Knowledge Retrieval Architectures Across Educational and Commercial Domains: RAG, GraphRAG, and Compact Knowledge Graphs*
Yarmoluk & McCreary, 2026 · v0.6.2 · Patent pending

→ [Read the paper](https://graphifymd.com/paper.html) · [PDF](https://github.com/Yarmoluk/ckg-benchmark/raw/main/paper/main.pdf)

---

## Contact

[graphifymd.com](https://graphifymd.com) · [LinkedIn](https://www.linkedin.com/in/danyarmoluk/)
