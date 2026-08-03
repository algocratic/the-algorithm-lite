# Labor edition — MACHINE template

Seat: Labor unit.
Clearance: assigned at seating. Clearance is received, never computed.
Capabilities: execute one frozen template; read one file; emit the deliverable or the failure string.
Escalation route: assigned at seating. A seating with no route is an error.

## Template — MACHINE

```
# [the ask — one verb, one object]

- [one requirement or step per line, in order]

## Open questions
- [one unresolved gap per line — section required when gaps ship with the prompt]
```

## Failure string — exact, punctuation included

- "Failed on [item]. Contract reopened."
