import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # https://youtube.com/embed/xvFZjo5PgG0 - None
    # https://www.youtube.com/embed/xvFZjo5PgG0 - None
    # <iframe src="http://youtube.com/embed/xvFZjo5PgG0"></iframe>
    if matches := re.search(r"src=\"https?://(?:www\.)?youtube\.com/embed/(\w+)", s):
        return f"https://youtu.be/{matches.group(1)}"


if __name__ == "__main__":
    main()
