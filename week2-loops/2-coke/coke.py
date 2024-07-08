def main():

    amount = 50
    while amount > 0:
        print(f"Amount Due: {amount}")
        coin = insert_coin(int(input("Insert Coin: ")))
        amount = amount - coin
    change_owed = amount * -1
    print(f"Change Owed: {change_owed}")

def insert_coin(coin):
        if coin == 5 or coin == 10 or coin == 25:
            return coin
        else:
            return 0

main()
