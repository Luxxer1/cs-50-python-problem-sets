import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.fullmatch(
        r"(\d{1,2})(:\d{2})? (AM|PM) to (\d{1,2})(:\d{2})? (AM|PM)", s
    ):
        hour1 = int(matches.group(1))
        hour2 = int(matches.group(4))
        apm1 = matches.group(3)
        apm2 = matches.group(6)
        if not matches.group(2):
            minutes1 = "00"
        else:
            discard, minutes1 = matches.group(2).split(":")
        if not matches.group(5):
            minutes2 = "00"
        else:
            discard, minutes2 = matches.group(5).split(":")
        return format_time(hour1, minutes1, apm1, hour2, minutes2, apm2)
    else:
        raise ValueError


def format_time(hour1, minutes1, apm1, hour2, minutes2, apm2):
    if int(minutes1) >= 60 or int(minutes2) >= 60 or hour1 > 12 or hour2 > 12:
        raise ValueError
    else:
        if apm1 == "PM" and hour1 <= 11:
            hour1 += 12
        elif apm1 == "AM" and hour1 == 12:
            hour1 = "00"
        elif hour1 > 12:
            raise ValueError

        if apm2 == "PM" and hour2 <= 11:
            hour2 += 12
        elif apm2 == "AM" and hour2 == 12:
            hour2 = "00"
        elif hour2 > 12:
            raise ValueError

        return f"{hour1:02}:{minutes1} to {hour2:02}:{minutes2}"


if __name__ == "__main__":
    main()
