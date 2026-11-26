"""Entry for the make.fun bounty "The Moon Finally Answers Back".

Writes the Moon's one-line comeback to /output/entry.txt.
Deterministic: no network, no randomness, no time dependence.
"""

import os

ENTRY = "Your wish is number 8,000,000,001 in the queue. Estimated wait time: one eclipse."

MAX_LENGTH = 240


def main() -> None:
    line = ENTRY
    if not line or not line.strip():
        raise ValueError("entry must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_LENGTH:
        raise ValueError(f"entry is {len(line)} characters, over the {MAX_LENGTH} limit")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
