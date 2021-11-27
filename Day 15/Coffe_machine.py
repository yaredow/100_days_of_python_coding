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


def process_coins():
    total_coin = 0
    print("Please inter coins: ")
    quarter = float(input("how many quarters? "))
    total_coin += quarter * 0.25
    dime = float(input("how many dimes?: "))
    total_coin += dime * 0.1
    nickel = float(input("how many nickels? "))
    total_coin += nickel * 0.05
    penny = float(input("how many pennies? "))
    total_coin += penny * 0.01
    return total_coin


def is_enough_ingrident(required_ingrident):
    is_enough = True
    for item in required_ingrident:
        required_ingrident[item] >= resources[item]
        is_enough = False
    return is_enough  


def transaction_check(money_recived, drink_cost):
    if money_recived > drink_cost:
        global profit
        change = money_recived - drink_cost - drink_cost
        profit += change
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
            