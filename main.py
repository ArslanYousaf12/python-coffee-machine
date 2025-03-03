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
profit = 0.0
price = {
"latte" : 2.50,
"espresso" : 3.50,
"cappuccino" : 3.60
}


is_machine_stop = False
user_choice = input(" What would you like? (espresso/latte/cappuccino): ").lower()


# TODO: 1 print report


def print_report():
    for key in resources:
        print(f"{key}: {resources[key]}")


if user_choice == "report":
    print_report()

# Turn off the machine
if user_choice == "off":
    is_machine_stop = True


#TODO:2 check resources sufficient


latte = {
        "water": 100,
        "milk": 55,
        "coffee": 30
    }
expresso = {
        "water": 0,
        "milk": 10,
        "coffee": 25
    }
cappuccino = {
        "water": 200,
        "milk": 10,
        "coffee": 35
    }


def is_resource_sufficient(drink):
    water = 0
    milk = 0
    coffee = 0
    for res in resources:
        if res == "water":
            water = resources[res]
        elif res == "milk":
            milk = resources[res]
        else:
            coffee = resources[res]
    if drink == "latte" and water >= 100 and milk >= 50 and coffee >= 30:
        return True
    elif drink == "expresso" and milk >= 10 and coffee >= 25:
        return True
    elif drink == "cappuccino" and water >= 200 and milk >= 100 and coffee >= 35:
        return True
    else:
        return False


result = is_resource_sufficient(user_choice)
if not result:
    print("There is not Enough resources")
else:
    print("Enough resources for drink")


# TODO:3 process the coins
def calculate_monetary_value(quarters, dimes, nickles, pennies):
    quarters_value = quarters * 0.25
    dimes_value = dimes * 0.10
    nickles_value = nickles * 0.05
    pennies_value = pennies * 0.01
    total_value = quarters_value + dimes_value + nickles_value + pennies_value
    print(total_value)
    return total_value


total_money: float | Any = calculate_monetary_value(quarters=4, dimes=5, nickles=34, pennies=2)


# TODO:4 Check Transaction SuccessFul


def is_transaction_successful(total_value, selected_drink):
    if selected_drink == "latte":
        if total_value >= 2.50:
            if total_value > 2.50:
                remaining = total_value - 2.50
                print(f"Here your change {remaining} ")
            print("Here is your latte")
            return True
        else:
            print(f"Sorry {total_value} that not enough money")
            return False
    elif selected_drink == "expresso":
        if total_value >= 3.50:
            if total_value > 2.50:
                remaining = total_value - 2.50
                print(f"Here your change {remaining} ")
            print("Here is your latte")
            return True
        else:
            print(f"Sorry {total_value} that not enough money")
            return False
    elif selected_drink == "cappuccino":
        if total_value >= 3.60:
            if total_value > 2.50:
                remaining = total_value - 2.50
                print(f"Here your change {remaining} ")
            print("Here is your latte")
            return True
        else:
            print(f"Sorry {total_value} that not enough money")
            return False


transaction = is_transaction_successful(total_value=total_money, selected_drink=user_choice)


def resource_deduction(drink):
    for res in resources:
        resources[res] = resources[res] - drink[res]



#TODO:5 Make Coffee

if transaction:
    profit = profit + price[user_choice]
    if user_choice == "latte":
        resource_deduction(latte)

    elif user_choice == "expresso":
        resource_deduction(expresso)
    else:
        resource_deduction(cappuccino)


print_report()

