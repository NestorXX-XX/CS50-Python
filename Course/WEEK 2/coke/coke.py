def main():
    x = 0
    while x < 50:
        y = int(input("Insert Coin: "))
        if y in [25, 10, 5]:
            x += y
        if x < 50:
            print(f"Amount Due: {50-x}")
    print(f"Change Owed: {x-50}")

main()