# Daniel Yarmoluk

**Building pre-structured knowledge graphs that outperform RAG at 11× lower token cost.**

Founder of [Graphify.md](https://graphifymd.com) — CKG architecture, benchmark design, and enterprise deployment.

---

## Compact Knowledge Graph Benchmark

**42× more intelligence per token than RAG. Zero hallucinations by construction.**

45 domains · 7,928 queries · Fully reproducible

| System | Macro F1 | Tokens/query | RDS |
|--------|----------|-------------|-----|
| **CKG** | **0.4709** | **269** | **0.00175** |
| RAG | 0.1231 | 2,982 | 0.0000413 |
| GraphRAG | 0.1200 | 3,450 | 0.0000452 |

CKG F1 **improves** with hop depth (0.374 → 0.772 at hop=5). RAG plateaus at hop=2.

→ [**ckg-benchmark**](https://github.com/Yarmoluk/ckg-benchmark) — benchmark repo, paper, reproducible results

---

## What Is CKG?

Pre-structured knowledge as a plain `.md` or `.csv` file. Drop it in your LLM context. No graph database, no embeddings, no retrieval pipeline.

The structure is the signal — not the curation effort. Track 2 proved this: a GLP-1/Obesity pharmacology CKG built entirely from the ClinicalTrials.gov API in one session achieved F1 = 0.530, exceeding the hand-curated educational average.

---

## Active Projects

| Project | What it is |
|---------|-----------|
| [ckg-benchmark](https://github.com/Yarmoluk/ckg-benchmark) | 45-domain RAG vs CKG vs GraphRAG benchmark — paper + data + code |
| `ckg-mcp` | MCP server — CKG as a pre-compiled routing layer for agent stacks *(coming)* |
| [Graphify.md](https://graphifymd.com) | Commercial CKG deployment — weekly-updated domain knowledge for enterprise AI |

---

## Paper

*Benchmarking Knowledge Retrieval Architectures Across Educational and Commercial Domains: RAG, GraphRAG, and Compact Knowledge Graphs*
Yarmoluk & McCreary, 2026 · v0.6.2 · Patent pending App #64/040,804

→ [Read the paper](https://graphifymd.com/paper.html) · [PDF](https://github.com/Yarmoluk/ckg-benchmark/raw/main/paper/main.pdf)

---

## Contact

[graphifymd.com](https://graphifymd.com) · [LinkedIn](https://www.linkedin.com/in/danyarmoluk/)
