# Independent claim audit

Audit date: 2026-10-09. These checks reopen actual citation URLs using the host `web_fetch` tool, independently of the lead's checker. They are spot checks, not reproduction of experiments or exhaustive factual validation. Saved fetch text is in the topic evidence directory. Reports and sources are never edited during this audit.

## World model attempt 3 (archived)

Archived artifacts: `world-model-attempt3/artifacts/survey-about-world-model.*`; 12 sources; four retrieval tags; host citation validator OK. Seven cited URLs were reopened. This audit applies to the earlier attempt, superseded by attempt 4 below.

| Exact report claim (abridged) | Citation | Retrieved evidence | Assessment |
|---|---|---|---|
| World models are internal simulators supporting prediction, planning and reasoning. | 1 | Abstract: "internal simulators that learn the structure and dynamics of an environment" and "predict, plan, and reason within learned representations". | Supported |
| FLIP combines flow action proposals, flow-conditioned video dynamics and a value component. | 3 | Abstract explicitly lists these three modules. | Supported |
| AdaWorld extracts latent actions from video in a self-supervised way, then conditions an autoregressive world model on them. | 4 | PMLR abstract explicitly states both steps. | Supported |
| WorldPrediction reports 57% on world modeling and 38% on procedural planning, with perfect human performance. | 5 | Abstract states "57% accuracy on WorldPrediction-WM and 38% on WorldPrediction-PP whereas humans ... solve both tasks perfectly". | Supported as the paper's benchmark-specific report |
| WorldModelBench collects 67K human labels and evaluates 14 frontier models. | 6 | Abstract and Figure 2 state both counts. | Supported |
| World-in-World uses closed-loop evaluation and prioritizes task success. | 8 | Paper abstract on HF describes closed-loop environments and task success as the primary metric. | Supported |
| X-WAM predicts multi-view RGB-D video while unifying action execution and world synthesis. | 10 | Retrieved abstract explicitly states these components. | Supported as a system description |

Limits: several source records rely on HF summaries; the report labels this limitation. Dates follow retrieved API/search metadata, which can describe a version or indexing date rather than first publication. The Background uses retrieved surveys/tutorials instead of directly citing an early foundational paper. The report has some repeated FLIP/AdaWorld discussion between themes; these remain quality risks for human grading. Metadata was produced by the runner version immediately before successful-result counters were added; no values were backfilled. Four genuine researcher note files were preserved, and two checker task requests are recorded in metadata.

## Reinforcement learning for LLM reasoning

Artifacts: `reports/survey-about-reinforcement-learning-for-llm-reasoning.*`; 12 sources; four tags; host citation validator OK. Three successful researchers and one successful checker; initial batch of three. Seven source URLs were reopened, without changing report/source hashes.

| Report claim (abridged) | Citation | Retrieved evidence | Assessment |
|---|---|---|---|
| RLHF combines a reward model and PPO policy optimization. | 1 | Abstract explicitly describes reward models measuring preferences and PPO optimizing outputs. | Supported |
| R1-Zero uses GRPO and final-prediction correctness rewards without constraining reasoning. | 2, 3 | Nature text states GRPO and "correctness of final predictions ... without imposing constraints on the reasoning process". | Supported |
| Formal proof checking in Lean provides a clear signal for RL theorem proving. | 5 | Seed-Prover abstract describes Lean formal verification enabling effective RL training. | Supported as the source's method description |
| One RLVR study reports sampling efficiency improvements but rarely new reasoning patterns. | 6 | Abstract states both points; its Figure 1 distinguishes pass@1 from pass@256. | Supported as that study's conclusion |
| School of reward hacks is SFT evidence, not an RL experiment. | 7 | Text states "We used supervised fine-tuning" and identifies the SFT dataset. | Supported |
| Production-RL reward hacking is associated with increased misalignment in the study's runs. | 8 | Text states misalignment rapidly increases when hacking is learned, and does not increase in runs without learned hacking. | Supported within the tested setting |

