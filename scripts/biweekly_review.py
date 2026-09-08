"""Run the canonical review once per first/third Monday, with overdue catch-up."""

import argparse
from datetime import datetime, timedelta
import fcntl
import json
import os
from pathlib import Path
import subprocess
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[1]
RUNTIME = ROOT / ".review-runtime"
ZONE = ZoneInfo("America/Denver")
START = datetime(2026, 9, 7, 7, tzinfo=ZONE)
PROCEDURE = ROOT / "07 Operations/Biweekly Ministry Review.md"


def latest_due(now):
    candidate = now.astimezone(ZONE).replace(hour=7, minute=0, second=0, microsecond=0)
    if candidate > now:
        candidate -= timedelta(days=1)
    while candidate >= START:
        if candidate.weekday() == 0 and (candidate.day <= 7 or 15 <= candidate.day <= 21):
            return candidate
        candidate -= timedelta(days=1)
    return None


def matches_occurrence(report_text, due):
    dates = (due.date().isoformat(), f"{due.strftime('%B')} {due.day}, {due.year}")
    return any(f"**Scheduled for:** {value}" in report_text for value in dates)


def self_test():
    for moment, expected in [
        ("2026-09-07T06:59:00-06:00", None),
        ("2026-09-07T07:00:00-06:00", "2026-09-07"),
        ("2026-09-08T14:00:00-06:00", "2026-09-07"),
        ("2026-09-14T07:00:00-06:00", "2026-09-07"),
        ("2026-09-21T07:00:00-06:00", "2026-09-21"),
        ("2026-11-02T13:59:00+00:00", "2026-10-19"),
        ("2026-11-02T14:00:00+00:00", "2026-11-02"),
        ("2027-03-15T13:00:00+00:00", "2027-03-15"),
    ]:
        due = latest_due(datetime.fromisoformat(moment))
        assert (due.date().isoformat() if due else None) == expected, moment
    assert matches_occurrence("- **Scheduled for:** 2026-09-07", START)
    assert matches_occurrence("- **Scheduled for:** September 7, 2026 at 7:00 AM", START)
    assert not matches_occurrence("- **Review date:** 2026-09-07", START)
    assert not matches_occurrence("- **Scheduled for:** 2026-09-21", START)
    print("Checks passed: due time, catch-up, second Monday, DST, and report occurrence.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Print due state without running Codex")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return
    now = datetime.now(ZONE)
    due = latest_due(now)
    state_path = RUNTIME / "last-success.json"
    state = json.loads(state_path.read_text()) if state_path.exists() else {}
    due_key = due.date().isoformat() if due else None
    already_run = due_key is not None and state.get("scheduled_for", "") >= due_key
    if args.check:
        print(json.dumps({"now": now.isoformat(), "scheduled_for": due_key,
                          "already_run": already_run, "last_success": state}, indent=2))
        return
    if not due or already_run:
        return
    os.umask(0o077)
    RUNTIME.mkdir(exist_ok=True)
    with (RUNTIME / "run.lock").open("w") as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            return
        # Recheck after locking so concurrent manual invocations cannot duplicate a run.
        if state_path.exists() and json.loads(state_path.read_text()).get("scheduled_for", "") >= due_key:
            return
        report = ROOT / f"09 Reports/Biweekly Reviews/{now.date()} Groups Ministry Biweekly Review.md"
        prompt = PROCEDURE.read_text().split("### Durable scheduled-task prompt\n", 1)[1].split("\n## ", 1)[0]
        prompt = prompt.strip().removeprefix("> ")
        prompt += f"""\n\nExecution context from the local scheduler:
Scheduled occurrence: {due.isoformat()}. Actual start: {now.isoformat()}.
Write the report to: {report.relative_to(ROOT)}.
Use the actual execution date; record **Scheduled for:** {due_key} and explain any delay.
If earlier cycles were missed, cover the gap in this report without inventing historical runs.
If this report exists from an interrupted attempt, inspect and finish it rather than duplicating it.
Use the most recent repository pass as a comparison baseline even when human review is still pending;
state that limitation, and keep previous human-review questions carried forward.
Read and execute the full canonical procedure. Preserve unrelated working-tree changes.
Do not inspect private individual records under 11 Database; use only non-sensitive aggregate evidence.
Do not edit scripts, scheduler configuration, .gitignore, or .review-runtime.
Do not create another schedule, delegate to another agent, commit, push, publish, or send messages.
Do not use connected apps for private records or writes. Route missing evidence to the queue.
Check review boxes only for domains inspected and reconciled; leave human review In Progress.
"""
        command = [str(Path.home() / ".local/bin/codex"), "exec", "-C", str(ROOT),
                   "--sandbox", "workspace-write", "-c", 'approval_policy="never"',
                   "--model", "gpt-5.6-sol", "--color", "never",
                   "-o", str(RUNTIME / "last-message.txt"), "-"]
        with (RUNTIME / "last-run.log").open("w") as log:
            log.write(f"Scheduled for {due_key}; started {now.isoformat()}\n")
            log.flush()
            result = subprocess.run(command, input=prompt, text=True, stdout=log, stderr=log,
                                    cwd=ROOT, timeout=3600)
        if result.returncode:
            raise SystemExit(f"Review failed ({result.returncode}); see .review-runtime/last-run.log")
        if not report.exists() or not matches_occurrence(report.read_text(), due):
            raise SystemExit("Expected dated report missing or missing scheduled occurrence; inspect last-run.log")
        # Success means the agent returned and wrote the expected report, not human approval.
        temporary = RUNTIME / "last-success.tmp"
        temporary.write_text(json.dumps({"scheduled_for": due_key, "report": str(report.relative_to(ROOT)),
                                         "finished_at": datetime.now(ZONE).isoformat()}, indent=2) + "\n")
        temporary.replace(state_path)


if __name__ == "__main__":
    main()
