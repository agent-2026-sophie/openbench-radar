from openbench_agent.config import Config
from openbench_agent.models import ResearchResult
from openbench_agent.report.generator import ReportGenerator


def _result(sample_items):
    return ResearchResult(
        executive_summary="Two relevant benchmarks appeared this week.\n\nThey matter.",
        highlights=["New reasoning benchmark", "Popular HF dataset"],
        items=sample_items,
        llm_used=False,
        topics=["benchmark"],
    )


def test_generate_writes_md_and_html(tmp_path, sample_items):
    cfg = Config(report={"title": "Test Digest", "group_by_source": True})
    gen = ReportGenerator(cfg, output_dir=tmp_path)
    written = gen.generate(_result(sample_items), fmt="both")

    assert written["md"].exists()
    assert written["html"].exists()
    assert (tmp_path / "latest.md").exists()
    assert (tmp_path / "latest.html").exists()
    assert (tmp_path / "index.html").exists()


def test_markdown_contains_key_sections(tmp_path, sample_items):
    cfg = Config(report={"title": "Test Digest"})
    gen = ReportGenerator(cfg, output_dir=tmp_path)
    gen.generate(_result(sample_items), fmt="md")
    md = (tmp_path / "latest.md").read_text(encoding="utf-8")

    assert "# Test Digest" in md
    assert "## Executive Summary" in md
    assert "## Key Highlights" in md
    assert "arxiv.org" in md


def test_html_is_self_contained(tmp_path, sample_items):
    cfg = Config(report={"title": "Test Digest"})
    gen = ReportGenerator(cfg, output_dir=tmp_path)
    gen.generate(_result(sample_items), fmt="html")
    page = (tmp_path / "latest.html").read_text(encoding="utf-8")

    assert page.startswith("<!DOCTYPE html>")
    assert "<style>" in page          # inline CSS -> no external deps
    assert "Executive Summary" in page
