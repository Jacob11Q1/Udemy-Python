# Coding Exercise: Love Calculator:

# Love Calculator Function
def calculate_love_score(name1, name2):
    # Combine both names into one string and convert to lowercase
    combined_names = (name1 + name2).lower()

    # Count letters for "TRUE"
    t = combined_names.count("t")
    r = combined_names.count("r")
    u = combined_names.count("u")
    e = combined_names.count("e")
    true_score = t + r + u + e

    # Count letters for "LOVE"
    l = combined_names.count("l")
    o = combined_names.count("o")
    v = combined_names.count("v")
    e = combined_names.count("e")  # Count again for "LOVE"
    love_score = l + o + v + e

    # Combine the two scores to form the final score
    final_score = int(str(true_score) + str(love_score))

    print(f"Love Score = {final_score}")

# Example Usage:
calculate_love_score("Kanye West", "Kim Kardashian")  # Expected output: 42