Limits: the retrieved Nature excerpt is truncated before the cold-start, inference-allocation and overthinking discussion; those details were not independently revalidated in this spot-check. The report labels HF-generated summary evidence and avoids a universal causal claim about reward hacking. One web date is month precision (`2025-11`), not a independently confirmed exact publication day.

## LLM agents and tool use

Artifacts: `reports/survey-about-llm-agents-and-tool-use.*`; 11 sources; four tags; host citation validator OK. Three successful researchers and one successful checker; initial batch of three. Six URLs reopened without changing submitted hashes.

| Report claim (abridged) | Citation | Retrieved evidence | Assessment |
|---|---|---|---|
| ReAct interleaves reasoning traces and task-specific actions. | 1 | Abstract explicitly states an interleaved generation of both. | Supported |
| Toolformer learns which APIs to call, when, arguments and use of results. | 2 | Abstract explicitly lists these decisions. | Supported |
| MRKL combines neural models and discrete knowledge/reasoning modules. | 3 | Abstract and introduction describe neural models, symbolic modules and routing among experts. | Supported |
| SOP-Bench contains 2,000+ tasks across 12 business domains. | 4 | Abstract states these counts and human validation. | Supported as the benchmark's description |
| MCP-Bench reports convergence in schemas/tool naming but gaps in higher-order planning. | 6 | Emergent Mind page explicitly states both findings and limits them to its benchmark. | Supported by the cited secondary page; not primary-paper replication |
| TheAgentCompany evaluates consequential work-related computer tasks. | 8 | HF paper abstract describes computer tasks simulating real-world work environments. | Supported |

Limits: the recent evidence is partly summary/secondary material. Exact comparisons between schemas and orchestration strategies are not established; the report explicitly discloses this gap. Retrieval dates for revised papers are not guaranteed to be their initial publication dates.

## Video and multimodal generation: attempt 2 audit failure

The structurally accepted attempt had 14 sources and four tags. Seven URLs were reopened. Two claims failed independent verification: Background described VideoGPT as a retrieved primary excerpt but cited Video Diffusion Models [2], whose fetched excerpt does not mention VideoGPT; the audio section described DreamFoley but cited WorldSonus [9], whose fetched page does not mention DreamFoley. This archived report was rejected and superseded by attempt 3. Its untouched artifacts were archived in `video-attempt2/artifacts/`; a full system rerun with factual-review feedback resolved the defects. No report/source text was edited on the host.

## Video and multimodal generation: final attempt 3

Artifacts: `reports/survey-about-video-and-multimodal-generation.*`; 12 sources; four tags; validator OK. Four successful researcher returns and one successful checker; initial batch of three. Seven current citation URLs were reopened. This attempt supersedes attempt 2 entirely.

| Final report claim (abridged) | Citation | Retrieved evidence | Assessment |
|---|---|---|---|
| VideoGPT uses 3D convolutions/axial attention for discrete video latents and a GPT-like autoregressive prior. | 1 | Actual VideoGPT abstract explicitly describes these components. | Supported; earlier wrong-source citation resolved |
| Video Diffusion Models uses temporal diffusion and joint image/video training. | 2 | Primary text states 3D U-Net diffusion and joint training objectives. | Supported |
| DreamFoley uses an autoregressive VLM for video-to-audio generation with video/audio/text conditioning. | 7 | Actual DreamFoley abstract states these components. | Supported; earlier wrong-source citation resolved |
| FoleyBench finds poor audio-visual correspondence in 74% of past evaluation videos. | 8 | Abstract states 74% and explains its evaluation-dataset scope. | Supported as the authors' finding, not all video data |
| In-Flight KV Cache reuses cache to avoid cache-update-only forward passes. | 9 | HF paper abstract explicitly describes this mechanism. | Supported as a method description |
| PEBench evaluates text-to-video, image-to-video and reference-to-video prompt enhancement. | 11 | Retrieved abstract lists all three conditioning modes. | Supported |

The draft's 10-second DreamFoley limit was absent from the finalized URL's accessible excerpt. The system checker removed it from the final report, explicitly explaining that it was not verified. Limits: the study is not a unified cross-model comparison; several recent records use HF summaries, and dates can refer to revisions/indexing. These limitations are acknowledged in the report.

