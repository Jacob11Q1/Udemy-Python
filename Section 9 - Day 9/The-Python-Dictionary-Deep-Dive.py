# The Python Dictionary: Deep Dive

# Define a programming dictionary
programming_dictionary = {
    "Bug": "An error in a program that prevents it from running as expected.",
    "Function": "A block of reusable code that can be called multiple times.",
    "Loop": "The action of doing something repeatedly."
}

# --- Retrieve an item from the dictionary by its key ---
print("Bug:", programming_dictionary["Bug"])

# --- Update the value of an existing key ---
programming_dictionary["Loop"] = "Repeating an action until a condition is met."
print("\nUpdated Dictionary:", programming_dictionary)

# --- Create an empty dictionary ---
empty_dictionary = {}
print("\nEmpty Dictionary:", empty_dictionary)

# --- Edit an item in a dictionary ---
programming_dictionary["Bug"] = "A small insect... or an error in your code!"
print("\nEdited Dictionary:", programming_dictionary)

# --- Loop through dictionary (keys only) ---
print("\nKeys in dictionary:")
for key in programming_dictionary:
    print(key)

# --- Loop through dictionary (keys & values) ---
print("\nKeys and Values in dictionary:")
for key, value in programming_dictionary.items():
    print(f"{key}: {value}")