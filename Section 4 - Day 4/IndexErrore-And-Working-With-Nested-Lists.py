# ---------------------------------------------
# Index Errors and Working with Nested Lists
# ---------------------------------------------

# ✅ List of U.S. States (example)
states_of_america = [
    "Delaware",
    "Pennsylvania",
    "New Jersey",
    "Georgia",
    "Connecticut"
]

# ✅ Print the last item using dynamic indexing
num_of_states = len(states_of_america)
print("Last state in the list:", states_of_america[num_of_states - 1])

# ❌ Uncommenting the line below will raise an IndexError:
# print(states_of_america[6])  # IndexError: list index out of range

# ---------------------------------------------
# Dirty Dozen: Nested List Example
# ---------------------------------------------

# ✅ Fruits and Vegetables Lists
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# ✅ Combine into a Nested List
dirty_dozen = [fruits, vegetables]

# ✅ Print the nested list
print("\nDirty Dozen (Nested List):")
print(dirty_dozen)

# ✅ Accessing nested items
print("\nFirst fruit:", dirty_dozen[0][0])        # 'Strawberries'
print("Last vegetable:", dirty_dozen[1][-1])      # 'Potatoes'