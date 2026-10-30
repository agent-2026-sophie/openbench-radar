# OpenBench Radar — AI/LLM Benchmark Digest

> Generated **2026-10-30 14:52 UTC** · 63 items · topics: LLM evaluation benchmark, large language model leaderboard, code generation benchmark, reasoning benchmark LLM, agent benchmark evaluation · analysis: extractive fallback

## Executive Summary

Retrieved **63** relevant items across topics (LLM evaluation benchmark, large language model leaderboard, code generation benchmark, reasoning benchmark LLM, agent benchmark evaluation): 61 from arxiv, 2 from huggingface. The most relevant findings, ranked by a keyword/recency/popularity heuristic, are listed below. (Set OPENAI_API_KEY to enable an LLM-written analytical summary.)

## Key Highlights

- [arxiv] It Takes Two to Probe, Thousands to Retrieve: Putting Vision--Language Probes to the Retrieval Test — Vision--language models (VLMs) are tested for fine-grained understanding with image--text matching probes, a model must prefer the correct i
- [arxiv] OpenTWBench (Open Taiwan Benchmark): Taiwan-Domain Knowledge Evaluation for Large Language Models, and How the Measurement Apparatus Shapes the Score — We present OpenTWBench, an open evaluation suite for Taiwan-domain knowledge in large language models, built around two benchmarks. tw-exam-
- [arxiv] Ramanujan Challenge Results: AI-Assisted Evaluation Pipeline for Multi-Format Proofs — As AI's mathematical capabilities rapidly improve, meaningful benchmarks are shifting from university-level problems and math olympiads to r
- [arxiv] Beyond Passing Tests: A Systematic Review and Controlled Re-evaluation of Techniques for Improving the Quality of LLM-Generated Code — Large language models pass most functional-correctness benchmarks, but passing tests says little about whether their code is readable, effic
- [arxiv] Elucidating the Design Space of LM Data Attribution — Data attribution methods for Language Models (LMs) are typically evaluated using downstream tasks like fact retrieval. However, existing eva
- [arxiv] Re-executing Coding-Agent Evaluations: Unchanged Decisions and Unresolved Policy Risk — Executable tests grade large language model (LLM) coding-agent patches for leaderboards, rewards and self-improvement. Two preregistered re-

## Findings by Source

### Arxiv (61)

