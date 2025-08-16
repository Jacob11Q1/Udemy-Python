# Exercise: Grading Program:

students_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}

# Create an empty dictionary to store results:
students_grades = {}

# Loop through student_scores and assign grades:
for student, score in students_scores.items():
    if score >= 91:
        students_grades[student] = "Outstanding"
    elif score >= 81:
        students_grades[student] = "Exceeds Expectations"
    elif score >= 71:
        students_grades[student] = "Acceptable"
    else:
        students_grades[student] = "Fail"

# Print the final dictionary:
print(students_grades)