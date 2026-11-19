# OpenBench Radar — AI/LLM Benchmark Digest

> Generated **2026-11-19 17:08 UTC** · 64 items · topics: LLM evaluation benchmark, large language model leaderboard, code generation benchmark, reasoning benchmark LLM, agent benchmark evaluation · analysis: extractive fallback

## Executive Summary

Retrieved **64** relevant items across topics (LLM evaluation benchmark, large language model leaderboard, code generation benchmark, reasoning benchmark LLM, agent benchmark evaluation): 62 from arxiv, 2 from huggingface. The most relevant findings, ranked by a keyword/recency/popularity heuristic, are listed below. (Set OPENAI_API_KEY to enable an LLM-written analytical summary.)

## Key Highlights

- [arxiv] SOTA or Luck? The Winner's Curse in LLM Leaderboards — Public LLM leaderboards guide model evaluation and adoption, yet the reported performance of top-ranked models can be systematically oversta
- [arxiv] AfriNORM: An Evaluation Benchmark for Normative Reasoning of LLMs Across African Cultures — Large language models (LLMs) are increasingly deployed across various sectors. However, current evaluation benchmarks are insufficient to as
- [huggingface] goodgentleman918/ai-data-quality-llm-evaluation-benchmark — Hugging Face dataset — 109 downloads, 1 likes. Tags: task_categories:reinforcement-learning, language:en, license:mit, size_categories:n<1K,
- [arxiv] SAGE-QA: Semantic-Aware, Grounded Evaluation for Closed-Context Question Answering on SQuAD 2.0 — Closed-context question answering (QA) requires a system to generate an answer strictly supported by a supplied passage, or to abstain when
- [arxiv] On Evaluating User Simulators for Interactive Agents — User simulators offer a scalable way to evaluate interactive agents, but how to assess their quality remains underexplored. In particular, i
- [arxiv] Who Pays for Byzantine Robustness? Validity, Data-Share Dictatorships, and Fairness When Only a Few Hospitals Collaborate — Clinical federated learning (FL) collaborations typically connect only three to six hospitals, yet Byzantine-robust aggregation rules are de

## Findings by Source

### Arxiv (62)

