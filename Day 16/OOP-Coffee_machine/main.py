from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
while is_on:
    menu = Menu
    option = menu.get_items()
    user_choice = input("What would you like to have? {}?: ".format(option))
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        coffee_maker = CoffeeMaker()
        coffee_maker.report()
    else:
        drink = menu.find_drink
        menu.find_drink(user_choice)
        
        


