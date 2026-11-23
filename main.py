"""Entry for make.fun — One-Line Laugh Sprint.

The program writes one original funny line about everyday life
to /output/entry.txt. Nothing else is written, no network, no tricks.
"""

LINE = "I set five alarms to wake up early. All five of us slept in."


def main() -> None:
    # Guard the gate: the line must stay within the 200-character cap.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    # One line, one file: the grader reads /output/entry.txt.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
