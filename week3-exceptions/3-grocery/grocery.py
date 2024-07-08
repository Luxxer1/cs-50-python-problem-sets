def main():
    grocery_list = {}

    while True:
        try:
            item = input().upper()
        except EOFError:
            print_grocery_list_sorted(grocery_list)
            break
        else:
            if item in grocery_list:
                grocery_list[item] = grocery_list[item] + 1
            else:
                grocery_list[item] = 1

def print_grocery_list_sorted(grocery_list):
    sorted_list = sorted(grocery_list)
    for x in sorted_list:
        print(f"{grocery_list[x]} {x}")

main()
