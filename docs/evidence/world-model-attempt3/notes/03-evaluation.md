# Question
Topic: World models in AI/robotics
Scope: Foundations plus last two years through 2026-10-09; evaluation evidence, limitations, and open problems concerning generalization, long-horizon consistency, action controllability, physical grounding, and benchmarks.
Source families attempted: hf-search, hf-daily, web

## Source 1
id: 2607.02642
url: https://huggingface.co/papers/2607.02642
title: GigaWorld-1: A Roadmap to Build World Models for Robot Policy Evaluation
date: 2026-07-02
source: hf-search
retrieved via: hf_search_papers query “world models robotics evaluation generalization long horizon consistency controllability physical grounding benchmark”
evidence type: HF AI-generated summary
evidence excerpt: “long-horizon rollout consistency and robot-specific controllability are more important than short-term visual realism”
supported claims:
- The summary reports a benchmark study emphasizing long-horizon consistency and robot-specific controllability in policy evaluation.
- Evidence is summary-only; this excerpt does not establish the study's detailed methodology or numerical results.

## Source 2
id: 2606.31672
url: https://huggingface.co/papers/2606.31672
title: WorldOdysseyBench: An Open-World Benchmark for Long-Horizon Stability of Interactive World Models
date: 2026-07-02
source: hf-search
retrieved via: hf_search_papers query “world models robotics evaluation generalization long horizon consistency controllability physical grounding benchmark”
evidence type: HF AI-generated summary
evidence excerpt: “evaluates interactive world models across action, vision, physics, and memory dimensions”
supported claims:
- The summary identifies four evaluation dimensions and states that the benchmark is designed to reveal failures missed by traditional benchmarks.

## Source 3
id: 2605.08567
url: https://huggingface.co/papers/2605.08567
title: ACWM-Phys: Investigating Generalized Physical Interaction in Action-Conditioned Video World Models
date: 2026-05-09
source: hf-search
retrieved via: hf_search_papers query “video world models action-conditioned robotics benchmark”
evidence type: HF AI-generated summary
evidence excerpt: “models performing better on simple geometric interactions than complex deformable contacts.”
supported claims:
- The summary indicates performance varies with physical regime and task complexity, with complex deformable contact a weak case.

## Source 4
id: https://openaccess.thecvf.com/content/CVPR2026W/GigaBrainChallenge/papers/Jiang_RoboWM-Bench_A_Benchmark_for_Evaluating_World_Models_in_Robotic_Manipulation_CVPRW_2026_paper.pdf
url: https://openaccess.thecvf.com/content/CVPR2026W/GigaBrainChallenge/papers/Jiang_RoboWM-Bench_A_Benchmark_for_Evaluating_World_Models_in_Robotic_Manipulation_CVPRW_2026_paper.pdf
title: RoboWM-Bench: A Benchmark for Evaluating World Models in Robotic Manipulation
date: 
source: web
retrieved via: web_search
 evidence type: website text (paper text returned by search)
evidence excerpt: “visual realism does not imply physical plausibility”
supported claims:
- The paper presents an embodiment-grounded benchmark that converts video behaviors into actions and validates execution.
- Its retrieved text reports failures in spatial reasoning, contact stability, and physical realism.
- It reports that success rates decrease as task complexity increases and that manipulation-data fine-tuning improves executability, although inconsistencies remain.

## Source 5
id: https://arxiv.org/html/2606.31672v3
url: https://arxiv.org/html/2606.31672v3
title: WorldRoamBench: An Open-World Benchmark for Long-Horizon Stability of Interactive World Models
date: 2026-07-06
source: web
retrieved via: web_search
evidence type: website text
 evidence excerpt: “none reliably satisfies all dimensions; even the best achieves only moderate scores.”
supported claims:
- The benchmark evaluates action following, visual drift, interaction physics, and memory under continuous long-horizon interaction.
- The retrieved text says existing methods can miss per-frame action failures and long-horizon quality collapse.
- It describes action imprecision as a confound for memory evaluation and action fidelity as distinct from visual quality.

