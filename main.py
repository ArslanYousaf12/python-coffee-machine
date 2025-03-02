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

# def resources_left():


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


result = is_resource_sufficient("latte")
print(result)

# TODO:3 process the coins
def calculate_monetary_value(quarters, dimes, nickles, pennies):
    quarters_value = quarters * 0.25
    dimes_value = dimes * 0.10
    nickles_value = nickles * 0.05
    pennies_value = pennies * 0.01
    total_value = quarters_value + dimes_value + nickles_value + pennies_value
    print(total_value)
    return total_value


calculate_monetary_value(quarters=1, dimes=2, nickles=1, pennies=2)




#TODO:4 Check Transaction SuccessFul


#TODO:5 Make Coffee
