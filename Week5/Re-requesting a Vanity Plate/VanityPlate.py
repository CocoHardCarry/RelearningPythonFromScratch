def main():
        plate = input("Plate: ")
        if is_valid(plate):
            print("Valid")
        else:
            print("Invalid")


def is_valid(s):
        endNumber = False

        if len(s) < 2 or len(s) > 6:
            return False

        if not s[0].isalpha() or not s[1].isalpha():
            return False

        for i in s:
            if not i.isalnum():
                return False
            if i.isdigit():
                if i == "0" and not endNumber:
                    return False
                endNumber = True

            elif endNumber:
                return False

        return True

if __name__ == "__main__":
    main()