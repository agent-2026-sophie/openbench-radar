# OpenBench Radar — AI/LLM Benchmark Digest

> Generated **2026-11-02 17:54 UTC** · 64 items · topics: LLM evaluation benchmark, large language model leaderboard, code generation benchmark, reasoning benchmark LLM, agent benchmark evaluation · analysis: extractive fallback

## Executive Summary

Retrieved **64** relevant items across topics (LLM evaluation benchmark, large language model leaderboard, code generation benchmark, reasoning benchmark LLM, agent benchmark evaluation): 63 from arxiv, 1 from huggingface. The most relevant findings, ranked by a keyword/recency/popularity heuristic, are listed below. (Set OPENAI_API_KEY to enable an LLM-written analytical summary.)

## Key Highlights

- [arxiv] What Standard Evaluations Hide About Detectors of Hijacked LLM Agents: Rare Attacks, Unseen Tools and Benchmark Transfer — Detectors can flag hijacked large language model (LLM) agents from the traces of the tools they call. In the eleven evaluations we audited,
- [arxiv] From Evaluation to Evolution: Benchmarking Image Editing and Evolving Image Models — Real-world image editing requires coordinating multiple visual transformations with content preservation and reference constraints, yet aggr
- [arxiv] GraphNIAH: A Benchmark for Long-Context Reasoning over Real-World Graphs — The needle-in-a-haystack (NIAH) benchmark was introduced as a test for measuring a model's ability to find small relevant facts within a ver
- [arxiv] OpenTWBench (Open Taiwan Benchmark): Taiwan-Domain Knowledge Evaluation for Large Language Models, and How the Measurement Apparatus Shapes the Score — We present OpenTWBench, an open evaluation suite for Taiwan-domain knowledge in large language models, built around two benchmarks. tw-exam-
- [arxiv] ProSearch: Benchmarking Multi-Constraint Protocol Retrieval in Experimental Science — In AI for Science scenarios, experimental design and method reproduction require retrieving protocols that satisfy multiple interdependent c
- [arxiv] Better Retrievers, Worse Labels: How Incomplete Relevance Judgments Distort Abstention Evaluation in Conversational RAG — Conversational RAG benchmarks such as MTRAG and RETECO evaluate retrieval and generation end to end: each system answers from its own retrie

## Findings by Source

### Arxiv (63)

