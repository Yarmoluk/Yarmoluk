<div align="center">

<img src="hud.svg" alt="CKG benchmark: macro-F1 0.471, 91% token efficiency, 0.772 at five hops, 307 domain graphs, 6 live MCP services" width="640">

### Daniel Yarmoluk

**AI Solutions Architect · Forward Deployed Engineer**

I build the protocol layer that lets agents act on trustworthy context.

[![Benchmark](https://img.shields.io/badge/macro--F1-0.471_vs_0.123_RAG-1f6feb?style=flat-square)](https://github.com/Yarmoluk/ckg-benchmark)
[![Tokens](https://img.shields.io/badge/tokens-269_vs_2%2C982-8b5cf6?style=flat-square)](https://github.com/Yarmoluk/ckg-benchmark)
[![Domains](https://img.shields.io/badge/domain_graphs-307-0f6e56?style=flat-square)](https://graphifymd.com)
[![PyPI](https://img.shields.io/badge/PyPI-12_packages-3775A9?style=flat-square&logo=pypi&logoColor=white)](https://pypi.org/user/danyarm/)
[![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-danyarm-f59e0b?style=flat-square)](https://huggingface.co/danyarm)
[![Patent](https://img.shields.io/badge/patent-pending-7c3aed?style=flat-square)](https://graphifymd.com)

**[Portfolio &amp; resume &rarr;](https://yarmoluk.github.io)**

[graphifymd.com](https://graphifymd.com) · [LinkedIn](https://linkedin.com/in/danyarmoluk) · [PyPI](https://pypi.org/user/danyarm/) · [Hugging&nbsp;Face](https://huggingface.co/danyarm)

</div>

---

## Try it in 30 seconds

Every MCP server I run publishes an [A2A agent card](https://ckg-nvidia-ai.onrender.com/.well-known/agent-card.json) that states its own economics, so a calling agent can decide whether invoking is worth it **before** it spends anything:

```bash
curl -s https://ckg-nvidia-ai.onrender.com/.well-known/agent-card.json | jq .economics
```

```jsonc
{
  "price_usd_per_call": 0.010,
  "mean_tokens_returned": 269,
  "baseline_mean_tokens": 2982,      // RAG over the same corpus
  "tokens_saved_per_call": 2713,
  "breakeven_input_price_usd_per_mtok": 3.69,
  "answer_quality_macro_f1": 0.471,
  "baseline_macro_f1": 0.123,
  "decision_rule": "…pays for itself on token cost alone when your input price
                    exceeds $3.69 per million tokens. Below that, invoke only
                    when answer quality matters."
}
```

That last field is the point: **it tells you when not to call it.** A card that claims savings at every price is one a good agent should distrust.

---

## The Compressed Knowledge Graph

RAG chunks prose and retrieves by embedding similarity, which discards the relationships. A CKG stores relationships as **typed, authored edges** and traverses them. Every answer traces to a source URL and a SHA-256 of the bytes it was authored from.

**Benchmarked against RAG and Microsoft GraphRAG** — 44 domains, 7,758 queries, locked at v0.6.2:

| | **CKG** | RAG | GraphRAG |
|:--|--:|--:|--:|
| macro-F1 | **0.471** | 0.123 | 0.120 |
| tokens per query | **269** | 2,982 | — |
| F1 at 5-hop depth | **0.772** | 0.170 | — |

The last row matters most. The advantage **grows with question complexity**, because multi-hop composition is exactly where embedding methods are weakest.

**[→ Clone the benchmark and re-run it](https://github.com/Yarmoluk/ckg-benchmark)** · [Dataset on Hugging Face](https://huggingface.co/datasets/danyarm/ckg-benchmark) (CC-BY-4.0)

> The repo includes a reconciliation document correcting my own published cost figures — an earlier version priced CKG and the baselines against different models, which inflated the ratio. Numbers I can't defend are worse than no numbers.

---

## Protocol work

<table>
<tr><td width="50%" valign="top">

**Model Context Protocol**

Tool and output schema design · JSON-RPC initialize handshake · streamable HTTP and SSE transport · session management · DNS-rebinding transport security · per-method metering · HTTP 402 payment rails · MCP-native observability

Built, shipped and debugged in production.

</td><td width="50%" valign="top">

**Agent-to-Agent**

Agent cards advertising skills, auth, payment terms and machine-readable economics · x402 / HTTP 402 · EIP-3009 signed authorizations · Coinbase CDP facilitator · Base settlement · ERC-8004 agent identity

</td></tr>
</table>

**Framework-agnostic by protocol.** The same servers register unchanged in Semantic Kernel, LangChain, LangGraph, AutoGen, CrewAI, Claude and Cursor — integration happens at the protocol layer, so framework choice stays the caller's decision.

```python
# Microsoft Semantic Kernel consumes an MCP server directly — no bridging code
from semantic_kernel import Kernel
from semantic_kernel.connectors.mcp import MCPStreamableHttpPlugin

async with MCPStreamableHttpPlugin(
    name="ckg", url="https://ckg-nvidia-ai.onrender.com/mcp"
) as plugin:
    kernel = Kernel()
    kernel.add_plugin(plugin, plugin_name="ckg")   # 9 tools → kernel functions
```

---

## Published packages

<details open>
<summary><b>12 packages on PyPI · 100+ releases · 6 running as live MCP services</b></summary>
<br>

| package | serves |
|:--|:--|
| [**ckg-nvidia-ai**](https://pypi.org/project/ckg-nvidia-ai/) | NVIDIA developer stack — 20 domains, metered free tier, x402 payment challenge |
| [**ckg-nvidia-nemoclaw**](https://pypi.org/project/ckg-nvidia-nemoclaw/) | NemoClaw stack — typed traversal with per-node provenance |
| [**ckg-agentforce**](https://pypi.org/project/ckg-agentforce/) | Salesforce Agentforce — license-gated tool surface |
| [**langchain-ckg**](https://pypi.org/project/langchain-ckg/) | LangChain retriever — API-key auth, 402 handling |
| [**ckg-ai-platforms**](https://pypi.org/project/ckg-ai-platforms/) · [**ckg-nemotron-perplexity**](https://pypi.org/project/ckg-nemotron-perplexity/) · [**ckg-agent-protocols**](https://pypi.org/project/ckg-agent-protocols/) | domain graphs |

</details>

<details>
<summary><b>Also here</b></summary>
<br>

- **[zep-ckg](https://github.com/Yarmoluk/zep-ckg)** — Graphiti (Zep) plus CKG as a two-layer context agent
- **[Agent Skills](https://github.com/Yarmoluk/skills-1)** — public Claude Code skills

</details>

---

## Before this

Fifteen years of enterprise architecture. Fortune 500 AI delivery at **Slalom** across healthcare, retail and supply chain, including production-readiness and evaluation frameworks for HIPAA-regulated environments. Earlier: industrial IoT and commercial AI architecture at **West Monroe**, and a data science and IoT practice built from zero at **ATEK**.

Adjunct professor, **University of St. Thomas** — Graduate AI Systems. Featured in CIO Dive. Patent pending.

<div align="center">

**Open to AI Solutions Architect, Forward Deployed Engineer and Agentic AI Architect roles.**

[**Resume**](https://yarmoluk.github.io#resume) · [daniel.yarmoluk@gmail.com](mailto:daniel.yarmoluk@gmail.com)

</div>