- **[SOTA or Luck? The Winner's Curse in LLM Leaderboards](https://arxiv.org/abs/2611.22227v1)** _(score 15.867 · 2026-11-17 · Sikun Xu, Raphael Thomadsen, Dennis J. Zhang…)_
  Public LLM leaderboards guide model evaluation and adoption, yet the reported performance of top-ranked models can be systematically overstated. This leaderboard winner's curse arises because ranking noisy benchmark scores rewards sampling luck alongside genuine ability. The same
- **[AfriNORM: An Evaluation Benchmark for Normative Reasoning of LLMs Across African Cultures](https://arxiv.org/abs/2611.22580v1)** _(score 15.367 · 2026-11-17 · Ahmad Samuel Gali, Tadesse Destaw Belay, Idris Abdulmumin…)_
  Large language models (LLMs) are increasingly deployed across various sectors. However, current evaluation benchmarks are insufficient to assess the applicability of these models in local African contexts, as most focus on linguistic fluency (grammar/translation) rather than cult
- **[SAGE-QA: Semantic-Aware, Grounded Evaluation for Closed-Context Question Answering on SQuAD 2.0](https://arxiv.org/abs/2611.16300v1)** _(score 13.533 · 2026-11-12 · Chandra N Sekharan, Vishakan Umapathy, Abhishek Phadke)_
  Closed-context question answering (QA) requires a system to generate an answer strictly supported by a supplied passage, or to abstain when the passage lacks adequate evidence. SQuAD 2.0 is a widely used benchmark for this setting, scored by Exact Match (EM) i.e., character-level
- **[On Evaluating User Simulators for Interactive Agents](https://arxiv.org/abs/2611.24892v1)** _(score 12.5 · 2026-11-18 · Hengguang Zhou, I-Hung Hsu, Li Chen…)_
  User simulators offer a scalable way to evaluate interactive agents, but how to assess their quality remains underexplored. In particular, it is unclear whether existing user simulator evaluation frameworks reliably detect meaningful failures in simulated user behavior. This unce
- **[Who Pays for Byzantine Robustness? Validity, Data-Share Dictatorships, and Fairness When Only a Few Hospitals Collaborate](https://arxiv.org/abs/2611.22904v1)** _(score 10.867 · 2026-11-17 · Adnan Malkani)_
  Clinical federated learning (FL) collaborations typically connect only three to six hospitals, yet Byzantine-robust aggregation rules are designed and benchmarked on synthetic partitions across dozens of equal-sized clients. We conduct an empirical audit of eight standard aggrega
- **[Benchmarking LLM abilities on postdoc-level natural science problems](https://arxiv.org/abs/2611.24321v1)** _(score 10.433 · 2026-11-18 · Alina Avanesyan, Alexey Boldyrev, Liqun Deng…)_
  Scientific problems have no answer key, so evaluating an agent means deciding what counts as a better solution before any agent is run. Existing benchmarks either match a symbolic answer against a key or, where they require executable work, score it by unit tests, by a rubric, or
- **[A Capability Framework for Evaluating Agentic AI Platforms in Regulated Enterprises](https://arxiv.org/abs/2611.24039v1)** _(score 10.433 · 2026-11-18 · Abbas Raza Ali, Muhammad Ajmal Siddiqui, Moona Zahid)_
  Agentic AI platforms-systems in which LLM agents plan, invoke tools, retain memory and coordinate to change the state of enterprise systems-are being procured faster than they can be measured. Public agent benchmarks score models in fixed harnesses; enterprises buy integrated pla
- **[RFBench: A Simulator-Grounded Multimodal Benchmark for Passive RF Layout Design and Understanding](https://arxiv.org/abs/2611.23410v1)** _(score 10.433 · 2026-11-17 · Jiarui Cui, Boxun Yan)_
  While multimodal language models can interpret diagrams and generate structured outputs, their capacity to connect passive radio-frequency (RF) design intent, layout geometry, and electromagnetic behavior remains largely untested. To address this gap, we introduce RFBench, a simu
- **[ForecastGym: A Live, Controlled, and Replayable Benchmark for Forecasting Agents](https://arxiv.org/abs/2611.23045v1)** _(score 10.367 · 2026-11-17 · Yicheng Tao, Yuante Li, Zipei Fan)_
  Agents built on large language models (LLMs) increasingly forecast real-world events by searching the Web and reasoning over what they find. How well such an agent forecasts depends on both the retrieved evidence and the model, making control over that evidence essential for eval
- **[Evaluating Governed LLM-Driven ML Experimentation: Lifecycle, Provenance, and Failure Metrics](https://arxiv.org/abs/2611.23678v1)** _(score 9.933 · 2026-11-18 · Dowling Wong)_
  Autonomous agents that run ML experiments are usually judged by the best score they reach. That score says nothing about how it was reached: whether the agent stayed within the files it was allowed to edit, whether failed trials were kept or silently dropped, and whether each kee
- **[AI Isn't Getting Dumber, We're Getting Pickier: Rising Standards in Human Evaluation of Large Language Models](https://arxiv.org/abs/2611.14333v1)** _(score 9.4 · 2026-11-10 · Zihan Chen, Lei Nico Zheng, Di Zhu)_
  Users often complain that AI assistants such as ChatGPT are getting worse. Some versions do change, but human evaluation leaves a second possibility untested: the people judging may change. We separate the two on Chatbot Arena, a public platform where people compare answers from
- **[Reliability is a user-specific property of large language models](https://arxiv.org/abs/2611.23732v1)** _(score 8.933 · 2026-11-18 · Xingyu Zhao)_
  Public benchmarks support comparisons of large language model (LLM) capabilities, yet users can experience the same highly ranked model differently. Drawing on traditional software reliability, we argue that the reliability of an LLM service should be assessed for specified users

### Huggingface (2)

- **[goodgentleman918/ai-data-quality-llm-evaluation-benchmark](https://huggingface.co/datasets/goodgentleman918/ai-data-quality-llm-evaluation-benchmark)** _(score 14.921 · 2026-11-10 · 109 downloads)_
  Hugging Face dataset — 109 downloads, 1 likes. Tags: task_categories:reinforcement-learning, language:en, license:mit, size_categories:n<1K, modality:text
- **[abdullahashraf122/algomyth-code-generation-benchmark](https://huggingface.co/datasets/abdullahashraf122/algomyth-code-generation-benchmark)** _(score 6.369 · 2026-10-18 · 21 downloads)_
  Hugging Face dataset — 21 downloads, 0 likes. Tags: task_categories:text-generation, annotations_creators:machine-generated, multilinguality:monolingual, source_datasets:original, language:en

---

_Produced by [OpenBench Radar](https://github.com/) — automated benchmark retrieval, research & reporting._