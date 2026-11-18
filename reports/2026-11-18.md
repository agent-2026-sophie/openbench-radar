# OpenBench Radar — AI/LLM Benchmark Digest

> Generated **2026-11-18 16:59 UTC** · 64 items · topics: LLM evaluation benchmark, large language model leaderboard, code generation benchmark, reasoning benchmark LLM, agent benchmark evaluation · analysis: extractive fallback

## Executive Summary

Retrieved **64** relevant items across topics (LLM evaluation benchmark, large language model leaderboard, code generation benchmark, reasoning benchmark LLM, agent benchmark evaluation): 62 from arxiv, 2 from huggingface. The most relevant findings, ranked by a keyword/recency/popularity heuristic, are listed below. (Set OPENAI_API_KEY to enable an LLM-written analytical summary.)

## Key Highlights

- [arxiv] SOTA or Luck? The Winner's Curse in LLM Leaderboards — Public LLM leaderboards guide model evaluation and adoption, yet the reported performance of top-ranked models can be systematically oversta
- [arxiv] AfriNORM: An Evaluation Benchmark for Normative Reasoning of LLMs Across African Cultures — Large language models (LLMs) are increasingly deployed across various sectors. However, current evaluation benchmarks are insufficient to as
- [huggingface] goodgentleman918/ai-data-quality-llm-evaluation-benchmark — Hugging Face dataset — 107 downloads, 1 likes. Tags: task_categories:reinforcement-learning, language:en, license:mit, size_categories:n<1K,
- [arxiv] SAGE-QA: Semantic-Aware, Grounded Evaluation for Closed-Context Question Answering on SQuAD 2.0 — Closed-context question answering (QA) requires a system to generate an answer strictly supported by a supplied passage, or to abstain when
- [arxiv] FVScore: Specification-Driven Neuro-Symbolic Video Evaluation — We introduce Faithfulness Video Score (FVSCORE), a neuro-symbolic framework for specification-driven video generation evaluation. Existing e
- [arxiv] Who Pays for Byzantine Robustness? Validity, Data-Share Dictatorships, and Fairness When Only a Few Hospitals Collaborate — Clinical federated learning (FL) collaborations typically connect only three to six hospitals, yet Byzantine-robust aggregation rules are de

## Findings by Source

### Arxiv (62)

