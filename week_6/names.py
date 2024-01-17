names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")

# with open("names.txt", "r") as file:
#     lines = file.readlines()

# for line in lines:
#     print("hello,", line.rstrip())

# name = input("What's your name? ")

# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")
