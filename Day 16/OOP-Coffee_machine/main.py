from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
while is_on:
    user_choice = input("What would you like to have? (espresso/latte/cappuccino)?: ")
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        report = CoffeeMaker.report("self")
        print(report)


