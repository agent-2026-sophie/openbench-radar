# OpenBench Radar — AI/LLM Benchmark Digest

> Generated **2026-11-26 18:10 UTC** · 60 items · topics: LLM evaluation benchmark, large language model leaderboard, code generation benchmark, reasoning benchmark LLM, agent benchmark evaluation · analysis: extractive fallback

## Executive Summary

Retrieved **60** relevant items across topics (LLM evaluation benchmark, large language model leaderboard, code generation benchmark, reasoning benchmark LLM, agent benchmark evaluation): 58 from arxiv, 2 from huggingface. The most relevant findings, ranked by a keyword/recency/popularity heuristic, are listed below. (Set OPENAI_API_KEY to enable an LLM-written analytical summary.)

## Key Highlights

- [arxiv] SOTA or Luck? The Winner's Curse in LLM Leaderboards — Public LLM leaderboards guide model evaluation and adoption, yet the reported performance of top-ranked models can be systematically oversta
- [huggingface] goodgentleman918/ai-data-quality-llm-evaluation-benchmark — Hugging Face dataset — 117 downloads, 1 likes. Tags: task_categories:reinforcement-learning, language:en, license:mit, size_categories:n<1K,
- [arxiv] SAGE-QA: Semantic-Aware, Grounded Evaluation for Closed-Context Question Answering on SQuAD 2.0 — Closed-context question answering (QA) requires a system to generate an answer strictly supported by a supplied passage, or to abstain when
- [arxiv] JHealthBench-L: Clinician-Reviewed Localization of HealthBench for Rubric-Based Medical LLM Evaluation in Japan — Rubric-based benchmarks such as HealthBench evaluate large language models (LLMs) on open-ended health consultations using case-specific phy
- [arxiv] Schedule, Rank, Profile: Continuous Evaluation of LLM Agents in Games — Games are a robust test for large language model agents: they require sequential decisions, adversarial or cooperative interaction, state tr
- [arxiv] DRBench Pro: A Knowledge-Centric Benchmark for Professional Deep Research Agents — Deep research agents gather information from multiple sources and synthesize it into reports on complex, open-ended questions. Existing benc

## Findings by Source

### Arxiv (58)

