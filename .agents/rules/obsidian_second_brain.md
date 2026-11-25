# Rule: Obsidian Second Brain & Session Synchronization Protocol

This workspace is integrated with Obsidian as a **Second Brain** for thesis research (skripsi). `AGENTS.md` remains the canonical session and safety contract. Use this rule only when the active task needs Obsidian, Graphify, research history, or when Arthur explicitly requests Second Brain work.

## 1. Task-Relevant Pre-Flight
When this rule is relevant:
1. **Inspect Git State Without Mutation:**
   - Inspect the current branch, `git status --short`, and recent commits. Never auto-run `git pull`, reset, clean, checkout, commit, or push; synchronize only with Arthur's explicit authorization after preserving dirty work.
2. **Inspect Graphify Knowledge When Needed:**
   - Check `graphify-out/` (`manifest.json` / `GRAPH_REPORT.md`) only for tasks involving codebase relationships, research entities, or file dependencies.
3. **Inspect Second Brain Dashboard When Needed:**
   - Read relevant sections of `00_DASHBOARD_SECOND_BRAIN.md` for research status, constructs, supervisor feedback, or open research tasks. Prefer `docs/agent/PROJECT_STATE.md` and current source files when stale dashboard text conflicts.
4. **Session Alignment:**
   - Proceed under the active task in `.agent/CURRENT_TASK.md`; do not emit a readiness-only turn when work can continue safely.

## 2. In-Flight Documentation (Purpose-Driven Notes)
Whenever creating or editing markdown notes in this vault:
1. **Mandatory Top Summary:**
   Every documentation, concept note, PRD, or bimbingan record must start with an Obsidian callout:
   ```markdown
   > [!SUMMARY] Tujuan & Solusi Catatan Ini
   > - **Untuk Apa:** [Purpose]
   > - **Masalah yang Diselesaikan:** [Problem Solved]
   > - **Keputusan/Output:** [Core Decision / Artifacts]
   ```
2. **Bidirectional Linking:**
   Connect concepts, theories, supervisors, and variables using `[[Wikilinks]]`.

## 3. Auto-Capture & Session End (Mandatory Update Rules)
Whenever a key milestone, decision, revision, or insight occurs:
1. **Source of Truth Synchronization (MANDATORY):**
   - Whenever a new methodological decision, parameter change, hypothesis refinement, or supervisor directive (from Dr. Fredella Colline / examiners) occurs, the assistant MUST record a new canonical decision entry (`D31`, `D32`, etc.) in `04_Riset_&_Metodologi/SOURCE_OF_TRUTH.md` with date, rationale, and academic justification. Never let `SOURCE_OF_TRUTH.md` go stale!
2. **Universal PRD Synchronization:**
   - Whenever workflow architecture, agent roles, quality gates, or file organization subsystems change, the assistant MUST update `04_Riset_&_Metodologi/PRD_UNIVERSAL_SKRIPSI_FRAMEWORK_GRAPH_OF_AGENTS.md`.
3. **Session Logging:**
   - Auto-append an entry to `04_Riset_&_Metodologi/LOG_SESI_SECOND_BRAIN.md` with timestamp, focus, solution achieved, and touched files (starting with `> [!SUMMARY]`, using `[[wikilinks]]`).
4. **Dashboard & Graphify Refresh:**
   - Keep `00_DASHBOARD_SECOND_BRAIN.md` up-to-date (active pages, 54 verified references, gate status).
   - Run incremental graphify update to keep `graphify-out/` synchronized.
