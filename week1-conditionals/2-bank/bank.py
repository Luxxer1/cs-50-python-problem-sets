def main():
    greetings = checkGreetings(input("Greeting: ").strip().casefold())
    print(f"${greetings}")

def checkGreetings(str):
    if str.lower().count("hello", 0, 5) == 1:
        return 0
    elif str.lower().count("h", 0, 1) == 1:
        return 20
    else:
        return 100

main()
