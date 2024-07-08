import sys
import re
import csv
import os
import pyfiglet
from tabulate import tabulate


MENU = pyfiglet.figlet_format("Database 4 Sales", font="slant")
OPTIONS = """
1 - Register Item
2 - Change Item
3 - Exit Program
"""
REGISTER_ITEM = """
-------------------
|  Register Item  |
-------------------
"""
input_register = f"* Letters and Numbers Only - No special characters allowed\n\nEnter the item name: "
CHANGE_ITEM = """
-------------------
|   Change Item   |
-------------------
"""
CHANGE_ITEM_OPTIONS = """
1 - Change Item Name
2 - Change Item Cost
3 - Change Item Sell
4 - Remove Item
5 - Return to Main Menu
"""


def main():
    invalid_menu = ""
    while True:
        database = att_database()
        clear()
        print(MENU, OPTIONS)
        print(invalid_menu)
        print()
        menu_option = input("Option: ")
        match menu_option:
            case "1":
                register_item(database)
                clear()
                # input("Item register sucessfull. Press enter to return to main menu.")
                invalid_menu = ""

            case "2":
                change_item(database)
                invalid_menu = ""

            case "3":
                clear()
                sys.exit("Good Bye. Have a nice day!")

            case _:
                invalid_menu = "[Error] Invalid Option, Try Again"


def register_item(database):
    invalid_name_register = ""
    invalid_cost_price = ""
    invalid_sell_price = ""
    input_cost = '* Register Cost: "." for decimal separator:\nExample: $ 4.95\n\nEnter the item cost price: '
    input_sell = '* Register Sell: "." for decimal separator:\nExample: $ 9.99\n\nEnter the item sell price: '
    while True:
        clear()
        print(REGISTER_ITEM)
        print(invalid_name_register)
        print()
        print("Press Enter to return to Main Menu")
        name = check_item_name(input(f"\n{input_register}"))
        if name == "":
            return
        elif name:
            for item in database:
                if item["item"] == name.lower():
                    clear()
                    print(REGISTER_ITEM)
                    input(
                        "[Error] Register aborted, item already registered. Press enter to return to Main Menu"
                    )
                    return
            break
        else:
            invalid_name_register = "[Error] Invalid Name, Try Again"

    while True:
        clear()
        print(REGISTER_ITEM)
        print(invalid_cost_price)
        print()
        cost = check_valid_float(input(input_cost))
        if cost:
            break
        else:
            invalid_cost_price = "[Error] Invalid Cost Price, Try Again"

    while True:
        clear()
        print(REGISTER_ITEM)
        print(invalid_sell_price)
        print()
        sell = check_valid_float(input(input_sell))
        if sell:
            break
        else:
            invalid_sell_price = "[Error] Invalid Sell Price, Try Again"

    item_id = get_unique_item_id(database)
    att_database({"id": item_id, "item": name, "cost": cost, "sell": sell})
    clear()
    print(REGISTER_ITEM)
    input("Item register sucessfull. Press enter to return to Main Menu")


def check_item_name(name):
    if name == "":
        return name
    return name.casefold() if re.fullmatch(r"[\w\s]+", name) else False


def check_valid_float(cost):
    try:
        return float(cost)
    except ValueError:
        return False


def get_unique_item_id(database):
    if database:
        return max(item["id"] for item in database) + 1
    else:
        return 1


