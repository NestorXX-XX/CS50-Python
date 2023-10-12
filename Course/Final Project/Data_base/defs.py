from tabulate import tabulate
import csv
import time
import os
from PATH import path

MAIN_PATH = path()


def interface():
    data = [
        ["Work on a flashcard", "W"],
        ["New flashcard", "N"],
        ["Delete flashcard", "D"],
        ["Exit", "E"],
    ]
    print(tabulate(data, tablefmt="grid"))
    o = input("What do you want to do? (Write the letter): ").lower()
    while True:
        if o not in ("w", "n", "d", "e"):
            o = input("What do you want to do? (Write the letter): ").lower()
        else:
            return o


def new_flashcard():
    h = []
    time.sleep(0.7)
    os.system("clear")
    while True:
        try:
            name = input("How would you like to call your flashcard?: ").lower()
            path = f"{MAIN_PATH}/Flash_card_data_base/{name}.csv"
            with open(path, "x") as file:
                break
        except FileExistsError:
            print("Your flashcard name is already in use.")
            print()
    time.sleep(0.7)
    os.system("clear")
    print(
        "Frist of all, you are gonna be asked to write the spanish, and after that\nyou will be asked for the english one. You can exit any time by typing\nexit in the spanish word, not in the english one.\n"
    )
    while True:
        spanish_word = input("Spanish word: ")
        print()
        if spanish_word.lower() == "exit":
            with open(path, "w") as file:
                writer = csv.DictWriter(file, fieldnames=["question", "answer"])
                writer.writeheader()
                for i in h:
                    writer.writerow(i)
            with open(f"{MAIN_PATH}/Flash_cards_active.csv", "a", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["name"])
                writer.writeheader()
                writer.writerow({"name": name})
                return
        english_word = input("English word: ")
        time.sleep(0.7)
        os.system("clear")
        h.append(
            {"question": spanish_word.capitalize(), "answer": english_word.capitalize()}
        )
