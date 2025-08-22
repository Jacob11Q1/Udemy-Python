# How To Create Your Ownn OOP Class In Python:

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        print(f"New user created: {self.username}")
    
    def follow(self, user):
        user.followers += 1
        self.following += 1

# Creating users
user_1 = User("001", "Angela")
user_2 = User("002", "Yacoub")

# User actions
user_1.follow(user_2)

# Display results
print(f"{user_1.username} - Followers: {user_1.followers}, Following: {user_1.following}")
print(f"{user_2.username} - Followers: {user_2.followers}, Following: {user_2.following}")