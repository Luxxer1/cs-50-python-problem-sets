def main():
    print(shorten(input("Input: ")))


def shorten(word):
    vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    str = ""
    for c in word:
        if vowels.count(c) == 0:
            str += c
        else:
            continue
    return str


if __name__ == "__main__":
    main()