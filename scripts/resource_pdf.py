"""Print resource HTML without replacing a usable PDF on render failure."""

from pathlib import Path
import subprocess
from tempfile import TemporaryDirectory
import time


CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


def complete_pdf(path):
    if not path.is_file():
        return False
    with path.open("rb") as pdf:
        if pdf.read(5) != b"%PDF-":
            return False
        pdf.seek(max(0, path.stat().st_size - 1024))
        return pdf.read().rstrip().endswith(b"%%EOF")


def render_pdf(html, destination):
    destination = Path(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    # Keep the candidate on the destination filesystem for atomic replacement.
    with TemporaryDirectory(prefix=".resource-pdf-", dir=destination.parent) as directory:
        workspace = Path(directory).resolve()
        page = workspace / "resource.html"
        candidate = workspace / "resource.pdf"
        page.write_text(html, encoding="utf-8")
        command = [
            CHROME, "--headless", "--disable-gpu", "--no-first-run",
            "--no-default-browser-check", "--disable-extensions",
            "--no-pdf-header-footer", f"--user-data-dir={workspace / 'chrome'}",
            f"--print-to-pdf={candidate}", page.as_uri(),
        ]
        try:
            chrome = subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except OSError as error:
            raise SystemExit(f"Could not start Chrome to render {destination}: {error}") from error
        try:
            deadline = time.monotonic() + 60
            while chrome.poll() is None and not complete_pdf(candidate) and time.monotonic() < deadline:
                time.sleep(0.25)
        finally:
            status = chrome.poll()
            # Chrome can linger after finishing a print job.
            if status is None:
                chrome.kill()
            chrome.wait()
        if status not in (0, None) or not complete_pdf(candidate):
            raise SystemExit(f"Chrome did not produce a complete PDF for {destination}")
        candidate.replace(destination)
    return destination
