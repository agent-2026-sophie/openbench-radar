# OpenBench Radar 📡

**Automated retrieval, research, and reporting agent for open AI / LLM benchmarks.**

OpenBench Radar continuously scans open sources (arXiv, Hugging Face, and the web) for the
latest AI/LLM **benchmarks, leaderboards and evaluations**, uses an LLM to research and
synthesize what it finds, and produces a clean **Markdown + HTML summary report**.

It is designed to be **deployed on GitHub**: run it locally as a CLI, or let a scheduled
**GitHub Action** run it for you and publish the reports to your repo and **GitHub Pages**.

```
 sources ──► retrieval ──► research (LLM) ──► report (MD + HTML) ──► GitHub / Pages
 (arXiv,        │              │                    │
  HF, web)      └── dedup      └── analysis          └── daily/weekly digest
```

---

## ✨ Features

- **Multi-source retrieval** — arXiv (free), Hugging Face datasets/models (free), and pluggable
  web search (Tavily / Serper). Each source is a small, self-contained plugin.
- **LLM-powered research** — clusters, ranks and summarizes findings into an executive digest.
  Uses any OpenAI-compatible API. **Falls back to an extractive summary when no key is set**,
  so it always produces a report.
- **Clean reports** — timestamped Markdown + a self-contained responsive HTML page suitable
  for GitHub Pages.
- **Works out-of-the-box** — arXiv + Hugging Face require **no API keys**.
- **GitHub-native** — includes a scheduled workflow that runs the pipeline, commits reports,
  and deploys the HTML digest to GitHub Pages.
- **Fully configurable** — topics, keywords, source toggles and limits live in `config/config.yaml`.

## 🚀 Quick start (local)

```bash
git clone <your-fork-url> && cd openbench-radar
python -m venv .venv && source .venv/bin/activate
pip install -e .            # or: pip install -r requirements.txt (then set PYTHONPATH=src)

# Run with defaults (arXiv + Hugging Face, no keys needed)
openbench-agent run          # equivalent to: python -m openbench_agent.cli run

# Reports are written to ./reports/
open reports/latest.html   # or reports/<date>.md
```

### Enable smarter research (optional)

Set environment variables (or a `.env` file) to unlock LLM synthesis and web search:

```bash
export OPENAI_API_KEY="sk-..."          # any OpenAI-compatible key
export OPENAI_BASE_URL="https://api.openai.com/v1"   # optional, for compatible endpoints
export OPENAI_MODEL="gpt-4o-mini"        # optional, defaults in config.yaml

export TAVILY_API_KEY="tvly-..."         # optional web search (or SERPER_API_KEY)
```

Then run again — the report will include an LLM-written executive summary and web results.

## 🛠️ CLI

```bash
python -m openbench_agent.cli run [options]

  --config PATH        Path to config file (default: config/config.yaml)
  --output DIR         Output directory for reports (default: reports)
  --topics "a,b,c"     Override topics from config
  --max-items N        Max items per source
  --no-llm             Force the extractive fallback (skip LLM)
  --format {md,html,both}   Report format (default: both)
  --dry-run            Retrieve + analyze but don't write files
  -v/--verbose         Verbose logging
```

## 📁 Project layout

```
openbench-radar/
├── config/config.yaml            # topics, sources, LLM settings
├── src/openbench_agent/
│   ├── config.py                 # config + env loading
│   ├── models.py                 # dataclasses (RetrievedItem, ...)
│   ├── retrieval/                # source plugins
│   │   ├── base.py  arxiv_source.py  huggingface_source.py  web_search.py
│   ├── research/analyzer.py      # LLM research + extractive fallback
│   ├── report/generator.py       # Markdown + HTML rendering
│   ├── pipeline.py               # orchestration
│   └── cli.py                    # command line entry point
├── .github/workflows/            # scheduled automation + Pages deploy
├── tests/                        # unit tests
├── examples/                     # sample output
└── reports/                      # generated reports (git-tracked)
```

## 🤖 Deploy on GitHub

1. Push this repo to GitHub.
2. (Optional) Add repository **secrets** for smarter output:
   `OPENAI_API_KEY`, `OPENAI_BASE_URL`, `OPENAI_MODEL`, `TAVILY_API_KEY`.
3. Enable **GitHub Pages** → *Build and deployment* → Source: **GitHub Actions**.
4. The workflow in `.github/workflows/benchmark-research.yml` runs on a schedule
   (default: daily 08:00 UTC), commits new reports under `reports/`, and publishes
   `reports/latest.html` to Pages. You can also trigger it manually from the Actions tab.

See [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md) for details.

## 🧩 Extending

Add a new source by subclassing `BaseSource` in `src/openbench_agent/retrieval/` and
registering it in `retrieval/__init__.py`. Each source only needs a `fetch(query, limit)`
method returning `List[RetrievedItem]`.

## 📝 License

MIT — see [LICENSE](LICENSE).
