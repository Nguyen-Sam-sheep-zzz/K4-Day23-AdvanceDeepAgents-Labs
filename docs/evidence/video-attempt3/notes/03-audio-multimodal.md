# Question
Topic: Survey about video and multimodal generation; audio-video generation, audio-conditioned/video-with-audio generation, cross-modal alignment and limitations.
Scope: Relevant foundations and work through 2026-10-09. Primary DreamFoley evidence is used; WorldSonus is not relied on.
Source families attempted: Hugging Face search, dated Hugging Face daily lists, arXiv search, web search.

## Source 1
id: 2512.06022
url: https://arxiv.org/abs/2512.06022
 title: DreamFoley: Scalable VLMs for High-Fidelity Video-to-Audio Generation
date: 2025-12-04
source: web
retrieved via: web_search (DreamFoley query; arXiv primary page and HTML full-text excerpts returned)
evidence type: paper abstract/full text
 evidence excerpt: “we introduce an autoregressive audio generation architecture (DreamFoley) that harnesses the capabilities of large vision-language models (VLMs) to jointly model sequential interactions among video, audio, and text modalities.” Full-text excerpt: “the current implementation of DreamFoley supports audio generation for videos up to 10 seconds in length.”
supported claims:
- DreamFoley is an autoregressive video-to-audio approach using a VLM to model video, audio, and text.
- It uses dual visual encoders and an RVQ audio tokenizer (as stated in the returned abstract).
- Its reported current implementation supports videos up to 10 seconds; this is a stated limitation in the returned full-text excerpt.

## Source 2
id: 2407.01494
url: https://huggingface.co/papers/2407.01494
title: FoleyCrafter: Bring Silent Videos to Life with Lifelike and Synchronized Sounds
date: 2024-07-01
source: hf-search
retrieved via: hf_search_papers (audio/video generation query)
evidence type: HF AI-generated summary
evidence excerpt: “generates high-quality, semantically aligned, and temporally synchronized sound effects for videos using parallel cross-attention layers and a timestamp-based adapter.”
supported claims:
- HF summary describes FoleyCrafter as video-conditioned sound-effect generation targeting semantic and temporal alignment.
- Summary identifies parallel cross-attention and a timestamp-based adapter; underlying full paper was not inspected here.

## Source 3
id: 2412.15322
url: https://huggingface.co/papers/2412.15322
title: Taming Multimodal Joint Training for High-Quality Video-to-Audio Synthesis
date: 2024-12-19
source: hf-search
retrieved via: hf_search_papers (audio/video generation query)
evidence type: HF AI-generated summary
evidence excerpt: “A multimodal framework jointly trains with video and text to generate high-quality, semantically aligned, and visually synchronized audio”
supported claims:
- The HF summary characterizes this approach as jointly conditioned/trained with video and text.
- Its claimed aim is semantic alignment and visual synchronization; this summary alone does not independently validate performance.

## Source 4
id: 2511.13219
url: https://arxiv.org/abs/2511.13219
title: FoleyBench: A Benchmark For Video-to-Audio Models
date: 2025-11-24
source: web
retrieved via: web_search (FoleyBench benchmark/limitation query; arXiv abstract text returned)
evidence type: paper abstract
 evidence excerpt: “We find that 74% of videos from past evaluation datasets have poor audio-visual correspondence.” The abstract also says Foley requires audio “both semantically aligned with visible events and temporally aligned with their timing.”
supported claims:
- The benchmark paper reports poor audio-visual correspondence in 74% of videos from past evaluation datasets.
- It frames Foley evaluation as requiring both semantic correspondence and temporal synchronization.
- Its abstract describes FoleyBench as 5,000 video/audio/text triplets with visible sound sources causally tied to on-screen events.

## Source 5
id: 2606.30811
url: https://arxiv.org/abs/2606.30811
title: AVTok: 1D Unified Tokenization for Holistic Audio-Video Generation
date: 2026-06-29
source: arxiv
retrieved via: arxiv_search (audio-conditioned/video generation alignment query; returned abstract summary)
evidence type: paper abstract (tool-provided summary)
evidence excerpt: “preceding methods predominantly adopt a dual-branch design with separate tokenization and generation modules per modality, neglecting the representation gap while necessitating intensive computational resources”
supported claims:
- The abstract summary identifies separate modality branches and a representation gap as concerns in prior audio-video generation.
- It presents AVTok as unified tokenization, but the available excerpt does not establish the magnitude of its benefits.

## Source 6
id: 2309.16429
url: https://huggingface.co/papers/2309.16429
title: Diverse and Aligned Audio-to-Video Generation via Text-to-Video Model Adaptation
date: 2023-09-28
source: hf-search
retrieved via: hf_search_papers (audio video generation multimodal alignment query)
evidence type: HF AI-generated summary
evidence excerpt: “A lightweight adaptor network improves video generation conditioned on audio and text by aligning audio segments with video segments and enhancing alignment and diversity.”
supported claims:
- The HF summary describes audio-and-text-conditioned video generation and segment-level alignment.
- It is an earlier audio-to-video direction, distinct from video-to-audio Foley generation.

## Synthesis
The sources describe complementary tasks rather than one uniform problem: FoleyCrafter, the joint-training work, and DreamFoley generate audio from video (sometimes text); the 2023 audio-to-video work conditions video on audio and text. Across them, alignment is semantic (the generated sound should match visible events) and temporal (sound timing should match events). DreamFoley's primary-source abstract describes an autoregressive VLM with dual visual encoders and RVQ audio tokens; its full-text excerpt makes the present 10-second implementation limit explicit. The newer AVTok summary points to representation gaps and compute costs in dual-branch designs, while FoleyBench cautions that commonly used evaluation data may itself have weak audio-visual correspondence. Claims from HF summaries are discovery-level and should not be treated as independently verified evaluations. The 2026 scope cutoff is 2026-10-09; searched records are dated no later than that cutoff.

## Gaps
- Dated HF daily attempts (all limit=100, keyword “audio video”): 2025-12-04, 2026-03-16, and 2024-11-26 each returned NO RESULTS. These are three distinct publication dates retrieved via HF search, but no relevant daily-list items were available. Thus hf-daily is an attempted but missing source tag; no daily citation is claimed.
- No direct hf_search match for DreamFoley was used as its primary evidence: the web result exposed the arXiv abstract and full-text excerpts, satisfying the instruction not to rely on WorldSonus.
- arXiv search returned relevant candidate records but only abstract/tool summaries, not full text. The excerpt for AVTok is the tool-provided abstract summary; detailed method/performance claims remain unverified.
- No full-text inspection was obtained for FoleyCrafter or the HF-described audio-to-video and joint-training papers; those entries are explicitly marked as AI-generated summaries.
- Web search found no separate non-paper technical documentation necessary to the core claims; web evidence here is paper text surfaced by web search.
