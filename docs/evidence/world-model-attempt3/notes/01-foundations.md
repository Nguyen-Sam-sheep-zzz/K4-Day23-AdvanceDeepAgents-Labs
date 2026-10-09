# Question
Topic: world models in AI/robotics
Scope: Foundations plus evidence relevant through 2026-10-09, emphasizing last two years when pertinent.
Source families attempted: arXiv, web, HF search (additional discovery); arXiv and web required families both retrieved.

## Source 1
id: 2606.00133
url: https://arxiv.org/abs/2606.00133
title: World Models: A Comprehensive Survey of Architectures, Methodologies, Reasoning Paradigms, and Applications
date: 2026-05-28
source: arxiv
retrieved via: arxiv_search; web_fetch
 evidence type: paper abstract/full text
 evidence excerpt: “World models, internal simulators that learn the structure and dynamics of an environment” and “enabling agents to predict, plan, and reason within learned representations.”
supported claims:
- This survey frames world models as learned internal simulators supporting prediction, planning, and reasoning.
- It organizes architectures, methodologies, reasoning strategies, and application domains into separate dimensions, rather than treating “world model” as one architecture.
- Its abstract flags compounding prediction errors, sim-to-real transfer, and fragmented evaluation as persistent challenges.

## Source 2
id: https://arxiv.org/html/2607.00836
url: https://arxiv.org/html/2607.00836
title: From World Models to World Action Models: A Concise Tutorial for Robotics
date: 
source: web
retrieved via: web_search; web_fetch
evidence type: paper full text
 evidence excerpt: “a world model predicts how future observations ... or states ... evolve under candidate actions”; “A world model does not, by itself, constitute a policy or controller.”
supported claims:
- World models can predict observations or states conditioned on candidate actions, in observation or state space, and may predict trajectories.
- Latent dynamics and direct observation-space generation are representational choices; the tutorial presents neural dynamics, symbolic equations, and diffusion video prediction as possible model forms.
- Prediction is distinct from decision/control: planning, policy, or controller mechanisms consume predictive capability; a world action model instead couples future modeling with action generation and need not retain a separate model at inference.
- The source cautions that action-conditioned predictions may support MPC, evaluation, or synthetic data, depending on the interface and representation.

## Source 3
id: https://dl.acm.org/doi/10.1145/3746449
url: https://dl.acm.org/doi/10.1145/3746449
title: Understanding World or Predicting Future? A Comprehensive Survey of World Models
date: 2025-09-09
source: web
retrieved via: web_search; web_fetch
evidence type: website text
 evidence excerpt: “Generally, world models are regarded as tools for either understanding the present state of the world or predicting its future dynamics.”
supported claims:
- The survey explicitly presents two conceptual emphases: internal representations that capture mechanisms/world knowledge and prediction of future states to simulate and guide decisions.
- It describes the definition as debated, rather than asserting a single settled boundary.
- Its account of latent representations describes retaining key information while filtering redundancies to support decision-making and planning.

## Synthesis
Across these sources, the most operationally useful framing is predictive: a world model estimates task-relevant future states/observations given present information and, commonly, candidate actions. Learned latent dynamics compress observations and allow prediction or imagination without requiring pixel-level outputs; observation-space/video predictors are another architecture, not a necessary definition. Planning is a use of prediction, not synonymous with the predictive model: a planner/policy evaluates rollouts or otherwise maps information to action. Some architectures integrate these functions, but the distinction remains important. Definitions are not fully uniform: the ACM survey includes a broader “understand the present” perspective, while the robotics tutorial centers action-conditioned future evolution. The 2026 arXiv survey likewise emphasizes internal simulation and decision support. Architecture labels therefore do not by themselves demonstrate controllability, planning utility, or reliable real-world transfer.

## Gaps
- HF search returned relevant papers, but was supplementary and not used as evidence; no HF daily attempt was assigned or necessary.
- arXiv_search yielded one relevant survey result; further primary foundational papers were not independently retrieved in this run. The 2026 survey provides historical discussion, but those cited works should not be treated as directly retrieved sources here.
- ACM and tutorial material are reviews/tutorials, not independent experimental demonstrations. The source record for the tutorial provides no publication date; left blank.
- The arXiv survey was fetched as an abstract page with substantial introduction text; claims above rely on its returned abstract/introduction excerpt, not an exhaustive technical review.
