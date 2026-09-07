# Astra Skill Optimizer

A Hermes-native skill for auditing and refactoring agent skills for an observed Astra model/runtime while preserving capability, safety and compatibility.

This is an instruction workflow plus read-only measurement and validation helpers, **not an automatic rewriting engine**. No Astra-specific performance improvement has been benchmarked by this release. Model identity must be verified for each evaluation; no vendor affiliation is implied.

## Use

Install this directory through your Hermes skill installation workflow, then load `astra-skill-optimizer`.

- `audit <skill>` — read-only assessment.
- `optimize <skill>` — candidate, old/new evaluation and authorized activation.
- `batch <explicit targets>` — per-target gates, no implicit whole-library rewrite.

Example request: “Use astra-skill-optimizer to audit my reporting skill. Do not change live files.”

For changes, the workflow expects the `create-skill` and `shaw` governing skills in the consuming environment. They are not vendored here. Adapt governance explicitly if using another agent; this package does not install runtime integrations or modify profile configuration.

## Verify locally

Python 3.9+; standard library only:

```sh
python3 -B scripts/test_optimizer.py
python3 -B scripts/measure.py .
```

The measurement helper reports UTF-8 bytes, characters and SHA-256 for `SKILL.md` and reference Markdown. It does not estimate tokens, latency, cost or reasoning quality. Static tests validate package contracts and helper behavior, not model performance. See [evaluation protocol](references/evaluation.md) for behavioral evaluation requirements.

No CI workflows are included. Tests are run locally and from a fresh clone before publication is reported complete.

## Safety

No network calls, provider spending or automatic installation in the helper scripts. Preserve source corpora and local overlays; require explicit scope for writes and protected effects. Never include private conversations, credentials or live payloads in benchmark fixtures.

## Contents

- `SKILL.md`: workflow and boundaries.
- `references/evaluation.md`: old/new protocol and synthetic cases.
- `scripts/measure.py`: read-only instruction measurement.
- `scripts/test_optimizer.py`: six deterministic tests, including negative cases.
