if __name__ == '__main__':
    prompt = input("Expression: ").strip()

    x, y, z = prompt.split(" ")

    x = float(x)
    z = float(z)

    if y == '+':
        print(x + z)
    elif y == '-':
        print(x - z)
    elif y == '*':
        print(x * z)
    elif y == '/':
        print(x / z)