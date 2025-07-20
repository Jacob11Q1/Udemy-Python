# # Rock Paper Scissors Game - Project:

# My Version Of This Code
# print(input("What do you choose? type 0 for Rock, 1 for paper or 2 for Sciccors."))
# rock = 0
# paper = 1
# scissors = 2
# list = [rock , paper , scissors]
# import random
# random_index = random.randint(0,2)

# if random_index == 0:
#     print("The Computer choose Rock")
#     if list == 0:
#         print("It is a draw")
#     elif list == 1:
#         print("You Won")
#     elif list == 2:
#         print("You lost")
#     else:
#         print("Choose a number from the list")

# elif random_index == 1:
#     print("The Computer choose Rock")
#     if list == 0:
#         print("You Lost")
#     elif list == 1:
#         print("It is a draw")
#     elif list == 2:
#         print("You lost")
#     else:
#         print("Choose a number from the list")
        
# elif random_index == 2:
#     print("The Computer choose Scissors")
#     if list == 0:
#         print("You Lost")
#     elif list == 1:
#         print("You Won")
#     elif list == 2:
#         print("It is a draw")
#     else:
#         print("Choose a number from the list")

# else:
#     print("You picked a number from outside the list, So you lost")



# The Refined Version Of This Code
import random

# Game options
rock = "Rock"
paper = "Paper"
scissors = "Scissors"

game_choices = [rock, paper, scissors]

# Ask user for input
user_input = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: ")

# Check if the input is valid (a digit and in range)
if user_input.isdigit() and int(user_input) in [0, 1, 2]:
    user_choice = int(user_input)
    computer_choice = random.randint(0, 2)

    print(f"\nYou chose: {game_choices[user_choice]}")
    print(f"Computer chose: {game_choices[computer_choice]}\n")

    # Determine the result
    if user_choice == computer_choice:
        print("Result: It's a draw!")
    elif (user_choice == 0 and computer_choice == 2) or \
        (user_choice == 1 and computer_choice == 0) or \
        (user_choice == 2 and computer_choice == 1):
        print("Result: You won!")
    else:
        print("Result: You lost!")

else:
    print("Invalid input! Please type 0, 1, or 2.")