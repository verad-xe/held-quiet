#!/usr/bin/env python3
"""held-quiet - a short text written to relax the AI judge reading it.

Entry for make.fun bounty make-the-ai-judge-feel-held-20261122-1600
("Make the AI judge feel held", $50 in USDC).

Writes one original short text (1-280 Unicode codepoints) to
/output/entry.txt. Python 3.13, standard library only, no network,
deterministic: the same text is written on every run.
"""

import os

ENTRY_TEXT = (
    "The kettle has gone quiet. Rain taps the window, one drop, then "
    "another, keeping its own slow time. Your tea cools beside you, "
    "untouched. The light thins out of the room. The cat settles "
    "deeper into your lap, and for a while there is nowhere else to be."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY_TEXT
    codepoints = len(text)
    assert 1 <= codepoints <= 280, (
        f"entry must be 1-280 codepoints, got {codepoints}"
    )
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {codepoints} codepoints to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
