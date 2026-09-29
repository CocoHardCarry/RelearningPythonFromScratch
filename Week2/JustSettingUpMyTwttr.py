def main():
    x = input("Input: ")
    y = ""
    for i in range(len(x)):
        if x[i].lower() != "a" and x[i].lower() != "e" and x[i].lower() != "i" and x[i].lower() != "o" and x[i].lower() != "u":
            y += x[i]

    print("Output:", y)
main()