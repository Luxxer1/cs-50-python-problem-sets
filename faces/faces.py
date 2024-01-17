def main():
    toEmoj = convert(input("Como está se sentindo hoje? "))
    print(toEmoj)

def convert(str):
    return str.replace(":)", "🙂").replace(":(", "🙁")

main()
