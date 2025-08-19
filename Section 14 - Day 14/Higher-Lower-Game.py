# Higher / Lower Project Game:

#   ___ ___ .__       .__                   .____                               
#  /   |   \|__| ____ |  |__   ___________  |    |    ______  _  __ ___________ 
# /    ~    \  |/ ___\|  |  \_/ __ \_  __ \ |    |   /  _ \ \/ \/ // __ \_  __ \
# \    Y    /  / /_/  >   Y  \  ___/|  | \/ |    |__(  <_> )     /\  ___/|  | \/
#  \___|_  /|__\___  /|___|  /\___  >__|    |_______ \____/ \/\_/  \___  >__|   
#        \/   /_____/      \/     \/                \/                 \/       


import random

def higher_lower_game():
    print("Welcome to the Higher-Lower Game!")
    score = 0
    current_number = random.randint(1 , 100)
    
    while True:
        print(f"\nCurrent number: {current_number}")
        choice = input("Will the next number be Higher (H) or Lower (L)? ").strip().lower()
        
        if choice not in ["h" , "l"]:
            print("Invalid choice. Please enter 'H' for higher or 'L' for lower")
            continue
        
        next_number = random.randint(1, 100)
        print(f"The next number is: {next_number}")
        
        if (choice == "h" and next_number > current_number) or (choice == "l" and next_number > current_number):
            print("Correct! 🎉")
            score += 1
        else:
            print("Wrong! ❌")
            break
        
        current_number = next_number
    
    print(f"\nGame Over! Your final score is: {score}")

higher_lower_game()