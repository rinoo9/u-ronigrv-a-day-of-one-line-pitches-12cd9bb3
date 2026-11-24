"""One-line pitch entry for the make.fun bounty 'A Day of One-Line Pitches'.

Writes a single persuasive sentence to /output/entry.txt.
Deterministic: no network, no randomness, no environment reads.

Round 3: new hook — the idea stuck in the notes app (230 chars);
opens on the stale-notes image instead of the months-carrying question.

Round 4: new hook — the app that works exactly the way you think
(208 chars). Rounds 1-3 all opened from "you have an idea, describe it";
this one flips the angle to the reader's frustration that no app-store
app fits the way they think, then reveals the missing app already
exists in their head — it just hasn't been built yet. The em-dash
turn turns a complaint into an invitation, and the close keeps the
free-to-try, no-coding-needed call to action.
"""

import os

PITCH = "Somewhere out there is an app that works exactly the way you think — it just hasn't been built yet. Describe it in plain words and an AI will build it for you on make.fun today, free to try, no coding needed."


def main() -> None:
    assert 1 <= len(PITCH) <= 240
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
