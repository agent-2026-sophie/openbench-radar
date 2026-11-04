# OpenBench Radar — AI/LLM Benchmark Digest

> Generated **2026-11-04 15:59 UTC** · 60 items · topics: LLM evaluation benchmark, large language model leaderboard, code generation benchmark, reasoning benchmark LLM, agent benchmark evaluation · analysis: extractive fallback

## Executive Summary

Retrieved **60** relevant items across topics (LLM evaluation benchmark, large language model leaderboard, code generation benchmark, reasoning benchmark LLM, agent benchmark evaluation): 59 from arxiv, 1 from huggingface. The most relevant findings, ranked by a keyword/recency/popularity heuristic, are listed below. (Set OPENAI_API_KEY to enable an LLM-written analytical summary.)

## Key Highlights

- [arxiv] OpenTWBench (Open Taiwan Benchmark): Taiwan-Domain Knowledge Evaluation for Large Language Models, and How the Measurement Apparatus Shapes the Score — We present OpenTWBench, an open evaluation suite for Taiwan-domain knowledge in large language models, built around two benchmarks. tw-exam-
- [arxiv] Typological Feature Induction as a Benchmark for Inductive Metalinguistic Reasoning — Existing metalinguistic reasoning benchmarks require both inference of rules and their application, making failures hard to diagnose. We int
- [arxiv] One Assistant, Many Memories: Benchmarking Real-World Group Assistance When Recall Is Not Enough — The value of memory lies not only in recall but in using it to provide appropriate assistance. Recent benchmarks test memory use in personal
- [arxiv] AgenticFinBench: Benchmarking Financial Agents on Diverse Tasks from Real-World Requests — Financial agents are becoming an important class of real-world AI systems. Financial tasks vary widely in type and difficulty, and many are
- [arxiv] MedPhysBench: A Benchmark for Evaluating Language Models on Medical Physics Calculations and Error Detection — Medical physicists turn a prescription into a delivered dose and check one another's calculations, because one error in a beam calibration o
- [arxiv] Beyond Scalar Leaderboards: Adaptive Sampling for Pareto Frontier Identification in Multi-Objective LLM Arenas — The evaluation of large language models (LLMs) is inherently multi-objective, as different models may offer different tradeoffs across perfo

## Findings by Source

### Arxiv (59)

