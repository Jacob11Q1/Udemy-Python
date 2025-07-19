# BMI Calculator With Interpretations:

weight = 95
height = 185
height_m = height / 100 # convert cm to meters

bmi = weight / (height_m ** 2)
print(f"Your BMI is: {bmi:.2f}") # prints BMI rounded to 2 decimals

if bmi >= 30:
    print("Obese")
elif bmi >= 25:
    print("Overweight")
elif bmi >= 18.5:
    print("Normal Weight")
else:
    print("Underweight")