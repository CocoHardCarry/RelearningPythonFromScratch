def main():
    while True:
        try:
            x = input("Fraction: ")
            f, s = x.split("/")

            f = int(f)
            s = int(s)

            if f > s or s == 0:
                raise ValueError

            p = round(f / s * 100)

            if p <= 1:
                print("E")
            elif p >= 99:
                print ("F")
            else:
                print(f"{p}%")

            break

        except (ValueError, ZeroDivisionError):
            pass

main()