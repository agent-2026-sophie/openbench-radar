# OpenBench Radar — AI/LLM Benchmark Digest

> Generated **2026-10-21 13:30 UTC** · 62 items · topics: LLM evaluation benchmark, large language model leaderboard, code generation benchmark, reasoning benchmark LLM, agent benchmark evaluation · analysis: extractive fallback

## Executive Summary

Retrieved **62** relevant items across topics (LLM evaluation benchmark, large language model leaderboard, code generation benchmark, reasoning benchmark LLM, agent benchmark evaluation): 60 from arxiv, 2 from huggingface. The most relevant findings, ranked by a keyword/recency/popularity heuristic, are listed below. (Set OPENAI_API_KEY to enable an LLM-written analytical summary.)

## Key Highlights

- [arxiv] DeclineCraft: A RAG Abstention Benchmark for Jointly Measuring Combined Retrieval and Parametric Knowledge — Reliable retrieval-augmented generation (RAG) requires recognizing when neither retrieved documents nor parametric knowledge supports an ans
- [arxiv] SciDiagBench: A Type-Specific Benchmark for Human-Aligned Evaluation of Scientific Diagrams — Recent agents have demonstrated strong capabilities in generating images from textual prompts, motivating their utilization for scientific d
- [arxiv] SHAM-Bench: A Span-level Hallucination Benchmark Across Multiple Tasks — Span-level hallucination detection pinpoints unsupported content in LLM outputs, enabling actionable feedback and targeted mitigation. Exist
- [arxiv] OpenTWBench (Open Taiwan Benchmark): Taiwan-Domain Knowledge Evaluation for Large Language Models, and How the Measurement Apparatus Shapes the Score — We present OpenTWBench, an open evaluation suite for Taiwan-domain knowledge in large language models, built around two benchmarks. tw-exam-
- [arxiv] GNN-CB: A Graph Neural Network Competition Benchmark for Human and LLM Evaluation — Large language models (LLMs) have demonstrated strong performance on coding and reasoning benchmarks; however, their ability to solve graph-
- [arxiv] ExeBench-FHD: Addressing Fidelity Issues in Decompiler Evaluation — ExeBench is one of the most widely used benchmarks for evaluating LLM-based decompilers. We analyze ExeBench and identify nine issues that a

## Findings by Source

### Arxiv (60)

