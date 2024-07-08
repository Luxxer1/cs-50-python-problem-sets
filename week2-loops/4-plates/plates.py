def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    elif not s[0:2].isalpha() or not s.isalnum():
        return False
    else:
        return check_numbers(s)


def check_numbers(s):
    for c in s:
        if c.isnumeric():
            split_index = s.index(c)
            end_plate = s[split_index:len(s)]
            if end_plate.startswith("0") or not end_plate.isnumeric():
                return False
            else:
                return True
    return True

main()
