import random
from art import logo
EASY_LEVEL_TURN = 10
HARD_LEVEL_TURN = 5
def difficulty_level():
    """Checks the randomly generated number with the guess"""
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURN
    else:
        return HARD_LEVEL_TURN
def guess_evaluator(guess, answer, turns):
    if guess > answer:
        print("Too High")
        return turns -1
    elif guess < answer:
        print("Too low")
        return turns -1
    else:
        print("You got it. The answer was {}".format(answer))

def game():
    print(logo)
    print("Welcome to a number guessing game!")
    print("I'm thining of a number between 1 and 100")
    answer = random.randint(1, 100)
    turns = difficulty_level()
    guess = 0
    while guess != answer:
        print("You have {} attempts to guess the number.".format(turns))
        guess = int(input("Make a guess: "))
        turns = guess_evaluator(guess, answer, turns)
        if turns == 0:
            print("You are out of attempts. You lose")
            return
        
        elif guess != answer:
            print("Guess again")
game()



