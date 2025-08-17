# Challenge: Loop Year:

# Version 1: Clean and concise
def is_leap_year_v1(year):
    if year % 4 != 0:
        return False
    if year % 100 != 0:
        return True
    if year % 400 == 0:
        return True
    return False

# Test multiple years
test_years = [2000, 2100, 2024, 1989, 2400]

for year in test_years:
    print(f"{year}: {is_leap_year_v1(year)}")

print("===== The Second Version =====")
# Version 2: Nested if statements
def is_leap_year_v2(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Test multiple years
test_years = [2000, 2100, 2024, 1989, 2400]

for year in test_years:
    print(f"{year}: {is_leap_year_v2(year)}")