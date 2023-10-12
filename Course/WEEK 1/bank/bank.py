x = str(input("Enter: ").lower().strip())

if x.find("hello") >= 0:
    print("$0")
elif x.find("h") == 0:
    print("$20")
else:
    print("$100")
