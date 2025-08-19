# Coffee Machine Project:

# _________         _____  _____                   
# \_   ___ \  _____/ ____\/ ____\____   ____       
# /    \  \/ /  _ \   __\\   __\/ __ \_/ __ \      
# \     \___(  <_> )  |   |  | \  ___/\  ___/      
#  \______  /\____/|__|   |__|  \___  >\___  >     
#         \/                        \/     \/      
#    _____                .__    .__               
#   /     \ _____    ____ |  |__ |__| ____   ____  
#  /  \ /  \\__  \ _/ ___\|  |  \|  |/    \_/ __ \ 
# /    Y    \/ __ \\  \___|   Y  \  |   |  \  ___/ 
# \____|__  (____  /\___  >___|  /__|___|  /\___  >
#         \/     \/     \/     \/        \/     \/ 


# Menu with ingredients and prices:
MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0,
    }
}

# Resources inside the machine
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0,
}

# Function: report
def print_report():
    print(f"Water: {resources['water']} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} g")
    print(f"Money: ${resources['money']:.2f}")

# Function: check resources
def is_resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources.get(item, 0):
            print(f"Sorry there is not enough {item}.")
            return False
    return True

# Function: process coins
def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickels = int(input("How many nickels? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01
    return quarters + dimes + nickels + pennies

# Function: check transaction
def is_transaction_successful(money_received, drink_cost):
    if money_received < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif money_received > drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
    resources["money"] += drink_cost
    return True

# Function: make coffee
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy! ☕")

# Main program loop
def coffee_machine():
    is_on = True
    while is_on:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == "off":
            is_on = False
        elif choice == "report":
            print_report()
        elif choice in MENU:
            drink = MENU[choice]
            if is_resources_sufficient(drink["ingredients"]):
                payment = process_coins()
                if is_transaction_successful(payment, drink["cost"]):
                    make_coffee(choice, drink["ingredients"])
        else:
            print("Invalid option. Please choose espresso, latte, or cappuccino.")

coffee_machine()