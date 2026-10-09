# Question
Topic: survey about video and multimodal generation
Scope: Text/image-to-video systems, 2024-10-09 through 2026-10-09; foundations where useful.
Source families attempted: arXiv, web, HF search

## Source 1
id: https://aclanthology.org/2025.findings-acl.241.pdf
url: https://aclanthology.org/2025.findings-acl.241.pdf
title: TC-Bench: Benchmarking Temporal Compositionality in Conditional Video Generation
date: 2025-07-27 (proceedings dates stated as July 27–August 1, 2025)
source: web
retrieved via: web_search; web_fetch
 evidence type: paper full text
 evidence excerpt: “Our experiments reveal that contemporary video generators are still weak in prompt understanding and achieve less than 20% of the compositional changes”
supported claims:
- TC-Bench targets temporal compositionality including attribute transitions, object relations, and background shifts.
- It proposes TCR and TC-Score, evaluated through frame-level assertions and VLMs; authors report better correlation with human judgments than existing metrics.
- Authors report most tested models accomplish less than ~20% of test cases; this is the paper's benchmark result, not independent verification.
- The text says models must synthesize seamless transitions while maintaining object consistency. It identifies prompt understanding and temporal consistency as weaknesses.

## Source 2
id: 2504.06861
url: https://huggingface.co/papers/2504.06861
title: EIDT-V: Exploiting Intersections in Diffusion Trajectories for Model-Agnostic, Zero-Shot, Training-Free Text-to-Video Generation
date: 2025-04-09
source: hf-search
retrieved via: hf_search_papers
 evidence type: HF AI-generated summary
 evidence excerpt: “A model-agnostic approach using diffusion trajectories and grid-based prompts generates high-quality, training-free text-to-video content with controlled coherence and variance.”
supported claims:
- The HF summary describes EIDT-V as model-agnostic, zero-shot, training-free T2V using diffusion trajectories and grid-based prompts.
- The summary asserts controlled coherence and variance; it provides no quantitative details or limitations, so these cannot be independently assessed here.

## Source 3
id: https://openaccess.thecvf.com/content/CVPR2025/papers/Cai_DiTCtrl_Exploring_Attention_Control_in_Multi-Modal_Diffusion_Transformer_for_Tuning-Free_CVPR_2025_paper.pdf
url: https://openaccess.thecvf.com/content/CVPR2025/papers/Cai_DiTCtrl_Exploring_Attention_Control_in_Multi-Modal_Diffusion_Transformer_for_Tuning-Free_CVPR_2025_paper.pdf
title: DiTCtrl: Exploring Attention Control in Multi-Modal Diffusion Transformer for Tuning-Free Multi-Prompt Longer Video Generation
date: 2025
source: web
retrieved via: web_search
 evidence type: paper text in search output
 evidence excerpt: “mask-guided KV-sharing strategy”
supported claims:
- The paper describes a training-free, multi-prompt generation approach using masked-guided attention/KV sharing and latent blending to create transitions.
- Its stated goal is semantic consistency and smooth transitions between prompt segments.
- The authors explicitly note limitations: weaker conceptual composition in open-source models and inference-speed challenges from DiT computational overhead.
- The reported human ranking involved 28 users; this is the paper's reported evaluation, not independent validation.

## Source 4
id: https://arxiv.org/html/2510.02226
url: https://arxiv.org/html/2510.02226
title: TempoControl: Temporal Attention Guidance for Text-to-Video Models
date: 2025
source: web
retrieved via: web_search
 evidence type: paper text in search output
 evidence excerpt: “without requiring retraining or additional supervision”
supported claims:
- TempoControl uses inference-time cross-attention steering to control the timing of visual concepts.
- The paper describes correlation, magnitude, and entropy components for temporal alignment, visibility strength, and spatial focus respectively.
- The authors report that temporal objectives can corrupt semantics and that detector-based evaluation is vulnerable to detection failures and degraded image quality.
- The reported evaluation includes a 50-person study and proxy metrics; these remain author-reported evidence.

## Synthesis
Recent approaches in the retrieved material chiefly operate on temporal conditioning rather than simply scaling a single generation pass: DiTCtrl reuses attention features and blends overlapping latent segments; TempoControl steers token attention at inference; EIDT-V's HF summary describes trajectory intersections and grid prompts. TC-Bench supplies a distinct evaluation perspective focused on whether attributes/relations actually change over time, and reports poor completion across tested systems. Evidence here does not support broad claims about scaling trends or training-data/model-size scaling: the sources found describe methods and benchmarks, not controlled scaling studies. Controllability is addressed through multi-prompt transitions and explicit temporal attention signals, but reported gains have tradeoffs (semantic corruption, inference overhead, and detection-based measurement fragility). Benchmark numbers and superiority statements are author-reported, not independently verified. HF summary is AI-generated and lacks detailed evidence.

## Gaps
- arxiv_search returned NO RESULTS for the initial broad query; no arXiv-tagged source obtained. Changed source families and queries rather than repeating the failed call.
- Web search returned useful paper text, while full-text inspection was possible for TC-Bench only. DiTCtrl and TempoControl evidence is from search-result excerpts, not full fetched papers.
- HF search supplied an AI-generated summary, not paper full text; no dated HF-daily attempt was made because HF-daily was not an assigned family.
- Limited direct evidence on scaling laws/model size, production systems, and rigorous cross-system comparison within the requested date range.