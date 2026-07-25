"""Research stage: de-duplicate, rank, and synthesize retrieved items.

The heavy lifting (executive summary + highlights) is done by an LLM when an
OpenAI-compatible API key is available. Otherwise a deterministic *extractive*
fallback produces a useful summary from the highest-ranked items, so the agent
always yields a report.
"""
from __future__ import annotations

import logging
import textwrap
from collections import defaultdict

from ..config import Config
from ..models import RetrievedItem, ResearchResult

logger = logging.getLogger(__name__)


# --------------------------------------------------------------------------- #
# Ranking / de-duplication (pure functions, no external dependencies)
# --------------------------------------------------------------------------- #
def rank_and_dedup(
    items: list[RetrievedItem],
    keywords: list[str],
) -> list[RetrievedItem]:
    """De-duplicate by uid and assign a relevance score, most relevant first."""
    seen: dict[str, RetrievedItem] = {}
    for it in items:
        if it.uid not in seen:
            seen[it.uid] = it

    unique = list(seen.values())
    for it in unique:
        it.score = _score(it, keywords)

    unique.sort(key=lambda x: x.score, reverse=True)
    return unique


def _score(item: RetrievedItem, keywords: list[str]) -> float:
    """Heuristic relevance score.

    Combines keyword hits in title/summary, recency, and source popularity
    signals (HF downloads/likes). Kept simple and explainable on purpose.
    """
    text = f"{item.title} {item.summary} {' '.join(item.tags)}".lower()
    score = 0.0

    for kw in keywords:
        if kw in text:
            score += 2.0
    # Title hits weigh more.
    for kw in keywords:
        if kw in item.title.lower():
            score += 1.5

    # Recency bonus (newer = better), capped.
    if item.published:
        from datetime import datetime, timezone

        age_days = (datetime.now(timezone.utc) - item.published).days
        score += max(0.0, 3.0 - age_days / 15.0)

    # Popularity signals from Hugging Face.
    downloads = item.extra.get("downloads", 0) or 0
    likes = item.extra.get("likes", 0) or 0
    if downloads:
        score += min(3.0, downloads / 10000.0)
    if likes:
        score += min(2.0, likes / 100.0)

    return round(score, 3)


# --------------------------------------------------------------------------- #
# Analyzer
# --------------------------------------------------------------------------- #
class Analyzer:
    def __init__(self, config: Config):
        self.config = config

    def analyze(
        self,
        items: list[RetrievedItem],
        topics: list[str],
    ) -> ResearchResult:
        ranked = rank_and_dedup(items, self.config.relevance_keywords)

        if self.config.llm.available:
            try:
                summary, highlights = self._llm_synthesize(ranked, topics)
                return ResearchResult(
                    executive_summary=summary,
                    highlights=highlights,
                    items=ranked,
                    llm_used=True,
                    topics=topics,
                )
            except Exception as exc:  # pragma: no cover - network dependent
                logger.warning("LLM synthesis failed (%s); using fallback", exc)

        summary, highlights = self._extractive_summary(ranked, topics)
        return ResearchResult(
            executive_summary=summary,
            highlights=highlights,
            items=ranked,
            llm_used=False,
            topics=topics,
        )

    # ------------------------------------------------------------- LLM path
    def _llm_synthesize(self, items, topics) -> tuple[str, list[str]]:
        from openai import OpenAI

        client = OpenAI(
            api_key=self.config.llm.api_key,
            base_url=self.config.llm.base_url or None,
        )

        top = items[:25]
        catalog = "\n".join(
            f"- [{it.source}] {it.title} ({it.published_str()}) :: "
            f"{it.summary[:200]}"
            for it in top
        )
        prompt = textwrap.dedent(
            f"""
            You are a research analyst tracking AI/LLM **benchmarks and evaluations**.
            Topics of interest: {', '.join(topics)}.

            Below is a catalog of recently retrieved papers, datasets, models and web
            results. Write a concise **executive summary** (3-5 short paragraphs) of the
            most important developments, focusing on new benchmarks, notable results,
            leaderboards and evaluation methodology. Be specific and cite item titles.

            Then output a line containing exactly `HIGHLIGHTS:` followed by 4-7 bullet
            points (one per line, starting with `- `) capturing the single most important
            takeaways.

            CATALOG:
            {catalog}
            """
        ).strip()

        resp = client.chat.completions.create(
            model=self.config.llm.model,
            temperature=self.config.llm.temperature,
            max_tokens=self.config.llm.max_tokens,
            messages=[
                {"role": "system", "content": "You are a precise, concise research analyst."},
                {"role": "user", "content": prompt},
            ],
        )
        content = resp.choices[0].message.content or ""
        return _split_summary_highlights(content)

    # -------------------------------------------------------- extractive path
    def _extractive_summary(self, items, topics) -> tuple[str, list[str]]:
        if not items:
            return (
                "No relevant items were retrieved in this run. Try broadening the "
                "topics or extending the recency window in config.yaml.",
                [],
            )

        by_source: dict[str, int] = defaultdict(int)
        for it in items:
            by_source[it.source] += 1

        source_line = ", ".join(f"{n} from {s}" for s, n in sorted(by_source.items()))
        summary = (
            f"Retrieved **{len(items)}** relevant items across topics "
            f"({', '.join(topics)}): {source_line}. "
            "The most relevant findings, ranked by a keyword/recency/popularity "
            "heuristic, are listed below. (Set OPENAI_API_KEY to enable an "
            "LLM-written analytical summary.)"
        )

        highlights = []
        for it in items[:6]:
            tag = it.source
            highlights.append(f"[{tag}] {it.title} — {it.summary[:140].strip()}")
        return summary, highlights


def _split_summary_highlights(content: str) -> tuple[str, list[str]]:
    if "HIGHLIGHTS:" in content:
        summary_part, _, hl_part = content.partition("HIGHLIGHTS:")
    else:
        summary_part, hl_part = content, ""
    highlights = [
        line.lstrip("-* ").strip()
        for line in hl_part.splitlines()
        if line.strip().startswith(("-", "*"))
    ]
    return summary_part.strip(), highlights
