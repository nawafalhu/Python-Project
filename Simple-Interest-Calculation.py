amount = float(input("Enter the amount : "))
interestRate = int(input("Enter the interest rate : "))
year = int(input("Enter the year : "))

interest = round(amount * (interestRate / 100) * year, 2)

print("the interest is ", interest)