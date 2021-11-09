## Step one

the first step in creating the Hangman game is to create.

### step one

* Randomly choose a word from the word_list and assign it to a variable called chosen_word.
* Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
* Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

### step two

* Create an empty List called display.
* For each letter in the chosen_word, add a "_" to 'display'.
* So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
* Loop through each position in the chosen_word;
* Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".

### step three

* Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

### step fou
* Create a variable called 'lives' to keep track of the number of lives left. 
* Set 'lives' to equal 6
* If guess is not a letter in the chosen_word,
* Then reduce 'lives' by 1. 
* If lives goes down to 0 then the game should stop and it should print "You lose."
* Join all the elements in the list and turn it into a String.
* Join all the elements in the list and turn it into a String.
* print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    