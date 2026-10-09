# Video and Multimodal Generation: Architectures, Control, and Alignment

## TL;DR
- Video generation has at least two distinct foundational routes: discrete video latents with an autoregressive prior, and spatiotemporal denoising diffusion; the primary papers support contrasting these rather than treating them as one method. [1][2]
- Recent work combines diffusion-transformer video synthesis with causal/autoregressive generation to target streaming and long duration, but reported speed and consistency depend on each paper's setup and are not a common benchmark. [3][4]
- Temporal direction is becoming more explicit: event-timestamp conditioning and motion control address different forms of controllability. [5][6]
- Audio-video generation is a separate alignment problem: semantic correspondence and event timing both matter, while a benchmark paper reports substantial correspondence defects in prior evaluation data. [7][8]
- The evidence retrieved through 2026-10-09 includes unified generation/understanding proposals and efficiency work, but many HF records are generated summaries rather than independently inspected primary-paper text. [9][10][11]

## Background
VideoGPT is a directly retrieved primary example of latent autoregressive video modeling: a VQ-VAE with 3D convolutions and axial self-attention compresses video into discrete codes, which a GPT-like prior models autoregressively. [1] This makes its contribution distinct from denoising approaches; it should not be conflated with the later paper named *Video Diffusion Models*. [1][2]

*Video Diffusion Models* extends image diffusion to video and reports joint training on image and video data, alongside conditional spatial and temporal extension. [2] Together these primary sources establish a useful conceptual split—next-token modeling over compressed video versus iterative denoising of video representations—without implying that either family alone describes today's systems. [1][2] The retrieved foundational coverage is intentionally narrow; it does not constitute a comprehensive history of GAN, VAE, or other early video-generation lines.

## Scaling duration and reducing latency
Recent approaches try to retain diffusion-transformer synthesis while introducing causal generation. *Stable Video Infinity* describes error-recycling fine-tuning in a DiT autoregressive setting to address self-generated errors and claims infinite-length generation; this is an author-reported goal, not independent proof of unbounded coherent output. [3] CausVid instead adapts a pretrained bidirectional diffusion transformer to frame-by-frame autoregressive generation; its reported distillation and speed figures are tied to its experimental setup. [4]

The daily-list summary for *In-Flight KV Cache with Clean Anchors* describes cache reuse as a way to avoid extra cache-update-only forwards, indicating that efficiency work targets inference overhead as well as model architecture. [9] These sources point toward a practical tradeoff: causalization can support streaming, but long-horizon drift and cache/compute costs remain central constraints; evidence is heterogeneous and the daily record is summary-level. [3][4][9]

## Temporal and motion control
Controllability spans distinct granularity. *Mind the Time* associates events with specified time intervals by fine-tuning a video diffusion transformer on temporally grounded data, targeting multi-event sequencing. [5] The HF-search summary for *AR-Drag* characterizes it as autoregressive video diffusion with motion control, a different control axis from scheduling event captions in time. [6] Because the latter is an AI-generated summary, its claims about real-time capability and alignment should be treated as discovery-level rather than independently verified evidence. [6]

This distinction matters for evaluation: event ordering and duration, object/camera motion, and overall visual plausibility are not interchangeable measures. A retrieved arXiv abstract summary describes PEBench as evaluating prompt enhancers across text-to-video, image-to-video, and reference-to-video settings, suggesting that conditioning mode itself should be accounted for in comparisons. [11] The available excerpt does not justify a claim that any one control method solves these dimensions jointly. [5][6][11]

## Joint audio-video generation and correspondence
Audio-video systems cover different directions of generation. DreamFoley's primary source describes autoregressive video-to-audio generation using a vision-language model to jointly model video, audio, and text. [7] Its cross-modal conditioning makes sound generation depend on visual and textual context, though the evidence retrieved here does not establish how well alignment generalizes across durations or datasets. [7][8] The paper's exact duration limit is omitted because it was not verified against the finalized URL text.

