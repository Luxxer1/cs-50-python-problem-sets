def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    while True:
        date = input("Date: ").split()
        if len(date) == 3:
            month, day, year = date
            if months.count(month.title()) > 0 and day.count(",") > 0:
                day = day.strip(" ,")
                if 1 < int(day) > 31:
                    pass
                else:
                    month = months.index(month.title()) + 1
                    print(f"{year}-{int(month):02}-{int(day):02}")
                    break
        else:
            month, day, year = date[0].split("/")
            month = month.strip(" ")
            year = year.strip(" ")
            try:
                if 1 < int(day) > 31 or 1 < int(month) > 12:
                    pass
                else:
                    print(f"{year}-{int(month):02}-{int(day):02}")
                    break
            except ValueError:
                pass


main()
