#!/usr/bin/env python3
"""One Line, No Deadline Met.

Writes a single-line joke giving an excuse for a missed deadline to
/output/entry.txt. Standard library only, fully deterministic: the same
line every run, one line, well under the 200-character cap.
"""

import os

LINE = "I outsourced the deadline to Future Me, and Future Me just ghosted me."


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = LINE.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")
    # Read back and verify: exactly one line, within the cap.
    with open(os.path.join(out_dir, "entry.txt"), "r", encoding="utf-8") as f:
        written = f.read()
    assert written == text + "\n", "entry.txt does not match the line"
    assert written.count("\n") == 1, "entry must be exactly one line"


if __name__ == "__main__":
    main()
