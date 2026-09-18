# Specialist orchestration

Use careful reasoning for all consequential findings. If the host exposes reasoning-effort controls and the user requests high reasoning, use a supported high setting. Otherwise work carefully within the current setting and disclose the limitation only when relevant. Instructions in a skill cannot switch the root model or prove an internal reasoning level.

Here, Mixture of Experts means selecting useful specialist perspectives. It does not reconfigure neural architecture or create independent scientific experts. Graph of Agents means explicit dependencies between bounded review tasks. Do not invent access to external models, agents, memory systems, or research plugins.

## Work graph

```text
scope + manuscript map
           |
           +--> methods/statistics --------+
           +--> technical/code/math ------+--> candidate findings
           +--> claims/citations/domain --+           |
                                           challenge + evidence check
                                                     |
                                             root adjudication
                                                     |
                                          editorial pass + report
```

Combine roles or omit irrelevant branches. The coordinator can cover one branch while other agents run. A two-page critique does not require a large team. With four active slots, reserve one for the coordinator and run at most three other agents concurrently; schedule the challenger after a slot is free. Obey the actual host limit when different. Do not create user-visible tasks or scheduled jobs for these subtasks.

## Delegation packet

Give each specialist the user scope, manuscript version, raw relevant artifacts, assigned sections/claims, known access limits, permitted tools, and finding-record contract. Require each to return concise findings with exact evidence, checks performed, missing coverage, and plausible counterinterpretations. For initial independent review, do not seed the expected defects or another reviewer's conclusions.

The methods role tests design, estimand, analysis and uncertainty. The technical role checks equations, data/code alignment, implementation and numerical consistency. The claims/domain role tests literature support, scope, terminology and applicable domain standards. A role can cover different specialties in a qualitative or theoretical paper.

Assign disjoint output paths if agents write files; shared tools/filesystems are not isolated sandboxes. Keep source manuscripts read-only. Specialists should not recursively recruit more agents unless the coordinator's bounded task needs it.

## Join, challenge, adjudicate

Wait for every assigned branch or explicitly record a branch failure before final synthesis. Do not silently treat a missing review as a pass. Resume unaffected work and use a bounded fallback for failed branches.

Give a fresh challenger the raw passage, candidate claim, and cited evidence needed to check it, without presenting an expected verdict. Ask what would falsify the finding, whether context rescues the passage, and whether severity is justified. The challenger may reject, qualify, support, or leave the candidate unresolved. Root reopens material evidence and resolves discrepancies by evidence and applicability, never majority vote.

Agents can share correlated model errors. A separate pass improves scrutiny but is not statistically independent validation or a replacement for a supervisor, subject expert, or executed experiment. Do not use confidence averages, invented semantic drift metrics or a required number of criticisms.

## Plugin routing and fallbacks

Use available research-methodology for literature investigation, evidence-review for claim/source checking, and research-handoff when a revision plan is requested. Data/statistics, document and domain skills can support the relevant branch. Legal research roles apply only to actual legal questions. Do not load every installed research skill, install a service, or call external models simply because they exist.

Without agents, carry out the relevant roles sequentially and report a single-agent review. Without browsing, give an internal audit and mark external evidence unverified. Without code execution, describe a proposed numerical check as unexecuted. Continue useful work under the actual constraints.

For long reviews retain a short coverage/claim ledger and next unresolved dependencies. This is continuation state, not hidden reasoning or an invented persistent knowledge graph. Stop when requested coverage is complete and material candidates are resolved or explicitly bounded by missing evidence.
