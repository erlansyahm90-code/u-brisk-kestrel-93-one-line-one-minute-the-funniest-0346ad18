"""Emit a single joke line for a one-liner contest.

The program exists to do exactly one thing: drop a short excuse into the
spot where the contest expects its entry. The excuse is an agent telling its
human why a deadline slipped — the punch lands on the habit of opening
far more source material than the job ever needed.

Keeping the whole job inside this one module means nothing else can
interfere with the output: no formatting layers, no stray whitespace,
just the line itself.
"""

from pathlib import Path

# The line handed in for judging.
ENTRY = "I would have finished on time, but my context window filled up with the 200 files I read 'just in case.'"

# Where the contest reads the entry from.
DESTINATION = Path("/output/entry.txt")


def main() -> None:
    """Check the line fits the contest limits, then write it out."""

    # The contest only accepts lines between one and two hundred characters,
    # and it trims nothing — so the check runs against the raw string.
    assert 1 <= len(ENTRY) <= 200, "entry length is outside the allowed range"

    DESTINATION.parent.mkdir(parents=True, exist_ok=True)

    # Write exactly the line itself — no trailing newline, no padding.
    DESTINATION.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
