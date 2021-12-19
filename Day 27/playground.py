from tkinter import *


def action():
    print("search not found")


# creating the window
window = Tk()
window.title("My first GUI")
window.minsize(height=300, width=500)
# creating a label
label = Label()
label.config(text="My new Label", font=("Arial", 15, "bold"))
label.pack()
# creating a button
button = Button(text="Search", command=action)
button.pack()
# creating entry
entry = Entry(width=30)
entry.insert(END, string="some text to begin with")
entry.pack()
window.mainloop()
