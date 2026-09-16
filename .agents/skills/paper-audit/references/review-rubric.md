# General review rubric

Select checks by research question, design, and stage. Record not-applicable items only when they clarify coverage. A checklist omission is not automatically a scientific error.

## Question, contribution, and inference

- Does the objective define what will be learned, for whom or what, and under which conditions? Does the design answer that question?
- Trace the claimed contribution to an observable result, argument, method, or synthesis. Separate novelty, usefulness, and correctness. A replication or bounded undergraduate comparison can be worthwhile without a new algorithm.
- Compare abstract, introduction, results, discussion and conclusion. Check causal language against identification assumptions, controls, confounding and alternative explanations. Distinguish absence of evidence from evidence of no effect.
- Examine whether limitations actually qualify the headline claims and whether contrary evidence is considered fairly.

## Design and analysis

- Define population, sampling frame, inclusion/exclusion, independent unit, controls/comparators, outcomes and operational definitions. Check selection, attrition, measurement and confounding risks in context.
- Track sample counts and denominators through exclusions and analyses. Check missing-data handling, dependence, multiplicity, subgroup exploration, prespecified versus post hoc choices, uncertainty, effect size and practical meaning.
- Ask whether model/test assumptions match the data and estimand. Lack of statistical significance does not demonstrate equivalence; repeated measurements are not automatically independent replicates. Do not require a particular test without establishing why it applies.
- For qualitative work examine sampling rationale, researcher position, collection and coding procedure, interpretive traceability, counterexamples and limits of transfer. Do not impose power calculations or quantitative metrics on every design.
- For literature syntheses distinguish systematic review from narrative review. For systematic claims check search dates/queries, eligibility, screening, extraction, study quality and synthesis method; verify the relevant current reporting guidance. A thesis background chapter is not automatically a systematic review.

## Mathematics, algorithms, and quantities

- Check definitions, units/dimensions, domains, assumptions, limiting cases, signs, factors, normalization, uncertainty propagation, and numerical examples where relevant.
- Track frequently used notation from first definition to later uses, including verbal role descriptors such as initial/final or source/target. Inspect derivations and appendices explicitly when they support the core result.
- Check branch/quadrant conventions only where applicable. `arctan(y/x)` can be valid on a stated restricted domain. Do not replace it mechanically with `atan2`: establish coordinate orientation, arguments, range, and special cases first.
- For algorithms distinguish what is mathematically defined from what a reader could implement. Compare pseudocode, equations, stopping rules, parameter definitions and code when supplied.
- Recalculate consequential arithmetic and table totals. Preserve decimal-comma conventions, units, rounding and denominator definitions. A different metric aggregation can explain an apparent mismatch.

## Results, visuals, and reproducibility

- Align text with tables, figures, captions and supplements. Inspect axis scales, units, legends, denominators, error-bar definitions, sample sizes and whether plots support the stated comparison. Extraction alone may lose these details.
- Identify versions, data provenance, preprocessing, parameters, randomization/seeds and computational resources needed to reproduce the claim. Repository availability is not evidence that code ran or results reproduce.
- Distinguish code inspection, a small executed check, full computational reproduction and independent replication. Report exactly which occurred. Availability restrictions may justify controlled access; do not demand release of sensitive data.
- Compare plans/protocols with reported analyses where supplied. Label deviations and selective reporting concerns with evidence, not speculation about intent. The [COS TOP guidance](https://www.cos.io/initiatives/top-guidelines) provides a transparency framework; apply relevant disclosure/verification ideas without claiming its policies bind every thesis.

## Citations, ethics, and writing

- Verify central citation support and bibliography metadata at the declared scope. Check broken cross-references, duplicate entries and quotation accuracy.
- Flag evidence of unattributed copying or integrity concerns carefully. Text similarity, conventional phrasing or AI-like style does not prove plagiarism, fabrication or authorship. No detector percentage establishes misconduct.
- Check consent, approval, data access and conflicts disclosures only as relevant to the actual design and governing requirements. Secondary/public data do not automatically prove either an exemption or an approval requirement.
- Correct wording that changes meaning, inconsistent terminology, ambiguous antecedents and conspicuous proofing defects. Keep stylistic preferences separate from necessary corrections. Use the author's vocabulary and applicable disciplinary conventions.
