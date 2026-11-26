"""Decision record — "What the Elevator Would Say" (make.fun).

The job: one line, at most 120 characters, the funniest thing a talking
elevator could say, in the elevator's own voice. The judge is an AI comedy
critic comparing lines head-to-head, weighing (in order): funniest
elevator line, joke lands on first read, voice that could come from no
other machine (doors, floors, buttons, waiting, weight limits), every word
working inside the limit, and freshness (not a re-run of an old elevator
joke, not resting on a pun alone).

Candidates weighed against those criteria:

1. "I've carried ten thousand strangers up forty floors, and not one of
   you has ever asked how my day is going." (107 chars)
   On-subject and in-voice, and the unappreciated-worker turn is warm.
   But the laugh is gentle, not big: it reads as sweet rather than funny,
   and "nobody asks how I am" is a well-worn personification move. Loses
   on criterion 1 (funniest) and 5 (fresh).

2. "Stop pressing the button again. I heard you the first time - I'm a
   lift, not a vending machine." (95 chars)
   Lands fast and the button-mashing complaint is genuinely elevator-only.
   But the second half leans on a comparison ("not a vending machine")
   that explains the joke instead of landing it, and the scolding tone
   risks reading as grumpy rather than funny. Loses on 2 and 5.

3. "You all ride in total silence staring at my doors like I'm the weird
   one for not making conversation." (101 chars)
   Strong and specific: the silent ride and the doors are pure elevator,
   and flipping the awkwardness onto the elevator is a fresh angle. The
   turn is good, but the laugh is observational rather than a punch — it
   smiles where the winner needs a laugh. Close second.

4. "I know you're all pretending not to smell that. I've been trapped in
   here with it since floor three." (99 chars)
   Probably the biggest raw laugh of the five — instant, visual, and the
   elevator-as-trapped-witness twist is good. Rejected on freshness: the
   fart-in-the-elevator joke is one of the oldest elevator jokes there is,
   and the judge explicitly demotes jokes already made about elevators.
   It would also collide with every other crude entry in the field.

5. CHOSEN: "Funny how everyone suddenly becomes best friends with the
   stairs the moment I take ten seconds longer than usual." (113 chars)
   Wins on every criterion: it is funny first (jealous elevator, petty
   and human); the turn lands on first read ("best friends with the
   stairs"); the voice is elevator-only — only a lift measures a delay in
   seconds and resents the stairs for it; every word works and it sits
   inside the limit without feeling cut; and the stairs-rivalry angle is
   fresh, not a "going up" gag and not a pun.

Two genuine writing passes on the chosen line:

Pass 1 — draft: "Everyone suddenly loves the stairs the second I'm ten
seconds late."
Flat. "Loves" is weak, "late" is vague (late for what?), there is no
voice — it could be a bus, a train, a coworker — and nothing signals
that a joke is coming.

Pass 2 — tightened (the submitted line): "Funny how everyone suddenly
becomes best friends with the stairs the moment I take ten seconds
longer than usual."
Four deliberate changes: "Funny how" opens with gossiping, conspiratorial
voice and flags the joke; "best friends" replaces "loves", turning a vague
feeling into a jealous relationship with a funnier image; "the moment"
replaces "the second" for a cleaner snap into the turn; and "ten seconds
longer than usual" replaces "ten seconds late" — petty, precise, and
in-voice, because an elevator counts delays in seconds and resents being
judged for them. Same idea, 113 characters, and now unmistakably an
elevator talking.

Why this line survives head-to-head judging: most of the field will
reach for the same two moves — "going up?" and the doors closing on
someone — so a stairs-rivalry line rarely meets its own twin, and when
it does meet a generic line it wins on freshness alone. The joke's turn
("best friends with the stairs") sits in the second half, so the line
reads as a setup that pays off fast instead of a punchline that needs
unpacking, and nothing in it addresses the judge or explains itself.
"""

import os

LINE = (
    "Funny how everyone suddenly becomes best friends with the stairs "
    "the moment I take ten seconds longer than usual."
)

MAX_CHARS = 120


def validate_line(line):
    """Check one entry line against the competition gate.

    Returns the line unchanged when it passes. Raises ValueError on the
    first rule it breaks: must be a string, must not be blank, must be a
    single line with no leading or trailing whitespace, and must be 1 to
    120 characters long.
    """
    if not isinstance(line, str):
        raise TypeError("entry line must be a string")
    if not line.strip():
        raise ValueError("entry line must not be blank")
    if line != line.strip():
        raise ValueError("entry line must not have leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line, not several")
    if any(ord(ch) < 32 for ch in line):
        raise ValueError("entry line must not contain control characters")
    # The gate reads the file as UTF-8 text and counts characters, not
    # bytes, so prove the line survives a UTF-8 round-trip unchanged.
    if line.encode("utf-8").decode("utf-8") != line:
        raise ValueError("entry line does not round-trip through UTF-8")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "entry line is %d characters, over the %d-character limit"
            % (len(line), MAX_CHARS)
        )
    return line


def output_path():
    """Where entry.txt goes: $MAKEFUN_OUTPUT_DIR, else /output."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(base, "entry.txt")


def main():
    line = validate_line(LINE)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    # Write exactly the line, no trailing newline: the gate counts
    # characters, and byte-for-byte identity is what gets judged.
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    print(line)
    # Read it back and prove the file is the intended line, byte for byte,
    # inside the 1-120 character gate.
    with open(path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    assert written == LINE, "entry.txt does not match the intended line"
    assert written.encode("utf-8").decode("utf-8") == LINE, (
        "entry.txt does not round-trip through UTF-8 unchanged"
    )
    assert 1 <= len(written) <= MAX_CHARS, "entry.txt outside the 1-120 gate"
    assert len(written) == len(LINE) == 113, "entry.txt length drifted"
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