- **[What Standard Evaluations Hide About Detectors of Hijacked LLM Agents: Rare Attacks, Unseen Tools and Benchmark Transfer](https://arxiv.org/abs/2610.41803v1)** _(score 13.3 · 2026-10-30 · Mahmoud Abbasi, Juan M. Núñez V., Amin Shahraki)_
  Detectors can flag hijacked large language model (LLM) agents from the traces of the tools they call. In the eleven evaluations we audited, attacks or anomalies make up 16% to 86% of the test samples, no evaluation varies that share, and six report no test on data from a second b
- **[From Evaluation to Evolution: Benchmarking Image Editing and Evolving Image Models](https://arxiv.org/abs/2610.41210v1)** _(score 13.3 · 2026-10-30 · Jun He, Canmiao Fu, Ying Zhang…)_
  Real-world image editing requires coordinating multiple visual transformations with content preservation and reference constraints, yet aggregate scores can readily obscure unmet local requirements. Effective evaluation must therefore identify local failures and translate them in
- **[GraphNIAH: A Benchmark for Long-Context Reasoning over Real-World Graphs](https://arxiv.org/abs/2610.41704v1)** _(score 12.3 · 2026-10-30 · Minh-Nam Tran, Abulhair Saparov)_
  The needle-in-a-haystack (NIAH) benchmark was introduced as a test for measuring a model's ability to find small relevant facts within a very large body of input text. However, existing NIAH benchmarks each suffer from one or more of the following limitations: (1) reliance on syn
- **[OpenTWBench (Open Taiwan Benchmark): Taiwan-Domain Knowledge Evaluation for Large Language Models, and How the Measurement Apparatus Shapes the Score](https://arxiv.org/abs/2610.19848v1)** _(score 12.233 · 2026-10-14 · Liang-Hsun Huang, Min-Yi Chen, Chao-Chun Chuang…)_
  We present OpenTWBench, an open evaluation suite for Taiwan-domain knowledge in large language models, built around two benchmarks. tw-exam-bench contains 255,854 four-option questions across 148 academic subjects, from fifteen years of Taiwan's national examinations published as
- **[ProSearch: Benchmarking Multi-Constraint Protocol Retrieval in Experimental Science](https://arxiv.org/abs/2610.41396v1)** _(score 11.8 · 2026-10-30 · Wenliang Liang, Zhiyuan Ning, Haolin Chen…)_
  In AI for Science scenarios, experimental design and method reproduction require retrieving protocols that satisfy multiple interdependent constraints, yet existing benchmarks lack systematic evaluation of this capability. To address this gap, we introduce ProSearch, a benchmark
- **[Better Retrievers, Worse Labels: How Incomplete Relevance Judgments Distort Abstention Evaluation in Conversational RAG](https://arxiv.org/abs/2610.40966v1)** _(score 11.8 · 2026-10-29 · Ivan Kochergin, Vasily Konovalov)_
  Conversational RAG benchmarks such as MTRAG and RETECO evaluate retrieval and generation end to end: each system answers from its own retrieval, so abstention must be scored against whether each retrieved context is sufficient. A convenient shortcut reads sufficiency off the rele
- **[Re-executing Coding-Agent Evaluations: Unchanged Decisions and Unresolved Policy Risk](https://arxiv.org/abs/2610.14460v1)** _(score 10.467 · 2026-10-10 · Tianyu Ding, Yaocheng Tong, Muzhi Yang…)_
  Executable tests grade large language model (LLM) coding-agent patches for leaderboards, rewards and self-improvement. Two preregistered re-execution studies returned negative results. SWE-bench Pro v1's offline option rejected none of 59 accepted Go patches whose grading configu
- **[Multi-Test Nation Bias Benchmarking of LLMs with Explicit Unbiased Baselines](https://arxiv.org/abs/2610.41486v1)** _(score 10.3 · 2026-10-30 · Jonghyeon Choi, Yeonjun Choi, Beakcheol Jang)_
  While prior work has highlighted that systematic nation-level bias in large language models (LLMs) can pose operational risks for international relations (IR) applications, many existing evaluations still lack a clearly specified unbiased reference (ground truth), limiting fully
- **[ANGLER: Verifier-Grounded Benchmarking with an Adaptive Attacker for Web Agents](https://arxiv.org/abs/2610.41272v1)** _(score 10.3 · 2026-10-30 · Yini Huang, Aiwen LU, Zhen Sun…)_
  Web agents are increasingly deployed to complete tasks autonomously on real websites, where adversarially injected content can induce them to perform unauthorized actions. Existing evaluations primarily use fixed attacks or focus on a single attack type, and evaluate attacks at t
- **[ImplicitHop: Evaluating knowledge integration across context and memory](https://arxiv.org/abs/2610.41169v1)** _(score 10.3 · 2026-10-30 · Alexander Detkov, Dashiel Karish, Matthew Oleynikov…)_
  The ability to integrate new information and deduce its consequences is central to learning, understanding, and reasoning in large language models (LLMs). Whether information arrives during training or in-context, models must not only store local facts, but propagate their long-r
- **[Benchmarking Forecasting Agents on Yesterday's Tomorrows](https://arxiv.org/abs/2610.40940v1)** _(score 10.3 · 2026-10-29 · Yuxuan Wang, Yishu Wang, Jiaqi Deng)_
  Digital agents can now gather and organize information, reason over it, and use tools to complete complex tasks. Forecasting puts all of these abilities to the test: it requires integrating incomplete evidence, inferring causal drivers, and committing to calibrated probabilistic
- **[SocialArena: Evaluating Social Intelligence in Large Language Models](https://arxiv.org/abs/2610.39247v1)** _(score 10.233 · 2026-10-29 · Zongqi Wang, Rui Wang, Yuchuan Wu…)_
  We introduce SocialArena, a benchmark for systematically defining and evaluating the social intelligence of large language models (LLMs). Although LLMs are increasingly deployed in socially interactive applications such as mental health counseling, companionship chatbots, and edu

### Huggingface (1)

- **[abdullahashraf122/algomyth-code-generation-benchmark](https://huggingface.co/datasets/abdullahashraf122/algomyth-code-generation-benchmark)** _(score 7.505 · 2026-10-18 · 55 downloads)_
  Hugging Face dataset — 55 downloads, 0 likes. Tags: task_categories:text-generation, annotations_creators:machine-generated, multilinguality:monolingual, source_datasets:original, language:en

---

_Produced by [OpenBench Radar](https://github.com/) — automated benchmark retrieval, research & reporting._