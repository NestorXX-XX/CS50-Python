def main():
    word = str(input("Input: ").strip())
    print(shorten(word))
def shorten(word):
    word = word.replace("A","",).replace("e","",).replace("i","",).replace("o","",).replace("u","",)
    word = word.replace("A","",).replace("E","",).replace("I","",).replace("O","",).replace("U","",)
    return word

if __name__ == "__main__":
    main()