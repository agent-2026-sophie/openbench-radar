# OpenBench Radar — AI/LLM Benchmark Digest

> Generated **2026-11-03 15:54 UTC** · 65 items · topics: LLM evaluation benchmark, large language model leaderboard, code generation benchmark, reasoning benchmark LLM, agent benchmark evaluation · analysis: extractive fallback

## Executive Summary

Retrieved **65** relevant items across topics (LLM evaluation benchmark, large language model leaderboard, code generation benchmark, reasoning benchmark LLM, agent benchmark evaluation): 64 from arxiv, 1 from huggingface. The most relevant findings, ranked by a keyword/recency/popularity heuristic, are listed below. (Set OPENAI_API_KEY to enable an LLM-written analytical summary.)

## Key Highlights

- [arxiv] Benchmark of THReD: Evaluating an LLM Agent and Its Preprocessing Tools for Turning Electronic Health Records into AI-Ready Datasets — LLM agents are increasingly built into data-analysis software, yet little evidence shows how reliably they preprocess clinical data or wheth
- [arxiv] Accounting for Irregular State Transitions through Belief Estimation in Online Medical Consultation — While online medical consultation broadens access, unprompted patient disclosures and topic shifts frequently disrupt clinician inquiry, lea
- [arxiv] CR-Bench-v2: Evaluating the Real-World Utility of AI Code Review Agents — The rapid growth of automated code generation has created a pressing need for automated code review. Yet code review resists full automation
- [arxiv] OpenTWBench (Open Taiwan Benchmark): Taiwan-Domain Knowledge Evaluation for Large Language Models, and How the Measurement Apparatus Shapes the Score — We present OpenTWBench, an open evaluation suite for Taiwan-domain knowledge in large language models, built around two benchmarks. tw-exam-
- [arxiv] CAREFUL-Bench: Effect-Aware, Judge-Free Evaluation of Multi-Turn LLM Function Calling — The multi-turn checker of the Berkeley Function Calling Leaderboard (BFCL) evaluates final state correctness but ignores the effects of inte
- [arxiv] VisCodeBench: a new benchmark dataset for Text-to-Vis reflecting real-world practice — Generating visualisations from natural language requests (text-to-vis) enables users to explore data more efficiently. While LLMs can comple

## Findings by Source

### Arxiv (64)

