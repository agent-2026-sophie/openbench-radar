# OpenBench Radar — AI/LLM Benchmark Digest

> Generated **2026-11-17 17:26 UTC** · 64 items · topics: LLM evaluation benchmark, large language model leaderboard, code generation benchmark, reasoning benchmark LLM, agent benchmark evaluation · analysis: extractive fallback

## Executive Summary

Retrieved **64** relevant items across topics (LLM evaluation benchmark, large language model leaderboard, code generation benchmark, reasoning benchmark LLM, agent benchmark evaluation): 62 from arxiv, 2 from huggingface. The most relevant findings, ranked by a keyword/recency/popularity heuristic, are listed below. (Set OPENAI_API_KEY to enable an LLM-written analytical summary.)

## Key Highlights

- [huggingface] goodgentleman918/ai-data-quality-llm-evaluation-benchmark — Hugging Face dataset — 106 downloads, 1 likes. Tags: task_categories:reinforcement-learning, language:en, license:mit, size_categories:n<1K,
- [arxiv] SAGE-QA: Semantic-Aware, Grounded Evaluation for Closed-Context Question Answering on SQuAD 2.0 — Closed-context question answering (QA) requires a system to generate an answer strictly supported by a supplied passage, or to abstain when
- [arxiv] CuRSE-Bench: A Benchmark for Probing Cultural Blind Spots in Text-to-Image Safety Evaluation — Text-to-image (T2I) safety evaluation typically assigns each prompt or image a single culture-blind harm label, so content that is harmful o
- [arxiv] Evaluation-Free Recursive Self-Improvement for Coding Agents — Recent self-improving coding agents have achieved strong benchmark performance by iteratively modifying their own executable implementations
- [arxiv] DetourBench: Trajectory-Level Evaluation of Interactive Agents with Exact Minimum-Action Bounds — Benchmarks judge language-model agents mainly by whether they reach the correct final state, not by how they got there. Endpoint scoring can
- [arxiv] Tracing Knowledge and Reasoning in LLM — Current evaluations of Large Language Models (LLMs) report performance at the dataset or task level, revealing what a model achieves but off

## Findings by Source

### Arxiv (62)

