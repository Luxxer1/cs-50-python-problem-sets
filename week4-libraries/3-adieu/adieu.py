import inflect

p = inflect.engine()
names = []

while True:
    try:
        names.append(input("Name: "))
    except EOFError:
        print()
        break

adieu_to = p.join(names)
print(f"Adieu, adieu, to {adieu_to}")
