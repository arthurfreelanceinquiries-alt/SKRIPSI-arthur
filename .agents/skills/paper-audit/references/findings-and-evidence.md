# Findings and evidence

## Keep three dimensions separate

Severity is consequence **if the finding is correct**:

| Severity | Use when |
|---|---|
| Critical | A demonstrated defect defeats a central result or makes its present interpretation untenable. Use sparingly. |
| Major | A material design, evidence, analysis, or reporting problem could change interpretation or prevent assessment. |
| Minor | A local correctness/clarity defect with limited effect on the conclusions. |

Classification describes the evidence state:

- **Definite error:** direct contradiction, a reproducible calculation, or clear source evidence establishes the defect under stated assumptions.
- **Unsupported claim:** the supplied evidence does not warrant the strength or scope of the claim. This does not establish that the claim is false.
- **Likely issue:** a concrete concern has support but unresolved context could change the finding.
- **Needs verification:** necessary external evidence, source context, data, or method detail is unavailable.

Confidence can be high, moderate, or low, with a short justification if it helps. Do not equate it with severity or invent numerical probabilities. Put very uncertain suspicions in questions, not in a list of established errors. Record extraction uncertainty separately from scientific uncertainty.

## Finding record

For each material finding provide:

1. Stable ID and descriptive title; severity and classification.
2. Exact location: file/version and source line, page plus section/table/equation, or an identifiable short quotation. Distinguish PDF page index from printed page labels. Never invent line numbers.
3. Evidence: the manuscript statement and the contradicting or missing support. Cite both sides of an internal mismatch. For a calculation show inputs, concise method and result. For an external check cite the specific source passage or page actually read.
4. Why it matters to this work's stated objective.
5. Smallest adequate fix or the evidence needed to resolve it. Distinguish a reporting clarification from a necessary reanalysis and an optional future experiment. Do not supply fabricated replacement results.

Example: `F001 | Major | Definite error | Results, Table 2 and abstract: the reported count is 42/60 but the abstract calls this 80%; 42 ÷ 60 × 100 = 70%. Correct the percentage after confirming the denominator; this changes the headline performance claim.`

Compact proofing entries need location, defect, and correction; repeated instances can be grouped. Do not label an entire study invalid because one caption is wrong.

## Verification of sources

Use original studies, official method documentation, data records, and applicable standards closest to the claim. A search snippet or DOI resolving successfully does not establish support. Open the source, match authors/title/year/identifier where relevant, then assess the exact statement, population, outcome, setting, method, and uncertainty. Distinguish full text from abstract-only access and peer-reviewed articles from preprints.

Prioritize central/controversial claims, method justifications, surprising numbers, and suspected citation mismatches. For a full bibliography audit record each entry's status; for a sample explicitly state the boundary. Check corrections/retractions when relevant and accessible. A failed lookup means unverified, not fabricated. Shared citations or copied summaries are not independent corroboration. No assertion of exhaustive novelty without a reproducible search boundary and its limits.

Minimize external query disclosure. Search bibliographic metadata or generalized methods instead of unpublished manuscript passages or private data. Respect any known venue restrictions for confidential third-party peer review; check applicable rules when this is the actual task. Do not introduce venue approval steps into review of the user's own thesis.

## Evidence ledger and final audit

For substantial reviews maintain a compact table: claim/finding ID; manuscript locator; supporting source/locator; access level; check performed; conclusion; unresolved dependency. Record source retrieval dates separately from publication dates when time matters. Keep user facts, observations, inferences, and assumptions distinguishable.

Before delivery check that every material finding has accessible support and a feasible correction; every high-risk uncertainty is either resolved or explicitly retained; duplicate findings are merged; and coverage statements match actual work. Do not include internal chain-of-thought. Provide concise justifications, calculations, and an auditable evidence trail.
