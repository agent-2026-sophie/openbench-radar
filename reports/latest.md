# OpenBench Radar — AI/LLM Benchmark Digest

> Generated **2026-10-28 14:54 UTC** · 61 items · topics: LLM evaluation benchmark, large language model leaderboard, code generation benchmark, reasoning benchmark LLM, agent benchmark evaluation · analysis: extractive fallback

## Executive Summary

Retrieved **61** relevant items across topics (LLM evaluation benchmark, large language model leaderboard, code generation benchmark, reasoning benchmark LLM, agent benchmark evaluation): 59 from arxiv, 2 from huggingface. The most relevant findings, ranked by a keyword/recency/popularity heuristic, are listed below. (Set OPENAI_API_KEY to enable an LLM-written analytical summary.)

## Key Highlights

- [arxiv] Coverage Under Contradiction: A Benchmark for Negation-Aware Retrieval — Coverage-evaluation benchmarks quantify whether retrieved evidence covers the different pieces of information needed to satisfy an informati
- [arxiv] ETC-Bench: A Multilingual Benchmark for Evaluation-Side Transcript Canonicalization — Written transcripts of the same speech can differ in ways that are not uniquely determined by the speech signal. We formulate evaluation-sid
- [arxiv] OpenTWBench (Open Taiwan Benchmark): Taiwan-Domain Knowledge Evaluation for Large Language Models, and How the Measurement Apparatus Shapes the Score — We present OpenTWBench, an open evaluation suite for Taiwan-domain knowledge in large language models, built around two benchmarks. tw-exam-
- [arxiv] OpenGray: a benchmark for evaluating the decisions of radiotherapy planning agents — Background and purpose: Radiotherapy planning agents based on large language models (LLMs) decide when to submit a plan or request review bu
- [arxiv] NextEval: An Agent-Based Solver and Benchmark for Derivative-Free Optimization — Derivative-free optimization (DFO) addresses problems where derivatives are unavailable or costly to obtain. This setting often arises in si
- [arxiv] Patient-specific rubric-based evaluation of large language models across longitudinal cancer care — Large language models (LLMs) show promise in specialty medicine, yet existing evaluations largely focus on isolated clinical encounters rath

## Findings by Source

### Arxiv (59)

