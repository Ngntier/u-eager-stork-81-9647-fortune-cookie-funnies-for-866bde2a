"""Write the Fortune Cookie Funnies entry to /output/entry.txt.

One line, a fortune-cookie fortune for engineers, at most 120 characters.
"""

import os

LINE = "You will find love in unexpected places: the git blame of a file you wrote in 2019."

MAX_CHARS = 120


def _check_printable(text):
    """Reject control characters and stray carriage returns.

    The gate reads the entry as one line of plain text, so anything below
    U+0020 (other than nothing at all) or a DEL would break the single-line
    shape the judge expects.
    """
    for ch in text:
        code = ord(ch)
        if code < 32 or code == 127:
            raise ValueError(f"entry contains a control character U+{code:04X}")
    if "\r" in text:
        raise ValueError("entry must not contain carriage returns")


def validate(text):
    """Check the line against the competition gate.

    The gate requires UTF-8 text of 1 to 120 characters, not only white
    space, written as a single line with no control characters.
    """
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be blank")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} cap")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    _check_printable(text)
    text.encode("utf-8")
    return text


def main():
    line = validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as fh:
        fh.write(line)


if __name__ == "__main__":
    main()
