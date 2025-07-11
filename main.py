from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("PyNumberWizard")
root.geometry("800x600")
root.resizable(False, False)
root.config(bg="#232A2F")

# Docs and keys for each widget
# print(widget.configure().keys())

# Colors (to save time)
bgc = "#232A2F"
fgc = "#bfbfbf"

# Some setup variables
isGameActive = False

guess = 50  # Starting guess for the game
maxNumber = 100  # Maximum number for the game
minNumber = 1  # Minimum number for the game

# Logic for the wizard
def startWizard():
    global isGameActive, guess, currentNumber
    isGameActive = True
    currentNumber.grid(row=0, column=0)
    currentNumber.config(text=f"Thinking about number: {guess}")  # Initial guess

def higher():
    global isGameActive, guess, currentNumber, maxNumber, minNumber
    if isGameActive:
        minNumber = guess + 1  # Update the minimum number
        guess = (maxNumber + minNumber) // 2
        currentNumber.config(text=f"Thinking about number: {guess}")  # Update guess label

def lower():
    global isGameActive, guess, currentNumber, maxNumber, minNumber
    if isGameActive:
        maxNumber = guess - 1  # Update the maximum number
        guess = (maxNumber + minNumber) // 2
        currentNumber.config(text=f"Thinking about number: {guess}")  # update guess label

def showCelebration():
    if isGameActive:
        celebration = messagebox.Message(root, message="I won, too smart :)", title="Celebrating", default=messagebox.OK)
        celebration.show()
        resetGame()

def resetGame():
    global isGameActive, guess, currentNumber, maxNumber, minNumber
    isGameActive = False
    guess = 50
    currentNumber.grid_forget()
    maxNumber = 100
    minNumber = 1

# TODO: reset logic and celebration

# Title
title = Label(root, text="PyNumberWizard", font=("Ubuntu", 24), fg=fgc, bg=bgc)
title.pack(pady=20, anchor="nw", padx=20)


# Frame for instructions
instructionsFrame = Frame(root, bg=bgc)
instructionsFrame.pack()

# Display current number
currentNumber = Label(instructionsFrame, text="Thinking about number: ", font=("Ubuntu", 16), fg=fgc, bg=bgc)
currentNumber.grid(pady=10, padx=20, row=0, column=0)
currentNumber.grid_forget()  # To make it hidden at the start of the game

# Higher lower buttons
higherButton = Button(instructionsFrame, text="Higher", font=("Ubuntu", 16), fg=fgc, bg="#2C3333", command=higher)
higherButton.grid(pady=10, row=1, column=0, padx=10)

lowerButton = Button(instructionsFrame, text="Lower", font=("Ubuntu", 16), fg=fgc, bg="#2C3333", command=lower)
lowerButton.grid(pady=10, row=1, column=1, padx=10)

# Revealing the correct number
correctBtn = Button(root, text="Correct!", font=("Ubuntu", 16), fg=fgc, bg="#2C3333", command=showCelebration)
correctBtn.pack(pady=10)

# Reset button to start over
resetBtn = Button(root, text="Reset", font=("Ubuntu", 16), fg=fgc, bg="#2C3333", command=resetGame, width=6)
resetBtn.place(x=700, y=20)

# Start button
startBtn = Button(root, text="Start", font=("Ubuntu", 16), fg=fgc, bg="#2C3333", command=startWizard, width=6)
startBtn.place(x=700, y=60)

# Label explaining the game
instructions =  "Try to think of a whole number between 1 and 100 then press start\n" \
                "and I will try to guess it through a binary search!\n" \
                "You can tell me if my guess is higher, lower, or correct.\n"
instructionsLabel = Label(root, text=instructions, font=("Ubuntu", 16), fg=fgc, bg=bgc)
instructionsLabel.pack(pady=20, padx=20)


# Start the application
if __name__ == "__main__":
    root.mainloop()
