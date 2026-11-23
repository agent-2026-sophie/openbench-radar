# OpenBench Radar — AI/LLM Benchmark Digest

> Generated **2026-11-23 19:54 UTC** · 64 items · topics: LLM evaluation benchmark, large language model leaderboard, code generation benchmark, reasoning benchmark LLM, agent benchmark evaluation · analysis: extractive fallback

## Executive Summary

Retrieved **64** relevant items across topics (LLM evaluation benchmark, large language model leaderboard, code generation benchmark, reasoning benchmark LLM, agent benchmark evaluation): 62 from arxiv, 2 from huggingface. The most relevant findings, ranked by a keyword/recency/popularity heuristic, are listed below. (Set OPENAI_API_KEY to enable an LLM-written analytical summary.)

## Key Highlights

- [arxiv] SOTA or Luck? The Winner's Curse in LLM Leaderboards — Public LLM leaderboards guide model evaluation and adoption, yet the reported performance of top-ranked models can be systematically oversta
- [huggingface] goodgentleman918/ai-data-quality-llm-evaluation-benchmark — Hugging Face dataset — 115 downloads, 1 likes. Tags: task_categories:reinforcement-learning, language:en, license:mit, size_categories:n<1K,
- [arxiv] Modeling Attributional Style at Scale: A Dataset and Analysis for Psychological Attribution Assessment and Reframing — According to the reformulated Learned Helplessness theory, repeated exposure to uncontrollable negative events can foster a depressogenic at
- [arxiv] Schema-Validated LLM Workflows: A Benchmark Protocol and Comparative Evaluation Across Six Python Implementations — Large language models are increasingly used to extract records, generate SQL, summarize reports, answer policy questions, and route operatio
- [arxiv] SAGE-QA: Semantic-Aware, Grounded Evaluation for Closed-Context Question Answering on SQuAD 2.0 — Closed-context question answering (QA) requires a system to generate an answer strictly supported by a supplied passage, or to abstain when
- [arxiv] Benchmarks' Last Exam — Public benchmarks guide model selection, post-training rewards and claims of progress in artificial intelligence, yet leaderboards report ag

## Findings by Source

### Arxiv (62)

