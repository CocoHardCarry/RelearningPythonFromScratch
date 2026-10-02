def main():
    x = input("Input: ")
    print(shorten(x))


def shorten(word):
    y = ""
    for i in range(len(word)):
        if word[i].lower() != "a" and word[i].lower() != "e" and word[i].lower() != "i" and word[i].lower() != "o" and word[i].lower() != "u":
            y += word[i]

    return "Output: " + y


if __name__ == "__main__":
    main()