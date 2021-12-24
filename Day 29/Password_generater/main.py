from tkinter import *
from tkinter import messagebox
import pyperclip
import string
import random
import json


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
    new_data = {
        website: {
            "email": email_username,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Please don't leave any of the field empty")
    else:
        try:
            with open("data.json", "r") as user_data:
                data = json.load(user_data)

        except FileNotFoundError:
            with open("data.json", "w") as user_data:
                json.dump(new_data, user_data, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as user_data:
                json.dump(data, user_data, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- Find password------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message=f"No data file found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title="email",
                                message=f"website: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No detail for {website} available")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Konjo Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
lock_key_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_key_image)
canvas.grid(column=1, row=0)
# label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_username_label = Label(text="Email/Username: ")
email_username_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
# entries
website_entry = Entry(width=24)
website_entry.focus()
website_entry.grid(column=1, row=1)
email_username_entry = Entry(width=40)
email_username_entry.insert(END, string="yaredyilma11@gmail.com")
email_username_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=24)
password_entry.grid(column=1, row=3)
# buttons
generate_password_button = Button(text="Generate Password", highlightthickness=0, width=12, command=password_generator)
generate_password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=37, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)
search_button = Button(text="Search", width=12, command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()
