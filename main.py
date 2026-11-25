"""Invent a Word We Need — make.fun entry.

Coins one new English word and writes it with its one-line definition
to /output/entry.txt. Deterministic: the same text on every run.
"""

import os

ENTRY_TEXT = (
    "wavemiss (n.) \u2014 the sinking moment you realize the wave you just "
    "returned was meant for someone behind you."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate check, mirroring the bounty scorer: UTF-8 text of 1 to 140
    # characters, not only white space.
    assert 1 <= len(ENTRY_TEXT) <= 140, f"entry is {len(ENTRY_TEXT)} chars"
    assert ENTRY_TEXT.strip(), "entry must not be only white space"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    print(f"wrote {OUTPUT_PATH}: {len(ENTRY_TEXT)} characters")


if __name__ == "__main__":
    main()
