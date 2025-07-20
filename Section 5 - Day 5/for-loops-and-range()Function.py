# For Loops and the range() Function:

for number in range(1, 10):
    print(f"Number from 1 to 9: {number}")

for number in range(1, 11):
    print(f"Number from 1 to 10: {number}")

for number in range(1, 11, 3):
    print(f"Number from 1 to 10 with a step of 3: {number}")

total = 0
for number in range(1, 101):
    total += number

print(f"Sum of numbers from 1 to 100: {total}")