- **[Benchmark of THReD: Evaluating an LLM Agent and Its Preprocessing Tools for Turning Electronic Health Records into AI-Ready Datasets](https://arxiv.org/abs/2611.02484v1)** _(score 13.433 · 2026-11-02 · Javad Mohammad Alizadeh, Huanmei Wu)_
  LLM agents are increasingly built into data-analysis software, yet little evidence shows how reliably they preprocess clinical data or whether the tools they invoke give correct, reproducible output. We report a benchmark of THReD, a web-based system that turns electronic health
- **[Accounting for Irregular State Transitions through Belief Estimation in Online Medical Consultation](https://arxiv.org/abs/2611.01474v1)** _(score 12.867 · 2026-11-01 · Mingzhe Lu, Xiangru Chen, Jian Qin…)_
  While online medical consultation broadens access, unprompted patient disclosures and topic shifts frequently disrupt clinician inquiry, leaving clinical states progressively revealed. We characterize these dynamics using both existing evaluation metrics and task-specific interac
- **[CR-Bench-v2: Evaluating the Real-World Utility of AI Code Review Agents](https://arxiv.org/abs/2611.02566v1)** _(score 12.433 · 2026-11-02 · Kristen Pereira, Neelabh Sinha, Rajat Ghosh…)_
  The rapid growth of automated code generation has created a pressing need for automated code review. Yet code review resists full automation: it depends on context beyond the \textit{diff}, on the author's intent, and on judgments about design and maintainability on which even ex
- **[OpenTWBench (Open Taiwan Benchmark): Taiwan-Domain Knowledge Evaluation for Large Language Models, and How the Measurement Apparatus Shapes the Score](https://arxiv.org/abs/2610.19848v1)** _(score 12.167 · 2026-10-14 · Liang-Hsun Huang, Min-Yi Chen, Chao-Chun Chuang…)_
  We present OpenTWBench, an open evaluation suite for Taiwan-domain knowledge in large language models, built around two benchmarks. tw-exam-bench contains 255,854 four-option questions across 148 academic subjects, from fifteen years of Taiwan's national examinations published as
- **[CAREFUL-Bench: Effect-Aware, Judge-Free Evaluation of Multi-Turn LLM Function Calling](https://arxiv.org/abs/2611.02978v1)** _(score 11.933 · 2026-11-02 · Alexander Kovalenko, Artem Redchych)_
  The multi-turn checker of the Berkeley Function Calling Leaderboard (BFCL) evaluates final state correctness but ignores the effects of intermediate calls: extra calls are free, function documentation does not describe side effects, and the scripted user never responds to proposa
- **[VisCodeBench: a new benchmark dataset for Text-to-Vis reflecting real-world practice](https://arxiv.org/abs/2611.02353v1)** _(score 11.933 · 2026-11-02 · Hy Nguyen, Thomas James Elton, Ella Wilson…)_
  Generating visualisations from natural language requests (text-to-vis) enables users to explore data more efficiently. While LLMs can complete simple visualisation requests, their performance on challenging ones is not well covered by existing benchmarks. We introduce VisCodeBenc
- **[Do Agents Still Follow the Rules? Benchmarking Rule Compliance under Agent Context Compaction](https://arxiv.org/abs/2611.03223v1)** _(score 10.433 · 2026-11-02 · Yiwei Zha, Qingyu Meng, Herbert Bos…)_
  LLM agents compact long histories to fit their context windows, but the compacted context must still carry the operating rules that govern later actions. Prior work shows that violations rise after compaction, but measures compliance outside a complete agent harness and does not
- **[A Fine-Grained Hierarchy and Benchmark for State Tracking in Language Models](https://arxiv.org/abs/2611.03094v1)** _(score 10.433 · 2026-11-02 · Jackson Petty, William Merrill, Ashish Sabharwal)_
  Theoretical limitations of transformers on state tracking---the ability to track information about entities or variables over long contexts---have motivated new recurrent language modeling (LM) architectures such as Gated DeltaNet (GDN). These architectures have, in particular, b
- **[Re-executing Coding-Agent Evaluations: Unchanged Decisions and Unresolved Policy Risk](https://arxiv.org/abs/2610.14460v1)** _(score 10.4 · 2026-10-10 · Tianyu Ding, Yaocheng Tong, Muzhi Yang…)_
  Executable tests grade large language model (LLM) coding-agent patches for leaderboards, rewards and self-improvement. Two preregistered re-execution studies returned negative results. SWE-bench Pro v1's offline option rejected none of 59 accepted Go patches whose grading configu
- **[Beyond Scalar Leaderboards: Adaptive Sampling for Pareto Frontier Identification in Multi-Objective LLM Arenas](https://arxiv.org/abs/2610.27447v1)** _(score 9.567 · 2026-10-20 · Liang Twist Shan, Jiahao Ai, Zhimei Ren)_
  The evaluation of large language models (LLMs) is inherently multi-objective, as different models may offer different tradeoffs across performance dimensions such as math, code, and writing. Because such evaluations are often based on costly and time-consuming human feedback, it
- **[Beyond Leaderboards: A Method for Application-Specific Capability Profiling of Large Language Models](https://arxiv.org/abs/2610.25659v1)** _(score 9.5 · 2026-10-19 · Oleg Grynets, Vasyl Lyashkevych, Andrii Salyk…)_
  Public leaderboards rank large language models (LLMs) in general, but an engineer has to choose a model for a specific application, architecture and cost. This paper presents a method for application-specific capability profiling of LLMs and its realization as a containerized tes
- **[ACE-Compression: An Ability-Centric Evaluation of Compressed Large Language Models](https://arxiv.org/abs/2610.27913v1)** _(score 9.067 · 2026-10-20 · Jiahui Ning, Liang Chen, Yuchen Liang…)_
  Model compression makes large language models deployable, but today's evaluation tells an incomplete story. Standard practice measures retained task performance and stops there. This misses a critical fact: compression perturbs the distributed knowledge embedded across billions o

### Huggingface (1)

- **[abdullahashraf122/algomyth-code-generation-benchmark](https://huggingface.co/datasets/abdullahashraf122/algomyth-code-generation-benchmark)** _(score 7.439 · 2026-10-18 · 55 downloads)_
  Hugging Face dataset — 55 downloads, 0 likes. Tags: task_categories:text-generation, annotations_creators:machine-generated, multilinguality:monolingual, source_datasets:original, language:en

---

_Produced by [OpenBench Radar](https://github.com/) — automated benchmark retrieval, research & reporting._