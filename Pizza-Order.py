# the menu
print("Small Pizza: $15\nMedium Pizza: $20\nLarge Pizza: $25\n\nPepperoni for Small Pizza: +$2\nPepperoni for Medium or Large Pizza: +$3\nExtra cheese for any size pizza: + $1")

# user input 
size = input("What size pizza do you want? S, M, or L ").capitalize()
pep = input("Do you want pepperoni? Y or N ").capitalize()
chees = input("Do you want extra cheese? Y or N ").capitalize()

# the total bill
total = 0

# size of pizza
if size == "S" : 
    total += 15
elif size == "M" :
    total += 20
elif size == "L" :
    total += 25
else : 
    print("wrong choice! Try again")

# pepperoni 
if pep == "Y" and size == "S":
    total += 2
elif pep == "Y" and size == "M" or size == "L":
    total += 3
elif pep != "N" :
    print("wrong choice! Try again")

# Extra chees
if chees == "Y" :
    total += 1
elif chees != "N" :
    print("wrong choice! Try again")
# print the total number
print(f"The total bill is {total}")
