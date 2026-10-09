# Question
What are the recent RL algorithms and training strategies for LLM reasoning, including reasoning-specific RL, verifiable rewards, data efficiency, and scaling?
Topic: reinforcement learning for LLM reasoning
Scope: 2024-10-09 through 2026-10-09 plus necessary methodological context; do not assume undated recency.
Source families attempted: hf-search, hf-daily, arxiv, web

## Source 1
id: 2506.18254
url: https://huggingface.co/papers/2506.18254
title: RLPR: Extrapolating RLVR to General Domains without Verifiers
date: 2025-06-23
source: hf-search
retrieved via: hf_search_papers
 evidence type: HF AI-generated summary
evidence excerpt: “RLPR, a verifier-free framework using LLM's token probability scores as reward signals”
supported claims:
- RLPR uses token probability scores as reward signals in a verifier-free framework.
- Summary says it targets general and mathematical domains.

## Source 2
id: 2511.22570
url: https://huggingface.co/papers/2511.22570
title: DeepSeekMath-V2: Towards Self-Verifiable Mathematical Reasoning
date: 2025-11-27
source: hf-search
retrieved via: hf_search_papers
evidence type: HF AI-generated summary
evidence excerpt: “A self-verifying large language model for theorem proving improves mathematical reasoning by incentivizing rigorous step-by-step derivations”
supported claims:
- Summary describes self-verification and rigorous derivations as central training objectives.

## Source 3
id: 2508.00410
url: https://huggingface.co/papers/2508.00410
title: Co-Reward: Self-supervised Reinforcement Learning for Large Language Model Reasoning via Contrastive Agreement
date: 2025-08-01
source: hf-search
retrieved via: hf_search_papers
evidence type: HF AI-generated summary
evidence excerpt: “using contrastive agreement across semantically analogical questions”
supported claims:
- The summary describes self-supervised RL with cross-question contrastive agreement and no human labels.

## Source 4
id: 2602.03048
url: https://huggingface.co/papers/2602.03048
title: CoBA-RL: Capability-Oriented Budget Allocation for Reinforcement Learning in LLMs
date: 2026-02-03
source: hf-search
retrieved via: hf_search_papers
evidence type: HF AI-generated summary
evidence excerpt: “adapts rollout budget allocation for LLM training by evaluating sample training value and optimizing resource distribution”
supported claims:
- Summary describes capability-oriented adjustment of rollout budgets to allocate resources by estimated training value.

## Source 5
id: 2509.23962
url: https://huggingface.co/papers/2509.23962
title: Conditional Advantage Estimation for Reinforcement Learning in Large Reasoning Models
date: 2025-09-28
source: hf-search
retrieved via: hf_search_papers
evidence type: HF AI-generated summary
evidence excerpt: “CANON, a conditional advantage estimation method, enhances reinforcement learning ... improving reasoning capabilities and token efficiency”
supported claims:
- Summary characterizes CANON as conditional advantage estimation with token-efficiency aims.

## Source 6
id: 2605.11403
url: https://arxiv.org/abs/2605.11403
title: fg-expo: Frontier-guided exploration-prioritized policy optimization via adaptive kl and gaussian curriculum
date: 2026-05-12
source: arxiv
retrieved via: arxiv_search
evidence type: paper abstract
evidence excerpt: “a fixed KL coefficient overly restricts policy exploration ... uniform question sampling overlooks that moderately difficult problems produce the most informative gradient signals.”
supported claims:
- Abstract motivates adaptive KL and difficulty-aware curriculum based on exploration and informativeness.

## Source 7
id: 2602.03452
url: https://arxiv.org/abs/2602.03452
title: Beyond Variance: Prompt-Efficient RLVR via Rare-Event Amplification and Bidirectional Pairing
date: 2026-02-03
source: arxiv
retrieved via: arxiv_search
evidence type: paper abstract
evidence excerpt: “an effective minibatch should provide both (i) a reliable positive anchor and (ii) explicit negative learning signals from rare failures.”
supported claims:
- Abstract proposes prompt selection/minibatch design combining positive anchors and rare negative examples for prompt-efficient RLVR.

