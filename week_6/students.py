import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students.csv", "a") as file:
    # writer = csv.writer(file)
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    # writer.writerow([name, home])
    writer.writerow({"home": home, "name": name})

students = []

with open("students.csv") as file:
    # reader = csv.reader(file)
    reader = csv.DictReader(file)
    # for name, home in reader:
    for row in reader:
        # students.append({"name": name, "home": home})
        students.append({"name": row['name'], "home": row['home']})



for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['home']}")


# Convert to LAMBDA Function (anonymous)
# def get_name(student):
#     return student["name"]
