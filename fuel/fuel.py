def main():
    while True:
        try:
            result = fuel_gauge(input("Fraction: "))
            # if x>y , so, result > 100, so, reprompt, not catching an exception
            while result > 100:
                result = fuel_gauge(input("Fraction: "))
            break
        except (ValueError, ZeroDivisionError):
            pass

    if(result >= 99):
        print("F")
    elif(result <= 1):
        print("E")
    else:
        print(f"{result}%")

def fuel_gauge(input):
    x, y = input.split("/")
    return round((int(x) / int(y)) * 100)

main()