## Source 8
id: 2512.23165
url: https://arxiv.org/abs/2512.23165
title: Evaluating Parameter Efficient Methods for RLVR
date: 2025-12-29
source: arxiv
retrieved via: arxiv_search
evidence type: paper abstract
evidence excerpt: “first comprehensive evaluation of over 12 PEFT methodologies across the DeepSeek-R1-Distill families”
supported claims:
- Abstract reports comparative evaluation of more than 12 parameter-efficient methods under RLVR.

## Source 9
id: 2501.12948
url: https://arxiv.org/abs/2501.12948
title: DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning
date: 2025-01-22
source: web
retrieved via: web_search (result on arxiv.org)
evidence type: paper abstract
 evidence excerpt: “reasoning abilities ... can be incentivized through pure reinforcement learning (RL), obviating the need for human-labeled reasoning trajectories.”
supported claims:
- Abstract says RL can induce reasoning without human-labeled reasoning trajectories.
- It reports emergent self-reflection, verification, and dynamic strategy adaptation.

## Source 10
id: https://www.nature.com/articles/s41586-025-09422-z
url: https://www.nature.com/articles/s41586-025-09422-z
title: DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning
 date: 2025-09-17
source: web
retrieved via: web_search
 evidence type: website text
 evidence excerpt: “The reward signal is only based on the correctness of final predictions against ground-truth answers, without imposing constraints on the reasoning process itself.”
supported claims:
- The report describes GRPO and outcome correctness reward without process constraints for R1-Zero.
- It describes R1's pipeline adding cold-start data, subsequent RL, rejection sampling/SFT, and a second RL stage.
- It says reasoning uses rule-based rewards, while general data uses model-based rewards.
- It reports dynamically allocating inference tokens by problem complexity, with overthinking still a concern.

## Source 11
id: 2507.23726
url: https://huggingface.co/papers/2507.23726
title: Seed-Prover: Deep and Broad Reasoning for Automated Theorem Proving
date: 2025-07-31
source: hf-daily
retrieved via: hf_daily_papers, date=2025-08-01, keyword=reasoning
 evidence type: HF AI-generated summary
evidence excerpt: “Dedicated domain-specific languages like Lean provide clear supervision via formal verification of proofs, enabling effective training through reinforcement learning.”
supported claims:
- Summary says formal verification in Lean supplies supervision for RL theorem proving.

## Synthesis
The retrieved sources point to several complementary strategies: outcome-verifiable rewards with GRPO (DeepSeek-R1), formal proof verification (Seed-Prover), and learned/verifier-free or self-supervised reward alternatives (RLPR and Co-Reward). Data efficiency is addressed explicitly through prompt selection and rare-failure signals, while computation efficiency appears in adaptive rollout budgeting, PEFT evaluation, and complexity-dependent inference allocation. New optimization proposals emphasize adaptive exploration/KL, difficulty curricula, and advantage estimation. These are mostly abstracts or HF-generated summaries, so reported benefits are not independently validated here. The R1 technical report presents a staged recipe rather than a single universal algorithm; its plain rule-based reasoning rewards differ from model-based rewards used for general tasks.

## Gaps
- HF daily attempts: 2025-06-23, keyword=reasoning (returned results, but none directly relevant to RL reasoning); 2025-08-01 (Seed-Prover relevant); 2025-09-28 returned NO RESULTS. The two non-relevant papers from June were not cited. Only one of the three dated lists yielded a clearly relevant paper.
- HF search summaries are AI-generated; paper full text was not fetched for those entries.
- Arxiv results were search-result abstracts only; no full-text fetch performed.
- Web result provided detailed Nature page text and an arXiv abstract surfaced through web search; no separate web_fetch performed.
- Recent literature coverage is partial; the HF-daily requirement for genuinely relevant listed work is fulfilled by Seed-Prover only, and the other inspected dates yielded a gap.
