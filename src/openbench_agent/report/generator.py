"""Render a ResearchResult into Markdown and a self-contained HTML page.

Also maintains ``reports/latest.md``, ``reports/latest.html`` and an
``reports/index.html`` landing page that lists historical reports (for GitHub
Pages).
"""
from __future__ import annotations

import html
import json
import logging
from collections import defaultdict
from datetime import datetime
from pathlib import Path

from ..models import ResearchResult, RetrievedItem

logger = logging.getLogger(__name__)


class ReportGenerator:
    def __init__(self, config, output_dir: str | Path = "reports"):
        self.config = config
        self.report_cfg = getattr(config, "report", {}) or {}
        self.output_dir = Path(output_dir)

    # ------------------------------------------------------------------ API
    def generate(self, result: ResearchResult, fmt: str = "both") -> dict[str, Path]:
        """Write report files. Returns a mapping of format -> path."""
        self.output_dir.mkdir(parents=True, exist_ok=True)
        date_str = result.generated_at.strftime("%Y-%m-%d")
        written: dict[str, Path] = {}

        markdown = self._render_markdown(result)
        if fmt in ("md", "both"):
            md_path = self.output_dir / f"{date_str}.md"
            md_path.write_text(markdown, encoding="utf-8")
            (self.output_dir / "latest.md").write_text(markdown, encoding="utf-8")
            written["md"] = md_path
            logger.info("wrote %s", md_path)

        if fmt in ("html", "both"):
            page = self._render_html(result, markdown)
            html_path = self.output_dir / f"{date_str}.html"
            html_path.write_text(page, encoding="utf-8")
            (self.output_dir / "latest.html").write_text(page, encoding="utf-8")
            written["html"] = html_path
            self._update_index()
            logger.info("wrote %s", html_path)

        return written

    # -------------------------------------------------------------- markdown
    def _render_markdown(self, result: ResearchResult) -> str:
        title = self.report_cfg.get("title", "OpenBench Radar Digest")
        ts = result.generated_at.strftime("%Y-%m-%d %H:%M UTC")
        lines: list[str] = [
            f"# {title}",
            "",
            f"> Generated **{ts}** · {len(result.items)} items · "
            f"topics: {', '.join(result.topics)} · "
            f"analysis: {'LLM' if result.llm_used else 'extractive fallback'}",
            "",
            "## Executive Summary",
            "",
            result.executive_summary or "_No summary available._",
            "",
        ]

        if result.highlights:
            lines += ["## Key Highlights", ""]
            lines += [f"- {h}" for h in result.highlights]
            lines.append("")

        max_per = int(self.report_cfg.get("max_items_per_section", 12))
        if self.report_cfg.get("group_by_source", True):
            groups: dict[str, list[RetrievedItem]] = defaultdict(list)
            for it in result.items:
                groups[it.source].append(it)
            lines += ["## Findings by Source", ""]
            for source in sorted(groups):
                lines.append(f"### {source.capitalize()} ({len(groups[source])})")
                lines.append("")
                lines += self._item_lines(groups[source][:max_per])
                lines.append("")
        else:
            lines += ["## Findings", ""]
            lines += self._item_lines(result.items[:max_per])
            lines.append("")

        lines += [
            "---",
            "",
            "_Produced by [OpenBench Radar](https://github.com/) — automated "
            "benchmark retrieval, research & reporting._",
        ]
        return "\n".join(lines)

    def _item_lines(self, items: list[RetrievedItem]) -> list[str]:
        out: list[str] = []
        for it in items:
            meta = []
            if it.published:
                meta.append(it.published_str())
            if it.authors:
                meta.append(", ".join(it.authors[:3]) + ("…" if len(it.authors) > 3 else ""))
            dl = it.extra.get("downloads")
            if dl:
                meta.append(f"{dl:,} downloads")
            meta_str = f" · {' · '.join(meta)}" if meta else ""
            out.append(f"- **[{it.title}]({it.url})** _(score {it.score}{meta_str})_")
            if it.summary:
                out.append(f"  {it.summary[:280].strip()}")
        return out

    # ------------------------------------------------------------------ html
    def _render_html(self, result: ResearchResult, markdown: str) -> str:
        title = html.escape(self.report_cfg.get("title", "OpenBench Radar Digest"))
        ts = result.generated_at.strftime("%Y-%m-%d %H:%M UTC")

        highlights_html = ""
        if result.highlights:
            lis = "".join(f"<li>{html.escape(h)}</li>" for h in result.highlights)
            highlights_html = f"<h2>Key Highlights</h2><ul class='hl'>{lis}</ul>"

        cards = ""
        for it in result.items[: int(self.report_cfg.get("max_items_per_section", 12)) * 3]:
            cards += self._card_html(it)

        summary_html = html.escape(result.executive_summary).replace("\n\n", "</p><p>")
        badge = "LLM" if result.llm_used else "extractive"

        return _HTML_TEMPLATE.format(
            title=title,
            ts=ts,
            count=len(result.items),
            topics=html.escape(", ".join(result.topics)),
            badge=badge,
            summary=summary_html,
            highlights=highlights_html,
            cards=cards,
            year=datetime.utcnow().year,
        )

    def _card_html(self, it: RetrievedItem) -> str:
        meta = []
        if it.published:
            meta.append(it.published_str())
        dl = it.extra.get("downloads")
        if dl:
            meta.append(f"⬇ {dl:,}")
        likes = it.extra.get("likes")
        if likes:
            meta.append(f"♥ {likes:,}")
        meta_str = " · ".join(meta)
        return (
            "<div class='card'>"
            f"<span class='src src-{html.escape(it.source)}'>{html.escape(it.source)}</span>"
            f"<a class='card-title' href='{html.escape(it.url)}' target='_blank' "
            f"rel='noopener'>{html.escape(it.title)}</a>"
            f"<p class='card-sum'>{html.escape(it.summary[:260])}</p>"
            f"<div class='card-meta'>score {it.score}"
            + (f" · {html.escape(meta_str)}" if meta_str else "")
            + "</div></div>"
        )

    # ------------------------------------------------------------ index page
    def _update_index(self) -> None:
        history_size = int(self.report_cfg.get("history_size", 30))
        reports = sorted(
            (p for p in self.output_dir.glob("*.html") if p.stem not in ("latest", "index")),
            reverse=True,
        )[:history_size]
        items = "".join(
            f"<li><a href='{p.name}'>{p.stem}</a></li>" for p in reports
        )
        title = html.escape(self.report_cfg.get("title", "OpenBench Radar"))
        page = _INDEX_TEMPLATE.format(
            title=title, items=items, year=datetime.utcnow().year
        )
        (self.output_dir / "index.html").write_text(page, encoding="utf-8")


_HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>{title}</title>
<style>
  :root {{ --bg:#0d1117; --panel:#161b22; --border:#30363d; --fg:#e6edf3;
           --muted:#8b949e; --accent:#58a6ff; --green:#3fb950; --purple:#bc8cff; }}
  * {{ box-sizing:border-box; }}
  body {{ margin:0; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
          background:var(--bg); color:var(--fg); line-height:1.6; }}
  .wrap {{ max-width:920px; margin:0 auto; padding:32px 20px 80px; }}
  header h1 {{ font-size:1.9rem; margin:0 0 6px; }}
  .meta {{ color:var(--muted); font-size:.9rem; }}
  .badge {{ display:inline-block; background:var(--panel); border:1px solid var(--border);
            border-radius:999px; padding:1px 10px; font-size:.75rem; color:var(--accent); }}
  h2 {{ margin-top:38px; border-bottom:1px solid var(--border); padding-bottom:6px; }}
  .summary p {{ color:var(--fg); }}
  ul.hl li {{ margin:6px 0; }}
  .cards {{ display:grid; gap:14px; margin-top:16px; }}
  .card {{ background:var(--panel); border:1px solid var(--border); border-radius:10px;
           padding:14px 16px; }}
  .card-title {{ display:block; font-weight:600; color:var(--accent);
                 text-decoration:none; margin:6px 0; }}
  .card-title:hover {{ text-decoration:underline; }}
  .card-sum {{ color:var(--muted); font-size:.9rem; margin:6px 0; }}
  .card-meta {{ color:var(--muted); font-size:.78rem; }}
  .src {{ font-size:.7rem; text-transform:uppercase; letter-spacing:.5px;
          padding:2px 8px; border-radius:6px; background:#21262d; color:var(--muted); }}
  .src-arxiv {{ color:#ff7b72; }}
  .src-huggingface {{ color:var(--green); }}
  .src-web {{ color:var(--purple); }}
  footer {{ margin-top:60px; color:var(--muted); font-size:.8rem; text-align:center; }}
  a {{ color:var(--accent); }}
</style>
</head>
<body>
<div class="wrap">
  <header>
    <h1>📡 {title}</h1>
    <p class="meta">Generated {ts} · {count} items · topics: {topics}
      · <span class="badge">{badge}</span></p>
  </header>
  <section class="summary"><h2>Executive Summary</h2><p>{summary}</p></section>
  {highlights}
  <h2>Findings</h2>
  <div class="cards">{cards}</div>
  <footer>Produced by OpenBench Radar · © {year} · automated benchmark
    retrieval, research &amp; reporting</footer>
</div>
</body>
</html>"""


_INDEX_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>{title} — Reports</title>
<style>
  body {{ font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
          background:#0d1117; color:#e6edf3; max-width:720px; margin:0 auto;
          padding:40px 20px; line-height:1.7; }}
  h1 {{ font-size:1.8rem; }}
  a {{ color:#58a6ff; text-decoration:none; }}
  a:hover {{ text-decoration:underline; }}
  li {{ margin:6px 0; }}
  .cta {{ display:inline-block; margin:16px 0; padding:8px 16px; background:#161b22;
          border:1px solid #30363d; border-radius:8px; }}
  footer {{ margin-top:50px; color:#8b949e; font-size:.8rem; }}
</style>
</head>
<body>
  <h1>📡 {title}</h1>
  <a class="cta" href="latest.html">→ View latest digest</a>
  <h2>Archive</h2>
  <ul>{items}</ul>
  <footer>© {year} · OpenBench Radar</footer>
</body>
</html>"""
