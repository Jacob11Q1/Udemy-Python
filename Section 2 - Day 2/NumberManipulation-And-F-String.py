height = 1.77
weight = 94
bmi = weight / height ** 2
print(bmi) # Output: 30.00414951003862
print(int(bmi)) # Output: 30
print(round(bmi)) # Output: 30
print(round(bmi, 2)) # OutPut: 30.0

# Assigmnent Operator: += / -= / *= / /+
score = 0
score += 1
print(score)


# F-Strings:
print(f"Your score Is: {score}, Your Height is: {height}, And Your BMI Is: {bmi}")
