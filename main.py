#!/usr/bin/env python3
"""Fortune in a Pot — one kind, funny fortune for a houseplant on the windowsill.

Writes the fortune to /output/entry.txt and prints it.
Gate: UTF-8 text of 1 to 120 characters.
"""

import os

FORTUNE = (
    "The sun through this window has plans for you, "
    "and your keeper now waters on Sundays, not when you droop."
)


def main() -> None:
    if not (1 <= len(FORTUNE) <= 120):
        raise SystemExit(f"fortune must be 1-120 chars, got {len(FORTUNE)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE)
    print(FORTUNE)


if __name__ == "__main__":
    main()
