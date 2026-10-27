import argparse
from pathlib import Path

def print_tree(directory: Path, prefix=""):
    print(prefix + directory.name + "/")
    for child in directory.iterdir():
        if child.is_dir():
            print_tree(child, prefix + "    ")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("dir", type=Path, default=".")
    args = parser.parse_args()
    print_tree(args.dir)

if __name__ == "__main__":
    main()
