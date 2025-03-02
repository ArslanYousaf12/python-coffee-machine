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

user_choice = input(" What would you like? (espresso/latte/cappuccino): ").lower()

# TODO: 1 print report


def print_report():
    for key in resources:
        print(f"{key}: {resources[key]}")


if user_choice == "report":
    print_report()



#TODO:2 check resources sufficient


#TODO:3 process the coins


#TODO:4 Check Transaction SuccessFul


#TODO:5 Make Coffee
