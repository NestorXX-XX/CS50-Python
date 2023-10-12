def main():
    menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
    total = 0.00
    while True:
        try:
            x = input("Item: ").lower().title()
            if not x in menu:
                pass
            else:
                total = float(total) + float(menu[x])
                print(f"Total: ${float(total):.2f}")
        except EOFError:
            break
main()