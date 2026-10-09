# Question
What foundational primary methods established modern video generation and what limitations remain?
Topic: Survey about video and multimodal generation.
Scope: Foundational work through 2026-10-09, emphasizing directly retrieved seminal primary sources and subsequent two years where evidence permits.
Source families attempted: arxiv, web

## Source 1
id: https://openaccess.thecvf.com/content_cvpr_2018/papers/Tulyakov_MoCoGAN_Decomposing_Motion_CVPR_2018_paper.pdf
url: https://openaccess.thecvf.com/content_cvpr_2018/papers/Tulyakov_MoCoGAN_Decomposing_Motion_CVPR_2018_paper.pdf
title: MoCoGAN: Decomposing Motion and Content for Video Generation
date: 2018
source: web
retrieved via: web_search
evidence type: paper abstract/full text
evidence excerpt: “Each random vector consists of a content part and a motion part. While the content part is kept fixed, the motion part is realized as a stochastic process.”
supported claims:
- MoCoGAN established an adversarial approach that separates relatively fixed video content from stochastic motion, using image and video discriminators (web output).
- The paper notes a fixed-length limitation: “this assumption forces every generated video clip to have the same length.”

## Source 2
id: https://export.arxiv.org/pdf/1907.06571
url: https://export.arxiv.org/pdf/1907.06571
title: ADVERSARIAL VIDEO GENERATION ON COMPLEX DATASETS
date: 2019
source: web
retrieved via: web_search
evidence type: paper abstract/full text
evidence excerpt: “Generating long and high resolution videos is a heavy computational challenge”
supported claims:
- DVD-GAN used dual spatial and temporal discriminators to scale video GAN training to complex Kinetics-600 footage, according to retrieved text.
- The authors identify computational cost and discriminator scalability as central constraints; mode collapse and lack of explicit likelihood are listed as GAN limitations.

## Source 3
id: https://arxiv.org/abs/1812.01717
url: https://arxiv.org/abs/1812.01717
title: Towards Accurate Generative Models of Video: A New Metric & Challenges
date: 2019-03-27
source: arxiv
retrieved via: arxiv_search
evidence type: paper abstract/full text
evidence excerpt: “current progress is hampered by (1) the lack of qualitative metrics that consider visual quality, temporal coherence, and diversity of samples, and (2) the wide gap between purely synthetic video data sets and challenging real-world data sets”
supported claims:
- This work introduced Fréchet Video Distance and the StarCraft 2 Videos benchmark to address evaluation and capability-testing challenges.
- The output identifies long-term memory and relational reasoning as unresolved challenges in the evaluated models.

## Source 4
id: https://proceedings.neurips.cc/paper_files/paper/2022/file/39235c56aef13fb05a6adc95eb9d8d66-Paper-Conference.pdf
url: https://proceedings.neurips.cc/paper_files/paper/2022/file/39235c56aef13fb05a6adc95eb9d8d66-Paper-Conference.pdf
title: Video Diffusion Models
date: 2022
source: web
retrieved via: web_search
evidence type: paper abstract/full text
evidence excerpt: “We train models that generate a fixed number of video frames using a 3D U-Net diffusion model architecture, and we enable generating longer videos by applying this model autoregressively”
supported claims:
- The primary method extends Gaussian diffusion to video with a 3D U-Net, factorized space-time attention, joint image/video training, and reconstruction-guided extension.
- Long video generation uses autoregressive extension; the paper reports replacement sampling yielded blocks “uncorrelated” in time, motivating reconstruction guidance.
- The paper explicitly flags dataset bias and says text-to-video work requires social-bias auditing; it describes the work as a starting point.

## Source 5
id: https://gwern.net/doc/www/arxiv.org/e81e41a4bb9fd362e05e1a33025a5b48d24ea046.pdf
url: https://gwern.net/doc/www/arxiv.org/e81e41a4bb9fd362e05e1a33025a5b48d24ea046.pdf
title: VideoGPT: Video Generation using VQ-VAE and Transformers
date: 2021
source: web
retrieved via: web_search
evidence type: paper abstract/full text
evidence excerpt: “A simple GPT like architecture is then used to autoregressively model the discrete latents using spatio-temporal position encodings.”
supported claims:
- VideoGPT established a compressed discrete-latent pipeline: a 3D-convolution/axial-attention VQ-VAE encodes clips and an autoregressive transformer models latents.
- Its authors report competitive BAIR samples and high-fidelity natural-video samples; the retrieved text also notes pixel-level autoregressive models have large sampling-time and compute requirements.

## Synthesis
The directly retrieved primary sources trace complementary foundations: GANs made motion/content factorization and scalable spatial/temporal discrimination explicit; compressed-latent autoregression (VideoGPT) made transformer likelihood modeling practical; diffusion models jointly denoised spatiotemporal blocks and introduced conditional extension for longer clips. FVD/SCV formalized that perceptual frame quality alone is insufficient: temporal coherence, diversity, long-term memory and relational reasoning matter. Persistent tradeoffs are compute and scaling to long/high-resolution footage, fixed or chunked temporal horizons and continuity across chunk boundaries, GAN diversity/evaluation issues, and unresolved temporal reasoning and bias. Sources do not directly establish a comprehensive multimodal-generation history; text conditioning appears explicitly in the diffusion source, but coverage is limited. Evidence is tool-returned excerpts/abstracts and highlights, not independently verified full-text inspection for every item; the scope endpoint is future-dated relative to retrieved records, so later work is not assessed.

## Gaps
- arxiv_search query returned NO RESULTS; changed to web discovery and obtained an arXiv-indexed result via that source family. No second identical failed call made.
- Web provided primary-source text for MoCoGAN, DVD-GAN, VideoGPT and Video Diffusion Models; no separate direct arXiv-search result for these was obtained.
- No evidence retrieved for the final portion of the requested time frame or a broad multimodal-generation survey; claims about those periods/topics are therefore not made.
