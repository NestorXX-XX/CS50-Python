def main():
    time = input("Time: ")
    x = convert(time)
    if 7 <= x <= 8:
        print("breakfast time")
    elif 12 <= x <= 13:
        print("lunch time")
    elif 18 <= x <= 19:
        print("dinner time")



def convert(time):
    return int(time.split(":")[0])+(int(time.split(":")[1]))/60

if __name__ == "__main__":
    main()
