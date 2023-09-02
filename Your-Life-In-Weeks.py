# User age 
Age = int(input("what is your current age?\n"))

# calculation the months, weeks, days and hours 
Months = Age * 12
Weeks = Age * 52
days = Age * 365
hours = days * 24

# print the result
massege = f"{Months} Months, {Weeks} Weeks, {days} days, {hours} hour"
print(massege)