#!/usr/bin/env python3
"""One Star, Written in Sap — entry generator.

Writes a single one-line 1-star review from a houseplant about its
human owner to /output/entry.txt. Deterministic, stdlib only.
"""

import os

ENTRY = (
    "★☆☆☆☆ He waters me every Sunday whether I'm thirsty or drowning, "
    "then moved me to the windowsill for one photo in March and never put "
    "me back — 214 days of direct sun, and he still calls it 'good light.'"
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
