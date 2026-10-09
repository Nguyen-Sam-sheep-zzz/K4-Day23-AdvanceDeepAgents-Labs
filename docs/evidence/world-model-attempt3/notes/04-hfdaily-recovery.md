# Question
Topic: World models in AI/robotics.
Scope: Can a genuinely relevant paper surfaced in a historical Hugging Face daily papers list serve as direct evidence for a world-model survey (planning, predictive dynamics, evaluation, control), distinct from existing HF-search papers? Historical-list window: 2024-10-09 to 2026-10-09.
Source families attempted: hf-search, hf-daily.

## Source 1
id: 2605.00080
url: https://huggingface.co/papers/2605.00080
title: World Model for Robot Learning: A Comprehensive Survey
date: 2026-04-30
source: hf-search
retrieved via: hf_search_papers query “world models robotics predictive dynamics planning control evaluation”
evidence type: HF AI-generated summary
evidence excerpt: “World models as predictive representations of environmental dynamics have become essential for robot learning, supporting policy learning, planning, and simulation across various embodied applications.”
supported claims:
- The HF summary characterizes this survey as covering predictive environmental dynamics and applications to policy learning, planning, and simulation.

## Source 2
id: 2510.19818
url: https://huggingface.co/papers/2510.19818
title: Semantic World Models
date: 2025-10-22
source: hf-search
retrieved via: hf_search_papers query “world models robotics predictive dynamics planning control evaluation”
evidence type: HF AI-generated summary
evidence excerpt: “Semantic world models, trained as vision language models, improve policy generalization in robotics by predicting task-relevant semantic information instead of pixel reconstruction.”
supported claims:
- The summary says the method predicts task-relevant semantic information rather than reconstructing pixels, and reports improved policy generalization.

## Source 3
id: 2604.26694
url: https://huggingface.co/papers/2604.26694
title: Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising
date: 2026-04-29
source: hf-daily
retrieved via: hf_daily_papers(limit=100, date=2026-04-30, keyword="world model")
evidence type: HF AI-generated summary
 evidence excerpt: “X-WAM, a Unified 4D World Model that unifies real-time robotic action execution and high-fidelity 4D world synthesis”; “predicting multi-view RGB-D videos”
supported claims:
- The daily-list summary describes a system unifying robotic action execution with world synthesis and predicting multi-view RGB-D video.
- This is directly relevant to predictive dynamics and robotic control, though the summary alone does not establish empirical performance.

## Source 4
id: 2510.18135
url: https://huggingface.co/papers/2510.18135
title: World-in-World: World Models in a Closed-Loop World
date: 2025-10-20
source: hf-daily
retrieved via: hf_daily_papers(limit=100, date="2025-10-22", keyword="world model")
evidence type: HF AI-generated summary
evidence excerpt: “most existing benchmarks adopt open-loop protocols that emphasize visual quality in isolation, leaving the core issue of embodied utility unresolved”; “benchmarks WMs in a closed-loop”
supported claims:
- The summary identifies a limitation in open-loop evaluation and describes a platform for closed-loop evaluation of embodied utility.
- This is directly relevant evaluation evidence for a world-model survey; it is not itself proof that world models improve task success.

## Source 5
id: 2501.09038
url: https://huggingface.co/papers/2501.09038
title: Do generative video models learn physical principles from watching videos?
date: 2025-01-14
source: hf-daily
retrieved via: hf_daily_papers(limit=100, date="2025-01-17", keyword="world model")
evidence type: HF AI-generated summary
evidence excerpt: “Do video models learn ``world models'' that discover laws of physics -- or, alternatively, are they merely sophisticated pixel predictors”; “developing Physics-IQ, a comprehensive benchmark dataset”
supported claims:
- The summary frames physical-principle learning versus pixel prediction as an evaluation question and describes a benchmark intended to test physical understanding.
- This is relevant to predictive-dynamics evaluation, but is less directly about robotics/control than Sources 3–4.

## Synthesis
The dated daily lists surfaced three individually distinct papers with clear survey relevance: X-WAM connects predicted future observations to action execution; World-in-World addresses closed-loop embodied evaluation; Physics-IQ targets whether video models capture physical principles rather than merely predict pixels. These are meaningful direct sources for control, evaluation, and predictive-dynamics sections, and are distinct from the two HF-search records included here. Search-list items include a broad robotics survey and a semantic-prediction example, but summaries are not a substitute for paper text. All evidence here is HF-provided summary text (including AI-generated summaries), not independently inspected full text; claims about results, methods, or comparative performance should be verified in the papers.

## Gaps
- Daily-list attempts: 2026-04-30 (candidate date retrieved for 2605.00080; returned paper dated 2026-04-29, X-WAM); 2025-10-22 (candidate date retrieved for 2510.19818; returned World-in-World dated 2025-10-20); 2025-01-17 (candidate date retrieved for 2501.10100; returned Physics-IQ dated 2025-01-14). The tool returns dated-list results whose publication dates may differ from the requested list date; retained the tool output dates and did not infer exact list membership beyond the tool call.
- HF search outputs include an apparent date/id inconsistency for 2504.16680 (published 2026-01-08); this record was not used.
- No arXiv or web source was attempted; only HF search summaries and daily-list summaries are available. Full-text inspection is absent, so the substantive claims remain summary-only.
