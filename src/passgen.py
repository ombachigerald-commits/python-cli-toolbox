import argparse
import secrets
import string

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--length", type=int, default=16)
    args = parser.parse_args()
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
    password = "".join(secrets.choice(alphabet) for _ in range(args.length))
    print(password)

if __name__ == "__main__":
    main()
