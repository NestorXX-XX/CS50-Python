def main():
    while True:
        fraction = input("Fraction: ")
        try:
            percentage = convert(fraction)
            break
        except (ValueError, ZeroDivisionError):
            continue

    print(gauge(percentage))



def convert(fraction):
    fraction = fraction.split("/")
    while True:
        try:
            if not fraction[0].isnumeric() or not fraction[1].isnumeric():
                raise ValueError
            elif int(fraction[0]) > int(fraction[1]):
                raise ValueError
            else:
                return str(round((int(fraction[0])/int(fraction[1])),2)*100)
        except ValueError:
            raise ValueError

        except ZeroDivisionError:
            raise ZeroDivisionError


def gauge(percentage):
    if percentage <= 1:
        return ("E")
    elif percentage >= 98:
        return ("F")
    else:
        return (f"{percentage}%")


if __name__ == "__main__":
    main()