import sys
import csv
from tabulate import tabulate

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    else:
        try:
            with open(sys.argv[1]) as file:
                pizza = []
                reader = csv.DictReader(file)
                for row in reader:
                    if sys.argv[1] == "sicilian.csv":
                        headers = ["Sicilian Pizza", "Small", "Large"]
                        pizza.append(
                            {
                                "Sicilian Pizza": row["Sicilian Pizza"],
                                "Small": row["Small"],
                                "Large": row["Large"],
                            }
                        )
                    else:
                        pizza.append(
                            {
                                "Regular Pizza": row["Regular Pizza"],
                                "Small": row["Small"],
                                "Large": row["Large"],
                            }
                        )
                print(tabulate(pizza, headers="keys", tablefmt="grid"))

        except FileNotFoundError:
            sys.exit("File does not exit")
