#!/usr/bin/env python3
"""One-line-joke entrypoint: write the fridge-alibi line to /output/entry.txt."""

import os
import sys

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


def read_back() -> bytes:
    """Read OUTPUT_PATH back from disk as raw bytes."""
    with open(OUTPUT_PATH, "rb") as handle:
        return handle.read()


def check() -> int:
    """Write the entry, read it back, and report whether the bytes match."""
    expected = write_entry()
    actual = read_back()
    if actual == expected:
        print(f"MATCH {len(actual)} bytes")
        return 0
    print(f"MISMATCH expected {len(expected)} bytes, read {len(actual)} bytes")
    return 1


if __name__ == "__main__":
    if "--check" in sys.argv[1:]:
        raise SystemExit(check())
    written = write_entry()
    print(f"wrote {len(written)} bytes to {OUTPUT_PATH}")
