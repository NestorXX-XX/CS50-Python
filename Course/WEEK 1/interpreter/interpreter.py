y = str(input("Enter: "))
x = int(y.split()[0])
z = int(y.split()[2])



if "/" in y:
    print(float(round(x/z, 1)))
elif "*" in y:
    print(float(round(x*z, 1)))
elif "+" in y:
    print(float(round(x+z, 1)))
elif "-" in y:
    print(float(round(x-z, 1)))