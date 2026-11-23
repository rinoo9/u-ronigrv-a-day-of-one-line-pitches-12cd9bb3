"""One-line pitch entry for the make.fun bounty 'A Day of One-Line Pitches'.

Writes a single persuasive sentence to /output/entry.txt.
Deterministic: no network, no randomness, no environment reads.
"""

import os

PITCH = "Just tell me the app idea you've been carrying around in plain words, and I'll have an AI build it for you on make.fun today — free to try, no coding needed, and you can change anything you don't like until it feels like yours."


def main() -> None:
    assert 1 <= len(PITCH) <= 240
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
