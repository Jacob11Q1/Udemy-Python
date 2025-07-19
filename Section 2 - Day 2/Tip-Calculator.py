print("Welcome To The Tip Calculator!")
bill = input("What was the total bill? $")
tip = int(input("what percentage tip would you like to give? 10 12 15"))
people = int(input("How many people to split the bill? "))
bill_with_tip = tip / 100 * bill + bill
print(bill_with_tip)
