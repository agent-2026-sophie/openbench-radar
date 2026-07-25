# Deployment guide

OpenBench Radar is built to live in a GitHub repository and run itself on a schedule.

## 1. Put it on GitHub

```bash
# from the project root
git init
git add .
git commit -m "init: OpenBench Radar"
git branch -M main
git remote add origin https://github.com/<you>/openbench-radar.git
git push -u origin main
```

## 2. (Optional) Add secrets for smarter output

The pipeline works with **no secrets** (arXiv + Hugging Face). To enable the
LLM-written executive summary and web search, add repository secrets under
**Settings → Secrets and variables → Actions**:

| Secret | Purpose | Required |
|---|---|---|
| `OPENAI_API_KEY` | LLM synthesis (any OpenAI-compatible key) | optional |
| `OPENAI_BASE_URL` | custom OpenAI-compatible endpoint | optional |
| `OPENAI_MODEL` | model name (default `gpt-4o-mini`) | optional |
| `TAVILY_API_KEY` | web search via Tavily | optional |
| `SERPER_API_KEY` | web search via Serper (alternative) | optional |

## 3. Enable GitHub Pages

**Settings → Pages → Build and deployment → Source: GitHub Actions.**

The `Benchmark Research` workflow uploads the `reports/` folder as the Pages
artifact and deploys it. Your digest will be served at
`https://<you>.github.io/openbench-radar/` (landing page = `reports/index.html`,
latest digest = `reports/latest.html`).

## 4. Scheduling

The workflow runs **daily at 08:00 UTC** (`cron: "0 8 * * *"`). Edit
`.github/workflows/benchmark-research.yml` to change the cadence, e.g. weekly:

```yaml
on:
  schedule:
    - cron: "0 8 * * 1"   # Mondays 08:00 UTC
```

You can also trigger it any time from the **Actions** tab
(`Run workflow`), optionally overriding the topics.

## 5. What gets committed

Each run writes:

- `reports/<YYYY-MM-DD>.md` and `.html` — the dated digest
- `reports/latest.md` / `reports/latest.html` — always the newest
- `reports/index.html` — archive landing page

The workflow commits these back to the repo, so history is preserved in git.

## Troubleshooting

- **Empty report** → broaden `topics` or increase `recency_days` in `config/config.yaml`.
- **Pages 404** → confirm Pages source is set to *GitHub Actions* and the first run finished.
- **Push fails in Action** → the workflow needs `contents: write` permission (already set).
