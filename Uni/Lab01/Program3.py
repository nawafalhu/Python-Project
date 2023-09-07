amount = float(input("Enter the amount of purchase:\n"))

Tax = amount * 0.15 
total = Tax + amount
 
print(f"Total purchase = {amount} SR")
print(f"Sales tax = {Tax} SR")
print(f"Total = {total} SR")