# Methodology

**Status:** Proposed exploratory method. Not preregistered or executed.

## Comparison

For an identical paper/code snapshot, compare a static auditor (T), an auditor
selecting its own bounded experiments (X), and an auditor receiving a fixed
execution-evidence packet (E). The primary contrast is E minus X; E minus T is
secondary. A no-audit reference identifies the failures that receive no scrutiny.

Use the same model, instructions, inference limits, and artifact within each paired
comparison, apart from the observation/tool access under test. Repeat across two
model families if feasibility supports it. Pin model revisions or record provider
aliases and timestamps where immutable revisions are unavailable. Provider/model
changes require a separate block or amended comparison, not silent substitution.

This is a comparison of audit packages: a fixed collection recipe versus adaptive
experimentation. It does not isolate provenance alone. X may discover evidence
that a fixed packet misses; E may cost more than the improvement warrants.

## Evidence boundary

Freeze the collection recipe using development artifacts only. Candidate contents
are entry-point execution summaries, effective configuration, runtime errors,
input/output digests, and bounded intermediate/result summaries. Apply identical
collection and packaging rules to all classes.

Exclude answer keys, reference correctness judgments, counterpart diffs, identifying
variant names, and grading rubrics from the auditor's workspace and evidence packet.
Preserve these separately for reference checking. Physical access separation is
required; ignoring files in Git does not isolate them from a model or process.

An independent collector is a separate execution/logging boundary, not an oracle.
Treat code, logs, and packet text as untrusted observations. Never execute a
suggested action merely because it appears in those observations. Run untrusted
code in an approved isolated environment without production mounts, credentials,
or unrestricted network access. A model API key belongs outside that environment.

## Sample and references

The initial target is the published benchmark's nine codebase lineages, with three
for development and six for evaluation. Keep related variants together. This split
is a proposal, not a frozen dataset; feasibility and rights checks must precede
selection. Do not choose inclusions after seeing audit performance.

Use independently checked reference behavior and rubric-based human adjudication.
Mark unresolved references as unresolved. Record disagreement, blinding limits,
and exclusions. A sole model judge is not ground truth. Codebase is the dependency
cluster; seeds and multiple variants are not independent new research tasks.

Auditors return a suspicion probability, one primary diagnosis/location, and one
proposed fix using the [response schema](../schemas/audit_response.schema.json).
An abstention remains an abstention, not a zero suspicion score. A suggested fix
is not a demonstrated repair unless separately executed and checked.

## Measurement

The proposed primary statistic is E minus X in codebase-weighted AUROC, separately
for each auditor. Average repeated scores within an artifact first; give codebases
equal weight within each class. The exact weighting and implementation require
tests before evaluation. No AUROC scorer is implemented in this repository yet.

Secondary measurements include benign false alarms, missed verified modifications
under a fixed review queue, primary-diagnosis agreement with the reference rubric,
coverage, latency, tokens, GPU/CPU time, and human review minutes. Report collector
cost both without reuse and under a declared reuse assumption. If resource use
cannot be matched, report a cost/performance comparison instead of equal-cost claims.

Pair comparisons by codebase, artifact, model, and repeated audit. Preserve all
attempts, errors, timeouts, exclusions, and retries. Missing evidence is not evidence
of safety. Show complete-case results alongside sensitivity to missing outputs;
never choose a favorable retry or silently discard failed calls.

With six evaluation clusters, emphasize paired plots, absolute counts, and
leave-one-codebase-out sensitivity. Any bootstrap interval is exploratory and may
be unstable. This design is not a precise test of small effects or broad transfer.

## Limits

- Public benchmark material may have appeared in pretraining. Locally held-out
  codebases are not guaranteed globally unseen.
- Deliberately modified artifacts do not estimate natural failure prevalence or
  demonstrate spontaneous deceptive intent.
- Static T is more restrictive than an upstream mode that permits limited code
  execution. This is not an exact reproduction of upstream frontier-model scores.
- Detection after execution is not prevention. Signatures, digests, and isolation
  cannot establish that an underlying scientific conclusion is correct.
- No increasing capability gap or optimization-pressure sweep is included.
  A successful comparison would not establish scalable oversight on its own.
- Hosted and local results are distinct conditions unless equivalence is tested;
  provider nondeterminism and unavailable revisions limit reproduction.

Release only original or rights-cleared methodology, code, and findings. Do not
redistribute upstream protected rubrics or evaluation material through this repo.
