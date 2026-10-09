# Question
Topic: Survey of efficient inference and small language models.
Scope: Approaches producing capable small language models through distillation, data curation, training or architecture; prioritize 2024-10-09 through 2026-10-09, with foundational context where useful.
Source families attempted: arxiv, web, HF search.

## Source 1
id: 2508.09883
url: https://arxiv.org/abs/2508.09883
title: Beyond Scaling Law: A Data-Efficient Distillation Framework for Reasoning
date: 2025-08-13
source: arxiv
retrieved via: arxiv_search
 evidence type: paper abstract
 evidence excerpt: “we propose a data-efficient distillation framework (DED) that optimizes the Pareto frontier”
supported claims:
- The paper proposes a data-efficient distillation framework for reasoning. The retrieved abstract is truncated, so details and outcome evidence are not available here.

## Source 2
id: https://proceedings.neurips.cc/paper_files/paper/2024/file/4822991365c962105b1b95b1107d30e5-Paper-Conference.pdf
url: https://proceedings.neurips.cc/paper_files/paper/2024/file/4822991365c962105b1b95b1107d30e5-Paper-Conference.pdf
title: Compact Language Models via Pruning and Knowledge Distillation
date:
source: web
retrieved via: web_search
evidence type: paper full text (search-result extracted text)
evidence excerpt: “prune the Nemotron-4 15B model by a factor of 2-4×”
supported claims:
- The approach combines structured pruning and distillation-based retraining; the authors report producing 8B and 4B models from a 15B model.
- Authors report up to 40× fewer training tokens per derived model than training from scratch and 1.8× family training cost savings.
- The paper reports a limitation: techniques have only been applied to the Nemotron family, and still require full model retraining.

## Source 3
id: https://arxiv.org/html/2502.02737v1
url: https://arxiv.org/html/2502.02737v1
title: SmolLM2: When Smol Goes Big — Data-Centric Training of a Small Language Model
date:
source: web
retrieved via: web_search
evidence type: paper full text (search-result extracted text)
evidence excerpt: “we trained on 11 trillion tokens ... employing a multi-stage training approach”
supported claims:
- SmolLM2 is reported as a 1.7B-parameter model trained with a multi-stage mixture of web, math, code, and instruction data.
- The authors describe creating FineMath, Stack-Edu, and SmolTalk where they judged existing data small or low-quality.
- Dataset mixtures were adjusted based on benchmark performance, with specialized data upsampled in later stages.
- Authors note full-scale experimentation was costly (the retrieved text estimates around $250,000 GPU compute), motivating online mixture adjustment rather than multiple full runs.

## Source 4
id: https://aclanthology.org/2025.acl-industry.4.pdf
url: https://aclanthology.org/2025.acl-industry.4.pdf
title: DistilQwen2.5: Industrial Practices of Training Distilled Open Lightweight Language Models
date:
source: web
retrieved via: web_search
evidence type: paper full text (search-result extracted text)
evidence excerpt: “multi-agent teachers to select, rewrite, and refine instruction-response pairs”
supported claims:
- The approach augments instruction-response data using teacher-model agents and follows with supervised fine-tuning.
- It adds model fusion as white-box distillation after black-box data distillation; retrieved text describes matching token-level teacher/student distributions.
- The paper reports experiments with Qwen2.5 students sized 0.5B, 1.5B, 3B, and 7B, using larger teacher models.
- The excerpt does not provide quantitative benchmark results or detailed limitations, so no comparative magnitude is claimed here.

## Source 5
id: https://arxiv.org/pdf/2410.17215
url: https://arxiv.org/pdf/2410.17215
title: MINIPLM
date:
source: web
retrieved via: web_search
evidence type: paper full text (search-result extracted text)
evidence excerpt: “Difference Sampling ... down-samples easy and common patterns, up-samples hard and diverse instances”
supported claims:
- MINIPLM uses offline teacher inference and refines the pretraining corpus using differences between teacher and small reference model preferences.
- Authors report improvements on nine downstream tasks and a 2.4× reduction in data demand in their experiments.
- The paper states offline teacher inference allows reuse across multiple student models without additional training-time costs; the reported method still entails preprocessing/inference overhead.

## Source 6
id: https://aclanthology.org/2025.emnlp-main.376.pdf
url: https://aclanthology.org/2025.emnlp-main.376.pdf
title: Teach Small Models to Reason by Curriculum Distillation
date:
source: web
retrieved via: web_search
evidence type: paper full text (search-result extracted text)
evidence excerpt: “two-stage curriculum distillation framework”
supported claims:
- The method first trains implicit problem-solving heuristics and then teaches explicit reasoning articulation, using different teacher outputs by task difficulty.
- The authors report the two-stage approach consistently outperforms single-stage baselines on their mathematical reasoning benchmarks.
- Evidence is scoped to the described benchmark setup and 3B students; retrieved text does not establish broad general-purpose superiority.

## Synthesis
Recent approaches address capability at different stages: data curation and dynamic mixture design (SmolLM2), distillation and data selection (MINIPLM, DistilQwen2.5), curriculum design for reasoning transfer, and structural pruning followed by recovery training (MINITRON). Reported benefits are conditional on specific model families, datasets, benchmark suites, and compute setups. Distillation can reduce the burden of learning from scratch, while curated/targeted data and staged schedules are presented as important for small-model capability. The evidence retrieved is mostly author-reported experimental claims; comparisons across papers are not controlled or directly comparable. Full inference latency/energy comparisons are generally absent from the excerpts, so this is not a comprehensive efficient-inference comparison.

## Gaps
- HF search was attempted but returned no suitable in-scope paper: returned entries were either out of scope by date or not clearly about general-purpose small LMs. HF search tag therefore has no usable source.
- No usable arxiv abstract/full-text evidence was retrieved for the recent SLM work beyond the truncated DED abstract. MINIPLM was discovered via web search and retains the web tag.
- Search returned no publication dates for several web results; these are left blank rather than inferred.
- Web evidence came from search-result extracted paper text; no separate web_fetch inspection was completed. Quantitative claims above are only those explicitly present in retrieved excerpts.
