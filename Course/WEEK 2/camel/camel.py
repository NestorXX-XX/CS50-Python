def main():
    camelCase = input("camelCase: ")
    print(f"snake_case: {convert_to_snake_case(camelCase)}")

def convert_to_snake_case(i):
    word =[]
    for char in i:
        if char.isupper():
            word.append("_")
            word.append(char.lower())
        else:
            word.append(char)
    return "".join(word)

main()