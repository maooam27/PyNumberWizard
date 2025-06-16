from tkinter import *

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


# Logic for the wizard
def startWizard():
    print(numberEntry.get())



# Title
title = Label(root, text="PyNumberWizard", font=("Ubuntu", 24), fg=fgc, bg=bgc)
title.pack(pady=20, anchor="nw", padx=20)

# Frame for instructions
instructionsFrame = Frame(root, bg=bgc)
instructionsFrame.pack()

# Label for number selection
numberChoosingLabel = Label(instructionsFrame, text="Choose your number!", font=("Ubuntu", 16), fg=fgc, bg=bgc)
numberChoosingLabel.grid(pady=10, row=0, column=0, padx=10)

# Entry for number selection
numberEntry = Entry(instructionsFrame, font=("Ubuntu", 16), fg=fgc, bg="#2C3333", width=10)
numberEntry.grid(pady=10, row=0, column=1, padx=10)

# Button to submit the number
submitBtn = Button(root, text="Submit", font=("Ubuntu", 16), fg=fgc, bg="#2C3333", command=startWizard)
submitBtn.pack(pady=10)


# TODO: validate the input

# Start the application
if __name__ == "__main__":
    root.mainloop()
