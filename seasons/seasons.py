import datetime
import inflect
import re
import sys

p = inflect.engine()


def main():
    print(calc_date(input("Date of Birth: ")))



def calc_date(inputdata):
    if matches := re.search(r"^(\d{4})-([0-1]?\d)-([0-3]?\d)$", inputdata):
        year, month, day = matches.groups()
        if 1 > int(month) > 12 or 1 > int(day) > 31:
            sys.exit("Invalid date")
        inputdata = datetime.date(int(year), int(month), int(day))
    else:
        sys.exit("Invalid date")
    today = datetime.date.today()
    newdate = today - inputdata
    return convert_to_minutes_str(newdate)


def convert_to_minutes_str(newdate):
    minutes = int(newdate.days) * 24 * 60
    return f"{p.number_to_words(minutes, andword="")} minutes".capitalize()


if __name__ == "__main__":
    main()