- **[DeclineCraft: A RAG Abstention Benchmark for Jointly Measuring Combined Retrieval and Parametric Knowledge](https://arxiv.org/abs/2610.28340v1)** _(score 15.5 · 2026-10-20 · Atharva Thakur, Abulhair Saparov, Bruno Ribeiro)_
  Reliable retrieval-augmented generation (RAG) requires recognizing when neither retrieved documents nor parametric knowledge supports an answer. We introduce DeclineCraft, a dynamic abstention benchmark whose unanswerable questions target Minecraft feature additions after a corpu
- **[SciDiagBench: A Type-Specific Benchmark for Human-Aligned Evaluation of Scientific Diagrams](https://arxiv.org/abs/2610.27841v1)** _(score 15.433 · 2026-10-20 · Hao Wang, Zixuan Li, Long Bai…)_
  Recent agents have demonstrated strong capabilities in generating images from textual prompts, motivating their utilization for scientific diagram generation. Scientific diagrams naturally span diverse types, each characterized by distinct visual structures and content organizati
- **[SHAM-Bench: A Span-level Hallucination Benchmark Across Multiple Tasks](https://arxiv.org/abs/2610.27370v1)** _(score 14.433 · 2026-10-19 · Sicong Huang, Ian Lane)_
  Span-level hallucination detection pinpoints unsupported content in LLM outputs, enabling actionable feedback and targeted mitigation. Existing evaluations for span-level hallucination detection methods are fragmented across tasks, annotation formats, and metrics, and most span-l
- **[OpenTWBench (Open Taiwan Benchmark): Taiwan-Domain Knowledge Evaluation for Large Language Models, and How the Measurement Apparatus Shapes the Score](https://arxiv.org/abs/2610.19848v1)** _(score 13.033 · 2026-10-14 · Liang-Hsun Huang, Min-Yi Chen, Chao-Chun Chuang…)_
  We present OpenTWBench, an open evaluation suite for Taiwan-domain knowledge in large language models, built around two benchmarks. tw-exam-bench contains 255,854 four-option questions across 148 academic subjects, from fifteen years of Taiwan's national examinations published as
- **[GNN-CB: A Graph Neural Network Competition Benchmark for Human and LLM Evaluation](https://arxiv.org/abs/2610.05387v1)** _(score 12.433 · 2026-10-04 · Murad Hossen, Tasneem Selim, Gurur Gamgam…)_
  Large language models (LLMs) have demonstrated strong performance on coding and reasoning benchmarks; however, their ability to solve graph-structured machine learning problems remains largely unexplored. In particular, no benchmark currently evaluates whether LLMs can autonomous
- **[ExeBench-FHD: Addressing Fidelity Issues in Decompiler Evaluation](https://arxiv.org/abs/2610.28212v1)** _(score 12.0 · 2026-10-20 · Akarsh Ashok, Dinil Mon Divakaran, Vivek Balachandran)_
  ExeBench is one of the most widely used benchmarks for evaluating LLM-based decompilers. We analyze ExeBench and identify nine issues that affect how faithfully a test measures a decompiler. Three of them prevent LLM decompilers from recovering C code from ExeBench's function. Th
- **[Re-executing Coding-Agent Evaluations: Unchanged Decisions and Unresolved Policy Risk](https://arxiv.org/abs/2610.14460v1)** _(score 11.267 · 2026-10-10 · Tianyu Ding, Yaocheng Tong, Muzhi Yang…)_
  Executable tests grade large language model (LLM) coding-agent patches for leaderboards, rewards and self-improvement. Two preregistered re-execution studies returned negative results. SWE-bench Pro v1's offline option rejected none of 59 accepted Go patches whose grading configu
- **[CAPSafe: A Benchmark for Contextual Action and Plan Safety Reasoning in Embodied Agents](https://arxiv.org/abs/2610.28381v1)** _(score 10.5 · 2026-10-20 · Youmna Farag, Svetlana Stoyanchev, Simon Keizer…)_
  Reasoning about safety is essential for embodied agents powered by large language models (LLMs). We introduce the Contextual Action and Plan Safety benchmark (CAPSafe), designed to evaluate safety reasoning at two levels: (1) an action-level dataset that tests whether a single ac
- **[Beyond Scalar Leaderboards: Adaptive Sampling for Pareto Frontier Identification in Multi-Objective LLM Arenas](https://arxiv.org/abs/2610.27447v1)** _(score 10.433 · 2026-10-20 · Liang Twist Shan, Jiahao Ai, Zhimei Ren)_
  The evaluation of large language models (LLMs) is inherently multi-objective, as different models may offer different tradeoffs across performance dimensions such as math, code, and writing. Because such evaluations are often based on costly and time-consuming human feedback, it
- **[RAG-NIMBF: A Non-Invasive, Modular Benchmarking Framework for Automated RAG Configuration Analysis](https://arxiv.org/abs/2610.27816v1)** _(score 10.433 · 2026-10-20 · Niclas Hart, Nicolas Weeger)_
  Retrieval-Augmented Generation (RAG) has become the dominant paradigm for grounding the outputs of large language models (LLM) in external knowledge. However, practitioners are faced with a vast configuration space comprising chunking, embedding, retrieval, reranking, prompting a
- **[Act on Your Behalf, Beyond Your Authorization: Benchmarking LLM Agent Authorization Alignment](https://arxiv.org/abs/2610.27548v1)** _(score 10.433 · 2026-10-20 · Zhiping Zhang, Franklin Mingzhe Li, Zihao Huang…)_
  When an LLM agent acts on behalf of a user, it is expected to act within the authorization scope the user grants. Existing agent evaluations largely measure task completion or harmful consequences and can therefore overlook actions that violate this delegation without producing c
- **[RealControlBench: A Benchmark for Interpretability-Informed Fine-Grained Control of LLMs and Agents](https://arxiv.org/abs/2610.27295v1)** _(score 10.433 · 2026-10-19 · Xinying Cai, Bin Hu, Mingyu Jin…)_
  Existing steering benchmarks are built around simplified, isolated generation tasks and evaluate a single behavioral attribute under controlled settings that do not reflect the diversity and complexity of practical deployment. As a result, performance on these benchmarks provides

### Huggingface (2)

- **[abdullahashraf122/algomyth-code-generation-benchmark](https://huggingface.co/datasets/abdullahashraf122/algomyth-code-generation-benchmark)** _(score 8.371 · 2026-10-18 · 42 downloads)_
  Hugging Face dataset — 42 downloads, 0 likes. Tags: task_categories:text-generation, annotations_creators:machine-generated, multilinguality:monolingual, source_datasets:original, language:en
- **[medreason/llm-medical-reasoning-steps-benchmark](https://huggingface.co/datasets/medreason/llm-medical-reasoning-steps-benchmark)** _(score 5.517 · 2026-05-04 · 68 downloads)_
  Hugging Face dataset — 68 downloads, 1 likes. Tags: task_categories:question-answering, task_categories:text-generation, language:en, license:cc-by-nc-4.0, size_categories:1K<n<10K

---

_Produced by [OpenBench Radar](https://github.com/) — automated benchmark retrieval, research & reporting._