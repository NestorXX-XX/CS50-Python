def main():
    k = how_much_left("Fraction: ")
    if k <= 1:
        print("E")
    elif k >= 99:
        print("F")
    else:
        print(f"{k}%")

def how_much_left(prompt):
    while True:
        try:
            x = input(prompt)
            x = x.split("/")
            if not x[0].isnumeric() or not x[1].isnumeric():
                pass
            elif int(x[0]) > int(x[1]):
                pass
            else:
                return int(round((int(x[0])/int(x[1])),2)*100)
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

main()