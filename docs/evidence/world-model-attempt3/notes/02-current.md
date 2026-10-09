# Question
What approaches and empirical results have emerged in the last two years for world models, including video generative models, action-conditioned models, latent-space planning, and embodied/robotic models?
Topic: world models in AI/robotics
Scope: 2024-10-09 through 2026-10-09. Retrieved publications are dated as returned; no future availability is assumed.
Source families attempted: arXiv, web.

## Source 1
id: 2412.08261
url: https://arxiv.org/abs/2412.08261
title: FLIP: Flow-Centric Generative Planning as General-Purpose Manipulation World Model
date: 2025-02-16
source: arxiv
retrieved via: arxiv_search
 evidence type: paper abstract
 evidence excerpt: “a multi-modal flow generation model as the general-purpose action proposal module; a flow-conditioned video generation model as the dynamics module; and a vision-language representation learning model as the value module.”
supported claims:
- FLIP combines flow proposals, flow-conditioned video prediction, and a value model for planning.
- Its abstract reports experiments on diverse benchmarks and improvement in success rates and long-horizon video-plan quality.

## Source 2
id: https://proceedings.mlr.press/v267/gao25u.html
url: https://proceedings.mlr.press/v267/gao25u.html
title: AdaWorld: Learning Adaptable World Models with Latent Actions
date: 2025-10-06
source: web
retrieved via: web_search
evidence type: website text
evidence excerpt: “extracting latent actions from videos in a self-supervised manner, capturing the most critical transitions between frames.”
supported claims:
- AdaWorld pretrains with self-supervised latent actions and autoregressive world modeling conditioned on them.
- The page’s abstract says experiments across multiple environments report superior simulation quality and visual planning; it gives no numerical result in the retrieved excerpt.

## Source 3
id: https://arxiv.org/html/2509.21797
url: https://arxiv.org/html/2509.21797
title: MoWM: Mixture-of-World-Models for Embodied Planning via Latent-to-Pixel Feature Modulation
date: 
source: web
retrieved via: web_search
evidence type: website text
 evidence excerpt: “MoWM achieves 5.7%, 13.4% improvement in the averaged task success rate across all five stages compared to the most competitive VLA-based and world model-based baselines.”
supported claims:
- This approach fuses pixel-space video-diffusion features with latent motion-aware world-model features for action decoding.
- The page reports CALVIN gains of 5.7% and 13.4% over the stated comparator categories and a 12.7% improvement on task five versus the most competitive baseline.
- Retrieval output did not provide publication date; thus date is left blank.

## Source 4
id: https://arxiv.org/html/2506.04363
url: https://arxiv.org/html/2506.04363
title: WorldPrediction: A Benchmark for High-level World Modeling and Long-horizon Procedural Planning
date: 
source: web
retrieved via: web_search
evidence type: website text
evidence excerpt: “frontier models barely achieve 57% accuracy on WorldPrediction-WM and 38% on WorldPrediction-PP whereas humans are able to solve both tasks perfectly.”
supported claims:
- The benchmark evaluates visual understanding of abstract actions and ordered long-horizon procedures.
- The page reports model performance of up to 57% and 38% on its two tasks, versus perfect human performance.
- The excerpt reports video diffusion model scores of 30.1% and 26.1%, suggesting limitations in action-state causal discrimination on this benchmark.

## Source 5
id: https://arxiv.org/html/2410.10076
url: https://arxiv.org/html/2410.10076
title: VideoAgent: Self-Improving Video Generation for Embodied Planning
date: 
source: web
retrieved via: web_search
evidence type: website text
evidence excerpt: “VideoAgent-Online can be further combined with replanning, achieving 53.7% overall success, surpassing prior state-of-the-art on this benchmark.”
supported claims:
- VideoAgent iteratively refines generated video plans using VLM feedback and can additionally learn from execution feedback.
- The retrieved page reports 53.7% overall success with online data collection and replanning in the described evaluation.
- The source date was not given by web-search output; no date inferred.

