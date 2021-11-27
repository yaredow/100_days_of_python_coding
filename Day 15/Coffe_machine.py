MENU = {
    "espresso": { 
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def coins():
    coin = 0
    quarter = float(input("how many quarters? "))
    coin += quarter * 0.25
    dime = float(input("how many dimes?: "))
    coin += dime * 0.1
    nickel = float(input("how many nickels? "))
    coin += nickel * 0.05
    penny = float(input("how many pennies? "))
    coin += penny * 0.01
    return coin

#TODO: 1. prompt the user by asking what they would like.
user_choice = input("What would you like? (espresso/latte/cappuccino):\n")
coins = input("Please insert coins:\n")
#TODO: 5. Process coins.
print("Please insert coins.")
coins()

#TODO: 2. Turn off the Coffee Machine by entering “​off​” to the prompt.

#TODO: 3. Print report.

#TODO: 4. Check resources sufficient?



#TODO: 6. Check transaction successful?

#TODO: 7. Make Coffee.