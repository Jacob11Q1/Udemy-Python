# Who Will Pay The Bill:
import random

# List of friends
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# ----------------------------------------------
# Example 1: Random selection with "split the bill" option
# ----------------------------------------------
# Generate a random index from 0 to length of friends - 1
random_index = random.randint(0, len(friends) - 1)

# If the random index is 0, everyone splits the bill
# Otherwise, the friend at the random index pays
if random_index == 0:
    print("Everyone will split the bill.")
else:
    print(f"The one who will pay is: {friends[random_index]}")

# ----------------------------------------------
# Example 2: Using random.choice() for simpler random selection
# ----------------------------------------------
random_friend = random.choice(friends)
print(f"The one who will pay is: {random_friend}")

# ----------------------------------------------
# Example 3: Random index selection with fixed range
# ----------------------------------------------
random_index_fixed = random.randint(0, 4)  # 0 to 4 for 5 friends
print(f"The one who will pay is: {friends[random_index_fixed]}")