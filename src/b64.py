import argparse
import base64

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["encode", "decode"])
    parser.add_argument("text")
    args = parser.parse_args()

    if args.action == "encode":
        print(base64.b64encode(args.text.encode()).decode())
    else:
        print(base64.b64decode(args.text.encode()).decode())

if __name__ == "__main__":
    main()
