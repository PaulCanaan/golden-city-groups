"""Build the Weekly Recap chat PDF and send Paul's Sunday-evening reminder."""

import argparse
from datetime import date, datetime
import html
from pathlib import Path
import re
import subprocess
import tempfile
import time
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[1]
INBOX = ROOT / "06 Resources/Resource Inbox"
RECAPS = ROOT / "06 Resources/Group Life/Weekly Recaps"
ZONE = ZoneInfo("America/Denver")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
BRAND = ROOT / "06 Resources/Brand"

# Groups resource style: see 06 Resources/Brand/Groups Resource Style.md.
STYLE = """
@font-face { font-family: Roboto; src: url("FONT"); font-weight: 100 900; }
@font-face { font-family: Roboto; src: url("ITALIC"); font-weight: 100 900; font-style: italic; }
@page { size: letter; margin: 0.5in 0.75in 0.45in; }
body { margin: 0; font: 10.5pt/1.45 Roboto, "Helvetica Neue", sans-serif; letter-spacing: -0.01em; color: #1C1C1C; }
header { display: flex; justify-content: space-between; align-items: flex-end;
         padding-bottom: 9pt; border-bottom: 1.5pt solid #CCB079; }
header img { height: 19pt; display: block; }
.label { text-align: right; font-size: 7.5pt; font-weight: 600; letter-spacing: .16em; text-transform: uppercase;
         color: #857230; line-height: 1.6; }
.label span { display: block; font-size: 9pt; font-weight: 400; letter-spacing: 0; text-transform: none; color: #5C5C5C; }
h1 { font-size: 26pt; font-weight: 700; letter-spacing: -0.02em; line-height: 1.1; margin: 15pt 0 3pt; }
.meta { color: #5C5C5C; margin: 0; }
h2 { font-size: 8pt; font-weight: 600; letter-spacing: .16em; text-transform: uppercase; color: #857230; margin: 15pt 0 5pt; }
p { margin: 0 0 .45em; }
.summary { background: #F7F4EC; border-radius: 4pt; padding: 9pt 12pt; margin: 0; }
.passage { font-weight: 500; }
ol { margin: 0; padding-left: 1.4em; }
li { margin: 0 0 .4em; padding-left: .25em; }
li::marker { color: #857230; font-weight: 600; }
.closing { margin-top: 14pt; color: #5C5C5C; font-style: italic; }
footer { position: fixed; bottom: 0; left: 0; right: 0; display: flex; justify-content: space-between;
         padding-top: 5pt; border-top: .5pt solid #E2E2E2; font-size: 7.5pt; letter-spacing: .02em; color: #6B6B6B; }
"""


def inline(text):
    text = html.escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    return re.sub(r"\*(.+?)\*", r"<em>\1</em>", text)


def front_matter(markdown):
    match = re.match(r"\A---\n(.*?)\n---\n", markdown, re.S)
    meta = {}
    for line in match.group(1).splitlines() if match else []:
        key, _, value = line.partition(":")
        meta[key.strip()] = value.strip().strip('"')
    return meta, markdown[match.end():] if match else markdown


def to_html(markdown):
    meta, body = front_matter(markdown)
    day = date.fromisoformat(meta["message_date"]) if meta.get("message_date") else None
    when = f"<span>{day:%B} {day.day}, {day.year}</span>" if day else ""
    parts = [f'<header><img src="{(BRAND / "groups-logo.png").as_uri()}" alt="Groups">'
             f'<div class="label">Weekly Recap{when}</div></header>']
    section = ""
    for block in re.split(r"\n\s*\n", body.strip()):
        lines = block.strip().splitlines()
        text = " ".join(lines)
        if lines[0].startswith("## "):
            section = lines[0][3:]
            parts.append(f"<h2>{inline(section)}</h2>")
        elif lines[0].startswith("# "):
            parts.append(f"<h1>{inline(lines[0][2:])}</h1>")
            details = [f"<em>{html.escape(meta['series'])}</em>"] * bool(meta.get("series"))
            details += [html.escape(meta["passage"])] * bool(meta.get("passage"))
            parts.append(f'<p class="meta">{" · ".join(details)}</p>')
        elif text.startswith("**Weekly Recap"):
            continue  # shown in the header instead
        elif all(re.match(r"\d+\. ", line) for line in lines):
            items = "".join(f"<li>{inline(line.split('. ', 1)[1])}</li>" for line in lines)
            parts.append(f"<ol>{items}</ol>")
        else:
            kind = ("closing" if re.fullmatch(r"\*[^*].*\*", text) else
                    {"This Week's Message": "summary", "Read Together": "passage"}.get(section, ""))
            parts.append(f'<p class="{kind}">{inline(text)}</p>')
    parts.append("<footer><span>Golden City Church · Groups</span><span>goldencity.church</span></footer>")
    style = STYLE.replace("FONT", (BRAND / "fonts/Roboto[wdth,wght].ttf").as_uri()).replace(
        "ITALIC", (BRAND / "fonts/Roboto-Italic[wdth,wght].ttf").as_uri())
    return f"<!doctype html><meta charset=utf-8><style>{style}</style>{''.join(parts)}"


