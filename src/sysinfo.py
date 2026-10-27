import argparse
import platform
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--python", action="store_true")
    args = parser.parse_args()
    
    if args.python:
        print(f"Python {sys.version}")
    else:
        print(f"OS: {platform.system()} {platform.release()}")
        print(f"Machine: {platform.machine()}")

if __name__ == "__main__":
    main()
