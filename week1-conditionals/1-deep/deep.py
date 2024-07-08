def main():
    answer = checkAnswer(input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().casefold())
    print(answer)

def checkAnswer(str):
    match str:
        case "42" | "forty-two" | "forty two":
            return "Yes"
        case _:
            return "No"

main()
