# Example output

These files are **real sample output** produced by running:

```bash
openbench-agent run --no-llm --output examples
```

- [`latest.md`](latest.md) / [`latest.html`](latest.html) — the digest (Markdown + standalone HTML page)
- [`index.html`](index.html) — the GitHub Pages archive landing page
- `<date>.md` / `<date>.html` — the dated snapshot

This run used only the **free** sources (arXiv + Hugging Face) and the
**extractive fallback** (no LLM key). With `OPENAI_API_KEY` set, the
*Executive Summary* section is instead written by the LLM.
