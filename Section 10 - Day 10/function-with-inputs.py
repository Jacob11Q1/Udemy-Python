# Functions With Inputs:

# Function to multiply two numbers
def multiply(a, b):
    return a * b

print(multiply(3, 2))  # Output: 6


# Function to format a full name (handles extra spaces)
def format_name(first_name, last_name):
    return f"{first_name.strip().title()} {last_name.strip().title()}"

print(format_name("JaCoB", "QuMsIyEh"))  # Output: Jacob Qumsiyeh


# Function to get the length of a string
def string_length(text):
    return len(text)

print(string_length("Angela"))  # Output: 6


# Function to duplicate a string
def duplicate_text(text):
    return text + text


# Function to capitalize the first letter of each word
def title_text(text):
    return text.title()


# Combining duplication and title formatting
def duplicate_and_title(text):
    return title_text(duplicate_text(text))

print(duplicate_and_title("Hello"))  # Output: Hellohello
