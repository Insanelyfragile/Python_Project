from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

a = 0
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
is_on = True
while is_on:
    meenu = menu.get_items()
    cf = input(f"What would you like ({meenu})? :").lower()
    drink = menu.find_drink(cf)
    if cf == "report":
        coffee_maker.report()
        money_machine.report()
    elif cf == "off":
        is_on = False
    elif coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
        coffee_maker.make_coffee(drink)

