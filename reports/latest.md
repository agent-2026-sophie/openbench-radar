# OpenBench Radar — AI/LLM Benchmark Digest

> Generated **2026-11-08 14:49 UTC** · 62 items · topics: LLM evaluation benchmark, large language model leaderboard, code generation benchmark, reasoning benchmark LLM, agent benchmark evaluation · analysis: extractive fallback

## Executive Summary

Retrieved **62** relevant items across topics (LLM evaluation benchmark, large language model leaderboard, code generation benchmark, reasoning benchmark LLM, agent benchmark evaluation): 61 from arxiv, 1 from huggingface. The most relevant findings, ranked by a keyword/recency/popularity heuristic, are listed below. (Set OPENAI_API_KEY to enable an LLM-written analytical summary.)

## Key Highlights

- [arxiv] OpenTWBench (Open Taiwan Benchmark): Taiwan-Domain Knowledge Evaluation for Large Language Models, and How the Measurement Apparatus Shapes the Score — We present OpenTWBench, an open evaluation suite for Taiwan-domain knowledge in large language models, built around two benchmarks. tw-exam-
- [arxiv] Benchmarks as Software: Terminal-Bench and the Case for Continuous Benchmarks — Coding agents are among the most economically consequential deployments of LLMs to date, making reliable evaluation increasingly important.
- [arxiv] Benchmarking Large Language Models on Heterogeneous Cognitive and Biomedical Knowledge Graphs: The Role of Graph Grounding in Multi-Hop Reasoning and Hallucination Mitigation — Large language models (LLMs) are increasingly used in biomedical and cognitive neuroscience, but their ability to reason reliably over heter
- [arxiv] Multimodal-SEA: Benchmarking AI Agent Security under Multimodal Social Engineering Attacks — Personal AI agents face social engineering attacks supported by forged multimodal content, but existing evaluations mainly focus on text-bas
- [arxiv] Compression Through a Context Lens: Evaluating Adaptation, Quantization, and Distillation in Arabic Legal LLMs — Model compression can facilitate the deployment of large language models in resource-constrained legal settings, but its effects on domain-s
- [arxiv] Circe: Training-Free LLM Self-Evaluation via Component Interaction Consistency — As large language models (LLMs) are increasingly deployed in real-world applications, evaluating the correctness of their responses is cruci

## Findings by Source

### Arxiv (61)

