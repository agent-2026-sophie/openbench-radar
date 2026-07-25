from openbench_agent.config import Config
from openbench_agent.models import ResearchResult
from openbench_agent.research.analyzer import Analyzer, rank_and_dedup

KEYWORDS = ["benchmark", "evaluation", "leaderboard", "dataset"]


def test_dedup_removes_duplicate_urls(sample_items):
    ranked = rank_and_dedup(sample_items, KEYWORDS)
    urls = [it.url for it in ranked]
    assert len(urls) == len(set(urls))
    # 4 items in, 1 duplicate -> 3 out
    assert len(ranked) == 3


def test_ranking_prioritizes_relevant_items(sample_items):
    ranked = rank_and_dedup(sample_items, KEYWORDS)
    # The unrelated cooking blog should rank last.
    assert "cooking" in ranked[-1].url
    # Scores are sorted descending.
    scores = [it.score for it in ranked]
    assert scores == sorted(scores, reverse=True)


def test_extractive_fallback_when_no_key(sample_items):
    cfg = Config(relevance_keywords=KEYWORDS)
    cfg.llm.api_key = None  # force fallback
    result = Analyzer(cfg).analyze(sample_items, topics=["benchmark"])
    assert isinstance(result, ResearchResult)
    assert result.llm_used is False
    assert result.executive_summary
    assert len(result.items) == 3


def test_empty_input_produces_graceful_summary():
    cfg = Config(relevance_keywords=KEYWORDS)
    cfg.llm.api_key = None
    result = Analyzer(cfg).analyze([], topics=["benchmark"])
    assert result.items == []
    assert "No relevant items" in result.executive_summary
