import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURN = 5
number = random.randint(1, 100)
def guess_number(guess, answer, turns):

        if guess < answer:
            print("Too law. \nGuess again")
            turns -= 1
        elif guess < answer:
            print("Too high. \nGuess again")
            turns -= 1
        else:
            game_over = True
            print("You got it. the answer was {}".format(number))

def set_difficulty():
    chosen_difficulty = input("Choose a difficuty. Type 'easy' or 'hard': ").lower()
    if chosen_difficulty == "easy":
        return EASY_LEVEL_TURNS
    elif chosen_difficulty == "hard":
        return HARD_LEVEL_TURN
   

def game():
    print("Welcome to the Number Guessing game")
    print("I'm Thinking of a number between 1 and 100")
    answer = random.randint(1, 100)
    turns = set_difficulty()
    guess = 0
    while answer != guess:
        print("You have {} attempts to guess the number!".format(turns))
        guess =int(input("Guess a number: "))
        turns = guess_number(guess, answer, turns)
game()        