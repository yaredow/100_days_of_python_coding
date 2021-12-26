from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- New flash card ------------------------------- #
data_dict = {}

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/Amharic.csv")
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")
    random_dict = {}


def new_flash_card():
    global random_dict, flip_timer
    window.after_cancel(flip_timer)
    random_dict = random.choice(data_dict)
    amharic_word = random_dict["Amharic"]
    canvas.itemconfig(text1, text="Amharic", fill="black")
    canvas.itemconfig(text2, text=f"{amharic_word}", fill="black")
    canvas.itemconfig(canvas_image, image=card_front_image)
    flip_timer = window.after(3000, func=flip_the_card)


# ---------------------------- flip the card ------------------------------- #
def flip_the_card():
    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(text1, text="English", fill="white")
    new_text = random_dict["English"]
    canvas.itemconfig(text2, text=new_text, fill="white")


# ---------------------------- saving the known words ------------------------------- #
def is_known():
    data_dict.remove(random_dict)
    data = pandas.DataFrame(data_dict)
    data.to_csv("./data/words_to_learn.csv")
    new_flash_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Konjo")
window.config(padx=40, pady=40, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_the_card)
# creating canvas
canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="./images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=card_front_image)
card_back_image = PhotoImage(file="./images/card_back.png")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
text1 = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
text2 = canvas.create_text(400, 300, text="Word", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)
# creating buttons
right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(column=0, row=1)
wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, fg=BACKGROUND_COLOR, highlightthickness=0, command=new_flash_card)
wrong_button.grid(column=1, row=1)
new_flash_card()
window.mainloop()
