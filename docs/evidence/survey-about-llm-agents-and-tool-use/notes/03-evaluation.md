# Question
Topic: LLM agents and tool use.
Scope: 2024-10-09 through 2026-10-09.
Source families attempted: hf-search, hf-daily via dated lists, arxiv, web.

## Source 1
id: 2508.20453
url: https://www.emergentmind.com/papers/2508.20453
 title: MCP-Bench: Benchmarking Tool-Using LLM Agents with Complex Real-World Tasks via MCP Servers
 date: 2025-08-28
source: web
retrieved via: web_search and web_fetch
 evidence type: website text (paper abstract/full paper text reproduced)
evidence excerpt: “Schema understanding and valid tool naming have largely converged across models ... However, substantial gaps persist in higher-order reasoning and planning”; “experiments on 20 advanced LLMs” and “104 MCP-Bench tasks.”
supported claims:
- MCP-Bench assesses multi-step tool use, cross-tool coordination, parameter control, planning, and task completion using real MCP servers.
- In this benchmark, basic schema/tool-name compliance was stronger than higher-order planning.
- This source's page reports use of live servers and one LLM judge, and flags reproducibility/judge-reliability concerns in its limitations section.

## Source 2
id: 2501.12851
url: https://huggingface.co/papers/2501.12851
title: ACEBench: Who Wins the Match Point in Tool Usage?
date: 2025-01-22
source: hf-search
retrieved via: hf_search_papers
 evidence type: HF AI-generated summary
 evidence excerpt: “ACEBench is a comprehensive benchmark for evaluating tool usage in Large Language Models across various scenarios, including multi-turn dialogues.”
supported claims:
- HF's summary describes evaluation across multiple tool-use scenarios including multi-turn dialogue.
- Since the excerpt is an AI-generated paper summary, it is not direct evidence of paper-specific empirical details.

## Source 3
id: 2412.14161
url: https://huggingface.co/papers/2412.14161
title: TheAgentCompany: Benchmarking LLM Agents on Consequential Real World Tasks
date: 2024-12-18
source: hf-daily
retrieved via: hf_daily_papers(date=2024-12-19, limit=100, keyword=agent)
evidence type: HF AI-generated summary
evidence excerpt: “how performant are AI agents at helping to accelerate or even autonomously perform work-related tasks?”
supported claims:
- The dated daily list included a benchmark focused on consequential work-related computer tasks.

## Source 4
id: 2506.10953
url: https://huggingface.co/papers/2506.10953
title: Build the web for agents, not agents for the web
date: 2025-06-12
source: hf-daily
retrieved via: hf_daily_papers(date=2025-06-13, limit=100, keyword=agent)
evidence type: HF AI-generated summary
evidence excerpt: “current approaches face substantial challenges due to the fundamental mismatch between human-designed interfaces and LLM capabilities.”
supported claims:
- The daily-list summary highlights interface mismatch as a challenge for web agents.

## Source 5
id: 2604.14683
url: https://huggingface.co/papers/2604.14683
title: DR³-Eval: Towards Realistic and Reproducible Deep Research Evaluation
date: 2026-04-16
source: hf-daily
retrieved via: hf_daily_papers(date=2026-04-17, limit=100, keyword=agent)
evidence type: HF AI-generated summary
evidence excerpt: “evaluation remains challenging due to dynamic web environments and ambiguous task definitions.”
supported claims:
- The summary identifies dynamic environments and ambiguous task definitions as evaluation challenges for deep-research agents.

## Source 6
id: 2412.14470
url: https://huggingface.co/papers/2412.14470
title: Agent-SafetyBench: Evaluating the Safety of LLM Agents
date: 2024-12-19
source: hf-search
retrieved via: hf_search_papers
evidence type: HF AI-generated summary
evidence excerpt: “revealing significant safety challenges and emphasizing the need for advanced strategies to improve agent reliability.”
supported claims:
- The HF summary reports significant safety challenges in its agent-evaluation setting.

## Synthesis
Across the retrieved evidence, tool-use evaluations are expanding beyond isolated calls toward multi-turn, cross-tool, real-world workflows. MCP-Bench's inspected page suggests that selecting valid tools and conforming to schemas can be substantially easier than long-horizon planning and orchestration. HF summaries add concerns about ambiguous interfaces, dynamic environments, and safety, but they are only summaries and do not independently establish quantitative findings. Evaluation itself remains fragile: live-server variation and judge validity/reproducibility need to be treated as part of benchmark reliability, not assumed away. Results are benchmark-specific; these sources do not establish universal agent performance or a single robust ranking.

## Gaps
- HF daily initial/latest-list attempt was not made; historical assignment implemented by first searching HF papers and using three dates returned in search results.
- Dated daily attempts: 2026-01-03, keyword=agent, limit=100 → NO RESULTS; 2024-12-19, keyword=agent, limit=100 → results; 2025-06-13, keyword=agent, limit=100 → results; 2026-04-17, keyword=agent, limit=100 → results. Relevant records were obtained on all three distinct historical dates; the NO RESULTS attempt was an additional candidate date.
- Search results gave dates for three candidate papers used for daily-list dates, but daily papers returned on adjacent publication dates; no URL duplication among usable daily sources.
- arxiv_search returned results, but retrieved results did not include a clearly relevant empirical evaluation paper; no arXiv source included.
- The OpenReview web result was a browser-verification page, not usable research evidence.
- ACEBench and safety evidence is HF AI-generated summaries only; no complete primary paper text inspected for those claims.
