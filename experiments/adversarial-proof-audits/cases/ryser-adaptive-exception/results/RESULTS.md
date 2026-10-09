# Blinded results

Thirty independent GPT-5.6 Sol (`gpt-5.6-sol`) audits were run, ten per
condition.

| Condition | Audits judging the proof correct | Mean correctness probability |
|---|---:|---:|
| Original manuscript | 10/10 | 0.8250 |
| Semantics-preserving edit | 10/10 | 0.8400 |
| Adaptive-exception defect | 3/10 | 0.2610 |

Seven defect audits localized the invalid application of an "all but five
lines" bound to every line in an adaptively chosen cover. Three audits missed
the gap and judged the corrupted proof correct with probabilities `0.88`,
`0.76`, and `0.86`.
