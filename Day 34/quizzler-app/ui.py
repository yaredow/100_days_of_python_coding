from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # creating canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.create_text(150, 125, text="Something", fill=THEME_COLOR,  font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        # button
        image = PhotoImage(file="./images/true.png")
        self.right_button = Button(image=image, highlightthickness=0)
        self.right_button.grid(column=0, row=2)
        image1 = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=image1, highlightthickness=0)
        self.false_button.grid(column=1, row=2)
        # score label
        self.score_label = Label(text="score=0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.window.mainloop()
