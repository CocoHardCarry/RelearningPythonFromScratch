import random

while True:
    try:
        level = int(input("Level: "))
        if level < 1:
            pass
        else:
            n = random.randint(1, level)
        break

    except ValueError:
        pass

while True:
    try:
        guess = int(input("Guess: "))
        if guess < 1:
            pass
        elif guess > n:
            print("Too large!")
        elif guess < n:
            print("Too small!")
        else:
            print("Just right!")
            break

    except ValueError:
        pass