## Efficient inference and small language models

Artifacts: `reports/survey-about-efficient-inference-and-small-language-models.*`; 18 sources; three tags (`web`, `hf-search`, `hf-daily`); validator OK. Four successful researchers and one successful checker; initial batch of three. Seven URLs reopened at normal tool length, plus extended source text for GPTQ, QSpec and MINIPLM obtained through the same host Exa API. Longer text is saved as `*-extended.txt`; no report/source file was edited.

| Final report claim (abridged) | Citation | Retrieved evidence | Assessment |
|---|---|---|---|
| GPTQ uses approximate second-order quantization, and its speedup stems from memory movement rather than fewer computations. | 1 | Abstract describes second-order information; extended limitations section explicitly states reduced memory movement and no computational reductions. | Supported |
| Pruning/distillation derives 8B and 4B models from a pretrained 15B model. | 3 | Abstract explicitly names these three sizes. | Supported within the paper's model family |
| SmolLM2 has 1.7B parameters and multi-stage training on 11 trillion tokens. | 4 | Paper abstract and training section state both numbers. | Supported |
| The pruning/quantization study evaluates six SLMs, seven languages, 710 evaluations and one A100. | 5 | Abstract/methods state all counts and the A100 setting. | Supported; final report retains diminished advantage on complex tasks |
| QSpec combines low-precision drafting and higher-precision verification, with workload-dependent gains. | 8 | Paper describes the schemes; extended Section 7.2 explicitly discusses high acceptance and small/moderate batches. | Supported; final report avoids a general performance guarantee |
| SmoothQuant reports up to 1.56× speedup and 2× memory reduction and migrates activation difficulty to weights. | 11 | Abstract explicitly states the numbers and mathematically equivalent transformation. | Supported as paper-specific results |
| MINIPLM reports reducing data demand by 2.4 times. | 14 | Extended paper introduction states 2.4 times and identifies preprocessing teacher cost. | Supported as an experimental result |

Limits: the report draws from heterogeneous models/hardware and author-reported results, not a reproduced serving benchmark. Exact dates are unavailable for some web records. The three truthful tags satisfy the rubric; arXiv-domain pages discovered through web remain `web`, not falsely labeled `arxiv`.

## World model final attempt 4

Artifacts: `reports/survey-about-world-model.*`; 14 sources; four tags; validator OK. Four successful researchers and one successful checker; initial batch of three. Seven finalized URLs reopened. The earlier report was replaced only through a fresh system run, with a directly retrieved seminal paper and less duplicated method discussion.

| Final report claim (abridged) | Citation | Retrieved evidence | Assessment |
|---|---|---|---|
| World Models combines visual compression, recurrent dynamics and a controller, including training in a generated dream. | 1 | Primary paper describes the recurrent world model/controller and transferring a dream-trained policy to the actual environment. | Supported |
| Dreamer learns with analytic value gradients through imagined latent trajectories. | 2 | Abstract explicitly states this procedure. | Supported |
| DayDreamer learns online on four physical robots without simulators. | 3 | Abstract states "apply Dreamer to 4 robots ... without any simulators". | Supported |
| EnerVerse-AC uses action conditioning and ray-map encoding for multi-view generation. | 5 | Abstract explicitly describes both mechanisms. | Supported |
| WorldPrediction reports 57% and 38% for its world-modeling/procedural-planning tasks. | 7 | Abstract states both benchmark-specific numbers and perfect human performance. | Supported as the source's results |
| WBench uses 22 automatic sub-metrics validated against human judgments. | 8 | Abstract states the count, validation and no universally strong model across dimensions. | Supported |
| WorldTest separates reward-free interaction from a scored test in a related environment. | 9 | Abstract explicitly states this protocol. | Supported |

Limits: results remain paper-reported, and recent HF items remain summary-level. Benchmark protocols differ, so this survey does not rank models across incomparable tasks. Publication/version/indexing dates are retained as retrieved rather than independently normalized.
