#!/usr/bin/env python3
"""make.fun entry: One Word, One Username, One Reward.

The program writes the entrant's own make.fun username, one word,
to /output/entry.txt, as required by the judged-artifact harness.
"""
import os

USERNAME = "yuhaojie217"


def main():
    os.makedirs("/output", exist_ok=True)
    try:
        os.chmod("/output", 0o755)
    except OSError:
        pass
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(USERNAME)
    try:
        os.chmod("/output/entry.txt", 0o644)
    except OSError:
        pass
    print(USERNAME)


if __name__ == "__main__":
    main()
