import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# assigning the computer image
computer_image = [rock, paper, scissors]
user_input = int(input("What do you choose? 0 for Rock, 1 for Paper, and 2 for Scissor?\n"))
# checking the conditions
if user_input >= 3 and user_input < 0:
    print("That is invalid number")
else:
    print(f"{computer_image[user_input]}")
    computer_choice = random.randint(0,2)
    print(f"The computer chose: ")
    print(f"{computer_image[computer_choice]}")

    if computer_choice == 2 and user_input == 0:
        print("You win!")
    elif  computer_choice == 0 and user_input == 2:
        print("You win!")
    elif user_input == 1 and computer_choice == 0:
        print("You win!")
    elif computer_choice == user_input:
        print("That is a draw")
    elif computer_choice > user_input:
        print("you lose")