- **[SOTA or Luck? The Winner's Curse in LLM Leaderboards](https://arxiv.org/abs/2611.22227v1)** _(score 15.6 · 2026-11-17 · Sikun Xu, Raphael Thomadsen, Dennis J. Zhang…)_
  Public LLM leaderboards guide model evaluation and adoption, yet the reported performance of top-ranked models can be systematically overstated. This leaderboard winner's curse arises because ranking noisy benchmark scores rewards sampling luck alongside genuine ability. The same
- **[Modeling Attributional Style at Scale: A Dataset and Analysis for Psychological Attribution Assessment and Reframing](https://arxiv.org/abs/2611.26900v1)** _(score 14.3 · 2026-11-19 · Qiang Zhou, Hanzhen Zhu, Pan Wang…)_
  According to the reformulated Learned Helplessness theory, repeated exposure to uncontrollable negative events can foster a depressogenic attributional style, increasing susceptibility to depression yet remaining a tractable target for cognitive therapy. Computational research on
- **[Schema-Validated LLM Workflows: A Benchmark Protocol and Comparative Evaluation Across Six Python Implementations](https://arxiv.org/abs/2611.27106v1)** _(score 13.3 · 2026-11-20 · Sidney Shapiro, Sanad Al-Khatib, Aurora Pinzón Arzola…)_
  Large language models are increasingly used to extract records, generate SQL, summarize reports, answer policy questions, and route operational work. At these software boundaries, parseable output is necessary but does not establish task correctness. We present a reproducible ben
- **[SAGE-QA: Semantic-Aware, Grounded Evaluation for Closed-Context Question Answering on SQuAD 2.0](https://arxiv.org/abs/2611.16300v1)** _(score 13.267 · 2026-11-12 · Chandra N Sekharan, Vishakan Umapathy, Abhishek Phadke)_
  Closed-context question answering (QA) requires a system to generate an answer strictly supported by a supplied passage, or to abstain when the passage lacks adequate evidence. SQuAD 2.0 is a widely used benchmark for this setting, scored by Exact Match (EM) i.e., character-level
- **[Benchmarks' Last Exam](https://arxiv.org/abs/2611.27622v1)** _(score 12.3 · 2026-11-20 · James Zhu, Zekki Cat)_
  Public benchmarks guide model selection, post-training rewards and claims of progress in artificial intelligence, yet leaderboards report aggregate scores without verifying whether each task's prompt, environment and grader agree on what counts as success. How often that agreemen
- **[Observed, Curated, Reused: Observation Bias in Clinical AI Evaluation](https://arxiv.org/abs/2611.27301v1)** _(score 11.8 · 2026-11-20 · Md Shamim Ahmed, Lukas Galke Poech, Richard Röttger)_
  Clinical AI evaluations are vulnerable to observation bias embedded in routine medical documentation, which captures only what clinicians notice, test, and record rather than a complete clinical picture. As this evidence travels into publications and reference knowledge graphs, c
- **[Verifiable Logic in Medical LLMs: A Critical Review of Agentic Clinical Reasoning Optimization and Neuro-Symbolic Grounding](https://arxiv.org/abs/2611.25898v1)** _(score 10.733 · 2026-11-19 · Youssef ElNahas, Adel Ammar, Soumaya Chaffar…)_
  Clinical large language models are usually judged by whether the final answer is right. Yet a model can reach a fluent, plausible output through invalid reasoning that static benchmarks do not detect, and confident hallucination, causally invalid inference, and spurious demograph
- **[Who Grades the Agent? Privilege Separation for Coding-Agent Benchmarks](https://arxiv.org/abs/2611.27860v1)** _(score 10.3 · 2026-11-20 · Nathan Nour Houlamy, Mattia Favretto, Earlence Fernandes…)_
  Benchmarks for AI-based coding agents are a staple of the current AI landscape, because they are the leading way to measure the performance of LLMs. Their scores guide business and research decisions. Evaluating coding agents is challenging, since they are able to manipulate thei
- **[Your Judge Inherits Your Prompt: In-Context Label Bias in an LLM-as-Judge Is Directional, Not Symmetric](https://arxiv.org/abs/2611.26881v1)** _(score 10.3 · 2026-11-19 · Abdullah Ahmad, Ahmed J. O. Ahmed, Luca Citi)_
  LLM-as-judge has become a standard way to score open-ended model outputs, yet the judge is itself a frozen language model steered by a few in-context examples, and such models are known to absorb the label balance of their demonstrations rather than treat them as neutral illustra
- **[ClosureBench: A Benchmark for Reasoning under Closure Assumptions](https://arxiv.org/abs/2611.26335v1)** _(score 10.233 · 2026-11-19 · Francesco Belardinelli, Flavio Corradini, Matteo Leonesi)_
  AI agents built on large language models (LLMs) often answer questions from incomplete records. Missing information might be interpreted as unknown or false, depending on the completeness of the source. Current evaluations fail to distinguish these two aspects, as they are usuall
- **[AI Isn't Getting Dumber, We're Getting Pickier: Rising Standards in Human Evaluation of Large Language Models](https://arxiv.org/abs/2611.14333v1)** _(score 9.133 · 2026-11-10 · Zihan Chen, Lei Nico Zheng, Di Zhu)_
  Users often complain that AI assistants such as ChatGPT are getting worse. Some versions do change, but human evaluation leaves a second possibility untested: the people judging may change. We separate the two on Chatbot Arena, a public platform where people compare answers from
- **[Jagged Robustness: Uneven Safety Transfer and Emerging Vulnerabilities under LLM Quantization](https://arxiv.org/abs/2611.27424v1)** _(score 8.8 · 2026-11-20 · Ramneek Agnihotri, Yingte Xu, Hans Vath)_
  Quantization enables efficient inference in language models through model parameter compression. This work audits the impact of quantization on capability and safety domains including model safeguards, instruction-following, ethics and bias. Through benchmarks, we find that model

### Huggingface (2)

- **[goodgentleman918/ai-data-quality-llm-evaluation-benchmark](https://huggingface.co/datasets/goodgentleman918/ai-data-quality-llm-evaluation-benchmark)** _(score 14.655 · 2026-11-10 · 115 downloads)_
  Hugging Face dataset — 115 downloads, 1 likes. Tags: task_categories:reinforcement-learning, language:en, license:mit, size_categories:n<1K, modality:text
- **[abdullahashraf122/algomyth-code-generation-benchmark](https://huggingface.co/datasets/abdullahashraf122/algomyth-code-generation-benchmark)** _(score 6.102 · 2026-10-18 · 19 downloads)_
  Hugging Face dataset — 19 downloads, 0 likes. Tags: task_categories:text-generation, annotations_creators:machine-generated, multilinguality:monolingual, source_datasets:original, language:en

---

_Produced by [OpenBench Radar](https://github.com/) — automated benchmark retrieval, research & reporting._