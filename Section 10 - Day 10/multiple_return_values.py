# Multiple Return Values:

# Function to format a full name
def format_name(f_name, l_name):
    # Handle empty input
    if not f_name or not l_name:
        return "Error: Both first and last names must be provided."
    
    return f"{f_name.strip().title()} {l_name.strip().title()}"

# Ask user for input
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")

# Print the formatted full name
print(format_name(first_name, last_name))