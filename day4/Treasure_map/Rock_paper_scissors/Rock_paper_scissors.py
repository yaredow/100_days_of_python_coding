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

user_input = input("What do you choose? 0 for Rock, 1 for Paper, and 2 for Scissor?\n")
computer_choice = random.randint(0,3)
print(f"The computer chose {computer_choice}")

