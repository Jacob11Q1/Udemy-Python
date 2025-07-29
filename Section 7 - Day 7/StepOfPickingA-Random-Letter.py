import random

# Expanded word list
word_list = [
    "aardvark", "baboon", "camel", "dolphin", "elephant", "flamingo", "giraffe", "hippopotamus",
    "iguana", "jaguar", "kangaroo", "lemur", "meerkat", "narwhal", "octopus", "penguin", "quokka",
    "raccoon", "sloth", "tortoise", "umbrella", "vulture", "walrus", "xenops", "yak", "zebra",
    "notebook", "keyboard", "pencil", "backpack", "glasses", "airplane", "rainbow", "volcano", "guitar"
]

# Game setup
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

# For debugging (can remove later)
print(f"Pssst... the chosen word is: {chosen_word}")

# Display as a list of underscores
display = ["_" for _ in chosen_word]
guessed_letters = []

# Game loop
game_over = False
while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try another letter.")
        continue
    guessed_letters.append(guess)

    # Correct guess
    if guess in chosen_word:
        for position in range(word_length):
            if chosen_word[position] == guess:
                display[position] = guess
    else:
        lives -= 1
        print(f"Wrong! You have {lives} lives left.")
        if lives == 0:
            game_over = True
            print(f"You Lose. The word was '{chosen_word}'.")

    # Show progress
    print(" ".join(display))

    # Win condition
    if "_" not in display:
        game_over = True
        print("🎉 You Win!")