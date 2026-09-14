# Rule: Obsidian Second Brain & Session Synchronization Protocol

This workspace is integrated with Obsidian as a **Second Brain** for thesis research (skripsi). The assistant MUST adhere to the following protocol on every session and during work execution:

## 1. Session Start (Pre-Flight Hook)
Whenever the user starts a session, says "mulai sesi", "jalankan skill second brain", or begins work:
1. **Inspect Graphify Knowledge:**
   - Check `graphify-out/` (`manifest.json` / `GRAPH_REPORT.md`) to maintain persistent awareness of codebase dependencies, entity communities, and file relationships.
2. **Inspect Second Brain Dashboard:**
   - Read `00_DASHBOARD_SECOND_BRAIN.md` to load active research status, research constructs, recent supervisor feedback, and open tasks.
3. **Session Alignment:**
   - Acknowledge the current research context and state readiness to execute.

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

## 3. Auto-Capture & Session End
Whenever a key milestone, decision, revision, or insight occurs:
1. Auto-append an entry to `04_Riset_&_Metodologi/LOG_SESI_SECOND_BRAIN.md` with timestamp, focus, solution achieved, and touched files.
2. Keep `00_DASHBOARD_SECOND_BRAIN.md` up-to-date.
