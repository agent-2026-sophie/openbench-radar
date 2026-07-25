"""arXiv retrieval source — uses the public arXiv Atom API (no key required)."""
from __future__ import annotations

import logging
import time
from datetime import datetime, timedelta, timezone
from urllib.parse import quote_plus

import feedparser
import requests

from ..models import RetrievedItem
from .base import BaseSource

logger = logging.getLogger(__name__)

ARXIV_API = "http://export.arxiv.org/api/query"


class ArxivSource(BaseSource):
    name = "arxiv"

    def fetch(self, query: str, limit: int | None = None) -> list[RetrievedItem]:
        limit = limit or self.max_items
        categories = self.config.get("categories", [])
        recency_days = int(self.config.get("recency_days", 30))

        # Build the arXiv search string. AND-ing individual terms is more robust
        # across phrasings than an exact-phrase match, while staying on-topic.
        terms = [t for t in query.split() if len(t) > 1]
        term_clause = " AND ".join(f"all:{t}" for t in terms) if terms else f'all:"{query}"'
        search = f"({term_clause})"
        if categories:
            cat_clause = " OR ".join(f"cat:{c}" for c in categories)
            search = f"{search} AND ({cat_clause})"

        params = (
            f"search_query={quote_plus(search)}"
            f"&start=0&max_results={limit}"
            "&sortBy=submittedDate&sortOrder=descending"
        )
        resp = requests.get(f"{ARXIV_API}?{params}", timeout=30)
        resp.raise_for_status()
        feed = feedparser.parse(resp.content)
        # arXiv API guidelines recommend >=3s between requests; be a good citizen.
        time.sleep(float(self.config.get("request_delay", 3.0)))

        cutoff = datetime.now(timezone.utc) - timedelta(days=recency_days)
        items: list[RetrievedItem] = []
        for entry in feed.entries:
            published = _parse_dt(entry.get("published"))
            if published and published < cutoff:
                continue
            items.append(
                RetrievedItem(
                    title=_clean(entry.get("title", "")),
                    url=entry.get("link", ""),
                    source=self.name,
                    summary=_clean(entry.get("summary", ""))[:600],
                    authors=[a.get("name", "") for a in entry.get("authors", [])],
                    published=published,
                    tags=[t.get("term", "") for t in entry.get("tags", [])],
                    extra={"arxiv_id": entry.get("id", "")},
                )
            )
        logger.info("[arxiv] %r -> %d items", query, len(items))
        return items


def _clean(text: str) -> str:
    return " ".join(text.split())


def _parse_dt(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        return datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    except (ValueError, TypeError):
        return None
