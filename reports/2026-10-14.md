# OpenBench Radar — AI/LLM Benchmark Digest

> Generated **2026-10-14 13:22 UTC** · 59 items · topics: LLM evaluation benchmark, large language model leaderboard, code generation benchmark, reasoning benchmark LLM, agent benchmark evaluation · analysis: extractive fallback

## Executive Summary

Retrieved **59** relevant items across topics (LLM evaluation benchmark, large language model leaderboard, code generation benchmark, reasoning benchmark LLM, agent benchmark evaluation): 58 from arxiv, 1 from huggingface. The most relevant findings, ranked by a keyword/recency/popularity heuristic, are listed below. (Set OPENAI_API_KEY to enable an LLM-written analytical summary.)

## Key Highlights

- [arxiv] Are We Testing Too Much? A Survey of Benchmark Compression for Efficient Evaluation of Large Language Models — Benchmarks are essential for evaluating and improving large language models (LLMs). Yet many widely used benchmarks are redundant, making ev
- [arxiv] GNN-CB: A Graph Neural Network Competition Benchmark for Human and LLM Evaluation — Large language models (LLMs) have demonstrated strong performance on coding and reasoning benchmarks; however, their ability to solve graph-
- [arxiv] Re-executing Coding-Agent Evaluations: Unchanged Decisions and Unresolved Policy Risk — Executable tests grade large language model (LLM) coding-agent patches for leaderboards, rewards and self-improvement. Two preregistered re-
- [arxiv] Beyond Leaderboards: Tokenomics of Agentic Small Language Model Ensembles — As large language models (LLMs) move from standalone assistants into agentic workflows, evaluation must extend beyond scalar leaderboard acc
- [arxiv] SolBehave: Evaluating the Behavioural Correctness of LLM-Generated Smart Contracts — Large language models increasingly generate Solidity smart contracts that, once deployed, can never be patched, making a single latent fault
- [arxiv] Autonomous Science Bench: Evaluating AI Agents for Autonomous Scientific Discovery — AI agents for autonomous scientific discovery must decide which experiments to run under a limited budget. Most benchmarks for science agent

## Findings by Source

### Arxiv (58)

