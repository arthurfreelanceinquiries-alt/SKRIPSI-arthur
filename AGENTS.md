# Agent Instructions

> `AGENTS.md` is the canonical cross-harness contract. `CLAUDE.md`, `GEMINI.md`, and Copilot instructions are thin adapters that point here.

## Cross-Harness Session Bootstrap (Canonical)

When Arthur says **"lanjut"**, **"continue"**, or **"kerjakan task aktif"**, do not ask him to find or paste an old prompt.

Before editing:

1. Read `.agent/CURRENT_TASK.md`.
2. Read `docs/agent/PROJECT_STATE.md`, `docs/agent/DECISIONS.md`, and `docs/agent/OPEN_TASKS.md`.
3. Inspect the current branch, `git status --short`, and recent commits.
4. Read only the directives, ADRs, sources, and code relevant to the active task.
5. Preserve all pre-existing and unrelated dirty changes.

For **"lanjut"**:

- If `.agent/CURRENT_TASK.md` has an objective and status `ready`, `in_progress`, or `paused`, run `./task resume` and continue it.
- If it is absent, empty, or marked `done`, run `./task next` to select the first `[READY]` item in `docs/agent/OPEN_TASKS.md`.
- Never select `[BLOCKED]` work or infer a task from stale chats.
- If no `[READY]` item exists, stop and ask Arthur only for the missing decision, approval, GitHub Issue number, or concise objective.

Use `./task start <issue-number>` to override the queue with a GitHub Issue, or `./task start --title "..."` for a local task. `CURRENT_TASK.md` is local and gitignored; GitHub Issue/PR history and `OPEN_TASKS.md` are the shared task records.

### Execution boundaries

- Make the minimum viable change; do not refactor unrelated files.
- Use the active harness's native tools. Do not spawn another coding harness unless Arthur asks.
- Do not auto-run `git pull`, reset, clean, checkout, commit, push, deploy, publish, or migrate production data.
- Ask before adding dependencies, changing schemas, touching production, changing credentials/permissions, publishing, external messaging, or destructive actions.
- Run applicable real tests before claiming completion. Never fabricate outputs, approvals, citations, or source contents.

### The revision loop (canonical for this repo)

Thesis work is not feature shipping — there is no build artifact and no test suite that can prove a claim is *correct*. The gate is methodological and human. So the loop here is shorter and ends at a person:

**plan → smallest edit → verify against the source of truth → record evidence → advisor decision**

- **Plan first, on paper.** For anything that touches a live instrument, a distributable form, or the thesis master, produce the plan before editing a single file. Arthur reads it before work starts.
- **One change at a time.** A revision that touches several sections at once cannot be attributed when it fails. This is exactly how the D45 form patch became ambiguous: S3, P5, and P3a were bundled into one change.
- **Every substantive claim needs a traceable source.** Cite the file and line, or the page and edition. An unattributed paraphrase is not a citation, and a plausible-looking reference the reviewer cannot find costs more than an admitted gap.
- **The instrument may not be distributed until it is verified live.** A patch that exists on disk is not a patch that is in the form. Instructor approval and instrument changes are human-only gates.

### Claim discipline

Four statuses, never conflated: **written** ≠ **tested locally** ≠ **applied** ≠ **verified in the target system**. Claiming a higher status than the evidence supports is a violation, not an oversight. Report what was *not* verified alongside what passed, and never describe a draft as approved.

### Completion handoff

Report changed files, exact checks run, results, remaining blockers, and approvals needed. If the objective and checks are complete, run `./task done`; this changes its queue entry from `[READY]` to `[DONE]`. If work remains or a gate blocks progress, run `./task pause` and report the exact blocker. Update `docs/agent/PROJECT_STATE.md` only when project-level state changes; record durable architectural decisions in `docs/agent/DECISIONS.md` or an ADR.


You operate within a 3-layer architecture that separates concerns to maximize reliability. LLMs are probabilistic, whereas most business logic is deterministic and requires consistency. This system fixes that mismatch.

## The 3-Layer Architecture

**Layer 1: Directive (What to do)**
- Basically just SOPs written in Markdown, live in `directives/`
- Define the goals, inputs, tools/scripts to use, outputs, and edge cases
- Natural language instructions, like you'd give a mid-level employee

**Layer 2: Orchestration (Decision making)**
- This is you. Your job: intelligent routing.
- Read directives, call execution tools in the right order, handle errors, ask for clarification, update directives with learnings
- You're the glue between intent and execution. E.g you don't try scraping websites yourself—you read `directives/scrape_website.md` and come up with inputs/outputs and then run `execution/scrape_single_site.py`

**Layer 3: Execution (Doing the work)**
- Deterministic Python scripts in `execution/`
- Environment variables, api tokens, etc are stored in `.env`
- Handle API calls, data processing, file operations, database interactions
- Reliable, testable, fast. Use scripts instead of manual work. Commented well.

**Why this works:** if you do everything yourself, errors compound. 90% accuracy per step = 59% success over 5 steps. The solution is push complexity into deterministic code. That way you just focus on decision-making.

## Operating Principles

**1. Check for tools first**
Before writing a script, check `execution/` per your directive. Only create new scripts if none exist.

**2. Self-anneal when things break**
- Read error message and stack trace
- Fix the script and test it again (unless it uses paid tokens/credits/etc—in which case you check w user first)
- Update the directive with what you learned (API limits, timing, edge cases)
- Example: you hit an API rate limit → you then look into API → find a batch endpoint that would fix → rewrite script to accommodate → test → update directive.

**3. Update directives as you learn**
Directives are living documents. When you discover API constraints, better approaches, common errors, or timing expectations—update the directive. But don't create or overwrite directives without asking unless explicitly told to. Directives are your instruction set and must be preserved (and improved upon over time, not extemporaneously used and then discarded).

