def main():
    x = input("Input: ").strip().lower()


def value(greeting):
    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")


if __name__ == "__main__":
    main()