#!/usr/bin/env python3
"""One-line-joke entrypoint: write the fridge-alibi line to /output/entry.txt."""

import os

# One short funny line answering an appliance-excuse prompt.
ENTRY = (
    "I turned off the light to eat your yoghurt "
    "\u2014 darkness is an excellent alibi.\n"
)

OUTPUT_PATH = "/output/entry.txt"


def write_entry() -> bytes:
    """Write the exact entry bytes to OUTPUT_PATH and return them."""
    data = ENTRY.encode("utf-8")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(data)
    return data


if __name__ == "__main__":
    written = write_entry()
    print(f"wrote {len(written)} bytes to {OUTPUT_PATH}")
