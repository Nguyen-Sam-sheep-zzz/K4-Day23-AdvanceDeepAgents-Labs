# Question
Topic: Modern video generation architectures and capabilities (diffusion/transformer/autoregressive, controllability, temporal consistency, quality evaluation); survey about video and multimodal generation.
Scope: 2024-10-09 to 2026-10-09, with foundations as useful; source dates retained as retrieved.
Source families attempted: hf-search, arxiv, web.

## Source 1
id: 2510.08131
url: https://huggingface.co/papers/2510.08131
title: Real-Time Motion-Controllable Autoregressive Video Diffusion
date: 2025-10-09
source: hf-search
retrieved via: hf_search_papers
 evidence type: HF AI-generated summary
evidence excerpt: “AR-Drag is a reinforcement learning-enhanced autoregressive video diffusion model that achieves real-time image-to-video generation with diverse motion control, high visual fidelity, precise motion alignment, and lower latency.”
supported claims:
- The summary characterizes the approach as autoregressive video diffusion with motion control.
- It reports real-time image-to-video, motion alignment, and lower latency as claimed capabilities; this is summary-level evidence only.

## Source 2
id: 2510.09212
url: https://arxiv.org/abs/2510.09212
title: Stable Video Infinity: Infinite-Length Video Generation with Error Recycling
date: 2025-10-10
source: arxiv
retrieved via: arxiv_search; web_fetch
 evidence type: paper abstract/full text
 evidence excerpt: “SVI incorporates Error-Recycling Fine-Tuning, a new type of efficient training that recycles the Diffusion Transformer (DiT)’s self-generated errors into supervisory prompts”
supported claims:
- SVI uses a DiT and trains on self-generated errors to address autoregressive train/test mismatch.
- The abstract claims infinite-length generation, temporal consistency, controllable streaming storylines, and compatibility with audio, skeleton, and text-stream conditions; these are the authors' stated claims, not independent verification.

## Source 3
id: https://arxiv.org/abs/2412.05263
title: Mind the Time: Temporally-Controlled Multi-Event Video Generation
date: 2024-12-02
source: web
retrieved via: web_search; web_fetch
 evidence type: paper abstract/full text
 evidence excerpt: “By fine-tuning a pre-trained video diffusion transformer on temporally grounded data, our approach produces coherent videos with smoothly connected events.”
supported claims:
- MinT associates events with specified time periods using a diffusion transformer.
- The abstract claims temporal control and coherent, smoothly connected events. The full text describes ReRoPE time-aware conditioning.

## Source 4
id: https://arxiv.org/abs/2412.07772
title: From Slow Bidirectional to Fast Autoregressive Video Diffusion Models
date: 2025-09-23
source: web
retrieved via: web_search; web_fetch
 evidence type: paper abstract/full text
 evidence excerpt: “We address this limitation by adapting a pretrained bidirectional diffusion transformer to an autoregressive transformer that generates frames on-the-fly.”
supported claims:
- CausVid converts a bidirectional diffusion transformer to causal autoregressive video generation.
- Abstract reports distillation from 50 to 4 steps, KV caching, 9.4 FPS on one GPU, and VBench-Long total 84.27. These are reported experimental results, dependent on their evaluation setup.

## Source 5
id: https://proceedings.iclr.cc/paper_files/paper/2025/file/e2fb048a8e37ad978fc895528102ce49-Paper-Conference.pdf
title: ARLON
date: 
source: web
retrieved via: web_search
 evidence type: website text
 evidence excerpt: “ARLON outperforms the baseline OpenSora-V1.2 on eight out of eleven metrics selected from VBench”
supported claims:
- ARLON combines autoregressive coarse predictions with a diffusion transformer for long video generation.
- The search result reports a comparison against OpenSora-V1.2 across eleven VBench metrics; date was not supplied in the returned text.

## Source 6
id: https://arxiv.org/pdf/2412.18597
title: DiTCtrl: Exploring Attention Control in Multi-Modal Diffusion Transformer
date: 
source: web
retrieved via: web_search
 evidence type: website text
 evidence excerpt: “We introduce MPVBench, a new benchmark with diverse transition types and specialized metrics for assessing multi-prompt transitions.”
supported claims:
- DiTCtrl is described as a training-free multi-prompt video-generation method using MM-DiT attention control.
- The authors introduce MPVBench and transition-specific evaluation; date was not supplied in the returned result.

## Synthesis
The retrieved work suggests an active architectural convergence: diffusion transformers remain a quality/scalability backbone, while causal/autoregressive generation is pursued for streaming, controllability, and long duration. CausVid uses distillation and caching to reduce latency; SVI instead emphasizes fine-tuning on generated error feedback to mitigate drift. ARLON couples coarse autoregressive planning with DiT refinement. For explicit control, MinT binds event captions to timestamps, while DiTCtrl targets multi-prompt transitions via attention control and proposes task-specific evaluation. Thus temporal consistency is not one property: sources operationalize it through long-horizon drift, chunk transitions, event transitions, and motion coherence. Evaluation spans VBench/VBench-Long, task-specific transition metrics, and throughput/latency; scores across such setups are not directly interchangeable. Evidence here is mostly paper abstracts/search excerpts, with authors' performance claims not independently validated. HF source is an AI-generated summary.

## Gaps
- No usable HF-daily source was requested or attempted.
- Web results for ARLON and DiTCtrl did not provide dates in the returned text; IDs are URLs where no paper ID was supplied. The latter URL is a PDF and could not be date-verified from the available search result.
- HF search returned several out-of-scope older works, excluded here; the selected in-scope HF item has summary-only evidence.
- Search results provide limited coverage of fully autoregressive non-diffusion/token-based video generators and standardized human evaluation; cited claims should be read as reported results, not a comprehensive leaderboard.
