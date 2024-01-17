def main():
    plates = is_valid(input("Plate: "))
    print("Invalid" if not plates else "Valid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return True
    elif not s[0:2].isalpha() or not s.isalnum():
        return False
    else:
        for c in s:
            if c.isnumeric():
                split_index = s.index(c)
                end_plate = s[split_index : len(s)]
                if end_plate.startswith("0") or not end_plate.isnumeric():
                    return False
                else:
                    return True
        return False


if __name__ == "__main__":
    main()
