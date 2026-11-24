# OpenBench Radar — AI/LLM Benchmark Digest

> Generated **2026-11-24 19:23 UTC** · 64 items · topics: LLM evaluation benchmark, large language model leaderboard, code generation benchmark, reasoning benchmark LLM, agent benchmark evaluation · analysis: extractive fallback

## Executive Summary

Retrieved **64** relevant items across topics (LLM evaluation benchmark, large language model leaderboard, code generation benchmark, reasoning benchmark LLM, agent benchmark evaluation): 62 from arxiv, 2 from huggingface. The most relevant findings, ranked by a keyword/recency/popularity heuristic, are listed below. (Set OPENAI_API_KEY to enable an LLM-written analytical summary.)

## Key Highlights

- [arxiv] SOTA or Luck? The Winner's Curse in LLM Leaderboards — Public LLM leaderboards guide model evaluation and adoption, yet the reported performance of top-ranked models can be systematically oversta
- [huggingface] goodgentleman918/ai-data-quality-llm-evaluation-benchmark — Hugging Face dataset — 115 downloads, 1 likes. Tags: task_categories:reinforcement-learning, language:en, license:mit, size_categories:n<1K,
- [arxiv] SAGE-QA: Semantic-Aware, Grounded Evaluation for Closed-Context Question Answering on SQuAD 2.0 — Closed-context question answering (QA) requires a system to generate an answer strictly supported by a supplied passage, or to abstain when
- [arxiv] ESGPT: A Data-Centric ESG Language Model with Unified Instruction and Benchmark Resources — ESG analysis requires complex language understanding across diverse sources, including corporate reports, news, and disclosures, for tasks s
- [arxiv] Diversity in Unity, Theory in Practice: Hierarchical Multitask Benchmarks for Chinese Minority Languages — Despite the rapid advancement of LLMs, their performance on linguistically and culturally diverse minority languages within a unified nation
- [arxiv] Transport-Safe Evaluation of LLM Agents: Trajectory-Dependent Judge Error and Anytime-Valid Auditing — Large language model (LLM) agents are often ranked by an LLM judge whose error rates are measured once and reused for every agent. The corre

## Findings by Source

### Arxiv (62)

