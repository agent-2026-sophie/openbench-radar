# OpenBench Radar — AI/LLM Benchmark Digest

> Generated **2026-11-25 18:28 UTC** · 62 items · topics: LLM evaluation benchmark, large language model leaderboard, code generation benchmark, reasoning benchmark LLM, agent benchmark evaluation · analysis: extractive fallback

## Executive Summary

Retrieved **62** relevant items across topics (LLM evaluation benchmark, large language model leaderboard, code generation benchmark, reasoning benchmark LLM, agent benchmark evaluation): 60 from arxiv, 2 from huggingface. The most relevant findings, ranked by a keyword/recency/popularity heuristic, are listed below. (Set OPENAI_API_KEY to enable an LLM-written analytical summary.)

## Key Highlights

- [arxiv] SOTA or Luck? The Winner's Curse in LLM Leaderboards — Public LLM leaderboards guide model evaluation and adoption, yet the reported performance of top-ranked models can be systematically oversta
- [huggingface] goodgentleman918/ai-data-quality-llm-evaluation-benchmark — Hugging Face dataset — 117 downloads, 1 likes. Tags: task_categories:reinforcement-learning, language:en, license:mit, size_categories:n<1K,
- [arxiv] SAGE-QA: Semantic-Aware, Grounded Evaluation for Closed-Context Question Answering on SQuAD 2.0 — Closed-context question answering (QA) requires a system to generate an answer strictly supported by a supplied passage, or to abstain when
- [arxiv] ASCENT: A Benchmark for Evaluating and Advancing Stepwise Diagnostic Reasoning in Large Language Models on Common Clinical Scenarios — Large language models (LLMs) excel at medical question answering yet are rarely evaluated on the stepwise diagnostic reasoning that defines
- [arxiv] Schedule, Rank, Profile: Continuous Evaluation of LLM Agents in Games — Games are a robust test for large language model agents: they require sequential decisions, adversarial or cooperative interaction, state tr
- [arxiv] ICLWorld: Benchmarking In-Context Learning of Agents from Digital to Physical Worlds — In-context learning (ICL) lets agents acquire new rules from context and adapt to user-specific requirements at inference time. The same fro

## Findings by Source

### Arxiv (60)

