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


def posthog_event_count(event_name: str, days: int = 7) -> int:
    if not POSTHOG_API_KEY or not POSTHOG_PROJECT_ID:
        return 0
    after = (datetime.utcnow() - timedelta(days=days)).strftime("%Y-%m-%dT%H:%M:%S")
    try:
        r = httpx.get(
            f"{POSTHOG_BASE}/api/projects/{POSTHOG_PROJECT_ID}/events/",
            params={"event": event_name, "after": after, "limit": 1},
            headers={"Authorization": f"Bearer {POSTHOG_API_KEY}"},
            timeout=15,
        )
        return r.json().get("count", 0)
    except Exception as e:
        print(f"PostHog error ({event_name}): {e}")
        return 0


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
    installs_7d = posthog_event_count("startup_ping", days=7)
    requests_7d = posthog_event_count("mcp_request", days=7)
    total_monthly = sum(pypi_monthly(p) for p in PACKAGES)

    print(f"PyPI/month: {total_monthly:,}")
    print(f"MCP installs 7d: {installs_7d}")
    print(f"MCP requests 7d: {requests_7d}")

    pypi_bar = bar(total_monthly, max_val=8000)
    install_bar = bar(installs_7d, max_val=100)
    request_bar = bar(requests_7d, max_val=500)

    block = f"""```
CONTEXT KING                              graphifymd.com · ckg-benchmark v0.6.2
─────────────────────────────────────────────────────────────────────────────────
 BENCHMARK F1    ████████████████░░░░░░░░  0.471  +283% vs RAG  +292% vs GraphRAG
 TOKENS/QUERY    ██████░░░░░░░░░░░░░░░░░░  269    vs 2,982 RAG        11× savings
 CKG DOMAINS     ████████████████████████  97     deployed · MCP-native · SHA-256
 PYPI / MONTH    {pypi_bar}  {total_monthly:,}  installs · 5 packages
 MCP INSTALLS    {install_bar}  {installs_7d}     7-day · startup pings
 MCP REQUESTS    {request_bar}  {requests_7d}     7-day · live via PostHog
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
