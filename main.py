from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menus = Menu()
available_drinks = menus.get_items()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_on= True
while is_on:
    print(f"What would you like? {available_drinks}")
    choice = input("What drink you want: ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(coffee_maker.report())
        print(money_machine.report())
    else:
        menuItem = menus.find_drink(choice)
        resource_sufficient = coffee_maker.is_resource_sufficient(menuItem)
        if resource_sufficient:
            # money_received = money_machine.process_coins()
            payment = money_machine.make_payment(menuItem.cost)
            if payment:
                coffee_maker.make_coffee(menuItem)

