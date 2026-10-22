# OpenBench Radar — AI/LLM Benchmark Digest

> Generated **2026-10-22 13:32 UTC** · 54 items · topics: LLM evaluation benchmark, large language model leaderboard, code generation benchmark, reasoning benchmark LLM, agent benchmark evaluation · analysis: extractive fallback

## Executive Summary

Retrieved **54** relevant items across topics (LLM evaluation benchmark, large language model leaderboard, code generation benchmark, reasoning benchmark LLM, agent benchmark evaluation): 52 from arxiv, 2 from huggingface. The most relevant findings, ranked by a keyword/recency/popularity heuristic, are listed below. (Set OPENAI_API_KEY to enable an LLM-written analytical summary.)

## Key Highlights

- [arxiv] OpenTWBench (Open Taiwan Benchmark): Taiwan-Domain Knowledge Evaluation for Large Language Models, and How the Measurement Apparatus Shapes the Score — We present OpenTWBench, an open evaluation suite for Taiwan-domain knowledge in large language models, built around two benchmarks. tw-exam-
- [arxiv] TIDE: Tree-Induced Fine-Grained Diagnostic Evaluation from Model Behaviors — Benchmark performance is the dominant standard for comparing large language models (LLMs), typically summarized by a single aggregate score,
- [arxiv] SWE-DIVE: Multi-Turn Coding Agent Evaluation with Dynamic User Simulation — Coding agents are typically evaluated using one-shot, well-formulated prompts. Benchmarks such as SWE-bench use existing GitHub issues as in
- [arxiv] Re-executing Coding-Agent Evaluations: Unchanged Decisions and Unresolved Policy Risk — Executable tests grade large language model (LLM) coding-agent patches for leaderboards, rewards and self-improvement. Two preregistered re-
- [arxiv] UserSWE: Evaluating Coding Agents in Multi-Turn Conversations with Dynamic Users — As coding agents become more capable, developers increasingly use them to fix bugs through multi-turn interactions. Existing benchmarks do n
- [arxiv] Benchmarking and Error Analysis of Deep Search and Deep Research LLM Agents — As Large Language Models (LLMs) evolve into autonomous Deep Search and Deep Research Agents capable of executing long-horizon, multi-step ta

## Findings by Source

### Arxiv (52)

