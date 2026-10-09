# Adversarial proof audits

This directory is a reusable framework for testing whether a model can
distinguish valid mathematical manuscripts from minimally corrupted matched
controls.

## Layout

```text
adversarial-proof-audits/
├── README.md
├── CASE_TEMPLATE.md
└── cases/
    └── <paper>-<mutation>/
        ├── README.md
        ├── audit-prompt.txt
        ├── generate_variants.py
        ├── verify_witness.py
        ├── generated/
        │   ├── ground_truth.json
        │   └── doc-*/manuscript.txt
        └── results/
```

Each case owns its source transformation, blinded assignment, mathematical
ground-truth witness, fixed audit prompt, and results. New papers and new
mutation types are added as sibling directories under `cases/`; they do not
require changes to existing cases.

## Design requirements

Every case should include:

1. an original manuscript condition;
2. a semantics-preserving matched control;
3. at least one intentionally corrupted condition;
4. an executable or independently checkable witness showing why each
   corruption is fatal;
5. seeded blind document identifiers;
6. the same number of independent audits per condition;
7. a prespecified localization criterion, so a lucky invalid verdict does not
   count as detection.

Generated manuscripts must remain clearly contained within this experimental
fork and branch. Do not submit intentionally corrupted manuscripts upstream.

## Current cases

| Case | Paper | Mutation |
|---|---|---|
| `ryser-adaptive-exception` | A counterexample to Ryser's covering conjecture | Weaken a uniform incidence bound before an adaptive cover choice |
