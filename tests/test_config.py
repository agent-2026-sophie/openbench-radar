import textwrap

from openbench_agent.config import Config
from openbench_agent.retrieval import build_sources


def test_config_load_from_yaml(tmp_path):
    cfg_file = tmp_path / "config.yaml"
    cfg_file.write_text(
        textwrap.dedent(
            """
            topics: ["benchmark a", "benchmark b"]
            relevance_keywords: ["Benchmark", "EVAL"]
            sources:
              arxiv: { enabled: true, max_items: 5 }
              huggingface: { enabled: false }
              web: { enabled: true }
            llm:
              model: test-model
              temperature: 0.1
            report:
              title: My Digest
            """
        ),
        encoding="utf-8",
    )
    cfg = Config.load(cfg_file)
    assert cfg.topics == ["benchmark a", "benchmark b"]
    # keywords are lower-cased on load
    assert cfg.relevance_keywords == ["benchmark", "eval"]
    assert cfg.source_enabled("arxiv") is True
    assert cfg.source_enabled("huggingface") is False
    assert cfg.llm.model == "test-model"
    assert cfg.report["title"] == "My Digest"


def test_build_sources_respects_enabled(tmp_path, monkeypatch):
    monkeypatch.delenv("TAVILY_API_KEY", raising=False)
    monkeypatch.delenv("SERPER_API_KEY", raising=False)
    cfg = Config(
        sources={
            "arxiv": {"enabled": True},
            "huggingface": {"enabled": True},
            "web": {"enabled": True},  # no key -> skipped
        }
    )
    sources = build_sources(cfg)
    names = {s.name for s in sources}
    assert "arxiv" in names
    assert "huggingface" in names
    # web has no API key -> not included
    assert "web" not in names


def test_missing_config_file_is_ok(tmp_path, monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    cfg = Config.load(tmp_path / "does-not-exist.yaml")
    assert cfg.topics == []
    assert cfg.llm.available is False
