import sys
from pyfiglet import Figlet
import random

def main():
    f = Figlet()
    available_fonts = f.getFonts()
    if (len(sys.argv) == 3) and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and (sys.argv[2] in available_fonts):
        f = Figlet(font=sys.argv[2])
        x = input("Input: ")
        print(f.renderText(x))
    elif len(sys.argv) == 1:
        random_font = random.choice(available_fonts)
        f = Figlet(font=random_font)
        x = input("Input: ")
        print(f.renderText(x))
    else:
         print("Invalid usage")
         sys.exit(1)








if __name__ == "__main__":
    main()