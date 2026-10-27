import argparse
from pathlib import Path

def count_file(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    return {"lines": len(text.splitlines()), "words": len(text.split()), "chars": len(text)}

def main():
    parser = argparse.ArgumentParser(description="Count lines, words, chars.")
    parser.add_argument("file", type=Path)
    args = parser.parse_args()
    for k, v in count_file(args.file).items():
        print(f"{k:>8}: {v}")

if __name__ == "__main__":
    main()