- **[SOTA or Luck? The Winner's Curse in LLM Leaderboards](https://arxiv.org/abs/2611.22227v1)** _(score 15.467 · 2026-11-17 · Sikun Xu, Raphael Thomadsen, Dennis J. Zhang…)_
  Public LLM leaderboards guide model evaluation and adoption, yet the reported performance of top-ranked models can be systematically overstated. This leaderboard winner's curse arises because ranking noisy benchmark scores rewards sampling luck alongside genuine ability. The same
- **[SAGE-QA: Semantic-Aware, Grounded Evaluation for Closed-Context Question Answering on SQuAD 2.0](https://arxiv.org/abs/2611.16300v1)** _(score 13.133 · 2026-11-12 · Chandra N Sekharan, Vishakan Umapathy, Abhishek Phadke)_
  Closed-context question answering (QA) requires a system to generate an answer strictly supported by a supplied passage, or to abstain when the passage lacks adequate evidence. SQuAD 2.0 is a widely used benchmark for this setting, scored by Exact Match (EM) i.e., character-level
- **[ASCENT: A Benchmark for Evaluating and Advancing Stepwise Diagnostic Reasoning in Large Language Models on Common Clinical Scenarios](https://arxiv.org/abs/2611.32734v1)** _(score 11.933 · 2026-11-24 · Yera Choi, Yeong Hwa Kim, Jaedeok Lee…)_
  Large language models (LLMs) excel at medical question answering yet are rarely evaluated on the stepwise diagnostic reasoning that defines real clinical workflows, where impressions are revised as information accumulates. We build Annotated Stepwise Clinical rEasoning for Natura
- **[Schedule, Rank, Profile: Continuous Evaluation of LLM Agents in Games](https://arxiv.org/abs/2611.28368v1)** _(score 11.733 · 2026-11-20 · Martyna Plomecka, Yao Yan, DJ Sterling…)_
  Games are a robust test for large language model agents: they require sequential decisions, adversarial or cooperative interaction, state tracking, reasoning under uncertainty, and long-horizon planning. However, a one-time game benchmark can go stale as models, prompts, environm
- **[ICLWorld: Benchmarking In-Context Learning of Agents from Digital to Physical Worlds](https://arxiv.org/abs/2611.32649v1)** _(score 10.433 · 2026-11-24 · Qingle Liu, Jieming Li, Pei-lin Li…)_
  In-context learning (ICL) lets agents acquire new rules from context and adapt to user-specific requirements at inference time. The same frontier agents now operate both computers and robots, yet their ICL remains insufficiently assessed: existing benchmarks are largely offline,
- **[Benchmarking Protein Structure Tokenizers as Generation Targets for Language Models](https://arxiv.org/abs/2611.32168v1)** _(score 10.433 · 2026-11-24 · Yong Liu, Zhanpeng Shi, Peicong Lin…)_
  Discrete structure tokenizers are the standard way to give a language model access to protein three-dimensional structure, yet they are selected on how accurately they can be read, their reconstruction fidelity, while the property that governs generation is how well a model can w
- **[Towards Realistic Evaluation of Uncertainty Quantification for LLM-Based Recommender Systems](https://arxiv.org/abs/2611.33036v1)** _(score 9.933 · 2026-11-24 · Hao Wu, Sipeng Chen, Weikai Li…)_
  Large language models (LLMs) provide a flexible interface for recommendation systems. However, their issued rankings require reliable instance-level uncertainty monitoring. In this scenario, comparing uncertainty quantification (UQ) methods becomes challenging because LLM rankers
- **[LUCID: Statistically Grounded Self-Correction for LLM Reasoning Evaluation](https://arxiv.org/abs/2611.31595v1)** _(score 9.933 · 2026-11-23 · Satiyabooshan Murugaboopathy, Adel Daoud, Connor T. Jerzak)_
  Cheap language-model raters grade chain-of-thought reasoning at scale, yet systematic step-rating errors can skew reasoning audits and solution rankings. We introduce LUCID (Loop for Unbiased Calibration via Inference-time Diagnosis), which pairs prompt self-correction with Desig
- **[FigmaEval: A Benchmark for Evaluating AI Agents in Professional UI Design](https://arxiv.org/abs/2611.32321v1)** _(score 9.933 · 2026-11-24 · Xinyue Huang, Yongyong Gao, Zhengyuan Pan…)_
  Recent advances in AI agents have enabled autonomous UI design using professional tools such as Figma, yet evaluating their design capabilities remains challenging due to the open-ended nature of design tasks and the absence of unique ground truths. We introduce FigmaEval, a benc
- **[AI Isn't Getting Dumber, We're Getting Pickier: Rising Standards in Human Evaluation of Large Language Models](https://arxiv.org/abs/2611.14333v1)** _(score 9.0 · 2026-11-10 · Zihan Chen, Lei Nico Zheng, Di Zhu)_
  Users often complain that AI assistants such as ChatGPT are getting worse. Some versions do change, but human evaluation leaves a second possibility untested: the people judging may change. We separate the two on Chatbot Arena, a public platform where people compare answers from
- **[A Text-to-SQL Benchmark for Official Statistics](https://arxiv.org/abs/2611.32646v1)** _(score 8.433 · 2026-11-24 · Lucas Lageweg, Karen Goes, Tom van den Broek…)_
  Official statistics are critical datasets for a wide variety of actors, including policymakers and businesses. For providers of official statistics, improving accessibility, governance, and disclosure of their data is of key importance. This can be improved by providing question-
- **[RecurSciBench: Benchmarking Recursive Self-Improvement in Data-Driven Scientific Research](https://arxiv.org/abs/2611.32508v1)** _(score 8.433 · 2026-11-24 · Wenxi Xu, Chuan Qin, Zihan Wang…)_
  Large language model (LLM)-based agents are advancing the automation of data-driven scientific research. Recent advances in recursive self-improvement (RSI) offer the potential for these agents to continuously improve through experience, but evaluating transfer across scientific

### Huggingface (2)

- **[goodgentleman918/ai-data-quality-llm-evaluation-benchmark](https://huggingface.co/datasets/goodgentleman918/ai-data-quality-llm-evaluation-benchmark)** _(score 14.522 · 2026-11-10 · 117 downloads)_
  Hugging Face dataset — 117 downloads, 1 likes. Tags: task_categories:reinforcement-learning, language:en, license:mit, size_categories:n<1K, modality:text
- **[abdullahashraf122/algomyth-code-generation-benchmark](https://huggingface.co/datasets/abdullahashraf122/algomyth-code-generation-benchmark)** _(score 5.969 · 2026-10-18 · 25 downloads)_
  Hugging Face dataset — 25 downloads, 0 likes. Tags: task_categories:text-generation, annotations_creators:machine-generated, multilinguality:monolingual, source_datasets:original, language:en

---

_Produced by [OpenBench Radar](https://github.com/) — automated benchmark retrieval, research & reporting._