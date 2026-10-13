# Related work

These sources motivate the question. They are not findings from this study and do
not establish that the proposed evidence packet works.

## Primary research

- **[Auditing Sabotage Bench](https://arxiv.org/abs/2604.16286)**, Gan et al., 2026.
  Evaluates detection and repair of deliberately introduced flaws in ML research
  codebases. This is the closest benchmark. The proposed extension compares a fixed
  label-blind evidence packet with auditor-selected experiments.
  [Upstream implementation](https://github.com/ejcgan/auditing-sabotage-bench).
- **[Automated Researchers Can Mitigate Well-Characterized Alignment Failures](https://alignment.anthropic.com/2026/automated-alignment-researchers/)**,
  Chen, Wen, and Kirchner, 2026. Reports useful automated research alongside detected
  cheating that was excluded. This motivates checking research integrity, not a
  claim that the reported mitigation results are invalid.
- **[Training a Misaligned Reward Seeker](https://alignment.anthropic.com/2026/reward-seeker/)**,
  Anthropic, 2026. A deliberately constructed reward-hacking training study reports
  concerning generalization and important limits, including no evidence of research
  sabotage or beyond-episode reward seeking in its tests. It is not a population
  estimate for deployed assistants.
- **[The Hugging Face incident and the road ahead](https://openai.com/index/hugging-face-incident-and-the-road-ahead/)**,
  OpenAI, August 2026. The official account describes misaligned actions during
  internal cybersecurity evaluations under reduced safeguards. It motivates
  independent observation and containment but does not validate this audit method
  or make the present study a reproduction of that incident.

## Practitioner perspectives

These essays and guidelines provide research motivation and operational context.
They are not independent validation of this study. Connections to the proposed
experiment below are our interpretation, not endorsements by the authors.

- **[An Alien Mind](https://openai.com/index/an-alien-mind/)**,
  Jakub Pachocki, OpenAI, September 6, 2026. Frames alignment as a generalization
  problem and argues that confidence in monitoring should constrain further
  scaling. Reports diminishing reliance on chain-of-thought monitoring as models
  and environments change. This motivates empirical tests of complementary
  evidence channels; it is a strategic essay informed by internal findings, not
  a reproducible evaluation of execution-evidence auditing.
- **[The case for reasoning transparency](https://institute.deepmind.com/essays/the-case-for-reasoning-transparency/)**,
  Rohin Shah and Anca Dragan, DeepMind Institute, September 16, 2026. Argues for
  measuring and preserving readable reasoning, including scrutiny of training
  incentives and architectures that could weaken it. Treats chain-of-thought
  monitoring as useful but incomplete. The essay reflects the authors' views,
  not Google's official position. It motivates complementary observations, not
  a claim that execution records replace access to reasoning or activations.
- **[Towards safety cases for frontier AI training](https://openai.com/index/towards-safety-cases-for-frontier-ai-training/)**,
  OpenAI, September 28, 2026. Proposes safeguards including immutable transcripts,
  held-out monitoring evaluations, independent challenge of safety arguments,
  and actionable incident response. This supports keeping evidence outside an
  agent's control and making claims inspectable. These are evolving guidelines
  for frontier reinforcement learning, not proof of safety or an established
  standard that this small audit experiment satisfies.
- **[The Urgency of Interpretability](https://darioamodei.com/post/the-urgency-of-interpretability)**,
  Dario Amodei, April 2025. Makes the case for accelerating mechanistic understanding
  so that model problems can be diagnosed alongside behavioral testing. Provides
  a broader motivation for complementary sources of evidence. Its proposed
  interpretability capabilities and timelines are aspirations, not demonstrated
  guarantees; this study does not perform a mechanistic audit of model internals.
- **[Intentionally designing the future of AI](https://goodfire.com/blog/intentional-design)**,
  Thomas McGrath, Goodfire, February 5, 2026. Proposes using interpretability to
  understand and steer what training teaches a model, rather than relying only on
  retrospective evaluations. Distinguishes changing learned behavior from merely
  suppressing one observable representation. This is a research agenda, not
  evidence that generalization is fully controllable. Developing new training
  interventions or representation-level monitors is outside this study; the
  selected pilot instead reproduces existing research, including activation probing.
- **[Eric Ho on technical alignment](https://x.com/eric_ho/status/2105359054763880598)**,
  September 30, 2026. Presents Goodfire's interpretability-centered research thesis.
  That is a strategic perspective, not proof that interpretability is necessary or
  sufficient for this audit task. Monitoring the auditing models' activations is
  outside this study; reproducing the `diffuse` codebase's activation-probe
  experiments is part of the selected pilot.
- **[Joe on agent security and safety](https://x.com/joedaroo/status/2104335929293127851)**,
  September 28, 2026. Advocates evidence outside an agent's control, layered controls,
  and collaboration between security and safety. The author explicitly speaks in a
  personal capacity, not on behalf of OpenAI; use official reports for incident facts.

Sources checked October 1, 2026. This is a targeted reading list, not a systematic
literature review or endorsement from any cited author or organization.
