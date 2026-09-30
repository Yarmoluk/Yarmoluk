# Technical notes

[← Back to Daniel's profile](README.md)

## Context architecture

The [stack diagram](stack.svg) shows an agent reaching typed domain knowledge through context routing. A router selects the domain, subgraph, access level and traversal depth; MCP provides a common tool interface. Framework-specific integrations can also use their native APIs. Source URLs and SHA-256 hashes identify captured evidence behind graph declarations. A matching hash establishes byte identity, not the correctness of a claim.

## Protocol work

| Model Context Protocol | Agent-to-Agent |
|:--|:--|
| Tool and output schema design; JSON-RPC initialize handshake; streamable HTTP and SSE transport; session management; DNS-rebinding transport security; per-method metering; HTTP 402 payment rails; MCP-native observability. | Agent cards advertising skills, authentication, payment terms and machine-readable economics; x402 / HTTP 402; EIP-3009 signed authorizations; Coinbase CDP facilitator; Base settlement; ERC-8004 agent identity. |

MCP supplies a shared tool interface. Framework-specific integrations, such as [`langchain-ckg`](https://pypi.org/project/langchain-ckg/), can expose graph context through a native retriever API.

```python
# Microsoft Semantic Kernel consumes an MCP server directly.
from semantic_kernel import Kernel
from semantic_kernel.connectors.mcp import MCPStreamableHttpPlugin

async with MCPStreamableHttpPlugin(
    name="ckg", url="https://ckg-nvidia-ai.onrender.com/mcp"
) as plugin:
    kernel = Kernel()
    kernel.add_plugin(plugin, plugin_name="ckg")
```

## Other projects

- [zep-ckg](https://github.com/Yarmoluk/zep-ckg) — Graphiti (Zep) plus CKG as a two-layer context agent.
- [Agent Skills](https://github.com/Yarmoluk/skills-1) — public Claude Code skills.

## Benchmark scope

The [v0.6.2 paper](https://github.com/Yarmoluk/ckg-benchmark/blob/main/paper/main.pdf) compares CKG retrieval against RAG and Microsoft GraphRAG on 44 domains and 7,758 questions. The locked measurements are **CKG macro-F1 0.471, RAG 0.123, GraphRAG 0.120**; **269 versus 2,982 tokens per query** for CKG and RAG; and **five-hop F1 0.772 versus 0.170** for CKG and RAG. These are benchmark measurements, not a guarantee for a particular integration or customer workload. The repo includes a reconciliation of earlier cost figures that used different model prices for CKG and the baselines.
