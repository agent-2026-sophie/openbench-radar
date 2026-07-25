"""End-to-end orchestration: retrieve -> research -> report."""
from __future__ import annotations

import logging
from pathlib import Path

from .config import Config
from .models import ResearchResult, RetrievedItem
from .report.generator import ReportGenerator
from .research.analyzer import Analyzer
from .retrieval import build_sources

logger = logging.getLogger(__name__)


class Pipeline:
    def __init__(self, config: Config):
        self.config = config
        self.sources = build_sources(config)
        self.analyzer = Analyzer(config)

    # ------------------------------------------------------------- retrieve
    def retrieve(self, topics: list[str], max_items: int | None = None) -> list[RetrievedItem]:
        items: list[RetrievedItem] = []
        for source in self.sources:
            for topic in topics:
                fetched = source._safe_fetch(topic, max_items)
                items.extend(fetched)
        logger.info("retrieved %d raw items from %d sources", len(items), len(self.sources))
        return items

    # -------------------------------------------------------------- research
    def research(self, items: list[RetrievedItem], topics: list[str]) -> ResearchResult:
        return self.analyzer.analyze(items, topics)

    # ------------------------------------------------------------------ full
    def run(
        self,
        topics: list[str] | None = None,
        output_dir: str | Path = "reports",
        max_items: int | None = None,
        fmt: str = "both",
        dry_run: bool = False,
    ) -> tuple[ResearchResult, dict[str, Path]]:
        topics = topics or self.config.topics
        if not topics:
            raise ValueError("No topics configured. Set `topics` in config.yaml or pass --topics.")

        raw = self.retrieve(topics, max_items)
        result = self.research(raw, topics)

        written: dict[str, Path] = {}
        if not dry_run:
            generator = ReportGenerator(self.config, output_dir)
            written = generator.generate(result, fmt=fmt)
        return result, written
