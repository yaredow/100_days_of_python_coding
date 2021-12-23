from tkinter import *
from tkinter import messagebox
import pyperclip
import string
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
    random.shuffle(characters)
    password = ""
    for i in range(16):
        password += random.choice(characters)
    password_entry.insert(END, string=password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Please don't leave any of the field empty")
    else:
        is_ok = messagebox.askokcancel(title="Website",
                                       message=f"These are the information entered:\nEmail: {email_username}\nPassword: {password}")
        if is_ok:
            with open("data.txt", "a+") as user_data:
                user_data.write(f"Website: {website} | Email/Username: {email_username} | Password: {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


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
generate_password_button = Button(text="Generate Password", highlightthickness=0, width=12, command=password_generator)
generate_password_button.grid(column=2, row=3)
# add button
add_button = Button(text="Add", width=37, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