- **[OpenTWBench (Open Taiwan Benchmark): Taiwan-Domain Knowledge Evaluation for Large Language Models, and How the Measurement Apparatus Shapes the Score](https://arxiv.org/abs/2610.19848v1)** _(score 12.967 · 2026-10-14 · Liang-Hsun Huang, Min-Yi Chen, Chao-Chun Chuang…)_
  We present OpenTWBench, an open evaluation suite for Taiwan-domain knowledge in large language models, built around two benchmarks. tw-exam-bench contains 255,854 four-option questions across 148 academic subjects, from fifteen years of Taiwan's national examinations published as
- **[TIDE: Tree-Induced Fine-Grained Diagnostic Evaluation from Model Behaviors](https://arxiv.org/abs/2610.29985v1)** _(score 12.0 · 2026-10-21 · Jiayi Chen, Hui Li, Yujiong Shen…)_
  Benchmark performance is the dominant standard for comparing large language models (LLMs), typically summarized by a single aggregate score, such as accuracy, pass rate, or rubric score. This aggregate score provides limited information about a model's underlying capabilities, ye
- **[SWE-DIVE: Multi-Turn Coding Agent Evaluation with Dynamic User Simulation](https://arxiv.org/abs/2610.30047v1)** _(score 12.0 · 2026-10-21 · Lorenz Brehme, Benjamin Steenhoek, Ruth Breu)_
  Coding agents are typically evaluated using one-shot, well-formulated prompts. Benchmarks such as SWE-bench use existing GitHub issues as input for a coding agent and evaluate whether the agent successfully solves the task. However, in real-world use cases, prompts are often not
- **[Re-executing Coding-Agent Evaluations: Unchanged Decisions and Unresolved Policy Risk](https://arxiv.org/abs/2610.14460v1)** _(score 11.2 · 2026-10-10 · Tianyu Ding, Yaocheng Tong, Muzhi Yang…)_
  Executable tests grade large language model (LLM) coding-agent patches for leaderboards, rewards and self-improvement. Two preregistered re-execution studies returned negative results. SWE-bench Pro v1's offline option rejected none of 59 accepted Go patches whose grading configu
- **[UserSWE: Evaluating Coding Agents in Multi-Turn Conversations with Dynamic Users](https://arxiv.org/abs/2610.29822v1)** _(score 10.5 · 2026-10-21 · Zhan-Yu Wu, Ji Luo, Alyssa Wu…)_
  As coding agents become more capable, developers increasingly use them to fix bugs through multi-turn interactions. Existing benchmarks do not adequately cover this scenario. Most present a complete issue report in a single turn without interaction. Their evaluation can produce b
- **[Benchmarking and Error Analysis of Deep Search and Deep Research LLM Agents](https://arxiv.org/abs/2610.29346v1)** _(score 10.433 · 2026-10-21 · Zixuan Yu, Zhenheng Tang, Xiaowen Chu…)_
  As Large Language Models (LLMs) evolve into autonomous Deep Search and Deep Research Agents capable of executing long-horizon, multi-step tasks, evaluating their reliability becomes increasingly critical. However, existing evaluation paradigms predominantly focus on final task ou
- **[Beyond Scalar Leaderboards: Adaptive Sampling for Pareto Frontier Identification in Multi-Objective LLM Arenas](https://arxiv.org/abs/2610.27447v1)** _(score 10.367 · 2026-10-20 · Liang Twist Shan, Jiahao Ai, Zhimei Ren)_
  The evaluation of large language models (LLMs) is inherently multi-objective, as different models may offer different tradeoffs across performance dimensions such as math, code, and writing. Because such evaluations are often based on costly and time-consuming human feedback, it
- **[Beyond Leaderboards: A Method for Application-Specific Capability Profiling of Large Language Models](https://arxiv.org/abs/2610.25659v1)** _(score 10.3 · 2026-10-19 · Oleg Grynets, Vasyl Lyashkevych, Andrii Salyk…)_
  Public leaderboards rank large language models (LLMs) in general, but an engineer has to choose a model for a specific application, architecture and cost. This paper presents a method for application-specific capability profiling of LLMs and its realization as a containerized tes
- **[ACE-Compression: An Ability-Centric Evaluation of Compressed Large Language Models](https://arxiv.org/abs/2610.27913v1)** _(score 9.867 · 2026-10-20 · Jiahui Ning, Liang Chen, Yuchen Liang…)_
  Model compression makes large language models deployable, but today's evaluation tells an incomplete story. Standard practice measures retained task performance and stops there. This misses a critical fact: compression perturbs the distributed knowledge embedded across billions o
- **[ACED-Bench: Evaluating How LLM Agents Acquire and Act on Causal Evidence](https://arxiv.org/abs/2610.14381v1)** _(score 9.7 · 2026-10-09 · Yiwei Chen, Amila Weerasinghe, Siddharth Biswal…)_
  Large language models are increasingly used as scientific assistants, yet we still lack reliable ways to evaluate whether they can investigate a system rather than merely answer a prompt. A useful evaluation must let agents choose experiments, interpret finite evidence, and make
- **[Quant-Arena: Benchmarking LLM Agents for Quantitative Trading Research](https://arxiv.org/abs/2610.30113v1)** _(score 8.5 · 2026-10-21 · Houde Qian, Zheng Jiang, Wenyi Li…)_
  Quantitative research is an iterative loop: a researcher proposes a market hypothesis, implements it as an executable signal, tests it on historical data, and decides what to keep. Existing benchmarks score formulas, code, or individual trading decisions, leaving open whether lar
- **[From Reasoning to Action: Benchmarking Frontier AI Models on LIBERO-10 Robot Manipulation Tasks](https://arxiv.org/abs/2610.30051v1)** _(score 8.5 · 2026-10-21 · May Espinola, Qifan Zhang, Yu Xiang)_
  Recent advances in frontier AI models have demonstrated remarkable capabilities in visual understanding, reasoning, planning, and tool use, raising the possibility of using general-purpose AI models for robot manipulation without task-specific training. However, their manipulatio

### Huggingface (2)

- **[abdullahashraf122/algomyth-code-generation-benchmark](https://huggingface.co/datasets/abdullahashraf122/algomyth-code-generation-benchmark)** _(score 8.304 · 2026-10-18 · 43 downloads)_
  Hugging Face dataset — 43 downloads, 0 likes. Tags: task_categories:text-generation, annotations_creators:machine-generated, multilinguality:monolingual, source_datasets:original, language:en
- **[medreason/llm-medical-reasoning-steps-benchmark](https://huggingface.co/datasets/medreason/llm-medical-reasoning-steps-benchmark)** _(score 5.517 · 2026-05-04 · 67 downloads)_
  Hugging Face dataset — 67 downloads, 1 likes. Tags: task_categories:question-answering, task_categories:text-generation, language:en, license:cc-by-nc-4.0, size_categories:1K<n<10K

---

_Produced by [OpenBench Radar](https://github.com/) — automated benchmark retrieval, research & reporting._