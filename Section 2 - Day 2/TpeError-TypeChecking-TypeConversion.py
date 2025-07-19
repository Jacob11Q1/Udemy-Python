# Type Error / Type Checking / Type Conversion

# The len will return the number of item in an objects not nuumbers
# print(len(123456)) # Output: Error we have to change it to string

print(type("Hello")) # Outpot: <class 'str'>
print(type(1235)) # Outpot: <class 'int'>
print(type(True)) # Outpot: <class 'bool'>
print(type(30.145)) # Outpot: <class 'float'>

# Type Conversion:
print(int("123") + int("456")) # Outpot: 579

# Exercise:
print("Number of letters in your name: " + str("Jacob Qumsiyeh"))