# 🎲 Random Module Example

# Import the built-in random module
import random

# -----------------------------------------------
# 🔢 Random Float between 0 and 10 using random.random()
# random.random() returns a float between 0.0 and 1.0
# Uncomment below to test:
# random_number_0_to_10 = random.random() * 10
# print("Random float between 0 and 10:", random_number_0_to_10)

# -----------------------------------------------
# 🎯 Random Float between any two values using random.uniform()
# Uncomment below to test:
# random_float = random.uniform(1, 25)
# print("Random float between 1 and 25:", random_float)

# -----------------------------------------------
# 📦 Example (Optional): Using a custom module
# Make sure my_module.py exists in the same folder
# import my_module
# print("My favourite number from my_module:", my_module.my_favourite_number)

# -----------------------------------------------
# 🪙 Example 1: Print Heads or Tails based on a random number (1–10)
random_num = random.randint(1, 10)
if random_num >= 5:
    print(f"Random number: {random_num}")
    print("Heads")
else:
    print(f"Random number: {random_num}")
    print("Tails")

# -----------------------------------------------
# 🪙 Example 2: True coin toss using 0 or 1
random_coin = random.randint(0, 1)
if random_coin == 1:
    print(f"Random coin toss: {random_coin}")
    print("Heads")
else:
    print(f"Random coin toss: {random_coin}")
    print("Tails")

# -----------------------------------------------
# 🪙 Example 3: Even simpler coin toss using random.choice()
print("Coin toss using random.choice():", random.choice(["Heads", "Tails"]))

# -----------------------------------------------
# 📘 What is a Module?
# A module is a way to split your code into separate files.
# Each file (module) contains specific functionality,
# helping you organize, reuse, and manage your program better.