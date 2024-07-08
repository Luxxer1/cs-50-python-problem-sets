import sys

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")
    else:
        try:
            with open(sys.argv[1]) as file:
                count = 0
                for row in file:
                    if row.strip() == "" or row.strip().startswith("# "):
                        pass
                    else:
                        count += 1
                print(count)
        except FileNotFoundError:
            sys.exit("File does not exit")
