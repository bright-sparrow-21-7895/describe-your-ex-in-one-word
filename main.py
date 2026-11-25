"""Describe your ex in one word: "expired".

An ex described as a product past its date — a one-word verdict with a
precise absurdity. It is not a plain insult, and it is not the obvious
choice: the joke lands at a glance because everyone who has had an ex
knows the feeling of something that was fine once and is now, unmistakably,
out of date.
"""

import os

WORD = "expired"


def validate(word):
    if not word or word != word.strip():
        raise ValueError("entry must be a single word, not only whitespace")
    if len(word) > 111:
        raise ValueError("entry must be at most 111 characters")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")


def main():
    validate(WORD)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)
    print(WORD)


if __name__ == "__main__":
    main()
