import random
from art import logo
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURN = 5
number = random.randint(1, 100)
def set_difficulty():
    chosen_difficulty = input("Choose a difficuty. Type 'easy' or 'hard': ").lower()
    if chosen_difficulty == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURN
   
def guess_number(guess, answer, turns):

        if guess < answer:
            print("Too law. \nGuess again")
            return turns - 1
        elif guess > answer:
            print("Too high. \nGuess again")
            return turns - 1
        else:
            print("You got it. the answer was {}".format(number))

def game():
    print(logo)
    print("Welcome to the Number Guessing game")
    print("I'm Thinking of a number between 1 and 100")
    answer = random.randint(1, 100)
    turns = set_difficulty()
    guess = 0
    while answer != guess:
        print("You have {} attempts to guess the number!".format(turns))
        guess =int(input("Guess a number: "))
        turns = guess_number(guess, answer, turns)
        if turns == 0:
            print("You are out of attempts")
game()          