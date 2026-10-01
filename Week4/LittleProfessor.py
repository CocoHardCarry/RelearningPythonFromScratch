import random


def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y

        wrong = 0

        while True:
            try:
                question = int(input(f"{x} + {y} = "))
                if answer != question:
                    print("EEE")
                    wrong += 1
                elif answer == question:
                    score += 1
                    break
                if wrong == 3:
                    print(f"{x} + {y} = {answer}")
                    break
            except ValueError:
                print("EEE")

    print("Score:", score)



def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level >= 1 and level <= 3:
                return level

        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(1, 10)
    elif level == 2:
        return random.randint(11, 100)
    elif level == 3:
        return random.randint(101, 100)
    else:
        raise ValueError


if __name__ == "__main__":
    main()