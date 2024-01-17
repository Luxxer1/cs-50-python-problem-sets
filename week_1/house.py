name = input("What's your name? ")

# if name == "Harry" or name == "Hermione" or name == "Ron":
#     print("Grifinória")
# elif name == "Draco":
#     print("Sonserina")
# else:
#     print("Who?")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Grifinória")
    case "Draco":
        print("Sonserina")
    case _:
        print("Who?")
