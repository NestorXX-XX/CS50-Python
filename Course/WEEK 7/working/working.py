import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    i = re.search(r"^([1]?[0-9]:?[0-5]?[0-9]?) (AM|PM) to ([1]?[0-9]:?[0-5]?[0-9]?) (AM|PM)$",s)
    if not i:
        raise ValueError
    else:
        if i.group(2) == "AM":
            first = i.group(1).split(":")
            try:
                if int(first[0]) > 10:
                    first = f"{first[0]}:{first[1]}"
                else:
                    first = f"0{first[0]}:{first[1]}"
            except IndexError:
                if int(first[0]) > 10:
                    first = f"{first[0]}:00"
                else:
                    first = f"0{first[0]}:00"
        elif i.group(2) == "PM":
            first = i.group(1).split(":")
            try:
                first = f"{int(first[0])+12}:{first[1]}"
            except IndexError:
                first = f"{int(first[0])+12}:00"
        if i.group(4) == "AM":
            second = i.group(3).split(":")
            try:
                if int(second[0]) > 10:
                    second = f"{second[0]}:{second[1]}"
                else:
                    second = f"0{second[0]}:{second[1]}"
            except IndexError:
                if int(second[0]) > 10:
                    second = f"{second[0]}:00"
                else:
                    second = f"0{second[0]}:00"
        elif i.group(4) == "PM":
            second = i.group(3).split(":")
            try:
                second = f"{int(second[0])+12}:{second[1]}"
            except IndexError:
                second = f"{int(second[0])+12}:00"
    return f"{first} to {second}"

if __name__ == "__main__":
    main()