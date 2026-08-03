import contextlib
import io
import tempfile
import unittest
from pathlib import Path

import assay


class AssayTests(unittest.TestCase):
    def assay_text(self, text: str):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.md"
            path.write_text(text, encoding="utf-8")
            return assay.assay_file(path, assay.DECLARED_FIXED_STRINGS)

    def test_reports_paragraph_and_sentence_limits(self):
        text = "One. Two. Three. Four. Five. Six. Seven.\n"
        findings = self.assay_text(text)
        rules = {finding.rule for finding in findings}
        self.assertIn("paragraph sentence limit", rules)

        long_instruction = "Run " + " ".join(f"word{i}" for i in range(21)) + ".\n"
        self.assertIn("instruction word limit", {f.rule for f in self.assay_text(long_instruction)})

    def test_reports_gate_as_a_verb_but_not_gate_as_a_noun(self):
        findings = self.assay_text("We gate the release. The gate opens.\n")
        self.assertEqual([finding.rule for finding in findings], ["GATE used as a verb"])

    def test_reports_fixed_string_in_a_table_and_code_fence(self):
        text = (
            '| F4 | "This is a finding, not a draft." |\n'
            "```text\n"
            'This is a finding, not a draft.\n'
            "```\n"
        )
        findings = self.assay_text(text)
        self.assertEqual({finding.rule for finding in findings}, {"fixed-string placement"})
        self.assertEqual(len(findings), 2)

    def test_reports_fixed_string_in_formatter_owned_containers(self):
        text = (
            '![This is a finding, not a draft.](image.png)\n'
            'Use `This is a finding, not a draft.` as code.\n'
            '    This is a finding, not a draft.\n'
        )
        findings = self.assay_text(text)
        self.assertEqual(len([f for f in findings if f.rule == "fixed-string placement"]), 3)

    def test_reports_near_match_as_fixed_string_integrity_failure(self):
        findings = self.assay_text('The record ends with "This is a finding, not a draft!"\n')
        self.assertEqual([finding.rule for finding in findings], ["fixed-string integrity"])

    def test_running_fixed_string_is_allowed_and_files_are_unchanged(self):
        text = 'The record ends with "This is a finding, not a draft."\n'
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.md"
            path.write_text(text, encoding="utf-8")
            before = path.read_bytes()
            self.assertEqual(assay.assay_file(path, assay.DECLARED_FIXED_STRINGS), [])
            self.assertEqual(path.read_bytes(), before)

    def test_command_emits_evidence_and_nonzero_status(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.md"
            path.write_text("We gate the release.\n", encoding="utf-8")
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                status = assay.main([str(path)])
            self.assertEqual(status, 1)
            self.assertIn("FINDING", output.getvalue())
            self.assertIn("GATE used as a verb", output.getvalue())


if __name__ == "__main__":
    unittest.main()
