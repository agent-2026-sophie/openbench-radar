"""Core data structures shared across the pipeline."""
from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class RetrievedItem:
    """A single artifact discovered by a retrieval source.

    Sources normalize their heterogeneous results into this common shape so the
    research and report layers can stay source-agnostic.
    """

    title: str
    url: str
    source: str  # e.g. "arxiv", "huggingface", "web"
    summary: str = ""
    authors: list[str] = field(default_factory=list)
    published: Optional[datetime] = None
    tags: list[str] = field(default_factory=list)
    # Free-form extra metadata (downloads, likes, category, ...).
    extra: dict = field(default_factory=dict)
    # Relevance score assigned during ranking (higher = more relevant).
    score: float = 0.0

    @property
    def uid(self) -> str:
        """Stable identifier used for de-duplication across sources."""
        basis = (self.url or self.title).strip().lower()
        return hashlib.sha1(basis.encode("utf-8")).hexdigest()[:16]

    def published_str(self) -> str:
        return self.published.strftime("%Y-%m-%d") if self.published else "—"


@dataclass
class ResearchResult:
    """Output of the research/analysis stage."""

    executive_summary: str
    highlights: list[str] = field(default_factory=list)
    # Items after ranking / de-duplication, most relevant first.
    items: list[RetrievedItem] = field(default_factory=list)
    # Whether an LLM produced the summary (vs. the extractive fallback).
    llm_used: bool = False
    topics: list[str] = field(default_factory=list)
    generated_at: datetime = field(default_factory=datetime.utcnow)
