"""Shared test fixtures."""
from datetime import datetime, timezone

import pytest

from openbench_agent.models import RetrievedItem


@pytest.fixture
def sample_items():
    now = datetime.now(timezone.utc)
    return [
        RetrievedItem(
            title="A new LLM evaluation benchmark for reasoning",
            url="https://arxiv.org/abs/2401.00001",
            source="arxiv",
            summary="We propose a benchmark to evaluate reasoning in LLMs.",
            published=now,
            tags=["cs.CL"],
        ),
        RetrievedItem(
            title="cool-dataset",
            url="https://huggingface.co/datasets/org/cool-dataset",
            source="huggingface",
            summary="A leaderboard dataset for evaluation.",
            published=now,
            extra={"downloads": 50000, "likes": 300, "kind": "datasets"},
        ),
        # Duplicate URL of the first item -> should be de-duplicated.
        RetrievedItem(
            title="A new LLM evaluation benchmark for reasoning (dup)",
            url="https://arxiv.org/abs/2401.00001",
            source="web",
            summary="duplicate",
        ),
        RetrievedItem(
            title="Unrelated cooking blog",
            url="https://example.com/cooking",
            source="web",
            summary="How to bake bread.",
        ),
    ]
