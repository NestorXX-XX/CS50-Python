import sys
import csv

def main():
    j = []

    with open(one_command_line_argument()[0]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            x = row["name"].split(",")
            row["name"] = row["name"].replace(x[0], "first").replace(x[1], "last")
            row["name"] = row["name"].replace("first", x[1].strip()).replace("last", f" {x[0].strip()}")
            j.append(
                {"name": row["name"], "house": row["house"]}
                )
 
    with open(one_command_line_argument()[1], "w") as file:
        writer = csv.DictWriter(file, fieldnames = ["name", "house"])
        writer.writerow({"name": "name", "house": "house"})
        for i in j:
            writer.writerow(i)




def one_command_line_argument():
    try:
        if len(sys.argv) < 3:
            print("Too few command-line arguments")
            sys.exit(1)
        elif len(sys.argv) > 3:
            print("Too many command-line arguments")
            sys.exit(1)
        elif not "before.csv" in sys.argv[1]:
            print(f"Could not read {sys.argv[1]}")
            sys.exit(1)
        elif not ".csv" in sys.argv[2]:
            print(f"{sys.argv[2].capitalize()} is not a Comma-Separated file")
            sys.exit(1)
        else:
            open(sys.argv[1])
        return sys.argv[1], sys.argv[2]
    except IndexError:
        print("Too few command-line arguments")
        sys.exit(1)
    except FileNotFoundError:
        print(f"Could not read {sys.argv[1]}")
        sys.exit(1)

if __name__ == "__main__":
    main()


