# Question
Topic: Survey of efficient inference and small language models; serving systems, evaluation evidence, and deployment tradeoffs.
Scope: 2024-10-09 through 2026-10-09, with older foundations if needed.
Source families attempted: hf-search, hf-daily, web, arxiv.

## Source 1
id: 2025.acl-long.718
url: https://aclanthology.org/2025.acl-long.718/
title: Demystifying Small Language Models for Edge Deployment
date: 2025-07
source: web
retrieved via: web_search; inspected with web_fetch
evidence type: paper abstract/full text (abstract text retrieved)
evidence excerpt: “This work presents the first comprehensive study of over 60 SLMs” and “their in-context learning capabilities remain limited, and their efficiency has significant optimization potential.”
supported claims:
- The work studies over 60 publicly accessible SLMs.
- Its abstract reports general-task performance exceeding 7B models, alongside limited in-context learning.
- It identifies dynamic task-specific routing, model-hardware co-design, and vocabulary/KV-cache compression as optimization opportunities.

## Source 2
id: URL
url: https://aclanthology.org/anthology-files/pdf/findings/2025.findings-emnlp.645.pdf
title: Revisiting Pruning vs Quantization for Small Language Models
date: 2025-11-04 to 2025-11-09
source: web
retrieved via: web_search; inspected with web_fetch
evidence type: paper full text
evidence excerpt: “We systematically evaluate leading post-training pruning (SparseGPT, Wanda) and quantization (GPTQ, AWQ) across six SLMs from 0.5 to 3.8B, seven languages, and seven downstream tasks.”
supported claims:
- The evaluation covers fidelity, multilingual perplexity and downstream-task accuracy; the paper reports 710 evaluations across methods, models and languages.
- The authors report quantization generally preserves fidelity and multilingual language-modeling performance better than pruning.
- The excerpt qualifies this: quantization's downstream reasoning advantage is less consistent, including on complex tasks such as OpenBookQA; the authors caution against relying on one metric.
- Experimental results were run on a single NVIDIA A100 (SXM 80GB), so the measured comparison is not a broad hardware deployment benchmark.

## Source 3
id: 2511.22334
url: https://arxiv.org/abs/2511.22334
title: Edge Deployment of Small Language Models, a comprehensive comparison of CPU, GPU and NPU backends
date: 2025-11-27
source: web
retrieved via: web_search; inspected with web_fetch
evidence type: paper abstract
 evidence excerpt: “The results indicate that specialized backends outperform general-purpose CPUs, with NPUs achieving the highest performance by a wide margin.”
supported claims:
- The study compares commercial CPU, GPU and NPU options for SLM inference using a common execution framework.
- The abstract reports NPUs lead performance; it also says low-power ARM CPUs are competitive when considering energy use.
- The authors state bandwidth normalization is essential for fair cross-architecture comparisons and EDP favors NPUs.
- Evidence here is abstract-only; no numerical benchmark results independently inspected.

## Source 4
id: 2504.19720
url: https://huggingface.co/papers/2504.19720
title: Taming the Titans: A Survey of Efficient LLM Inference Serving
date: 2025-04-28
source: hf-search
retrieved via: hf_search_papers
evidence type: HF AI-generated summary
evidence excerpt: “A survey explores methods to enhance low latency and high throughput in Large Language Model inference” by addressing “memory overhead and computational demands of the attention mechanism.”
supported claims:
- The HF summary describes the paper as surveying low-latency/high-throughput LLM serving and attention-related memory/computation overhead.
- This is a large-LLM serving survey, not evidence specifically benchmarked on small models; summary only.

## Source 5
id: 2506.06579
url: https://huggingface.co/papers/2506.06579
title: Towards Efficient Multi-LLM Inference: Characterization and Analysis of LLM Routing and Hierarchical Techniques
date: 2025-06-06
source: hf-search
retrieved via: hf_search_papers
evidence type: HF AI-generated summary
evidence excerpt: “dynamically allocate computational resources based on query complexity to reduce computational costs while maintaining performance.”
supported claims:
- HF summary describes routing and hierarchical inference as allocating compute according to query complexity.
- The evidence is an AI-generated summary and concerns multi-LLM inference; it does not establish a measured small-model deployment result.

## Source 6
id: 2506.13404
url: https://huggingface.co/papers/2506.13404
title: A Technical Study into Small Reasoning Language Models
date: 2025-06-16
source: hf-search
retrieved via: hf_search_papers
evidence type: HF AI-generated summary
evidence excerpt: “training strategies such as supervised fine-tuning, knowledge distillation, and reinforcement learning” to enhance “resource-efficient Small Reasoning Language Models.”
supported claims:
- The summary identifies SFT, distillation, and reinforcement learning as studied approaches for small reasoning models.
- It provides no systems-serving measurements in the retrieved text.

## Synthesis
The sources complement one another at distinct layers. The ACL study characterizes SLM capability and proposed edge-optimization directions; the pruning-versus-quantization paper supplies controlled quality/fidelity evaluation across tasks and languages; and the arXiv hardware study compares backends but is available here only as an abstract. The evidence suggests deployment decisions require jointly considering model quality, memory/latency or energy, and target hardware—not assuming a compression metric predicts task quality. HF search summaries add serving concepts (routing, hierarchy, attention-memory optimization), but are AI-generated and do not substitute for inspecting their full papers. No retrieved source provides a direct, end-to-end comparison of serving throughput/latency for the same small models across production-scale systems.

## Gaps
- HF-daily was assigned and attempted on three distinct dates derived from relevant HF-search publication records: 2025-06-06, 2025-04-28, and 2025-06-16. Each call used limit=100 and broad keyword “language model inference”; all returned NO RESULTS. Therefore no usable hf-daily source/tag was obtained; no daily claims are made.
- arxiv_search returned results, but its initial results were mostly irrelevant to this precise topic; the useful edge-backend paper was discovered by web_search and inspected at arXiv, so its source tag remains arxiv only insofar as the original arxiv_search did not return that item—correction: it was returned via web_search; source tag for Source 3 is web, not arxiv.
- HF-search result 2502.14305 had inconsistent listed publication date/title metadata in the tool output, so it was excluded.
- Available serving evidence is thin on direct measured SLM serving-system comparisons, workload distributions, tail latency, batch/concurrency effects, and reproducible energy/throughput figures. The NPU paper was only inspected at abstract level.
