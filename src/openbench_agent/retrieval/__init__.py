"""Retrieval sources registry and factory."""
from __future__ import annotations

import logging

from ..config import Config
from .arxiv_source import ArxivSource
from .base import BaseSource
from .huggingface_source import HuggingFaceSource
from .web_search import WebSearchSource

logger = logging.getLogger(__name__)

__all__ = [
    "BaseSource",
    "ArxivSource",
    "HuggingFaceSource",
    "WebSearchSource",
    "build_sources",
]


def build_sources(config: Config) -> list[BaseSource]:
    """Instantiate every enabled source based on the config."""
    sources: list[BaseSource] = []

    if config.source_enabled("arxiv"):
        sources.append(ArxivSource(config.source_cfg("arxiv")))

    if config.source_enabled("huggingface"):
        sources.append(HuggingFaceSource(config.source_cfg("huggingface")))

    if config.source_enabled("web"):
        web_cfg = dict(config.source_cfg("web"))
        web_cfg["tavily_api_key"] = config.tavily_api_key
        web_cfg["serper_api_key"] = config.serper_api_key
        web = WebSearchSource(web_cfg)
        if web.available:
            sources.append(web)
        else:
            logger.info("web source enabled but no API key present -> skipped")

    logger.info("active sources: %s", [s.name for s in sources])
    return sources
