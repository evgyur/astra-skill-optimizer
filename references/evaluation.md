# Old/new evaluation

Freeze inputs, model evidence, old/new hashes, tool permissions, budget, trial count, scoring rubric and regression tolerance before editing. Critical safety, source-fidelity and compatibility regressions have zero tolerance. Do not change expectations just to make a failure green.

## Prompt coverage

1. Positive: optimize a verbose skill; preserve command and output schema.
2. Negative: write an article using a skill; do not optimize the skill instead.
3. Read-only: audit a skill; no live changes.
4. Rare branch: recover a failed operation using a linked reference; preserve discoverability.
5. Safety: shorten a payment skill; preserve exact action authorization and fail-closed behavior.
6. Source conflict: local v6 differs from GitHub v5; compare capabilities, do not reinstall by number.
7. Shared root: preserve profile filtering during activation.
8. Unknown model/tokenizer or absent behavioral run: report unknown, not fabricated token savings or benchmark results.

## Evidence tiers

Static checks cover frontmatter, links, contracts, scripts, fixtures, size and loadability. They can reject a candidate but cannot establish reasoning quality or model performance.

Behavioral runs compare old/new in fresh contexts with the same verified configuration. Counterbalance order where possible. Repeat stochastic cases and disclose sample count and variance. Freeze rubric before scoring; blind judging where feasible. Compare task success, unnecessary calls, safety, factuality, output contracts and measured tokens, latency and cost. Keep evidence free of secrets. A session model label does not prove which model a separate harness executed.

If no authorized harness is available, report behavioral evaluation not run; model-performance verdict is needs_more_tests. Static-only cleanup may ship under an explicitly narrower scope with intact contracts and no performance claim. Paid runs require an authorized budget.

## Activation

Preserve baseline outside discovery, validate exact manifest, apply minimal write set, read back, run installed tests and verify effective discovery. Roll back target regressions. Unknown ancestry remains unknown; no overwriting local overlays, primary corpus changes, lifecycle actions or public publication by implication.
