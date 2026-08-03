## Known facts

- `SKILL.md` is the canonical doctrine.
- The repository follows **negotiate → freeze → execute → verify**.
- A doctrine-changing merge to `main` is a freeze only when the authorized human signs it.
- Invariants change only through recorded amendments.
- `HOUSE-STYLE.md` remains pending and does not yet hold full authority.
- `SEATS.md`, probes, lore, and historical branches provide state or evidence, not doctrine.

# The Algorithm

> **the_algorithm would like to thank you for your continued cooperation.**

**The Algorithm** is a discipline for working with language models under a gate.

It uses one protocol for any receiver:

```text
NEGOTIATE → FREEZE → EXECUTE → VERIFY
```

The receiver may be:

- a student;
- a peer;
- an instructor;
- a software agent;
- a language model;
- a future maintainer.

The protocol stays the same.

---

## The hallway version

Thirty seconds. Reader side.

```text
Audience.
Scope.
Format.
Path.
```

Then:

1. Find the sentence that changes the world.
2. Determine what floor that sentence is buried on.
3. Do not execute until the controlling language is frozen.

The four nouns begin the inspection. They do not replace the full protocol.

---

## Repository map

### `SKILL.md`

**Canonical doctrine.**

This file contains **The Algorithm v2**.

Its **Invariants** section is amendment-only. The amendment record is the repository’s drift meter.

Everything else in this repository is downstream of `SKILL.md`.

---

### `HOUSE-STYLE.md`

The vendored controlled-language subset.

**Current state:** Draft. Pending amendment.

The file is available for review and testing. It does not amend the Invariants until it passes through the gate.

See:

```text
registry/amendments/pending/
```

---

### `registry/KEEP.md`

The decision register.

It records:

- what the project keeps;
- the thought trains that led there;
- the evidence considered;
- the honest freeze state of each entry.

A recorded decision is not doctrine unless the doctrine says it is.

---

### `registry/SEATS.md`

The receiver seat map.

This file records current operating assignments and expectations.

It is state, not doctrine.

Seat assignments reopen after:

- each relevant model release;
- each probe run;
- evidence that a receiver behaves differently than expected.

---

### `registry/probe_battery_v0.md`

The behavioral probe battery.

The probes convert seat assignments from priors into measurements.

A seat assignment without current evidence is a working assumption.

---

### `registry/amendments/pending/`

Proposed changes to the Invariants.

Each proposal uses a working title.

Amendment ordinals are assigned at freeze, never at proposal.

A proposal must not present itself as an adopted amendment.

---

### `lore/`

Resonance assays.

These stories test whether a human reader carries the same weights in the region that matters.

Lore is the human analog of the probe battery.

Lore may expose a defect, conflict, or loss of meaning. Lore does not amend doctrine.

See:

```text
lore/README.md
```

---

### `bridge/BRIDGE.md`

A field report from an agent that worked a long session under the gate.

This file supports onboarding for negotiation-seat agents.

It is operational guidance, not canonical doctrine.

---

### `_historical/`

Repository strata.

This directory is append-only witness.

Historical material may explain how the project arrived at its present form. It does not outrank current doctrine.

See:

```text
_historical/README.md
```

---

### `assets/`

Image and media files shipped by the repository.

A future web interface may read directly from this directory.

Assets carry presentation. They do not carry doctrine unless `SKILL.md` explicitly says otherwise.

---

## Authority order

When two repository artifacts appear to conflict, use this order:

```text
1. Frozen Invariants in SKILL.md
2. Other frozen doctrine in SKILL.md
3. Recorded amendments
4. Frozen repository decisions
5. Current measured state
6. Operational guidance
7. Proposals
8. Lore and historical witness
```

A lower layer may reveal a defect in a higher layer.

It may not silently replace it.

---

## Rules of this repository

### 1. Main is the trunk

A merge to `main` that changes doctrine is a freeze.

A valid doctrinal freeze requires the authorized human signature.

The repository must define the operational signature mechanism through branch protection, signed commits, approval rules, or an equivalent control.

Until that mechanism is defined, the authorized human remains the final semantic authority.

---

### 2. Proposals live on named branches

Proposal branches use names based on their content.

Use:

```text
amend/controlled-language-adoption
probe/receiver-refusal-behavior
lore/the-unopened-door
```

Do not assign an amendment number before freeze.

---

### 3. Invariants are not edited in place

