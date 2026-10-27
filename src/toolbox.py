import argparse
import sys
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="Master CLI")
    sub = parser.add_subparsers(dest="cmd", required=True)
    
    p_wc = sub.add_parser("wc")
    p_wc.add_argument("file", type=Path)

    args = parser.parse_args()
    
    if args.cmd == "wc":
        print("Running word count on", args.file)

if __name__ == "__main__":
    main()
