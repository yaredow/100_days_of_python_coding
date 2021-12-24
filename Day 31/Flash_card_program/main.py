from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"


# ---------------------------- New flash card ------------------------------- #
def new_flash_card():
    data = pandas.read_csv("./data/Amharic.csv")
    data_dict = data.to_dict(orient="records")
    random_dict = random.choice(data_dict)
    amharic_word = random_dict["Amharic"]
    canvas.itemconfig(text2, text=f"{amharic_word}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Konjo")
window.config(padx=40, pady=40, bg=BACKGROUND_COLOR)
# creating canvas
canvas = Canvas(width=800, height=526)
front_image = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
text1 = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
text2 = canvas.create_text(400, 300, text="Word", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)
# creating buttons
right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=new_flash_card)
right_button.grid(column=0, row=1)
wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, fg=BACKGROUND_COLOR, highlightthickness=0, command=new_flash_card)
wrong_button.grid(column=1, row=1)

window.mainloop()
