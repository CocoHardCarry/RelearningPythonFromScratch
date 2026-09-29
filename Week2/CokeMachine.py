def main():
    amount = 50
    while amount > 0:
        amountDue(amount)
        coin = int(input("Insert Coin: "))
        if coin == 50 or coin == 25 or coin == 10 or coin == 5:
            amount -= coin
        else:
            print()

    amount *= -1
    print(f"Change Owed: {amount}")

def amountDue(x):
    print(f"Amount Due: {x}")

main()