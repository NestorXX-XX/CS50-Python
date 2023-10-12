from Data_base.defs import interface
from Data_base.defs import new_flashcard
from tabulate import tabulate
import sys
import csv
from random import randint
from gtts import gTTS
import os
import time
import contextlib

with contextlib.redirect_stdout(None):
    from pygame import mixer
from tkinter import *
from PATH import path

MAIN_PATH = path()

# Delete
# Window


def main():
    # save flas_cards betwween sessions.
    while True:
        interface_ = interface()
        if interface_ == "w":
            work_flashcard()
            time.sleep(3)
            os.system("clear")
        elif interface_ == "n":
            new_flashcard()
            time.sleep(3)
            os.system("clear")
        elif interface_ == "d":
            delete_flashcard()
            time.sleep(3)
            os.system("clear")
        else:
            exit()


def delete_flashcard():
    time.sleep(0.7)
    os.system("clear")
    flash_cards = []
    with open(f"{MAIN_PATH}/Flash_cards_active.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            flash_cards.append([row["name"]])
    if len(flash_cards) == 0:
        print("You don't have any flash_cards to delete.")
        return
    while ["name"] in flash_cards:
        flash_cards.remove(["name"])
    time.sleep(0.7)
    os.system("clear")
    while ["name"] in flash_cards:
        flash_cards.remove(["name"])
    print(tabulate(flash_cards, tablefmt="grid"))
    while True:
        try:
            flash_cards_filtered = []
            l = flash_cards
            delete = input("Which flashcard would you like to delete?: ").lower()
            if delete in ["Exit", "exit"]:
                return
            for i in l:
                if i == [delete]:
                    l.remove([delete])
            for i in l:
                flash_cards_filtered.append({"name": i[0]})

            with open(f"{MAIN_PATH}/Flash_cards_active.csv", "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["name"])
                writer.writeheader()
                writer.writerows(flash_cards_filtered)
                os.remove(f"{MAIN_PATH}/Flash_card_data_base/{delete}.csv")
                return
        except FileExistsError:
            print("Please type a existing flashcard")


def work_flashcard():
    flash_cards = []
    with open(f"{MAIN_PATH}/Flash_cards_active.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            flash_cards.append([row["name"]])
    while ["name"] in flash_cards:
        flash_cards.remove(["name"])
    time.sleep(0.7)
    os.system("clear")
    print(tabulate(flash_cards, tablefmt="grid"))
    while True:
        try:
            if len(flash_cards) == 0:
                print("Please create a flashcard first.")
                return
            name = input("Type the name of the one you want to work on: ").lower()
            if name == "exit":
                return
            print()
            path = f"{MAIN_PATH}/Flash_card_data_base/{name}.csv"
            with open(path) as file:
                break
        except FileNotFoundError:
            print("Please type a existing flashcard")
            time.sleep(0.7)
            os.system("clear")
    while True:
        type = input("Would you like to study or practice: ").lower()
        if type == "study" or type == "practice":
            break
    j = []
    with open(path) as file:
        reader = csv.DictReader(file)
        for row in reader:
            j.append({"question": row["question"], "answer": row["answer"]})
    if type == "study":
        window_study(j)
    else:
        window(j)


def exit():
    time.sleep(0.7)
    os.system("clear")
    print("THANK YOU, FOR USING THE PROGRAM. ALL YOUR FLASHCARDS WILL BE SAVED. 😊😊😊")
    time.sleep(3)
    os.system("clear")
    sys.exit(0)


def window(words):
    root = Tk()
    root.title("Flash-Cards-Practice")
    root.geometry("550x410")
    root.configure(bg="#6693F5")

    count = len(words)

    def next():
        global hinter, hint_count
        # Clear the screen
        answer_label.config(text="")
        my_entry.delete(0, END)
        hint_label.config(text="")
        # Reset Hint stuff
        hinter = ""
        hint_count = 0

        # Create random selection
        global random_word
        random_word = randint(0, count - 1)
        # update label with Spanish Word
        spanish_word.config(text=words[random_word]["question"])

    def answer():
        if my_entry.get().lower() == words[random_word]["answer"].lower():
            answer_label.config(
                text=f"Correct! {words[random_word]['question']} is {words[random_word]['answer'].capitalize()}",
                highlightbackground="#6693F5",
            )
        elif len(my_entry.get()) == 0:
            answer_label.config(
                text=f"Please type something", highlightbackground="#6693F5"
            )
        else:
            answer_label.config(
                text=f"Incorrect! {words[random_word]['question']} is not {my_entry.get().capitalize()}",
                highlightbackground="#6693F5",
            )

    # Keep Track Of the Hints
    hinter = ""
    hint_count = 0

    def hint():
        global hint_count
        global hinter

        if hint_count < len(words[random_word]["answer"]):
            j = words[random_word]["answer"].capitalize()
            hinter = hinter + j[hint_count]
            hint_label.config(text=hinter)
            hint_count += 1

    def back():
        root.destroy()

    def text_to_sppech():
        if words[random_word]["question"] == spanish_word.cget("text"):
            language = "es"
            mytext = words[random_word]["question"]
        else:
            language = "en"
            mytext = words[random_word]["answer"]

        myobj = gTTS(text=mytext, lang=language, slow=False)
        path = f"{MAIN_PATH}/Speech/x.mp3"
        myobj.save(path)
        mixer.init()
        mixer.music.load(path)
        mixer.music.play()
        while mixer.music.get_busy():  # wait for music to finish playing
            time.sleep(1)
        os.remove(path)

    spanish_word = Label(
        root, text="", font=("Helvetica", 36), bg="#6693F5", fg="black"
    )
    spanish_word.place(relx=0.5, rely=0.3, anchor="center")

    answer_label = Label(
        root, text="", bg="#6693F5", fg="black", highlightbackground="#6693F5"
    )
    answer_label.place(relx=0.5, rely=0.65, anchor="center")  # Add "sticky" option

    my_entry = Entry(root, font=("Helvetica", 18), highlightbackground="#6693F5")
    my_entry.place(relx=0.5, rely=0.5, anchor="center")

    answer_button = Button(
        root,
        text="Answer",
        command=answer,
        fg="black",
        highlightbackground="#6693F5",
        borderwidth=10,
    )
    answer_button.place(relx=0.3, rely=0.75, anchor="center")

    next_button = Button(
        root,
        text="Next",
        command=next,
        fg="black",
        highlightbackground="#6693F5",
        borderwidth=10,
    )
    next_button.place(relx=0.5, rely=0.75, anchor="center")

    hint_button = Button(
        root,
        text="Hint",
        command=hint,
        fg="black",
        highlightbackground="#6693F5",
        borderwidth=10,
    )
    hint_button.place(relx=0.7, rely=0.75, anchor="center")

    reproduce_button = Button(
        root,
        text="Reproduce word",
        command=text_to_sppech,
        fg="black",
        highlightbackground="#6693F5",
        borderwidth=10,
    )
    reproduce_button.place(relx=0.72)

    hint_label = Label(
        root, text="", bg="#6693F5", fg="black", highlightbackground="#6693F5"
    )
    hint_label.place(relx=0.45, rely=0.85)

    root.bind("<Return>", lambda event: answer())
    root.bind("<Right>", lambda event: next())
    root.bind("<Escape>", lambda event: back())

    next()
    root.mainloop()
    return


def window_study(words):
    global i
    i = 2
    root = Tk()
    root.title("Flash-Cards-Study")
    root.geometry("550x410")
    root.configure(bg="#6693F5")

    # get a count of our word list
    def change_back():
        english_word.lower(spanish_word)
        spanish_word.config(text="")
        english_word.config(text="")
        spanish_word.config(text=words[random_word]["question"])

    def change():
        spanish_word.lower(english_word)
        spanish_word.config(text="")
        english_word.config(text="")
        english_word.config(text=words[random_word]["answer"])

    def change_general():
        if words[random_word]["question"] == spanish_word.cget("text"):
            spanish_word.lower(english_word)
            spanish_word.config(text="")
            english_word.config(text="")
            english_word.config(text=words[random_word]["answer"])
        else:
            english_word.lower(spanish_word)
            spanish_word.config(text="")
            english_word.config(text="")
            spanish_word.config(text=words[random_word]["question"])

    count = len(words)

    def next():
        english_word.lower(spanish_word)
        global i
        spanish_word.config(text="")
        english_word.config(text="")
        global random_word
        random_word = randint(0, count - 1)
        if count > 1:
            if random_word == i:
                while random_word == i:
                    random_word = randint(0, count - 1)
            i = random_word
        # update label with Spanish Word
        spanish_word.config(text=words[random_word]["question"])

    def back():
        root.destroy()

    def text_to_sppech():
        if words[random_word]["question"] == spanish_word.cget("text"):
            language = "es"
            mytext = words[random_word]["question"]
        else:
            language = "en"
            mytext = words[random_word]["answer"]

        myobj = gTTS(text=mytext, lang=language, slow=False)
        path = f"{MAIN_PATH}/Speech/x"
        myobj.save(path)
        mixer.init()
        mixer.music.load(path)
        mixer.music.play()
        while mixer.music.get_busy():  # wait for music to finish playing
            time.sleep(1)
        os.remove(path)

    spanish_word = Label(
        root, text="", font=("Helvetica", 45), bg="#6693F5", fg="black"
    )
    spanish_word.place(relx=0.5, rely=0.4, anchor="center")
    english_word = Label(
        root, text="", font=("Helvetica", 45), bg="#6693F5", fg="black"
    )
    english_word.place(relx=0.5, rely=0.4, anchor="center")

    next_button = Button(
        root,
        text="Next",
        command=next,
        fg="black",
        highlightbackground="#6693F5",
        borderwidth=10,
    )
    next_button.place(relx=0.38, rely=0.75, anchor="center")
    hint_button = Button(
        root,
        text="Reveal",
        command=change_general,
        fg="black",
        highlightbackground="#6693F5",
        borderwidth=10,
    )
    hint_button.place(relx=0.58, rely=0.75, anchor="center")

    reproduce_button = Button(
        root,
        text="Reproduce word",
        command=text_to_sppech,
        fg="black",
        highlightbackground="#6693F5",
        borderwidth=10,
    )
    reproduce_button.place(relx=0.72)

    root.bind("<Right>", lambda event: next())
    root.bind("<Up>", lambda event: change())
    root.bind("<Down>", lambda event: change_back())
    root.bind("<Escape>", lambda event: back())

    next()
    root.mainloop()

    return


if __name__ == "__main__":
    main()
