def main():
    print(shorten(input("Input: ")))


def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]
    str = ""
    for c in word:
        if vowels.count(c) == 0:
            str += c
        else:
            str += ""
    return str


if __name__ == "__main__":
    main()
