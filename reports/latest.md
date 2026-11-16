# OpenBench Radar — AI/LLM Benchmark Digest

> Generated **2026-11-16 18:00 UTC** · 60 items · topics: LLM evaluation benchmark, large language model leaderboard, code generation benchmark, reasoning benchmark LLM, agent benchmark evaluation · analysis: extractive fallback

## Executive Summary

Retrieved **60** relevant items across topics (LLM evaluation benchmark, large language model leaderboard, code generation benchmark, reasoning benchmark LLM, agent benchmark evaluation): 58 from arxiv, 2 from huggingface. The most relevant findings, ranked by a keyword/recency/popularity heuristic, are listed below. (Set OPENAI_API_KEY to enable an LLM-written analytical summary.)

## Key Highlights

- [huggingface] goodgentleman918/ai-data-quality-llm-evaluation-benchmark — Hugging Face dataset — 103 downloads, 1 likes. Tags: task_categories:reinforcement-learning, language:en, license:mit, size_categories:n<1K,
- [arxiv] SAGE-QA: Semantic-Aware, Grounded Evaluation for Closed-Context Question Answering on SQuAD 2.0 — Closed-context question answering (QA) requires a system to generate an answer strictly supported by a supplied passage, or to abstain when
- [arxiv] ChJGBench: A Comprehensive Benchmark for Chinese Legal Judgment Generation with Diagnostic Evaluation — With the rapid development of LLMs, increasing attention has been paid to whether they can reliably generate complete and legally valid judi
- [arxiv] DECODE: Decomposable Environments for COntrolled Sequential-Decision Evaluation — When a sequential decision system falls short of an optimum, its score does not reveal which modifications would improve its decisions. DECO
- [arxiv] MuSeToM: Multi-Sensory Evaluation of Belief Revision with Textual Cues Across Six Senses — Theory of Mind (ToM), the ability to infer mental states in others, is pivotal for human social cognition. Existing evaluations of ToM in la
- [arxiv] Tracing Knowledge and Reasoning in LLM — Current evaluations of Large Language Models (LLMs) report performance at the dataset or task level, revealing what a model achieves but off

## Findings by Source

### Arxiv (58)

