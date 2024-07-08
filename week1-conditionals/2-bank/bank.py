def main():
    greetings = checkGreetings(input("Greeting: ").strip().casefold())
    print(f"${greetings}")

def checkGreetings(str):
    # If a greeting start with "hello" = return 0
    if str.count("hello", 0, 5) == 1:
        return 0
    elif str.count("h", 0, 1) == 1:
        return 20
    else:
        return 100

main()
