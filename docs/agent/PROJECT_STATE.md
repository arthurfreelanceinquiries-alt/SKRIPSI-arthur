# Project State — Skripsi Arthur

Last verified: 2026-11-24 (WIB)
Status: manuscript current; D45 instrument patch applied and verified on the live form; recruitment still blocked.

## Canonical project

- Repository root: this directory (`.`).
- Model: Hedonic Motivation, Desire for Completeness, Speculative Motive → Impulsive Buying; Self-Control moderator.
- Sample wording: minimum 111 respondents.
- Instrument: 27 first-order items (Y6, X1-5, X2-5, X3-5, M6), plus consent, 4 screening items, and 6 profile items.

## Verified instrument state (2026-11-24)

- `forms.get` revisionId **0000002c** after the D45 patch (was `0000002b`).
- Content: 50 items, 13 sections, 38 questions, 27 Likert items. One item added (`P3a`), none removed, routing unchanged.
- S3 uses the inclusive "minimal salah satu" wording with explicit option labels.
- P5 lists marketplace first, with named platforms.
- P3a records the form of West Jakarta linkage and is optional.
- Response sheet: 39 columns, header row only (no responses collected). Sheets appends new questions at the far right, so P3a sits in the last column, not beside P3.
- `emailCollectionType`: DO_NOT_COLLECT. `isAcceptingResponses`: true.

## Current gates

- Candidate rc2 content alignment: PASS limited, inherited from verified review.
- D45 instrument patch (S3 wording, P5 order, P3a addition): **applied and verified live** on the retained live form.
- Public form title no longer carries an "rc2 / Draf Privat" label; no edit was needed.
- Privacy, contact, raw-data access, retention, and age-17 institutional rules: **open**.
- Three-versus-four screening wording reconciliation in the manuscript: **open**.
- X3 wording: verified aligned with Tabel 3.2 as a first-person adaptation; the previously reported order mismatch was not confirmed against the current manuscript and is retracted.
- Publication, recruitment, and participant response collection: **blocked** pending the open gates above.

## Git caution

A pre-existing untracked Google Forms automation script exists. It was not executed. The applied patch used a separate reviewed path and the Forms API; do not treat the old automation script as reviewed or authorized.