def change_item(database):
    invalid_item = ""
    invalid_change_item_option = ""
    invalid_name_register = ""
    invalid_cost_price = ""
    invalid_sell_price = ""
    input_item = "Select an item to change by its number or press Enter to return to main menu: "
    input_cost = '* Register Cost: "." for decimal separator:\nExample: $ 4.95\n\nEnter the item cost price: $ '
    input_sell = '* Register Sell: "." for decimal separator:\nExample: $ 9.99\n\nEnter the item sell price: $ '
    clear()
    print(CHANGE_ITEM)
    if len(database) == 0:
        input("No items registered. Press enter to return to main menu.")
    else:
        while True:
            clear()
            print(CHANGE_ITEM)
            print_database(database)
            print(invalid_item)
            print()
            select_item = check_item_id(input(input_item), database)
            if select_item == "":
                return
            elif select_item:
                break
            else:
                invalid_item = "Invalid item. Select a item correctly."

        while True:
            removed = False
            clear()
            print(CHANGE_ITEM)
            for item in database:
                if item["id"] == select_item:
                    print(
                        f"[{item['id']}] {item['item']} | Cost: {item['cost']} | Sell: {item['sell']}"
                    )
            print(CHANGE_ITEM_OPTIONS)
            print(invalid_change_item_option)
            print()
            change_item_option = input("Option: ")
            match change_item_option:
                case "1":
                    while True:
                        repeated = False
                        att_database()
                        clear()
                        print(CHANGE_ITEM)
                        for item in database:
                            if item["id"] == select_item:
                                print(f"Name: {item['item']}")
                        print()
                        print(invalid_name_register)
                        print()
                        name = check_item_name(input(input_register))
                        if name:
                            for item in database:
                                if item["item"] == name.lower():
                                    invalid_name_register = (
                                        "[Error] Invalid Name, already registered"
                                    )
                                    repeated = True

                            if not repeated:
                                for item in database:
                                    if item["id"] == select_item:
                                        item["item"] = name
                                        change_database_item(item=item)
                                        repeated = False
                                break
                        else:
                            invalid_name_register = "[Error] Invalid Name, Try Again"

                case "2":
                    while True:
                        att_database()
                        clear()
                        print(CHANGE_ITEM)
                        for item in database:
                            if item["id"] == select_item:
                                print(f"Item: {item['item']} | Cost: {item['cost']}")
                        print()
                        print(invalid_cost_price)
                        print()
                        cost = check_valid_float(input(input_cost))
                        if cost:
                            for item in database:
                                if item["id"] == select_item:
                                    item["cost"] = cost
                                    change_database_item(cost=item)
                            break
                        else:
                            invalid_cost_price = "[Error] Invalid Cost Price, Try Again"

                case "3":
                    while True:
                        att_database()
                        clear()
                        print(CHANGE_ITEM)
                        for item in database:
                            if item["id"] == select_item:
                                print(f"Item: {item['item']} | Sell: {item['sell']}")
                        print()
                        print(invalid_sell_price)
                        print()
                        sell = check_valid_float(input(input_sell))
                        if sell:
                            for item in database:
                                if item["id"] == select_item:
                                    item["sell"] = sell
                                    change_database_item(sell=item)
                            break
                        else:
                            invalid_sell_price = "[Error] Invalid Sell Price, Try Again"

                case "4":
                    clear()
                    print(CHANGE_ITEM)
                    print(
                        "Be careful, if you are using the database, deleting an item may generate an error."
                    )
                    for item in database:
                        if item["id"] == select_item:
                            print(
                                f"\n[{item['id']}] {item['item']} | Cost: {item['cost']} | Sell: {item['sell']}"
                            )
                    print()
                    confirmation = input("Enter [Y] or [y] to confirm remove: ")
                    if confirmation.lower() == "y":
                        for i, item in enumerate(database):
                            if item["id"] == select_item:
                                remove_database_item(database, select_item)
                                input("\nRemove sucesfull. Press enter to return.")
                                removed = True
                                break

                case "5":
                    clear()
                    removed = True
                    break

                case _:
                    invalid_change_item_option = "[Error] Invalid Change Item Option"

            if removed:
                break


def att_database(item=None):
    database_array = []

    if item != None:
        with open("database.csv", "a") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "item", "cost", "sell"])
            writer.writerow(item)

    with open("database.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            database_array.append(
                {
                    "id": int(row["id"]),
                    "item": row["item"],
                    "cost": row["cost"],
                    "sell": row["sell"],
                }
            )
    return database_array


def remove_database_item(database, select_item):
    database_array = []

    with open("database.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            database_array.append(
                {
                    "id": int(row["id"]),
                    "item": row["item"],
                    "cost": row["cost"],
                    "sell": row["sell"],
                }
            )

    for i, item in enumerate(database_array):
        if item["id"] == select_item:
            database_array.pop(i)

    with open("database.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "item", "cost", "sell"])
        writer.writeheader()
        writer.writerows(database_array)


def change_database_item(item=None, cost=None, sell=None):
    database_array = []

    with open("database.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            database_array.append(
                {
                    "id": int(row["id"]),
                    "item": row["item"],
                    "cost": row["cost"],
                    "sell": row["sell"],
                }
            )

    if item != None:
        for i, item_to_change in enumerate(database_array):
            if item_to_change["id"] == item["id"]:
                database_array[i] = item
                break

    if cost != None:
        for i, item_to_change in enumerate(database_array):
            if item_to_change["id"] == cost["id"]:
                database_array[i] = cost
                break

    if sell != None:
        for i, item_to_change in enumerate(database_array):
            if item_to_change["id"] == sell["id"]:
                database_array[i] = sell
                break

    with open("database.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames=["id", "item", "cost", "sell"])
        writer.writeheader()
        for item in database_array:
            writer.writerow(item)


def print_database(database):
    for item in database:
        print(
            f"[{item['id']}] {item['item']} | Cost: {item['cost']} | Sell: {item['sell']}"
        )
    print()


def check_item_id(item, database):
    if item == "":
        return ""
    try:
        if database and 1 <= int(item) <= max(item["id"] for item in database):
            return int(item)
    except ValueError:
        return False


def clear():
    os.system("cls" if os.name == "nt" else "clear")


if __name__ == "__main__":
    main()
