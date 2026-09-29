if __name__ == '__main__':
    x = input("Input: ").strip().lower()

    if x.startswith("hello"):
        print("$0")
    elif x.startswith("h"):
        print("$20")
    else:
        print("$100")