import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURN = 5
number = random.randint(1, 100)
def guess_number(user_input, number):

        if user_input < number:
            print("Too law. \nGuess again")
        elif user_input < number:
            print("Too high. \nGuess again")
        else:
            game_over = True
            print("You got it. the answer was {}".format(number))

def game_level():
    if chosen_difficulty == "easy":
        return "You have {} attempts to guess the game".format(EASY_LEVEL_TURNS)
    elif chosen_difficulty == "hard":
        return "You have {} attempts to guess the game".format(HARD_LEVEL_TURN)
    else:
        return "Wrong input"

def game():
    print("Welcome to the Number Guessing game")
    print("I'm Thinking of a number between 1 and 100")
    print("Pssst, The correct answer is {}".format(random.randint(1, 100)))
    chosen_difficulty = input("Choose a difficuty. Type 'easy' or 'hard': ").lower()
    print(game_level())
    while number != user_input:
        user_input =int(input("Guess a number: "))
        print(guess_number(user_input, number))
game()        