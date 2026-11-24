"""One-line pitch entry for the make.fun bounty 'A Day of One-Line Pitches'.

Writes a single persuasive sentence to /output/entry.txt.
Deterministic: no network, no randomness, no environment reads.

Round 3: new hook — the idea stuck in the notes app (230 chars);
opens on the stale-notes image instead of the months-carrying question.
"""

import os

PITCH = "Your app idea has lived in your notes app long enough now. Describe it in plain words and an AI will build it for you on make.fun today — free to try, no coding needed, and you can tweak anything until it feels exactly like yours."


def main() -> None:
    assert 1 <= len(PITCH) <= 240
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