- **[OpenTWBench (Open Taiwan Benchmark): Taiwan-Domain Knowledge Evaluation for Large Language Models, and How the Measurement Apparatus Shapes the Score](https://arxiv.org/abs/2610.19848v1)** _(score 12.1 · 2026-10-14 · Liang-Hsun Huang, Min-Yi Chen, Chao-Chun Chuang…)_
  We present OpenTWBench, an open evaluation suite for Taiwan-domain knowledge in large language models, built around two benchmarks. tw-exam-bench contains 255,854 four-option questions across 148 academic subjects, from fifteen years of Taiwan's national examinations published as
- **[Typological Feature Induction as a Benchmark for Inductive Metalinguistic Reasoning](https://arxiv.org/abs/2611.04421v1)** _(score 10.433 · 2026-11-03 · Chen Zhang, Seth Aycock, Yusuke Miyao)_
  Existing metalinguistic reasoning benchmarks require both inference of rules and their application, making failures hard to diagnose. We introduce typological feature induction (TFI) which targets the former step. Given sentences in an unnamed language paired with translations in
- **[One Assistant, Many Memories: Benchmarking Real-World Group Assistance When Recall Is Not Enough](https://arxiv.org/abs/2611.04867v1)** _(score 10.433 · 2026-11-03 · Zhanghao Hu, Linhai Zhang, Qian Zhao…)_
  The value of memory lies not only in recall but in using it to provide appropriate assistance. Recent benchmarks test memory use in personalisation and agentic tasks, but seldom evaluate assistance without fixed answers or integration across multiple participants. Group chats mak
- **[AgenticFinBench: Benchmarking Financial Agents on Diverse Tasks from Real-World Requests](https://arxiv.org/abs/2611.04813v1)** _(score 10.433 · 2026-11-03 · Shu Zhou, Ziyang He, Yuxin Rao…)_
  Financial agents are becoming an important class of real-world AI systems. Financial tasks vary widely in type and difficulty, and many are open-ended with no ground-truth answers. However, existing benchmarks neither capture this breadth and open-endedness nor separate grounding
- **[MedPhysBench: A Benchmark for Evaluating Language Models on Medical Physics Calculations and Error Detection](https://arxiv.org/abs/2611.05340v1)** _(score 10.0 · 2026-11-03 · Omar Nusrat)_
  Medical physicists turn a prescription into a delivered dose and check one another's calculations, because one error in a beam calibration or a monitor-unit (MU) calculation can affect every patient treated with it. MedPhysBench has ten seeded generators of calculation items in r
- **[Beyond Scalar Leaderboards: Adaptive Sampling for Pareto Frontier Identification in Multi-Objective LLM Arenas](https://arxiv.org/abs/2610.27447v1)** _(score 9.5 · 2026-10-20 · Liang Twist Shan, Jiahao Ai, Zhimei Ren)_
  The evaluation of large language models (LLMs) is inherently multi-objective, as different models may offer different tradeoffs across performance dimensions such as math, code, and writing. Because such evaluations are often based on costly and time-consuming human feedback, it
- **[Beyond Leaderboards: A Method for Application-Specific Capability Profiling of Large Language Models](https://arxiv.org/abs/2610.25659v1)** _(score 9.433 · 2026-10-19 · Oleg Grynets, Vasyl Lyashkevych, Andrii Salyk…)_
  Public leaderboards rank large language models (LLMs) in general, but an engineer has to choose a model for a specific application, architecture and cost. This paper presents a method for application-specific capability profiling of LLMs and its realization as a containerized tes
- **[ACE-Compression: An Ability-Centric Evaluation of Compressed Large Language Models](https://arxiv.org/abs/2610.27913v1)** _(score 9.0 · 2026-10-20 · Jiahui Ning, Liang Chen, Yuchen Liang…)_
  Model compression makes large language models deployable, but today's evaluation tells an incomplete story. Standard practice measures retained task performance and stops there. This misses a critical fact: compression perturbs the distributed knowledge embedded across billions o
- **[Are LLM Assistants Regulatory Ready? Answers from regenold's 2026 EU AI Act Q&A Challenge](https://arxiv.org/abs/2611.04546v1)** _(score 8.933 · 2026-11-03 · Marco Virgolin, Thomas Haszprunar, Maximilian Regenold)_
  Large language model (LLM) assistants are increasingly proposed for regulatory affairs, yet their reliability in regulatory tasks remains unclear. We introduce the EU AI Act Q&A Benchmark, an expert-curated benchmark of 110 open-ended questions about the EU AI Act (Regulation (EU
- **[CardioVascBench:Prioritized Diagnosis Generation from Real-World Chinese Cardiovascular Records](https://arxiv.org/abs/2611.04687v1)** _(score 8.933 · 2026-11-03 · Minghao Kong, Muyao Chen, Jianhao Wu…)_
  Identifying the primary diagnosis alone does not fully characterize a model's diagnosis-generation performance. We introduce CardioVascBench, a retrospective benchmark for prioritized diagnosis generation from real-world Chinese cardiovascular inpatient records. It contains 3,262
- **[DualWorldBench: Can Agents Plan Deliveries across Symbolic and Grounded Worlds?](https://arxiv.org/abs/2611.04228v1)** _(score 8.933 · 2026-11-03 · Yang Chen, Bin Wen, Danyang Peng…)_
  Recent multimodal agents have shown promising progress in embodied planning and web interaction. However, existing evaluations often rely on simplified tasks with limited combinatorial structure, leaving it unclear whether current agents can robustly integrate perception and reas
- **[ScienceVision: Can AI Observe and Reason Like a Scientist?](https://arxiv.org/abs/2611.04087v1)** _(score 8.933 · 2026-11-02 · Tianyi Ma, Jing Gu, Haozhe Zhao…)_
  Scientific discovery builds on accurate observations interpreted through domain knowledge and reasoning. For scientific 3D data, this requires understanding structures and spatial relationships, from protein contacts to anatomical organization. Existing multimodal benchmarks larg

### Huggingface (1)

- **[abdullahashraf122/algomyth-code-generation-benchmark](https://huggingface.co/datasets/abdullahashraf122/algomyth-code-generation-benchmark)** _(score 7.372 · 2026-10-18 · 55 downloads)_
  Hugging Face dataset — 55 downloads, 0 likes. Tags: task_categories:text-generation, annotations_creators:machine-generated, multilinguality:monolingual, source_datasets:original, language:en

---

_Produced by [OpenBench Radar](https://github.com/) — automated benchmark retrieval, research & reporting._