Quality also depends on whether sound matches visible events and their timing. FoleyBench frames both semantic and temporal alignment as necessary and reports that 74% of videos in past evaluation datasets have poor audio-visual correspondence. [8] This figure is the benchmark authors' finding about those datasets, not an estimate of all video data or all model outputs. [8] AVTok's abstract summary describes separate modality branches and a representation gap as concerns motivating unified tokenization; the retrieved evidence supports the stated motivation, not a quantified advantage. [12]

## Unified multimodality and evaluation
Some recent proposals unify understanding and generation rather than treating video synthesis as an isolated endpoint. HF search describes Uni-ViGU as a diffusion-based approach to unified video understanding and generation; this is an AI-generated summary and does not establish comparative performance. [10] More broadly, such proposals frame a research direction, while their practical value depends on task-specific quality, control, and evaluation evidence not supplied by the summary. [10]

The sources collectively show why a single score is inadequate: long-video consistency, event timing, motion adherence, audio correspondence, prompt enhancement, and inference cost measure different objectives. [3][5][4][8][9][11] Retrieved papers and summaries use different benchmarks and evidence levels; their results should not be ranked as if measured under one shared protocol. [4][8][11]

## Trends and open problems
The recent trajectory is toward causal or autoregressive operation layered onto diffusion-transformer systems, with work on error feedback and cache reuse addressing different failure or cost modes. [3][4][9] Whether these methods maintain identity, physical plausibility, and event continuity over genuinely long generations remains uncertain in the evidence reviewed here; papers' stated goals should not be read as settled capability. [3][4]

A second trend is finer-grained conditioning—from timed events to motion instructions and multimodal inputs—but control dimensions require separate, reproducible measurements. [5][6][11] For audio-video synthesis, semantic and temporal alignment must be evaluated together, and flawed correspondence in benchmark material can confound comparisons. [7][8]

Finally, unified multimodal representations and understanding-generation systems are proposed as ways to reduce modality separation, yet retrieved claims are often based on abstracts or generated summaries, and independent comparative evaluations are sparse in this evidence set. [12][10] The source window ends on 2026-10-09; it supports these directions and caveats, not a definitive ranking of systems or a claim that the identified limitations have been solved. [9][11]

## References
[1] VideoGPT: Video Generation using VQ-VAE and Transformers. arxiv. https://arxiv.org/abs/2104.10157 (2021-04-20)
[2] Video Diffusion Models. arxiv. https://arxiv.org/abs/2204.03458 (2022-04-07)
[3] Stable Video Infinity: Infinite-Length Video Generation with Error Recycling. arxiv. https://arxiv.org/abs/2510.09212 (2025-10-10)
[4] From Slow Bidirectional to Fast Autoregressive Video Diffusion Models. web. https://arxiv.org/abs/2412.07772 (2025-09-23)
[5] Mind the Time: Temporally-Controlled Multi-Event Video Generation. web. https://arxiv.org/abs/2412.05263 (2024-12-02)
[6] Real-Time Motion-Controllable Autoregressive Video Diffusion. hf-search. https://huggingface.co/papers/2510.08131 (2025-10-09)
[7] DreamFoley: Scalable VLMs for High-Fidelity Video-to-Audio Generation. web. https://arxiv.org/abs/2512.06022 (2025-12-04)
[8] FoleyBench: A Benchmark For Video-to-Audio Models. web. https://arxiv.org/abs/2511.13219 (2025-11-24)
[9] In-Flight KV Cache with Clean Anchors for Faster Autoregressive Video Diffusion. hf-daily. https://huggingface.co/papers/2609.32540 (2026-09-26)
[10] Uni-ViGU: Towards Unified Video Generation and Understanding via A Diffusion-Based Video Generator. hf-search. https://huggingface.co/papers/2604.08121 (2026-04-09)
[11] Towards Unified Evaluation of Prompt Enhancers for Video Generation. arxiv. https://arxiv.org/abs/2610.11736 (2026-10-08)
[12] AVTok: 1D Unified Tokenization for Holistic Audio-Video Generation. arxiv. https://arxiv.org/abs/2606.30811 (2026-06-29)
