# Nested (IF) Statements And (ELIF) Statements:

height = 180
age = 19

if height > 120:
    print("You can ride")
    
    if age < 12: # Nested IF Statement inside the original IF Statement
        print("You have to pay $5")
    elif age <= 12 and age <= 18:
        print("You have to pay $7")
    else:
        print("You have to pay $12")

else:
    print("Sorry, your height is less than 120 cm")