import sys
import csv
from tabulate import tabulate


def main():
    data = []

    with open(one_command_line_argument()) as file:
        reader = csv.reader(file)
        for row, i in enumerate(reader):
            if row == 0:
                headers = [i[0],i[1],i[2]]
            else:
                data.append([i[0],i[1],i[2]])

    print(tabulate(data, headers, tablefmt="grid"))


def one_command_line_argument():
    try:
        if len(sys.argv) < 2:
            print("Too few command-line arguments")
            sys.exit(1)
        elif len(sys.argv) > 2:
            print("Too many command-line arguments")
            sys.exit(1)
        elif not ".csv" in sys.argv[1]:
            print("Not a Comma-Separated file")
            sys.exit(1)
        else:
            open(sys.argv[1])
        return sys.argv[1]
    except IndexError:
        print("Too few command-line arguments")
        sys.exit(1)
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)

if __name__ == "__main__":
    main()