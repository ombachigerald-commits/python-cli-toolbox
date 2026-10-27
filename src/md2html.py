import argparse
import re

def convert(md: str) -> str:
    html = re.sub(r"^# (.+)$", r"<h1>\1</h1>", md, flags=re.M)
    html = re.sub(r"^## (.+)$", r"<h2>\1</h2>", html, flags=re.M)
    return html

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()
    with open(args.file) as f:
        print(convert(f.read()))

if __name__ == "__main__":
    main()
