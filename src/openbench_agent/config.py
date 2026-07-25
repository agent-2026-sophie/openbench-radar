"""Configuration loading (YAML file + environment variables)."""
from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml


def _load_dotenv(path: str = ".env") -> None:
    """Minimal .env loader (avoids a hard dependency on python-dotenv).

    Only sets variables that are not already present in the environment.
    """
    p = Path(path)
    if not p.exists():
        return
    for raw in p.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key, value = key.strip(), value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


@dataclass
class LLMConfig:
    model: str = "gpt-4o-mini"
    base_url: str | None = None
    api_key: str | None = None
    temperature: float = 0.3
    max_tokens: int = 2000
    fallback_when_no_key: bool = True

    @property
    def available(self) -> bool:
        return bool(self.api_key)


@dataclass
class Config:
    topics: list[str] = field(default_factory=list)
    relevance_keywords: list[str] = field(default_factory=list)
    sources: dict[str, Any] = field(default_factory=dict)
    llm: LLMConfig = field(default_factory=LLMConfig)
    report: dict[str, Any] = field(default_factory=dict)
    # Populated from env, not the YAML file.
    tavily_api_key: str | None = None
    serper_api_key: str | None = None

    # --------------------------------------------------------------- loading
    @classmethod
    def load(cls, path: str | os.PathLike = "config/config.yaml") -> "Config":
        _load_dotenv()

        data: dict[str, Any] = {}
        p = Path(path)
        if p.exists():
            data = yaml.safe_load(p.read_text(encoding="utf-8")) or {}

        llm_data = data.get("llm", {}) or {}
        llm = LLMConfig(
            model=os.environ.get("OPENAI_MODEL", llm_data.get("model", "gpt-4o-mini")),
            base_url=os.environ.get("OPENAI_BASE_URL", llm_data.get("base_url")),
            api_key=os.environ.get("OPENAI_API_KEY"),
            temperature=float(llm_data.get("temperature", 0.3)),
            max_tokens=int(llm_data.get("max_tokens", 2000)),
            fallback_when_no_key=bool(llm_data.get("fallback_when_no_key", True)),
        )

        return cls(
            topics=data.get("topics", []),
            relevance_keywords=[k.lower() for k in data.get("relevance_keywords", [])],
            sources=data.get("sources", {}),
            llm=llm,
            report=data.get("report", {}),
            tavily_api_key=os.environ.get("TAVILY_API_KEY"),
            serper_api_key=os.environ.get("SERPER_API_KEY"),
        )

    # --------------------------------------------------------------- helpers
    def source_cfg(self, name: str) -> dict[str, Any]:
        return self.sources.get(name, {}) or {}

    def source_enabled(self, name: str) -> bool:
        return bool(self.source_cfg(name).get("enabled", False))
