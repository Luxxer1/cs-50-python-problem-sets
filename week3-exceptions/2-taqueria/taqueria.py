def main():
  menu = {
    "Baja Taco": 21.25,
    "Burrito": 27.00,
    "Bowl": 27.00,
    "Nachos": 27.00,
    "Quesadilla": 21.25,
    "Super Burrito": 21.25,
    "Super Quesadilla": 9.50,
    "Taco": 14.00,
    "Tortilla Salad": 14.00
  }


  while True:
    try:
      item = input("Item: ")
    except EOFError:
      print()
      break
    else:
      print_price(item.title(), menu)

def print_price(item, menu):
  if item in menu:
    print(f"Total: ${menu[item]:.2f}")

main()
