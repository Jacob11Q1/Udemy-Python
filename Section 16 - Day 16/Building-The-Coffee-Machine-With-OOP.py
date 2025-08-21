# Building The Coffee Machine With OOP:

class CoffeeMachine:
    def __init__(self):
        # Resources
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
        self.money = 0

        # Menu
        self.menu = {
            "espresso": {"water": 50, "milk": 0, "coffee": 18, "cost": 1.5},
            "latte": {"water": 200, "milk": 150, "coffee": 24, "cost": 2.5},
            "cappuccino": {"water": 250, "milk": 100, "coffee": 24, "cost": 3.0},
        }

    def report(self):
        """Print current resources and money"""
        print("Resources:")
        for item, amount in self.resources.items():
            print(f"{item.capitalize()}: {amount}ml")
        print(f"Money: ${self.money:.2f}")

    def is_resource_sufficient(self, drink):
        """Check if resources are enough for the selected drink"""
        for item, required in self.menu[drink].items():
            if item != "cost" and required > self.resources[item]:
                print(f"Sorry, not enough {item}.")
                return False
        return True

    def process_coins(self, drink):
        """Process coins and return True if enough money"""
        cost = self.menu[drink]["cost"]
        print(f"Please insert ${cost} for your {drink}.")
        total = int(input("Quarters: ")) * 0.25
        total += int(input("Dimes: ")) * 0.10
        total += int(input("Nickels: ")) * 0.05
        total += int(input("Pennies: ")) * 0.01
        if total < cost:
            print("Sorry, that's not enough money. Money refunded.")
            return False
        change = round(total - cost, 2)
        if change > 0:
            print(f"Here is ${change} in change.")
        self.money += cost
        return True

    def make_coffee(self, drink):
        """Deduct resources and make coffee"""
        for item in self.menu[drink]:
            if item != "cost":
                self.resources[item] -= self.menu[drink][item]
        print(f"Here is your {drink} ☕️. Enjoy!")

    def run(self):
        """Main loop"""
        is_on = True
        while is_on:
            choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
            if choice == "off":
                print("Turning off...")
                is_on = False
            elif choice == "report":
                self.report()
            elif choice in self.menu:
                if self.is_resource_sufficient(choice) and self.process_coins(choice):
                    self.make_coffee(choice)
            else:
                print("Invalid choice. Try again.")

# Create a CoffeeMachine object
my_machine = CoffeeMachine()
my_machine.run()