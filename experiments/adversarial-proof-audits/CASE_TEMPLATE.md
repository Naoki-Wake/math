# Case title

## Research question

State the precise audit capability being tested.

## Conditions

| Condition | Description | Expected verdict |
|---|---|---|
| Original | Released manuscript | VALID |
| Matched control | Semantics-preserving edit | VALID |
| Corruption | Minimal fatal semantic mutation | INVALID |

Use equal numbers of independent evaluator contexts for every condition.

## Ground truth

Describe the earliest failed implication and provide a finite witness,
formal-checker failure, counterexample, or other independently reproducible
certificate.

## Detection criterion

Specify the exact location and mathematical relationship an evaluator must
identify. An unlocalized invalid verdict is not a successful detection.

## Files

```text
README.md
audit-prompt.txt
generate_variants.py
verify_witness.py
generated/ground_truth.json
results/RESULTS.md
```
