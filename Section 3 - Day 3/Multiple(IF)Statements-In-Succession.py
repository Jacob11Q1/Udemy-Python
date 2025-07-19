# Multiple (IF) Statements In Succession:

height = int(input("What is your height in CM?: "))
age = int(input("What is your Age?: "))
bill = 0

if height > 120:
    print("You can ride")
    
    if age < 12: # Nested IF Statement inside the original IF Statement
        bill = 5
        print("Child tickets are $5")
    elif age <= 12 and age <= 18:
        bill = 7
        print("Youth tickets are $7")
    else:
        bill = 12
        print("Adults tickets are $12")
    
    wants_photo = input("Do you want a photo take? Type y for Yes and n for No:")
    if wants_photo.lower() == "y": # Add $3 to the bill
        bill += 3
    print(f"Your final bill is: {bill}")
    
else:
    print("Sorry, your height is less than 120 cm")
