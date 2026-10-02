def main():
    while True:
        try:
            x = input("Fraction: ")
            convert(x)

        except (ValueError, ZeroDivisionError):
            pass

        break

def convert(fraction):
    f, s  = fraction.split("/")
    f = int(f)
    s = int(s)

    if f > s or s == 0:
        raise ValueError

    p = round(f / s * 100)
    gauge(p)

def gauge(percentage):
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")


if __name__ == "__main__":
    main()