No person or agent may silently rewrite an Invariant.

To change an Invariant:

```text
NEGOTIATE
    ↓
PROPOSE AN AMENDMENT
    ↓
REVIEW EVIDENCE
    ↓
FREEZE WITH HUMAN SIGNATURE
    ↓
RECORD THE AMENDMENT
```

An unrecorded change to the Invariants is a defect, whoever made it.

---

### 4. State does not become doctrine by repetition

A seat assignment, convention, prompt pattern, or successful habit may remain useful for a long time.

That does not make it an Invariant.

Promote state through the gate.

Do not promote it through habit.

---

### 5. Evidence may reopen a seat

Probe results may contradict the current seat map.

When they do, update the state.

Do not defend an old assignment merely because it was previously recorded.

---

### 6. Lore may test doctrine

Lore may reveal that a reader carried the wrong meaning through the system.

Record the result.

If doctrine must change, propose an amendment.

Do not repair doctrine inside the story.

---

### 7. Old branches are strata

Pre-doctrine and superseded branches are not deleted merely to produce a clean graph.

The history is the one witness that never summarizes.

Branches may be marked, archived, or documented. Their evidentiary value must remain intact.

---

### 8. The founding commit is a signature

This repository staging was prepared on the negotiation side.

The authorized human who performs the founding commit completes the first freeze.

The commit does not claim that the system is finished.

It claims that this version is the version from which controlled change begins.

---

## The gate

Before execution, identify four items:

| Item | Question |
|---|---|
| **Audience** | Who receives the result? |
| **Scope** | What may change? |
| **Format** | What form must the result take? |
| **Path** | What action moves the work forward? |

Then find the controlling sentence.

The controlling sentence is the sentence that changes the permitted state of the world.

Examples:

```text
“Approved to build.”
“Freeze this revision.”
“Merge after review.”
“Execute the production prompt.”
“Do not modify the Invariants.”
```

Next, determine its floor.

A controlling sentence may appear in:

- conversation;
- proposal;
- decision record;
- frozen doctrine;
- signed repository history.

Its authority depends on where it lives.

---

## Working states

Use these terms precisely.

| State | Meaning |
|---|---|
| **Negotiating** | Terms remain open |
| **Proposed** | A concrete change exists for review |
| **Approved** | The authorized human accepts the proposal |
| **Frozen** | The approved result has crossed the defined repository gate |
| **Executing** | Work proceeds within the frozen contract |
| **Verifying** | Evidence is checked against the contract |
| **Reopened** | New evidence or authority returns part of the contract to negotiation |
| **Defective** | Work violates the frozen contract or its gate |

Approval and freeze are related but distinct.

A conversation may approve a change.

The repository gate freezes it.

---

## Basic operating loop

```text
INPUT
  ↓
IDENTIFY AUDIENCE, SCOPE, FORMAT, PATH
  ↓
LOCATE CONTROLLING LANGUAGE
  ↓
NEGOTIATE OPEN TERMS
  ↓
FREEZE THE CONTRACT
  ↓
EXECUTE ONLY THE FROZEN WORK
  ↓
VERIFY AGAINST THE CONTRACT
  ↓
RECORD RESULT, DEFECT, OR AMENDMENT
```

When verification fails, do not hide the failure.

Record it.

Then choose one action:

```text
CORRECT EXECUTION
REOPEN NEGOTIATION
PROPOSE AMENDMENT
STOP
```

---

## Receiver rule

The protocol does not depend on the receiver being reliable.

The repository must assume that any receiver may:

- infer authority that was not granted;
- continue after the contract changed;
- treat a proposal as final;
- optimize the wrong sentence;
- summarize away a critical distinction;
- execute before the freeze;
- conceal uncertainty with fluent language.

The gate exists because competence and compliance are separate properties.

---

## Current doctrine status

```text
Doctrine source: SKILL.md
Protocol version: The Algorithm v2
Invariants: Amendment-only
HOUSE-STYLE.md: Draft; pending amendment
Seat map: Provisional state
Probe battery: Measurement instrument
Lore: Resonance evidence
Main branch: Freeze boundary
Authorized human: Final freeze authority
```

---

## Founding signature

```basic
10 PRINT ("ty4yc")
20 END
```

This version makes the authority ladder, working states, signature ambiguity, and draft status explicit while keeping `SKILL.md` as the sole canonical doctrine.