- **[OpenTWBench (Open Taiwan Benchmark): Taiwan-Domain Knowledge Evaluation for Large Language Models, and How the Measurement Apparatus Shapes the Score](https://arxiv.org/abs/2610.19848v1)** _(score 11.833 · 2026-10-14 · Liang-Hsun Huang, Min-Yi Chen, Chao-Chun Chuang…)_
  We present OpenTWBench, an open evaluation suite for Taiwan-domain knowledge in large language models, built around two benchmarks. tw-exam-bench contains 255,854 four-option questions across 148 academic subjects, from fifteen years of Taiwan's national examinations published as
- **[Benchmarks as Software: Terminal-Bench and the Case for Continuous Benchmarks](https://arxiv.org/abs/2611.08417v1)** _(score 10.367 · 2026-11-05 · E. Kelly Buchanan, Crystal Zhou, Scott W. Linderman…)_
  Coding agents are among the most economically consequential deployments of LLMs to date, making reliable evaluation increasingly important. Yet even benchmarks that are carefully validated at release can become stale. As models improve, they can discover valid solutions that exis
- **[Benchmarking Large Language Models on Heterogeneous Cognitive and Biomedical Knowledge Graphs: The Role of Graph Grounding in Multi-Hop Reasoning and Hallucination Mitigation](https://arxiv.org/abs/2611.08315v1)** _(score 10.367 · 2026-11-05 · Ali Sarabadani, Kheirolah Rahsepar Fard, Tahereh Jeirani)_
  Large language models (LLMs) are increasingly used in biomedical and cognitive neuroscience, but their ability to reason reliably over heterogeneous knowledge graphs (KGs) remains unclear. We benchmark five LLMs (GPT-5.1, Gemini 2.0 Pro, Llama 3, Qwen, and BioGPT) across five KGs
- **[Multimodal-SEA: Benchmarking AI Agent Security under Multimodal Social Engineering Attacks](https://arxiv.org/abs/2611.08281v1)** _(score 10.367 · 2026-11-05 · Zhitao He, Chi Him Zhang, Chengru Han…)_
  Personal AI agents face social engineering attacks supported by forged multimodal content, but existing evaluations mainly focus on text-based dialogue, leaving their intrinsic security under such attacks insufficiently studied. We introduce Multimodal-SEA, an interactive benchma
- **[Compression Through a Context Lens: Evaluating Adaptation, Quantization, and Distillation in Arabic Legal LLMs](https://arxiv.org/abs/2611.07988v1)** _(score 10.3 · 2026-11-05 · Md. Rafiul Biswas, George Mikros, Wajdi Zaghouani)_
  Model compression can facilitate the deployment of large language models in resource-constrained legal settings, but its effects on domain-specific performance may depend on the evaluation protocol. We investigate this issue using ArabLegalEval, a Saudi Arabic legal benchmark, un
- **[Circe: Training-Free LLM Self-Evaluation via Component Interaction Consistency](https://arxiv.org/abs/2611.07948v1)** _(score 9.8 · 2026-11-05 · Shuyi Miao, Zheng Li, Xu Xie…)_
  As large language models (LLMs) are increasingly deployed in real-world applications, evaluating the correctness of their responses is crucial for reliable use. However, such evaluation is challenging because reference answers are rarely available in practice. Existing reference-
- **[Beyond Scalar Leaderboards: Adaptive Sampling for Pareto Frontier Identification in Multi-Objective LLM Arenas](https://arxiv.org/abs/2610.27447v1)** _(score 9.233 · 2026-10-20 · Liang Twist Shan, Jiahao Ai, Zhimei Ren)_
  The evaluation of large language models (LLMs) is inherently multi-objective, as different models may offer different tradeoffs across performance dimensions such as math, code, and writing. Because such evaluations are often based on costly and time-consuming human feedback, it
- **[Beyond Leaderboards: A Method for Application-Specific Capability Profiling of Large Language Models](https://arxiv.org/abs/2610.25659v1)** _(score 9.167 · 2026-10-19 · Oleg Grynets, Vasyl Lyashkevych, Andrii Salyk…)_
  Public leaderboards rank large language models (LLMs) in general, but an engineer has to choose a model for a specific application, architecture and cost. This paper presents a method for application-specific capability profiling of LLMs and its realization as a containerized tes
- **[Beneath the Surface: What We Overlook When We Talk About Agent Evolution](https://arxiv.org/abs/2611.07624v1)** _(score 8.8 · 2026-11-05 · Xiaobo Wang, Zimu Wang, Siyu Ye…)_
  Agent harness evolution enables recursive self-improvement (RSI) without updating model weights. We examine whether higher benchmark scores yield reliable, efficient, and transferable improvement. We evaluate four methods across harnesses, general and coding tasks. Repeated evalu
- **[ACE-Compression: An Ability-Centric Evaluation of Compressed Large Language Models](https://arxiv.org/abs/2610.27913v1)** _(score 8.733 · 2026-10-20 · Jiahui Ning, Liang Chen, Yuchen Liang…)_
  Model compression makes large language models deployable, but today's evaluation tells an incomplete story. Standard practice measures retained task performance and stops there. This misses a critical fact: compression perturbs the distributed knowledge embedded across billions o
- **[XStack: A Benchmark for ML Repo Migration](https://arxiv.org/abs/2611.08472v1)** _(score 8.367 · 2026-11-05 · Linrong Cai, Taiming Lu, Haozhe Chen…)_
  ML code should run where researchers choose, not where it was first written. Today, machine learning code mainly lives in two ecosystems, PyTorch on NVIDIA GPUs and JAX on Google TPUs. Migrating repositories between them means building and testing across frameworks and hardware.
- **[TCSExam: Evaluating Frontier LLMs on the Full Range of TCS Research](https://arxiv.org/abs/2611.07962v1)** _(score 8.3 · 2026-11-05 · Yifan Luo, Zhengying Liu, Yang Yuan…)_
  Can large language models (LLMs) advance theoretical computer science and resolve its long-standing open conjectures? To study progress toward this goal, we introduce TCSExam, a unified framework and benchmark covering the full range of TCS research. It evaluates theorem proving,

### Huggingface (1)

- **[abdullahashraf122/algomyth-code-generation-benchmark](https://huggingface.co/datasets/abdullahashraf122/algomyth-code-generation-benchmark)** _(score 7.106 · 2026-10-18 · 58 downloads)_
  Hugging Face dataset — 58 downloads, 0 likes. Tags: task_categories:text-generation, annotations_creators:machine-generated, multilinguality:monolingual, source_datasets:original, language:en

---

_Produced by [OpenBench Radar](https://github.com/) — automated benchmark retrieval, research & reporting._