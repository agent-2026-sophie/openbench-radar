# OpenBench Radar — AI/LLM Benchmark Digest

> Generated **2026-10-26 14:56 UTC** · 61 items · topics: LLM evaluation benchmark, large language model leaderboard, code generation benchmark, reasoning benchmark LLM, agent benchmark evaluation · analysis: extractive fallback

## Executive Summary

Retrieved **61** relevant items across topics (LLM evaluation benchmark, large language model leaderboard, code generation benchmark, reasoning benchmark LLM, agent benchmark evaluation): 59 from arxiv, 2 from huggingface. The most relevant findings, ranked by a keyword/recency/popularity heuristic, are listed below. (Set OPENAI_API_KEY to enable an LLM-written analytical summary.)

## Key Highlights

- [arxiv] OpenTWBench (Open Taiwan Benchmark): Taiwan-Domain Knowledge Evaluation for Large Language Models, and How the Measurement Apparatus Shapes the Score — We present OpenTWBench, an open evaluation suite for Taiwan-domain knowledge in large language models, built around two benchmarks. tw-exam-
- [arxiv] IndoNutriQA: An Indonesian Clinical Nutrition Question Answering Benchmark — Clinical Question Answering (QA) underpins Clinical Intelligent Decision Support Systems, but progress is severely limited for low-resource
- [arxiv] Re-executing Coding-Agent Evaluations: Unchanged Decisions and Unresolved Policy Risk — Executable tests grade large language model (LLM) coding-agent patches for leaderboards, rewards and self-improvement. Two preregistered re-
- [arxiv] Trial by Trace: Benchmarking AI Agent Harnesses for Reliability and Failure Attribution — LLM agents are increasingly used to solve real-world problems, and their effectiveness depends on both the underlying models and the harness
- [arxiv] 4DMemory: Benchmarking Long-Horizon Spatiotemporal Memory with Harness-Augmented Agents — Humans efficiently process multimodal streams spanning hours to years, building persistent, fine-grained spatiotemporal memories that suppor
- [arxiv] Beyond Scalar Leaderboards: Adaptive Sampling for Pareto Frontier Identification in Multi-Objective LLM Arenas — The evaluation of large language models (LLMs) is inherently multi-objective, as different models may offer different tradeoffs across perfo

## Findings by Source

### Arxiv (59)

