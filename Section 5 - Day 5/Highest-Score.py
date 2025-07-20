# Highest Score:

# A giant list of student scores:
student_scores = [
    150, 142, 185, 120, 171, 184, 149, 24, 59, 68,
    199, 78, 65, 89, 86, 55, 91, 64, 89
]

# Example 1: Using Python's built-in sum function
total_exam_score = sum(student_scores)
print(f"Total Exam Score (using built-in sum): {total_exam_score}")

# Example 2: Calculating the sum using a loop (primitive way)
total = 0
for score in student_scores:
    total += score
print(f"The Sum Of Students Score Is: {total}")

# Example 3: Finding the highest score using a for loop
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The Highest Score Is: {highest_score}")


# Challenge 1:
students = [
    {"name": "Ali", "score": 91},
    {"name": "Lina", "score": 88},
    {"name": "Tariq", "score": 95},
    {"name": "Sami", "score": 78},
    {"name": "Noor", "score": 85}
]

# Initialize tracking variables
highest_score = 0
top_student = ""
total_score = 0

# Loop through students to find highest and calculate total
for student in students:
    score = student["score"]
    total_score += score

    if score > highest_score:
        highest_score = score
        top_student = student["name"]

# Calculate average
average_score = total_score / len(students)

# Output results
print(f"The student with the highest score is: {top_student} ({highest_score})")
print(f"The average score is: {average_score}")


# Challenge 2:
students1 = [
    {"name": "Yasmine", "score": 92},
    {"name": "Omar", "score": 76},
    {"name": "Farah", "score": 89},
    {"name": "Rami", "score": 83},
    {"name": "Dana", "score": 90}
]

# Counter for students scoring above 85
students_above_85 = 0

# Loop through each student
for student in students1:
    if student["score"] > 85:
        students_above_85 += 1

# Print result once
print(f"Number of students who scored above 85: {students_above_85}")


# Challenge 3:
students3 = [
    {"name": "Leen", "score": 70},
    {"name": "Hassan", "score": 82},
    {"name": "Maya", "score": 90},
    {"name": "Khaled", "score": 63},
    {"name": "Nada", "score": 77}
]

print("Students who passed the exam:")

for student in students3:
    if student["score"] >= 75:
        print(student["name"])


# Challenge 4:
students4 = [
    {"name": "Salma", "score": 45},
    {"name": "Zain", "score": 74},
    {"name": "Firas", "score": 58},
    {"name": "Raya", "score": 91},
    {"name": "Adnan", "score": 33}
]

failed_students = 0

for student in students4:
    if student["score"] < 60:
        failed_students += 1

print(f"Number of students who failed the exam: {failed_students}")


# Challenge 5:
students5 = [
    {"name": "Rasha", "score": 52},
    {"name": "Omar", "score": 67},
    {"name": "Nour", "score": 45},
    {"name": "Tarek", "score": 73},
    {"name": "Lina", "score": 38}
]

print("Students who failed the exam:")

for student in students5:
    if student["score"] < 60:
        print(student["name"])


# My Way (commented out - needs fixing):
# student_highest = 0
# for highest in students:
#     if highest > student_highest:
#         student_highest = highest
# print(f"The student with the highest score is: {students(__name__)} {student_highest}")

# average = 0
# for avg in students:
#     average /= students
# print(f"The average score is: {average}")