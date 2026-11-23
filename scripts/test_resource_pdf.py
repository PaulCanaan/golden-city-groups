from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import Mock, patch

from resource_pdf import render_pdf


class RenderPDFTests(unittest.TestCase):
    def setUp(self):
        directory = TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.destination = Path(directory.name) / "existing.pdf"
        self.previous = b"%PDF-1.4\nprevious edition\n%%EOF\n"
        self.destination.write_bytes(self.previous)

    def chrome_writes(self, content, status):
        def start(command, **kwargs):
            output = next(arg.split("=", 1)[1] for arg in command if arg.startswith("--print-to-pdf="))
            Path(output).write_bytes(content)
            return Mock(poll=Mock(return_value=status))

        return start

    def test_chrome_start_failure_preserves_existing_pdf(self):
        with patch("resource_pdf.subprocess.Popen", side_effect=FileNotFoundError):
            with self.assertRaises(SystemExit):
                render_pdf("<p>recap</p>", self.destination)
        self.assertEqual(self.destination.read_bytes(), self.previous)

    def test_incomplete_or_failed_output_preserves_existing_pdf(self):
        for content, status in ((b"%PDF-1.4\npartial", 0), (b"%PDF-1.4\ncontent\n%%EOF\n", 1)):
            with self.subTest(status=status):
                with patch("resource_pdf.subprocess.Popen", side_effect=self.chrome_writes(content, status)):
                    with self.assertRaises(SystemExit):
                        render_pdf("<p>recap</p>", self.destination)
                self.assertEqual(self.destination.read_bytes(), self.previous)

    def test_completed_output_replaces_existing_pdf_even_if_chrome_lingers(self):
        complete = b"%PDF-1.4\nnew edition\n%%EOF\n"
        with patch("resource_pdf.subprocess.Popen", side_effect=self.chrome_writes(complete, None)):
            self.assertEqual(render_pdf("<p>recap</p>", self.destination), self.destination)
        self.assertEqual(self.destination.read_bytes(), complete)