## Source 6
id: https://arxiv.org/pdf/2601.04137
url: https://arxiv.org/pdf/2601.04137
title: WoW-World-Eval (title not provided in retrieved output)
date: 
source: web
retrieved via: web_search
evidence type: website text
 evidence excerpt: “visual realism alone is insufficient for embodied execution.”
supported claims:
- Retrieved text reports evaluation of generalization, planning, prediction, and execution in a robotics benchmark.
- It reports limitations in long-horizon planning, physical consistency, and execution, based on the returned text; numerical figures in that text are not independently verified here.

## Source 7
id: https://arxiv.org/html/2607.02642v1
url: https://arxiv.org/html/2607.02642v1
title: GigaWorld-1: A Roadmap to Build World Models for Robot Policy Evaluation
date: 
source: web
retrieved via: web_search
evidence type: website text
 evidence excerpt: “preserve actionable state information under repeated autoregressive feedback”
supported claims:
- The returned text says generic video models can suffer viewpoint drift, object-identity collapse, texture accumulation, and late-stage degradation during long rollouts.
- It identifies robot-specific controllability and persistent memory as relevant to reliable policy evaluation.

## Source 8
id: https://arxiv.org/html/2605.29360
title: MiraBench: Evaluating Action-Conditioned Reliability in Robotic World Models
url: https://arxiv.org/html/2605.29360
date: 
source: web
retrieved via: web_search
evidence type: website text
evidence excerpt: “visual fidelity is a poor proxy for action fidelity”
supported claims:
- The retrieved text describes evaluation of physics adherence, action-following fidelity, and optimism bias.
- It reports that model scale does not reliably improve action following and that optimism bias is prevalent, according to the returned text.
- It states scope limitations (tabletop, short-horizon contact dynamics) and proposes broader domains as future extensions.

## Synthesis
The sources converge on a central evaluation problem: visually convincing prediction is not sufficient evidence of a useful world model. Benchmark evidence emphasizes executing generated or conditioned behaviors, faithful action response, physical plausibility, and sustained consistency over extended rollouts. RoboWM-Bench and the interactive-benchmark text identify contact/spatial failures, increased difficulty with task complexity, action errors, drift, and memory confounds. MiraBench's reported hierarchy distinguishes physical coherence from action sensitivity and preserving failure outcomes, addressing optimism in simulated futures. GigaWorld-1 and WorldOdysseyBench summaries likewise foreground controllability, memory, and long-horizon stability. Generalization is named as a test dimension in the WoW-World-Eval text, but the excerpts provide less detail about robust out-of-distribution evidence than about action and physical grounding. These findings should be treated cautiously: much evidence is search-result text or HF-generated summaries rather than inspected full papers; benchmark protocols and model-dependent findings are not directly comparable.

## Gaps
- Historical HF daily attempts (limit=100): 2026-07-02, keyword “world model” — returned ABot-M0.5 and Valdi; neither directly supplies the cited evaluation findings, so not used as evidence. 2026-10-06, keyword “world model” — returned World Editing, HLA-WM, and MM-ABC; not used because the results do not directly address the benchmark evidence needed here. 2026-05-09, keyword “world model” — NO RESULTS. Retried the same retrieved candidate date 2026-05-09 with keyword “robotics” — NO RESULTS. Replaced that date with candidate date 2026-03-26 (retrieved from HF search), keyword “world model” — returned Pulse of Motion and PhyGenesis; neither directly matched the needed evaluation evidence. Additional distinct date 2026-05-01 (retrieved from HF search), keyword “world model” — returned a general visual-generation survey, not a directly usable benchmark source. No irrelevant daily listings cited.
- HF daily contributes no directly usable source tag for this question despite historical list retrieval; requirement to retrieve relevant candidates by HF search and inspect three lists was attempted, with dated gaps stated above.
- Web results were available, but no web_fetch full-text inspection was performed. Exact bibliographic dates/titles were absent in some returned excerpts; blank dates are left blank, and title wording is marked when not provided.
- No foundational pre-2024 source was retrieved; evidence mainly concerns 2025–2026 benchmarks and evaluations.
