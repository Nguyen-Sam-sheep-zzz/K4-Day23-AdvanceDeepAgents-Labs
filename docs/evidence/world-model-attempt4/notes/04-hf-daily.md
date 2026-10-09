# Question
Which relevant papers appear in dated Hugging Face daily paper lists, and what do their paper entries establish?
Topic: World models in AI: learned predictive models for control, embodied agents, and interactive video/world simulation.
Scope: Retrieved publication dates through 2026-10-09; prioritize 2024-10-09–2026-10-09. Historic foundations included only if actually dated/listed.
Source families attempted: hf-search; hf-daily.

## Source 1
id: 2511.07416
url: https://huggingface.co/papers/2511.07416
title: Robot Learning from a Physical World Model
date: 2025-11-10
source: hf-daily
retrieved via: hf_daily_papers, date=2025-11-11, keyword=world
 evidence type: HF AI-generated summary
evidence excerpt: “We introduce PhysWorld, a framework that enables robot learning from video generation through physical world modeling.”
supported claims:
- The entry presents PhysWorld as using video generation with physical world modeling for robot learning.

## Source 2
id: 2410.18072
url: https://huggingface.co/papers/2410.18072
title: WorldSimBench: Towards Video Generation Models as World Simulators
date: 2024-10-23
source: hf-daily
retrieved via: hf_daily_papers, date=2024-10-24, keyword=world
evidence type: HF AI-generated summary
evidence excerpt: “we classify the functionalities of predictive models into a hierarchy and take the first step in evaluating World Simulators by proposing a dual evaluation fram”
supported claims:
- The entry describes a hierarchy of predictive-model functionalities and a proposed dual evaluation framework for world simulators.

## Source 3
id: 2607.03964
url: https://huggingface.co/papers/2607.03964
title: Worldscape-MoE: A Unified Mixture-of-Experts World Model for Scalable Heterogeneous Action Control
date: 2026-07-04
source: hf-search
retrieved via: hf_search_papers, query=world models learned predictive models control embodied agents interactive video simulation
evidence type: HF AI-generated summary
evidence excerpt: “Worldscape-MoE is a Mixture-of-Experts world model using Diffusion Transformers that unifies heterogeneous action control through shared dynamics modeling and modality-aware injection.”
supported claims:
- The search entry characterizes Worldscape-MoE as a MoE world model using Diffusion Transformers for heterogeneous action control and shared dynamics modeling.

## Source 4
id: 2511.09057
url: https://huggingface.co/papers/2511.09057
title: PAN: A World Model for General, Interactable, and Long-Horizon World Simulation
date: 2025-11-12
source: hf-search
retrieved via: hf_search_papers, query=world models learned predictive models control embodied agents interactive video simulation
evidence type: HF AI-generated summary
evidence excerpt: “PAN, a general, interactable, and long-horizon world model, predicts future world states using a Generative Latent Prediction (GLP) architecture”
supported claims:
- The entry says PAN predicts future world states with a GLP architecture and frames it as interactive, long-horizon simulation.

## Synthesis
The dated daily-list entries recovered here span two distinct functions: PhysWorld connects generated video and physical reconstruction to robot learning, while WorldSimBench proposes a way to evaluate predictive models as world simulators. These are daily-list records, not independent verification of reported capabilities; the available evidence is the HF paper-page summary, not fetched full paper text. HF search surfaced examples of action-control world modeling (Worldscape-MoE) and long-horizon interactive simulation (PAN), but those are not evidence of appearance on a daily list. No disagreements are apparent in these short summaries; they make different claims and do not provide comparable empirical results.

## Gaps
- Required HF search was performed first and returned relevant candidates with publication dates. Three distinct retrieved candidate dates were queried in dated daily lists: 2026-07-04 (keyword `world model`), 2025-11-12 (`world model`), and 2024-10-23 (`world model`); all returned NO RESULTS.
- As instructed after empty results, tried adjacent dates with broader keyword `world`: 2026-07-05 returned NO RESULTS; 2025-11-11 returned results including relevant PhysWorld (published 2025-11-10); 2024-10-24 returned results including relevant WorldSimBench (published 2024-10-23).
- Dates above refer to the requested daily-list date versus each returned paper's `published` date. No other daily-list items were treated as relevant. No arXiv or web sources were attempted; daily entries only provide HF-generated summaries here, not full-text confirmation.
