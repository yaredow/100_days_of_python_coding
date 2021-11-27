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

profit = 0 


def is_enough_ingrident(orderd_ingrident):
    for item in orderd_ingrident:
        orderd_ingrident[item] > resources[item]
        return False
    return True


def process_coins():
    print("Please insert coins")
    total_coin = int(input("How many quarters?: ")) * 0.25
    total_coin += int(input("How many dimes?: ")) * 0.1
    total_coin += int(input("How many nickles?: ")) * 0.05 
    total_coin += int(input("How many pennies?: ")) * 0.01
    return total_coin


def transaction_check(money_recived, drink_cost):
    if money_recived >= drink_cost:
        global profit
        change = round(money_recived - drink_cost, 2)
        profit += change
        print("Here is ${} in change".format(profit))
        return True
    else:
        print("​Sorry that's not enough money. Money refunded.")
        return False

is_on = True
while is_on:
    user_choice = input("​What would you like? (espresso/latte/cappuccino): ")
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        print("Water: {}ml".format(resources['water']))
        print("Milk: {}ml".format(resources['milk']))
        print("Coffee: {}g".format(resources['coffee']))
    else:
        drink = MENU[user_choice]
        if is_enough_ingrident(drink["ingredients"]):
            payment = process_coins()
            transaction_check(payment, drink["cost"])
            