cash = []
while True:
    i = int(input("Insert Coin: "))

    if i == 25 or i == 10 or i == 5:
        if sum(cash) >= 50:
            print(f"Change Owed: {50 - sum(cash)}")
            break
        else:
            cash.append(i)
            if sum(cash) >= 50:
                print(f"Change Owed: {sum(cash) - 50}")
                break
            else:
                print(f"Amount Due: {50 - sum(cash)}")
    else:
        print(f"Amount Due: {50 - sum(cash)}")
            