- **[Are We Testing Too Much? A Survey of Benchmark Compression for Efficient Evaluation of Large Language Models](https://arxiv.org/abs/2610.18248v1)** _(score 13.433 · 2026-10-13 · Guoming Ling, Yupei Lin, Zhongzhan Huang…)_
  Benchmarks are essential for evaluating and improving large language models (LLMs). Yet many widely used benchmarks are redundant, making evaluation unnecessarily expensive. Benchmark compression lowers this cost by estimating full-benchmark scores and rankings from a partial eva
- **[GNN-CB: A Graph Neural Network Competition Benchmark for Human and LLM Evaluation](https://arxiv.org/abs/2610.05387v1)** _(score 12.9 · 2026-10-04 · Murad Hossen, Tasneem Selim, Gurur Gamgam…)_
  Large language models (LLMs) have demonstrated strong performance on coding and reasoning benchmarks; however, their ability to solve graph-structured machine learning problems remains largely unexplored. In particular, no benchmark currently evaluates whether LLMs can autonomous
- **[Re-executing Coding-Agent Evaluations: Unchanged Decisions and Unresolved Policy Risk](https://arxiv.org/abs/2610.14460v1)** _(score 11.733 · 2026-10-10 · Tianyu Ding, Yaocheng Tong, Muzhi Yang…)_
  Executable tests grade large language model (LLM) coding-agent patches for leaderboards, rewards and self-improvement. Two preregistered re-execution studies returned negative results. SWE-bench Pro v1's offline option rejected none of 59 accepted Go patches whose grading configu
- **[Beyond Leaderboards: Tokenomics of Agentic Small Language Model Ensembles](https://arxiv.org/abs/2610.00954v1)** _(score 11.633 · 2026-10-01 · Alexei N. Skurikhin, Emily M. Taylor, Nathan A. DeBardeleben)_
  As large language models (LLMs) move from standalone assistants into agentic workflows, evaluation must extend beyond scalar leaderboard accuracy to account for operational reliability, cost, latency, and token efficiency. We use an agentic ensemble of small language models (SLMs
- **[SolBehave: Evaluating the Behavioural Correctness of LLM-Generated Smart Contracts](https://arxiv.org/abs/2610.18745v1)** _(score 10.5 · 2026-10-13 · Giovanni Pio Delvecchio, Stefano Fantazzini, Giacomo Frisoni…)_
  Large language models increasingly generate Solidity smart contracts that, once deployed, can never be patched, making a single latent fault permanent and exploitable. Yet current evaluations mostly ask only whether generated code compiles. We introduce SolBehave, a benchmark for
- **[Autonomous Science Bench: Evaluating AI Agents for Autonomous Scientific Discovery](https://arxiv.org/abs/2610.18449v1)** _(score 10.5 · 2026-10-13 · Yibo Wen, Han Liu)_
  AI agents for autonomous scientific discovery must decide which experiments to run under a limited budget. Most benchmarks for science agents provide fixed datasets, while others that support active experimentation largely rely on simulation. We introduce Autonomous Science Bench
- **[SWE-MISBEHAVIOR: Benchmarking and Mitigating Boundary Violations in Software Coding Agents](https://arxiv.org/abs/2610.18206v1)** _(score 10.433 · 2026-10-13 · Do Xuan Trong, Duc Anh Nguyen, Do Xuan Long…)_
  We present SWE-MISBEHAVIOR, the first taxonomy and evaluation framework for diagnosing boundary-violating misbehaviors in coding agents. It contains 7.4K human-in-the-loop synthesized samples spanning three layers of agent action space: (i) Code Generation, (ii) File Management,
- **[ACED-Bench: Evaluating How LLM Agents Acquire and Act on Causal Evidence](https://arxiv.org/abs/2610.14381v1)** _(score 10.233 · 2026-10-09 · Yiwei Chen, Amila Weerasinghe, Siddharth Biswal…)_
  Large language models are increasingly used as scientific assistants, yet we still lack reliable ways to evaluate whether they can investigate a system rather than merely answer a prompt. A useful evaluation must let agents choose experiments, interpret finite evidence, and make
- **[CompanionSafe: From Multi-turn Safety Evaluation to Guardrails for AI Companions](https://arxiv.org/abs/2610.18095v1)** _(score 9.933 · 2026-10-13 · Xinyang Liao, Lingyu Li, Kaicheng Shen…)_
  AI companions provide users with emotional support and ongoing companionship, but their sustained relational interactions also introduce distinct safety risks. Prior work largely targets general harms or specific companion platforms and risk categories, while relying on manually
- **[EgoOmniWorld: Unifying Egocentric Understanding via Ego-Action-World Interactions](https://arxiv.org/abs/2610.18499v1)** _(score 9.0 · 2026-10-13 · Songruo Chen, Yuqian Fu, Yu Li…)_
  Egocentric video understanding spans diverse capabilities, modalities, and evaluation formats, yet these are often studied in isolation despite their tight coupling in real-world interaction. We propose the Ego-Action-World interaction loop as a unifying principle: the wearer per
- **[Choosing LLMs for Strategic Agent Interactions](https://arxiv.org/abs/2610.18354v1)** _(score 8.933 · 2026-10-13 · Arastun Mammadli, Herbert Woisetschläger, Jawad Fayaz…)_
  Game-theoretic benchmarks claim that large language model (LLM) strategic decision-making varies across game types, interaction structures, and capability dimensions. However, they only evaluate strategic performance across individual fixed models. In parallel, contemporary LLM r
- **[Beyond Belief Nesting: Rethinking Higher-Order Theory of Mind in Large Language Models](https://arxiv.org/abs/2610.17777v1)** _(score 8.933 · 2026-10-13 · Shanshan You, Zhengqi Wang, Hao Liu…)_
  Theory of mind (ToM), the ability to reason about others' mental states, underlies effective communication and coordination. Its higher-order form enables reasoning over nested perspectives in strategic interactions. However, existing evaluations often equate belief-nesting depth

### Huggingface (1)

- **[medreason/llm-medical-reasoning-steps-benchmark](https://huggingface.co/datasets/medreason/llm-medical-reasoning-steps-benchmark)** _(score 5.516 · 2026-05-04 · 59 downloads)_
  Hugging Face dataset — 59 downloads, 1 likes. Tags: task_categories:question-answering, task_categories:text-generation, language:en, license:cc-by-nc-4.0, size_categories:1K<n<10K

---

_Produced by [OpenBench Radar](https://github.com/) — automated benchmark retrieval, research & reporting._