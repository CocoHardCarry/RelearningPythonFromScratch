# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def ifstatement():
    x = int(input("x: "))
    y = int(input("y: "))

    if x < y:
        print(" x is less than y")
    elif x > y:
        print(" x is greater than y")
    else:
        print("x is equal to y")

    # elif x == y:
    # print(" x is equal to y")

def grade():
    score = int(input("Enter your score: "))

    if score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    elif score >= 60:
        print("Grade: D")
    else:
        print("Grade: F")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    # return True if n % 2 == 0 else False
    # return (n % 2 == 0)

if __name__ == '__main__':
    # ifstatement()
    # grade()
    # x = int(input("x: "))
    # if is_even(x):
        # print(f"{x} is even")
    # else:
        # print(f"{x}1 is odd")
    name = input("Enter your name: ")

    match name:
        case "Harry" | "Hermione" | "Ron":
            print("Gryffindor")
        case "Draco":
            print("Slytherin")
        case _:
            print("Who?")