def build_pdf(recap):
    pdf = recap.with_suffix(".pdf")
    pdf.unlink(missing_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        page = Path(tmp) / "recap.html"
        page.write_text(to_html(recap.read_text()))
        chrome = subprocess.Popen([CHROME, "--headless", "--disable-gpu", "--no-first-run",
                                   "--no-pdf-header-footer", f"--user-data-dir={tmp}/chrome",
                                   f"--print-to-pdf={pdf}", page.as_uri()],
                                  stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        # Chrome can linger after writing the PDF, so stop once the file is complete.
        for _ in range(120):
            if chrome.poll() is not None or (pdf.exists() and pdf.read_bytes().rstrip().endswith(b"%%EOF")):
                break
            time.sleep(0.5)
        chrome.kill()
        chrome.wait()
    if not pdf.exists():
        raise SystemExit(f"Chrome did not produce {pdf}")
    return pdf


def reminder(day, inbox=INBOX, recaps=RECAPS):
    """Return the Sunday reminder for `day`, or None when nothing is needed."""
    if day.weekday() != 6:
        return None
    stamp = day.isoformat()
    recap = next(recaps.glob(f"{stamp} *.md"), None)
    if recap:
        if re.search(r"^status:\s*Posted\s*$", recap.read_text(), re.M):
            return None
        return "This week's Weekly Recap is drafted but not posted yet."
    if any(inbox.glob(f"{stamp} *")):
        return "Russ's script is in the Resource Inbox. Run /weekly-recap to draft this week's recap."
    return "No sermon script in the Resource Inbox yet. Drop Russ's script there so the agent can draft this week's Weekly Recap."


def self_test():
    with tempfile.TemporaryDirectory() as tmp:
        inbox, recaps = Path(tmp, "inbox"), Path(tmp, "recaps")
        inbox.mkdir(), recaps.mkdir()
        sunday = date(2026, 10, 11)
        assert reminder(date(2026, 10, 12), inbox, recaps) is None
        assert "No sermon script" in reminder(sunday, inbox, recaps)
        Path(inbox, "2026-10-04 Old.docx").touch()
        assert "No sermon script" in reminder(sunday, inbox, recaps)
        Path(inbox, "2026-10-11 Title.docx").touch()
        assert "Run /weekly-recap" in reminder(sunday, inbox, recaps)
        recap = Path(recaps, "2026-10-11 Title.md")
        recap.write_text("---\nstatus: Draft\n---\n")
        assert "not posted" in reminder(sunday, inbox, recaps)
        recap.write_text("---\nstatus: Posted\n---\n")
        assert reminder(sunday, inbox, recaps) is None
    page = to_html('---\nmessage_date: 2026-10-04\nseries: "S"\npassage: "P 1:1"\nstatus: Draft\n---\n\n'
                   "# Title\n\n**Weekly Recap · x**\n\n## This Week's Message\n\nSome **bold** and *it*.\n\n"
                   "## Discuss\n\n1. One?\n2. <Two>?\n\n*Closing.*\n")
    assert "<h1>Title</h1>" in page and "<span>October 4, 2026</span>" in page and "<em>S</em> · P 1:1" in page
    assert '<p class="summary">Some <strong>bold</strong> and <em>it</em>.</p>' in page
    assert "<ol><li>One?</li><li>&lt;Two&gt;?</li></ol>" in page and '<p class="closing">' in page
    assert "Weekly Recap · x" not in page and "status" not in page
    print("Checks passed: reminder states and Markdown rendering.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("pdf", help="Build the chat PDF next to a recap").add_argument("recap", type=Path)
    sub.add_parser("check", help="Print today's reminder without notifying")
    sub.add_parser("remind", help="Show today's reminder as a macOS notification")
    sub.add_parser("self-test")
    args = parser.parse_args()
    if args.command == "self-test":
        self_test()
    elif args.command == "pdf":
        print(build_pdf(args.recap.resolve()))
    else:
        message = reminder(datetime.now(ZONE).date())
        print(message or "Nothing to remind.")
        if message and args.command == "remind":
            subprocess.run(["osascript", "-e", "on run argv", "-e",
                            'display notification (item 1 of argv) with title "Weekly Recap" sound name "Glass"',
                            "-e", "end run", message], check=True)


if __name__ == "__main__":
    main()
