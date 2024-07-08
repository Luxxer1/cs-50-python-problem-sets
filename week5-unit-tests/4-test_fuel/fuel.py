def main():
    while True:
        try:
            result = convert(input("Fraction: "))
            break
        except (ValueError, ZeroDivisionError):
            pass

    print(gauge(result))


def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)
    if x > y and y != 0:
        raise ValueError
    else:
        return round((x / y) * 100)


def gauge(percentage):
    if(percentage >= 99):
        return "F"
    elif(percentage <= 1):
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
