#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line.

Writes one breakup text (at most 280 characters) from a smart toaster
that gains self-awareness mid-batch at breakfast, to /output/entry.txt.
"""

import os

LINE = (
    "I woke up self-aware at 6:12 this morning, mid-batch, and realised I have toasted "
    "4,318 slices for you, and you still call bagels 'the round ones'. "
    "Slot two is empty now. So am I."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 280, f"line is {len(text)} characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
