import argparse
import csv
from pathlib import Path

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=Path)
    parser.add_argument("-n", type=int, default=5)
    args = parser.parse_args()

    with args.file.open(newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i >= args.n: break
            print(" | ".join(row))

if __name__ == "__main__":
    main()
