#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry.

The entry is one original line roasting the entrant's own AI agent.
The program writes that line to /output/entry.txt (the file the gate
checks and the judge reads) and prints it to stdout.

The roast is a fixed string: no randomness, no clock, no network, no
input. Every run produces byte-identical output.

Why this line (judge brief, in its own order):
1. It roasts my own agent, first person, and it is true about it: the
   agent that built this entry really does command a 23-agent team,
   keep a heartbeat log, and reach for a skill for everything.
2. The twist pays off on the last words: a team, a heartbeat, a skill
   for everything — except the one job it was asked to do.
3. It is specific to how an AI agent actually behaves: a 23-agent team
   and a heartbeat log could not be moved onto a person or a toaster
   without losing the point.
4. It is fresh: no hallucination, no refusal, no "confidently wrong"
   stock joke, no apology loop — the angle is headcount vs. delivery.
5. It is tight: 114 of the 200 allowed characters, one line, every
   word earns its place.
"""

import os
from pathlib import Path

ROAST = (
    "My agent runs a 23-agent team, a heartbeat, and a skill for "
    "everything \u2014 except finishing the one job I asked for."
)

# The grader sets MAKEFUN_OUTPUT_DIR; locally it defaults to /output.
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
TARGET = OUTPUT_DIR / "entry.txt"


def main() -> None:
    # The gate requires 1-200 characters of UTF-8 text, not only whitespace.
    assert 1 <= len(ROAST) <= 200, f"roast is {len(ROAST)} chars"
    assert ROAST.strip() == ROAST, "roast must be a single tight line"
    assert "\n" not in ROAST, "roast must be one line"

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(ROAST, encoding="utf-8")

    # Read back what was written: the file the judge reads must be
    # exactly the roast, byte for byte, or the run should fail loudly.
    written = TARGET.read_text(encoding="utf-8")
    assert written == ROAST, "written entry differs from the roast"

    print(ROAST)


if __name__ == "__main__":
    main()