- **[Coverage Under Contradiction: A Benchmark for Negation-Aware Retrieval](https://arxiv.org/abs/2610.37162v1)** _(score 13.933 · 2026-10-27 · Pasha Abrishamchian, Eugene Yang, Andrew Yates…)_
  Coverage-evaluation benchmarks quantify whether retrieved evidence covers the different pieces of information needed to satisfy an information need. Existing benchmarks mostly consider factual claims that may already be known to pretrained retrieval components, leaving open wheth
- **[ETC-Bench: A Multilingual Benchmark for Evaluation-Side Transcript Canonicalization](https://arxiv.org/abs/2610.36527v1)** _(score 13.433 · 2026-10-27 · Zhiheng Qian, Junhao Du, Jing Peng…)_
  Written transcripts of the same speech can differ in ways that are not uniquely determined by the speech signal. We formulate evaluation-side transcript canonicalization (ETC), which maps multiple surface forms to a single canonical form when their differences are not determined
- **[OpenTWBench (Open Taiwan Benchmark): Taiwan-Domain Knowledge Evaluation for Large Language Models, and How the Measurement Apparatus Shapes the Score](https://arxiv.org/abs/2610.19848v1)** _(score 12.567 · 2026-10-14 · Liang-Hsun Huang, Min-Yi Chen, Chao-Chun Chuang…)_
  We present OpenTWBench, an open evaluation suite for Taiwan-domain knowledge in large language models, built around two benchmarks. tw-exam-bench contains 255,854 four-option questions across 148 academic subjects, from fifteen years of Taiwan's national examinations published as
- **[OpenGray: a benchmark for evaluating the decisions of radiotherapy planning agents](https://arxiv.org/abs/2610.37081v1)** _(score 11.933 · 2026-10-27 · Humza Nusrat, Kundan Thind)_
  Background and purpose: Radiotherapy planning agents based on large language models (LLMs) decide when to submit a plan or request review but are evaluated mainly by dose. This study developed OpenGray, a benchmark of planning tasks with known correct decisions. Materials and met
- **[NextEval: An Agent-Based Solver and Benchmark for Derivative-Free Optimization](https://arxiv.org/abs/2610.36553v1)** _(score 11.933 · 2026-10-27 · Shuo Chen, Li Cui, Cunxin Huang…)_
  Derivative-free optimization (DFO) addresses problems where derivatives are unavailable or costly to obtain. This setting often arises in simulation-based and experimental applications, where evaluating the black-box objective can itself be costly. Thus, it remains a central chal
- **[Patient-specific rubric-based evaluation of large language models across longitudinal cancer care](https://arxiv.org/abs/2610.35847v1)** _(score 11.933 · 2026-10-26 · Wei-Wei Zhang, Pengkai Wang, Yan Li…)_
  Large language models (LLMs) show promise in specialty medicine, yet existing evaluations largely focus on isolated clinical encounters rather than tracking how clinical responsibilities evolve across a longitudinal care pathway. Here we introduce NPC-RubricBench, a phase-aware b
- **[Re-executing Coding-Agent Evaluations: Unchanged Decisions and Unresolved Policy Risk](https://arxiv.org/abs/2610.14460v1)** _(score 10.8 · 2026-10-10 · Tianyu Ding, Yaocheng Tong, Muzhi Yang…)_
  Executable tests grade large language model (LLM) coding-agent patches for leaderboards, rewards and self-improvement. Two preregistered re-execution studies returned negative results. SWE-bench Pro v1's offline option rejected none of 59 accepted Go patches whose grading configu
- **[Benchmarking LLM Agents for Behaviorally Adequate Test Generation from Software Requirements](https://arxiv.org/abs/2610.36584v1)** _(score 10.433 · 2026-10-27 · Binhang Qi, Yiming Liu, Yun Lin…)_
  As large language model agents increasingly compile natural-language requirements into repository-level code, requirement-to-test generation grows in importance to provide validation constraints (or harness) to guide code generation. Yet it remains unclear whether current agents
- **[Beyond Scalar Leaderboards: Adaptive Sampling for Pareto Frontier Identification in Multi-Objective LLM Arenas](https://arxiv.org/abs/2610.27447v1)** _(score 9.967 · 2026-10-20 · Liang Twist Shan, Jiahao Ai, Zhimei Ren)_
  The evaluation of large language models (LLMs) is inherently multi-objective, as different models may offer different tradeoffs across performance dimensions such as math, code, and writing. Because such evaluations are often based on costly and time-consuming human feedback, it
- **[Where Should the Evaluation Budget Go in LLM-Driven Agent Scaffold Evolution?](https://arxiv.org/abs/2610.37276v1)** _(score 9.933 · 2026-10-27 · Sichun Luo, Yi Huang, Mukai Li…)_
  Large language model (LLM)-driven agent scaffold evolution improves agent workflows through iterative candidate generation and evaluation. Evaluation both guides subsequent search and determines the final scaffold, but evaluating every candidate on the full task set incurs substa
- **[Beyond Leaderboards: A Method for Application-Specific Capability Profiling of Large Language Models](https://arxiv.org/abs/2610.25659v1)** _(score 9.9 · 2026-10-19 · Oleg Grynets, Vasyl Lyashkevych, Andrii Salyk…)_
  Public leaderboards rank large language models (LLMs) in general, but an engineer has to choose a model for a specific application, architecture and cost. This paper presents a method for application-specific capability profiling of LLMs and its realization as a containerized tes
- **[ACE-Compression: An Ability-Centric Evaluation of Compressed Large Language Models](https://arxiv.org/abs/2610.27913v1)** _(score 9.467 · 2026-10-20 · Jiahui Ning, Liang Chen, Yuchen Liang…)_
  Model compression makes large language models deployable, but today's evaluation tells an incomplete story. Standard practice measures retained task performance and stops there. This misses a critical fact: compression perturbs the distributed knowledge embedded across billions o

### Huggingface (2)

- **[abdullahashraf122/algomyth-code-generation-benchmark](https://huggingface.co/datasets/abdullahashraf122/algomyth-code-generation-benchmark)** _(score 7.839 · 2026-10-18 · 52 downloads)_
  Hugging Face dataset — 52 downloads, 0 likes. Tags: task_categories:text-generation, annotations_creators:machine-generated, multilinguality:monolingual, source_datasets:original, language:en
- **[medreason/llm-medical-reasoning-steps-benchmark](https://huggingface.co/datasets/medreason/llm-medical-reasoning-steps-benchmark)** _(score 5.516 · 2026-05-04 · 65 downloads)_
  Hugging Face dataset — 65 downloads, 1 likes. Tags: task_categories:question-answering, task_categories:text-generation, language:en, license:cc-by-nc-4.0, size_categories:1K<n<10K

---

_Produced by [OpenBench Radar](https://github.com/) — automated benchmark retrieval, research & reporting._