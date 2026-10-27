import argparse
import json
from pathlib import Path

def count_file(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    return {"lines": len(text.splitlines()), "words": len(text.split()), "chars": len(text)}

def main():
    parser = argparse.ArgumentParser(description="Count lines, words, chars.")
    parser.add_argument("file", type=Path)
    parser.add_argument("--json", action="store_true", help="Output as JSON") # <-- NEW
    args = parser.parse_args()
    
    result = count_file(args.file)
    
    if args.json:
        print(json.dumps(result))
    else:
        for k, v in result.items():
            print(f"{k:>8}: {v}")

if __name__ == "__main__":
    main()
