"""Validate the notebook-style research/voice handoff using only the stdlib."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def main():
    report = (ROOT / "reports/latest.md").read_text(encoding="utf-8")
    match = re.search(r"Run ID: `([A-Za-z0-9_-]+)`", report)
    if not match:
        raise SystemExit("Missing or invalid run ID")
    run = ROOT / "runs" / match.group(1)
    for name in ("activity_log.md", "literature_evidence.md", "gap_assessment.md",
                 "study_protocol.md", "feasibility_matrix.csv", "briefing.md"):
        if not (run / name).is_file():
            raise SystemExit(f"Missing artifact: {name}")
    if report != (run / "briefing.md").read_text(encoding="utf-8"):
        raise SystemExit("Latest report differs from preserved briefing")
    if not re.search(r"Verification phrase: `[^`]+`", report):
        raise SystemExit("Missing verification phrase")
    speech = report.split("## Spoken briefing\n", 1)[1].split("\n## References", 1)[0]
    count = len(speech.split())
    if not 500 <= count <= 650:
        raise SystemExit(f"Briefing must be 500–650 words; found {count}")
    for link in re.findall(r"\]\(([^)]+)\)", report):
        if not link.startswith(("https://", "http://", "#")):
            if not (ROOT / "reports" / link).resolve().is_file():
                raise SystemExit(f"Broken local link: {link}")
    print(f"Validated {match.group(1)}: six artifacts, matching report, {count} spoken words.")


if __name__ == "__main__":
    main()
