# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def square(n):
    return n * n

def calculator():
    #x = int(input("x: "))
    # y = int(input("y: "))

    x = float(input("x: "))
    y = float(input("y: "))

    #z = round(x + y)
    z = round(x/y, 3)
    print(f"{z:,}" )

def hello(x="world"):
    print("hello," , x)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # x = input("What is your name?").strip().title()

    # Split user name into first and last name'
    # first, last = x.split(" ")

    # Remove whitespace from str
    #x = x.strip()

    # Capitalize name
    # x = x.capitalize()

    # Title based Capitalization
    # x = x.title()

    # x = x.strip().title()
    # print("yo", first, "tags")
    # calculator()
    # hello()
    # hello(x)
    x = int(input("x: "))
    print("x squared is", square(x))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
