# Exercise: Life in Weeks

# Version 1 - Simple calculation (age in weeks)
def life_in_weeks(age):
    weeks = age * 52  # 52 weeks in a year
    print(f"You have lived for about {weeks} weeks.")

life_in_weeks(90)

# Version 2 - Weeks remaining until age 90
def life_in_weeks(age):
    years_remaining = 90 - age
    weeks_remaining = years_remaining * 52
    print(f"You have {weeks_remaining} weeks left until you turn 90.")

life_in_weeks(12)