def main():
    x = input("Enter: ")
    print(convert(x))

def convert(x):
    x = x.replace(":(","🙁").replace(":)","🙂")
    return x

main()