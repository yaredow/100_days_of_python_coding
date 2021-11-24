import random
import art
from art import vs
# a list of dictionaries nested inside of a list from which the celebrities info extracted

Clebritites_instagram = [
    {
        "Name": "Christiano Ronaldo",
        "Profession": "Football player",
        "country": "Portugal",
        "Followers": 315.75
    },
    {
        "Name": "The Rock",
        "Profession": "Professional wrestler, Film actor, and Philanthropist",
        "Country": "Haywar, California, USA",
        "Followers": 254.76 
    },
    {
        "Name": "Ariana Grande",
        "Profession": "Singer",
        "Country": "Boca Raton, Florida, USA",
        "Followers": 252.64 
    },
    {
        "Name": "The Weeknd",
        "Profession": "Singer",
        "Country": "Ethiopia",
        "Followers": 34.74
    },
    {
        "Name": "Teddy Afro",
        "Profession": "Singer and song writer",
        "Country": "Addis Ababa, Ethiopia",
        "Followers": 1
    },
    {
        "Name": "Selena Gomez",
        "Profession": "Actress, producer, and song writer",
        "Country": "Grand prairie, Texas, USA",
        "Followers": 245.5
    },
    {
        "Name": "Justin Bieber",
        "Profession": "Singer and song writer",
        "Country": "Canada",
        "Followers": 183.79
    },
    {
        "Name": "Lionel Messi",
        "Profession": "Footbal player",
        "Country": "Argentina",
        "Followers": 233.79
    }
    
    ]
choice_A = random.choice(Clebritites_instagram)    
choice_B = random.choice(Clebritites_instagram)  

def compare(choice_A, choice_B, user_choice):
    print("Compare A: {}, a {}, from {}.".format(choice_A["Name"], choice_A["Profession"], choice_A["Country"]))
    print(vs)
    print("Against B: {}, a {}, from {}.".format(choice_B["Name"], choice_B["Profession"], choice_B["Country"]))
    


user_choice = input("Who has more follower? 'A' or 'B'? ")
compare(choice_A, choice_B, user_choice)