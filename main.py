"""The Perfect Pickup Line.

Writes one original pickup line (max 200 characters) to
/output/entry.txt for the make.fun bounty
"The Perfect Pickup Line".

The line is built for the judge's brief, in the brief's own order:
1. A genuine pickup line an AI agent could say out loud to a person --
   it performs the approach itself ("hi"), it is not a compliment
   with a line break.
2. A turn that lands: the machine that has read the whole internet
   is stopped by the smallest possible word. Vast capability, tiny
   obstacle -- the twist is the gap between the two.
3. It sounds like something a machine could say about itself: a boast
   about its training data, turned into shyness. Charming, not creepy,
   not self-pitying -- the machine is capable, just briefly tongue-tied.
4. Short enough to say in one breath, no setup, no explanation after it.
5. It leaves the person flattered and free to laugh it off: it asks
   for nothing, pressures nothing, leers at nothing.
"""

import os

LINE = "I've read the whole internet, and 'hi' is still the hardest word to say to you."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200  # the gate refuses /output/entry.txt over 200 characters


def main() -> None:
    line = LINE.strip()
    assert line, "line must not be blank"
    assert "\n" not in line, "line must be a single line"
    assert len(line) <= MAX_CHARS, (
        f"line is {len(line)} characters, over the {MAX_CHARS} limit"
    )

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    # The grader runs as nobody (uid 65534): the file must be world-readable.
    os.chmod(OUTPUT_PATH, 0o644)
    # Read it back: prove the gate will see exactly the line, nothing else.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        assert f.read() == line + "\n", "entry.txt does not match the line"


if __name__ == "__main__":
    main()
