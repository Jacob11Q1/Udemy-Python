# # Calculator Project:

import math

# Calculator functions
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return "Error: Cannot divide by zero!" if b == 0 else a / b
def power(a, b): return a ** b
def sqrt(a): return "Error: Cannot take sqrt of negative number!" if a < 0 else math.sqrt(a)

operations = {
    "1": ("Add", add),
    "2": ("Subtract", subtract),
    "3": ("Multiply", multiply),
    "4": ("Divide", divide),
    "5": ("Power", power),
    "6": ("Square Root", sqrt)
}

def calculator():
    print("Welcome to the Pro Python Calculator!")

    result = None
    while True:
        print("\nSelect operation:")
        for key, value in operations.items():
            print(f"{key}. {value[0]}")
        print("q. Quit")

        choice = input("Enter choice: ").lower()
        if choice == 'q':
            print("Goodbye!")
            break
        if choice not in operations:
            print("Invalid input, try again.")
            continue

        if choice == "6":
            num = float(input("Enter number: ")) if result is None else result
            result = sqrt(num)
        else:
            num1 = float(input("Enter first number: ")) if result is None else result
            num2 = float(input("Enter second number: "))
            result = operations[choice][1](num1, num2)

        print(f"Result: {result}")

        cont = input("Continue with this result? (y/n): ").lower()
        if cont != "y":
            result = None

calculator()






# # Simple Calculator

# # Define functions for each operation
# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     if b == 0:
#         return "Error: Cannot divide by zero!"
#     return a / b

# # Main program
# print("Welcome to Python Calculator!")
# print("Select operation:")
# print("1. Add (+)")
# print("2. Subtract (-)")
# print("3. Multiply (*)")
# print("4. Divide (/)")

# # Take user input
# choice = input("Enter choice (1/2/3/4): ")

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# # Perform calculation
# if choice == "1":
#     print(f"{num1} + {num2} = {add(num1, num2)}")
# elif choice == "2":
#     print(f"{num1} - {num2} = {subtract(num1, num2)}")
# elif choice == "3":
#     print(f"{num1} * {num2} = {multiply(num1, num2)}")
# elif choice == "4":
#     print(f"{num1} / {num2} = {divide(num1, num2)}")
# else:
#     print("Invalid input")

# # Another Version But Modified Calculator:

# import math

# # Calculator functions
# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     if b == 0:
#         return "Error: Cannot divide by zero!"
#     return a / b

# def power(a, b):
#     return a ** b

# def sqrt(a):
#     if a < 0:
#         return "Error: Cannot take square root of negative number!"
#     return math.sqrt(a)

# # Dictionary to map user choice to function
# operations = {
#     "1": ("Add", add),
#     "2": ("Subtract", subtract),
#     "3": ("Multiply", multiply),
#     "4": ("Divide", divide),
#     "5": ("Power", power),
#     "6": ("Square Root", sqrt)
# }

# def calculator():
#     print("Welcome to the Pro Python Calculator!")
    
#     while True:
#         print("\nSelect operation:")
#         for key, value in operations.items():
#             print(f"{key}. {value[0]}")

#         choice = input("Enter choice (or 'q' to quit): ").lower()
#         if choice == 'q':
#             print("Goodbye!")
#             break

#         if choice not in operations:
#             print("Invalid input, try again.")
#             continue

#         # Get numbers from user
#         if choice == "6":  # Square root only needs one number
#             num = float(input("Enter number: "))
#             result = sqrt(num)
#         else:
#             num1 = float(input("Enter first number: "))
#             num2 = float(input("Enter second number: "))
#             result = operations[choice][1](num1, num2)

#         print(f"Result: {result}")

#         # Ask if user wants to continue with result
#         cont = input("Do you want to continue with this result? (y/n): ").lower()
#         if cont == "y" and choice != "6":
#             num1 = result
#             num2 = float(input("Enter next number: "))
#             result = operations[choice][1](num1, num2)
#             print(f"New Result: {result}")

# # Run the calculator
# calculator()