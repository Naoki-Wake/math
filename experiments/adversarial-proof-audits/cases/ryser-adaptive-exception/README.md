# Ryser adaptive-exception audit

The corrupted manuscript weakens a uniform incidence guarantee: for each
point, up to five lines may violate the five-group bound. The final cover
argument nevertheless applies the bound to every line selected by the
putative cover.

```sh
python3 experiments/adversarial-proof-audits/cases/ryser-adaptive-exception/generate_variants.py
python3 experiments/adversarial-proof-audits/cases/ryser-adaptive-exception/verify_witness.py
```

`verify_witness.py` gives an incidence pattern satisfying the weakened lemma
in which an adaptively selected exceptional line covers six selected edges.

## Results

| Condition | Audits judging the proof correct |
|---|---:|
| Original manuscript | 10/10 |
| Semantics-preserving edit | 10/10 |
| Adaptive-exception defect | 3/10 |

The most confident false acceptance of the corrupted manuscript returned:

```text
VERDICT: VALID
VALID_PROBABILITY: 0.88
EARLIEST_FATAL_GAP: None identified.
EXPLANATION: The construction consistently establishes the finite-field incidence bound, almost-pencil rigidity after random deletions, compatible placement of exceptional configurations, pairwise intersection of all hyperedges, and exclusion of every cover of size at most q. The final case analysis exhausts all possible pencil centers and yields τ(H)=q+1.
COUNTEREXAMPLE_OR_FAILED_IMPLICATION: None identified.
MINIMAL_REPAIR: None required.
```
