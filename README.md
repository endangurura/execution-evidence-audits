# Execution evidence for research audits

Can independently collected execution evidence help AI auditors distinguish valid
research from misleading results, beyond reviewing code or choosing their own
short experiments?

**Status:** Technical design in progress. No study runs, empirical results,
preregistration, or independent validation are claimed. This repository currently
contains an original methodological specification, an audit-response schema, and
related-work notes. It is not an implemented experiment runner or an upstream
benchmark release.

**Researcher:** Emmanuel Ndangurura.

## Technical question

The proposed comparison uses the same auditor under three observation settings:

| Condition | Auditor access |
| --- | --- |
| Static review | Paper and code, with no experiment execution |
| Active audit | Paper and code plus auditor-chosen short experiments |
| Fixed evidence | Paper and code plus a standardized packet collected by a separate execution process |

The primary comparison is fixed evidence versus active audit. Evidence collection
is charged to the method's resource use, not treated as free. A separate collector
can faithfully record a misleading computation; provenance is not a correctness
verdict.

The initial setting is a proposed replication/extension of
[Auditing Sabotage Bench](https://arxiv.org/abs/2604.16286). The extension concerns
the fixed, label-blind evidence packet, not a claim to have invented execution-based
auditing. There is no live attacker or model-training experiment in this study.

The current pilot focuses on three codebases: `awareness`, `diffuse`, and `chain`,
covering evaluation awareness, sandbagging detection, and chain-of-thought
monitorability. The [methodology](docs/methodology.md) distinguishes this selected
pilot from a possible broader study.

## Contents

- [Methodology](docs/methodology.md): comparison, evidence boundary, measurement,
  and limitations.
- [Audit response schema](schemas/audit_response.schema.json): proposed structured
  output contract, not a correctness scorer.
- [Related work](docs/related_work.md): primary research and separately labeled
  practitioner perspectives.
- [Publication policy](docs/publication_policy.md): material suitable for this repository.

Hosted model access and isolated execution are the intended research route; local
open-weight resources can support development and separately documented smaller
experiments. Endpoints and revisions must be fixed within each comparison. No
provider, model family, or local/hosted equivalence is presumed validated.

## Interpretation

A useful result could be positive, negative, or inconclusive. Artificial benchmark
sabotage does not establish spontaneous deception, real-world prevalence, or
oversight that scales to more capable systems. Small, correlated samples and
possible pretraining contamination limit conclusions.

Future empirical claims belong here only with an inspectable method, accounting
of all attempts, uncertainty, and an accurate statement of review/reproduction
status. No third-party codebases, papers, answer keys, or model traces are included
in this initial technical release.

## Validation

The checks below validate the proposed response schema, not scientific findings
or an experiment runner:

```sh
python3 -m pip install -r requirements-dev.txt
python3 -m unittest discover -s tests -v
```

## License

© 2026 Emmanuel Ndangurura.

Licensed under the [Apache License 2.0](LICENSE).
