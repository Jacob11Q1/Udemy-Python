# How To Add Python Packages And Use PyPi

from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Name" , "Age"]
table.add_row(["Yacoub" , 29])
table.add_row(["Alice" , 30])
print(table)