import sys
from PIL import Image, ImageOps


def main():
    shirt = Image.open("shirt.png")
    before = Image.open(one_command_line_argument()[0])
    result = ImageOps.fit(before, shirt.size)
    result.paste(shirt, shirt)
    result.save(one_command_line_argument()[1])

def one_command_line_argument():
    extensions = (".jpg", "jpeg", "png")
    try:
        if len(sys.argv) < 3:
            print("Too few command-line arguments")
            sys.exit(1)
        elif len(sys.argv) > 3:
            print("Too many command-line arguments")
            sys.exit(1)
        elif not any(i in sys.argv[1] for i in extensions):
            print(f"{sys.argv[1]} is not a .jpg or a jpeg or a png")
            sys.exit(1)
        elif not sys.argv[1].split(".")[1] == sys.argv[2].split(".")[1]:
            print(f"The input's name does not have the same extension as the output's name")
            sys.exit(1)
        else:
            open(sys.argv[1])
        return sys.argv[1], sys.argv[2]
    except IndexError:
        print("Too few command-line arguments")
        sys.exit(1)
    except FileNotFoundError:
        print(f"Could not open {sys.argv[1]}")
        sys.exit(1)

if __name__ == "__main__":
    main()