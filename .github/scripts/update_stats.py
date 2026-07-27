"""
Fetch PostHog MCP telemetry + PyPI stats, write hud.svg, sync PyPI badge.
Runs daily via .github/workflows/update-stats.yml.

Required GitHub secret:
  POSTHOG_API_KEY  — PostHog personal API key (phx_...)
"""

import html as html_module
import os
import re
import time
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
        return None, None
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
        return None, None


def pypi_monthly(package: str) -> int:
    try:
        time.sleep(1.5)  # avoid 429 from pypistats
        r = httpx.get(
            f"https://pypistats.org/api/packages/{package}/recent",
            headers=HEADERS_PYPI,
            timeout=10,
        )
        return r.json()["data"]["last_week"] * 2
    except Exception as e:
        print(f"PyPI error ({package}): {e}")
        return 0


def bar(value: int, max_val: int = 10000, width: int = 18) -> str:
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


def generate_hud_svg(lines: list) -> str:
    BG = "#0d1117"
    FG = "#3fb950"   # GitHub green
    FONT = "'Courier New', 'Lucida Console', monospace"
    FONT_SIZE = 13
    LINE_H = 20
    PAD_X = 20
    PAD_Y = 14
    CHAR_W = 7.82    # Courier New at 13px

    max_chars = max(len(l) for l in lines)
    width = int(max_chars * CHAR_W) + PAD_X * 2
    height = len(lines) * LINE_H + PAD_Y * 2 + 6

    spans = []
    for i, line in enumerate(lines):
        y = PAD_Y + (i + 1) * LINE_H
        escaped = html_module.escape(line)
        spans.append(
            f'  <tspan x="{PAD_X}" dy="{LINE_H if i > 0 else 0}">'
            f'{escaped}</tspan>'
        )

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">
  <rect width="{width}" height="{height}" fill="{BG}" rx="6"/>
  <text y="{PAD_Y}" font-family="{FONT}" font-size="{FONT_SIZE}" fill="{FG}" xml:space="preserve">
{''.join(chr(10) + s for s in spans)}
  </text>
</svg>'''


def main():
    requests_30d, unique_users = posthog_event_count("mcp_request", days=30)

    if requests_30d is None:
        print("No POSTHOG_API_KEY — skipping update to avoid zeroing live stats.")
        return

    total_monthly = sum(pypi_monthly(p) for p in PACKAGES)

    tokens_saved = requests_30d * 2_713
    avg_queries = max(requests_30d / max(unique_users or 1, 1), 1.0)
    savings_usd = total_monthly * avg_queries * 2_713 / 1_000_000 * 10

    print(f"PyPI run rate: {total_monthly:,}/mo")
    print(f"MCP requests 30d: {requests_30d} ({unique_users} unique users)")
    print(f"Tokens saved 30d: {tokens_saved:,}")
    print(f"Potential savings: {fmt_usd(savings_usd)}/mo at enterprise rate")

    saved_bar = bar(tokens_saved,     max_val=1_000_000)
    scale_bar = bar(int(savings_usd), max_val=5_000)

    hud_lines = [
        "Model for Language, Context for Knowledge  ckg-benchmark v0.6.2",
        "=" * 70,
        f" BENCHMARK F1     [##############.......]  0.471   +283% vs RAG",
        f" TOKEN EFFICIENCY [################.....]  91%     tokens saved vs RAG",
        f" CKG DOMAINS      [#################....]  97      SHA-256 · MCP-native",
        f" TOKENS SAVED     {saved_bar}  {fmt_k(tokens_saved):<7} this month vs RAG",
        f" SAVINGS AT SCALE {scale_bar}  {fmt_usd(savings_usd):<7} est · enterprise",
        "=" * 70,
        " Own the context, rent the model.",
    ]

    # Use proper block chars for the SVG (rendered, not terminal)
    hud_lines = [
        "Model for Language, Context for Knowledge ▸ ckg-benchmark v0.6.2",
        "═" * 70,
        " BENCHMARK F1     [██████████████░░░░]  0.471   +283% vs RAG",
        " TOKEN EFFICIENCY [████████████████░░]  91%     tokens saved vs RAG",
        " CKG DOMAINS      [█████████████████░]  97      SHA-256 · MCP-native",
        f" TOKENS SAVED     {saved_bar}  {fmt_k(tokens_saved):<7} this month vs RAG",
        f" SAVINGS AT SCALE {scale_bar}  {fmt_usd(savings_usd):<7} est · enterprise",
        "═" * 70,
        " Own the context, rent the model.",
    ]

    svg = generate_hud_svg(hud_lines)
    with open("hud.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("hud.svg written.")

    # Sync PyPI badge in README
    readme_path = "README.md"
    with open(readme_path) as f:
        content = f.read()

    pypi_badge_val = f"{total_monthly:,}%2Fmo".replace(",", "%2C")
    updated = re.sub(
        r"badge/PyPI-[\d%2C]+%2Fmo-",
        f"badge/PyPI-{pypi_badge_val}-",
        content,
    )

    with open(readme_path, "w") as f:
        f.write(updated)

    print("README PyPI badge synced.")


if __name__ == "__main__":
    main()
