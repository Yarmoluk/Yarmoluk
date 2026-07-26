"""
Fetch PostHog MCP telemetry + PyPI stats and rewrite the TELEMETRY block in README.md.
Runs daily via .github/workflows/update-stats.yml.

Required GitHub secrets:
  POSTHOG_API_KEY      — PostHog personal API key (phx_...)
  POSTHOG_PROJECT_ID   — PostHog project numeric ID
"""

import os
import re
import httpx
from datetime import datetime, timedelta

POSTHOG_API_KEY = os.environ.get("POSTHOG_API_KEY", "")
POSTHOG_PROJECT_ID = os.environ.get("POSTHOG_PROJECT_ID", "")
POSTHOG_BASE = "https://us.posthog.com"

PACKAGES = [
    "ckg-mcp",
    "ckg-nvidia-ai",
    "ckg-nvidia-nemoclaw",
    "ckg-agentforce",
    "ckg-nemotron-perplexity",
]


def posthog_event_count(event_name: str, days: int = 30) -> tuple[int, int]:
    """Returns (total_count, unique_users) for an event over the last N days."""
    if not POSTHOG_API_KEY or not POSTHOG_PROJECT_ID:
        return 0, 0
    try:
        r = httpx.post(
            f"{POSTHOG_BASE}/api/projects/{POSTHOG_PROJECT_ID}/query/",
            headers={"Authorization": f"Bearer {POSTHOG_API_KEY}", "Content-Type": "application/json"},
            json={
                "query": {
                    "kind": "EventsQuery",
                    "select": ["event", "count()", "count(distinct distinct_id)"],
                    "where": [f"event = '{event_name}'"],
                    "after": f"-{days}d",
                    "limit": 1,
                }
            },
            timeout=15,
        )
        rows = r.json().get("results", [])
        if rows:
            return int(rows[0][1]), int(rows[0][2])
        return 0, 0
    except Exception as e:
        print(f"PostHog error ({event_name}): {e}")
        return 0, 0


def pypi_monthly(package: str) -> int:
    try:
        r = httpx.get(
            f"https://pypistats.org/api/packages/{package}/recent",
            timeout=10,
        )
        return r.json()["data"]["last_month"]
    except Exception as e:
        print(f"PyPI error ({package}): {e}")
        return 0


def bar(value: int, max_val: int = 10000, width: int = 24) -> str:
    if max_val == 0:
        return "░" * width
    filled = min(int((value / max_val) * width), width)
    return "█" * filled + "░" * (width - filled)


def main():
    requests_30d, unique_users = posthog_event_count("mcp_request", days=30)
    rate_hits, hot_buyers = posthog_event_count("rate_limit_hit", days=30)
    total_monthly = sum(pypi_monthly(p) for p in PACKAGES)

    print(f"PyPI/month: {total_monthly:,}")
    print(f"MCP requests 30d: {requests_30d} ({unique_users} unique users)")
    print(f"Rate limit hits 30d: {rate_hits} ({hot_buyers} hot buyers)")

    pypi_bar = bar(total_monthly, max_val=8000)
    request_bar = bar(requests_30d, max_val=500)
    buyer_bar = bar(hot_buyers, max_val=20)

    block = f"""```
CONTEXT KING                              graphifymd.com · ckg-benchmark v0.6.2
─────────────────────────────────────────────────────────────────────────────────
 BENCHMARK F1    ████████████████░░░░░░░░  0.471  +283% vs RAG  +292% vs GraphRAG
 TOKENS/QUERY    ██████░░░░░░░░░░░░░░░░░░  269    vs 2,982 RAG        11× savings
 CKG DOMAINS     ████████████████████████  97     deployed · MCP-native · SHA-256
 PYPI / MONTH    {pypi_bar}  {total_monthly:,}  installs · 5 packages
 MCP REQUESTS    {request_bar}  {requests_30d}    30-day · {unique_users} unique users
 RATE LIMIT HITS {buyer_bar}  {hot_buyers}     active buyers hitting ceiling
─────────────────────────────────────────────────────────────────────────────────
 Own the context, rent the model.           Model for language, context for knowledge.
```"""

    readme_path = "README.md"
    with open(readme_path) as f:
        content = f.read()

    updated = re.sub(
        r"<!-- TELEMETRY_START -->.*?<!-- TELEMETRY_END -->",
        f"<!-- TELEMETRY_START -->\n{block}\n<!-- TELEMETRY_END -->",
        content,
        flags=re.DOTALL,
    )

    with open(readme_path, "w") as f:
        f.write(updated)

    print("README updated.")


if __name__ == "__main__":
    main()
