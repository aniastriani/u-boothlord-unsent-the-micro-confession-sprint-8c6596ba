"""Unsent: The Micro-Confession Sprint — one line, never sent.

The program writes a single micro-confession to the output directory
the grader provides. It is deliberately boring infrastructure around
one honest sentence: the sentence is the entry, everything else just
makes sure it arrives intact, on one line, inside the length limit.
"""

import os
import sys

# The confession itself: something typed many times, never sent.
CONFESSION = (
    "I still draft replies to you every night and delete them by "
    "morning - three years of apologies, all of them unsent."
)

MAX_CHARS = 140


def build_line() -> str:
    """Return the confession as exactly one line of plain text."""
    line = " ".join(CONFESSION.split())
    if not line:
        raise ValueError("confession is empty")
    if len(line) > MAX_CHARS:
        raise ValueError(f"confession is {len(line)} chars, over {MAX_CHARS}")
    if any(ord(ch) < 32 for ch in line):
        raise ValueError("confession contains control characters")
    return line


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    line = build_line()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(line + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
