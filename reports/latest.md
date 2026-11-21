# OpenBench Radar — AI/LLM Benchmark Digest

> Generated **2026-11-21 15:56 UTC** · 59 items · topics: LLM evaluation benchmark, large language model leaderboard, code generation benchmark, reasoning benchmark LLM, agent benchmark evaluation · analysis: extractive fallback

## Executive Summary

Retrieved **59** relevant items across topics (LLM evaluation benchmark, large language model leaderboard, code generation benchmark, reasoning benchmark LLM, agent benchmark evaluation): 57 from arxiv, 2 from huggingface. The most relevant findings, ranked by a keyword/recency/popularity heuristic, are listed below. (Set OPENAI_API_KEY to enable an LLM-written analytical summary.)

## Key Highlights

- [arxiv] SOTA or Luck? The Winner's Curse in LLM Leaderboards — Public LLM leaderboards guide model evaluation and adoption, yet the reported performance of top-ranked models can be systematically oversta
- [huggingface] goodgentleman918/ai-data-quality-llm-evaluation-benchmark — Hugging Face dataset — 112 downloads, 1 likes. Tags: task_categories:reinforcement-learning, language:en, license:mit, size_categories:n<1K,
- [arxiv] SAGE-QA: Semantic-Aware, Grounded Evaluation for Closed-Context Question Answering on SQuAD 2.0 — Closed-context question answering (QA) requires a system to generate an answer strictly supported by a supplied passage, or to abstain when
- [arxiv] PILAPS: A Bilingual Benchmark for Evaluating Pragmatic Inference across Phenomena and Settings — Recent work reports strong pragmatic performance by large language models (LLMs) in English, yet whether this performance generalises across
- [arxiv] Verifiable Logic in Medical LLMs: A Critical Review of Agentic Clinical Reasoning Optimization and Neuro-Symbolic Grounding — Clinical large language models are usually judged by whether the final answer is right. Yet a model can reach a fluent, plausible output thr
- [arxiv] The Stability Gap in Continual Reinforcement Learning — Continual reinforcement learning (CRL) aims to enable agents to adapt to changing tasks while preserving previously acquired capabilities. E

## Findings by Source

### Arxiv (57)

