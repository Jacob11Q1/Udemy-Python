# NameSpaces: Local VS. Global Scope:

# Global Scope:
enemies = 1   # Global variable
def increase_enemies():
    enemies = 2   # Local variable (only exists inside this function)
    print(f"enemies inside function: {enemies}")  # Output: 2

increase_enemies()
print(f"enemies outside function: {enemies}")     # Output: 1


# Local Scope:
def drink_potion():
    potion_strength = 2  # Local variable
    print(f"Potion Strength: {potion_strength}")

drink_potion()       # Output: Potion Strength: 2

# print(potion_strength)  
# ❌ NameError: 'potion_strength' is not defined

# Global Scope:
player_health = 10   # Global variable

def game():
    def drink_potion():
        potion_strength = 2   # Local variable
        print(f"Potion Strength: {potion_strength}")
    
    drink_potion()
    print(player_health)   # Accessing global variable

game()