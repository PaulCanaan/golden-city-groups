"""Print a Collective Galatians handout markdown file to PDF.

Reuses the Groups resource style from scripts/weekly_recap.py. The handout
markdown is the editable source: page breaks, writing lines, and the Scripture
credit are explicit comments in that file.
"""

import argparse
from datetime import date
import html
from pathlib import Path
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
BRAND = ROOT / "06 Resources/Brand"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

STYLE = """
@font-face { font-family: Roboto; src: url("FONT"); font-weight: 100 900; }
@font-face { font-family: Roboto; src: url("ITALIC"); font-weight: 100 900; font-style: italic; }
@page { size: letter; margin: 0.48in 0.68in 0.42in; }
body { margin: 0; font: 10.5pt/1.45 Roboto, "Helvetica Neue", sans-serif; letter-spacing: -0.01em; color: #1C1C1C; }
.sheet { display: flex; flex-direction: column; min-height: 9.85in; break-after: page; }
.sheet:last-child { break-after: auto; }
.sheet .body { flex: 1 1 auto; }
header { display: flex; justify-content: space-between; align-items: flex-end;
         padding-bottom: 8pt; border-bottom: 1.5pt solid #CCB079; }
header img { height: 19pt; display: block; }
.label { text-align: right; font-size: 7.5pt; font-weight: 600; letter-spacing: .16em; text-transform: uppercase;
         color: #857230; line-height: 1.45; }
.label span { display: block; font-size: 9pt; font-weight: 400; letter-spacing: 0; text-transform: none; color: #5C5C5C; }
h1 { font-size: 26pt; font-weight: 700; letter-spacing: -0.02em; line-height: 1.05; margin: 12pt 0 2pt; }
.kicker { color: #5C5C5C; margin: 0 0 2pt; }
h3 { font-size: 13pt; font-weight: 700; letter-spacing: -0.01em; margin: 13pt 0 1pt; }
h3 + .kicker, h3 + p.sub { font-size: 9.5pt; color: #5C5C5C; margin: 0 0 4pt; }
h2 { font-size: 8pt; font-weight: 600; letter-spacing: .16em; text-transform: uppercase; color: #857230; margin: 11pt 0 4pt; }
p { margin: 0 0 .42em; }
.read p { margin: 0 0 .32em; }
.credit { margin-top: 8pt; font-size: 8pt; line-height: 1.35; color: #6B6B6B; }
ol { margin: 2pt 0 0; padding-left: 1.35em; }
li { margin: 0 0 .38em; padding-left: .2em; }
li::marker { color: #857230; font-weight: 600; }
sup.v { font-size: 7.5pt; font-weight: 600; color: #857230; line-height: 0; margin-right: 1px; }
.lines { margin-top: 4pt; }
.lines div { border-bottom: .6pt solid #E2E2E2; height: 15.5pt; }
footer { display: flex; justify-content: space-between; margin-top: 10pt; padding-top: 5pt;
         border-top: .5pt solid #E2E2E2; font-size: 7.5pt; letter-spacing: .02em; color: #6B6B6B; }
"""


