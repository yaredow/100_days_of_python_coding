class QuizBrain:
    
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0 


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input("Q.{}: {} (True/False)? ".format(self.question_number, current_question.text)) 
        self.check_answer(user_answer, current_question.answer)


    def still_has_question(self):
        if self.question_number <= len(self.question_list):
            return True
        else:
            return False
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right")
            print("Your current score is {}".format(self.score))
        else:
            print("That's wrong.".format(correct_answer))
        print("The correct answer is {}".format(correct_answer))
        print("Your current score is: {}/{}".format(self.score, self.question_number))