# Conditional biomedical and machine-learning audit

Load only for biomedical, omics, or predictive-model studies. These are audit prompts, not findings about a manuscript. Sources verified 8 September 2026; recheck versions when applying a named standard. Distinguish missing reporting, demonstrable implementation defects, and limitations of the scientific claim.

## 1. Establish the question and applicable standard

Record population, prediction target, predictors, unit of observation, intended use, and evaluation setting. A normalization benchmark, biological discovery study, and clinical diagnostic model require different evidence.

- **TRIPOD+AI**, published **16 April 2024**, addresses reporting of clinical prediction models using regression or machine learning. Apply relevant items when that is the study's purpose; for a methodological subtype benchmark, explain any selected adaptation. Checklist completeness does not establish validity. [Official statement and supplement](https://www.tripod-statement.org/); [primary publication](https://doi.org/10.1136/bmj-2023-078378).
- **PROBAST+AI**, published **24 March 2025**, assesses quality, risk of bias, and applicability of healthcare prediction models. Keep model-development quality distinct from bias in performance evaluation. It is an appraisal tool, not a reporting checklist. For formal assessment, retrieve the actual tool and follow its signalling questions; do not invent an overall score. [Official tool](https://www.probast.org/); [primary publication](https://www.bmj.com/content/388/bmj-2024-082505).
- Route other study designs through the [EQUATOR library](https://www.equator-network.org/reporting-guidelines/). Do not impose PRISMA merely because a thesis has a literature-review chapter, or require clinical-deployment evidence for a claim restricted to a retrospective benchmark.

## 2. Cohort, labels, and independence

Request the cohort flow, exclusions, missingness, class counts, data release, accession/file identifiers, sample types, and label-source version. Reconcile participant counts with samples, aliquots, and analyzed rows. In TCGA, resolve the case/sample/aliquot hierarchy using metadata; a distinct file or aliquot is not automatically an independent participant. For new-patient prediction, keep all records from each participant together in both outer and inner splits. Check duplicate and near-duplicate records, repeated measures, sites, and batches against the intended generalization target. [GDC barcode hierarchy](https://docs.gdc.cancer.gov/Encyclopedia/pages/TCGA_Barcode/).

For expression-derived labels such as PAM50, inspect the precise label-generating pipeline, gene overlap, centroids, platform, preprocessing, and whether label generation used the full cohort. PAM50 originated as a 50-gene expression-based predictor; that does not identify how a particular downloaded annotation was produced. [Parker et al., 2009](https://pubmed.ncbi.nlm.nih.gov/19204204/).

**Audit inference:** Predicting such labels from expression can validly measure label reproduction. It does not independently establish biological truth, clinical utility, or prognosis. Shared predictor/label information warrants claim limits and, where useful, sensitivity analyses; it is not automatically train/test leakage or misconduct. Excluding the 50 genes alone cannot establish independence because correlated expression may remain. Investigate outcome access and label construction before assigning severity.

## 3. Trace preprocessing information flow

For every operation, record its inputs, learned state, labels accessed, fitting population, and application to unseen data.

- Fixed elementwise transforms, such as a prespecified log transform, and genuinely sample-local library-size operations need no cross-sample fitting. Their position before splitting alone does not prove leakage. Verify fixed gene definitions, denominators, and upstream processing.
- Cohort-estimated means/variances, quantile references, imputation, gene filtering, PCA, feature selection, batch correction, and estimated dispersion trends require scrutiny. For inductive evaluation, fit learned components within the relevant training partition and apply that state to validation/test data. Label-free does not mean leakage-free. [scikit-learn guidance](https://scikit-learn.org/stable/common_pitfalls.html#data-leakage).
- For DESeq2-style normalization/VST, inspect size-factor references, dispersion fitting, design information, and frozen application rather than judging by the method name or `blind` flag alone. The package documents reusing a fitted dispersion function on new samples. [DESeq2 manual](https://www.bioconductor.org/packages/release/bioc/manuals/DESeq2/man/DESeq2.pdf).

Explicitly declared transductive analysis may use unlabeled target-cohort information; evaluate it against that setting, and limit claims about isolated future samples. Unknown upstream normalization is an uncertainty to disclose, not proof of contamination.

## 4. Selection, comparisons, and uncertainty

When tuning and estimating performance on one dataset, check nested evaluation or a genuinely untouched test set. Include feature counts, preprocessing choices, class balancing, thresholds, early stopping, and model-family selection within the appropriate selection boundary. Fixed prespecified models do not automatically require an inner tuning loop. Inspect whether outer results later chose a winner whose same score is presented as independently validated. [Nested evaluation](https://scikit-learn.org/stable/auto_examples/model_selection/plot_nested_cross_validation_iris.html); [selection bias analysis](https://jmlr.org/papers/v11/cawley10a.html).

For algorithm-by-normalization comparisons, check shared splits, comparable tuning effort, appropriate scaling, convergence, failed runs, complete experiment coverage, prespecified primary contrasts, and interactions. Report effect sizes and per-class errors alongside aggregate metrics; justify averaging conventions and imbalance handling. Partial runs cannot support a complete ranking.

Do not treat overlapping CV folds or repeated predictions of the same patient as independent experimental replicates. Require uncertainty methods matched to the estimand and dependence structure; fold standard deviation is not automatically a confidence interval. State assumptions and multiplicity handling. A nonsignificant difference does not establish equivalence. [Bengio and Grandvalet, 2004](https://www.jmlr.org/papers/v5/grandvalet04a.html).

## 5. Bound claims and request proportionate repairs

Internal TCGA validation supports claims within its evaluated sampling setting. Cross-platform, institutional, temporal, or clinical claims need corresponding evidence; external validation is not universally mandatory for a bounded undergraduate benchmark. If probabilities or decisions are claimed, inspect calibration and decision relevance. Feature importance alone does not establish causation.

For each concern, identify the manuscript/code location, information path or unsupported inference, affected result, smallest sufficient repair, and evidence that would change the judgment. Prefer correcting claim scope when new experiments are unnecessary. Recommend costly reanalysis only when it resolves a material uncertainty.
