def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) > 6 or len(s) < 2:
        return False
    elif s[0].isnumeric() or s[1].isnumeric():
        return True
    else:
        j = 0
        for i in s:
            if i.isnumeric():
                j = j +1
                if int(i) == 0 and j == 1:
                   return False
            else:
                if j > 0:
                    return False
    if s.find(".") != -1 or s.find(" ") != -1:
        return False
    return True

if __name__ == "__main__":
    main()