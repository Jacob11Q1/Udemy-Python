# Positional vs. Keyword Arguments

# Function with more than one input
def greet_with(name, location):
    print(f"My name is {name}, and I live in {location}")

    # Challenge
    print(f"Hello, {name}")
    print(f"What is it like to live in {location}?")

# Calling the function with positional arguments
greet_with("Jacob", "Palestine")

# Calling the function with keyword arguments
greet_with(location="London", name="Jacob")