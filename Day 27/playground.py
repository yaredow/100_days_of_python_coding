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
# creating text box
text = Text()
text.config(height=5, width=15)
text.focus()
text.insert(END, "Example of text")
text.pack()


# creating a spin box
def spin_box():
    print(spinbox.get())


# checkbutton
def checked_button():
    print(checked_state.get())


checked_state = IntVar()
checkbutton = Checkbutton(text="Is on", variable=checked_state, command=checked_button)
checkbutton.pack()
spinbox = Spinbox(from_=0, to=10, width=5, command=spin_box)
spinbox.pack()

window.mainloop()
