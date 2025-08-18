# Does Python Have Block Scope?:

game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

def create_enemy():
    new_enemy = ""
    if game_level < 5:   # This "if" block does NOT create a new scope
        new_enemy = enemies[0]

    print(new_enemy)

create_enemy()
