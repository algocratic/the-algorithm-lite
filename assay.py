#!/usr/bin/env python3
"""Read-only HOUSE-STYLE assayer.

The command reports evidence. It never changes the files that it reads.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence


MAX_INSTRUCTION_WORDS = 20
MAX_DESCRIPTION_WORDS = 25
MAX_SENTENCES_PER_PARAGRAPH = 6

# These strings are the contracts declared by HOUSE-STYLE.md. They are kept
# here so the assayer can detect a changed contract declaration as well as a
# misplaced occurrence in a document.
DECLARED_FIXED_STRINGS = {
    "F1": "Freeze this contract and execute, or keep negotiating?",
    "F2": "Contract frozen. Executing.",
    "F3": "Failed on [item]. Contract reopened.",
    "F4": "This is a finding, not a draft.",
}

IMPERATIVE_STARTS = {
    "add",
    "assay",
    "ask",
    "avoid",
    "build",
    "call",
    "check",
    "close",
    "control",
    "declare",
    "determine",
    "do",
    "ensure",
    "execute",
    "file",
    "find",
    "flag",
    "follow",
    "freeze",
    "give",
    "identify",
    "include",
    "keep",
    "lint",
    "locate",
    "make",
    "name",
    "never",
    "open",
    "pass",
    "provide",
    "read",
    "record",
    "report",
    "return",
    "review",
    "run",
    "seat",
    "ship",
    "spawn",
    "treat",
    "use",
    "warn",
    "write",
}

FIXED_STRING_VARIANT_PATTERNS = {
    "F1": re.compile(r"Freeze this contract and execute[^\n]*?(?:\?|$)", re.IGNORECASE),
    "F2": re.compile(r"Contract frozen\.[^\n]*?(?:[.!?]|$)", re.IGNORECASE),
    "F3": re.compile(r"Failed on \[[^\]]+\]\.[^\n]*?(?:[.!?]|$)", re.IGNORECASE),
    "F4": re.compile(r"This is a finding, not a draft[^\n]*?(?:[.!?]|$)", re.IGNORECASE),
}


@dataclass(frozen=True)
class Finding:
    path: Path
    line: int
    rule: str
    evidence: str
    expected: str

    def render(self) -> str:
        evidence = self.evidence.replace("\n", " ").strip()
        return (
            f"FINDING {self.path}:{self.line} | {self.rule} | "
            f"evidence: {evidence} | expected: {self.expected}"
        )


@dataclass(frozen=True)
class TextBlock:
    start_line: int
    end_line: int
    text: str
    kind: str = "paragraph"
    protected: bool = False


def word_count(text: str) -> int:
    """Count words without treating Markdown punctuation as words."""

    return len(re.findall(r"[A-Za-z0-9]+(?:[-’'][A-Za-z0-9]+)*", text))


def sentence_spans(text: str) -> list[tuple[int, int]]:
    """Return sentence spans using terminal punctuation as the boundary."""

    spans: list[tuple[int, int]] = []
    start = 0
    # A boundary is terminal punctuation followed by whitespace or EOF. This
    # intentionally stays conservative; a peer can decide on ambiguous prose.
    for match in re.finditer(r"[.!?](?:[\"'”’\)\]]+)?(?=\s|$)", text):
        end = match.end()
        if text[start:end].strip():
            spans.append((start, end))
        start = end
    if text[start:].strip():
        spans.append((start, len(text)))
    return spans


def line_for_offset(text: str, start_line: int, offset: int) -> int:
    return start_line + text.count("\n", 0, offset)


def clean_sentence(sentence: str) -> str:
    sentence = re.sub(r"^\s*(?:[-*+]\s+|\d+[.)]\s+|>\s*)+", "", sentence)
    return sentence.strip()


def is_instruction(sentence: str) -> bool:
    cleaned = clean_sentence(sentence)
    first = re.match(r"([A-Za-z]+)", cleaned)
    if not first:
        return False
    return first.group(1).lower() in IMPERATIVE_STARTS


def markdown_blocks(lines: Sequence[str], protected_sections: set[str]) -> list[TextBlock]:
    """Extract prose blocks while retaining Markdown container boundaries."""

    blocks: list[TextBlock] = []
    paragraph_lines: list[str] = []
    paragraph_start = 0
    in_fence = False
    fence_start = 0
    section = ""

    def flush() -> None:
        nonlocal paragraph_lines, paragraph_start
        if not paragraph_lines:
            return
        raw = "\n".join(paragraph_lines)
        first = paragraph_lines[0].lstrip()
        is_list_item = bool(re.match(r"(?:[-*+]\s+|\d+[.)]\s+)", first))
        blocks.append(
            TextBlock(
                paragraph_start,
                paragraph_start + len(paragraph_lines) - 1,
                raw,
                "list" if is_list_item else "paragraph",
                section in protected_sections,
            )
        )
        paragraph_lines = []

    for number, raw_line in enumerate(lines, start=1):
        line = raw_line.rstrip("\n")
        if re.match(r"^\s*(```|~~~)", line):
            flush()
            in_fence = not in_fence
            fence_start = number if in_fence else fence_start
            if not in_fence:
                blocks.append(TextBlock(fence_start, number, "", "fence"))
            continue
        if in_fence:
            continue

        heading = re.match(r"^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$", line)
        if heading:
            flush()
            section = heading.group(1).strip().lower()
            continue
        if not line.strip() or line.lstrip().startswith("<!--"):
            flush()
            continue
        if re.match(r"^\s*\|.*\|\s*$", line):
            flush()
            blocks.append(TextBlock(number, number, line, "table", section in protected_sections))
            continue
        if re.match(r"^\s*(?:[-*+]\s+|\d+[.)]\s+)", line) and paragraph_lines:
            flush()
        if not paragraph_lines:
            paragraph_start = number
        paragraph_lines.append(line)

    flush()
    return blocks


def fixed_strings_from_style(style_text: str) -> dict[str, str]:
    found: dict[str, str] = {}
    for match in re.finditer(r"^\s*-\s*(F[1-4]):\s*[\"“](.*?)[\"”]\s*$", style_text, re.MULTILINE):
        found[match.group(1)] = match.group(2)
    return found


def protected_sections_for(path: Path) -> set[str]:
    if path.name != "HOUSE-STYLE.md":
        return set()
    return {
        "fixed strings — dedicated block, per rule 11",
        "technical verbs — the operational set",
    }


def is_caption(line: str) -> bool:
    stripped = line.strip()
    return bool(
        re.match(r"(?i)^(?:figure|fig\.|table|caption)\s*\d*\s*[:.-]", stripped)
        or re.search(r"(?i)<figcaption\b|</figcaption>", stripped)
        or re.match(r"!\[[^]]*\]\([^)]*\)", stripped)
    )


def formatter_container(line: str, in_fence: bool) -> str | None:
    """Return the formatter-owned container on a line, if one is clear."""

    if in_fence:
        return "fenced code"
    if re.match(r"^\s*\|.*\|\s*$", line):
        return "table cell"
    if is_caption(line):
        return "caption"
    if re.match(r"^(?: {4,}|\t)", line):
        return "indented code"
    if re.search(r"`[^`]*`", line):
        return "inline code"
    if re.search(r"(?i)<(?:code|pre|figure|figcaption|table)\b|</(?:code|pre|figure|figcaption|table)>", line):
        return "HTML formatter container"
    return None


def fixed_string_findings(path: Path, lines: Sequence[str], fixed: dict[str, str]) -> list[Finding]:
    findings: list[Finding] = []
    in_fence = False
    for number, raw_line in enumerate(lines, start=1):
        line = raw_line.rstrip("\n")
        if re.match(r"^\s*(```|~~~)", line):
            in_fence = not in_fence
        for label, value in fixed.items():
            if value in line:
                container = formatter_container(line, in_fence)
                if container:
                    findings.append(
                        Finding(
                            path,
                            number,
                            "fixed-string placement",
                            f"{label} occurs in a {container}: {line.strip()!r}",
                            "fixed strings occur only in running text or a dedicated block",
                        )
                    )

            # A near-match is evidence that a contract was edited. Use the
            # placement rule when the near-match sits in a formatter-owned
            # container, because both parts of rule 11 then fail.
            variant = FIXED_STRING_VARIANT_PATTERNS[label].search(line)
            if variant and value not in line:
                container = formatter_container(line, in_fence)
                rule = "fixed-string placement" if container else "fixed-string integrity"
                expected = (
                    "the fixed string must occur verbatim in running text or a dedicated block"
                    if container
                    else f"{label} is {value!r}, verbatim"
                )
                findings.append(
                    Finding(
                        path,
                        number,
                        rule,
                        f"near-match for {label}: {variant.group(0)!r}",
                        expected,
                    )
                )

        # A contract declaration in HOUSE-STYLE.md must remain exact. This
        # catches an edited F1-F4 line even though the edited value is no
        # longer equal to the expected string.
        if path.name == "HOUSE-STYLE.md":
            declaration = re.match(r"^\s*-\s*(F[1-4]):\s*[\"“](.*?)[\"”]\s*$", line)
            if declaration and declaration.group(1) in DECLARED_FIXED_STRINGS:
                label, actual = declaration.groups()
                expected = DECLARED_FIXED_STRINGS[label]
                if actual != expected:
                    findings.append(
                        Finding(
                            path,
                            number,
                            "fixed-string integrity",
                            f"{label} is {actual!r}",
                            f"{label} is {expected!r}, verbatim",
                        )
                    )

    return findings


def gate_verb_findings(path: Path, lines: Sequence[str], blocks: Iterable[TextBlock]) -> list[Finding]:
    findings: list[Finding] = []
    protected_ranges = {(block.start_line, block.end_line) for block in blocks if block.protected}

    def protected(number: int) -> bool:
        return any(start <= number <= end for start, end in protected_ranges)

    for number, raw_line in enumerate(lines, start=1):
        if protected(number):
            continue
        line = raw_line.rstrip("\n")
        # Participles are unambiguous verb forms. The remaining patterns are
        # conservative signals for a direct object after GATE/GATES.
        matches = list(re.finditer(r"\b(?:gated|gating)\b", line, re.IGNORECASE))
        matches += list(
            re.finditer(
                r"\b(?:gate|gates)\s+(?:a|an|the|this|that|each|every|all|it|them|us|requests?|changes?|releases?|files?|text|work)\b",
                line,
                re.IGNORECASE,
            )
        )
        matches += list(
            re.finditer(
                r"\b(?:to|will|can|may|must|should|do|does|did|not)\s+gate\b",
                line,
                re.IGNORECASE,
            )
        )
        seen: set[tuple[int, int]] = set()
        for match in matches:
            key = (match.start(), match.end())
            if key in seen:
                continue
            seen.add(key)
            findings.append(
                Finding(
                    path,
                    number,
                    "GATE used as a verb",
                    f"{match.group(0)!r} in {line.strip()!r}",
                    "use GATE as a noun; use FREEZE for the act",
                )
            )
    return findings


def prose_findings(path: Path, lines: Sequence[str], blocks: Iterable[TextBlock]) -> list[Finding]:
    findings: list[Finding] = []
    for block in blocks:
        if block.kind in {"fence", "table"} or block.protected or not block.text.strip():
            continue
        spans = sentence_spans(block.text)
        if len(spans) > MAX_SENTENCES_PER_PARAGRAPH:
            findings.append(
                Finding(
                    path,
                    block.start_line,
                    "paragraph sentence limit",
                    f"paragraph contains {len(spans)} sentences",
                    f"at most {MAX_SENTENCES_PER_PARAGRAPH} sentences per paragraph",
                )
            )
        # A list item is a separate paragraph for sentence limits, but the
        # declared one-instruction-per-line rule still applies below.
        for start, end in spans:
            sentence = clean_sentence(block.text[start:end])
            count = word_count(sentence)
            limit = MAX_INSTRUCTION_WORDS if is_instruction(sentence) else MAX_DESCRIPTION_WORDS
            kind = "instruction" if limit == MAX_INSTRUCTION_WORDS else "descriptive sentence"
            if count > limit:
                findings.append(
                    Finding(
                        path,
                        line_for_offset(block.text, block.start_line, start),
                        f"{kind} word limit",
                        f"{count} words: {sentence!r}",
                        f"at most {limit} words per {kind}",
                    )
                )

    # One instruction per physical line. Only lines with two or more
    # recognizable imperative sentences are findings; descriptive sentences
    # are not penalized by this rule.
    protected_lines = {
        number
        for block in blocks
        if block.kind in {"fence", "table"} or block.protected
        for number in range(block.start_line, block.end_line + 1)
    }
    for number, raw_line in enumerate(lines, start=1):
        line = raw_line.strip()
        if number in protected_lines or not line or line.startswith("#") or line.startswith("|"):
            continue
        sentences = [line[start:end] for start, end in sentence_spans(line)]
        if sum(is_instruction(sentence) for sentence in sentences) > 1:
            findings.append(
                Finding(
                    path,
                    number,
                    "one instruction per line",
                    f"{sum(is_instruction(sentence) for sentence in sentences)} instructions: {line!r}",
                    "place one instruction on each line",
                )
            )
    return findings


def assay_file(path: Path, style_fixed: dict[str, str]) -> list[Finding]:
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        return [Finding(path, 1, "input", f"cannot read file: {error}", "a readable UTF-8 Markdown file")]
    lines = text.splitlines(keepends=True)
    blocks = markdown_blocks(lines, protected_sections_for(path))
    findings = []
    findings.extend(prose_findings(path, lines, blocks))
    findings.extend(gate_verb_findings(path, lines, blocks))
    findings.extend(fixed_string_findings(path, lines, style_fixed))
    return findings


def markdown_paths(root: Path) -> list[Path]:
    return sorted(
        path
        for path in root.rglob("*.md")
        if ".git" not in path.parts and ".DS_Store" not in path.parts
    )


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Read-only assayer for the concrete rules in HOUSE-STYLE.md."
    )
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        help="Markdown files or directories to assay (default: the repository).",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    root = Path(__file__).resolve().parent
    style_path = root / "HOUSE-STYLE.md"
    try:
        style_fixed = fixed_strings_from_style(style_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError) as error:
        print(f"ERROR cannot read {style_path}: {error}", file=sys.stderr)
        return 2
    if style_fixed != DECLARED_FIXED_STRINGS:
        # The integrity findings below make the mismatch inspectable. Keep
        # running so the user receives the complete evidence set.
        style_fixed = {**DECLARED_FIXED_STRINGS, **style_fixed}

    requested = args.paths or [root]
    files: list[Path] = []
    for requested_path in requested:
        if requested_path.is_dir():
            files.extend(markdown_paths(requested_path))
        elif requested_path.suffix.lower() == ".md":
            files.append(requested_path)
        else:
            print(f"ERROR expected a Markdown file or directory: {requested_path}", file=sys.stderr)
            return 2
    files = sorted(set(files))

    findings: list[Finding] = []
    for path in files:
        findings.extend(assay_file(path, style_fixed))

    print(f"ASSAY {len(files)} Markdown file(s)")
    if findings:
        print(f"STATUS FINDINGS ({len(findings)})")
        for finding in findings:
            print(finding.render())
        return 1
    print("STATUS PASS")
    print("evidence: no concrete HOUSE-STYLE rule violations found")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