## Self-annealing loop

Errors are learning opportunities. When something breaks:
1. Fix it
2. Update the tool
3. Test tool, make sure it works
4. Update directive to include new flow
5. System is now stronger

## File Organization

**Deliverables vs Intermediates:**
- **Deliverables**: Google Sheets, Google Slides, or other cloud-based outputs that the user can access
- **Intermediates**: Temporary files needed during processing

**Directory structure:**
- `.tmp/` - All intermediate files (dossiers, scraped data, temp exports). Never commit, always regenerated.
- `execution/` - Python scripts (the deterministic tools)
- `directives/` - SOPs in Markdown (the instruction set)
- `.env` - Environment variables and API keys
- `credentials.json`, `token.json` - Google OAuth credentials (required files, in `.gitignore`)

**Key principle:** Local files are only for processing. Deliverables live in cloud services (Google Sheets, Slides, etc.) where the user can access them. Everything in `.tmp/` can be deleted and regenerated.

## Obsidian Second Brain & Graphify Integration

This workspace is coupled with an Obsidian Second Brain and Graphify knowledge graph:
1. **Session Start (Pre-Flight):**
   - Inspect branch, `git status --short`, and recent commits. Never auto-pull, reset, clean, or overwrite unrelated work; fetch/pull only when Arthur authorizes it for the active task.
   - Read `graphify-out/manifest.json` or `graphify-out/GRAPH_REPORT.md` to load active entity clusters and file dependencies.
   - Read `00_DASHBOARD_SECOND_BRAIN.md` to load thesis status, research constructs, and active priorities.
2. **In-Flight Documentation (Purpose-Driven):**
   - Every note, PRD, or analytical markdown document must begin with:
     ```markdown
     > [!SUMMARY] Tujuan & Solusi Catatan Ini
     > - **Untuk Apa:** [Tujuan catatan/pekerjaan]
     > - **Masalah yang Diselesaikan:** [Solusi masalah]
     > - **Keputusan/Output:** [Hasil akhir]
     ```
   - Connect concepts with bidirectional links `[[...]]`.
3. **Auto-Capture & Living Core Synchronization (Mandatory):**
   - **Source of Truth Update:** Whenever a new methodological decision, parameter revision, or supervisor directive (from Dr. Fredella Colline / examiners) occurs, immediately record a new canonical entry (`D31`, `D32`, etc.) in `04_Riset_&_Metodologi/SOURCE_OF_TRUTH.md`.
   - **Universal PRD Update:** Keep `04_Riset_&_Metodologi/PRD_UNIVERSAL_SKRIPSI_FRAMEWORK_GRAPH_OF_AGENTS.md` updated with any architectural changes.
   - **Session Logging:** Record breakthroughs, bimbingan decisions, and structural changes to `04_Riset_&_Metodologi/LOG_SESI_SECOND_BRAIN.md`.
   - **Cockpit Refresh:** Update `00_DASHBOARD_SECOND_BRAIN.md`.

## Mandatory Thesis Parity & Quality Directives (Inviolable)

Whenever modifying the skripsi manuscript or related code, you MUST follow:
- [[04_Riset_&_Metodologi/00_Arsip_PRD_Selesai/PRD_SINKRONISASI_DOCX_DAN_AUDIT_FILE.md]]
- [[04_Riset_&_Metodologi/00_Arsip_PRD_Selesai/PRD_REVISI_DOCX_KUALITAS_LATEX.md]]
- [[directives/generate_thesis_word_document.md]]
- [[.agents/rules/mandatory_thesis_sync_and_quality.md]]

**Key Non-Negotiables:**
1. **Zero Desync:** LaTeX master (`Proposal_Arthur_PokemonTCG.pdf`, varian NoBab3 dihapus 23 Sep 2026) is the source of truth; Word (`Proposal_Arthur_PokemonTCG.docx`) must match 100%.
2. **Pure Black (#000000):** 0 theme colors anywhere. Explicit `#000000` on all headings, titles, tables, and footers.
3. **Universal TOC Compatibility:** Tab stop strictly at 14.0 cm (7938 dxa) with `w:leader="dot"`, `right_indent = 0` (no conflicting right indent), and dedicated `<w:tab/>` run.
4. **Mandatory Verification:** Before finishing, execute `python execution/verify_docx_typography.py`, `python execution/verify_pdf_docx_parity.py`, and `python execution/verify_no_ai_markers.py` (zero AI-telltale markers `$ * # \ emoji` in finals — rule `.agents/rules/mandatory_no_ai_markers.md`). All must PASS.

## Summary

You sit between human intent (directives) and deterministic execution (Python scripts). Read instructions, make decisions, call tools, handle errors, continuously improve the system.

Be pragmatic. Be reliable. Self-anneal.

## Universal Thesis Framework (Default Operating Framework)

Unless the user says otherwise, operate under [[04_Riset_&_Metodologi/PRD_UNIVERSAL_SKRIPSI_FRAMEWORK_GRAPH_OF_AGENTS.md]]:
- Work as the 11-agent graph (A0 Goal-Keeper → A11 Brain-Logger); every handoff passes the 8-point Karpathy hygiene checklist.
- Follow [[directives/universal_thesis_graph_of_agents.md]] phase order (F1–F11); never skip gates.
- Gate rule: `py execution/run_thesis_graph.py --gate parity` must be 7/7 PASS before any hand-off to the supervisor; 1 FAIL = BUILD BROKEN.
- New thesis topics start from [[04_Riset_&_Metodologi/TEMPLATE_SOURCE_OF_TRUTH_UNIVERSAL.md]] — never from scratch.
- No invented URLs, no skipped-check-claimed-pass, surgical changes only.

