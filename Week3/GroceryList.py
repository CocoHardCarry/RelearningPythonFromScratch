def main():
    list = {}
    while True:
        x = input("Enter Grocery: ")

        if x == "":
            break


        if x in list:
            list[x] += 1
        else:
            list[x] = 1

    for i in list:
        print(list[i], i.upper())
main()