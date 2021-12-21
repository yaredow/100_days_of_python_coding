from tkinter import *


def mile_converter():
    miles = float(entry.get())
    km = round(miles * 1.609, 2)
    label4.config(text=km)


window = Tk()
window.title("Miles to Km converter")
window.config(padx=20, pady=20)

# creating label
label1 = Label(text="is equal to", font=("Arial", 10, "bold"))
label1.grid(column=0, row=1)

# creating entry
entry = Entry(width=10)
entry.insert(END, string="Mile")
entry.grid(column=1, row=0)

# creating label 2
label2 = Label(text="Miles", font=("Arial", 10, "bold"))
label2.grid(column=2, row=0)

# label 3
label3 = Label(text="Km", font=("Arial", 10, "bold"))
label3.grid(column=2, row=1)

# label4
label4 = Label(text="0", font=("Arial", 10, "bold"))
label4.config(padx=10, pady=5)
label4.grid(column=1, row=1)

# button
button = Button(text="Calculate", command=mile_converter)
button.config(padx=5, pady=10)
button.grid(column=1, row=3)

window.mainloop()
