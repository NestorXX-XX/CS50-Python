months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
def main():
    while True:
        x = input("Date: ").strip()
        if "/" in x:
            if not x[0].isnumeric():
                pass
            else:
                u = x.split("/")
                if int(u[0]) > 12 or int(u[1]) > 31:
                    pass
                else:
                    print(convert_type1_to_type3(x))
                    break

        elif "," in x:
            if x[0].isnumeric():
                pass
            else:
                x = convert_type2_to_type1(x)
                u = x.split("/")
                if int(u[0]) > 12 or int(u[1]) > 31:
                    pass
                else:
                    print(convert_type1_to_type3(x))
                    break
        else:
            pass



def convert_type2_to_type1(i):
     return i.replace(" ","/").replace(",","").replace(i.split()[0], str(months.index(i.split()[0])+1))

def convert_type1_to_type3(i):
    k = str(i.split("/")[2])
    y = int(i.split("/")[0])
    j = int(i.split("/")[1])
    if y < 10:
        y = str(f"0{y}")
    if j < 10:
        j = str(f"0{j}")
    return f"{k}-{y}-{j}"
main()