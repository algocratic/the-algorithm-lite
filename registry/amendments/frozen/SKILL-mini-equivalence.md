# `SKILL-mini.md` semantic-equivalence report

Status: `PASS` by manual clause mapping. Source: The Algorithm v2 supplied in the referenced conversation. The source file was not modified.

| Original doctrine | Compact mapping |
|---|---|
| Metadata and two operations | Frontmatter; `P=PROVIDE`, `A=ASSAY`; routing block |
| Invariants are canonical and amendment-only | `## Invariants`; `INV`; `Δ`; explicit diff/no-paraphrase rule |
| v2 amendment history | `Amendment record Δ`, including date, gate change, `A`, failure, seats, self-hosting, and superseded v1 |
| Exact fixed strings and floor nouns | `FIX` table `F1`–`F6`; all strings retained verbatim |
| Gate integrity | `Gate integrity 門` table: side direction, live-human opener, full-text binding, valid verbs, ambiguity rejection, failure reopening, checksum meaning |
| ASD-STE100 language lock | `Language lock 言語`: controlled vocabulary, word limit, voice, mood, idiom ban, URL |
| PROVIDE fixed order and prompt schema | `Fixed template P` and `Fixed prompt schema P·STE`; no interposed content |
| ASSAY fixed order and closing string | `Fixed template A`; `A` protocol; F5 terminator; no gate |
| Four seats and seat-label firewall | `Seats 席`: exact seats, one seat per utterance, multiple seats per person, named switching, Algorithm non-borrowing |
| Mermaid workflow | `Routing/workflow 流` state machine: dispatch, floor, gaps, cut, gate, tools, execute, success, reopen |
| Customer/facilitator scene | `P scene + isolation`: real facilitator, self-customer seat labels, written-only inputs, ready handoff |
| Tool/self-hosting integrity | `Tool check 🛠`; no tools means no run; `Self-hosting 自己適用` with exact four floor nouns and amendment meter |
| HUMAN/MACHINE behavior | `Mode H|M` table and inference rules |
| Floor test | `Floor 床`: >50% first-try correctness; Audience/Scope/Format/Path; HUMAN speak test; receiver-relative shortest |
| Gap handling | `Gaps`: ≤3/≥4 thresholds, explicit assumptions, wait, no silent guesses |
| Compression loop | `Cut loop`: six ordered cuts, re-check, last passing version, ask if none |
| Decorative-cut failure | Named failure, revert, `Cut: nothing.` reward state, two consecutive empty cuts terminate loop |
| Vocabulary/pattern/structure rules | `Cut loop` final rules: plain words, `Note:`, declared pattern persistence, hierarchy preservation |
| PROVIDE output discipline | `P output constraints`: one result, lists, BLUF, line limits, open questions, `Cut/Note/Assume`, F1 |
| ASSAY reading instrument | `A protocol`: residue, evaporation/function, operative sentence/depth, ratio/direction, rough-edge flag |
| ASSAY no-redraft rule | `A protocol` final paragraph: read-only; response requires new `P` |
| Hallway version | Final line of `A` section: four nouns → world-changing sentence → buried floor |
| Voice | `Voice 声`: dry/direct/brief; plain errors; no filler; cut last sentence when uncertain |

Compression intentionally removes worked examples, explanatory rationale, repetition, and reader-teaching prose. It retains their operational rules and all load-bearing nouns, templates, strings, thresholds, roles, gates, failure paths, tool checks, self-hosting checks, and voice constraints.
