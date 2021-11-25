import random
from Game_data import Celebritites_instagram
import art
from art import vs
from art import logo

# a list of dictionaries nested inside of a list from which the celebrities info extracted

def format_data(account):
    """returns a formated list of dictionaries"""
    celeb_name = account["Name"]
    celeb_profession = account["Profession"]
    celeb_country = account["Country"]
    return "{}, a {}, from {}".format(celeb_name, celeb_profession, celeb_country)

def check(number_of_followers_a, number_of_followers_b, user_guess):
    """Recieve number of follower and user guess, check and return true or false"""
    if number_of_followers_a > number_of_followers_b:
        return True
    else:
        return False


continue_operation = True
choice_b = random.choice(Celebritites_instagram)
while continue_operation:
    print(logo)
    # generate a random dictionaries from the nested list
    choice_a = choice_b
    choice_b = random.choice(Celebritites_instagram)
    while choice_a == choice_b:
        choice_b = random.choice(Celebritites_instagram)
    # pick number of followers from the randomly generated dictionery
    number_of_followers_a = choice_a["Followers"]
    number_of_followers_b = choice_b["Followers"]

    # Check if both the generated values are equal. if they are equal generated the second one again 
    if choice_a == choice_b:
        choice_b = random.choice(Celebritites_instagram)
    print("Compare A: {}".format(format_data(choice_a)))
    print(vs)
    print("Against B: {}".format(format_data(choice_b)))

    # recieve user guess and store it in avariable called "guess"
    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    score = 0
    follower_check = check(number_of_followers_a, number_of_followers_b, user_guess)
    if follower_check == True:
        score += 1
        print("You are right. The current score: {}".format(score))
    else:
        print("Sorry, that's wrong. Final score: {}".format(score))
        continue_operation = False


