# Question
Topic: LLM agents and tool use
Scope: Foundations plus relevant framing through 2026-10-09; prioritize original papers.
Source families attempted: arxiv, web (publisher/project pages)

## Source 1
id: 2210.03629
url: https://arxiv.org/abs/2210.03629
title: ReAct: Synergizing Reasoning and Acting in Language Models
date: 2023-03-10
source: web
retrieved via: web_search
 evidence type: paper abstract
 evidence excerpt: “ReAct prompts LLMs to generate both verbal reasoning traces and actions pertaining to a task in an interleaved manner”
supported claims:
- ReAct interleaves reasoning traces and task-specific actions.
- Reasoning updates plans, while actions interact with external sources/environments for information.

## Source 2
id: 2302.04761
url: https://arxiv.org/abs/2302.04761
title: Toolformer: Language Models Can Teach Themselves to Use Tools
date: 2023-02-09
source: web
retrieved via: web_search
evidence type: paper abstract
 evidence excerpt: “decide which APIs to call, when to call them, what arguments to pass, and how to best incorporate the results into future token prediction.”
supported claims:
- Tool use can be learned self-supervised from API demonstrations.
- Its framing explicitly handles tool choice, timing, arguments, and incorporation of outputs.

## Source 3
id: 2205.00445
url: https://arxiv.org/abs/2205.00445
title: MRKL Systems: A modular, neuro-symbolic architecture that combines large language models, external knowledge sources and discrete reasoning
date: 2022-05-01
source: web
retrieved via: web_search
evidence type: paper abstract
 evidence excerpt: “a flexible architecture with multiple neural models, complemented by discrete knowledge and reasoning modules.”
supported claims:
- MRKL frames tool use as a modular architecture mixing language models and discrete reasoning/knowledge components.
- The abstract presents this as a systems response to limits of language models.

## Synthesis
These sources foreground complementary foundations. MRKL describes a modular systems view: route work among neural and discrete experts. Toolformer focuses on learning the decision to call APIs and use their results. ReAct emphasizes runtime control: interleave reasoning, actions, and environmental observations so plans can be revised. Together they ground current tool-using agents in external capability access, action selection, and feedback-informed iteration; they are not identical methods or evidence of a single settled architecture. Evidence here is abstracts and search-returned paper text rather than independent replication. The ReAct abstract also identifies prompting limitations, so a loop alone does not guarantee robust planning.

## Gaps
- Initial arxiv_search for ReAct-related terms returned NO RESULTS; a changed broad query succeeded, returning mostly 2026 papers. These were not used as foundational evidence.
- Web search supplied paper abstracts and excerpts, but no separate publisher/full-text inspection was completed. Arxiv as a retrieval source-family tag was attempted but did not yield the used sources; usable source tags are web only.
- Coverage of planning and environment feedback rests especially on ReAct; additional foundational planning frameworks and detailed full-text methods were not inspected.
