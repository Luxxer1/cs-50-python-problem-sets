def main():
    to_snake(input("camelCase: "))

def to_snake(str):
    for letter in str:
        if letter.isupper():
            print("_", letter.casefold(), sep="", end="")
        else:
            print(letter, end="")
    print()

main()
