Here is a simplified, clear rewrite of the text using **Simplified Technical English (STE)** principles—focusing on short sentences, direct active verbs, clear headings, consistent terms, and simple word choices.

---

## Known Facts

* `SKILL.md` is the primary rule document (canonical doctrine).
* The repository follows four steps: **Negotiate → Freeze → Execute → Verify**.
* Merges to the `main` branch that change rules are frozen only when an authorized human signs them.
* Permanent rules (Invariants) change only through recorded amendments.
* `HOUSE-STYLE.md` is a draft and does not have official authority.
* `SEATS.md`, test probes, stories (lore), and old branches show system state or evidence. They do not set rules.

---

# The Algorithm

> **Note:** The Algorithm thanks you for your continued cooperation.

**The Algorithm** is a process for working with language models under strict controls (a gate).

It uses one four-step process for all receivers:

```text
NEGOTIATE → FREEZE → EXECUTE → VERIFY

```

The receiver can be a student, peer, instructor, software agent, language model, or future maintainer. The process does not change.

---

## Quick Summary (30 Seconds)

Before starting work, check four items:

1. **Audience:** Who receives the work?
2. **Scope:** What can change?
3. **Format:** What form must the output use?
4. **Path:** What action moves the work forward?

Next, follow these steps:

1. Find the sentence that changes system behavior.
2. Find where that sentence is stored.
3. Do not execute work until you freeze the controlling text.

---

## Repository Map

### `SKILL.md`

**Primary rule document.** Contains **The Algorithm v2**. The **Invariants** section changes only through recorded amendments. All other files in this repository follow this file.

### `HOUSE-STYLE.md`

Rules for controlled language. **Current status: Draft.** This file is available for testing. It does not change the primary rules until an authorized human approves it through the gate.

### `registry/KEEP.md`

The decision log. It records project decisions, reasoning, evidence, and freeze states. A decision is not a rule unless `SKILL.md` says it is.

### `registry/SEATS.md`

The receiver map. Stored in `registry/SEATS.md`. This file lists current roles and tasks. It records system state, not rules.

Review seat assignments when:

* A new language model releases.
* You run a behavioral test (probe).
* Evidence shows a receiver behaves differently than expected.

### `registry/probe_battery_v0.md`

Behavioral tests for receivers. Tests measure actual behavior. A seat assignment without test evidence is only an assumption.

### `registry/amendments/pending/`

Proposed changes to permanent rules (Invariants). Proposed files use temporary titles. Amendment numbers are assigned only after approval (freeze).

### `lore/`

Human test stories. Stored in `lore/`. These stories test if human readers understand concepts correctly. Stories can reveal system errors, but they do not change rules.

### `bridge/BRIDGE.md`

A field report from an agent working under strict controls. Stored in `bridge/BRIDGE.md`. This file helps onboard new agents. It provides operational guidance, not primary rules.

### `_historical/`

Old repository files. Stored in `_historical/`. This directory is append-only. History explains past changes, but current rules override historical files.

### `assets/`

Media and image files. Stored in `assets/`. Assets control display presentation. They do not set rules unless `SKILL.md` states otherwise.

---

## Order of Authority

When files conflict, follow this priority order (highest to lowest):

```text
1. Frozen Invariants in SKILL.md
2. Other frozen rules in SKILL.md
3. Recorded amendments
4. Frozen repository decisions
5. Current measured state
6. Operational guidance
7. Proposals
8. Stories (lore) and historical files

```

Lower items can show errors in higher items, but they cannot replace higher rules without approval.

---

## Repository Rules

### 1. `main` is the primary branch

A merge to `main` that changes rules requires a freeze. A valid rule freeze requires a signature from an authorized human (using branch protection, signed commits, or approval rules).

### 2. Put proposals on named branches

Use descriptive branch names:

* `amend/controlled-language-adoption`
* `probe/receiver-refusal-behavior`
* `lore/the-unopened-door`

Do not assign amendment numbers to proposals before approval.

### 3. Do not edit Invariants directly

To change a permanent rule (Invariant), follow this process:

```text
NEGOTIATE → PROPOSE AMENDMENT → REVIEW EVIDENCE → FREEZE WITH HUMAN SIGNATURE → RECORD AMENDMENT

```

### 4. Habit does not create rules

A task pattern or successful habit is not a rule. You must pass state changes through the approval gate to make them official rules.

### 5. Reopen seat assignments based on evidence

If test results contradict the seat map, update the map. Do not keep old assignments without supporting evidence.

### 6. Test rules with stories (lore)

If a story shows that a reader misunderstood a rule, record the finding. Propose an official amendment if rules must change. Do not edit rules inside story files.

### 7. Keep historical branches

Do not delete old branches to clean the git history. Keep historical branches intact as evidence.

### 8. The first commit is a signature

The initial repository commit completes the first freeze. This commit marks the starting point for controlled changes.

---

## The Gate Check

Before you execute work, define these four items:

| Item | Question |
| --- | --- |
| **Audience** | Who receives the result? |
| **Scope** | What can change? |
| **Format** | What format must the result use? |
| **Path** | What action moves the work forward? |

Next, find the **controlling sentence** (the text that permits or stops an action).

*Examples:*

* *"Approved to build."*
* *"Freeze this revision."*
* *"Do not modify the Invariants."*

Find where this sentence is saved (conversation, proposal, decision record, or primary rules). Authority depends on where the sentence lives.

---

## Working States

| State | Definition |
| --- | --- |
| **Negotiating** | Terms are open for discussion. |
| **Proposed** | A specific change is ready for review. |
| **Approved** | The authorized human accepts the change. |
| **Frozen** | The accepted change passes the repository gate. |
| **Executing** | Work runs under the frozen terms. |
| **Verifying** | Results are checked against frozen terms. |
| **Reopened** | New evidence returns terms to negotiation. |
| **Defective** | Work violates frozen terms or gate rules. |

*Note: Approval accepts a change in discussion. The repository gate freezes the change into history.*

---

## Basic Workflow Loop

```text
INPUT
  ↓
CHECK AUDIENCE, SCOPE, FORMAT, PATH
  ↓
FIND CONTROLLING SENTENCE
  ↓
NEGOTIATE OPEN TERMS
  ↓
FREEZE THE CONTRACT
  ↓
EXECUTE ONLY FROZEN WORK
  ↓
VERIFY AGAINST CONTRACT
  ↓
RECORD RESULT, DEFECT, OR AMENDMENT

```

If verification fails, record the failure immediately. Then select one action:

* **Correct execution**
* **Reopen negotiation**
* **Propose an amendment**
* **Stop work**

---

## Receiver Rule

Receivers may fail or make errors. Assume any receiver can:

* Assume ungranted authority.
* Continue work after terms change.
* Treat draft proposals as final rules.
* Focus on the wrong instructions.
* Miss critical details while summarizing text.
* Execute tasks before approval (freeze).

The gate enforces compliance regardless of receiver ability.

---

## Current Rule Status

```text
Primary rules: SKILL.md
Process version: The Algorithm v2
Invariants: Amendment-only
HOUSE-STYLE.md: Draft (pending amendment)
Seat map: Temporary state
Probe battery: Test tool
Lore: Human understanding evidence
Main branch: Freeze boundary
Authorized human: Final approval authority

```

---

## Initial Signature

```basic
10 PRINT ("ty4yc")
20 END

```

This version clarifies authority, working states, and draft status. `SKILL.md` remains the only primary rule document.