- **[SOTA or Luck? The Winner's Curse in LLM Leaderboards](https://arxiv.org/abs/2611.22227v1)** _(score 15.533 · 2026-11-17 · Sikun Xu, Raphael Thomadsen, Dennis J. Zhang…)_
  Public LLM leaderboards guide model evaluation and adoption, yet the reported performance of top-ranked models can be systematically overstated. This leaderboard winner's curse arises because ranking noisy benchmark scores rewards sampling luck alongside genuine ability. The same
- **[SAGE-QA: Semantic-Aware, Grounded Evaluation for Closed-Context Question Answering on SQuAD 2.0](https://arxiv.org/abs/2611.16300v1)** _(score 13.2 · 2026-11-12 · Chandra N Sekharan, Vishakan Umapathy, Abhishek Phadke)_
  Closed-context question answering (QA) requires a system to generate an answer strictly supported by a supplied passage, or to abstain when the passage lacks adequate evidence. SQuAD 2.0 is a widely used benchmark for this setting, scored by Exact Match (EM) i.e., character-level
- **[ESGPT: A Data-Centric ESG Language Model with Unified Instruction and Benchmark Resources](https://arxiv.org/abs/2611.30052v1)** _(score 12.433 · 2026-11-23 · Jaeyoung Lee, Misuk Kim)_
  ESG analysis requires complex language understanding across diverse sources, including corporate reports, news, and disclosures, for tasks such as ESG relevance detection, action interpretation, impact analysis, and question answering. However, existing ESG datasets are fragmente
- **[Diversity in Unity, Theory in Practice: Hierarchical Multitask Benchmarks for Chinese Minority Languages](https://arxiv.org/abs/2611.29635v1)** _(score 12.367 · 2026-11-22 · Yijie Li, Xi Cao, Yuan Sun…)_
  Despite the rapid advancement of LLMs, their performance on linguistically and culturally diverse minority languages within a unified national context remains underexplored. We present CMiLBench, a collection of hierarchical multitask benchmarks designed to translate theoretical
- **[Transport-Safe Evaluation of LLM Agents: Trajectory-Dependent Judge Error and Anytime-Valid Auditing](https://arxiv.org/abs/2611.30742v1)** _(score 11.933 · 2026-11-23 · Yulliwas Ameur, Samia Bouzefrane, Soumya Banerjee)_
  Large language model (LLM) agents are often ranked by an LLM judge whose error rates are measured once and reused for every agent. The corrected success rates can then be biased when the judge's errors depend on the trajectory and agents differ in the trajectories they produce fo
- **[Attributing Security Outcomes in LLM-Agent Evaluations: The Role of Content-Free State](https://arxiv.org/abs/2611.30259v1)** _(score 11.933 · 2026-11-23 · Abdelmonaim Bounite, Zangir Iklassov)_
  Security benchmarks for LLM agents record whether each attack succeeded and compare agents, attacks, and defenses by attack success rate (ASR). Such comparisons are valid only if the agent, the attack, and the defense cause each verdict. We show that verdicts also depend on conte
- **[Self-Evolving Evaluation Environments for Computer-Use Agents](https://arxiv.org/abs/2611.30962v1)** _(score 11.933 · 2026-11-23 · Wenhao Wang, Panrong Tong, Quyu Kong…)_
  Computer-use agents (CUAs) are rapidly improving, yet their evaluation remains largely static. Existing benchmarks provide a strong foundation, but fixed difficulty ceilings, limited feature coverage, and coarse aggregate scores progressively weaken their discriminative and diagn
- **[Schedule, Rank, Profile: Continuous Evaluation of LLM Agents in Games](https://arxiv.org/abs/2611.28368v1)** _(score 11.8 · 2026-11-20 · Martyna Plomecka, Yao Yan, DJ Sterling…)_
  Games are a robust test for large language model agents: they require sequential decisions, adversarial or cooperative interaction, state tracking, reasoning under uncertainty, and long-horizon planning. However, a one-time game benchmark can go stale as models, prompts, environm
- **[From Local Errors to System Failures: Modeling and Benchmarking Error Propagation in Multi-Agent LLM Systems](https://arxiv.org/abs/2611.31063v1)** _(score 10.433 · 2026-11-23 · Wenlong Yu, Bingxu Lu, Qilong Wang…)_
  In multi-agent systems (MAS) built on large language models (LLMs), errors can propagate through intermediate messages and compromise final answers. However, outcome-based evaluation obscures how agents amplify, attenuate, or correct these errors. We propose Response-Aware Error
- **[When 1+1 $\neq$ 2: Benchmarking Civil-Time Reasoning in Large Language Models](https://arxiv.org/abs/2611.29972v1)** _(score 10.433 · 2026-11-23 · Melika Shirian, Kianoosh Vadaei, Arshia Hemmat…)_
  Calendar arithmetic is non-linear. When 1:59 AM + 1 minute occurs during daylight saving spring-forward, the result is 3:00 AM, not 2:00 AM, as the hour is skipped. We introduce CivilTime-Bench, a benchmark for civil-time reasoning covering daylight saving transitions, non-hour o
- **[Beyond Accuracy: A Diagnostic Benchmark for Hypothesis-Driven Experiment Planning in LLM Agents](https://arxiv.org/abs/2611.29467v1)** _(score 10.367 · 2026-11-22 · Ryo Kuroki, Amin Mansouri, Philippe Schwaller)_
  Evaluating large language model (LLM) agents on scientific tasks typically reduces to final-task accuracy, which obscures where reasoning succeeds or breaks down. We introduce a benchmark and diagnostic evaluation framework for hypothesis-driven adaptive experimental planning in
- **[BenchMint: From Real-World Tasks to Executable Benchmarks](https://arxiv.org/abs/2611.29367v1)** _(score 10.367 · 2026-11-22 · Zining Huang, Zuo Wang, Mengyao Zhang…)_
  Large language models (LLMs) need evaluations of everyday reasoning and tool use, such as planning itineraries under user constraints and grounding numerical answers in evidence. We introduce BenchMint, an automated benchmark-construction workflow, and Daily-Life, its collection

### Huggingface (2)

- **[goodgentleman918/ai-data-quality-llm-evaluation-benchmark](https://huggingface.co/datasets/goodgentleman918/ai-data-quality-llm-evaluation-benchmark)** _(score 14.588 · 2026-11-10 · 115 downloads)_
  Hugging Face dataset — 115 downloads, 1 likes. Tags: task_categories:reinforcement-learning, language:en, license:mit, size_categories:n<1K, modality:text
- **[abdullahashraf122/algomyth-code-generation-benchmark](https://huggingface.co/datasets/abdullahashraf122/algomyth-code-generation-benchmark)** _(score 6.035 · 2026-10-18 · 21 downloads)_
  Hugging Face dataset — 21 downloads, 0 likes. Tags: task_categories:text-generation, annotations_creators:machine-generated, multilinguality:monolingual, source_datasets:original, language:en

---

_Produced by [OpenBench Radar](https://github.com/) — automated benchmark retrieval, research & reporting._