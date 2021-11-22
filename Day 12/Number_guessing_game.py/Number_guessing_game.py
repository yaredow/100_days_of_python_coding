import random
print("Welcome to the Number Guessing game")
print("I'm Thinking of a number between 1 and 100")
print("Pssst, The correct answer is {}".format(random.randint(1, 100)))


choosen_difficulty = input("choose a difficulty! type 'easy' or 'hard' ").lower()

user_input = int(input("Make a guess:\n"))

