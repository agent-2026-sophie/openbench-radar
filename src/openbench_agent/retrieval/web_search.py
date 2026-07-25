"""Web search source — supports Tavily and Serper. Skipped silently if no key."""
from __future__ import annotations

import logging

import requests

from ..models import RetrievedItem
from .base import BaseSource

logger = logging.getLogger(__name__)


class WebSearchSource(BaseSource):
    """Pluggable web search.

    Provide either a Tavily key (``tavily_api_key``) or a Serper key
    (``serper_api_key``) via the constructor config. If neither is present the
    source returns nothing rather than raising.
    """

    name = "web"

    def __init__(self, config: dict | None = None):
        super().__init__(config)
        self.tavily_key = (config or {}).get("tavily_api_key")
        self.serper_key = (config or {}).get("serper_api_key")

    @property
    def available(self) -> bool:
        return bool(self.tavily_key or self.serper_key)

    def fetch(self, query: str, limit: int | None = None) -> list[RetrievedItem]:
        limit = limit or self.max_items
        if self.tavily_key:
            return self._tavily(query, limit)
        if self.serper_key:
            return self._serper(query, limit)
        logger.info("[web] no search API key configured; skipping")
        return []

    # ---------------------------------------------------------------- Tavily
    def _tavily(self, query: str, limit: int) -> list[RetrievedItem]:
        resp = requests.post(
            "https://api.tavily.com/search",
            json={
                "api_key": self.tavily_key,
                "query": query,
                "max_results": limit,
                "search_depth": "basic",
            },
            timeout=30,
        )
        resp.raise_for_status()
        items = []
        for r in resp.json().get("results", []):
            items.append(
                RetrievedItem(
                    title=r.get("title", ""),
                    url=r.get("url", ""),
                    source=self.name,
                    summary=(r.get("content", "") or "")[:600],
                    extra={"relevance": r.get("score")},
                )
            )
        logger.info("[web/tavily] %r -> %d items", query, len(items))
        return items

    # ---------------------------------------------------------------- Serper
    def _serper(self, query: str, limit: int) -> list[RetrievedItem]:
        resp = requests.post(
            "https://google.serper.dev/search",
            headers={"X-API-KEY": self.serper_key, "Content-Type": "application/json"},
            json={"q": query, "num": limit},
            timeout=30,
        )
        resp.raise_for_status()
        items = []
        for r in resp.json().get("organic", [])[:limit]:
            items.append(
                RetrievedItem(
                    title=r.get("title", ""),
                    url=r.get("link", ""),
                    source=self.name,
                    summary=(r.get("snippet", "") or "")[:600],
                )
            )
        logger.info("[web/serper] %r -> %d items", query, len(items))
        return items
