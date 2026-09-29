def main():
    case = input("camelCase: ")
    snake =""

    for i in range(len(case)):
        if case[i].isupper():
            snake += "_"
            snake += case[i].lower()

        else:
            snake += case[i]

    print(snake)





main()