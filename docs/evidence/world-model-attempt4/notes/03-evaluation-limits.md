# Question
How should world-model performance be evaluated, and what are key limitations in grounding, long-horizon consistency, controllability, and transfer?
Topic: World models in AI, especially learned predictive environment models for embodied agents and generative interactive environments.
Scope: Evidence 2024-10-09 through 2026-10-09; foundational context only as needed. Current date: 2026-10-09 (Asia/Saigon).
Source families attempted: web sources; arXiv/HF search.

## Source 1
id: https://arxiv.org/html/2605.25874
url: https://arxiv.org/html/2605.25874
title: WBench: A Comprehensive Multi-turn Benchmark for Interactive Video World Model Evaluation
date: 
source: web
retrieved via: web_search and web_fetch
evidence type: paper full text
 evidence excerpt: “Evaluation remains fragmented, with many works relying on selected demos or task-specific protocols, making fair comparison and failure diagnosis difficult across visual quality, controllability, memory, and physics.”
supported claims:
- WBench evaluates video quality, setting adherence, interaction adherence, consistency, and physics compliance in multi-turn cases.
- It combines 22 automatic sub-metrics and states these were validated against human judgments.
- The paper reports that no one model performs strongly across all dimensions; navigation is largely independent of other dimensions.
- Metrics of visual quality alone do not probe interactive controllability or world-modeling competence, according to the paper.

## Source 2
id: https://arxiv.org/html/2510.18135
url: https://arxiv.org/html/2510.18135
title: World-in-World: World Models in a Closed-Loop World
date: 
source: web
retrieved via: web_search and web_fetch
evidence type: paper full text
 evidence excerpt: “visual quality alone does not guarantee task success—controllability matters more”
supported claims:
- Evaluations should include closed-loop embodied task success, not only open-loop visual quality.
- The authors report that stronger visual scores do not necessarily yield higher success rates.
- The benchmark uses standardized action APIs and online planning to test model utility in agent-environment interaction.
- The paper says long-horizon planning remains challenging due to limited accumulation of spatiotemporal history; panorama-based context gains were inconsistent.
- The authors report adaptation gains from post-training on action-observation data and inference-time planning, but these results are specific to their benchmark/tasks.

## Source 3
id: 2506.04363
url: https://arxiv.org/html/2506.04363
title: WorldPrediction: A Benchmark for High-level World Modeling and Long-horizon Procedural Planning
date: 
source: web
retrieved via: web_search
evidence type: paper text via search result
 evidence excerpt: “current frontier models barely achieve 57% accuracy on WorldPrediction-WM and 38% on WorldPrediction-PP whereas humans are able to solve both tasks perfectly.”
supported claims:
- The benchmark tests semantic/temporal abstraction and procedural planning using visual observations and counterfactual choices.
- It uses action equivalents across visually different contexts to reduce reliance on low-level background continuity cues.
- Its authors identify a gap in perceptual grounding and longer-horizon planning; the reported results apply to this benchmark and tested systems.

## Source 4
id: 2510.19788
url: https://arxiv.org/pdf/2510.19788
title: WorldTest: Evaluating World Models Beyond Next-Frame Prediction
date: 
source: web
retrieved via: web_search
evidence type: paper text via search result
 evidence excerpt: “training and evaluation are anchored to next-frame prediction, and success is scored by reward maximization in the same environment.”
supported claims:
- WorldTest proposes reward-free interaction followed by behavior-based evaluation in a different but related challenge environment.
- The authors argue this tests broad downstream use and transfer rather than only next-frame prediction or reward in the training environment.
- AutumnBench instantiates tasks including masked-frame prediction, planning, and causal-dynamics change prediction; the benchmark is limited to its implemented task/environment suite.

## Synthesis
Evaluation should be multi-axis and behaviorally consequential: assess action-conditioned prediction and interaction fidelity, multi-turn state/identity consistency, physical plausibility, and success in closed-loop tasks. Separate visual fidelity from control: WBench reports navigation capability is largely independent of other dimensions, while World-in-World argues task success cannot be inferred from appearance. Grounding requires tests that tie observations and actions to causal consequences, not merely plausible frames; WorldPrediction uses visually grounded discriminative tasks and exposes remaining model-human gaps. For transfer, WorldTest's derived challenge environment offers a useful test beyond the environment of interaction. These sources differ in emphasis (generative video interaction versus learned agent models) and their benchmarks are not interchangeable. Automatic metric validation, benchmark coverage, task distributions, and the difference between visual consistency and latent causal correctness remain uncertainties; results should not be generalized beyond evaluated settings.

## Gaps
- arxiv_search returned NO RESULTS for the initial broad query; no arxiv-tagged source obtained. HF search returned relevant candidates, but it provides AI-generated summaries and those were not used as direct evidence.
- Web-search output supplied excerpts for WorldPrediction and WorldTest, but full-text fetching was not attempted for these pages; their support here is search-result text only. Dates were not supplied in retrieved output, so left blank.
