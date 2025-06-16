from tkinter import *

root = Tk()
root.title("PyNumberWizard")
root.geometry("800x600")
root.resizable(False, False)
root.config(bg="#232A2F")

# Colors (to save time)
bgc = "#232A2F"
fgc = "#bfbfbf"

# Title
title = Label(root, text="PyNumberWizard", font=("Ubuntu", 24), fg=fgc, bg=bgc)
title.pack()

placeholder = Label(root, text="Placeholder label", font=("Ubuntu", 16), fg=fgc, bg=bgc)
placeholder.place(x=100, y=400)

another_placeholder = Label(root, text="Another placeholder label", font=("Ubuntu", 16), fg=fgc, bg=bgc)
another_placeholder.pack()

# Start the application
if __name__ == "__main__":
    root.mainloop()