- **[It Takes Two to Probe, Thousands to Retrieve: Putting Vision--Language Probes to the Retrieval Test](https://arxiv.org/abs/2610.40124v1)** _(score 12.433 · 2026-10-29 · Ivana Beňová, Michal Gregor, Marián Šimko)_
  Vision--language models (VLMs) are tested for fine-grained understanding with image--text matching probes, a model must prefer the correct image or caption over handcrafted negative. In retrieval, the correct item must beat thousands of alternatives. We measure how these two eval
- **[OpenTWBench (Open Taiwan Benchmark): Taiwan-Domain Knowledge Evaluation for Large Language Models, and How the Measurement Apparatus Shapes the Score](https://arxiv.org/abs/2610.19848v1)** _(score 12.433 · 2026-10-14 · Liang-Hsun Huang, Min-Yi Chen, Chao-Chun Chuang…)_
  We present OpenTWBench, an open evaluation suite for Taiwan-domain knowledge in large language models, built around two benchmarks. tw-exam-bench contains 255,854 four-option questions across 148 academic subjects, from fifteen years of Taiwan's national examinations published as
- **[Ramanujan Challenge Results: AI-Assisted Evaluation Pipeline for Multi-Format Proofs](https://arxiv.org/abs/2610.40551v1)** _(score 12.0 · 2026-10-29 · Alan Sorani, Ashvni Narayanan, Michael Shalyt…)_
  As AI's mathematical capabilities rapidly improve, meaningful benchmarks are shifting from university-level problems and math olympiads to research-level mathematics. The Ramanujan Challenge is a benchmark comprised of research-level problems in number theory, including unpublish
- **[Beyond Passing Tests: A Systematic Review and Controlled Re-evaluation of Techniques for Improving the Quality of LLM-Generated Code](https://arxiv.org/abs/2610.38977v1)** _(score 11.933 · 2026-10-28 · Prashank Kadam)_
  Large language models pass most functional-correctness benchmarks, but passing tests says little about whether their code is readable, efficient or secure. Many techniques claim to improve these qualities, yet their evidence is scattered, usually covers one quality dimension and
- **[Elucidating the Design Space of LM Data Attribution](https://arxiv.org/abs/2610.40655v1)** _(score 11.0 · 2026-10-29 · Steven Yu, Sheng-Yu Wang, Kimia Hamidieh…)_
  Data attribution methods for Language Models (LMs) are typically evaluated using downstream tasks like fact retrieval. However, existing evaluations vary multiple dataset properties simultaneously, making it impossible to isolate exactly why an attribution algorithm fails. To dia
- **[Re-executing Coding-Agent Evaluations: Unchanged Decisions and Unresolved Policy Risk](https://arxiv.org/abs/2610.14460v1)** _(score 10.667 · 2026-10-10 · Tianyu Ding, Yaocheng Tong, Muzhi Yang…)_
  Executable tests grade large language model (LLM) coding-agent patches for leaderboards, rewards and self-improvement. Two preregistered re-execution studies returned negative results. SWE-bench Pro v1's offline option rejected none of 59 accepted Go patches whose grading configu
- **[Prefix Executability: Evaluating Tool-Using Agents Beyond Final Success](https://arxiv.org/abs/2610.40444v1)** _(score 10.5 · 2026-10-29 · Amir H. Rezaeian, Weiyi Sun, Yassine Benajiba…)_
  Tool-use benchmarks often score agents by final task success, but terminal outcomes can obscure whether the intermediate tool-call trajectory was executable. We propose prefix executability as a trajectory-level evaluation protocol for tool-using agents. The protocol measures whe
- **[Well-Specified and Well-Tested? Assessing SWE-bench-Style Datasets with a Self-Evolving Agent](https://arxiv.org/abs/2610.39417v1)** _(score 10.433 · 2026-10-29 · Zhonghao Jiang, Xuyang Zheng, Yanfu Yan…)_
  Large language models (LLMs) have shown strong performance on software engineering (SE) tasks, driving the need for high-quality datasets for reliable training and evaluation. SWE-bench-style datasets (SWE datasets) are widely used to evaluate LLM-based coding agents on real-worl
- **[SocialArena: Evaluating Social Intelligence in Large Language Models](https://arxiv.org/abs/2610.39247v1)** _(score 10.433 · 2026-10-29 · Zongqi Wang, Rui Wang, Yuchuan Wu…)_
  We introduce SocialArena, a benchmark for systematically defining and evaluating the social intelligence of large language models (LLMs). Although LLMs are increasingly deployed in socially interactive applications such as mental health counseling, companionship chatbots, and edu
- **[DynaRev: Benchmarking Web Agents under Dynamic Goal Revision](https://arxiv.org/abs/2610.40133v1)** _(score 10.433 · 2026-10-29 · Shiqi Zhang, Guochen Zhou, Zesheng Wei…)_
  Web agents are typically evaluated with goals fully specified before execution and fixed thereafter, whereas real users often revise their requirements during interaction. To study such interactions, we introduce DynaRev, a benchmark of 181 tasks to evaluate web agents under dyna
- **[Bank-World: A Benchmark for Evaluating Agents on Banking Workflows](https://arxiv.org/abs/2610.39733v1)** _(score 9.933 · 2026-10-29 · Daniel Rupawalla)_
  Bank-World is a benchmark of 50 banking tasks across two simulated institutions. Completing banking work requires more than producing the right calculation: agents must reconcile records, obtain permission, execute transactions, and keep instructions and status reports consistent
- **[Beyond Scalar Leaderboards: Adaptive Sampling for Pareto Frontier Identification in Multi-Objective LLM Arenas](https://arxiv.org/abs/2610.27447v1)** _(score 9.833 · 2026-10-20 · Liang Twist Shan, Jiahao Ai, Zhimei Ren)_
  The evaluation of large language models (LLMs) is inherently multi-objective, as different models may offer different tradeoffs across performance dimensions such as math, code, and writing. Because such evaluations are often based on costly and time-consuming human feedback, it

### Huggingface (2)

- **[abdullahashraf122/algomyth-code-generation-benchmark](https://huggingface.co/datasets/abdullahashraf122/algomyth-code-generation-benchmark)** _(score 7.705 · 2026-10-18 · 54 downloads)_
  Hugging Face dataset — 54 downloads, 0 likes. Tags: task_categories:text-generation, annotations_creators:machine-generated, multilinguality:monolingual, source_datasets:original, language:en
- **[medreason/llm-medical-reasoning-steps-benchmark](https://huggingface.co/datasets/medreason/llm-medical-reasoning-steps-benchmark)** _(score 5.517 · 2026-05-04 · 71 downloads)_
  Hugging Face dataset — 71 downloads, 1 likes. Tags: task_categories:question-answering, task_categories:text-generation, language:en, license:cc-by-nc-4.0, size_categories:1K<n<10K

---

_Produced by [OpenBench Radar](https://github.com/) — automated benchmark retrieval, research & reporting._