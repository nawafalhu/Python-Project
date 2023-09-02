# User input
height = float(input("Enter your height in m "))
age = int(input("What is your age? "))
photo = input("Do you want a photo? Y, N ")


bill = 0
if height > 1.20 : 
    if age < 12 : 
        bill += 5
    elif age >= 12 and age < 18 :
        bill += 7
    elif age >= 18 : 
        bill += 12
    elif age >= 45 and age <= 55 :
        bill += 0
    if photo == "Y" : 
        bill += 3
    else : 
        print(f"Your bill is {bill}")
else :
    print('Sorry. you can\'t ride')