- **[SAGE-QA: Semantic-Aware, Grounded Evaluation for Closed-Context Question Answering on SQuAD 2.0](https://arxiv.org/abs/2611.16300v1)** _(score 13.667 · 2026-11-12 · Chandra N Sekharan, Vishakan Umapathy, Abhishek Phadke)_
  Closed-context question answering (QA) requires a system to generate an answer strictly supported by a supplied passage, or to abstain when the passage lacks adequate evidence. SQuAD 2.0 is a widely used benchmark for this setting, scored by Exact Match (EM) i.e., character-level
- **[CuRSE-Bench: A Benchmark for Probing Cultural Blind Spots in Text-to-Image Safety Evaluation](https://arxiv.org/abs/2611.20821v1)** _(score 13.433 · 2026-11-16 · Minsuk Jang, Minseok Son, KiHyun Seol…)_
  Text-to-image (T2I) safety evaluation typically assigns each prompt or image a single culture-blind harm label, so content that is harmful only within a particular culture can pass as benign. We introduce CultureCraft, an agentic framework that constructs T2I prompts that appear
- **[Evaluation-Free Recursive Self-Improvement for Coding Agents](https://arxiv.org/abs/2611.21056v1)** _(score 11.933 · 2026-11-16 · Zhe Ren, Guowei Rong, Yimeng Chen…)_
  Recent self-improving coding agents have achieved strong benchmark performance by iteratively modifying their own executable implementations. A common pattern uses downstream task-derived evidence to decide which candidates or lineages continue evolving, which we term evaluate-an
- **[DetourBench: Trajectory-Level Evaluation of Interactive Agents with Exact Minimum-Action Bounds](https://arxiv.org/abs/2611.20844v1)** _(score 11.933 · 2026-11-16 · Hanlin Tian, Sihan Zhu, Zhao Yang…)_
  Benchmarks judge language-model agents mainly by whether they reach the correct final state, not by how they got there. Endpoint scoring cannot separate an agent that retrieved exactly the evidence a decision required from one that read most of the environment, nor an agent that
- **[Tracing Knowledge and Reasoning in LLM](https://arxiv.org/abs/2611.17461v1)** _(score 10.733 · 2026-11-12 · Yang Wang, Xiao Wang, Yiqi Liu…)_
  Current evaluations of Large Language Models (LLMs) report performance at the dataset or task level, revealing what a model achieves but offering little insight into the internal processing associated with its performance. We propose a task-centric framework for characterising th
- **[When Do Histology Foundation Models Need Geometric Test-Time Augmentation?](https://arxiv.org/abs/2611.21565v1)** _(score 10.5 · 2026-11-16 · Lars Chen, Valentino F. Foit, Dorry Segev…)_
  Test-time augmentation (TTA) aggregates model predictions across multiple transformed views of an input during inference. Because histology images lack a canonical orientation, $D_4$ TTA---pooling across the 8 rotations and reflections of a square---is a standard default in compu
- **[ReconPotBench: Evaluating LLM Honeypots in Multi-Round Linux Reconnaissance](https://arxiv.org/abs/2611.20528v1)** _(score 10.433 · 2026-11-16 · Qianli Wang, Junchao Wu, Binkai Ou…)_
  Large language models (LLMs) are increasingly used to build interactive honeypots, yet existing evaluations mainly assess isolated command outputs and cannot determine whether a system remains believable when later commands depend on earlier results. We present ReconPotBench, a m
- **[VAHBench: A Harness Benchmark for Agentic Long-Video Generation](https://arxiv.org/abs/2611.20535v1)** _(score 10.433 · 2026-11-16 · Hongbo Zhang, Liuyang Song, Hang Zhou…)_
  AI agents are commonly used for everyday information retrieval and coding. We ask whether they can also interpret human requests and turn them into complete videos. We introduce VAHBench, a benchmark that tests this ability through five short-drama briefs specifying story, charac
- **[VisualArtifactSpec 1.0: Evaluating Visual Artifacts under Task Specifications](https://arxiv.org/abs/2611.21382v1)** _(score 10.433 · 2026-11-16 · Shuyi Ouyang, Xiaojun Tang, Zijian Zou…)_
  Visual artifact tasks test agents' ability to translate task specifications and source materials into outputs that meet practical needs. Evaluation across artifact families helps distinguish broadly applicable authoring capabilities from strengths confined to a particular medium.
- **[A Dataset for Misogyny Detection in Polish Social Media: Transferability of Hateful Speech Detection from General to Specific Types of Hate](https://arxiv.org/abs/2611.20044v1)** _(score 10.367 · 2026-11-15 · Ewelina Gajewska)_
  Harmful language detection is commonly evaluated on broadly defined hate speech and toxicity benchmarks, yet it remains unclear whether models that successfully detect harmful language in general can transfer this capability to more specific forms of hate. We investigate this pro
- **[IndustrialKnowEval: A Benchmark for Evaluating Multi-Level Industrial Knowledge in LLMs](https://arxiv.org/abs/2611.20695v1)** _(score 9.933 · 2026-11-16 · Haiteng Wang, Haoze Li, Jingwei Guo…)_
  Large language models (LLMs) are increasingly explored for industrial tasks, yet few benchmarks evaluate their mastery of industrial knowledge across different types of cognitive demand. We introduce IndustrialKnowEval (IndKnow), a benchmark for industrial knowledge and engineeri
- **[Benchmark Factory: Agentic Benchmark Creation via Dataset Curation and Label-Free Quality Anchors](https://arxiv.org/abs/2611.18890v1)** _(score 9.8 · 2026-11-13 · Shervin Shahidi, James Poon, Hang Xie…)_
  Teams deploying coding agents need benchmarks built from their own code, but curating and validating them by hand is resource intensive, and an unvalidated benchmark can mislead silently. We present Benchmark Factory, an autonomous meta-agent loop with human checkpoints: an LLM a

### Huggingface (2)

- **[goodgentleman918/ai-data-quality-llm-evaluation-benchmark](https://huggingface.co/datasets/goodgentleman918/ai-data-quality-llm-evaluation-benchmark)** _(score 15.054 · 2026-11-10 · 106 downloads)_
  Hugging Face dataset — 106 downloads, 1 likes. Tags: task_categories:reinforcement-learning, language:en, license:mit, size_categories:n<1K, modality:text
- **[abdullahashraf122/algomyth-code-generation-benchmark](https://huggingface.co/datasets/abdullahashraf122/algomyth-code-generation-benchmark)** _(score 6.504 · 2026-10-18 · 37 downloads)_
  Hugging Face dataset — 37 downloads, 0 likes. Tags: task_categories:text-generation, annotations_creators:machine-generated, multilinguality:monolingual, source_datasets:original, language:en

---

_Produced by [OpenBench Radar](https://github.com/) — automated benchmark retrieval, research & reporting._