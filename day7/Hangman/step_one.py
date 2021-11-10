#Step 1

word_list = ["aardvark", "baboon", "camel"]
import random
chosen_word = random.choice(word_list)
guess = input("guess a letter: ").lower()
for letter in chosen_word:
    if letter == guess:
        print("right")
    else:
        print("wrong")