def inline(text):
    text = html.escape(text)
    text = re.sub(r"\*\*(\d+)\*\*", r'<sup class="v">\1</sup>', text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    return re.sub(r"\*(.+?)\*", r"<em>\1</em>", text)


def session_label(study_id):
    """G02 is Session 2 (one chapter per session); G01A/G01B keep the earlier two-per-chapter numbering."""
    match = re.fullmatch(r"G(\d+)([AB])?", study_id or "")
    if not match:
        return ""
    number = int(match.group(1))
    if match.group(2):
        number = (number - 1) * 2 + (1 if match.group(2) == "A" else 2)
    return f"Session {number}"


def front_matter(markdown):
    match = re.match(r"\A---\n(.*?)\n---\n", markdown, re.S)
    meta, body = {}, markdown
    if match:
        body = markdown[match.end():]
        for line in match.group(1).splitlines():
            key, _, value = line.partition(":")
            meta[key.strip()] = value.strip().strip('"')
    return meta, body


def chunks(page):
    pieces, buf = [], []

    def flush():
        if buf:
            pieces.append("\n".join(buf))
            buf.clear()

    for line in page.strip().splitlines():
        if line.strip().startswith("<!--"):
            flush()
            pieces.append(line.strip())
        elif not line.strip():
            flush()
        else:
            buf.append(line)
    flush()
    return pieces


def blocks(page):
    parts = []
    credit_next = False
    after_title = False
    for block in chunks(page):
        lines = [line for line in block.splitlines() if line.strip()]
        if not lines:
            continue
        if lines[0].startswith("<!--"):
            comment = " ".join(lines)
            if "scripture-credit" in comment:
                credit_next = True
            found = re.search(r"writing-lines:\s*(\d+)", comment)
            if found:
                rows = "".join("<div></div>" for _ in range(int(found.group(1))))
                parts.append(f'<div class="lines">{rows}</div>')
            continue
        if lines[0].startswith("### "):
            parts.append(f"<h3>{inline(lines[0][4:])}</h3>")
            after_title = True
        elif lines[0].startswith("## "):
            parts.append(f"<h2>{inline(lines[0][3:])}</h2>")
            after_title = False
        elif lines[0].startswith("# "):
            parts.append(f"<h1>{inline(lines[0][2:])}</h1>")
            after_title = True
        elif all(re.match(r"\d+\. ", line) for line in lines):
            items = "".join(f"<li>{inline(line.split('. ', 1)[1])}</li>" for line in lines)
            parts.append(f"<ol>{items}</ol>")
            after_title = False
        else:
            text = inline(" ".join(lines))
            if credit_next:
                parts.append(f'<p class="credit">{text}</p>')
                credit_next = False
            elif after_title:
                parts.append(f'<p class="kicker">{text}</p>')
                after_title = False
            else:
                parts.append(f"<p>{text}</p>")
    return "".join(parts)


def to_html(markdown):
    meta, body = front_matter(markdown)
    when = date.fromisoformat(meta["gathering_date"])
    label = (f'<div class="label">{html.escape(meta["audience"])}'
             f'<span>{session_label(meta.get("study_id"))} · {when:%B} {when.day}, {when.year}</span></div>')
    header = (f'<header><img src="{(BRAND / "groups-logo.png").as_uri()}" alt="Groups">{label}</header>')
    pages = re.split(r"<!--\s*pagebreak\s*-->", body)
    sheets = []
    total = len(pages)
    for number, page in enumerate(pages, start=1):
        read = ' class="body read"' if "Read Together" in page else ' class="body"'
        footer = (f'<footer><span>Golden City Church · Groups</span>'
                  f'<span>goldencity.church · {number} / {total}</span></footer>')
        sheets.append(f'<section class="sheet">{header}<div{read}>{blocks(page)}</div>{footer}</section>')
    style = STYLE.replace("FONT", (BRAND / "fonts/Roboto[wdth,wght].ttf").as_uri()).replace(
        "ITALIC", (BRAND / "fonts/Roboto-Italic[wdth,wght].ttf").as_uri())
    return f"<!doctype html><meta charset=utf-8><style>{style}</style>{''.join(sheets)}"


def build_pdf(source, destination):
    destination = Path(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.unlink(missing_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        page = Path(tmp) / "handout.html"
        page.write_text(to_html(Path(source).read_text()))
        subprocess.run(
            [CHROME, "--headless=new", "--disable-gpu", "--no-first-run", "--no-default-browser-check",
             "--disable-extensions", "--no-pdf-header-footer", f"--user-data-dir={tmp}/chrome",
             f"--print-to-pdf={destination}", page.as_uri()],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=60, check=False)
    if not destination.exists():
        raise SystemExit(f"Chrome did not produce {destination}")
    return destination


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source")
    parser.add_argument("destination")
    args = parser.parse_args()
    print(build_pdf(args.source, args.destination))


if __name__ == "__main__":
    main()
