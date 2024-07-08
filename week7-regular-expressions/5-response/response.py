from validator_collection import checkers

def main():
    print(check_email(input("Text: ")))


def check_email(s):
    if checkers.is_email(s):
        return "Valid"
    else:
        return "Invalid"

main()
