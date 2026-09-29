def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        x = int(input("x: "))
        if x > 0:
            break

    return x


def meow(n):
    for _ in range(n):
        print("Meow")

def print_square(size):
    # for each row in square
    for i in range(size):
        # for each brick in row
        for j in range(size):
            print("#", end="")
        print()

if __name__ == '__main__':
    # Loops
    i = 3
    while i != 0:
        print("meow")
        i -= 1
    for i in range(3):
        print("Meow")

    # print("meow\n" + 3)
    # main()

    # Lists
    students = ["Coco", "Me", "BK"]
    for i in students:
        print(i)
    for i in range(len(students)):
        print(f"{i+1}.", students[i])

    # Dictionaries
    student ={"Hermione": "Gryffindor",
              "Harry": "Gryffindor",
              "Ron": "Gryffindor",
              "Draco": "Slytherin"}
    for i in student:
        print(i, student[i])

    s = [
        {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
        {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
        {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel terrier"},
        {"name": "Draco", "house": "Slytherin", "patronus" : None}
    ]
    for i in s:
        print(i["name"], i["house"], i["patronus"], sep=", ")

    print_square(3)

