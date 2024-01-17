import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.fullmatch(r"(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})", ip):
        for n in matches.groups():
            if int(n) > 255:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()
