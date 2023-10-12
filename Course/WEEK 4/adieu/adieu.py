def main():
    x = []
    while True:
        try:
            x.append(input("Name: "))
        except EOFError:
            break
    print(convert_list_to_the_text(x))

def convert_list_to_the_text(x):
    if len(x) == 1:
        return f"Adieu, adieu, to {x[0]}"
    elif len(x) == 2:
        return f"Adieu, adieu, to {x[0]} and {x[1]}"
    else:
        for i in x:
            if x.index(i) == 0:
                j = f"Adieu, adieu, to {i},"
            elif x.index(i) == (len(x)-1):
                j = j+" and "+i
                return j
            else:
                j = j+" "+i+","


if __name__ == "__main__":
	main()
