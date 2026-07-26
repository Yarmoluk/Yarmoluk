"""
Fetch PostHog MCP telemetry + PyPI stats and rewrite the TELEMETRY block in README.md.
Runs daily via .github/workflows/update-stats.yml.

Required GitHub secret:
  POSTHOG_API_KEY  — PostHog personal API key (phx_...)
"""

import os
import re
import httpx

POSTHOG_API_KEY = os.environ.get("POSTHOG_API_KEY", "")
POSTHOG_PROJECT_ID = "526902"
POSTHOG_BASE = "https://us.posthog.com"

PACKAGES = [
    "ckg-mcp",
    "ckg-nvidia-ai",
    "ckg-nvidia-nemoclaw",
    "ckg-agentforce",
    "ckg-nemotron-perplexity",
]

HEADERS_PYPI = {"User-Agent": "github-actions/ckg-stats-updater"}


def posthog_event_count(event_name: str, days: int = 30) -> tuple[int, int]:
    """Returns (total_count, unique_users) for an event over the last N days."""
    if not POSTHOG_API_KEY:
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
            headers=HEADERS_PYPI,
            timeout=10,
        )
        return r.json()["data"]["last_month"]
    except Exception as e:
        print(f"PyPI error ({package}): {e}")
        return 0


def bar(value: int, max_val: int = 10000, width: int = 18) -> str:
    """Return a bracketed [▓▓▓░░░] bar of fixed width."""
    if max_val == 0:
        return "[" + "░" * width + "]"
    filled = min(int((value / max_val) * width), width)
    return "[" + "▓" * filled + "░" * (width - filled) + "]"


def fmt_k(n: int) -> str:
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M"
    if n >= 1000:
        return f"{n // 1000}k"
    return str(n)


def fmt_usd(n: float) -> str:
    if n >= 1000:
        return f"${n / 1000:.1f}k"
    return f"${n:.0f}"


def main():
    requests_30d, unique_users = posthog_event_count("mcp_request", days=30)
    total_monthly = sum(pypi_monthly(p) for p in PACKAGES)

    # Tokens saved: actual queries × per-query delta vs RAG (2,982 - 269 = 2,713)
    tokens_saved = requests_30d * 2_713

    # Savings at scale: monthly PyPI installs × avg queries/user × $10/1M enterprise rate
    avg_queries = max(requests_30d / max(unique_users, 1), 1.0)
    savings_usd = total_monthly * avg_queries * 2_713 / 1_000_000 * 10

    print(f"PyPI/month: {total_monthly:,}")
    print(f"MCP requests 30d: {requests_30d} ({unique_users} unique users)")
    print(f"Tokens saved 30d: {tokens_saved:,}")
    print(f"Potential savings: {fmt_usd(savings_usd)}/mo at enterprise rate")

    pypi_bar   = bar(total_monthly,    max_val=8_000)
    saved_bar  = bar(tokens_saved,     max_val=1_000_000)
    scale_bar  = bar(int(savings_usd), max_val=5_000)

    G = "\x1b[92m"   # bright green
    R = "\x1b[0m"    # reset

    block = f"""```ansi
{G}CONTEXT KING ▸ ckg-benchmark v0.6.2        graphifymd.com
══════════════════════════════════════════════════════════════════════════
 BENCHMARK F1     [▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░]  0.471   +283% vs RAG
 TOKEN EFFICIENCY [▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░]  91%     tokens saved vs RAG
 CKG DOMAINS      [▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░]  97      SHA-256 · MCP-native
 PYPI / MONTH     {pypi_bar}  {total_monthly:,}   downloads / month
 TOKENS SAVED     {saved_bar}  {fmt_k(tokens_saved)}    this month vs RAG
 SAVINGS AT SCALE {scale_bar}  {fmt_usd(savings_usd)}   est · enterprise
══════════════════════════════════════════════════════════════════════════
 Own the context, rent the model.{R}
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