## Source 6
id: https://papers.nips.cc/paper_files/paper/2024/file/7dbb5bfab324e3b86af9bd0df15498dd-Paper-Conference.pdf
url: https://papers.nips.cc/paper_files/paper/2024/file/7dbb5bfab324e3b86af9bd0df15498dd-Paper-Conference.pdf
title: iVideoGPT: Interactive VideoGPTs are Scalable World Models
date: 
source: web
retrieved via: web_search
evidence type: website text
evidence excerpt: “action-conditioning improves FVD for BAIR by almost 20%.”
supported claims:
- iVideoGPT is an autoregressive transformer that tokenizes visual observations alongside actions and rewards.
- The retrieved text reports competitive video-prediction and planning performance and an almost 20% BAIR FVD improvement from action conditioning.
- The source is a NeurIPS 2024 paper, but web retrieval did not expose an exact publication date; date left blank.

## Source 7
id: https://arxiv.org/html/2410.15461
url: https://arxiv.org/html/2410.15461
title: Empowering World Models with Reflection for Embodied Video Prediction
date: 
source: web
retrieved via: web_search
evidence type: website text
evidence excerpt: “EVA outperformed AVDC with a 28% higher overall success rate, achieving a 100% success rate in the Move Object task”
supported claims:
- EVA combines video generation and reflection/self-correction to extend prediction and address OOD scenarios.
- The retrieved page reports a 28% higher overall success rate than AVDC in its RT1 evaluation and 100% on Move Object.

## Source 8
id: https://papers.neurips.cc/paper_files/paper/2025/file/4ec03ed08a3fcb59e1c815b5598beff1-Paper-Datasets_and_Benchmarks_Track.pdf
url: https://papers.neurips.cc/paper_files/paper/2025/file/4ec03ed08a3fcb59e1c815b5598beff1-Paper-Datasets_and_Benchmarks_Track.pdf
title: WorldModelBench: Judging Video Generation Models As World Models
date: 
source: web
retrieved via: web_search
evidence type: website text
evidence excerpt: “We crowd-source 67K human labels to accurately measure 14 frontier models.”
supported claims:
- WorldModelBench evaluates video generators on instruction following and physics adherence, rather than only generic video quality.
- The paper reports collecting 67K human labels and evaluating 14 models.
- Retrieved text says models commonly struggle in autonomous driving, human activities, and robotics categories.

## Synthesis
Within the retrieved 2024–2025 evidence, approaches range from interactive action-conditioned video prediction (iVideoGPT), flow-guided generative planning (FLIP), latent-action-conditioned adaptation (AdaWorld), and hybrid pixel/latent representations for embodied planning (MoWM). Other work improves video plans through reflection and feedback (EVA, VideoAgent), while benchmarks test whether generated futures preserve causal/action semantics and physical plausibility (WorldPrediction, WorldModelBench). Reported results are promising but not directly comparable: datasets, tasks, metrics, baselines, and success-rate definitions differ. Specific gains include FLIP’s qualitative claim of improved benchmark success and video quality, iVideoGPT’s nearly 20% BAIR FVD improvement under action conditioning, MoWM’s reported CALVIN gains, and VideoAgent’s 53.7% benchmark success with online data and replanning. Benchmark evidence warns that video realism alone is insufficient: WorldPrediction reports low action/procedure accuracy, and WorldModelBench emphasizes physics violations. Several web results omit exact publication dates, and claims are limited to retrieved abstracts/page text rather than independently checked full papers.

## Gaps
- arXiv search succeeded; web search succeeded. Two distinct retrieval families used.
- No arXiv rate limit or NO RESULTS errors occurred.
- Web-search discovery text often omitted exact publication dates, so these remain blank rather than inferred. Some results may be outside scope if their exact date falls before 2024-10-09; verify dates before relying on them.
- Full-text claims are based on text surfaced by web search; no web_fetch was performed. No sources dated after the actual retrieval horizon are presumed available.