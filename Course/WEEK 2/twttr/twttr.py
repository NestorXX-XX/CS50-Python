def main():
    x = str(input("Input: ").strip())
    x = x.replace("a","",).replace("e","",).replace("i","",).replace("o","",).replace("u","",)
    x = x.replace("A","",).replace("E","",).replace("I","",).replace("O","",).replace("U","",)
    print(f"Output: {x}")
main()