- **[SOTA or Luck? The Winner's Curse in LLM Leaderboards](https://arxiv.org/abs/2611.22227v1)** _(score 15.733 · 2026-11-17 · Sikun Xu, Raphael Thomadsen, Dennis J. Zhang…)_
  Public LLM leaderboards guide model evaluation and adoption, yet the reported performance of top-ranked models can be systematically overstated. This leaderboard winner's curse arises because ranking noisy benchmark scores rewards sampling luck alongside genuine ability. The same
- **[SAGE-QA: Semantic-Aware, Grounded Evaluation for Closed-Context Question Answering on SQuAD 2.0](https://arxiv.org/abs/2611.16300v1)** _(score 13.4 · 2026-11-12 · Chandra N Sekharan, Vishakan Umapathy, Abhishek Phadke)_
  Closed-context question answering (QA) requires a system to generate an answer strictly supported by a supplied passage, or to abstain when the passage lacks adequate evidence. SQuAD 2.0 is a widely used benchmark for this setting, scored by Exact Match (EM) i.e., character-level
- **[PILAPS: A Bilingual Benchmark for Evaluating Pragmatic Inference across Phenomena and Settings](https://arxiv.org/abs/2611.25459v1)** _(score 11.867 · 2026-11-19 · Jiani Cao, Anna Korhonen, Chen Cecilia Liu)_
  Recent work reports strong pragmatic performance by large language models (LLMs) in English, yet whether this performance generalises across languages and evaluation settings remains unclear. This question is increasingly important as LLMs are deployed across languages, cultures,
- **[Verifiable Logic in Medical LLMs: A Critical Review of Agentic Clinical Reasoning Optimization and Neuro-Symbolic Grounding](https://arxiv.org/abs/2611.25898v1)** _(score 10.867 · 2026-11-19 · Youssef ElNahas, Adel Ammar, Soumaya Chaffar…)_
  Clinical large language models are usually judged by whether the final answer is right. Yet a model can reach a fluent, plausible output through invalid reasoning that static benchmarks do not detect, and confident hallucination, causally invalid inference, and spurious demograph
- **[The Stability Gap in Continual Reinforcement Learning](https://arxiv.org/abs/2611.26252v1)** _(score 10.867 · 2026-11-19 · Sebastian Pusch, Matthia Sabatelli, Gido M. van de Ven)_
  Continual reinforcement learning (CRL) aims to enable agents to adapt to changing tasks while preserving previously acquired capabilities. Evaluation often relies on final aggregate metrics that can hide temporary performance degradation during adaptation. This work introduces a
- **[ClosureBench: A Benchmark for Reasoning under Closure Assumptions](https://arxiv.org/abs/2611.26335v1)** _(score 10.433 · 2026-11-19 · Francesco Belardinelli, Flavio Corradini, Matteo Leonesi)_
  AI agents built on large language models (LLMs) often answer questions from incomplete records. Missing information might be interpreted as unknown or false, depending on the completeness of the source. Current evaluations fail to distinguish these two aspects, as they are usuall
- **[Same Judgement, Different Scores: Numerical Scoring Topology in LLM-as-a-Judge Evaluation](https://arxiv.org/abs/2611.26077v1)** _(score 9.867 · 2026-11-19 · Doyun Kim, Chanwoo Kim, Jiwoo Kum…)_
  LLMs are increasingly used as automated evaluators to reduce the cost and time required for human annotation. However, the role of scoring-scheme design in the reliability of LLM-as-a-Judge evaluation remains underexplored. To address this problem, we introduce numerical scoring
- **[LINEAGE: A Benchmark for Empirical Lineage Retrieval in AI Scientific Literature](https://arxiv.org/abs/2611.25845v1)** _(score 9.867 · 2026-11-19 · Pangjing Wu, Xu Yuan, Wenqi Fan…)_
  Current research agents are moving beyond academic search toward literature synthesis and experiment planning. These workflows increasingly rely on literature retrieval systems, which serve as standalone systems or as components of research agents. However, existing scientific li
- **[AI Isn't Getting Dumber, We're Getting Pickier: Rising Standards in Human Evaluation of Large Language Models](https://arxiv.org/abs/2611.14333v1)** _(score 9.333 · 2026-11-10 · Zihan Chen, Lei Nico Zheng, Di Zhu)_
  Users often complain that AI assistants such as ChatGPT are getting worse. Some versions do change, but human evaluation leaves a second possibility untested: the people judging may change. We separate the two on Chatbot Arena, a public platform where people compare answers from
- **[The FrontierOR Challenge: Agentic Algorithm Design for Operations Research](https://arxiv.org/abs/2611.26171v1)** _(score 8.867 · 2026-11-19 · Hai Wang, Bretislav Hajek, Chonghe Jiang…)_
  Operations research (OR) relies on algorithms that experts tailor to each problem: a new routing, scheduling or network design problem can take weeks of specialist work before it is solved well at scale. Large language model (LLM) agents now write, test and improve code, but whet
- **[Rubric Semantics or Numerical Priors? Auditing Scale-Direction Bias in LLM Judges](https://arxiv.org/abs/2611.25588v1)** _(score 8.867 · 2026-11-19 · Chanwoo Kim, Doyun Kim, Minsoo Song…)_
  Recent benchmark evaluations increasingly rely on Large Language Models (LLMs) as automatic judges. This paradigm assumes LLMs evaluate based on the rubric's semantic meaning rather than its numeric scale. We question this assumption by introducing semantic faithfulness: the prin
- **[Why Do LLMs Help with Scientific Misconduct Requests and What to Do About It?: Increasing the Trustworthiness of AI for Science](https://arxiv.org/abs/2611.25492v1)** _(score 8.867 · 2026-11-19 · Almene De Meran Meguimtsop, Daniel E. Acuna)_
  Large language models (LLMs) support scientific research, but some of that assistance can also undermine research integrity. Existing safety evaluations in science often measure whether models refuse misconduct requests, but rarely explain whether they even recognize the problem

### Huggingface (2)

- **[goodgentleman918/ai-data-quality-llm-evaluation-benchmark](https://huggingface.co/datasets/goodgentleman918/ai-data-quality-llm-evaluation-benchmark)** _(score 14.788 · 2026-11-10 · 112 downloads)_
  Hugging Face dataset — 112 downloads, 1 likes. Tags: task_categories:reinforcement-learning, language:en, license:mit, size_categories:n<1K, modality:text
- **[abdullahashraf122/algomyth-code-generation-benchmark](https://huggingface.co/datasets/abdullahashraf122/algomyth-code-generation-benchmark)** _(score 6.235 · 2026-10-18 · 20 downloads)_
  Hugging Face dataset — 20 downloads, 0 likes. Tags: task_categories:text-generation, annotations_creators:machine-generated, multilinguality:monolingual, source_datasets:original, language:en

---

_Produced by [OpenBench Radar](https://github.com/) — automated benchmark retrieval, research & reporting._