"""Base class and shared helpers for retrieval sources."""
from __future__ import annotations

import abc
import logging

from ..models import RetrievedItem

logger = logging.getLogger(__name__)


class BaseSource(abc.ABC):
    """A retrieval source turns a text query into a list of RetrievedItems.

    Subclasses implement :meth:`fetch`. They should never raise on network
    errors — instead log a warning and return an empty list, so one flaky
    source cannot break the whole pipeline.
    """

    #: short, stable identifier used in RetrievedItem.source and config keys
    name: str = "base"

    def __init__(self, config: dict | None = None):
        self.config = config or {}

    @property
    def max_items(self) -> int:
        return int(self.config.get("max_items", 15))

    @abc.abstractmethod
    def fetch(self, query: str, limit: int | None = None) -> list[RetrievedItem]:
        """Return items matching *query* (at most *limit*)."""
        raise NotImplementedError

    # -- convenience -------------------------------------------------------
    def _safe_fetch(self, query: str, limit: int | None = None) -> list[RetrievedItem]:
        try:
            return self.fetch(query, limit)
        except Exception as exc:  # pragma: no cover - defensive
            logger.warning("[%s] fetch failed for %r: %s", self.name, query, exc)
            return []
