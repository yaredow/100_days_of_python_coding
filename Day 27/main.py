from tkinter import *

window = Tk()
window.title("My first GUI")
window.minsize(height=300, width=500)
# creating label
my_label = Label(text="New label", font=("Arial", 20, "bold"))
my_label.pack()


def great_the_god():
    print("Hello Yared")
    text = input.get()
    my_label.config(text=text)


button = Button(text="Greeting", command=great_the_god)
button.pack()
input = Entry()
input.pack()
window.mainloop()
