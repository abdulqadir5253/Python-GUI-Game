import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import re

# Declaring global variable

timeleft = 60
score = 0
text = ""
foreGround = ""

# file open and get the variables
file = open("highestScore.txt", "r")
a = file.read()
hgstScore = "".join(re.findall("[0-9]", a))
name = []
name = re.split("[[]", a)
name = name[1]
length = len(name)
name = name[:(length - 1)]








# Declaring a function to create widgets for the game

def CreateWidgets():
    instLabel = Label(root, text="Enter Color of the Text",
                      font=("Helvetica", 30),
                      background="WHITE")
    instLabel.grid(row=0, column=0, columnspan=3, padx=5, pady=15)

    highestScore = Label(root, text="Highest Score: " + hgstScore,
                         font=("Helvetica", 20),
                         background="WHITE"
                         )
    highestScore.grid(row=0, column=3)

    scorerName = Label(root, text="Name: " + name,
                       font=("Helvetica", 20),
                       background="WHITE")
    scorerName.grid(row=1, column=3)

    startButton = Button(root, text="START GAME", width=20,
                         font=("Helvetica", 15), command=buttonPress,
                         background="WHITE")
    startButton.grid(row=1, column=0, pady=15, columnspan=3)

    stopButton = Button(root, text="Stop game", background="WHITE", command=EndGame)
    stopButton.grid(row=5, pady=15, columnspan=3)

    root.timeLabel = Label(root, text="TIME LEFT: ",
                           font=('Helvetica', 30),
                           background="WHITE")
    root.timeLabel.grid(row=2, column=0, padx=5, pady=15)

    root.scoreLabel = Label(root, text="Score: " + str(score),
                            font=('Helvetica', 30),
                            background="WHITE")
    root.scoreLabel.grid(row=2, column=1, padx=5, pady=15)

    root.gameLabel = Label(root,
                           font=('Comic Sans MS', 60),
                           background="WHITE")
    root.gameLabel.grid(row=3, column=0, padx=5, pady=15, columnspan=2)

    root.answerEntry = Entry(root, width=50,
                             font=60,
                             background="SILVER")
    root.answerEntry.grid(row=4, column=0, padx=5, pady=15, columnspan=2)
    root.answerEntry.focus()


# Defining buttonMethod

def buttonPress():
    global timeleft
    global score

    if timeleft == 60:
        StartGame()
    elif 0 < timeleft < 60:
        messagebox.showinfo("Score Box", "Your Score is: " + str(score))
        timeleft = 60
        score = 0
        root.scoreLabel.config(text="Score: " + str(score))
        root.gameLabel.config(text="")
        CreateWidgets()


# Defining function to start game

def StartGame():
    # Calling the above declare global variable
    global timeleft
    global text
    global foreGround

    # Checking if the timeleft is greater than 0. If yes do the following
    if timeleft == 60:
        text, foreGround = colorGenerator()
    if timeleft > 0:
        # Decrementing the timeleft by 1
        timeleft -= 1

        # Displaying the time left in above created label for time left
        root.timeLabel.config(text="Time Left: " + str(timeleft))
        root.timeLabel.after(1000, StartGame)


    # If timeleft is equal to 0, then stop the game and display the user's score
    else:
        if int(hgstScore) < score:
            writeCodeDisplay()
        else:
            messagebox.showinfo("Time UP!", "Your Score is: " + str(score))


# Stop the game
def EndGame():
    messagebox.showinfo("Game Stopped ", "Your Score " + str(score))
    exit()


# defining game to check score
def game(event):
    global score
    global text
    global foreGround

    # Check if the user's input is equal to the Font Color of the Text

    if root.answerEntry.get().lower() == foreGround.lower():
        # If yes increment the score by one
        score += 1

        # Displaying the score
        root.scoreLabel.config(text="Score: " + str(score))

        # Clearing the user's entry
        root.answerEntry.delete(0, END)

        # Calling the colorGenerator() to produce the next question
        text, foreGround = colorGenerator()

    else:
        # Calling the colorGenerator() to produce the next question
        text, foreGround = colorGenerator()

        # Clearing the user's entry
        root.answerEntry.delete(0, END)


# Writing the code in file


def writeCodeDisplay():
    root_new.deiconify()
    root_new.nameEntry = Entry(root_new)
    root_new.nameEntry.grid(row=1, column=1)
    root_new.nameEntry.focus()
    root_new.bind('<Return>', writeCode)
    # Storing the values for future


def writeCode(event):
    file = open("highestScore.txt", "w")
    a = str(score)
    file.write("highestScore = " + a + "\n")
    file.write("name = [" + root_new.nameEntry.get() + "]")
    file.close()
    root_new.withdraw()
    messagebox.showinfo("High Scorer Board", root_new.nameEntry.get()+" \nis the new High score Achiever")


# Defining random color generator

def colorGenerator():
    randomColor = ['RED', 'GREEN', 'BLUE', 'VIOLET', 'PINK', 'BROWN', 'BLACK']

    # Shuffling the list
    random.shuffle(randomColor)
    root.gameLabel.config(text=str(randomColor[0]), fg=randomColor[1])

    return randomColor[0], randomColor[1]


# Creating object of the class
root = tk.Tk()
root_new = tk.Tk()
root_new.withdraw()

root.bind('<Return>', game)

# Starting the title and background color
# displaying the resizing property

root.title("PyColor Game")
root_new.title("High Scorer!")
root.configure(background="WHITE")
root.resizable(False, False)

CreateWidgets()

root.mainloop()