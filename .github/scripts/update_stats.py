"""Render the profile HUD from locked v0.6.2 benchmark results.

This panel reports benchmark measurements, not live customer telemetry.
No download-based usage extrapolation or estimated monthly savings.
"""

from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BENCHMARK_VERSION = "v0.6.2"


def generate_hud_svg():
    rows = [
        ("MACRO-F1", "0.471", "RAG 0.123", 0.471),
        ("TOKENS / QUERY", "269", "RAG 2,982", 269 / 2982),
        ("TOKEN REDUCTION", "91%", "relative to RAG", 1 - 269 / 2982),
        ("F1 AT FIVE HOPS", "0.772", "RAG 0.170", 0.772),
    ]
    blocks = []
    for index, (label, value, baseline, fraction) in enumerate(rows):
        y = 91 + index * 29
        blocks.append(f'<text x="26" y="{y}" fill="#7d8590">{escape(label)}</text>')
        for segment in range(12):
            color = "#3fb950" if segment < round(fraction * 12) else "#21262d"
            blocks.append(f'<rect x="{190 + segment * 8}" y="{y - 10}" width="5" height="11" fill="{color}"/>')
        blocks.append(f'<text x="320" y="{y}" fill="#3fb950" font-weight="700">{escape(value)}</text>')
        blocks.append(f'<text x="421" y="{y}" fill="#c9d1d9">{escape(baseline)}</text>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="640" height="254" viewBox="0 0 640 254" role="img" aria-labelledby="title desc">
  <title id="title">CKG benchmark {BENCHMARK_VERSION}</title>
  <desc id="desc">Macro-F1 0.471 versus RAG 0.123; 269 versus 2,982 tokens per query; 91 percent fewer tokens; five-hop F1 0.772 versus 0.170. Bars show F1 on a zero-to-one scale, token use relative to RAG, and the fraction of tokens saved. Locked benchmark results, not live usage.</desc>
  <rect width="640" height="254" rx="8" fill="#0d1117"/>
  <g font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="13">
    <text x="26" y="30" fill="#3fb950" font-weight="700">MODEL FOR LANGUAGE. CONTEXT FOR KNOWLEDGE.</text>
    <text x="26" y="50" fill="#7d8590" font-size="11">ckg-benchmark {BENCHMARK_VERSION} · locked results</text>
    <line x1="26" y1="64" x2="614" y2="64" stroke="#238636"/>
    {chr(10).join(blocks)}
    <line x1="26" y1="196" x2="614" y2="196" stroke="#238636"/>
    <text x="26" y="219" fill="#3fb950">Own the context, rent the model.</text>
    <text x="26" y="238" fill="#7d8590" font-size="10">Benchmark measurements · not live traffic or customer savings</text>
  </g>
</svg>
'''


def main():
    (ROOT / "hud.svg").write_text(generate_hud_svg(), encoding="utf-8")
    print(f"hud.svg rendered from locked {BENCHMARK_VERSION} benchmark results.")


if __name__ == "__main__":
    main()
