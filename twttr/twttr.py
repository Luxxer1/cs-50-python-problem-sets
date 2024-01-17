def main():
    delete_vowels(input("Input: "))

def delete_vowels(str):
    for c in str:
        if check_vowels(c):
            print("", end="")
        else:
            print(c, end="")
    print()

def check_vowels(letter):
    vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
    for i in vowels:
        if letter == i:
            return True

main()
