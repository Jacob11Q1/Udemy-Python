# ✅ Nesting Lists and Dictionaries

# Simple dictionary
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Example: Nested list
nested_list = ["A", "B", ["C", "D"]]

# Challenge: Print "D" from the nested_list
print("From nested_list:", nested_list[2][1])  # Output: D


# ✅ Nested Dictionary
travel_log = {
    "France": {
        "total_visits": 8,
        "cities_visited": ["Paris", "Lille", "Dijon"]
    },
    "Germany": {
        "total_visits": 5,
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"]
    },
}

# Challenge: Print "Stuttgart" from the travel_log
print("From travel_log:", travel_log["Germany"]["cities_visited"][2])  # Output: Stuttgart