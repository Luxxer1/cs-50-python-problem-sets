def main():
    greetings = checkGreetings(input("Greeting: ").strip().casefold())
    print(f"${greetings}")


def value(str):
    str = str.lower();

    if str.startswith("hello"):
        return 0
    elif str.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
