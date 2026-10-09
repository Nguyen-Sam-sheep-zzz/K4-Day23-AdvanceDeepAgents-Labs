# Question
What seminal primary methods established modern generative video foundations, and what exactly do their primary records support?
Topic: Survey about video and multimodal generation; foundational generative video methods.
Scope: Foundations plus relevant work through 2026-10-09; emphasis on directly retrieved seminal papers. Claims below are limited to retrieved primary-record excerpts.
Source families attempted: arXiv; web.

## Source 1
id: https://openaccess.thecvf.com/content_cvpr_2018/papers/Tulyakov_MoCoGAN_Decomposing_Motion_CVPR_2018_paper.pdf
url: https://openaccess.thecvf.com/content_cvpr_2018/papers/Tulyakov_MoCoGAN_Decomposing_Motion_CVPR_2018_paper.pdf
title: MoCoGAN: Decomposing Motion and Content for Video Generation
date: 
source: web
retrieved via: web_search
evidence type: paper full text (search-result excerpt of paper)
evidence excerpt: “Each random vector consists of a content part and a motion part. While the content part is kept fixed, the motion part is realized as a stochastic process.”
supported claims:
- MoCoGAN represents generated video frames using content and motion components, holding content fixed while motion evolves stochastically.
- The record says its adversarial scheme uses both image and video discriminators and supports generating same-content/different-motion and different-content/same-motion videos.

## Source 2
id: https://arxiv.org/html/2104.10157v2
url: https://arxiv.org/html/2104.10157v2
title: VideoGPT: Video Generation using VQ-VAE and Transformers
date: 
source: web
retrieved via: web_search
evidence type: paper full text (search-result excerpt of paper)
evidence excerpt: “VideoGPT uses VQ-VAE that learns downsampled discrete latent representations of a raw video by employing 3D convolutions and axial self-attention. A simple GPT-like architecture is then used to autoregressively model the discrete latents”
supported claims:
- VideoGPT's method discretizes compressed video representations with a VQ-VAE and autoregressively models those latents with a GPT-like transformer.
- The excerpt says the model produced samples competitive with state-of-the-art GAN models on BAIR and high-fidelity natural videos on UCF-101 and TGIF; this is the paper's stated result, not an independent validation.

## Source 3
id: http://arxiv.org/pdf/1907.06571
url: http://arxiv.org/pdf/1907.06571
title: Adversarial Video Generation
date: 
source: web
retrieved via: web_search
evidence type: paper full text (search-result excerpt of paper)
evidence excerpt: “Our proposed model, Dual Video Discriminator GAN (DVD-GAN), scales to longer and higher resolution videos by leveraging a computationally efficient decomposition of its discriminator.”
supported claims:
- DVD-GAN is presented as a GAN for natural video, built on BigGAN and using a spatiotemporal discriminator decomposition.
- The record claims samples up to 256 × 256 resolution and 48 frames, and establishes class-conditional synthesis on Kinetics-600 as a benchmark; these are reported contributions by the authors.

## Source 4
id: https://proceedings.neurips.cc/paper_files/paper/2022/file/39235c56aef13fb05a6adc95eb9d8d66-Paper-Conference.pdf
url: https://proceedings.neurips.cc/paper_files/paper/2022/file/39235c56aef13fb05a6adc95eb9d8d66-Paper-Conference.pdf
title: Video Diffusion Models
date: 
source: web
retrieved via: web_search
evidence type: paper full text (search-result excerpt of paper)
evidence excerpt: “We train models that generate a fixed number of video frames using a 3D U-Net diffusion model architecture, and we enable generating longer videos by applying this model autoregressively using a new method for conditional generation.”
supported claims:
- The work adapts diffusion to video using a 3D U-Net and extends generated sequences with conditional/autoregressive temporal extension.
- Its record says joint image/video training reduces minibatch-gradient variance and speeds optimization, and reports unconditional, prediction, and initial text-conditioned video results.

## Source 5
id: https://makeavideo.studio/Make-A-Video.pdf
url: https://makeavideo.studio/Make-A-Video.pdf
title: Make-A-Video: Text-to-Video Generation without Text-Video Data
date: 
source: web
retrieved via: web_search
evidence type: paper full text (search-result excerpt of paper)
evidence excerpt: “learn what the world looks like and how it is described from paired text-image data, and learn how the world moves from unsupervised video footage.”
supported claims:
- Make-A-Video describes a text-to-video strategy combining paired text-image learning with unsupervised video footage, avoiding paired text-video data.
- Its paper excerpt describes spatial-temporal modules and a pipeline including video decoding, frame interpolation, and two super-resolution models.

## Synthesis
The retrieved records show several complementary foundational design patterns, not a single linear replacement: MoCoGAN makes motion/content disentanglement an explicit latent control; DVD-GAN scales adversarial video synthesis through discriminator decomposition; VideoGPT moves video generation into compressed discrete latents with autoregressive transformer modeling; Video Diffusion Models adapt the diffusion/U-Net family to space-time and describe conditional temporal extension; Make-A-Video transfers image-text priors to video motion learning without paired text-video training. The sources support these method descriptions and authors' stated evaluations, but do not independently establish that any is universally “seminal” or best. The only direct arXiv-family tool call returned NO RESULTS; all usable evidence here came from web search results pointing to primary paper text. Dates were not supplied in the retrieved excerpts, so left blank. The scope's future endpoint (2026-10-09) is not validated by this retrieval.

## Gaps
- arXiv search for “generative video models foundational video generation GAN autoregressive video diffusion video” returned NO RESULTS. Per instructions, no unchanged retry was made; web results provided usable alternatives.
- Source-family coverage includes web only; the requested/arXiv family was attempted but yielded no usable arXiv-tagged source.
- Web results expose paper text excerpts, but no separate web_fetch inspection was performed; source tags reflect web_search retrieval.
- Metadata dates were unavailable in returned result text. No coverage claim is made for work after the retrieved records or through 2026-10-09.
