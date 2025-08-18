# Number Guessing Project: 


#  _______               ___.                    ________                            .__                
#  \      \  __ __  _____\_ |__   ___________   /  _____/ __ __   ____   ______ _____|__| ____    ____  
#  /   |   \|  |  \/     \| __ \_/ __ \_  __ \ /   \  ___|  |  \_/ __ \ /  ___//  ___/  |/    \  / ___\ 
# /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/ \    \_\  \  |  /\  ___/ \___ \ \___ \|  |   |  \/ /_/  >
# \____|__  /____/|__|_|  /___  /\___  >__|     \______  /____/  \___  >____  >____  >__|___|  /\___  / 
#         \/            \/    \/     \/                \/            \/     \/     \/        \//_____/  



import random

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

def check_answer(guess, answer, attempts):
    """Checks the player's guess against the answer and returns remaining attempts."""
    if guess > answer:
        print("Too high.")
        return attempts - 1
    elif guess < answer:
        print("Too low.")
        return attempts - 1
    else:
        print(f"🎉 You got it! The answer was {answer}.")
        return attempts

def set_difficulty():
    """Returns the number of attempts based on chosen difficulty."""
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_ATTEMPTS
    else:
        return HARD_ATTEMPTS

def game():
    print("\nWelcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    
    attempts = set_difficulty()
    guess = 0

    while guess != answer and attempts > 0:
        print(f"\nYou have {attempts} attempts remaining.")
        guess = int(input("Make a guess: "))
        attempts = check_answer(guess, answer, attempts)
        
        if guess != answer and attempts > 0:
            print("Guess again.")
        
        if attempts == 0 and guess != answer:
            print(f"❌ You've run out of guesses. The number was {answer}.")

def play():
    while True:
        game()
        play_again = input("\nDo you want to play again? Type 'y' or 'n': ").lower()
        if play_again != 'y':
            print("Thanks for playing! Goodbye 👋")
            break

play()