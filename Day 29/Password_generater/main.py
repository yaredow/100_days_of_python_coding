from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    pass


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Konjo Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
lock_key_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_key_image)
canvas.grid(column=1, row=0)
# creating website label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
# email and username label
email_username_label = Label(text="Email/Username: ")
email_username_label.grid(column=0, row=2)
# password label
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
# website entry
website_entry = Entry(width=40)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)
# email and username entry
email_username_entry = Entry(width=40)
email_username_entry.insert(END, string="yaredyilma11@gmail.com")
email_username_entry.grid(column=1, row=2, columnspan=2)
# password entry
password_entry = Entry(width=24)
password_entry.grid(column=1, row=3)
# password generator button
generate_password_button = Button(text="Generate Password", highlightthickness=0, width=12)
generate_password_button.grid(column=2, row=3)
# add button
add_button = Button(text="Add", width=37)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
