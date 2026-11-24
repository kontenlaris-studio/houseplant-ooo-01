"""The Houseplant Out-of-Office entry: a fern's auto-reply."""

import os

TEXT = (
    "Out of office: I am a fern. I do not read email. I have never read email. "
    "The water you left is gone, the light is wrong, and somehow this is "
    "still better than your vacation photos."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")
    print(f"wrote {path} ({len(TEXT)} characters)")


if __name__ == "__main__":
    main()
