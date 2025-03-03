from typing import Any

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
is_on = True
profit = 0

def is_resource_sufficient(ordered_ingredient):
    for item in ordered_ingredient:
        if ordered_ingredient[item] >= resources[item]:
            print(f"There are not enough {item}")
            return False
    return True


def process_coin():
    print("Please Insert the coins")
    total = 0
    total = int(input("How many quarters ")) * 0.25
    total += int(input("How many dimes ")) * 0.10
    total += int(input("How many nickles ")) * 0.05
    total += int(input("How many pennies ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost)
        print(f"Please collect your change {change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredient):
    for items in order_ingredient:
        resources[items] -= order_ingredient[items]
    print(f"Here is your {drink_name}")


while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        print(MENU[choice])
        drink = MENU[choice]
        print(drink["ingredients"])
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coin()
            print(payment)
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])


