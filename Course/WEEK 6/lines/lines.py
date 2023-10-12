import sys

def main():
    counter = 0
    with open(one_command_line_argument()) as file:
        for line in file:
            line = line.strip().rstrip()
            if line == "" or line[0] == "#":
                pass
            else:
                counter += 1
    print(counter)

def one_command_line_argument():
    try:
        if len(sys.argv) < 2:
            print("Too few command-line arguments")
            sys.exit(1)
        elif len(sys.argv) > 2:
            print("Too many command-line arguments")
            sys.exit(1)
        elif not ".py" in sys.argv[1]:
            print("Not a Python file")
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