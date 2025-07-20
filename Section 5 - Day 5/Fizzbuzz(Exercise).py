# FizzBuzz Exercise

# Challenge:
# Print numbers from 1 to 100.
# - If a number is divisible by 3, print "Fizz"
# - If divisible by 5, print "Buzz"
# - If divisible by both 3 and 5 (i.e. 15), print "FizzBuzz"
# - Otherwise, print the number itself.

for number in range(1, 101):
    if number % 15 == 0:
        print(f"{number}: FizzBuzz")
    elif number % 5 == 0:
        print(f"{number}: Buzz")
    elif number % 3 == 0:
        print(f"{number}: Fizz")
    else:
        print(number)