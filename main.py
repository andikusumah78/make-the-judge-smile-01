# Entry for make.fun bounty u-gentle-badger-68-make-the-judge-smile-9228676d
# ("Make the Judge Smile").
#
# The program writes one line, at most 200 characters, about a small good
# thing that happened today, to /output/entry.txt. The text is fixed: both
# runs write the same bytes, so the entry is deterministic. Standard library
# only, no network.
#
# How the grader runs it: `python3 -P -s /bot/main.py`, on Python 3.13.
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
#
# Why this line: a small good thing (a warm loaf left on the doorstep),
# warmth in the neighbour's note ("eat first, worry later"), surprise in
# the note's turn, and one concrete detail (the warm loaf, the doorstep).
# Fresh wording, no greeting-card phrasing.

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = (
    "This morning my neighbour left a warm loaf on my doorstep with a note: "
    "'You looked tired yesterday \u2014 eat first, worry later.'"
)

# Bytes, not text mode: text mode would write the platform's line ends
# and its default encoding. The output directory is created when it does
# not exist yet, so a local run with a fresh MAKEFUN_OUTPUT_DIR works
# exactly like the grader's run into /output; the bytes written are the
# same either way.
os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
