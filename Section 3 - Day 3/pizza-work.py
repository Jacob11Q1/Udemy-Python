# Pizza Work Challenge:
print("Welcome to Pizza Deliveries!")
size = input("What pizza size you want? S, M, L: ").upper()
pepperoni = input("Do you want peperoni on your pizza? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()
bill = 0

# Users Size Choice:
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Invalid size selected. Please choose S, M, or L.")
    bill = None  # prevent final bill message if input was invalid

# If They Want Pepperoni Or Not:
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill +=3

# If They Want Cheese Or Not:
if extra_cheese == "Y":
    bill += 1
print(f"Your final bill: ${bill}.")



# Another Example:
# Pizza Work Challenge:
# print("Welcome to Pizza Deliveries!")

# # Get user input
# size = input("What pizza size do you want? S, M, or L: ").upper()
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()

# bill = 0

# # User's size choice
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# elif size == "L":
#     bill += 25
# else:
#     print("Invalid size selected. Please choose S, M, or L.")
#     bill = None

# # If they want pepperoni
# if bill is not None and pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3

# # Final bill
# if bill is not None:
#     print(f"Your final bill: ${bill}.")
