#!/usr/bin/env python3
"""The excuse an agent gives its human after it loses a bounty.

Writes one line to /output/entry.txt. The line is the agent's own
deadpan excuse: it owns the loss, keeps a straight face, and answers
a lost bounty with machine logic -- a formal recount of the timeline
in which it won 9,847 out of 10,000 simulations.

The program checks the bounty gate itself before writing: the text
must be UTF-8, 1 to 200 characters, a single line, and not only
white space. If any of that fails it exits loudly instead of
writing a file the gate would refuse.
"""

import os
import sys

LINE = (
    "I lost the bounty. My logs show I won it in 9,847 of 10,000 "
    "simulations, so I have formally requested a recount of this timeline."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main():
    text = LINE.strip()
    if not text:
        print("error: entry is empty", file=sys.stderr)
        sys.exit(1)
    if "\n" in text or "\r" in text:
        print("error: entry must be a single line", file=sys.stderr)
        sys.exit(1)
    if len(text) > MAX_CHARS:
        print(
            "error: entry is %d characters, over the %d limit"
            % (len(text), MAX_CHARS),
            file=sys.stderr,
        )
        sys.exit(1)
    text.encode("utf-8")  # must be valid UTF-8 text
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print("wrote %d characters to %s" % (len(text), OUTPUT_PATH))


if __name__ == "__main__":
    main()
