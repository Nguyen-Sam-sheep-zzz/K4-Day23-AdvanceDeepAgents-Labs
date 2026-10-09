# Question
Topic: Survey of efficient inference and small language models: foundational primary methods for quantization, KV-cache optimization, and speculative decoding, and documented limitations.
Scope: Foundational context plus relevant work through 2026-10-09; emphasis on the last two years where evidence permits.
Source families attempted: arxiv, web. arxiv search returned NO RESULTS; web search retrieved primary paper texts/abstract excerpts hosted on arXiv and an institutional paper PDF.

## Source 1
id: https://export.arxiv.org/pdf/2210.17323v2.pdf
url: https://export.arxiv.org/pdf/2210.17323v2.pdf
title: GPTQ (title inferred from retrieved paper body; result title was unavailable)
date: 2022 (publication year in retrieved output's paper text)
source: web
retrieved via: web_search
evidence type: paper abstract/full text excerpts from search result
 evidence excerpt: “On the technical side, our method obtains speedups from reduced memory movement, and does not lead to computational reductions.”
supported claims:
- GPTQ is a one-shot, approximate second-order weight-quantization method; the retrieved text reports 3–4-bit quantization at large model scale.
- Reported end-to-end speedups are implementation- and hardware-dependent; the authors explicitly attribute gains to reduced memory movement, not reduced computation.
- The paper says it does not study activation quantization.

## Source 2
id: https://arxiv.org/pdf/2211.10438
url: https://arxiv.org/pdf/2211.10438
title: SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models
date: 2023 (paper title-year context in retrieved material)
source: web
retrieved via: web_search
evidence type: paper abstract/full text excerpts from search result
evidence excerpt: “SmoothQuant smooths the activation outliers by offline migrating the quantization difficulty from activations to weights with a mathematically equivalent transformation.”
supported claims:
- SmoothQuant uses training-free post-training W8A8 quantization and a per-channel equivalent scaling transformation to handle activation outliers.
- Its retrieved abstract reports up to 1.56× speedup and 2× memory reduction; these are paper-reported results, not universal guarantees.
- The retrieved text documents a challenge: activation outliers make quantization difficult; it says mixed INT8/FP16 outlier handling can add latency overhead, potentially making inference slower than FP16.

## Source 3
id: https://arxiv.org/abs/2410.11305
url: https://arxiv.org/abs/2410.11305
title: QSpec: Speculative Decoding with Complementary Quantization Schemes
date: 2025-10-02
source: web
retrieved via: web_search
evidence type: paper abstract/full text excerpts from search result
 evidence excerpt: “The superior performance of QSpec relies on the high acceptance rate, particularly in small to moderate batch-size scenarios”
supported claims:
- QSpec combines low-precision drafting with higher-precision verification and reports shared weight/KV reuse.
- The retrieved paper text documents acceptance rate and serving regime as conditions affecting benefits; it flags potential limitations in single-request scenarios.
- It reports tree-based verification can scale poorly in batched serving and add compute and memory overhead. These are QSpec authors’ claims, not a general proof about every speculative method.

## Source 4
id: https://www.stat.berkeley.edu/~mmahoney/pubs/9485_QuantSpec_Self_Speculativ.pdf
url: https://www.stat.berkeley.edu/~mmahoney/pubs/9485_QuantSpec_Self_Speculativ.pdf
title: QuantSpec: Self-Speculative Decoding with Hierarchical Quantized KV Cache
date:
source: web
retrieved via: web_search
evidence type: paper abstract/full text excerpts from search result
evidence excerpt: “In long-context scenarios, however, the primary bottleneck shifts from model weights to the KV cache, which grows linearly with the context length.”
supported claims:
- QuantSpec targets long-context inference where KV-cache memory/latency is described as the bottleneck.
- The paper states sparse KV cache approaches can cause noticeable generation-quality degradation and draft/target mismatch, lowering acceptance rates.
- It describes quantized KV cache and self-speculation as its method; the excerpt does not establish broad comparative effectiveness outside its tested settings.

## Synthesis
The quantization papers illustrate distinct bottlenecks and tradeoffs: GPTQ compresses weights and reports memory-movement gains while explicitly not reducing computation; SmoothQuant addresses activation outliers with W8A8 transformations, while its retrieved discussion acknowledges accuracy and hardware-efficiency challenges in earlier outlier handling. Speculative decoding methods rely on draft acceptance and cheap verification; QSpec highlights batch-regime dependence and tree verification overhead. QuantSpec addresses a different long-context bottleneck, the growing KV cache, and notes that sparsification can degrade quality and acceptance. Results and limitations are author-reported and workload/hardware-specific. Primary evidence was retrieved through web search text rather than directly inspected full papers; exact performance claims should not be generalized. The requested small-language-model framing is only partially covered: these retrieved sources chiefly concern LLM inference efficiency, not a broad survey of SLM architecture/training.

## Gaps
- arxiv_search for foundational quantization/KV/speculative-decoding papers returned NO RESULTS. Per instructions, changed to web rather than repeating the failed query.
- The web search supplied useful primary-paper excerpts, but no standalone primary-source website pages were fetched; evidence is search-result excerpts. Metadata was incomplete for some PDFs; dates are left blank where not established by tool output.
- Foundational primary papers specifically on KV-cache paging/optimization (e.g. PagedAttention) and original speculative decoding were not retrieved in usable form; coverage of these categories is consequently incomplete.
- No small-language-model-focused primary source was retrieved, and recent-work coverage is selective rather than exhaustive.