# -----------------------------------------------
# List Fundamentals: Indexing, Appending, Extending
# -----------------------------------------------

# 📌 Lists are Data Structures used to store multiple items.

# ✅ Example 1: Fruits List
fruits = ["Cherry", "Apples", "Pear"]
fruits.append("Orange")  # Add 'Orange' to the end
print("Fruits List:", fruits)  # Output: ['Cherry', 'Apples', 'Pear', 'Orange']

# ✅ Example 2: US States List (demo with a few states)
states_of_america = [
    "Delaware",
    "Pennsylvania",
    "New Jersey",
    "Georgia",
    "Connecticut"
]

# -----------------------------------------------
# List Access (Offset / Indexing)
# -----------------------------------------------
print("\nFirst state:", states_of_america[0])        # Index 0
print("Last 5 states:", states_of_america[-5:])      # Slice all (since list has 5)
print("Last state:", states_of_america[-1])          # Negative index for last item

# -----------------------------------------------
# List Modifications
# -----------------------------------------------

# Change a state name (simulate a typo)
states_of_america[1] = "Pencilvania"

# Append a single new item
states_of_america.append("Illinois")

# Extend list with multiple new items
states_of_america.extend([
    "JacobsLand",
    "Mansory",
    "Benz",
    "Yamaha R1",
    "Kawasaki H2R"
])

# Insert an item at a specific position (index 1)
states_of_america.insert(1, "Hawaii")

# -----------------------------------------------
# Print Final List + Length
# -----------------------------------------------
print("\nFull List of States:")
print(states_of_america)

print("\nTotal states in the list:", len(states_of_america))

# -----------------------------------------------
# Remove an item from the list
# -----------------------------------------------
states_of_america.remove("Benz")  # Remove specific item
print("\nList after removing 'Benz':")
print(states_of_america)