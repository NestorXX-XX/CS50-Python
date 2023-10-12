def main():
    greeting = str(input("Enter: "))
    print(f"${value(greeting)}")

def value(greeting):
    greeting = greeting.lower().strip()
    if greeting.find("hello") == 1:
        return 0
    elif greeting.find("h") == 0:
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()