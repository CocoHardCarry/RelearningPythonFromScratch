import csv
# names = input("What's your name? ")

# "w" = write but recreates
# "a" = append
# file = open("names.txt","a")
# file.write(f"{names}\n")
# file.close()

# with open("names.txt","a") as file:
    # file.write(f"{names}\n")

with open("names.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip())

names = []
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print(f"hello,{name.upper()}")

print("==============================")
students = []

with open("students.csv") as file:
    reader = csv.reader(file)
    # reader = csv.DictReader(file)
    for name, house in reader:
        students.append({"name": name, "house": house})


    """
    for line in file:
    name, house = line.rstrip().split(",")
    print(f"{name} is in {house}")
    student = {"name": name, "house": house}
    student["name"] = name
    student["house"] = house
    students.append(student)
    """

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['house']}")

n = names = input("What's your name? ")
h = input("Wheres your home? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, filenames=["name", "home"])
    writer.writerow({"name": n, "home": h})