- **[SOTA or Luck? The Winner's Curse in LLM Leaderboards](https://arxiv.org/abs/2611.22227v1)** _(score 15.4 · 2026-11-17 · Sikun Xu, Raphael Thomadsen, Dennis J. Zhang…)_
  Public LLM leaderboards guide model evaluation and adoption, yet the reported performance of top-ranked models can be systematically overstated. This leaderboard winner's curse arises because ranking noisy benchmark scores rewards sampling luck alongside genuine ability. The same
- **[SAGE-QA: Semantic-Aware, Grounded Evaluation for Closed-Context Question Answering on SQuAD 2.0](https://arxiv.org/abs/2611.16300v1)** _(score 13.067 · 2026-11-12 · Chandra N Sekharan, Vishakan Umapathy, Abhishek Phadke)_
  Closed-context question answering (QA) requires a system to generate an answer strictly supported by a supplied passage, or to abstain when the passage lacks adequate evidence. SQuAD 2.0 is a widely used benchmark for this setting, scored by Exact Match (EM) i.e., character-level
- **[JHealthBench-L: Clinician-Reviewed Localization of HealthBench for Rubric-Based Medical LLM Evaluation in Japan](https://arxiv.org/abs/2611.34024v1)** _(score 11.933 · 2026-11-25 · Shohei Hisada, Keisuke Orimo, Kenji Igarashi…)_
  Rubric-based benchmarks such as HealthBench evaluate large language models (LLMs) on open-ended health consultations using case-specific physician criteria, many of which presuppose the healthcare institutions, medications, and care pathways of their source region. Under machine
- **[Schedule, Rank, Profile: Continuous Evaluation of LLM Agents in Games](https://arxiv.org/abs/2611.28368v1)** _(score 11.667 · 2026-11-20 · Martyna Plomecka, Yao Yan, DJ Sterling…)_
  Games are a robust test for large language model agents: they require sequential decisions, adversarial or cooperative interaction, state tracking, reasoning under uncertainty, and long-horizon planning. However, a one-time game benchmark can go stale as models, prompts, environm
- **[DRBench Pro: A Knowledge-Centric Benchmark for Professional Deep Research Agents](https://arxiv.org/abs/2611.34852v1)** _(score 10.5 · 2026-11-25 · Han Huang, Yuchen Yan, Xingyu Wu…)_
  Deep research agents gather information from multiple sources and synthesize it into reports on complex, open-ended questions. Existing benchmarks assess report quality along several dimensions, but lack a dedicated knowledge-centric evaluation of which research directions a repo
- **[$μ$-Bench: Benchmarking Multi-User Task Completion in Shared Interaction Voice Agents](https://arxiv.org/abs/2611.34920v1)** _(score 10.5 · 2026-11-25 · Qihao Lin, Guanxu Chen, Shuhang Zheng…)_
  Voice agents in shared spaces must satisfy interdependent multi-user requests while upholding per-user authority, privacy, and task constraints. Existing evaluations offer limited coverage when participants react throughout a session. We introduce $μ$-Bench, a benchmark for joint
- **[Puzzling-Bench: Evaluating Language Models on 23,777 Human-Written Puzzles with Community-Verified Answers](https://arxiv.org/abs/2611.34331v1)** _(score 10.433 · 2026-11-25 · Abhinav Sharma, Li Li, Chien Van Nguyen…)_
  We introduce Puzzling-Bench, a benchmark of 23,777 puzzles with community-verified answers drawn from the Puzzling Stack Exchange archive (2014-2026): riddles, ciphers, logic grids, lateral-thinking problems, wordplay and recreational mathematics, a third of them with images. Eve
- **[Crucible: Evaluating LLM Agents in Executable Chemistry Research Environments](https://arxiv.org/abs/2611.34254v1)** _(score 10.433 · 2026-11-25 · Yinjun Liu, Xinye Li, Ruisen Peng…)_
  Large language models (LLMs) perform well on chemistry knowledge benchmarks, which mainly assess question answering and isolated tasks. Chemical research, however, requires using specialized tools and interpreting their outputs to obtain chemically valid results. To address this
- **[WorldPhy: Benchmarking Fine-Grained Physical Plausibility of World Models in Robotics](https://arxiv.org/abs/2611.34130v1)** _(score 10.433 · 2026-11-25 · Ziyuan Chu, Mingzhi Zheng, Kaiyue Zhang…)_
  World models are increasingly used in robotics to improve the performance of embodied models. Compared with general-purpose video generation, robotics places more stringent requirements on world models. Generated videos must satisfy fine-grained physical constraints on robot moti
- **[ChemDeduce: Benchmarking LLMs for Unknown Chemical Identification through Interactive Simulated Experiments](https://arxiv.org/abs/2611.33848v1)** _(score 10.433 · 2026-11-25 · Hengyi Cai, Yuqi Tang, Zichang Li…)_
  Large language models (LLMs) have shown strong performance in chemical knowledge and reasoning, yet it remains unclear whether they can solve problems whose answers must be discovered through experimentation. We investigate this question through Unknown Chemical Identification, w
- **[Shape-Aware Three-Way Merge for RDF Knowledge Graphs: The schema defines the conflict: an implementation and evaluation](https://arxiv.org/abs/2611.34870v1)** _(score 10.0 · 2026-11-25 · Steve Brown)_
  Merging RDF serializations creates ordering conflicts and misses semantic ones. We describe and evaluate a three-way merge in which the schema defines a conflict: set algebra combines canonical triples, and a slot is contended only where a SHACL shape bounds its cardinality and b
- **[EvoLink-Bench: A Benchmark for Evaluating Self-Evolving Agents in Long-Horizon Interdependent Task Streams](https://arxiv.org/abs/2611.34400v1)** _(score 9.933 · 2026-11-25 · Wei Chen, Xiaodong Lu, Weihao Shen…)_
  Large language model (LLM) agents are evolving from passive chatbots into autonomous systems that operate continuously in dynamic environments. Such agents need not only solve current tasks but also learn from past interactions to improve future performance. However, existing str

### Huggingface (2)

- **[goodgentleman918/ai-data-quality-llm-evaluation-benchmark](https://huggingface.co/datasets/goodgentleman918/ai-data-quality-llm-evaluation-benchmark)** _(score 14.455 · 2026-11-10 · 117 downloads)_
  Hugging Face dataset — 117 downloads, 1 likes. Tags: task_categories:reinforcement-learning, language:en, license:mit, size_categories:n<1K, modality:text
- **[abdullahashraf122/algomyth-code-generation-benchmark](https://huggingface.co/datasets/abdullahashraf122/algomyth-code-generation-benchmark)** _(score 5.903 · 2026-10-18 · 25 downloads)_
  Hugging Face dataset — 25 downloads, 0 likes. Tags: task_categories:text-generation, annotations_creators:machine-generated, multilinguality:monolingual, source_datasets:original, language:en

---

_Produced by [OpenBench Radar](https://github.com/) — automated benchmark retrieval, research & reporting._