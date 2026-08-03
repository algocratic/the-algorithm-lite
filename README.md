Here is a condensed, high-level summary:

* **Core Workflow:** **The Algorithm** enforces a strict **Negotiate → Freeze → Execute → Verify** cycle to safely manage work across AI models and human collaborators.
* **Execution Gate:** No action is taken until four key factors (**Audience, Scope, Format, Path**) and the controlling instruction are locked into a **Frozen** state.
* **Governance & Authority:** **`SKILL.md`** is the sole canonical source of doctrine. Changes require formal, signed human approval; lower-level files, habits, and history cannot alter doctrine without going through the gate.
* **Receiver Agnosticism:** The protocol assumes any worker (AI or human) may misinterpret rules or act prematurely, relying on strict system gates rather than trust to ensure compliance.
  
Here is a concise summary of the provided text:

---

## Overview

**The Algorithm** is a standardized workflow designed for managing collaboration with language models (or human receivers) under strict oversight. Its core governing framework operates on a four-step cycle: **Negotiate → Freeze → Execute → Verify**.

---

## Core Protocol & Inspection Framework

### The Four Inspection Nouns

Before starting any task, four parameters must be established:

1. **Audience:** Who receives the work?
2. **Scope:** What is permitted to change?
3. **Format:** What structure must the result take?
4. **Path:** What specific action moves the work forward?

### Execution Rules

1. Identify the **controlling sentence** (the language that changes the permitted state of the world).
2. Determine what "floor" or level of authority that sentence sits on.
3. **Never execute** until the controlling language is officially frozen.

---

## Authority & Repository Architecture

Files and repository artifacts operate under a strict **Hierarchy of Authority** (higher ranks override lower ones):

1. **`SKILL.md` (Frozen Invariants & Doctrine):** The single canonical source of truth containing *The Algorithm v2*. Invariants can only be changed through formal amendments.
2. **Recorded Amendments:** Official, assigned logs of changes to invariants.
3. **`registry/KEEP.md`:** The decision register recording project choices and reasoning.
4. **`registry/SEATS.md` & `probe_battery_v0.md`:** Current operational state and receiver measurements (subject to change based on evidence).
5. **Operational Guidance (`bridge/BRIDGE.md`):** Non-canonical agent field reports and onboarding guides.
6. **Proposals (`HOUSE-STYLE.md`, `registry/amendments/pending/`):** Pending drafts on named branches.
7. **Lore & Historical Witnesses (`lore/`, `_historical/`):** Qualitative resonance assays and historical strata used for context or defect detection, never for doctrine.

---

## Key Governance Rules

* **Human Signature Required:** A merge to `main` that alters doctrine is a freeze and strictly requires approval/signing from the authorized human.
* **No In-Place Edits:** Invariants cannot be silently rewritten; changes must follow the full proposal, review, and freeze pipeline.
* **Separation of State and Doctrine:** Practical habits, prompt patterns, or seat assignments are operational *state*, not doctrine, and must be formally promoted to become invariants.
* **Branch Persistence:** Superseded or historical branches are kept as permanent, un-summarized witness history.
* **Receiver Agnosticism:** The gate exists assuming receivers (humans or AIs) will misinterpret authority, execute prematurely, or obscure defects. Safe operation relies on enforced contracts, not receiver trust.
