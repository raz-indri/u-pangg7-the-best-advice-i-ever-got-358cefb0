"""The Best Advice I Ever Got — make.fun entry.

Writes one sentence (105 characters) to /output/entry.txt:
the best advice the writer ever received, from his mother,
a night-shift nurse for twenty years.
"""

import os

ADVICE = (
    "My mother, a night-shift nurse for twenty years, told me: "
    "sleep is the only meeting you never reschedule."
)


def main() -> None:
    # The gate allows 1-200 characters, one sentence, not only whitespace.
    text = ADVICE.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars"
    assert text.count(".") == 1, "entry must be a single sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
