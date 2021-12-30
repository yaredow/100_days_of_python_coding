from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.user_answer = quiz_brain
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # creating canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Something", fill=THEME_COLOR,
                                                     font=("Arial", 15, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        # button
        image = PhotoImage(file="./images/true.png")
        self.right_button = Button(image=image, highlightthickness=0, command=self.true_pressed)
        self.right_button.grid(column=0, row=2)
        image1 = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=image1, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)
        # score label
        self.score_label = Label(text="score=0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score={self.quiz.score}")
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def true_pressed(self):
        is_true = self.quiz.check_answer("True")
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_true = self.quiz.check_answer("False")
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_true):
        if is_true:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        after = self.window.after(1000, func=self.get_next_question)

