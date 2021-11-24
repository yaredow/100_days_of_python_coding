import random
from Game_data import Celebritites_instagram
import art
from art import vs
from art import logo
# a list of dictionaries nested inside of a list from which the celebrities info extracted
def format_data(account):
    celeb_name = account["Name"]
    celeb_profession = account["Profession"]
    celeb_country = account["Country"]
    return "{}, a {}, from {}".format(celeb_name, celeb_profession, celeb_country)
print(logo)
choice_a = random.choice(Celebritites_instagram)    
choice_b = random.choice(Celebritites_instagram)  
if choice_a == choice_b:
    choice_b = random.choice(Celebritites_instagram)
print("Compare A: {}".format(format_data(choice_a)))
print(vs)
print("Against B: {}".format(format_data(choice_b)))

user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()