- **[OpenTWBench (Open Taiwan Benchmark): Taiwan-Domain Knowledge Evaluation for Large Language Models, and How the Measurement Apparatus Shapes the Score](https://arxiv.org/abs/2610.19848v1)** _(score 12.7 · 2026-10-14 · Liang-Hsun Huang, Min-Yi Chen, Chao-Chun Chuang…)_
  We present OpenTWBench, an open evaluation suite for Taiwan-domain knowledge in large language models, built around two benchmarks. tw-exam-bench contains 255,854 four-option questions across 148 academic subjects, from fifteen years of Taiwan's national examinations published as
- **[IndoNutriQA: An Indonesian Clinical Nutrition Question Answering Benchmark](https://arxiv.org/abs/2610.31256v1)** _(score 12.233 · 2026-10-22 · Tirana Noor Fatyanosa, Ummu Ditya Erliana, Mahendra Data…)_
  Clinical Question Answering (QA) underpins Clinical Intelligent Decision Support Systems, but progress is severely limited for low-resource languages such as Indonesian by the absence of public domain-specific data. We introduce IndoNutriQA, an expert-curated Indonesian clinical
- **[Re-executing Coding-Agent Evaluations: Unchanged Decisions and Unresolved Policy Risk](https://arxiv.org/abs/2610.14460v1)** _(score 10.933 · 2026-10-10 · Tianyu Ding, Yaocheng Tong, Muzhi Yang…)_
  Executable tests grade large language model (LLM) coding-agent patches for leaderboards, rewards and self-improvement. Two preregistered re-execution studies returned negative results. SWE-bench Pro v1's offline option rejected none of 59 accepted Go patches whose grading configu
- **[Trial by Trace: Benchmarking AI Agent Harnesses for Reliability and Failure Attribution](https://arxiv.org/abs/2610.32285v1)** _(score 10.3 · 2026-10-23 · Zhiyong Cao, Hengjie Zhu, Yongxin Wang…)_
  LLM agents are increasingly used to solve real-world problems, and their effectiveness depends on both the underlying models and the harnesses that support their operation. However, most existing benchmarks focus on model capabilities and overall agent performance, with limited a
- **[4DMemory: Benchmarking Long-Horizon Spatiotemporal Memory with Harness-Augmented Agents](https://arxiv.org/abs/2610.32332v1)** _(score 10.3 · 2026-10-23 · Yanhao Jia, Yi Zhu, Yiran Zhong…)_
  Humans efficiently process multimodal streams spanning hours to years, building persistent, fine-grained spatiotemporal memories that support reasoning about and predicting long-horizon events. In contrast, existing benchmarks focus on short- and medium-context tasks, and most fo
- **[Beyond Scalar Leaderboards: Adaptive Sampling for Pareto Frontier Identification in Multi-Objective LLM Arenas](https://arxiv.org/abs/2610.27447v1)** _(score 10.1 · 2026-10-20 · Liang Twist Shan, Jiahao Ai, Zhimei Ren)_
  The evaluation of large language models (LLMs) is inherently multi-objective, as different models may offer different tradeoffs across performance dimensions such as math, code, and writing. Because such evaluations are often based on costly and time-consuming human feedback, it
- **[Beyond Leaderboards: A Method for Application-Specific Capability Profiling of Large Language Models](https://arxiv.org/abs/2610.25659v1)** _(score 10.033 · 2026-10-19 · Oleg Grynets, Vasyl Lyashkevych, Andrii Salyk…)_
  Public leaderboards rank large language models (LLMs) in general, but an engineer has to choose a model for a specific application, architecture and cost. This paper presents a method for application-specific capability profiling of LLMs and its realization as a containerized tes
- **[ACE-Compression: An Ability-Centric Evaluation of Compressed Large Language Models](https://arxiv.org/abs/2610.27913v1)** _(score 9.6 · 2026-10-20 · Jiahui Ning, Liang Chen, Yuchen Liang…)_
  Model compression makes large language models deployable, but today's evaluation tells an incomplete story. Standard practice measures retained task performance and stops there. This misses a critical fact: compression perturbs the distributed knowledge embedded across billions o
- **[ACED-Bench: Evaluating How LLM Agents Acquire and Act on Causal Evidence](https://arxiv.org/abs/2610.14381v1)** _(score 9.433 · 2026-10-09 · Yiwei Chen, Amila Weerasinghe, Siddharth Biswal…)_
  Large language models are increasingly used as scientific assistants, yet we still lack reliable ways to evaluate whether they can investigate a system rather than merely answer a prompt. A useful evaluation must let agents choose experiments, interpret finite evidence, and make
- **[Can LLM Annotators Match Human Consistency? Benchmarking Human Agreement and Optimizing Multi-Agent with Contrastive Knowledge](https://arxiv.org/abs/2610.32415v1)** _(score 8.3 · 2026-10-23 · Xiaopeng Ke, Zhixin Wang, Xuebo Liu…)_
  LLM-based annotation has advanced rapidly, yet existing benchmarks remain misaligned with real-world practice. Actual annotation often involves lengthy, task-specific guidelines, and different annotators may produce divergent but reasonable judgments, especially on boundary cases
- **[Tampered ML: Evaluating LLM Judgment of Machine Learning Research](https://arxiv.org/abs/2610.32114v1)** _(score 8.3 · 2026-10-23 · Soroush Ebadian, Parand A. Alamdari, Joe Benton…)_
  One approach to accelerating progress on AI alignment is to automate parts of alignment research itself. Doing so requires systems that can perform reliably on hard-to-supervise research tasks, including identifying flaws in research proposals and evaluating whether a proposed ex
- **[Benchmarks Are Surprisingly Compaction-Friendly](https://arxiv.org/abs/2610.31778v1)** _(score 8.3 · 2026-10-22 · Jeanne Salle, Hardik Bhatnagar, Matthias Bethge…)_
  Long horizon agentic tasks are now pushing LLM agents past their context window. To continue the task, the agent scaffold has to free up the context window, a process known as context compaction. Compaction is generally lossy by design: agents can silently lose task constraints,

### Huggingface (2)

- **[abdullahashraf122/algomyth-code-generation-benchmark](https://huggingface.co/datasets/abdullahashraf122/algomyth-code-generation-benchmark)** _(score 7.972 · 2026-10-18 · 50 downloads)_
  Hugging Face dataset — 50 downloads, 0 likes. Tags: task_categories:text-generation, annotations_creators:machine-generated, multilinguality:monolingual, source_datasets:original, language:en
- **[medreason/llm-medical-reasoning-steps-benchmark](https://huggingface.co/datasets/medreason/llm-medical-reasoning-steps-benchmark)** _(score 5.517 · 2026-05-04 · 68 downloads)_
  Hugging Face dataset — 68 downloads, 1 likes. Tags: task_categories:question-answering, task_categories:text-generation, language:en, license:cc-by-nc-4.0, size_categories:1K<n<10K

---

_Produced by [OpenBench Radar](https://github.com/) — automated benchmark retrieval, research & reporting._