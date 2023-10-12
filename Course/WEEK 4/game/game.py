from random import randint
def main():
    Level = input("Level: ")
    while not Level.isnumeric() or int(Level) < 1:
        Level = input("Level: ")
    Guess = input("Guess: ")
    while not Guess.isnumeric() or int(Guess) < 1:
        Guess = input("Guess: ")
    Random_number = randint(1,int(Level))
    if int(Guess) < Random_number:
        print("Too small!")
    elif int(Guess) > Random_number:
        print("Too large!")
    else:
        print("Just right!")


if __name__ == "__main__":
	main()