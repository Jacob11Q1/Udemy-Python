# File handling in Python using the "with" keyword

# --- 1. Writing to a file (overwrites if exists) ---
with open("my_file.txt", "w") as file:
    file.write("Hello, this is the first line.\n")
    file.write("This is the second line.\n")
print("File written successfully.\n")

# --- 2. Reading the entire file ---
try:
    with open("my_file.txt", "r") as file:
        contents = file.read()
        print("Reading the file:")
        print(contents)
except FileNotFoundError:
    print("The file does not exist yet.\n")

# --- 3. Appending to the file ---
with open("my_file.txt", "a") as file:
    file.write("This line is appended.\n")
print("Line appended successfully.\n")

# --- 4. Reading line by line ---
with open("my_file.txt", "r") as file:
    print("Reading file line by line:")
    for line in file:
        print(line.strip())  # strip removes extra newline characters

# --- 5. Overwriting again ---
with open("my_file.txt", "w") as file:
    file.write("May God Bless You.\n")
print("\nFile overwritten successfully.\n")

# --- 6. Appending again ---
with open("my_file.txt", "a") as file:
    file.write("May God Bless You.\n")
print("Line appended again successfully.\n")

# --- 7. Final read ---
with open("my_file.txt", "r") as file:
    print("Final file content:")
    print(file.read())