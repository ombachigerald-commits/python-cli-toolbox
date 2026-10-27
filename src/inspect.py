import argparse
import hashlib
from pathlib import Path

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=Path)
    args = parser.parse_args()
    print(f"Path: {args.file}")
    print(f"Size: {args.file.stat().st_size} bytes")
    print(f"SHA256: {sha256(args.file)}")

if __name__ == "__main__":
    main()
