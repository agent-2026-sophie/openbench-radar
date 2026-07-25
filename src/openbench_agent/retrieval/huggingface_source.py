"""Hugging Face retrieval source — datasets & models via the public Hub API (no key)."""
from __future__ import annotations

import logging
from datetime import datetime, timedelta, timezone

import requests

from ..models import RetrievedItem
from .base import BaseSource

logger = logging.getLogger(__name__)

HF_API = "https://huggingface.co/api"


class HuggingFaceSource(BaseSource):
    name = "huggingface"

    def fetch(self, query: str, limit: int | None = None) -> list[RetrievedItem]:
        limit = limit or self.max_items
        kinds = self.config.get("kinds", ["datasets", "models"])
        recency_days = int(self.config.get("recency_days", 180))
        cutoff = datetime.now(timezone.utc) - timedelta(days=recency_days)

        items: list[RetrievedItem] = []
        per_kind = max(1, limit // max(1, len(kinds)))
        for kind in kinds:
            items.extend(self._fetch_kind(kind, query, per_kind, cutoff))
        logger.info("[huggingface] %r -> %d items", query, len(items))
        return items

    def _fetch_kind(self, kind, query, limit, cutoff) -> list[RetrievedItem]:
        endpoint = f"{HF_API}/{kind}"
        params = {
            "search": query,
            "limit": limit,
            "sort": "lastModified",
            "direction": -1,
            "full": "true",
        }
        resp = requests.get(endpoint, params=params, timeout=30)
        resp.raise_for_status()
        results = []
        for row in resp.json():
            rid = row.get("id", "")
            if not rid:
                continue
            modified = _parse_dt(row.get("lastModified"))
            if modified and modified < cutoff:
                continue
            noun = "datasets" if kind == "datasets" else "models" if kind == "models" else kind
            url = f"https://huggingface.co/{'datasets/' if kind == 'datasets' else ''}{rid}"
            results.append(
                RetrievedItem(
                    title=rid,
                    url=url,
                    source=self.name,
                    summary=_describe(row, kind),
                    published=modified,
                    tags=row.get("tags", [])[:8],
                    extra={
                        "kind": kind,
                        "downloads": row.get("downloads", 0),
                        "likes": row.get("likes", 0),
                    },
                )
            )
        return results


def _describe(row: dict, kind: str) -> str:
    downloads = row.get("downloads", 0)
    likes = row.get("likes", 0)
    tags = ", ".join(row.get("tags", [])[:5])
    return (
        f"Hugging Face {kind[:-1] if kind.endswith('s') else kind} — "
        f"{downloads:,} downloads, {likes:,} likes. Tags: {tags or '—'}"
    )


def _parse_dt(value: str | None) -> datetime | None:
    if not value:
        return None
    for fmt in ("%Y-%m-%dT%H:%M:%S.%fZ", "%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%dT%H:%M:%S.%f%z"):
        try:
            dt = datetime.strptime(value, fmt)
            return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
        except (ValueError, TypeError):
            continue
    return None
