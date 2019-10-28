**Highly unusual mutations** are defined as amino acids with an overall group M
prevalence <0.01% that do not have a mutation penalty score in the HIVDB
genotypic resistance interpretation program and that are not
[signature APOBEC mutations](/page/apobecs/).

## Steps and Criteria
First we calculate the prevalence of an amino acid at a position:

1. Same amino acid at the same position from a single person is only
   counted once. (`PATIENT_PER_MUT_COUNT`)
2. Multiple Amino acids at the same position from a single sample are not
   counted. (`EXCLUDE_MIXTURES`)
3. Stop codons are not counted. (`EXCLUDE_STOP_CODONS`)
4. Sequences only used in unpublished studies are not used. (`PUBLISHED_ONLY`)
5. DNAChip Sequences are not used. (`NO_DNACHIP`)
6. Sequences with quality issues are not used. (`NO_QA_ISSUES`)

In general, an amino acid at a position with its prevalence < 0.01% is
considered unusual, with the following exception:

- The amino acid is a known drug resistance mutation according to latest HIVDB algorithm.

## Sequence QA Criteria

A sequence falls in either of the conditions below is filtered.

| Gene | APOBEC cutoff | Score cutoff | Min AA   | Max AA |
|------|---------------|--------------|----------|--------|
| PR   | >=2           | >=4          | >=31     | <=89   |
| RT   | >=3           | >=6          | >=66     | <=214  |
| IN   | >=3           | >=5          | >=67     | <=154  |


Score cutoff: the "score" here is defined as the total number of problematic mutations.
A problematic mutation is defined either an APOBEC mutation or an unusual mutation.

## Subtype and treatment distribution

|           | PR     | RT     | IN    |
|-----------|--------|--------|-------|
| # Total   | 186116 | 189748 | 22868 |
| # B       | 102435 | 100064 | 12615 |
| # Non-B   | 83681  | 89684  | 10253 |
| % Treated | 15.86% | 58.14% | 6.69% |
