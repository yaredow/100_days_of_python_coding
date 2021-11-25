import random
from Game_data import Celebritites_instagram
import art
from art import vs
from art import logo
import os


# a list of dictionaries nested inside of a list from which the celebrities info extracted
def clear():
    return os.system('clear')


def format_data(account):
    """returns a formatted list of dictionaries"""
    celeb_name = account["Name"]
    celeb_profession = account["Profession"]
    celeb_country = account["Country"]
    return "{}, a {}, from {}".format(celeb_name, celeb_profession, celeb_country)


def check(number_of_followers_a, number_of_followers_b, user_guess):
    """Receive number of follower and user guess, check and return true or false"""
    if number_of_followers_a > number_of_followers_b:
        return user_guess == "a"
    else:
        return user_guess == "b"


def game():
    score = 0
    continue_operation = True
    # generate a random dictionaries from the nested list
    choice_b = random.choice(Celebritites_instagram)
    print(logo)
    while continue_operation:
        choice_a = choice_b
        choice_b = random.choice(Celebritites_instagram)
        while choice_a == choice_b:
            choice_b = random.choice(Celebritites_instagram)
        # pick number of followers from the randomly generated dictionary
        number_of_followers_a = choice_a["Followers"]
        number_of_followers_b = choice_b["Followers"]

        print("Compare A: {}".format(format_data(choice_a)))
        print(vs)
        print("Against B: {}".format(format_data(choice_b)))
        # receive user guess and store it in variable called "guess"
        user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        # clear the screen after the players saw their score
        follower_check = check(number_of_followers_a, number_of_followers_b, user_guess)
        clear()
        print(logo)
        if follower_check == True:
            score += 1
            print("You are right. The current score: {}".format(score))
        else:
            print("Sorry, that's wrong. Final score: {}".format(score))
            continue_operation = False
game()
