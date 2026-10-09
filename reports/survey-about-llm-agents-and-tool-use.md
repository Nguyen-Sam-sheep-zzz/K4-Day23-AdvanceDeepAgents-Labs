# LLM Agents and Tool Use: From API Calls to Reliable Workflows

## TL;DR
- Tool-using agents rest on complementary ideas: modular routing to external capabilities, learned decisions about when/how to invoke APIs, and iterative action with observations that can revise a plan [1][2][3].
- The evidence does not support a single settled design. Recent work explores structured API representations for multi-call tasks, while evaluation benchmarks target lengthy procedures and coordination [4][5].
- In a benchmark using real MCP servers, schema comprehension and valid tool naming reportedly outpaced higher-order planning and reasoning; this is a result in that benchmark, not a universal ranking [6].
- Evaluation is shifting toward work-like and dynamic tasks, but much of the retrieved HF evidence is AI-generated summary material rather than inspected paper text [7][8][9][10][11].

## Background
Tool use extends a language model beyond its internal token-generation process by connecting it to external knowledge or operations. MRKL presents a modular architecture combining neural models with discrete knowledge and reasoning modules [3]. Toolformer frames API use as decisions about which API to call, when, arguments, and how results feed into later prediction [2]. These are distinct emphases: system modularity versus learning the invocation policy.

ReAct focuses on inference-time control, interleaving verbal reasoning and task actions so that interaction with external sources or environments can inform later steps [1]. Together, these foundational ideas motivate the familiar agent loop—choose an action, execute it, consume the observation, and continue—but they do not establish that a loop by itself guarantees correct or safe behavior [1][2][3].

## From invocation to multi-step tool control
The contemporary material is thinner on exact implementation details than the broad agent literature might suggest. An HF-generated summary for In-N-Out describes converting API documentation into structured graphs to improve tasks requiring multiple API calls [5]. This is evidence that structured representations are being explored, not a verified result about superiority over other schemas: the retrieved material is explicitly an AI-generated summary.

A complementary arXiv abstract for SOP-Bench characterizes complex, multi-step standard operating procedures as a difficulty for LLM agents and presents a benchmark of 2,000+ tasks across 12 business domains, described as human-validated [4]. Taken together, these sources suggest the design problem extends beyond emitting a syntactically valid call: agents must select and sequence operations within procedures. The available evidence does not let us compare structured API graphs, function-calling formats, or orchestration frameworks head-to-head [4][5].

## Evaluation beyond isolated calls
Recent benchmark material broadens the unit of evaluation from a single invocation to multi-turn and real-world workflows. ACEBench's HF summary describes tool-use evaluation across scenarios including multi-turn dialogue [7]; TheAgentCompany's dated HF-daily entry frames consequential work-related computer tasks [8]. MCP-Bench's inspected page describes tasks involving multi-step use, cross-tool coordination, parameter control, planning, and completion through real MCP servers [6]. These sources point toward measuring end-to-end task completion and coordination, rather than API syntax alone.

The strongest specific comparative finding in the retrieved evidence is benchmark-local: MCP-Bench reports that schema understanding and valid tool naming have largely converged across models, while higher-order reasoning and planning remain substantially weaker [6]. SOP-Bench independently foregrounds complex procedure execution as a challenge [4]. Neither establishes a universal capability threshold; task distributions, server conditions, and evaluation design constrain generalization [4][6].

## Interfaces, environments, and safety
Agent performance depends on the affordances and stability of the tools and interfaces, not only on the model's policy. An HF-daily summary for “Build the web for agents, not agents for the web” identifies a mismatch between human-designed interfaces and LLM capabilities [9]. The DR³-Eval HF summary flags dynamic web environments and ambiguous task definitions as evaluation challenges [10]. Because these are generated summaries, they support only cautious reporting of what those sources emphasize, not independently validated empirical conclusions.

Safety is also a tool-use concern: the HF-generated summary of Agent-SafetyBench characterizes its evaluation as revealing significant safety challenges and a need for improved reliability strategies [11]. This is a high-level summary, without details here about attack categories or measured rates. The available corpus therefore suggests that robust tool use must address interface design, changing environments, and safety, but does not permit a quantitative comparison across these risks [9][10][11].

## Trends and open problems
The retrieved sources suggest a move toward longer-horizon, realistic workflows and structured descriptions of tool capabilities: SOP-Bench targets complex procedures, MCP-Bench cross-tool tasks on live servers, and In-N-Out's summary describes API graphs for multi-call execution [4][5][6]. This trend is credible as a statement about the retrieved benchmark and dataset designs, not proof that such evaluations adequately represent deployment.

Several limitations remain. First, benchmark-specific findings may not transfer across domains or tool ecosystems [4][6]. Second, MCP-Bench's page itself flags live-server variation and reliance on a single LLM judge as reproducibility and judge-reliability concerns [6]. Third, HF-generated summaries dominate several recent records, so details and quantitative claims from ACEBench, interface-mismatch work, DR³-Eval, and Agent-SafetyBench cannot be established from the retrieved excerpts alone [7][9][10][11]. Finally, this search did not yield strong primary evidence directly comparing function-call schemas, agent orchestration strategies, or safety mitigations. Those are evidence gaps, not grounds to declare an approach ineffective.

## References
[1] ReAct: Synergizing Reasoning and Acting in Language Models. web. https://arxiv.org/abs/2210.03629 (2023-03-10)
[2] Toolformer: Language Models Can Teach Themselves to Use Tools. web. https://arxiv.org/abs/2302.04761 (2023-02-09)
[3] MRKL Systems: A modular, neuro-symbolic architecture that combines large language models, external knowledge sources and discrete reasoning. web. https://arxiv.org/abs/2205.00445 (2022-05-01)
[4] SOP-Bench: Complex Industrial SOPs for Evaluating LLM Agents. arxiv. https://arxiv.org/abs/2506.08119 (2025-06-09)
[5] In-N-Out: A Parameter-Level API Graph Dataset for Tool Agents. hf-search. https://huggingface.co/papers/2509.01560 (2025-12-30)
[6] MCP-Bench: Benchmarking Tool-Using LLM Agents with Complex Real-World Tasks via MCP Servers. web. https://www.emergentmind.com/papers/2508.20453 (2025-08-28)
[7] ACEBench: Who Wins the Match Point in Tool Usage?. hf-search. https://huggingface.co/papers/2501.12851 (2025-01-22)
[8] TheAgentCompany: Benchmarking LLM Agents on Consequential Real World Tasks. hf-daily. https://huggingface.co/papers/2412.14161 (2024-12-18)
[9] Build the web for agents, not agents for the web. hf-daily. https://huggingface.co/papers/2506.10953 (2025-06-12)
[10] DR³-Eval: Towards Realistic and Reproducible Deep Research Evaluation. hf-daily. https://huggingface.co/papers/2604.14683 (2026-04-16)
[11] Agent-SafetyBench: Evaluating the Safety of LLM Agents. hf-search. https://huggingface.co/papers/2412.14470 (2024-12-19)
