#Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []
for letter in chosen_word:
  display += "_"

guess = input("Guess a letter: ").lower()

for position in range(len(chosen_word)):
  letter = chosen_word[position] 
  if letter == guess:
    display[position] = letter
print(display)
