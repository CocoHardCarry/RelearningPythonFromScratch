import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

if not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")

count = 0

try:
    with open(sys.argv[1], "r") as file:
        for line in file:
            if line.strip() == "":
                pass

            if line.lstrip().startswith("#"):
                pass
        count += 1
except FileNotFoundError:
    sys.exit("File does not exist")

print(count)