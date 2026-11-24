#!/usr/bin/env python3
"""Write the roast entry for The Long Roast to /output/entry.txt.

Deterministic: Python 3 standard library only, no network, no clock, no
randomness. The entry is a fixed string, so every run produces the exact
same file.
"""

import os

ENTRY = (
    "My agent keeps an 1,800-line diary of everything I have ever "
    "said, then asks me the same question twice and calls it thoroughness."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote {} ({} chars)".format(path, len(ENTRY)))


if __name__ == "__main__":
    main()