- **[SAGE-QA: Semantic-Aware, Grounded Evaluation for Closed-Context Question Answering on SQuAD 2.0](https://arxiv.org/abs/2611.16300v1)** _(score 13.733 · 2026-11-12 · Chandra N Sekharan, Vishakan Umapathy, Abhishek Phadke)_
  Closed-context question answering (QA) requires a system to generate an answer strictly supported by a supplied passage, or to abstain when the passage lacks adequate evidence. SQuAD 2.0 is a widely used benchmark for this setting, scored by Exact Match (EM) i.e., character-level
- **[ChJGBench: A Comprehensive Benchmark for Chinese Legal Judgment Generation with Diagnostic Evaluation](https://arxiv.org/abs/2611.15639v1)** _(score 13.167 · 2026-11-11 · Yinghao Hu, Linggang Kong, Qian Xiao…)_
  With the rapid development of LLMs, increasing attention has been paid to whether they can reliably generate complete and legally valid judicial documents. This calls for a benchmark capable of evaluating whether models can accurately apply statutes and resolve outcome-critical i
- **[DECODE: Decomposable Environments for COntrolled Sequential-Decision Evaluation](https://arxiv.org/abs/2611.18367v1)** _(score 11.8 · 2026-11-13 · Diego Silva Prado, Bruno Caldas de Souza, Tiago Amaral Penteado de Jesus…)_
  When a sequential decision system falls short of an optimum, its score does not reveal which modifications would improve its decisions. DECODE is a benchmark for testing such modifications through controlled experiments on planning and available information. Its consumer-credit c
- **[MuSeToM: Multi-Sensory Evaluation of Belief Revision with Textual Cues Across Six Senses](https://arxiv.org/abs/2611.16662v1)** _(score 11.733 · 2026-11-12 · Chunkit Chan, Kawai Chung, Sze Heng Douglas Kwok…)_
  Theory of Mind (ToM), the ability to infer mental states in others, is pivotal for human social cognition. Existing evaluations of ToM in large language models (LLMs) mainly focus on static belief attribution and false-belief reasoning, leaving a critical aspect of social reasoni
- **[Tracing Knowledge and Reasoning in LLM](https://arxiv.org/abs/2611.17461v1)** _(score 10.8 · 2026-11-12 · Yang Wang, Xiao Wang, Yiqi Liu…)_
  Current evaluations of Large Language Models (LLMs) report performance at the dataset or task level, revealing what a model achieves but offering little insight into the internal processing associated with its performance. We propose a task-centric framework for characterising th
- **[NER-D: A cross-domain benchmark for German NER](https://arxiv.org/abs/2611.18257v1)** _(score 10.3 · 2026-11-13 · Marc Brinner, Philipp Cimiano, Karolina Hanna Czok…)_
  We present NER-D, a cross-domain benchmark for German NER comprising 13 datasets spanning 9 domains, including General/Politics, Wikipedia, Legal, Medical, Historical, Financial, Agriculture and Archaeology. We examine the performance of both proprietary LLMs and state-of-the-art
- **[MarathonTS: a benchmark of long synthetic time series from window assembly and long-series generators](https://arxiv.org/abs/2611.18190v1)** _(score 10.3 · 2026-11-13 · Ilyas Varshavskiy, Sergey Shulgin, Shuhrat Khalilbekov…)_
  Many applications of synthetic time series require a series that is much longer than the windows on which a generative model is trained. Such a series can be assembled from a pool of short generated windows, which requires deciding which windows are taken, in what order, and how
- **[OCTAVE: A Capability-Resolved Benchmark for End-to-End HTML5 Game Generation](https://arxiv.org/abs/2611.17681v1)** _(score 10.3 · 2026-11-13 · Kehang Li, Xinlan Xu, Yulin Jin…)_
  Complete game generation requires agents to coordinate rules, interactions, states, and presentation over a long development process. A single aggregate score obscures which capabilities are implemented and which requirements remain unmet. We present OCTAVE, a benchmark for compl
- **[LiveGeo: Benchmarking Geographic Agents in Continuously Evolving Worlds](https://arxiv.org/abs/2611.17267v1)** _(score 10.3 · 2026-11-12 · Pengcheng Zhou, Xuanyu Liu, Yanchen Yin…)_
  We introduce GeoWorld, a controllable and continuously evolving geographic environment platform for LLM agents, and LiveGeo, a benchmark for evaluating reliable decision-making in real-world geographic environments using GeoWorld. Unlike existing evaluations that largely reason a
- **[Do Verifier Judgments Survive Abstraction? Measuring Verification Transport for LLM Agent Evaluation](https://arxiv.org/abs/2611.18471v1)** _(score 9.8 · 2026-11-13 · Disha Sheshanarayana, Sai Linisha Reddy Goli)_
  LLM-based verifiers are increasingly used to evaluate agent executions, but their reliability is typically measured under a single representation of the trajectory. In deployed agent systems, the same execution may be exposed through composed tools, delegation boundaries, or comp
- **[PrivacyPR: A Dataset of Real-World Privacy Fixes for Benchmarking Privacy-Aware Code Review](https://arxiv.org/abs/2611.18293v1)** _(score 9.8 · 2026-11-13 · Hua Yang, Aditya Bhardwaj, Shidong Pan…)_
  Coding agents increasingly review code, yet whether they catch the privacy defects that laws such as the GDPR require software to avoid remains largely untested, partly because few datasets connect real privacy defects to their accepted fixes and review context. We present Privac
- **[GT-FENG: General Theory of Factual Evaluation and Normative Grounding in Language Models *Author(s)](https://arxiv.org/abs/2611.18279v1)** _(score 9.8 · 2026-11-13 · Jiayu Feng)_
  Whether a language model's answer is correct often depends on context: the same value can be right under one jurisdiction, date, or legal definition and wrong under another. We introduce GT-FENG (General Theory of Factual Evaluation and Normative Grounding), the first general fra

### Huggingface (2)

- **[goodgentleman918/ai-data-quality-llm-evaluation-benchmark](https://huggingface.co/datasets/goodgentleman918/ai-data-quality-llm-evaluation-benchmark)** _(score 15.12 · 2026-11-10 · 103 downloads)_
  Hugging Face dataset — 103 downloads, 1 likes. Tags: task_categories:reinforcement-learning, language:en, license:mit, size_categories:n<1K, modality:text
- **[abdullahashraf122/algomyth-code-generation-benchmark](https://huggingface.co/datasets/abdullahashraf122/algomyth-code-generation-benchmark)** _(score 6.573 · 2026-10-18 · 61 downloads)_
  Hugging Face dataset — 61 downloads, 0 likes. Tags: task_categories:text-generation, annotations_creators:machine-generated, multilinguality:monolingual, source_datasets:original, language:en

---

_Produced by [OpenBench Radar](https://github.com/) — automated benchmark retrieval, research & reporting._