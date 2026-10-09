# Question
What primary video-generation foundations are supported by an independent arXiv-family retrieval, and how does that check address the supplied prior notes?
Topic: Video and multimodal generation.
Scope: Foundations and developments through 2026-10-09; independent audit of three prior notes plus directly retrieved seminal video-generation paper.
Source families attempted: arXiv, web (inspection of prior notes; web fallback discovery).

## Source 1
id: 2204.03458
url: https://arxiv.org/abs/2204.03458
title: Video Diffusion Models
date: 
source: arxiv
retrieved via: arxiv_search (query: video generation diffusion models seminal video diffusion model)
evidence type: arXiv search result abstract / paper text
 evidence excerpt: “We train models that generate a fixed number of video frames using a 3D U-Net diffusion model architecture, and we enable generating longer videos by applying this model autoregressively using a new method for conditional generation.”
supported claims:
- The primary record describes fixed-frame video generation with a 3D U-Net diffusion architecture and autoregressive conditional extension for longer sequences.
- The record also describes joint image/video training and results for unconditional, video-prediction, and text-conditioned generation.
- These are claims in the retrieved paper record, not independent replication or a comparative judgment that it is universally seminal.

## Source 2
id: https://arxiv.org/abs/2204.03458
url: https://arxiv.org/abs/2204.03458
title: Video Diffusion Models
date: N/A
source: web
retrieved via: web_search
evidence type: web search result reproducing paper abstract and text
evidence excerpt: “Our model is a natural extension of the standard image diffusion architecture, and it enables jointly training from image and video data”
supported claims:
- The independent web discovery result corroborates the paper's stated image/video joint training and diffusion-video contribution.
- This source is a web-tagged discovery, not an arXiv-tool result; URL is recorded once here as a separate retrieval record only because the source tag differs. (Same paper URL as Source 1.)

## Synthesis
The independent arXiv tool returned a directly relevant primary record, repairing the missing arXiv family in the supplied notes. The evidence supports a specific foundational architectural claim: a 3D U-Net diffusion model generates fixed-length clips, with conditional autoregressive extension, and the record discusses joint image/video training. Web search independently surfaced the same primary paper record and corroborated its framing. The prior notes' Source 4 already quotes the same paper through a NeurIPS PDF found via web, but that does not constitute arXiv-tool source-family coverage. The three reviewed notes otherwise contain many web-tagged sources and HF-tagged summaries; their claims were not re-verified here. Note 02's malformed leading whitespace on some evidence-type lines and Note 03's date/family descriptions were not edited. The available evidence establishes the paper's own claims, not a field-wide ranking or independent evaluation.

## Gaps
- Prior notes inspected: /tmp/work/research/notes/01-foundations.md, /tmp/work/research/notes/02-video-systems.md, /tmp/work/research/notes/03-multimodal.md. Their original citations and exact excerpts remain those notes' evidence; this audit only adds its own usable sources.
- The first arXiv search result was relevant but not the requested direct foundational video paper; the changed query returned Video Diffusion Models. No arXiv tool failure remained unresolved.
- Web search independently returned the same arXiv URL, not a distinct paper. No full web_fetch was performed for this audit.
- No separate new multimodal-specific primary source was retrieved in this audit; the third note already contains multimodal audio/video and interactive-world records. Coverage through 2026-10-09 was not systematically checked.
