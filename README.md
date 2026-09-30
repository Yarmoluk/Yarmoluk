<div align="center">

<img src="stack.svg" alt="Context architecture: agents connect through MCP and context routing to typed knowledge graphs, with source URLs and SHA-256 hashes on captured evidence." width="640">

**Agents → context routing over MCP → Compressed Knowledge Graphs → source evidence.**

### Hi, I'm Daniel 👋

**Forward Deployed Engineer · AI Solutions Architect · Minneapolis, MN**

I work on **context architecture** — the layer between an agent and everything it is
expected to know. **Context routing** decides which knowledge an agent gets and what it
costs to get it. The **knowledge layer** underneath is typed and traversable, giving
agents declared relationships and source evidence they can cite.

Fifteen years of enterprise architecture, most recently at Slalom delivering Fortune 500 AI.
I like the deployed half of the job: the customer's environment, their constraints, the
failure modes that never show up in a demo.

**Measured on the public benchmark: 3.8× macro-F1 versus RAG.**

[![Benchmark](https://img.shields.io/badge/benchmark-v0.6.2-1f6feb?style=flat-square)](https://github.com/Yarmoluk/ckg-benchmark/blob/main/paper/main.pdf)
[![Domains](https://img.shields.io/badge/domain_graphs-explore-0f6e56?style=flat-square)](https://graphifymd.com)
[![PyPI](https://img.shields.io/badge/PyPI-packages-3775A9?style=flat-square&logo=pypi&logoColor=white)](https://pypi.org/user/danyarm/)
[![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97-danyarm-f59e0b?style=flat-square)](https://huggingface.co/danyarm)
[![Patent](https://img.shields.io/badge/patent-pending-7c3aed?style=flat-square)](https://graphifymd.com)

**[Portfolio &amp; resume &rarr;](https://yarmoluk.github.io)**

[Contact about a role](mailto:daniel.yarmoluk@gmail.com?subject=Forward%20deployed%20engineering%20role) · [Discuss a project](mailto:daniel.yarmoluk@gmail.com?subject=Context%20architecture%20project) · [LinkedIn](https://linkedin.com/in/danyarmoluk)

</div>

---

## What I build

| Work | What it involves | Explore |
|:--|:--|:--|
| **Context architecture** | Route a question to the relevant domain, subgraph and traversal depth; return typed relationships with source evidence. | [Graphify.md](https://graphifymd.com) |
| **Agent integrations** | Deliver local graph context through LangChain and LangGraph, or connect a hosted graph through MCP. | [CKGRetriever in LangChain's directory](https://docs.langchain.com/oss/python/integrations/retrievers#:~:text=CKGRetriever) |
| **Deployed systems** | Work through transport behavior, tool schemas, access controls, metering and observability. | [ckg-nvidia-ai](https://github.com/Yarmoluk/ckg-nvidia-ai) |
| **Evaluation** | Compare answer quality, context size and multi-hop performance against explicit baselines. | [ckg-benchmark](https://github.com/Yarmoluk/ckg-benchmark) |

My focus is the whole path: the customer's source material, the context an agent receives,
and the behavior we can inspect after deployment.

---

## LangChain and LangGraph

I built [`langchain-ckg`](https://pypi.org/project/langchain-ckg/), an independently maintained retriever that turns graph lookups into LangChain `Document` results. `CKGRetriever` appears in [LangChain's retriever directory](https://docs.langchain.com/oss/python/integrations/retrievers#:~:text=CKGRetriever). The reviewed release bundles 11 domain graphs and can run locally without an embedding API. It can also be wrapped as a LangChain tool or used inside a LangGraph workflow.

That work connects to the part of deployed engineering I care about: getting useful context into an agent, making the result inspectable, and testing how it behaves in a real workflow. The [package](https://pypi.org/project/langchain-ckg/) and [benchmark paper](https://github.com/Yarmoluk/ckg-benchmark/blob/main/paper/main.pdf) are separate projects; the benchmark measures CKG retrieval, not a performance guarantee for this integration.

---

## Work with me

I help teams with two practical jobs:

1. **Context architecture review.** Map one agent workflow, trace where its knowledge comes from, and identify the retrieval, access and evaluation gaps that matter in deployment.
2. **CKG pilot.** Turn a bounded set of trusted documents into a source-traceable graph, connect it to the team's agent stack, and compare it with the existing retrieval path on agreed questions.

**[Discuss a project →](mailto:daniel.yarmoluk@gmail.com?subject=Context%20architecture%20project)**

For a hands-on starting point, install the [public `langchain-ckg` package](https://pypi.org/project/langchain-ckg/). Hosted integration and billing are separate from that local package.

---

## The Compressed Knowledge Graph

A CKG stores relationships as **typed, authored edges** and traverses them. Source URLs and SHA-256 hashes identify the captured evidence behind graph declarations. A hash verifies which bytes were captured; it does not, by itself, prove that an answer is correct.

<p align="center">
  <img src="hud.svg" alt="Locked CKG benchmark v0.6.2: macro-F1 0.471 versus RAG 0.123; 269 versus 2,982 tokens per query; five-hop F1 0.772 versus 0.170." width="640">
</p>

**Benchmarked against RAG and Microsoft GraphRAG** — 44 domains, 7,758 queries, locked at v0.6.2:

| | **CKG** | RAG | GraphRAG |
|:--|--:|--:|--:|
| macro-F1 | **0.471** | 0.123 | 0.120 |
| tokens per query | **269** | 2,982 | — |
| F1 at 5-hop depth | **0.772** | 0.170 | — |

The last row matters most. The advantage **grows with question complexity**, because multi-hop composition is exactly where embedding methods are weakest.

**[Read the benchmark paper](https://github.com/Yarmoluk/ckg-benchmark/blob/main/paper/main.pdf)** · [Clone and re-run it](https://github.com/Yarmoluk/ckg-benchmark) · [Dataset on Hugging Face](https://huggingface.co/datasets/danyarm/ckg-benchmark) (CC-BY-4.0)

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

**Framework choice stays with the caller.** MCP provides a shared tool interface; framework-specific integrations such as `langchain-ckg` can expose graph context through their native retriever APIs.

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
<summary><b>Published packages and MCP integrations</b></summary>
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

[**Resume**](https://yarmoluk.github.io#resume) · [**Discuss a project**](mailto:daniel.yarmoluk@gmail.com?subject=Context%20architecture%20project)

</div>
