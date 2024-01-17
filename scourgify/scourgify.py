import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    else:
        try:
            with open(sys.argv[1]) as file:
                students = []
                reader = csv.DictReader(file)
                for row in reader:
                    last, first = row["name"].split(", ")
                    students.append(
                        {"first": first, "last": last, "house": row["house"]}
                    )

            with open(sys.argv[2], "w") as file:
                writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
                writer.writeheader()
                for student in students:
                    writer.writerow(student)

        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")