- **[SOTA or Luck? The Winner's Curse in LLM Leaderboards](https://arxiv.org/abs/2611.22227v1)** _(score 15.933 · 2026-11-17 · Sikun Xu, Raphael Thomadsen, Dennis J. Zhang…)_
  Public LLM leaderboards guide model evaluation and adoption, yet the reported performance of top-ranked models can be systematically overstated. This leaderboard winner's curse arises because ranking noisy benchmark scores rewards sampling luck alongside genuine ability. The same
- **[AfriNORM: An Evaluation Benchmark for Normative Reasoning of LLMs Across African Cultures](https://arxiv.org/abs/2611.22580v1)** _(score 15.433 · 2026-11-17 · Ahmad Samuel Gali, Tadesse Destaw Belay, Idris Abdulmumin…)_
  Large language models (LLMs) are increasingly deployed across various sectors. However, current evaluation benchmarks are insufficient to assess the applicability of these models in local African contexts, as most focus on linguistic fluency (grammar/translation) rather than cult
- **[SAGE-QA: Semantic-Aware, Grounded Evaluation for Closed-Context Question Answering on SQuAD 2.0](https://arxiv.org/abs/2611.16300v1)** _(score 13.6 · 2026-11-12 · Chandra N Sekharan, Vishakan Umapathy, Abhishek Phadke)_
  Closed-context question answering (QA) requires a system to generate an answer strictly supported by a supplied passage, or to abstain when the passage lacks adequate evidence. SQuAD 2.0 is a widely used benchmark for this setting, scored by Exact Match (EM) i.e., character-level
- **[FVScore: Specification-Driven Neuro-Symbolic Video Evaluation](https://arxiv.org/abs/2611.22673v1)** _(score 11.933 · 2026-11-17 · Do Xuan Long, Long T. Le, Yiwen Song…)_
  We introduce Faithfulness Video Score (FVSCORE), a neuro-symbolic framework for specification-driven video generation evaluation. Existing evaluators rely on holistic MLLM judgments or vision-language metrics, yet aligning their scores with human judgments and tracing them to spe
- **[Who Pays for Byzantine Robustness? Validity, Data-Share Dictatorships, and Fairness When Only a Few Hospitals Collaborate](https://arxiv.org/abs/2611.22904v1)** _(score 10.933 · 2026-11-17 · Adnan Malkani)_
  Clinical federated learning (FL) collaborations typically connect only three to six hospitals, yet Byzantine-robust aggregation rules are designed and benchmarked on synthetic partitions across dozens of equal-sized clients. We conduct an empirical audit of eight standard aggrega
- **[Do Diffusion Models Learn to Generalize Basic Visual Skills?](https://arxiv.org/abs/2611.22427v1)** _(score 10.933 · 2026-11-17 · Amish Sethi, Boya Zeng, Wenhao Chai…)_
  Diffusion models generate high-quality images, but how well they generalize is hard to measure. Current evaluations rely on human preference and prompt-following benchmarks for text-to-image models and on distribution-level metrics such as Fréchet Inception Distance (FID) and Inc
- **[ForecastGym: A Live, Controlled, and Replayable Benchmark for Forecasting Agents](https://arxiv.org/abs/2611.23045v1)** _(score 10.433 · 2026-11-17 · Yicheng Tao, Yuante Li, Zipei Fan)_
  Agents built on large language models (LLMs) increasingly forecast real-world events by searching the Web and reasoning over what they find. How well such an agent forecasts depends on both the retrieved evidence and the model, making control over that evidence essential for eval
- **[DiagTrace: An Interactive Benchmark for Clinical Decision Making](https://arxiv.org/abs/2611.22009v1)** _(score 10.433 · 2026-11-16 · Yufan Wang, Rui Yang, Yi Lin…)_
  Large language models (LLMs) have shown strong performance on medical question answering and diagnostic reasoning benchmarks. However, existing evaluations typically provide all patient information upfront and assess only the final diagnosis or rationale. This setup ignores the n
- **[AI Isn't Getting Dumber, We're Getting Pickier: Rising Standards in Human Evaluation of Large Language Models](https://arxiv.org/abs/2611.14333v1)** _(score 9.467 · 2026-11-10 · Zihan Chen, Lei Nico Zheng, Di Zhu)_
  Users often complain that AI assistants such as ChatGPT are getting worse. Some versions do change, but human evaluation leaves a second possibility untested: the people judging may change. We separate the two on Chatbot Arena, a public platform where people compare answers from
- **[Right Diagnosis, Unsafe Route: Auditing Clinical AI Decision Trajectories and Corrective Oversight for Validity and Potential Harm](https://arxiv.org/abs/2611.22612v1)** _(score 8.933 · 2026-11-17 · Guanqiao Chen, Wei Jiang, Shu Zhang…)_
  A clinical AI system can reach a correct final diagnosis through intermediate decisions that could have harmed the patient, and can repair an error while introducing new risks. Most evaluations score final diagnoses; even stepwise benchmarks, which release a case's evidence over
- **[RAG in a Trenchcoat: When Minimal Memory Is Enough for Agentic Systems, and When It Isn't](https://arxiv.org/abs/2611.22179v1)** _(score 8.933 · 2026-11-17 · Jingyu Liu, Zongze Li, Zach Xu…)_
  Agentic memory research has accumulated extraction, supersession, reflection, and graph synthesis on top of retrieval-augmented generation. However, we found that almost none of those primitives earn their cost in our tested memory benchmarks: we show this with BRIDGE, a delibera
- **[Can Coding Agents Write and Transpile Unit Tests](https://arxiv.org/abs/2611.21797v1)** _(score 8.933 · 2026-11-16 · Gil Pasternak, AJ Langley, Tom Yotam…)_
  Coding assistants built on Large Language Models (LLMs) have become a staple of modern software development, increasingly trusted to execute workflows and modernize code end-to-end. Much of this trust rests on passing tests, which are often written by the coding agents themselves

### Huggingface (2)

- **[goodgentleman918/ai-data-quality-llm-evaluation-benchmark](https://huggingface.co/datasets/goodgentleman918/ai-data-quality-llm-evaluation-benchmark)** _(score 14.987 · 2026-11-10 · 107 downloads)_
  Hugging Face dataset — 107 downloads, 1 likes. Tags: task_categories:reinforcement-learning, language:en, license:mit, size_categories:n<1K, modality:text
- **[abdullahashraf122/algomyth-code-generation-benchmark](https://huggingface.co/datasets/abdullahashraf122/algomyth-code-generation-benchmark)** _(score 6.436 · 2026-10-18 · 27 downloads)_
  Hugging Face dataset — 27 downloads, 0 likes. Tags: task_categories:text-generation, annotations_creators:machine-generated, multilinguality:monolingual, source_datasets:original, language:en

---

_Produced by [OpenBench Radar](https://github.com/) — automated benchmark retrieval, research & reporting._