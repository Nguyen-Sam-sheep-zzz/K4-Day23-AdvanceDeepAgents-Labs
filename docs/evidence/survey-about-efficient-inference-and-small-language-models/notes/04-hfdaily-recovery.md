# Question
Topic: Efficient inference and small language models
Scope: Focused recovery of HF-daily source family; through 2026-10-09.
Source families attempted: hf-search, hf-daily

## Source 1
id: 2608.11045
url: https://huggingface.co/papers/2608.11045
title: ReRound: Reconstructive Rounding to Resolve Midpoint Ambiguity in Calibration-Free LLM Quantization
date: 2026-08-11
source: hf-daily
retrieved via: hf_daily_papers, historical daily list dated 2026-08-13, keyword "model"
evidence type: HF daily paper summary (AI-generated summary; not full text)
evidence excerpt: “ReRound (Reconstructive Rounding) is a post-training quantization method that addresses the midpoint ambiguity inherent in standard round-to-nearest (RTN) schemes when quantizing weights near the centers of quantization intervals.”
supported claims:
- The summary describes ReRound as a post-training quantization method addressing midpoint ambiguity in round-to-nearest weight quantization.

## Source 2
id: 2409.02060
url: https://huggingface.co/papers/2409.02060
title: OLMoE: Open Mixture-of-Experts Language Models
date: 2024-09-03
source: hf-daily
retrieved via: hf_daily_papers, historical daily list dated 2024-09-04, keyword "model"
evidence type: HF daily paper summary (AI-generated summary; not full text)
evidence excerpt: “OLMoE-1B-7B has 7 billion (B) parameters but uses only 1B per input token.”
supported claims:
- The summary reports that OLMoE-1B-7B uses one billion parameters per input token despite having seven billion total parameters.

## Source 3
id: 2608.12307
url: https://huggingface.co/papers/2608.12307
title: AI4AI at Test-Time: Strong-to-Weak Capability Transfer via Harnesses
date: 2026-08-12
source: hf-daily
retrieved via: hf_daily_papers, historical daily list dated 2026-08-14, keyword "model"
evidence type: HF daily paper summary (AI-generated summary; not full text)
evidence excerpt: “whether such transfer can instead occur at test time. We study strong-to-weak scaffolding: whether a stronger builder model can construct inference-time harnesses that help a weaker target model solve tasks more reliably without any parameter updates.”
supported claims:
- The summary says the paper studies inference-time harnesses to assist weaker target models without changing their parameters.

## Source 4
id: 2609.33601
url: https://huggingface.co/papers/2609.33601
title: JustQuant: You Don't Need Smoothing, SVD, or Rotation for 4-Bit Activation Quantization
date: 2026-09-27
source: hf-search
retrieved via: hf_search_papers query “efficient inference small language models quantization distillation”
evidence type: HF search result summary (AI-generated summary; not full text)
evidence excerpt: “Model quantization offers a promising way to compress these models and accelerate inference.”
supported claims:
- The returned summary characterizes quantization as a compression and inference acceleration approach.

## Source 5
id: 2608.11981
url: https://huggingface.co/papers/2608.11981
title: Benchmarking Trustworthiness of SLMs: Pre-trained vs. Compressed
date: 2026-08-12
source: hf-search
retrieved via: hf_search_papers query “efficient inference small language models quantization distillation”
evidence type: HF search result summary (AI-generated summary; not full text)
evidence excerpt: “Quantized compression of reliable large language models yields small language models with better trustworthiness and adaptability than training from scratch”
supported claims:
- The returned summary reports the stated comparison of compressed models and models trained from scratch; this is summary-only evidence.

## Synthesis
The HF-daily results supply examples spanning sparse activation (OLMoE), weight quantization (ReRound), and inference-time scaffolding for weaker models (AI4AI). HF-search adds a recent quantization summary and an SLM-compression comparison. These are complementary indications of efficiency strategies, not directly comparable measurements: evidence here is limited to HF-provided summaries, and no full paper text was inspected. Search and daily lists overlap in topic but the distinct daily URLs are retained once each.

## Gaps
- Three initial historical daily calls were made at dates retrieved from HF-search: 2026-09-27, 2026-08-12, and 2024-09-03, limit=100, keyword “language model”. The 2026-09-27 call returned NO RESULTS; the other lists yielded no clearly relevant efficient/small-model item.
- Per allowed adjacent-date/broader-keyword retry, daily calls were made at 2026-09-26, 2026-08-13, and 2024-09-04, limit=100, keyword “model”. 2026-09-26 returned NO RESULTS; 2026-08-13 yielded ReRound; 2024-09-04 yielded OLMoE.
- The adjacent 2026-08-14 call (limit=100, keyword “model”) yielded AI4AI, a relevant weaker-model inference-time item. Date selection came from HF-daily output dated 2026-08-12, and thus was a nearby-day follow-up rather than an independently HF-search-retrieved date.
- Prior failed dates named in the task (2025-06-06, 2025-04-28, 2025-06-16) were not retried; this run documents its new attempts and did not establish relevant records for those dates.
- No web or arXiv family attempted; assigned HF-daily and HF-search families were obtained. All evidence is summary-only; no primary full-text source inspected.
