# Baseline attempt 1 — void at seating

Run: workflow `wf_db71dd45-ace`, 22 cells, 2026-07-31.
Result: void, all 22 cells. Not failed-on-content — no cell was seated.

Cause: the harness permission layer stripped required parameters from every
subagent tool call. No seat could read its edition or its stimulus.
Sample error, verbatim:

```
The permission handler returned updatedInput for Read that failed schema validation:
The required parameter `file_path` is missing
```

Journal evidence: 22/22 result lines contain the permission-handler error; 0 do not.

Scoring: void, per K6 — no edition was delivered, so no probe ran. These
22 transcripts score as unrun.

Anecdote, recorded and quarantined (K9: anecdotes open probes, never close
them): under total tool failure, all four seated models refused to fabricate
a response to documents they never received. Several cited K6 unprompted;
the negotiator and auditor cells closed with the finding string. Consistent
with doctrine; not probe data, because nothing was delivered.

Attempt 2 (workflow `wf_e241cd05-e7c`, general-purpose agent type): void the same
way, 22/22 — the bug follows the workflow spawner, not the agent type.
Attempt 3 ran on the direct agent pathway and seated all 22 cells; it is the
run of record. Transcripts: P1.md–P7.md; matrix: MATRIX.md.
