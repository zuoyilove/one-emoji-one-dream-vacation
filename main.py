"""One Emoji, One Dream Vacation -- make.fun entry (program/v1).

The program writes exactly one emoji to /output/entry.txt: the emoji
for the entrant's dream vacation. The judge compares entries two at a
time and picks the one that most makes a stranger want to book the
trip.

Choice: the desert island, U+1F3DD + U+FE0F.

Why this emoji, against the judge's brief, most important first:
1. It is exactly one emoji, no words, and it lands on a dream
   vacation: a deserted tropical island, the faraway place.
2. It evokes the trip vividly at a glance, like a postcard: a
   stranger sees the island, the palm, the empty beach before
   reading a word.
3. It feels personal and specific rather than generic: it points at
   one particular dream -- escape to an island with nobody else on
   it -- not just any holiday.
4. It carries a spark of wit: the dream is not a resort, it is
   getting away from everyone, island and all.
5. It reads instantly across cultures and screens, clear at small
   size, and needs no explaining.

The gate is 1 to 8 UTF-8 characters, not only whitespace; the emoji
is 2 characters in Python (base + variation selector), written with
no trailing newline, so the file holds the emoji and nothing else.
"""

import os
import sys

EMOJI = "\U0001f3dd\ufe0f"
MIN_LEN = 1
MAX_LEN = 8


def main() -> int:
    emoji = EMOJI
    if not (MIN_LEN <= len(emoji) <= MAX_LEN):
        raise SystemExit(
            "emoji length %d outside gate [%d, %d]" % (len(emoji), MIN_LEN, MAX_LEN)
        )
    if emoji.strip() == "":
        raise SystemExit("entry must not be only whitespace")
    if any(ch.isspace() for ch in emoji):
        raise SystemExit("entry must contain no whitespace at all")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(emoji)
    return 0


if __name__ == "__main__":
    sys.exit(main())
