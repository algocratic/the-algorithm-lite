# Verb pair adjudication — FREEZE and EXECUTE against their challengers

- Status: FROZEN at merge `76c60b9`, 2026-07-31, by the gate holder's typed verb.
- Ordinal: A1 — allocated in the ledger.
- Mode: HUMAN, declared. This file obeys HOUSE-STYLE v2.0.
- Owning clearance: the human at GREEN gate color.
- Origin: issue #8, signed teacherbot.help, 2026-07-30.
- Scheduled by: the green standing orders backlog.

This document asks no gate question. The FILE verb voids a filing that asks one.
Merging this file to main is the freeze. Nothing here freezes before that.

## What this document does

Issue #8 set the disposition path. Run each candidate through rule 1 against the
current controlled vocabulary. The lint decides eligibility. The gate decides taste.

This document runs the lint, records two dispositions, and files one defect.
The green standing orders hold that findings are not dispositions. Each
disposition below carries its own reopen condition.

## Reads declared

- `SKILL.md` — Invariants, fixed strings, gate integrity, self-hosting.
- `HOUSE-STYLE.md` — the enforced subset, controlled protocol nouns, the verb table.
- `registry/KEEP.md` — K5, K6, K16.
- `docs/green/green_standing_orders.md` — the backlog entry.
- Issue #8 — full text.

No external read occurred. Every source above is in this repository.

## The lint — four tests, applied in order

1. Rule 1 in corpus: one word, one meaning, one part of speech, across these files.
2. The verb-entry rule: one meaning, one part of speech, a completion condition, a
   failure condition. No fourth item, no entry.
3. Substrate collision: the run target is a Codespace with git. A word that means
   two things in one transcript fails rule 1 in that transcript.
4. Amendment surface: count the frozen text the candidate rewrites.

## Results

| Candidate | Side | Rule 1 in corpus | Substrate | Verdict |
|---|---|---|---|---|
| FREEZE | gate | pass | none | eligible — incumbent |
| EXECUTE | run | pass | code execution — known, accepted | eligible — incumbent |
| PLAN | gate | fail | none | ineligible |
| BUILD | run | pass | fail — build systems | ineligible |
| SEAL | gate | pass | minor — sealed secrets, signing | eligible — challenger |
| PERFORM | run | fail | none | ineligible |
| COMMIT | gate | fail | fail — git | ineligible |
| ENACT | both | fail | none | ineligible |

## Findings, one per candidate

**PLAN — ineligible.** The corpus already uses PLAN as a noun. SPECTRUM is the plan.
Verbing it gives one word two parts of speech. This is the defect the style file
already names for GATE. See the filed defect below: the register lacks the entry.

**BUILD — ineligible.** BUILD does not collide inside the corpus today. It collides
at the substrate. Every run target carries a build system. One transcript would then
hold "run the build" and the gate verb, with two meanings and no way to tell them
apart. Rule 1 fails where the document is actually read.

**SEAL — eligible.** SEAL clears rule 1 in the corpus. Its collision with sealed
secrets and with signing is real and small. It signals cost as well as FREEZE does.
It loses on fit, not on collision. See the disposition below.

**PERFORM — ineligible.** The verb table defines EXECUTE with the word perform.
Promoting the defining word to the defined word makes the entry circular. A second
collision is worse: K6 names ritual performance as a failure mode this project
expects. The execution verb must not share a word with the failure it invites.

**COMMIT — ineligible.** Issue #8 called the git collision likely fatal. It is fatal.
K5 makes a freeze a signed commit, so COMMIT would name both the act and its own
mechanism. Two meanings, one word, in the substrate the project is leaning toward.

**ENACT — ineligible.** ENACT means to make a text binding and also to carry a text
out. Those are the two sides the gate exists to separate. One word cannot hold both
and leave the gate detectable. ENACT also arrives without a partner verb, so it is
not yet a pair.

## The amendment surface — the cost issue #8 did not count

FREEZE and EXECUTE both appear inside F1 and F2. Two of the four fixed strings would
be rewritten by any change to either verb.

Fixed strings are contracts under rule 8. They are exempt from editing outside the
amendment process. F1 and F2 also live in the SKILL.md Invariants section, which is
amendment-only. A verb change is therefore an Invariants amendment, not a style edit.
It costs a GREEN gate, an amendment-record entry, and a skew against every quoted
transcript already in the strata.

This cost does not decide the question. It sets the bar a challenger must clear.

## Disposition 1 — retain FREEZE and EXECUTE

Retain both incumbents. Make no change to the verb table. Propose no amendment to
Invariants. The four challengers named in issue #8 are eliminated on collisions,
before taste is consulted.

Reopens if: a challenger clears rule 1 in corpus and at the substrate, and shows a
measured cost of the incumbents beyond preference.

## Disposition 2 — SEAL is filed, not adopted

SEAL is the only challenger that survives the lint. It is recorded here and adopted
nowhere.

The argument against SEAL is fit, and it runs against the intuition. FREEZE carries
a thaw. A seal is broken and does not return. This protocol reopens contracts as a
first-class state, named in F3. The incumbent verb carries a return path that the
protocol actually uses, and the challenger does not.

Reopens if: someone measures a cost of the thaw connotation — a seat that treats a
frozen contract as provisional, and cites the word.

## Defect filed — the register is missing an entry the lint relies on

HOUSE-STYLE registers two controlled protocol nouns: GATE and SEAT. It does not
register PLAN. The rule 1 argument against PLAN depends on PLAN being controlled.
The argument holds in practice and lacks its register entry.

Proposed addition to the controlled protocol nouns block, for a separate gate:

- PLAN: noun only. The document the negotiation side produces. Text that verbs a
  plan fails the lint.

This addition is not folded into disposition 1. It is a separate amendment and needs
its own freeze.

## Prediction resolved

Issue #8 predicted, hedged, that the incumbents survive because the house style
eliminates both challengers on collisions. Confirmed for PLAN and for BUILD. The
prediction did not cover the third options. All three fell to the same test, which
is weak evidence that the lint is doing the work and not the incumbency.

## Known path skew — recorded at filing, closed on main

At filing, the README placed the register at `registry/KEEP.md` and the seat map
at `registry/SEATS.md`, and both files sat at the repository root. This file
followed the README path because the README declared it. Main closed the skew at
commit `0566779`, after this filing. Both files now sit at `registry/`. No repair
remains for this document to schedule.
