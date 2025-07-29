# Picking A Random Word And Checking Answers:
import random

# To Do Number 1: Choose a word from the word_list
word_list = ["aardvark" , "baboon" , "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

# To Do Number 2: Ask the user to guess a letter
guess = input("Guess a letter: ").lower()
print(guess)

# To Do Number 3: Check if the letter the user guessed is on of the leters
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")