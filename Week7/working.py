import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    match = re.search(
        r"^([1-9]|1[0-2])(?::([0-5]\d))? (AM|PM) to ([1-9]|1[0-2])(?::([0-5]\d))? (AM|PM)$",
        s
    )

    if not match:
        raise ValueError

    hour1 = int(match.group(1))
    minute1 = int(match.group(2) or 0)
    period1 = match.group(3)

    hour2 = int(match.group(4))
    minute2 = int(match.group(5) or 0)
    period2 = match.group(6)

    if period1 == "AM" and hour1 == 12:
        hour1 = 0
    elif period1 == "PM" and hour1 != 12:
        hour1 += 12

    if period2 == "AM" and hour2 == 12:
        hour2 = 0
    elif period2 == "PM" and hour2 != 12:
        hour2 += 12

    return f"{hour1:02}:{minute1:02} to {hour2:02}:{minute2:02}"


if __name__ == "__main__":
    main()